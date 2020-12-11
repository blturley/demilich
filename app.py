"""Flask app for Demilich"""

from flask import Flask, request, redirect, render_template, flash, jsonify, session, g
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Character, Ability, Weapon, Item
from forms import AddUserForm, LoginUserForm, AddCharacterForm, AddAbilityForm, AddWeaponForm, AddItemForm, EditWeaponForm, EditItemForm, KillCharacterForm
from sqlalchemy.exc import IntegrityError
import random
import copy
import requests
import os

CURR_USER_KEY = "curr_user"

app = Flask(__name__, static_folder="static")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql:///demilich')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.debug = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'noneofyourbeeswax')

toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)


#############################################################################


@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


#############################################################################


@app.route("/")
def home_page():
    """Render main page."""

    if not g.user:
        return redirect("/login")

    characters = g.user.characters

    form1 = AddCharacterForm() 
    form2 = AddAbilityForm()
    form3 = AddWeaponForm ()
    form4 = AddItemForm()

    weapons = requests.get('https://www.dnd5eapi.co/api/equipment-categories/weapon')
    armor = requests.get('https://www.dnd5eapi.co/api/equipment-categories/armor')
    gear = requests.get('https://www.dnd5eapi.co/api/equipment-categories/standard-gear')
    symbols = requests.get('https://www.dnd5eapi.co/api/equipment-categories/holy-symbols')
    tools = requests.get('https://www.dnd5eapi.co/api/equipment-categories/tools')
    spells = requests.get('https://www.dnd5eapi.co/api/spells')
    skills = requests.get('https://www.dnd5eapi.co/api/skills')

    weapons_json = weapons.json()
    armor_json = armor.json()
    gear_json = gear.json()
    symbols_json = symbols.json()
    tools_json = tools.json()
    spells_json = spells.json()
    skills_json = skills.json()

    randnum = random.randint(1, 5000)

    return render_template("home.html", form1=form1, form2=form2, form3=form3, form4=form4, characters=characters,
                        weapons=weapons_json, armor=armor_json, gear=gear_json, symbols=symbols_json, tools=tools_json,
                        spells=spells_json, skills=skills_json, randnum=randnum)


@app.route("/signup", methods=["GET", "POST"])
def user_register():
    """Register new user."""

    form = AddUserForm()

    if form.validate_on_submit():
        try:
            new_user = User.signup(
                username=form.username.data,
                password=form.password.data,
                email=form.email.data,
            )
            db.session.commit()

        except IntegrityError:
            db.session.rollback()
            if User.query.filter_by(username=form.username.data).first():
                form.username.errors = ['Username taken']
            if User.query.filter_by(email=form.email.data).first():
                form.email.errors = ['Email taken']
            return render_template('signup.html', form=form)
        
        db.session.commit()

        session[CURR_USER_KEY] = new_user.id

        return redirect('/')

    return render_template('signup.html', form=form)


@app.route("/login", methods=["GET", "POST"])
def user_login():
    """Login user."""

    form = LoginUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user = User.authenticate(username, password)

        if user:
            session[CURR_USER_KEY] = user.id
            return redirect('/')
        else:
            form.username.errors = ['Invalid username or password']

    return render_template('login.html', form=form)


@app.route("/logout", methods=["POST"])
def logout_user():
    """Logout user."""
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
    return redirect("/login")


@app.route("/about")
def show_about_page():
    """Show about page."""
    
    return render_template('about.html')


@app.route("/character/<int:char_id>", methods=["GET"])
def get_character_info(char_id):
    """get info for current character."""

    character = Character.query.get_or_404(char_id)
    char_abilities = {}
    char_weapons = {}
    char_items = {}

    for val in character.abilities:
        char_abilities[val.name] = {"name": val.name, "id": val.id}

    for val in character.weapons:
        char_weapons[val.name] = {"name": val.name, "id": val.id, "is_equipped": val.is_equipped}

    for val in character.items:
        char_items[val.name] = {"name": val.name, "id": val.id, "is_equipped": val.is_equipped}

    resp = {
        "character": character.serialize(),
        "abilities": char_abilities,
        "weapons": char_weapons,
        "items": char_items,
    }

    response_json = jsonify(resp)
    return (response_json, 200)


