# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions, Visibility
# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value
from typing import Type, Any


####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#

class include_irenicus_dungeon(Toggle):
    """Adds key items and locations related to Chapter 1 (Irenicus's Dungeon).
    When false, it is recommended that you use the Skip Chateau Irenicus mod to get out of there easier after starting a new game."""
    display_name = "Include Irenicus's Dungeon"
    default = True

class final_chapter(Choice):
    """Select which chapter to finish the game in. When you choose a later chapter, the previous chapters are automatically enabled. 
    Later chapter = longer game, more items, and more locations.
    Some goal options override this choice."""
    option_chapter3 = 0
    option_chapter4 = 1
    option_chapter5 = 2
    option_chapter6 = 3
    option_chapter7 = 4
    display_name = "Final Chapter"
    default = 0

class include_city_of_caverns(Toggle):
    """When this option is true, key items and locations related to the optional Chapter 4 area, City of Caverns/Sahaguin City will be included in the multiworld.
    When this is on, you'll need to take Saemon's offer to sail away from Spellhold at the end of that questline. If you're not using this option, you can take the portal under Spellhold directly to Chapter 5."""
    display_name = "Include City of Caverns"
    default = False

class gaelan_or_bodhi(Choice):
    """Choose whether you will side with Gaelan Bayle and the Shadow Thieves, or with Bodhi and the vampires, in Chapter 3.
    This affects the names of item and location checks, so be sure to match this with your choice in the game."""
    display_name = "Side in Chapter 3"
    option_shadow_thieves = 0    
    option_bodhi = 1
    default = 0

class misc_items(Choice):
    """Choose how you'd like miscellaneous items in the item pool. Miscellaneous items are things like the spider figurine and the harp of discord.
    No Misc. Items- No miscellaneous items are in the pool. This works best with the Gibberlings 3 Item Randomizer mod. 
    Base Game Misc. Items Only - Miscellaneous items from the base game are added to the pool. Does not include Collector's Edition or Enhanced Edition items. 
    Base Game Misc. Items and Collector's Edition - Miscellaneous items from the base game are added to the pool, including Collector's Edition items. 
    Base Game Misc. Items and Enhanced Edition - Miscellaneous items from the base game are added to the pool, including Enhanced Edition items.
    Base Game Misc. Items, Collector's Edition, and Enhanced Edition - Miscellaneous items from the base game are added to the pool, including Collector's Edition and Enhanced Edition items.
    """
    option_no_misc_items = 0
    option_base_game_only = 1
    option_base_game_and_ce = 2
    option_base_game_and_ee = 3
    option_base_game_ce_and_ee = 4
    default = 0
    display_name = "Misc. Items in pool"

class equipment(Choice):
    """Choose how you'd like equipment in the item pool. Please note the more equipment you add, the more chapters you should include too, else items will be lost during generation.
    No Equipment - No equipment is in the pool. This works best with the Gibberlings 3 Item Randomizer mod. 
    Base Game Magical Equipment Only - Each individual magical equipment item from the base game is added to the pool. Does not include Collector's Edition or Enhanced Edition items. 
    Base Game Magical Equipment and Collector's Edition - Each individual magical equipment item from the base game is added to the pool, including Collector's Edition items. These items might be considered overpowered.
    Base Game Magical Equipment and Enhanced Edition - Each individual magical equipment item from the base game is added to the pool, including Enhanced Edition items.
    Base Game Magical Equipment, Collector's Edition, and Enhanced Edition - Each individual magical equipment item from the base game is added to the pool, including Collector's Edition and Enhanced Edition items.
    """
    option_no_equipment = 0
    option_base_game_only = 1
    option_base_game_and_ce = 2
    option_base_game_and_ee = 3
    option_base_game_ce_and_ee = 4
    default = 0
    display_name = "Equipment in pool"

class progressive_equipment(Toggle):
    """Use this option to make equipment progressive. You can't use +x weapons until you've received the same number of progressives for that weapon type. For example, the Namarra short sword is a +2 short sword. You'll need two “Progressive Short Sword” items in order to be able to use it. Works well with the Gibberlings 3 Item Randomizer mod.
    This CAN be combined with the equipment option choice above, however items will likely be lost during generation.
    Be aware that currently the logic does not account for whether you've received enough progressives to defeat enemies that require certain +x's (golems, jellies, etc.)."""
    default = 1
    display_name = "Progressive Equipment"

