from models import db, User, Character, Ability, Weapon, Item
from app import app

db.drop_all()
db.create_all()

User.query.delete()
Character.query.delete()
Ability.query.delete()
Weapon.query.delete()
Item.query.delete()

user1 = User.signup(username="eggman556",
                      email="egghead@email.com", 
                      password="iloveeggs")

db.session.commit()

character1 = Character(name = "Edgar Meloncamp", 
                       portrait_url = "static/portrait01.png", 
                       icon = "static/charactericon01.png", 
                       class_name = "Fighter", 
                       race = "Orc", 
                       level = "12", 
                       stats = "Strength - 20<br>Constitution- 15<br>Dexterity- 17<br>Intelligence- 10<br>Wisdom- 9<br>Charisma- 5", 
                       alignment = "Lawful Neutral", 
                       proficiencies = "Heavy Armor<br>Two handed swords<br>Two handed axes<br>Athletics<br>Intimidation", 
                       statuses = "dysentery", 
                       age = "55", 
                       backstory = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est, distinctio! Deleniti delectus harum blanditiis suscipit dolorem quam officiis id odit, qui alias, corrupti esse dolores libero at culpa itaque eveniet.", 
                       languages = "Orcish<br>Common<br>Goblish", 
                       notes = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est, distinctio! Deleniti delectus harum blanditiis suscipit dolorem quam officiis id odit, qui alias, corrupti esse dolores libero at culpa itaque eveniet.", 
                       is_dead = False,  
                       hirelings = "Mr.Friendly", 
                       pets_minions = "Buhbuh", 
                       user_id = user1.id)

character2 = Character(name = "Mario Macaroni", 
                       portrait_url = "static/portrait02.png", 
                       icon = "static/charactericon04.png", 
                       class_name = "Wizard", 
                       race = "Human", 
                       level = "9", 
                       stats = "Strength - 20<br>Constitution- 15<br>Dexterity- 17<br>Intelligence- 10<br>Wisdom- 9<br>Charisma- 5", 
                       alignment = "Lawful Neutral", 
                       proficiencies = "Light Armor<br>Staff<br>Two handed axes<br>Dagger<br>Destruction<br>Conjuration", 
                       statuses = "dysentery", 
                       age = "55", 
                       backstory = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est, distinctio! Deleniti delectus harum blanditiis suscipit dolorem quam officiis id odit, qui alias, corrupti esse dolores libero at culpa itaque eveniet.", 
                       languages = "Orcish<br>Common<br>Goblish", 
                       notes = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est, distinctio! Deleniti delectus harum blanditiis suscipit dolorem quam officiis id odit, qui alias, corrupti esse dolores libero at culpa itaque eveniet.", 
                       is_dead = False,  
                       hirelings = "Mr.Friendly", 
                       pets_minions = "Buhbuh", 
                       user_id = user1.id)

db.session.add_all([character1, character2])

db.session.commit()

ability1 = Ability(name = "Faerie Fire",
                   image_url = "static/spell01.png",
                   damage = "1D6",
                   damage_type = "fire",
                   description = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est, distinctio! Deleniti delectus harum blanditiis suscipit dolorem quam officiis id odit, qui alias, corrupti esse dolores libero at culpa itaque eveniet.",
                   ability_range = "20 feet",
                   effect_area = "straight line",
                   min_level = "2",
                   is_spell = True,
                   school = "Destruction",
                   notes = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est, distinctio! Deleniti delectus harum blanditiis suscipit dolorem quam officiis id odit, qui alias, corrupti esse dolores libero at culpa itaque eveniet.",
                   character_id = character1.id)

ability2 = Ability(name = "Athletics",
                   image_url = "static/spell01.png",
                   damage = "N/A",
                   damage_type = "physical",
                   description = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est, distinctio! Deleniti delectus harum blanditiis suscipit dolorem quam officiis id odit, qui alias, corrupti esse dolores libero at culpa itaque eveniet.",
                   ability_range = "N/A",
                   effect_area = "self",
                   min_level = "1",
                   is_spell = False,
                   notes = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est, distinctio! Deleniti delectus harum blanditiis suscipit dolorem quam officiis id odit, qui alias, corrupti esse dolores libero at culpa itaque eveniet.",
                   character_id = character1.id)

weapon1 = Weapon(name = "Orcish Blade",
                 image_url = "static/weapon01.png",
                 weapon_type = "Short Sword",
                 damage = "1D6",
                 damage_type = "Slashing",
                 weapon_range = "4 ft",
                 description = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est, distinctio! Deleniti delectus harum blanditiis suscipit dolorem quam officiis id odit, qui alias, corrupti esse dolores libero at culpa itaque eveniet.",
                 weight = 5,
                 condition = "Fair",
                 rarity = "Common",
                 notes = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est, distinctio! Deleniti delectus harum blanditiis suscipit dolorem quam officiis id odit, qui alias, corrupti esse dolores libero at culpa itaque eveniet.",
                 is_equipped = True,
                 character_id = character1.id)

weapon2 = Weapon(name = "Wooden Bow",
                 image_url = "static/weapon03.png",
                 weapon_type = "Ranged",
                 damage_type = "Piercing",
                 damage = "2D4",
                 weapon_range = "100 ft",
                 description = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est, distinctio! Deleniti delectus harum blanditiis suscipit dolorem quam officiis id odit, qui alias, corrupti esse dolores libero at culpa itaque eveniet.",
                 weight = 3,
                 condition = "Good",
                 rarity = "Common",
                 notes = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est, distinctio! Deleniti delectus harum blanditiis suscipit dolorem quam officiis id odit, qui alias, corrupti esse dolores libero at culpa itaque eveniet.",
                 is_equipped = False,
                 character_id = character1.id)

item1 = Item(name = "Iron Shield",
             image_url = "static/item01.png",
             description = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est, distinctio! Deleniti delectus harum blanditiis suscipit dolorem quam officiis id odit, qui alias, corrupti esse dolores libero at culpa itaque eveniet.", 
             weight = 8,           
             is_wearable = True,
             armor_class = "Heavy Shield",
             condition = "Poor",
             rarity = "Common",
             quantity = 1,
             notes = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est, distinctio! Deleniti delectus harum blanditiis suscipit dolorem quam officiis id odit, qui alias, corrupti esse dolores libero at culpa itaque eveniet.",
             is_equipped = True,
             character_id = character1.id)

item2 = Item(name = "Health Potion",
             image_url = "static/item02.png",
             description = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est, distinctio! Deleniti delectus harum blanditiis suscipit dolorem quam officiis id odit, qui alias, corrupti esse dolores libero at culpa itaque eveniet.",
             weight = 0.5,             
             is_wearable = False,
             condition = "New",
             rarity = "Common",
             quantity = 3,
             notes = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Est, distinctio! Deleniti delectus harum blanditiis suscipit dolorem quam officiis id odit, qui alias, corrupti esse dolores libero at culpa itaque eveniet.",
             character_id = character1.id)


db.session.add_all([ability1, ability2, weapon1,
                    weapon2, item1, item2])

db.session.commit()
