from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, IntegerField, TextField, BooleanField, DecimalField, SelectField
from wtforms.validators import InputRequired, Length, NumberRange, Optional
from wtforms.widgets import TextArea


class AddUserForm(FlaskForm):
    """Form used to add users to the database"""

    username = StringField("Username", validators=[
                           InputRequired(), Length(min=1, max=25, message="Username must be at least 1 character and not over 25.")])
    password = PasswordField("Password", validators=[InputRequired(), Length(
        min=5, max=50, message="Password must be at least 5 character and not over 50.")])
    email = StringField("Email", validators=[InputRequired(), Length(
        min=5, max=250, message="First name must be at least 5 character and not over 250.")])


class LoginUserForm(FlaskForm):
    """Form used to login user"""

    username = StringField("Username", validators=[
                           InputRequired(), Length(min=1, max=25, message="Username must be at least 1 character and not over 25.")])
    password = PasswordField("Password", validators=[InputRequired()])


class AddCharacterForm(FlaskForm):
    """Form to add new character"""

    name = StringField("Name", validators=[
                           InputRequired(), Length(min=1, max=50, message="Name must be at least 1 character and not over 50.")])
    portrait_url = SelectField("Portrait", choices=[("static/portrait01.png", "Knight"), 
                                                    ("static/portrait02.png", "Wizard"), 
                                                    ("static/portrait03.png", "Elf Archer"), 
                                                    ("static/portrait04.png", "Halfling")])
    icon = SelectField("Icon Image", choices=[("static/charactericon01.png", "Icon 1"), 
                                              ("static/charactericon02.png", "Icon 2"), 
                                              ("static/charactericon03.png", "Icon 3"), 
                                              ("static/charactericon04.png", "Icon 4"), 
                                              ("static/charactericon05.png", "Icon 5"), 
                                              ("static/charactericon06.png", "Icon 6")])
    class_name = StringField("Class", validators=[InputRequired(), Length(
        min=1, max=25, message="URL must be at least 1 character and not over 25.")])
    race = StringField("Race", validators=[InputRequired(), Length(
        min=1, max=25, message="Race must be at least 1 character and not over 25.")])
    level = IntegerField("Level", validators=[Optional()])
    alignment = StringField("Alignment", validators=[Length(
        min=0, max=25, message="Alignment must be under 25 characters.")])
    proficiencies = TextField("Proficiencies")
    statuses = StringField("Statuses", validators=[Length(
        min=0, max=50, message="Statuses must be under 50 characters.")])
    age = StringField("Age", validators=[Length(
        min=0, max=50, message="Age must be under 25 characters.")])
    traits = TextField("Traits")
    languages = TextField("Languages")
    stats = TextField("Stats", widget=TextArea(), validators=[InputRequired()])
    backstory = TextField("Backstory", widget=TextArea())
    notes = TextField("Notes", widget=TextArea())
    hirelings = TextField("List of Hirelings", widget=TextArea())
    pets_minions = TextField("List of Pets and Minions", widget=TextArea())


class AddAbilityForm(FlaskForm):
    """Form to add new Ability"""

    name = StringField("Name", validators=[
                           InputRequired(), Length(min=1, max=50, message="Name must be at least 1 character and not over 50.")])
    image_url = SelectField("Icon Image", choices=[("static/spell01.png", "spell 1")])
    damage = TextField("Damage")
    damage_type = StringField("Damage Type", validators=[Length(
        min=0, max=25, message="Damage type must be under 25 characters.")])
    ability_range = StringField("Range", validators=[Length(
        min=0, max=25, message="Range must be under 25 characters.")])
    effect_area = StringField("Area of Effect", validators=[Length(
        min=0, max=25, message="Area of effect must be under 25 characters.")])
    min_level = IntegerField("Minimum Level Required", validators=[Optional()])  
    school = StringField("School", validators=[Length(
        min=0, max=25, message="School must be under 25 characters.")])
    description = TextField("Description", widget=TextArea())
    notes = TextField("Notes", widget=TextArea())
    is_spell = BooleanField("Ability is a spell")


