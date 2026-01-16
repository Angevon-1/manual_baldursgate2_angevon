from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

def requiresCrushSlashPlus1():
    """Returns a requires string that checks if the player has a magical crushing or slashing weapon, for defeating mustard jellies."""
    return "{OptAll((|Progressive Club:1| AND |@Weapons - Clubs:1|) OR (|Progressive Flail:1| AND |@Weapons - Flails:1|) OR (|Progressive Mace:1| AND |@Weapons - Maces:1|) OR (|Progressive War Hammer:1| AND |@Weapons - War Hammers:1|) OR (|Progressive Morning Star:1| AND |@Weapons - Morning Stars:1|) OR (|Progressive Staff:1| AND |@Weapons - Staves & Rods:1|) OR (|Progressive Axe:1| AND |@Weapons - Axes:1|) OR (|Progressive Bastard Sword:1| AND |@Weapons - Bastard Swords:1|) OR (|Progressive Katana:1| AND |@Weapons - Katanas:1|) OR (|Progressive Long Sword:1| AND |@Weapons - Long Swords:1|) OR (|Progressive Two Handed Sword:1| AND |@Weapons - Two Handed Swords:1|))}"

def requiresCrushPlus1():
    """Returns a requires string that checks if the player has a magical crushing weapon, for defeating clay golems."""
    return "{OptAll((|Progressive Club:1| AND |@Weapons - Clubs:1|) OR (|Progressive Flail:1| AND |@Weapons - Flails:1|) OR (|Progressive Mace:1| AND |@Weapons - Maces:1|) OR (|Progressive War Hammer:1| AND |@Weapons - War Hammers:1|) OR (|Progressive Morning Star:1| AND |@Weapons - Morning Stars:1|) OR (|Progressive Staff:1| AND |@Weapons - Staves & Rods:1|))}"

#def requiresPlus3():
#    """Returns a requires string that checks if the player has at least one +3 weapon and/or Progressive Weapon up to a count of 3. 
#    This to evaluate whether an enemy (e.g. a golem) can be defeated by the player based on their available equipment"""
#    return "{OptAll(|Progressive Club:3| OR |Progressive Flail:3| OR |Progressive Mace:3| OR |Progressive Morning Star:3| OR |Progressive War Hammer:3| OR |Progressive Staff:3| OR |Progressive Axe:3| OR |Progressive Bastard Sword:3| OR |Progressive Katana:3| OR |Progressive Long Sword:3| OR |Progressive Scimitar, Wakizashi, Ninja-To:3| OR |Progressive Two Handed Sword:3| OR |Progressive Dagger:3| OR |Progressive Halberd:3| OR |Progressive Spear:3| OR |Progressive Short Sword:3|)}"

def requiresPlus4():
    """Returns a requires string that checks if the player has at least one +4 weapon and/or Progressive Weapon up to a count of 4. 
    This to evaluate whether an enemy (e.g. a golem) can be defeated by the player based on their available equipment"""
    return "{OptAll(((|@+4 Crushing Weapons:1| OR |@+5 Crushing Weapons:1|) AND (|Progressive Club:4| OR |Progressive Flail:4| OR |Progressive Mace:4| OR |Progressive Morning Star:4| OR |Progressive War Hammer:4| OR |Progressive Staff:4|)) OR ((|@+4 Slashing Weapons:1| OR |@+5 Slashing Weapons:1|) AND (|Progressive Axe:4| OR |Progressive Bastard Sword:4| OR |Progressive Katana:4| OR |Progressive Long Sword:4| OR |Progressive Two Handed Sword:4|)) OR (|@+4 Piercing Weapons:1| AND (|Progressive Dagger:4| OR |Progressive Halberd:4| OR |Progressive Spear:4| OR |Progressive Short Sword:4|)))}"

def requiresPlus3():
    """Returns a requires string that checks if the player has at least one +3 weapon and/or Progressive Weapon up to a count of 3. 
    This to evaluate whether an enemy (e.g. a golem) can be defeated by the player based on their available equipment"""
    return "{OptAll(((|@+3 Crushing Weapons:1| OR |@+4 Crushing Weapons:1| OR |@+5 Crushing Weapons:1|) AND (|Progressive Club:3| OR |Progressive Flail:3| OR |Progressive Mace:3| OR |Progressive Morning Star:3| OR |Progressive War Hammer:3| OR |Progressive Staff:3|)) OR ((|@+3 Slashing Weapons:1| OR |@+4 Slashing Weapons:1| OR |@+5 Slashing Weapons:1|) AND (|Progressive Axe:3| OR |Progressive Bastard Sword:3| OR |Progressive Katana:3| OR |Progressive Long Sword:3| OR |Progressive Two Handed Sword:3|)) OR ((|@+3 Piercing Weapons:1| OR |@+4 Piercing Weapons:1|) AND (|Progressive Dagger:3| OR |Progressive Halberd:3| OR |Progressive Spear:3| OR |Progressive Short Sword:3|)))}"