@app.route("/ability/<int:ability_id>", methods=["GET"])
def get_ability_html(ability_id):
    """get html for current ability."""

    ability = Ability.query.get_or_404(ability_id)

    response_json = jsonify(render_template('abilitydetails.html', ability=ability, characters=g.user.characters))
    return (response_json, 200)


@app.route("/weapon/<int:weapon_id>", methods=["GET"])
def get_weapon_html(weapon_id):
    """get html for current weapon."""

    weapon = Weapon.query.get_or_404(weapon_id)

    response_json = jsonify(render_template('weapondetails.html', weapon=weapon, characters=g.user.characters))
    return (response_json, 200)


@app.route("/item/<int:item_id>", methods=["GET"])
def get_item_html(item_id):
    """get html for current item."""

    item = Item.query.get_or_404(item_id)

    response_json = jsonify(render_template('itemdetails.html', item=item, characters=g.user.characters))
    return (response_json, 200)


@app.route("/geteditcharacter/<int:char_id>", methods=["GET"])
def get_edit_character(char_id):
    """get html for edit character form."""

    character = Character.query.get_or_404(char_id)

    form = AddCharacterForm(obj=character)

    response_json = jsonify(render_template('editcharacter.html', form=form, character=character))
    return (response_json, 200)


@app.route("/geteditability/<int:ability_id>", methods=["GET"])
def get_edit_ability(ability_id):
    """get html for edit ability form."""

    ability = Ability.query.get_or_404(ability_id)

    form=AddAbilityForm(obj=ability)

    response_json = jsonify(render_template('editability.html', form=form, ability=ability))
    return (response_json, 200)


@app.route("/geteditweapon/<int:weapon_id>", methods=["GET"])
def get_edit_weapon(weapon_id):
    """get html for edit weapon form."""

    weapon = Weapon.query.get_or_404(weapon_id)

    form=EditWeaponForm(obj=weapon)

    response_json = jsonify(render_template('editweapon.html', form=form, weapon=weapon))
    return (response_json, 200)


@app.route("/getedititem/<int:item_id>", methods=["GET"])
def get_edit_item(item_id):
    """get html for edit item form."""

    item = Item.query.get_or_404(item_id)

    form=EditItemForm(obj=item)

    response_json = jsonify(render_template('edititem.html', form=form, item=item))
    return (response_json, 200)


@app.route("/newcharacter", methods=['POST'])
def process_new_character_form():
    """Add new character to database."""
    form = AddCharacterForm()
    if form.validate_on_submit():

        stats = form.stats.data
        prof = form.proficiencies.data
        statuses = form.statuses.data
        lang = form.languages.data
        hires = form.hirelings.data
        pets = form.pets_minions.data

        new_stats = stats.replace(",", "<br>")
        new_prof = prof.replace(",", "<br>")
        new_statuses = statuses.replace(",", "<br>")
        new_lang = lang.replace(",", "<br>")
        new_hires = hires.replace(",", "<br>")
        new_pets = pets.replace(",", "<br>")

        new_char = Character(
                name = form.name.data,
                portrait_url = form.portrait_url.data,
                icon = form.icon.data,
                class_name = form.class_name.data,
                race = form.race.data,
                level = form.level.data,
                stats = new_stats,
                alignment = form.alignment.data,
                proficiencies = new_prof,
                statuses = new_statuses,
                age = form.age.data,
                backstory = form.backstory.data,
                languages = new_lang,
                notes = form.notes.data,
                hirelings = new_hires,
                pets_minions = new_pets,
                user_id = g.user.id)

        db.session.add(new_char)

        db.session.commit()

        serial_char = new_char.serialize()

        return (jsonify(serial_char), 200)

    errors = {"errors":form.errors}
    return jsonify(errors)


@app.route("/newability/<int:char_id>", methods=['POST'])
def process_new_ability_form(char_id):
    """Add new ability to database."""
    form = AddAbilityForm()
    if form.validate_on_submit():

        new_ability = Ability(
                name = form.name.data,
                image_url = form.image_url.data,
                damage = form.damage.data,
                damage_type = form.damage_type.data,
                description = form.description.data,
                ability_range = form.ability_range.data,
                effect_area = form.effect_area.data,
                min_level = form.min_level.data,
                is_spell = form.is_spell.data,
                school = form.school.data,
                notes = form.notes.data,
                character_id = char_id)

        db.session.add(new_ability)

        db.session.commit()

        serial_ability = new_ability.serialize()

        return (jsonify(serial_ability), 200)

    errors = {"errors":form.errors}
    return jsonify(errors)


