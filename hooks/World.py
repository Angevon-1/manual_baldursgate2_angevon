# Object classes from AP core, to represent an entire MultiWorld and this individual World that's part of it
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState, Item

# Object classes from Manual -- extending AP core -- representing items and locations that are used in generation
from ..Items import ManualItem
from ..Locations import ManualLocation

# Raw JSON data from the Manual apworld, respectively:
#          data/game.json, data/items.json, data/locations.json, data/regions.json
#
from ..Data import game_table, item_table, location_table, region_table

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value, format_state_prog_items_key, ProgItemsCat

# calling logging.info("message") anywhere below in this file will output the message to both console and log file
import logging

########################################################################################
## Order of method calls when the world generates:
##    1. create_regions - Creates regions and locations
##    2. create_items - Creates the item pool
##    3. set_rules - Creates rules for accessing regions and locations
##    4. generate_basic - Runs any post item pool options, like place item/category
##    5. pre_fill - Creates the victory location
##
## The create_item method is used by plando and start_inventory settings to create an item from an item name.
## The fill_slot_data method will be used to send data to the Manual client for later use, like deathlink.
########################################################################################



# Use this function to change the valid filler items to be created to replace item links or starting items.
# Default value is the `filler_item_name` from game.json
def hook_get_filler_item_name(world: World, multiworld: MultiWorld, player: int) -> str | bool:
    return False

# Called before regions and locations are created. Not clear why you'd want this, but it's here. Victory location is included, but Victory event is not placed yet.
def before_create_regions(world: World, multiworld: MultiWorld, player: int):

    #checking goal vs. final chapter option and setting the correct final chapter if neccesary
    goal = get_option_value(multiworld, player, "goal") # 6 = spellhold, 7 & 28 firkraag / kangaxx, 9 = irenicus, before that are the tokens
    final_chapter = get_option_value(multiworld, player, "final_chapter") #0 = c3, 1 = c4, 2 = c5, 3 = c6, 4 = c7
    include_city_of_caverns = get_option_value(multiworld, player, "include_city_of_caverns")
    companions = get_option_value(multiworld, player, "companions") 
    starting_companion_amount = get_option_value(multiworld, player, "starting_companion_amount") 
    if goal == 6:
        if final_chapter == 0:
            world.options.final_chapter.value = 1
        if include_city_of_caverns == 1:
            world.options.include_city_of_caverns.value = 0            
    if goal == 7:
        if final_chapter <= 3:
            world.options.final_chapter.value = 3
    if goal == 8:
        if final_chapter <= 3:
            world.options.final_chapter.value = 3
    if goal == 9:
        if final_chapter <= 4:
            world.options.final_chapter.value = 4
    #check for city of caverns being included but not setting a final chapter past 3, or spellhold goal, then change to disable city of caverns
    if include_city_of_caverns == 1:
        if final_chapter == 0:
            world.options.include_city_of_caverns.value = 0
    #check if companions are enabled, if not, set starting amount to 0
    if companions == 0 or companions == 3 or companions == 4:
        if starting_companion_amount >= 1:
            world.options.starting_companion_amount.value = 0
    else:
        pass