class include_watchers_keep(Toggle):
    """When this is true, it adds equipment from Watcher's Keep to the multiworld. When false, they aren't added.
    Note: watcher's keep location checks are NOT affected, they are not implemented at all at this time, this is purely about the item rewards."""
    display_name = "Add Watcher's Keep Items"
    default = False

class companions(Choice):
    """Choose how you'd like the companion NPCs (items) & their quests (locations) randomized. 
    None - Companions and their quests are not included in the multiworld. 
    Companions Only - Each individual non-EE companion is an item. To see what companions are available to you, open the Manual Client and connect to your room. Then open the Manual tab. Then expand the 'Companions' section.
    Companions Only Including Enhanced Edition - as above, but includes the Enhanced Edition companions.
    Quests Only - Adds location checks for the non-EE companion quests. These quests can take a long time to activate in the game; speedrunners should not use any option that includes quests.  
    Quests Only Including Enhanced Edition - as above, but includes the Enhanced Editions companions and their quests and areas.
    Companions and Quests - Adds non-EE companions and their quests. 
    Companions and Quests Including Enhanced Edition - Adds all companions and quests and areas, including Enhanced Edition.
    """
    option_none = 0
    option_companions_only = 1
    option_companions_only_including_ee = 2
    option_quests_only = 3
    option_quests_only_including_ee = 4
    option_companions_and_quests = 5
    option_companions_and_quests_including_ee = 6
    default = 0
    display_name = "Companion Option"

class starting_companion_amount(Range):
    """When companions are randomized, use this option to set how many companions you'll already have at the start of the game. They will be added at random to your starting inventory. You'll still have to go and recruit them.
    Leave this at 0 if you're not randomizing the companions.""" 
    display_name = "Starting Companion Amount"
    range_start = 0
    range_end = 5
    default = 0

class loot_checks(Choice):
    """Choose how you want loot checks to work.
    None - No loot checks.
    Rooms - Adds general "loot x room" checks. Lockpicking ability is not necessarily required.
    Containers - Adds every INDIVIDUAL lootable crate/barrel/chest as location checks. To compensate for check count, consumable potions and scrolls will be added to the item pool to add filler. Lockpicking is required and NOT accounted for. Progression may be locked behind a locked chest and it's up to you to get past it."""
    display_name = "Loot checks type"
    option_none = 0
    option_rooms = 1
    option_containers = 2
    option_rooms_and_containers = 3
    default = 0

class forging_checks(Toggle):
    """Set this to true if you'd like to earn a check for forging items like Crom Faeyr, Flail of the Ages, etc. Adds 11 checks and 20 items."""
    display_name = "Include Forging Checks"
    default = False
    
class adrian_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Adrian NPC Mod"
    default = False

class ajantis_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Ajantis for BG2 NPC Mod"
    default = False

class angelo_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Angelo NPC Mod"
    default = False

class arath_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Arath NPC Mod"
    default = False

class auren_aseph_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Auren Aseph NPC Mod"
    default = False

class branwen_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Branwen for BG2 NPC Mod"
    default = False

class chloe_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Chloe NPC Mod"
    default = False

class coran_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Coran for BG2 NPC Mod"
    default = False

class dace_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Dace Linton NPC Mod"
    default = False

class darian_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Darian NPC Mod"
    default = False

class drake_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Drake NPC Mod"
    default = False

class dvaradime_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Dvaradime NPC Mod"
    default = False

class evandra_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Evandra NPC Mod"
    default = False

class fade_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Fade NPC Mod"
    default = False

class faren_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Faren NPC Mod"
    default = False

class gavin_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Gavin NPC Mod"
    default = False

class hubelpot_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Hubelpot NPC Mod"
    default = False
    
class isra_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Isra NPC Mod"
    default = False

class kelsey_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Kelsey NPC Mod"
    default = False

class keto_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Keto NPC Mod"
    default = False

