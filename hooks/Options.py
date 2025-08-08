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

#class Goal(Choice):
#    """There are several goal options: 
#    1. Complete major sidequest(s) (deArnise Keep, Cult of the Eyeless, Trademeet, Windspear Hills, Planar Sphere, Shade Lord) to receive tokens. Collect enough tokens to goal. More required tokens makes for a longer game. Any chapter amount can be used with this goal. 
#    2. Escape Spellhold - Reach Chapter 4 and complete it (excludes City of Caverns). 
#    3. Defeat Red Dragon Firkraag - Reach Chapter 6 and defeat Firkraag. You can complete this sooner but the logic expects Chapter 6 to ensure you're properly equipped. 
#    4. Defeat Kangaxx the Demilich - Reach Chapter 6 and defeat Kangaxx. You can complete this sooner but the logic expects Chapter 6 to ensure you're properly equipped.
#    5. Defeat Jon Irenicus - Reach Chapter 7 and defeat Irenicus at the Tree of Life 
#    Please ensure you have the required chapters enabled below if you're choosing a late chapter goal or it won't generate."""
#    display_name = "Goal condition"
#    option_earn_at_least_1_token = 0
#    option_earn_2_tokens = 1
#    option_earn_3_tokens = 2
#    option_earn_4_tokens = 3
#    option_earn_5_tokens = 4
#    option_earn_6_tokens = 5
#    option_escape_spellhold = 6
#    option_defeat_firkraag = 7
#    option_defeat_kangaxx = 8
#    option_defeat_irenicus = 9
#    default = 2

class IncludeIrenicusDungeon(Toggle):
    """Adds key items and locations related to Chapter 1 (Irenicus's Dungeon).
    When false, it is recommended that you use the Skip Chateau Irenicus mod to get out of there easier after starting a new game."""
    display_name = "Include Irenicus's Dungeon?"
    default = True

class IncludeC4(Toggle):
    """When this option is true, key items and locations related to Chapter 4 (Brynnlaw, Spellhold) will be included in the multiworld.
    This option is required for the Escape Spellhold goal."""
    display_name = "Include Chapter 4?"
    default = True

class IncludeCoC(Toggle):
    """When this option is true, key items and locations related to the optional Chapter 4 area, City of Caverns/Sahaguin City will be included in the multiworld.
    When this is on, you'll need to take Saemon's offer to sail away from Spellhold at the end of that questline. If you're not using this option, you can take the portal under Spellhold directly to Chapter 5."""
    display_name = "Include City of Caverns?"
    default = False

class IncludeC5(Toggle):
    """When this option is true, key items and locations related to Chapter 5 (Underdark) will be included in the multiworld.
    It is recommended to include more chapters if you're using the options below that add a lot of items. If this is true, the previous chapters must also be true."""          
    display_name = "Include Chapter 5?"
    default = True

class IncludeC6(Toggle):
    """When this option is true, key items and locations related to Chapter 6 will be included in the multiworld.
    This option is required to be true for the Defeat Red Dragon Firkraag and Defeat Kangaxx the Demilich goals.
    If this is true, the previous chapters must also be true."""          
    display_name = "Include Chapter 6?"
    default = True

class IncludeC7(Toggle):
    """When this option is true, key items and locations related to the Final Chapter, Chapter 7 (Suldanessellar), will be included in the multiworld.
    This option is required to be true for the Defeat Jon Irenicus goal.
    If this is true, the previous chapters must also be true."""          
    display_name = "Include Chapter 7?"
    default = True

#class ChaptersToInclude(Choice):
#   """Select which extra chapters to include in the game. Chapter 2 and 3 are always enabled. Some chapters are required for the different goals."""
#   option_no_extra_chapters = 0
#   option_chapter4 = 1
#   option_chapter5 = 2
#   option_chapter6 = 3
#   option_chapter7 = 4
#   display_name = "Chapters to include"
#   default = 1

class PayGaelanBayle(Toggle):
    """When this option is true, you'll side with Gaelan Bayle and the Shadow Thieves in Chapter 3.
    When false, you'll side with Bodhi instead.
    This affects the names of item and location checks, so please choose the path in the game that matches your option choice here."""
    display_name = "Side with the Shadow Thieves in Chapter 3?"
    default = True

class IncludeEnhancedEdition(Toggle):
    """Adds enhanced edition items, characters, and locations to the relevant options."""
    display_name = "Include Enhanced Edition?"
    default = False

class IncludeEquipment(Toggle):
    """This adds each magical equipment item to the multiworld. By default this is set to true.
    This adds A LOT OF ITEMS. When using this option, you should include more chapters in the options above or else items will be lost in generation."""
    display_name = "Add Magical Equipment to the item pool?"
    default = True

class ProgressiveEquipment(Toggle):
    """When this is true, you can't use +x weapons until you've received the same number of progressives for that weapon type.
    For example, the Namarra short sword is a +2 short sword. You'll need two “Progressive Short Sword” items in order to be able to use it."""
    display_name = "Make Equipment Progressive?"
    default = False

