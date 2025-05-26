## Below is a list of yaml options for the manual

## enhanced_edition
Set this to true if you’re playing the enhanced edition. This will include enhanced edition items and locations.<br>
Default: true

## enable_companion_quests
When this is true, items & locations related to all the NPC companions's quests are added to the multiworld.<br>

You must not kill any potential party members! Don't let any die before you’ve done their checks!<br>

Alternatively if you do kill someone / let someone die, the cheat console command CreateCreature may be able to bring them back. Codelist is here:<br>
https://gamefaqs.gamespot.com/pc/258273-baldurs-gate-ii-shadows-of-amn/faqs/11646<br>
The number after the NPCs name is their level. The list does not include EE NPCs. <br>
Default: true

## skip_irenicus_dungeon
Enable this if you want to skip all of Irenicus’s Dungeon. It will remove all Irenicus Dungeon-specific items and locations from the multiworld (Equipment like the Sword of Chaos and Key Items used outside of the dungeon like the dryad acorns are not affected). It is expected that you’re using [Dungeon-Be-Gone](https://www.pocketplane.net/dungeon-be-gone/) so that you’re given the dungeon's goodies before leaving (important if you’re playing in unlock mode or not using the cheat console/save editor).<br>
Default: false

## include_npcs
This adds the recruitable party member NPCs as unlockables in the item list. You will automatically be given 3 NPCs at random in the starting inventory. If you want to guarantee specific NPCs in your team, please make use of [start_inventory](https://archipelago.gg/tutorial/Archipelago/advanced_settings/en) or [plando](https://archipelago.gg/tutorial/Archipelago/plando/en).<br>

Note: mod npcs are not included at this time, but I’m open to requests.<br>

You can use the CreateCreature console command to immediately recruit the NPCs, or simply go find them in their vanilla locations in the game and recruit them from there. However, you’ll also need the region unlocks, and in some cases like Edwin, relevant quest items/progress.<br>

When used in conjunction with enable_companion_quests, this option adds more logical access rules based on your available NPCs. You won’t be expected to complete a companion quest until you have received the corresponding NPC. Without this option, companion quests are instead locked by the region unlocks where the companion exists and where the quests take place.<br>
Default: false

## include_multiple_strongholds
When this option is true, checks and items related to [b]all[/b] the available class strongholds will be added. This requires either the multiple strongholds setting from the BGTweaks mod, or save editing to temporarily change your PC’s class in order to start each stronghold quest. Strongholds are generally considered tedious busywork by the BG community, but this option will add more checks.<br>

If you’re not using a mod, this is the cheat console command to reset the stronghold start quest:
CLUAConsole:SetGlobal("PlayerHasStronghold","GLOBAL",0)<br>
or C:SetGlobal("PlayerHasStronghold","GLOBAL",0) for enhanced edition<br>
Or find the global in a save editor and change it to 0.<br>

Then change your pc’s class (how?) and talk to the relevant stronghold NPC. Once started, the stronghold quests will continue even if you change class after and reset the global. In fact, you’ll have to reset the global each time you want to start a new stronghold.<br>

When false, no checks or items related to any strongholds are added.<br>
Default: false

## progressive_equipment
When this is true, equipment is progressive. You can’t use +x weapons until you’ve received the same number of progressives for that weapon type.<br>
For example, the Namarra short sword is a +2 short sword. You’ll need two “Progressive Short Sword” items in order to be able to use it.<br>
This option makes the game more balanced since you won’t be able to receive a Carsomyr +5 from the multiworld; you’ll have to find it in game and receive 5 “Progressive Two Handed Sword” items to use it. <br>
When this is true, all equipment in the game is replaced by the progressive system and you’ll need to find items in the game. This option works well with Item Randomizer. <br>
Default: false

## loot_checks
Set this to true if you want a bunch of individual lootable crates/barrels/chests added to the pool as location checks.<br>
To compensate for check count, this will also add a bunch of filler potions and scrolls to the item list.<br>
Note that your Lockpicking ability is NOT accounted for at this time. Progression may be locked behind a locked chest and it's up to you to get past it.<br>
Default: false

## loot_checks_lite
Set this to true if instead of EVERY lootable as a check, you'd rather have 'loot x room' as checks.
This is more balanced than full loot_checks and easier to track. Lockpicking ability is not required.<br>
This is the recommended loot setting.<br>
Default: true