@app.route("/newweapon/<int:char_id>", methods=['POST'])
def process_new_weapon_form(char_id):
    """Add new weapon to database."""

    form = AddWeaponForm()
    if form.validate_on_submit():
        new_weapon = Weapon(
                name = form.name.data,
                image_url = form.image_url.data,
                weapon_type = form.weapon_type.data,
                damage = form.damage.data,
                damage_type = form.damage_type.data,
                weapon_range = form.weapon_range.data,
                description = form.description.data,
                weight = form.weight.data,
                condition = form.condition.data,
                rarity = form.rarity.data,
                notes = form.notes.data,
                is_equipped = form.is_equipped.data,
                character_id = char_id)

        db.session.add(new_weapon)

        db.session.commit()

        serial_weapon = new_weapon.serialize()

        return (jsonify(serial_weapon), 200)

    errors = {"errors":form.errors}
    return jsonify(errors)


@app.route("/newitem/<int:char_id>", methods=['POST'])
def process_new_item_form(char_id):
    """Add new item to database."""

    form = AddItemForm()
    if form.validate_on_submit():
        new_item = Item(
                name = form.name.data,
                image_url = form.image_url.data,
                description = form.description.data,
                weight = form.weight.data,          
                is_wearable = form.is_wearable.data,
                armor_class = form.armor_class.data,
                condition = form.condition.data,
                rarity = form.rarity.data,
                quantity = form.quantity.data,
                notes = form.notes.data,
                is_equipped = form.is_equipped.data,
                character_id = char_id)

        if new_item.is_wearable == False:
            new_item.is_equipped = False

        db.session.add(new_item)

        db.session.commit()

        serial_item = new_item.serialize()

        return (jsonify(serial_item), 200)

    errors = {"errors":form.errors}
    return jsonify(errors)


@app.route("/deletecharacter/<int:char_id>", methods=['DELETE'])
def delete_character(char_id):
    """Delete character from database."""

    character = Character.query.get_or_404(char_id)

    if session[CURR_USER_KEY] == character.user.id:
        db.session.delete(character)
        db.session.commit()

    return jsonify("Character deleted")


@app.route("/deleteability/<int:ability_id>", methods=['DELETE'])
def delete_ability(ability_id):
    """Delete ability from database."""

    ability = Ability.query.get_or_404(ability_id)

    if session[CURR_USER_KEY] == ability.character.user.id:
        db.session.delete(ability)
        db.session.commit()

    return jsonify("Ability deleted")


@app.route("/deleteweapon/<int:weapon_id>", methods=['DELETE'])
def delete_weapon(weapon_id):
    """Delete weapon from database."""

    weapon = Weapon.query.get_or_404(weapon_id)

    if session[CURR_USER_KEY] == weapon.character.user.id:
        db.session.delete(weapon)
        db.session.commit()

    return jsonify("Weapon deleted")


@app.route("/deleteitem/<int:item_id>", methods=['DELETE'])
def delete_item(item_id):
    """Delete item from database."""

    item = Item.query.get_or_404(item_id)

    if session[CURR_USER_KEY] == item.character.user.id:
        db.session.delete(item)
        db.session.commit()

    return jsonify("Item deleted")


@app.route("/editcharacter/<int:char_id>", methods=['PATCH'])
def process_edit_character_form(char_id):
    """Edit character."""

    character = Character.query.get_or_404(char_id)

    form = AddCharacterForm()

    if form.validate_on_submit():

        stats = form.stats.data
        prof = form.proficiencies.data
        statuses = form.statuses.data
        lang = form.languages.data
        hires = form.hirelings.data
        pets = form.pets_minions.data

        new_stats = stats.replace(",", "<br>")
        new_prof = prof.replace(",", "<br>")
        new_statuses = statuses.replace(",", "<br>")
        new_lang = lang.replace(",", "<br>")
        new_hires = hires.replace(",", "<br>")
        new_pets = pets.replace(",", "<br>")

        character.name = form.name.data
        character.portrait_url = form.portrait_url.data
        character.icon = form.icon.data
        character.class_name = form.class_name.data
        character.race = form.race.data
        character.level = form.level.data
        character.stats = new_stats
        character.alignment = form.alignment.data
        character.proficiencies = new_prof
        character.statuses = new_statuses
        character.age = form.age.data
        character.backstory = form.backstory.data
        character.languages = new_lang
        character.notes = form.notes.data
        character.hirelings = new_hires
        character.pets_minions = new_pets

        db.session.commit()

        serial_char = character.serialize()

        return (jsonify(serial_char), 200)

    errors = {"errors":form.errors}
    return jsonify(errors)