class nathaniel_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Nathaniel NPC Mod"
    default = False
   
class nephele_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Nephele NPC Mod"
    default = False

class ninde_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Ninde NPC Mod"
    default = False

class paina_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Pai'Na NPC Mod"
    default = False

class sirene_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Sirene NPC Mod"
    default = False

class tashia_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Tashia NPC Mod"
    default = False

class xan_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Xan for BG2 NPC Mod"
    default = False

class xulaye_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Xulaye NPC Mod"
    default = False

class yeslick_mod_npc(Toggle):
    """Set this to true if you're using this companion mod. This adds the npc as a receivable item if the companions have been randomized."""
    display_name = "Yeslick for BG2 NPC Mod"
    default = False

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["final_chapter"] = final_chapter
    options["include_irenicus_dungeon"] = include_irenicus_dungeon
    options["gaelan_or_bodhi"] = gaelan_or_bodhi
    options["include_city_of_caverns"] = include_city_of_caverns
    options["equipment"] = equipment
    options["misc_items"] = misc_items
    options["progressive_equipment"] = progressive_equipment    
    options["loot_checks"] = loot_checks
    options["forging_checks"] = forging_checks
    options["include_watchers_keep"] = include_watchers_keep
    options["companions"] = companions
    options["starting_companion_amount"] = starting_companion_amount 
    options["adrian_mod_npc"] = adrian_mod_npc  
    options["ajantis_mod_npc"] = ajantis_mod_npc 
    options["angelo_mod_npc"] = angelo_mod_npc  
    options["arath_mod_npc"] = arath_mod_npc
    options["auren_aseph_mod_npc"] = auren_aseph_mod_npc
    options["branwen_mod_npc"] = branwen_mod_npc
    options["chloe_mod_npc"] = chloe_mod_npc 
    options["coran_mod_npc"] = coran_mod_npc 
    options["dace_mod_npc"] = dace_mod_npc 
    options["darian_mod_npc"] = darian_mod_npc 
    options["drake_mod_npc"] = drake_mod_npc 
    options["dvaradime_mod_npc"] = dvaradime_mod_npc 
    options["evandra_mod_npc"] = evandra_mod_npc  
    options["fade_mod_npc"] = fade_mod_npc
    options["faren_mod_npc"] = faren_mod_npc
    options["gavin_mod_npc"] = gavin_mod_npc
    options["hubelpot_mod_npc"] = hubelpot_mod_npc
    options["isra_mod_npc"] = isra_mod_npc
    options["kelsey_mod_npc"] = kelsey_mod_npc 
    options["keto_mod_npc"] = keto_mod_npc 
    options["nathaniel_mod_npc"] = nathaniel_mod_npc 
    options["nephele_mod_npc"] = nephele_mod_npc 
    options["ninde_mod_npc"] = ninde_mod_npc   
    options["paina_mod_npc"] = paina_mod_npc  
    options["sirene_mod_npc"] = sirene_mod_npc   
    options["tashia_mod_npc"] = tashia_mod_npc
    options["xan_mod_npc"] = xan_mod_npc  
    options["xulaye_mod_npc"] = xulaye_mod_npc  
    options["yeslick_mod_npc"] = yeslick_mod_npc 


    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: Type[PerGameCommonOptions]):
    # To access a modifiable version of options check the dict in options.type_hints
    # For example if you want to change DLC_enabled's display name you would do:
    # options.type_hints["DLC_enabled"].display_name = "New Display Name"

    #  Here's an example on how to add your aliases to the generated goal
    # options.type_hints['goal'].aliases.update({"example": 0, "second_alias": 1})
    # options.type_hints['goal'].options.update({"example": 0, "second_alias": 1})  #for an alias to be valid it must also be in options

    pass

# Use this Hook if you want to add your Option to an Option group (existing or not)
def before_option_groups_created(groups: dict[str, list[Type[Option[Any]]]]) -> dict[str, list[Type[Option[Any]]]]:
    # Uses the format groups['GroupName'] = [TotalCharactersToWinWith]
    return groups

def after_option_groups_created(groups: list[OptionGroup]) -> list[OptionGroup]:
    return groups