class AddWeaponForm(FlaskForm):
    """Form to add new Weapon"""

    name = StringField("Name", validators=[
                           InputRequired(), Length(min=1, max=50, message="Name must be at least 1 character and not over 50.")])
    image_url = SelectField("Icon Image", choices=[("static/weapon01.png", "Sword"), 
                                                   ("static/weapon02.png", "Battle Axe"), 
                                                   ("static/weapon03.png", "Bow")])
    damage = StringField("Damage", validators=[Length(
        min=0, max=25, message="Damage must be under 25 characters.")])
    weapon_type = StringField("Weapon Type", validators=[Length(
        min=0, max=25, message="Weapon type must be under 25 characters.")])
    damage_type = StringField("Damage Type", validators=[Length(
        min=0, max=25, message="Damage type must be under 25 characters.")])
    weapon_range = TextField("Weapon Range", validators=[Length(
        min=0, max=25, message="Weapon range must be under 25 characters.")])
    weight = DecimalField("Weight", validators=[Optional()])
    condition = StringField("Condition", validators=[Length(
        min=0, max=25, message="Condition must be under 25 characters.")])
    rarity = StringField("Rarity", validators=[Length(
        min=0, max=25, message="Rarity must be under 25 characters.")])
    description = TextField("Description", widget=TextArea())
    notes = TextField("Notes", widget=TextArea())
    is_equipped = BooleanField("Is equipped")


class EditWeaponForm(FlaskForm):
    """Form to edit Weapon"""

    name = StringField("Name", validators=[
                           InputRequired(), Length(min=1, max=50, message="Name must be at least 1 character and not over 50.")])
    image_url = SelectField("Icon Image", choices=[("static/weapon01.png", "Sword"), 
                                                   ("static/weapon02.png", "Battle Axe"), 
                                                   ("static/weapon03.png", "Bow")])
    damage = StringField("Damage", validators=[Length(
        min=0, max=25, message="Damage must be under 25 characters.")])
    weapon_type = StringField("Weapon Type", validators=[Length(
        min=0, max=25, message="Weapon type must be under 25 characters.")])
    damage_type = StringField("Damage Type", validators=[Length(
        min=0, max=25, message="Damage type must be under 25 characters.")])
    weapon_range = TextField("Weapon Range", validators=[Length(
        min=0, max=25, message="Weapon range must be under 25 characters.")])
    weight = DecimalField("Weight", validators=[Optional()])
    condition = StringField("Condition", validators=[Length(
        min=0, max=25, message="Condition must be under 25 characters.")])
    rarity = StringField("Rarity", validators=[Length(
        min=0, max=25, message="Rarity must be under 25 characters.")])
    description = TextField("Description", widget=TextArea())
    notes = TextField("Notes", widget=TextArea())


class AddItemForm(FlaskForm):
    """Form to add new Item"""

    name = StringField("Name", validators=[
                           InputRequired(), Length(min=1, max=50, message="Name must be at least 1 character and not over 50.")])
    image_url = SelectField("Icon Image", choices=[("static/item01.png", "Shield"), 
                                                   ("static/item02.png", "Potion")])
    weight = DecimalField("Weight", validators=[Optional()])
    armor_class = StringField("Armor Class", validators=[Length(
        min=0, max=25, message="Armor Class must be under 25 characters.")])
    damage_type = StringField("Damage Type", validators=[Length(
        min=0, max=25, message="Damage type must be under 25 characters.")])
    condition = StringField("Condition", validators=[Length(
        min=0, max=25, message="Condition must be under 25 characters.")])
    rarity = StringField("Rarity", validators=[Length(
        min=0, max=25, message="Rarity must be under 25 characters.")])
    quantity = StringField("Quantity", validators=[Length(
        min=0, max=25, message="Quantity must be under 25 characters.")])
    description = TextField("Description", widget=TextArea())
    notes = TextField("Notes", widget=TextArea())
    is_wearable = BooleanField("Item is Wearable")
    is_equipped = BooleanField("If wearable is it equipped?")


class EditItemForm(FlaskForm):
    """Form to edit Item"""

    name = StringField("Name", validators=[
                           InputRequired(), Length(min=1, max=50, message="Name must be at least 1 character and not over 50.")])
    image_url = SelectField("Icon Image", choices=[("static/item01.png", "Shield"), 
                                                   ("static/item02.png", "Potion")])
    weight = DecimalField("Weight", validators=[Optional()])
    armor_class = StringField("Armor Class", validators=[Length(
        min=0, max=25, message="Armor Class must be under 25 characters.")])
    damage_type = StringField("Damage Type", validators=[Length(
        min=0, max=25, message="Damage type must be under 25 characters.")])
    condition = StringField("Condition", validators=[Length(
        min=0, max=25, message="Condition must be under 25 characters.")])
    rarity = StringField("Rarity", validators=[Length(
        min=0, max=25, message="Rarity must be under 25 characters.")])
    quantity = StringField("Quantity", validators=[Length(
        min=0, max=25, message="Quantity must be under 25 characters.")])
    description = TextField("Description", widget=TextArea())
    notes = TextField("Notes", widget=TextArea())


class KillCharacterForm(FlaskForm):
    """Form to kill character"""

    cause_of_death = StringField("Cause of Death", validators=[Length(
        min=0, max=50, message="Cause of death must be under 50 characters.")])
    eulogy = TextField("Eulogy", widget=TextArea())