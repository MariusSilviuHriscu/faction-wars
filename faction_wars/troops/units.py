import typing
from dataclasses import dataclass
from enum import Enum
from faction_wars.resources.resources import Resources


class UnitType(Enum):
    INFANTRY = 1
    CAVALRY = 2
    ARTILLERY = 3

class UnitAttackType(Enum):
    PHYSICAL = 1
    MAGIC = 2
    PIERCING = 3

class MagickalType(Enum):
    FIRE = 1
    ICE = 2
    LIGHTNING = 3

@dataclass
class UnitData:
    unit_id : int
    name : str
    required_resources : Resources
    
    unit_speed : float
    unit_health : int
    unit_armor : int
    unit_magickal_resistence : int
    unit_type : UnitType
    unit_attack_type : UnitAttackType
    magickal_type : MagickalType | None

    attack_range : float
    attack_speed : float
    attack_damage : int
    attack_cooldown : float
    attack_radius : float
    attack_range : float
    
    