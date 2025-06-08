## Introduction
<b>This readme expects you to have knowledge of both Archipelago and Manual.<br/>If you don't, please see [the Archipelago readme](Archipelago_README.md) first!</b>

Baldur's Gate 2: Shadows of Amn currently does not have an Archipelago implementation. Since I don't have the programming knowledge to make that happen, this is a manual implementation instead.

Conveniently, BG2 has randomizers available, and an extensive, easy to use cheat console. Depending on how you'd like to play, this manual may require use of the cheat console and/or save editing. The randomizers, however, are optional.

## Ways to play this manual
<ul><li><u>Cheat console or save editing method.</u> Items in the multiworld are actual items. Use the cheat console or save editing to give yourself the item in game when you’ve received it. In this mode, you’re not supposed to pick up any magical or key items you find in the game. You’re supposed to receive them from the multiworld only. As a result, Item Randomizer has no effect and shouldn't be used. This is the mode the manual is intended to be played with; the multiworld does the randomizing for you.</li>
<li><u>No cheat console or save editing method.</u> Items in the multiworld are simply unlocks. When you receive an item from the multiworld, it’s actually the unlock to be allowed to use the item. For example, when playing the game, you find the Namarra sword +2 from the Crypt King, as usual, but you can’t equip it until you’ve received the Namarra item from the multiworld. This method works well with Item Randomizer. This method should be used if you are playing the console or mobile version of BG2 and cannot use the cheat console or save editors, or are simply not interested in using them.</li>
<li><u>Free for all method.</u> Same as the cheat console/save editing method, except you can pick up whatever magical equipment you find too! This allows for duplicate items. Your mom lets you have two Carsomyr +5s??? This mode works well with Item Randomizer.</li>
<li><u>Any method you like.</u> Take a look at the game's options in the yaml file and decide from there how you'd like to play yourself. Maybe it's a comination of the ideas above. There's no wrong answer!</li>
</ul>

## Cheat console information:
There are two versions of Baldur's Gate 2: classic and Enhanced Edition. The steps to enable the cheat console depend on the version. Classic has been discontinued for sale on digital storefronts, but some may still have the CDs, so I'll include the instructions for completion's sake. Enhanced Edition is available on many digital storefronts. 

For classic:<br/>
Open the Baldur.ini file (located in the BG2 installation directory).<br/>
Find the line [Program Options] and add the text Debug Mode=1 underneath.<br/>
Save and close the file.

For Enhanced Edition:<br/>
Locate the folder at Documents > Baldur's Gate - Enhanced Edition.<br/>
This is usually in  C:\users\ (username)\Documents but may be somewhere in your OneDrive.<br/>
In a text editor, open the file Baldur.lua.<br/>
Add the line SetPrivateProfileString('Program Options','Debug Mode','1') to the file.<br/>
Save and close the file.

After loading your game save, press ctrl + spacebar at the same time to open the cheat console window at the bottom. It looks like a chat box. That's where cheat console commands will go.

Say you've received "Boots of Speed (boot01)" from the multiworld. The (boot01) is the item code. All items in this manual will have the item code in parenthesis like this. To receive it in game, you'd type the following into the cheat console. Again, the command will change based on version.

For classic, type the following command into the cheat console chat area:<br/>
CLUAConsole:CreateItem("boot01")<br/>
And then press enter to submit the command.

For enhanced, they've shortened the command to:<br/>
C:CreateItem("boot01")<br/>
And then press enter to submit the command.

The item will appear in the first free inventory spot, starting with the first character in your party.

Alternatively, a save editor like <a href="https://sorcerers.net/Games/BG2/index_editors.php">Shadowkeeper</a> (classic) or <a href="https://sourceforge.net/projects/eekeeper/">EEKeeper</a> (enhanced) can be used to edit received items directly into your inventory.

## About this manual
Items distributed in the multiworld include:<br/>
Magical Equipment (e.g. Dagger +1, Helm of Balduran, Mail of the Dead +2) (optional)<br/>
Key items (e.g. keys, quest items like the dryads’ acorns)<br/>
Forgeable equipment pieces (optional)<br/>
Location unlocks (e.g. Bridge District, Windspear Hills)<br/>
Potions and scrolls (optional)<br/>
Gold (filler item)

Locations to check off in the Manual Client include:<br/>
Defeating quest and location-specific enemies (e.g. "Defeat the Otyugh in Irenicus’s Dungeon")<br/>
Completing objectives<br/>
Meeting NPCs (e.g. "Meet Jan in the Government District". Don't necessarily have to recruit, just meet)<br/>
Looting entire rooms, and/or crates/barrels/tables/etc (optional)

The manual-created generic filler item is 100 Gold. The cheat console command to receive gold is:<br/>
Classic:<br/>
CLUAConsole:AddGold("100")<br/>
or<br/>
Enhanced Edition:<br/>
C:AddGold("100")<br/>
If you're not using the cheat console, you can just ignore this item.

## The randomizers
There are two optional randomizers that may be used with the manual. These will only work with the PC version of BG2.<br/>
<a href="https://www.gibberlings3.net/mods/items/item_rand/">Item Randomizer</a> - randomizes monster drops, items in crates, etc. Does not affect quest items.<br/>
<a href="https://www.gibberlings3.net/mods/tweaks/enemy_randomizer/">Enemy randomizer</a> - as the name implies. Does not affect quest enemies. Enemy randomizer may make some check names for the manual more confusing, for example “Clear the Mephit room” may refer to a room that no longer contains Mephits. As a result, this is not recommended unless you have extensive knowledge of the original game.

## Options
Please see [the options list](optionslist.md) for information on the manual's different options. These are also described in the yaml file.