# Called after regions and locations are created, in case you want to see or modify that information. Victory location is included.
def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to remove locations from the world
    locationNamesToRemove: list[str] = [] # List of location names

    #setting option names with their results for ease of use
    include_irenicus_dungeon = get_option_value(multiworld, player, "include_irenicus_dungeon")
    gaelan_or_bodhi = get_option_value(multiworld, player, "gaelan_or_bodhi")
    include_city_of_caverns = get_option_value(multiworld, player, "include_city_of_caverns")
    final_chapter = get_option_value(multiworld, player, "final_chapter") #0 = c3, 1 = c4, 2 = c5, 3 = c6, 4 = c7
    loot_checks = get_option_value(multiworld, player, "loot_checks") #0 - none, 1 = by room, 2 = by container, 3 = both
    companions = get_option_value(multiworld, player, "companions") #0 none, 1 vanilla companions, 2 v + ee companions, 3 vanilla quests, 4 ee quests, 5 vanilla c & q, 6 all       
    starting_companion_amount = get_option_value(multiworld, player, "starting_companion_amount")   
    forging = get_option_value(multiworld, player, "forging_checks")

    # Add your code here to calculate which locations to remove
    if include_irenicus_dungeon == 0:
        locationNamesToRemove += world.location_name_groups["ID"]    
    if gaelan_or_bodhi == 1:
        locationNamesToRemove += world.location_name_groups["Shadow Thieves"]
    if gaelan_or_bodhi == 0:
        locationNamesToRemove += world.location_name_groups["Bodhi"]    
    if include_city_of_caverns == 0:
        locationNamesToRemove += world.location_name_groups["City of Caverns"]
    if final_chapter == 0:
        locationNamesToRemove += world.location_name_groups["Chapter 4"]
        locationNamesToRemove += world.location_name_groups["Chapter 5"]
        locationNamesToRemove += world.location_name_groups["Chapter 6"]
        locationNamesToRemove += world.location_name_groups["Chapter 7"]
    if final_chapter == 1:
        locationNamesToRemove += world.location_name_groups["Chapter 5"]
        locationNamesToRemove += world.location_name_groups["Chapter 6"]
        locationNamesToRemove += world.location_name_groups["Chapter 7"]
    if final_chapter == 2:
        locationNamesToRemove += world.location_name_groups["Chapter 6"]
        locationNamesToRemove += world.location_name_groups["Chapter 7"]
    if final_chapter == 3:
        locationNamesToRemove += world.location_name_groups["Chapter 7"]
    if companions <= 2:
        locationNamesToRemove += world.location_name_groups["Companion Quests"]
        locationNamesToRemove += world.location_name_groups["EE Companion Quests"]
    if companions == 3 or companions == 5:
        locationNamesToRemove += world.location_name_groups["EE Companion Quests"]
    if loot_checks == 0:
        locationNamesToRemove += world.location_name_groups["Loot"]
        locationNamesToRemove += world.location_name_groups["LootLite"]
    if loot_checks == 1:
        locationNamesToRemove += world.location_name_groups["Loot"]
    if loot_checks == 2:
        locationNamesToRemove += world.location_name_groups["LootLite"]
    if forging == 0:
        locationNamesToRemove += world.location_name_groups["Forging"]

    #starting companion locations
    if starting_companion_amount < 5:
        locationNamesToRemove.append("Starting Companion 5")
        if starting_companion_amount < 4:
            locationNamesToRemove.append("Starting Companion 4")
            if starting_companion_amount < 3:
                locationNamesToRemove.append("Starting Companion 3")
                if starting_companion_amount < 2:
                    locationNamesToRemove.append("Starting Companion 2")
                    if starting_companion_amount < 1:
                        locationNamesToRemove.append("Starting Companion 1")

    #remove the calculated locations
    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name in locationNamesToRemove:
                    region.locations.remove(location)        
    if hasattr(multiworld, "clear_location_cache"):
        multiworld.clear_location_cache()

# This hook allows you to access the item names & counts before the items are created. Use this to increase/decrease the amount of a specific item in the pool
# Valid item_config key/values:
# {"Item Name": 5} <- This will create qty 5 items using all the default settings
# {"Item Name": {"useful": 7}} <- This will create qty 7 items and force them to be classified as useful
# {"Item Name": {"progression": 2, "useful": 1}} <- This will create 3 items, with 2 classified as progression and 1 as useful
# {"Item Name": {0b0110: 5}} <- If you know the special flag for the item classes, you can also define non-standard options. This setup
#       will create 5 items that are the "useful trap" class
# {"Item Name": {ItemClassification.useful: 5}} <- You can also use the classification directly
def before_create_items_all(item_config: dict[str, int|dict], world: World, multiworld: MultiWorld, player: int) -> dict[str, int|dict]:
    return item_config

