"""Demilich Models"""

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

bcrypt = Bcrypt()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """User model."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True, unique=True)
    username = db.Column(db.String(25),
                         nullable=False, unique=True)
    email = db.Column(db.String(250),
                      nullable=False, unique=True)
    password = db.Column(db.Text,
                         nullable=False)

    characters = db.relationship('Character', backref="user", cascade="all, delete-orphan")
    
    @classmethod
    def signup(cls, username, password, email):
        """Registers new user with hashed password."""

        hashed = bcrypt.generate_password_hash(password)

        # Converts hasehd code from byte form to utf8
        hashed_utf8 = hashed.decode("utf8")

        user = User(username=username, password=hashed_utf8, email=email)
        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Authenticate user for login."""

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, password):
            return u
        else:
            return False

    def serialize(self):
        """Returns user in an easy to use dict format"""

        return {"id": self.id, "username": self.username, "password": self.password, "email": self.email}

    def __repr__(self):
        """Shows info about the user."""

        return f"<User {self.id} {self.username} {self.password} {self.email}>"


class Character(db.Model):
    """Character model."""

    __tablename__ = "characters"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True, unique=True)
    name = db.Column(db.String(50),
                      nullable=False)
    portrait_url = db.Column(db.String(500),
                      nullable=False)
    icon = db.Column(db.String(100),
                      nullable=False)
    class_name = db.Column(db.String(25),
                      nullable=False)
    race = db.Column(db.String(25),
                      nullable=False)
    level = db.Column(db.Integer,
                      nullable=False, 
                      default=1)
    stats = db.Column(db.Text,
                        nullable=False)
    alignment = db.Column(db.String(25),
                        nullable=False)
    proficiencies = db.Column(db.Text)
    statuses = db.Column(db.String(50))
    age = db.Column(db.String(25))
    backstory = db.Column(db.Text)
    languages = db.Column(db.Text)
    notes = db.Column(db.Text)
    is_dead = db.Column(db.Boolean, default=False)
    abyss_layer = db.Column(db.Text)
    hirelings = db.Column(db.Text)
    pets_minions = db.Column(db.Text)
    cause_of_death = db.Column(db.String(50))
    eulogy = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)

    abilities = db.relationship('Ability', backref="character", cascade="all, delete-orphan")
    weapons = db.relationship('Weapon', backref="character", cascade="all, delete-orphan")
    items = db.relationship('Item', backref="character", cascade="all, delete-orphan")

    def serialize(self):
        """Returns character in an easy to use dict format"""

        return {"id": self.id, "name": self.name, "portrait_url": self.portrait_url, "icon": self.icon, "class_name": self.class_name, "race": self.race, "level": self.level,
         "stats": self.stats, "alignment": self.alignment, "proficiencies": self.proficiencies, "statuses": self.statuses,
         "age": self.age, "backstory": self.backstory, "languages": self.languages, "notes": self.notes,
         "is_dead": self.is_dead, "abyss_layer": self.abyss_layer, "hirelings": self.hirelings, "pets_minions": self.pets_minions,
         "cause_of_death": self.cause_of_death, "eulogy": self.eulogy, "user_id": self.user_id}

    def __repr__(self):
        """Shows info about the character."""

        return f"<Character {self.id} {self.name} {self.class_name} {self.race} {self.level} {self.user_id}>"


class Ability(db.Model):
    """Ability model."""

    __tablename__ = "abilities"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True, unique=True)
    name = db.Column(db.String(50),
                      nullable=False)
    image_url = db.Column(db.String(500),
                      nullable=False)
    damage = db.Column(db.Text)
    damage_type = db.Column(db.String(25))
    description = db.Column(db.Text)
    ability_range = db.Column(db.String(25))
    effect_area = db.Column(db.String(25))
    min_level = db.Column(db.Integer)
    is_spell = db.Column(db.Boolean)
    school = db.Column(db.String(25))
    notes = db.Column(db.Text)
    character_id = db.Column(db.Integer, db.ForeignKey(
        'characters.id'), nullable=False)

    def serialize(self):
        """Returns ability in an easy to use dict format"""

        return {"id": self.id, "name": self.name, "image_url": self.image_url, "damage": self.damage, "damage_type": self.damage_type, "description": self.description, 
         "ability_range": self.ability_range, "effect_area": self.effect_area, "min_level": self.min_level,
         "is_spell": self.is_spell, "school": self.school, "notes": self.notes, "character_id": self.character_id}

    def __repr__(self):
        """Shows info about the ability."""

        return f"<Ability {self.id} {self.name} {self.is_spell} {self.school} {self.character_id}>"


class Weapon(db.Model):
    """Weapon model."""

    __tablename__ = "weapons"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True, unique=True)
    name = db.Column(db.String(50),
                      nullable=False)
    image_url = db.Column(db.String(500),
                      nullable=False)
    weapon_type = db.Column(db.String(25))
    damage = db.Column(db.String(25))
    damage_type = db.Column(db.String(25))
    weapon_range = db.Column(db.String(25))
    description = db.Column(db.Text)
    weight = db.Column(db.Float, default=0)
    condition = db.Column(db.String(25))
    rarity = db.Column(db.String(25))
    notes = db.Column(db.Text)
    is_equipped = db.Column(db.Boolean, default=False)
    character_id = db.Column(db.Integer, db.ForeignKey(
        'characters.id'), nullable=False)

    def serialize(self):
        """Returns weapon in an easy to use dict format"""

        return {"id": self.id, "name": self.name, "image_url": self.image_url, "weapon_type": self.weapon_type, "damage": self.damage, "damage_type": self.damage_type, 
         "weapon_range": self.weapon_range, "description": self.description, "weight": self.weight,
         "condition": self.condition, "rarity": self.rarity, "notes": self.notes, "is_equipped": self.is_equipped, "character_id": self.character_id}

    def __repr__(self):
        """Shows info about the weapon."""

        return f"<Ability {self.id} {self.name} {self.weapon_type} {self.damage_type} {self.character_id}>"


class Item(db.Model):
    """Item model."""

    __tablename__ = "items"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True, unique=True)
    name = db.Column(db.String(50),
                      nullable=False)
    image_url = db.Column(db.String(500),
                      nullable=False)
    description = db.Column(db.Text)
    weight = db.Column(db.Float, default=0)          
    is_wearable = db.Column(db.Boolean, default=False)
    armor_class = db.Column(db.String(25))
    condition = db.Column(db.String(25))
    rarity = db.Column(db.String(25))
    quantity = db.Column(db.String(25))
    notes = db.Column(db.Text)
    is_equipped = db.Column(db.Boolean, default=False)
    character_id = db.Column(db.Integer, db.ForeignKey(
        'characters.id'), nullable=False)

    def serialize(self):
        """Returns item in an easy to use dict format"""

        return {"id": self.id, "name": self.name, "image_url": self.image_url, "description": self.description, "weight": self.weight, 
        "is_wearable": self.is_wearable, "armor_class": self.armor_class, "condition": self.condition, "rarity": self.rarity, "quantity": self.quantity,
        "notes": self.notes, "is_equipped": self.is_equipped, "character_id": self.character_id}

    def __repr__(self):
        """Shows info about the item."""

        return f"<Item {self.id} {self.name} {self.is_wearable} {self.armor_class} {self.quantity} {self.character_id}>"