#class Equipment(Choice):
#    """Choose how you'd like equipment in the item pool. 
#    No Equipment - No equipment is in the pool. This works best with the item randomizer mod.
#    Magical Equipment - Each individual magical equipment item is added to the pool.
#    Progressive Equipment - Equipment is progressive. You can't use +x weapons until you've received the same number of progressives for that weapon type. For example, the Namarra short sword is a +2 short sword. You'll need two “Progressive Short Sword” items in order to be able to use it.
#    Both Magical and Progressive - Adds a lot of items, so be sure to add more chapters to accomade them, else some items will be lost."""
#    option_no_equipment = 0
#    option_magical_equipment = 1
#    option_progressive_equipment = 2
#    option_magical_and_progressive = 3

class IncludeCollectorsEdition(Toggle):
    """When this is true, it adds equipment from the BG2 Collector's Edition to the multiworld. When false, they aren't added.
    These items might be considered overpowered; as such this option exists to exclude them."""
    display_name = "Add Collector's Edition Equipment?"
    default = False

class IncludeWatchersKeep(Toggle):
    """When this is true, it adds equipment from Watcher's Keep to the multiworld. When false, they aren't added.
    Note: watcher's keep location checks are NOT affected, they are not implemented at all at this time, this is purely about the item rewards."""
    display_name = "Add Watcher's Keep Items?"
    default = False

class IncludeCompanionQuests(Toggle):
    """When this option is true, items & locations related to all the companion NPC quests are added to the multiworld.
    You must not kill any potential party members! Don't let any die before you've done their checks!
    These quests can take a long time to activate in the game; speedrunners should keep this set to false."""
    display_name = "Add Companion quests?"
    default = False

class IncludeNPCs(Toggle):
    """When this option is true, the companion NPCs themselves are added as unlockable items to be found in the multiworld. You will automatically be given 3 NPCs at random at the start of the game.
    To see what characters are available to you, open the Manual Client and connect to your room. Then open the Manual tab. Then expand the 'Characters' section.
    When used in conjunction with include_companion_quests, this option adds more logical access rules based on your available NPCs. You won't be expected to complete a companion quest until you have received the corresponding NPC.
    Without this option, companion quests are instead locked by the region where the companion exists and where the quests take place.
    When true this adds 17 items (22 if enhanced edition is enabled)."""
    display_name = "Add npc companions?"
    default = False

class LootChecks(Toggle):
    """Set this to true if you want INDIVIDUAL lootable crates/barrels/chests added to the pool as location checks.
    To compensate for check count, include_consumables and/or include_equipment options should be set to true to add filler.
    Note that your Lockpicking ability is NOT accounted for. Progression may be locked behind a locked chest and it's up to you to get past it."""
    display_name = "Add individual lootables?"
    default = False

class LootChecksLite(Toggle):
    """Set this to true to have general 'loot x room' as checks instead of every individual lootable as a check.
    This is more balanced than the full loot checks option and easier to track. Lockpicking ability is not required.
    This is the recommended loot setting."""
    display_name = "Add looting by room?"
    default = True

class ForgingChecks(Toggle):
    """Set this to true if you'd like to earn a check for forging items like Crom Faeyr, Flail of the Ages, etc. Adds 11 checks and 20 items."""
    display_name = "Include Forging Checks?"
    default = False

class Consumables(Toggle):
    """When this is true, scrolls and potions are added as filler to the multiworld.
    This should mostly only be on when loot_checks_by_lootable is on, to add filler."""
    display_name = "Add consumables to the location pool?"
    default = False

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict[str, Type[Option[Any]]]) -> dict[str, Type[Option[Any]]]:
#    options["goal"] = Goal
    options["include_irenicus_dungeon"] = IncludeIrenicusDungeon
    options["pay_gaelan_bayle"] = PayGaelanBayle    
    options["include_enhanced_edition"] = IncludeEnhancedEdition    
    options["include_chapter4"] = IncludeC4    
    options["include_city_of_caverns"] = IncludeCoC
    options["include_chapter5"] = IncludeC5
    options["include_chapter6"] = IncludeC6
    options["include_chapter7"] = IncludeC7
#    options["chapters_to_include"] = ChaptersToInclude
#    options["include_equipment"] = Equipment
    options["include_equipment"] = IncludeEquipment
    options["include_collectors_edition"] = IncludeCollectorsEdition
    options["include_companion_quests"] = IncludeCompanionQuests
    options["include_npcs"] = IncludeNPCs
    options["loot_checks_by_lootable"] = LootChecks
    options["loot_checks_by_room"] = LootChecksLite
    options["forging_checks"] = ForgingChecks
    options["progressive_equipment"] = ProgressiveEquipment
    options["include_watchers_keep"] = IncludeWatchersKeep
    options["include_consumables"] = Consumables

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
