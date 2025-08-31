## Introduction
<b>This readme expects you to have knowledge of both Archipelago and Manual.<br/>If you don't, please see [the Archipelago readme](Archipelago_README.md) first!</b>

Baldur's Gate 2: Shadows of Amn currently does not have an Archipelago implementation. Since I don't have the programming knowledge to make that happen, this is a manual implementation instead.

Conveniently, BG2 has randomizers available, and an extensive, easy to use cheat console. This manual will require use of the cheat console and/or save editing and/or the GO_AP BG2 mod that I've made. The randomizers, however, are optional.

## How to Install
See [setup_en](docs/setup_en.md) for instructions.

## About this manual
<u>Items distributed in the multiworld include:</u><br/>
Key items (e.g. keys, quest items like the dryads’ acorns)<br/>
Area unlocks (e.g. Bridge District, Windspear Hills)<br/>
Companion characters (e.g. Minsc) (optional)<br/>
Magical Equipment (e.g. Dagger +1, Helm of Balduran, Mail of the Dead +2) (optional)<br/>
Forgeable equipment pieces (e.g. Pommel Jewel of the Equalizer) (optional)<br/>
Potions and scrolls (optional)<br/>
Gold (filler item)

<u>Locations to check off in the Manual Client include:</u><br/>
Defeating specific enemies (e.g. "Defeat the Otyugh in Irenicus’s Dungeon")<br/>
Completing objectives (e.g. "Free Minsc from the cell")<br/>
Meeting NPCs (e.g. "Meet Jan in the Government District". Don't necessarily have to recruit, just meet)<br/>
Looting rooms or areas, and/or crates/barrels/tables/etc (optional)

The generic filler item is 100 Gold.

## Ways to play this manual
<ul><li><u>Items received from the multiworld are actual items.</u> Use the cheat console/save editing/GO_AP mod to give yourself the item in game when you’ve received it. In this mode, you’re not supposed to pick up any magical or key items you find in the game. You’re supposed to receive them from the multiworld only. As a result, Item Randomizer has no effect and shouldn't be used. This is the mode the manual is intended to be played with; the multiworld does the randomizing for you. This method works best with the "equipment" yaml option.</li>
<li><u>Items received from the multiworld are simply unlocks.</u> When you receive an item from the multiworld, it’s actually the unlock to be allowed to use the item. For example, when playing the game, you find the Namarra sword +2 from the Crypt King, as usual, but you can’t equip it until you’ve received the Namarra item from the multiworld, and/or enough Progressive Short Sword items. This method works well with Item Randomizer and the "progressive_equipment" yaml option.</li>
<li><u>Free for all method.</u> Same as the first method, except you can pick up whatever magical equipment you find too! This allows for duplicate items. This mode is also compatible with Item Randomizer.</li>
<li><u>Any method you like.</u> Take a look at the game's options in the yaml file and decide from there how you'd like to play yourself. Maybe it's a combination of the ideas above. There's no wrong answer!</li>
</ul>

## The randomizers
There are two optional randomizers that may be used with the manual.<br/>
<a href="https://www.gibberlings3.net/mods/items/item_rand/">Item Randomizer</a> - randomizes monster drops, items in crates, etc. Does not affect quest items.<br/>
<a href="https://www.gibberlings3.net/mods/tweaks/enemy_randomizer/">Enemy randomizer</a> - as the name implies. Does not affect quest enemies. Enemy randomizer may make some check names for the manual more confusing, for example “Clear the Mephit room” may refer to a room that no longer contains Mephits. As a result, this randomizer is not recommended unless you have extensive knowledge of the original game.

## Cheat console information:
There are two versions of Baldur's Gate 2: classic and Enhanced Edition. The steps to enable the cheat console depend on the version. Classic has been discontinued for sale on digital storefronts, but I'll include the instructions for completion's sake. Enhanced Edition is available on many digital storefronts. 

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

The item will appear in the first free inventory spot, starting with the first character in your party.<br/>

You can also teleport to new maps with the following command:<br/>
CLUAConsole:MovetoArea('AR0602')<br/>
or C:MovetoArea('AR0602') for enhanced edition. In this example 'AR0602' is the area code for Irenicus's Dungeon. Change it to the proper area code for where you want to go. See <a href="https://gibberlings3.github.io/iesdp/appendices/area_lists/bg2aref.htm">here</a> for a list. The area code is also in the area unlock item name when you receive it in the Manual Client.<br/>

<b>IMPORTANT: Do not go to a chapter you haven't reached yet!</b> (e.g. don't go to Brynnlaw when you're still in chapter 2). It may cause quest bugs! The manual will expect you to complete chapters before moving on. You might receive an area unlock for a later chapter before you complete your current chapter, that's just how randomizers are, but you won't be expected to go there until you've completed the previous chapters.

The cheat console command to receive 100 gold is:<br/>
Classic:<br/>
CLUAConsole:AddGold("100")<br/>
or C:AddGold("100") for enhanced edition. Change the 100 to whatever gold amount.

## Save Editors

Instead of using the cheat console, a save editor like <a href="https://sorcerers.net/Games/BG2/index_editors.php">Shadowkeeper</a> (classic) or <a href="https://sourceforge.net/projects/eekeeper/">EEKeeper</a> (enhanced) can be used to edit received items directly into your inventory. Save editors don't have a teleport option so you'll still need the cheat console or GO_AP mod to teleport.

## GO_AP Mod Information
To reduce the amount of cheat console and save editing, I made a mod for the game. The mod adds an item to Ribald's store. When you right-click -> Converse with the item, it opens a convenient dialogue tree you can use instead. You can teleport and receive items.<br/>

This mod does NOT interface with Archipelago at all. You still need to keep track of what you've received in the Manual Client.