@app.route("/editability/<int:ability_id>", methods=['PATCH'])
def process_edit_ability_form(ability_id):
    """Edit ability."""

    ability = Ability.query.get_or_404(ability_id)

    form = AddAbilityForm()

    if form.validate_on_submit():

        ability.name = form.name.data
        ability.image_url = form.image_url.data
        ability.damage = form.damage.data
        ability.damage_type = form.damage_type.data
        ability.description = form.description.data
        ability.ability_range = form.ability_range.data
        ability.effect_area = form.effect_area.data
        ability.min_level = form.min_level.data
        ability.is_spell = form.is_spell.data
        ability.school = form.school.data
        ability.notes = form.notes.data

        db.session.commit()

        serial_ability = ability.serialize()

        return (jsonify(serial_ability), 200)

    errors = {"errors":form.errors}
    return jsonify(errors)


@app.route("/editweapon/<int:weapon_id>", methods=['PATCH'])
def process_edit_weapon_form(weapon_id):
    """Edit weapon."""

    weapon = Weapon.query.get_or_404(weapon_id)

    form = EditWeaponForm()

    if form.validate_on_submit():

        weapon.name = form.name.data
        weapon.image_url = form.image_url.data
        weapon.weapon_type = form.weapon_type.data
        weapon.damage = form.damage.data
        weapon.damage_type = form.damage_type.data
        weapon.weapon_range = form.weapon_range.data
        weapon.description = form.description.data
        weapon.weight = form.weight.data
        weapon.condition = form.condition.data
        weapon.rarity = form.rarity.data
        weapon.notes = form.notes.data

        db.session.commit()

        serial_weapon = weapon.serialize()

        return (jsonify(serial_weapon), 200)

    errors = {"errors":form.errors}
    return jsonify(errors)


@app.route("/edititem/<int:item_id>", methods=['PATCH'])
def process_edit_item_form(item_id):
    """Edit item."""

    item = Item.query.get_or_404(item_id)

    form = EditItemForm()

    if form.validate_on_submit():

        item.name = form.name.data
        item.image_url = form.image_url.data
        item.description = form.description.data
        item.weight = form.weight.data
        item.armor_class = form.armor_class.data
        item.condition = form.condition.data
        item.rarity = form.rarity.data
        item.quantity = form.quantity.data
        item.notes = form.notes.data

        db.session.commit()

        serial_item = item.serialize()

        return (jsonify(serial_item), 200)

    errors = {"errors":form.errors}
    return jsonify(errors)


@app.route("/weaponequip/<int:weapon_id>", methods=['PATCH'])
def process_equip_weapon(weapon_id):
    """Equip weapon."""

    weapon = Weapon.query.get_or_404(weapon_id)

    weapon.is_equipped = True

    db.session.commit()

    serial_weapon = weapon.serialize()

    return (jsonify(serial_weapon), 200)


@app.route("/weaponunequip/<int:weapon_id>", methods=['PATCH'])
def process_unequip_weapon(weapon_id):
    """Unequip weapon."""

    weapon = Weapon.query.get_or_404(weapon_id)

    weapon.is_equipped = False

    db.session.commit()

    serial_weapon = weapon.serialize()

    return (jsonify(serial_weapon), 200)


@app.route("/itemequip/<int:item_id>", methods=['PATCH'])
def process_equip_item(item_id):
    """Equip item."""

    item = Item.query.get_or_404(item_id)

    item.is_equipped = True

    db.session.commit()

    serial_item = item.serialize()

    return (jsonify(serial_item), 200)


