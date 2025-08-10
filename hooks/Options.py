# Object classes from AP that represent different types of options that you can create
from Options import Option, FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange, OptionGroup, PerGameCommonOptions
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

class Goal(Choice):
    """There are several goal options: 
    1. Complete major sidequest(s) (deArnise Keep, Cult of the Eyeless, Trademeet, Windspear Hills, Planar Sphere, Shade Lord) to receive tokens. Collect enough tokens to goal. More required tokens makes for a longer game. Any chapter amount can be used with this goal. 
    2. Escape Spellhold - Reach Chapter 4 and complete it (excludes City of Caverns). 
    3. Defeat Red Dragon Firkraag - Reach Chapter 6 and defeat Firkraag. You can complete this sooner but the logic expects Chapter 6 to ensure you're properly equipped. 
    4. Defeat Kangaxx the Demilich - Reach Chapter 6 and defeat Kangaxx. You can complete this sooner but the logic expects Chapter 6 to ensure you're properly equipped.
    5. Defeat Jon Irenicus - Reach Chapter 7 and defeat Irenicus at the Tree of Life 
    Please ensure you have the required chapters enabled below if you're choosing a late chapter goal or it won't generate."""
    display_name = "Goal condition"
    option_earn_at_least_1_token = 0
    option_earn_2_tokens = 1
    option_earn_3_tokens = 2
    option_earn_4_tokens = 3
    option_earn_5_tokens = 4
    option_earn_6_tokens = 5
    option_escape_spellhold = 6
    option_defeat_firkraag = 7
    option_defeat_kangaxx = 8
    option_defeat_irenicus = 9
    default = 2

class IncludeIrenicusDungeon(Toggle):
    """Adds key items and locations related to Chapter 1 (Irenicus's Dungeon).
    When false, it is recommended that you use the Skip Chateau Irenicus mod to get out of there easier after starting a new game."""
    display_name = "Include Irenicus's Dungeon"
    default = True

class ChapterToFinish(Choice):
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

class IncludeCoC(Toggle):
    """When this option is true, key items and locations related to the optional Chapter 4 area, City of Caverns/Sahaguin City will be included in the multiworld.
    When this is on, you'll need to take Saemon's offer to sail away from Spellhold at the end of that questline. If you're not using this option, you can take the portal under Spellhold directly to Chapter 5."""
    display_name = "Include City of Caverns"
    default = False

class PayGaelanBayle(Choice):
    """Choose whether you will side with Gaelan Bayle and the Shadow Thieves, or with Bodhi and the vampires, in Chapter 3.
    This affects the names of item and location checks, so be sure to match this with your choice in the game."""
    display_name = "Side in Chapter 3"
    option_shadow_thieves = 0    
    option_bodhi = 1
    default = 0

class IncludeEnhancedEdition(Toggle):
    """Adds enhanced edition items, characters, and locations to the relevant options."""
    display_name = "Include Enhanced Edition"
    default = False

class Equipment(Choice):
    """Choose how you'd like equipment in the item pool. 
    No Equipment - No equipment is in the pool. This works best with the Gibberlings 3 Item Randomizer mod. 
    Magical Equipment - Each individual magical equipment item is added to the pool.
    Progressive Equipment - Equipment is progressive. You can't use +x weapons until you've received the same number of progressives for that weapon type. For example, the Namarra short sword is a +2 short sword. You'll need two “Progressive Short Sword” items in order to be able to use it.
    Both Magical and Progressive - Adds a lot of items, so be sure to add more chapters, or some items will be lost."""
    option_no_equipment = 0
    option_magical_equipment = 1
    option_progressive_equipment = 2
    option_magical_and_progressive = 3
    default = 1
    display_name = "Equipment in pool"

class IncludeCollectorsEdition(Toggle):
    """When this is true, it adds equipment from the BG2 Collector's Edition to the multiworld. When false, they aren't added.
    These items might be considered overpowered; as such this option exists to exclude them."""
    display_name = "Add Collector's Edition Items"
    default = False

class IncludeWatchersKeep(Toggle):
    """When this is true, it adds equipment from Watcher's Keep to the multiworld. When false, they aren't added.
    Note: watcher's keep location checks are NOT affected, they are not implemented at all at this time, this is purely about the item rewards."""
    display_name = "Add Watcher's Keep Items"
    default = False

class Companions(Choice):
    """Choose how you'd like the companion NPCs & their quests randomized. 
    None - Companions and their quests are not included in the multiworld. 
    Companions Only - Each individual companion is an item in the pool. To see what companions are available to you, open the Manual Client and connect to your room. Then open the Manual tab. Then expand the 'Companions' section.
    Companion Quests Only - Adds checks for the companion quests. These quests can take a long time to activate in the game; speedrunners should not use this.
    Both Companions and quests - Adds both chacters and their quests."""
    option_none = 0
    option_companion_quests_only = 1
    option_companions_only = 2
    option_companions_and_quests = 3
    default = 0
    display_name = "Companion Option"

class StartingCompanionAmount(Range):
    """When companions are randomized, use this option to set how many companions you'll already have at the start of the game. They will be added at random to your starting inventory. You'll still have to go and recruit them."""
    display_name = "Starting Companion Amount"
    range_start = 0
    range_end = 15
    default = 3

class LootChecks(Choice):
    """Choose how you want loot checks to work.
    None - No loot checks.
    Rooms - Adds general "loot x room" checks. This is the recommended setting. Lockpicking ability is not required.
    Containers - Adds every INDIVIDUAL lootable crate/barrel/chest as location checks. To compensate for check count, consumable potions and scrolls will be added to the item pool to add filler. Lockpicking is required and NOT accounted for. Progression may be locked behind a locked chest and it's up to you to get past it."""
    display_name = "Loot checks type"
    option_none = 0
    option_rooms = 1
    option_containers = 2
    option_rooms_and_containers = 3
    default = 1

class ForgingChecks(Toggle):
    """Set this to true if you'd like to earn a check for forging items like Crom Faeyr, Flail of the Ages, etc. Adds 11 checks and 20 items."""
    display_name = "Include Forging Checks"
    default = False

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
    options["goal"] = Goal
    options["final_chapter"] = ChapterToFinish
    options["include_irenicus_dungeon"] = IncludeIrenicusDungeon
    options["gaelan_or_bodhi"] = PayGaelanBayle
    options["include_city_of_caverns"] = IncludeCoC
    options["equipment"] = Equipment    
    options["include_enhanced_edition"] = IncludeEnhancedEdition
    options["include_collectors_edition"] = IncludeCollectorsEdition
    options["include_watchers_keep"] = IncludeWatchersKeep
    options["companions"] = Companions
    options["starting_companion_amount"] = StartingCompanionAmount
    options["loot_checks"] = LootChecks
    options["forging_checks"] = ForgingChecks

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