# The item pool before starting items are processed, in case you want to see the raw item pool at that stage
def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    itemNamesToRemove = []
    
    include_irenicus_dungeon = get_option_value(multiworld, player, "include_irenicus_dungeon")
    gaelan_or_bodhi = get_option_value(multiworld, player, "gaelan_or_bodhi")
    include_watchers_keep = get_option_value(multiworld, player, "include_watchers_keep")
    include_city_of_caverns = get_option_value(multiworld, player, "include_city_of_caverns")
    final_chapter = get_option_value(multiworld, player, "final_chapter") #0 = c3, 1 = c4, 2 = c5, 3 = c6, 4 = c7
    equipment = get_option_value(multiworld, player, "equipment") #0 - no equips, 1 = base game magical eq, 2 = base game magical eq + ce, 3 = base and ee, 4 all
    misc_items = get_option_value(multiworld, player, "misc_items") #0 - no misc., 1 = base game, 2 = base game + ce, 3 = base game + ee, 4 = all
    progressive_equipment = get_option_value(multiworld, player, "progressive_equipment") # toggle
    loot_checks = get_option_value(multiworld, player, "loot_checks") #0 - none, 1 = by room, 2 = by container, 3 = both
    forging = get_option_value(multiworld, player, "forging_checks")
    companions = get_option_value(multiworld, player, "companions") #0 none, 1 vanilla companions, 2 v + ee companions, 3 vanilla quests, 4 v & ee quests, 5 vanilla c & q, 6 all       
    
    if include_irenicus_dungeon == 0:
        itemNamesToRemove += [item.name for item in item_pool if "ID" in world.item_name_to_item[item.name].get("category", [])]
    if gaelan_or_bodhi == 1:
        itemNamesToRemove += [item.name for item in item_pool if "Shadow Thieves" in world.item_name_to_item[item.name].get("category", [])]
    if gaelan_or_bodhi == 0:
        itemNamesToRemove += [item.name for item in item_pool if "Bodhi" in world.item_name_to_item[item.name].get("category", [])]
    if companions == 0 or companions == 3:
        itemNamesToRemove += [item.name for item in item_pool if "EE Areas" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "EE Companions" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "NPCs" in world.item_name_to_item[item.name].get("category", [])]
    if companions == 1:
        itemNamesToRemove += [item.name for item in item_pool if "EE Companions" in world.item_name_to_item[item.name].get("category", [])] 
        itemNamesToRemove += [item.name for item in item_pool if "EE Areas" in world.item_name_to_item[item.name].get("category", [])]
    if companions == 2:
        itemNamesToRemove += [item.name for item in item_pool if "EE Areas" in world.item_name_to_item[item.name].get("category", [])]
    if companions == 4:
        itemNamesToRemove += [item.name for item in item_pool if "NPCs" in world.item_name_to_item[item.name].get("category", [])] 
        itemNamesToRemove += [item.name for item in item_pool if "EE Companions" in world.item_name_to_item[item.name].get("category", [])] 
    if companions == 5:
        itemNamesToRemove += [item.name for item in item_pool if "EE Companions" in world.item_name_to_item[item.name].get("category", [])] 
        itemNamesToRemove += [item.name for item in item_pool if "EE Areas" in world.item_name_to_item[item.name].get("category", [])]          
    if include_watchers_keep == 0:
        itemNamesToRemove += [item.name for item in item_pool if "Watcher's Keep" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "Watcher's Keep Equipment" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "Watcher's Keep Misc." in world.item_name_to_item[item.name].get("category", [])]
    if include_city_of_caverns == 0:
        itemNamesToRemove += [item.name for item in item_pool if "City of Caverns" in world.item_name_to_item[item.name].get("category", [])]      
    if final_chapter == 0:        
        itemNamesToRemove += [item.name for item in item_pool if "Key Items - Chapter 4" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "Chapter 4 Token" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "Key Items - Chapter 5" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "Chapter 4" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "Chapter 5" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "Chapter 5 Token" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "Chapter 6 Token" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "Key Items - Chapter 7" in world.item_name_to_item[item.name].get("category", [])]
    if final_chapter == 1:
        itemNamesToRemove += [item.name for item in item_pool if "Key Items - Chapter 5" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "Chapter 5" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "Chapter 5 Token" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "Chapter 6 Token" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "Key Items - Chapter 7" in world.item_name_to_item[item.name].get("category", [])]
    if final_chapter == 2:
        itemNamesToRemove += [item.name for item in item_pool if "Key Items - Chapter 7" in world.item_name_to_item[item.name].get("category", [])]
    if final_chapter == 3:
        itemNamesToRemove += [item.name for item in item_pool if "Key Items - Chapter 7" in world.item_name_to_item[item.name].get("category", [])]
    if equipment == 0:
        itemNamesToRemove += [item.name for item in item_pool if "Magical Equipment" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "Collector's Edition Equipment" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "EE Equipment" in world.item_name_to_item[item.name].get("category", [])]
    if equipment == 1:
        itemNamesToRemove += [item.name for item in item_pool if "Collector's Edition Equipment" in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "EE Equipment" in world.item_name_to_item[item.name].get("category", [])]
    if equipment == 2:
        itemNamesToRemove += [item.name for item in item_pool if "EE Equipment" in world.item_name_to_item[item.name].get("category", [])]
    if equipment == 3:
        itemNamesToRemove += [item.name for item in item_pool if "Collector's Edition Equipment" in world.item_name_to_item[item.name].get("category", [])]    
    if misc_items == 0:
        itemNamesToRemove += [item.name for item in item_pool if "Misc." in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "Collector's Edition Misc." in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "EE Misc." in world.item_name_to_item[item.name].get("category", [])]
    if misc_items == 1:
        itemNamesToRemove += [item.name for item in item_pool if "Collector's Edition Misc." in world.item_name_to_item[item.name].get("category", [])]
        itemNamesToRemove += [item.name for item in item_pool if "EE Misc." in world.item_name_to_item[item.name].get("category", [])]
    if misc_items == 2:
        itemNamesToRemove += [item.name for item in item_pool if "EE Misc." in world.item_name_to_item[item.name].get("category", [])]
    if misc_items == 3:
        itemNamesToRemove += [item.name for item in item_pool if "Collector's Edition Misc." in world.item_name_to_item[item.name].get("category", [])]
    if progressive_equipment == 0:
        itemNamesToRemove += [item.name for item in item_pool if "Progressive Equipment" in world.item_name_to_item[item.name].get("category", [])]
    if loot_checks <= 1:
        itemNamesToRemove += [item.name for item in item_pool if "Consumables" in world.item_name_to_item[item.name].get("category", [])]
    if forging == 0:
        itemNamesToRemove += [item.name for item in item_pool if "Forging Items" in world.item_name_to_item[item.name].get("category", [])]

    
    for itemName in itemNamesToRemove:
        item = next(i for i in item_pool if i.name == itemName)
        item_pool.remove(item)

    return item_pool