@app.route("/itemunequip/<int:item_id>", methods=['PATCH'])
def process_unequip_item(item_id):
    """Unequip item."""

    item = Item.query.get_or_404(item_id)

    item.is_equipped = False

    db.session.commit()

    serial_item = item.serialize()

    return (jsonify(serial_item), 200)


@app.route("/deathform/<int:char_id>/")
def render_kill_form(char_id):
    """Get form to kill character."""

    if not g.user:
        return redirect("/login")

    character = Character.query.get_or_404(char_id)

    if character.user_id != g.user.id:
        return redirect("/logout")
 
    form = KillCharacterForm()

    return render_template("deathform.html", form=form, character=character)


@app.route("/killcharacter/<int:char_id>", methods=['POST'])
def process_kill_char(char_id):
    """Kill character off"""

    if g.user:
        
        character = Character.query.get_or_404(char_id)

        if character.user_id != g.user.id:
            return redirect("/logout")

        abysslayers = [
            "Layer 1: Plain of Infinite Portals", "Layer 2: Driller's Hives", "Layer 3: The Forgotten Land",
            "Layer 4: The Grand Abyss", "Layer 5: Wormblood", "Layer 6: Realm of a Million Eyes",
            "Layer 7: The Phantom Plane", "Layer 8: The Skin-Shedder", "Layer 9: Burningwater",
            "Layer 10: That Hellhole", "Layer 11: Molrat", "Layer 12: Twelvetrees", "Layer 13: Blood Tor",
            "Layer 14: The Steaming Fen", "Layer 17: Death's Reward", "Layer 21: The Sixth Pyre",
            "Layer 23: The Iron Wastes", "Layer 27: Malignebula", "Layer 32: Sholo-Tovoth: The Fields of Consumption",
            "Layers 45–47: Azzagrat", "Layer 48: Skeiqulac, the Ocean of Tears", "Layer 49: Shaddonon",
            "Layer 52: Vorganund", "Layer 53: Phage Breeding Grounds", "Layer 57: Torturous Truth",
            "Layer 65: Court of the Spider Queen", "Layer 66: The Demonweb Pits", "Layer 67: The Heaving Hills",
            "Layer 68: The Swallowed Void", "Layer 69: Gibbering Hollow", "Layer 70: The Ice Floe",
            "Layer 71: Spirac", "Layer 72: Darklight", "Layer 73: The Wells of Darkness", "Layer 74: Smaragd",
            "Layer 77: The Gates of Heaven", "Layer 79: The Emessu Tunnels", "Layer 81: Blood Shallows",
            "Layer 88: Gaping Maw", "Layer 89: The Shadowsea", "Layer 90: The Guttering Grove", "Layer 92: Ulgurshek",
            "Layer 99: Unnamed", "Layer 100: The Barrens", "Layer 111: The Mind of Evil", "Layer 113: Thanatos",
            "Layer 128: Slugbed", "Layer 137: Outcasts' End", "Layer 142: Lifebane", "Layer 148: Torrent",
            "Layer 176: Hollow's Heart", "Layer 177: Writhing Realm", "Layer 181: The Rotting Plain",
            "Layer 191: Fountain of Screams", "Layer 193: Vulgarea", "Layer 222: Shedaklah", "Layer 223: Offalmound",
            "Layer 230: The Dreaming Gulf", "Layer 241: Palpitatia", "Layer 245: The Scalding Sea", "Layer 248: The Hidden Layer",
            "Layer 274: Durao", "Layer 277: Belistor", "Layer 297: The Sighing Cliffs", "Layer 300: Feng-Tu",
            "Layer 303: The Sulfanorum", "Layer 313: Gorrion's Grasp", "Layer 333: The Broken Scale", "Layer 340: The Black Blizzard",
            "Layer 348: Indifference", "Layer 359: The Arc of Eternity", "Layer 377: Plains of Gallenshu",
            "Layer 399: Worm Realm", "Layer 400: Woeful Escarand", "Layer 403: The Rainless Waste", "Layer 421: The White Kingdom",
            "Layer 422: Death Dells", "Layer 423: Galun-Khur", "Layer 444: Unnamed", "Layer 452: Ahriman-abad",
            "Layer 471: Androlynne", "Layer 480: Guttlevetch", "Layer 487: Lair of the Beast and Mansion of the Rake",
            "Layer 489: Noisome Vale", "Layer 493: The Steeping Isle", "Layer 499: Carroristo", "Layer 500: Unnamed",
            "Layer 503: Torremor", "Layer 507: Occipitus", "Layer 518: Melantholep", "Layer 519: March of the Pierced Men",
            "Layer 524: Shatterstone", "Layer 528: Molor", "Layer 531: Vudra", "Layer 548: Garavond", "Layer 550: Forest of Living Tongues",
            "Layer 558: Fleshforges", "Layer 566: Soulfreeze", "Layer 570: Shendilavri", "Layer 586: Prison of the Mad God",
            "Layer 597: Goranthis", "Layer 600: Endless Maze", "Layer 601: Conflagratum", "Layer 628: Vallashan",
            "Layer 643: Caverns of the Skull", "Layer 651: Nethuria", "Layer 652: The Rift of Corrosion", "Layer 663: Zionyn",
            "Layer 665: Unnamed"]

        ran_num = random.randint(0, (len(abysslayers) - 1))

        form = KillCharacterForm()

        if form.validate_on_submit():

            character.cause_of_death = form.cause_of_death.data
            character.eulogy = form.eulogy.data
            character.is_dead = True
            character.abyss_layer = abysslayers[ran_num]
            db.session.commit()
            return redirect("/")

    return redirect("/login")


@app.route("/resurrectform/<int:char_id>/")
def render_res_form(char_id):
    """Get form to resurrect character."""

    if not g.user:
        return redirect("/login")

    character = Character.query.get_or_404(char_id)

    if character.user_id != g.user.id:
        return redirect("/logout")

    return render_template("resurrectform.html", character=character)


@app.route("/resurrectcharacter/<int:char_id>", methods=['POST'])
def process_res_char(char_id):
    """Resurrect character after death."""

    if g.user:
        
        character = Character.query.get_or_404(char_id)

        if character.user_id != g.user.id:
            return redirect("/logout")

        character.cause_of_death = None
        character.eulogy = None
        character.is_dead = False
        character.abyss_layer = None
        db.session.commit()
        return redirect("/")

    return redirect("/login")


@app.route("/copyitem", methods=["GET"])
def copy_item():
    """Copy item to other character."""

    if not g.user:
        return (jsonify("error: login"), 403)

    args = request.args

    charid = args["charid"]
    itemid = args["itemid"]
    itemtype = args["itemtype"]

    item = None
    newitem = None
    
    character = Character.query.get(charid)

    if character.user_id != g.user.id:
        if not g.user:
            return (jsonify("error: login"), 403)
   
    if itemtype == "ability":
        item = Ability.query.get(itemid)
        newitem = Ability(name = item.name,
                          image_url = item.image_url,
                          damage = item.damage,
                          damage_type = item.damage_type,
                          description = item.description,
                          ability_range = item.ability_range,
                          effect_area = item.effect_area,
                          min_level = item.min_level,
                          is_spell = item.is_spell,
                          school = item.school,
                          notes = item.notes,
                          character_id = character.id)
    elif itemtype == "weapon":
        item = Weapon.query.get(itemid)
        newitem = Weapon(name = item.name,
                         image_url = item.image_url,
                         weapon_type = item.weapon_type,
                         damage = item.damage,
                         damage_type = item.damage_type,
                         weapon_range = item.weapon_range,
                         description = item.description,
                         weight = item.weight,
                         condition = item.condition,
                         rarity = item.rarity,
                         notes = item.notes,
                         is_equipped = item.is_equipped,
                         character_id = character.id)
    else:
        item = Item.query.get(itemid)
        newitem = Item(name = item.name,
                          image_url = item.image_url,
                          description = item.description,
                          weight = item.weight,
                          is_wearable = item.is_wearable,
                          armor_class = item.armor_class,
                          condition = item.condition,
                          rarity = item.rarity,
                          quantity = item.quantity,
                          notes = item.notes,
                          is_equipped = item.is_equipped,
                          character_id = character.id)
        
    db.session.add(newitem)
    db.session.commit()

    return (jsonify(newitem.serialize()), 200)


@app.route("/deleteaccount", methods=['POST'])
def delete_user():
    """Delete user account."""

    if not g.user:
        return redirect("/logout")

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

    db.session.delete(g.user)
    db.session.commit()

    return redirect("/login")