# The item pool after starting items are processed but before filler is added, in case you want to see the raw item pool at that stage
def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    # Use this hook to remove items from the item pool
    itemNamesToRemove: list[str] = [] # List of item names

    # Add your code here to calculate which items to remove.
    #
    # Because multiple copies of an item can exist, you need to add an item name
    # to the list multiple times if you want to remove multiple copies of it.

    for itemName in itemNamesToRemove:
        item = next(i for i in item_pool if i.name == itemName)
        item_pool.remove(item)

    return item_pool

    # Some other useful hook options:

    ## Place an item at a specific location
    # location = next(l for l in multiworld.get_unfilled_locations(player=player) if l.name == "Location Name")
    # item_to_place = next(i for i in item_pool if i.name == "Item Name")
    # location.place_locked_item(item_to_place)
    # item_pool.remove(item_to_place)

# The complete item pool prior to being set for generation is provided here, in case you want to make changes to it
def after_create_items(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# Called before rules for accessing regions and locations are created. Not clear why you'd want this, but it's here.
def before_set_rules(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after rules for accessing regions and locations are created, in case you want to see or modify that information.
def after_set_rules(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to modify the access rules for a given location

    def Example_Rule(state: CollectionState) -> bool:
        # Calculated rules take a CollectionState object and return a boolean
        # True if the player can access the location
        # CollectionState is defined in BaseClasses
        return True

    ## Common functions:
    # location = world.get_location(location_name, player)
    # location.access_rule = Example_Rule

    ## Combine rules:
    # old_rule = location.access_rule
    # location.access_rule = lambda state: old_rule(state) and Example_Rule(state)
    # OR
    # location.access_rule = lambda state: old_rule(state) or Example_Rule(state)

# The item name to create is provided before the item is created, in case you want to make changes to it
def before_create_item(item_name: str, world: World, multiworld: MultiWorld, player: int) -> str:
    return item_name

# The item that was created is provided after creation, in case you want to modify the item
def after_create_item(item: ManualItem, world: World, multiworld: MultiWorld, player: int) -> ManualItem:
    return item

# This method is run towards the end of pre-generation, before the place_item options have been handled and before AP generation occurs
def before_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This method is run at the very end of pre-generation, once the place_item options have been handled and before AP generation occurs
def after_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This method is run every time an item is added to the state, can be used to modify the value of an item.
# IMPORTANT! Any changes made in this hook must be cancelled/undone in after_remove_item
def after_collect_item(world: World, state: CollectionState, Changed: bool, item: Item):
    # the following let you add to the Potato Item Value count
    # if item.name == "Cooked Potato":
    #     state.prog_items[item.player][format_state_prog_items_key(ProgItemsCat.VALUE, "Potato")] += 1
    pass

# This method is run every time an item is removed from the state, can be used to modify the value of an item.
# IMPORTANT! Any changes made in this hook must be first done in after_collect_item
def after_remove_item(world: World, state: CollectionState, Changed: bool, item: Item):
    # the following let you undo the addition to the Potato Item Value count
    # if item.name == "Cooked Potato":
    #     state.prog_items[item.player][format_state_prog_items_key(ProgItemsCat.VALUE, "Potato")] -= 1
    pass


# This is called before slot data is set and provides an empty dict ({}), in case you want to modify it before Manual does
def before_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called after slot data is set and provides the slot data at the time, in case you want to check and modify it after Manual is done with it
def after_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called right at the end, in case you want to write stuff to the spoiler log
def before_write_spoiler(world: World, multiworld: MultiWorld, spoiler_handle) -> None:
    pass

# This is called when you want to add information to the hint text
def before_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:

    ### Example way to use this hook:
    # if player not in hint_data:
    #     hint_data.update({player: {}})
    # for location in multiworld.get_locations(player):
    #     if not location.address:
    #         continue
    #
    #     use this section to calculate the hint string
    #
    #     hint_data[player][location.address] = hint_string

    pass

def after_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:
    pass
