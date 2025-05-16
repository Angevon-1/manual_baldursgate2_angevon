<b>This readme expects you to have knowledge of both Archipelago and Manual.<br/>If you don't, please see [the Archipelago readme](Archipelago_README.md) first!</b>

Baldur's Gate 2: Shadows of Amn is a classic isometric-style RPG with a cast of memorable characters in the Forgotten Realms setting. It is among the handful of BioWare games that started the genre of “real-time with pause” combat mechanics later seen in Dragon Age. 

Conveniently, BG2 has randomizers available, and an extensive, easy to use cheat console. Depending on how you'd like to play, this manual may require use of the cheat console and/or save editing. The randomizers, however, are optional.

<u>Ways to play this manual:</u><br/>
<ul><li>Cheat console or save editing method. Items in the multiworld are actual items. Use the cheat console or save editing to give yourself the item in game when you’ve received it. In this mode, you’re not supposed to pick up any magical or key items you find in the game. You’re supposed to receive them from the multiworld only. As a result, item randomizer has no effect and shouldn't be used. This is the mode the manual is intended to be played with since the multiworld does the randomizing for you.</li>
<li>No cheat console or save editing method. Items in the multiworld are simply unlocks. When you receive an item from the multiworld, it’s actually the unlock to be allowed to use the item. For example, when playing the game, you find the Namarra sword +2 from the random bandit encounter, as usual, but you can’t equip it until you’ve received the Namarra item from the multiworld. This mode works well with the item randomizer.</li>
<li>Free for all method. Same as the cheat console/save editing method, except you can pick up whatever you find too! This allows for duplicate items. Your mom lets you have two Carsomyr +5s??? This mode works well with item randomizer.</li>
</ul>

<u>Cheat console information:</u><br/>
There are two versions of the game: classic and Enhanced Edition. The steps to enable the cheat console depend on the version. Classic has been discontinued for sale on digital storefronts, but some may still have the CDs, so I'll include the instructions for completion's sake. Enhanced Edition is available on many digital storefronts. 

For classic:<br/>
Open the Baldur.ini file (located in the BG2 installation directory).
Find the line [Program Options] and add the text Debug Mode=1 underneath.
Save and close the file.

For Enhanced Edition:<br/>
Locate the folder at Documents > Baldur's Gate - Enhanced Edition. This is usually in  C:\users\ (username)\Documents but may be somewhere in your OneDrive. In a text editor, open the file Baldur.lua.
Add the line SetPrivateProfileString('Program Options','Debug Mode','1') to the file.
Save and close the file.

After loading your game save, press ctrl + spacebar at the same time to open the cheat console window at the bottom. It looks like a chat box. That's where cheat console commands will go.

Say you've received "Boots of Speed (boot01)" from the multiworld. The (boot01) is the item code. All items in this manual will have the item code in parenthesis like this. To receive it in game, you'll type the following into the cheat console. Again, the command will change based on version.

For classic, type the following command into the cheat console chat area:<br/>
CLUAConsole:CreateItem("boot01")<br/>
And then press enter to submit the command.

For enhanced, they've shortened the command to:<br/>
C:CreateItem("boot01")<br/>
And then press enter to submit the command.

The item will appear in the top character's inventory.

Alternatively, a save editor like <a href="https://sorcerers.net/Games/BG2/index_editors.php">Shadowkeeper</a> (classic) or <a href="https://sourceforge.net/projects/eekeeper/">EEKeeper</a> (enhanced) can be used to edit received items directly into your inventory.

<u>About this manual:</u><br/>
Items include:<br/>
Magical Equipment (e.g. Dagger +1, Helm of Balduran, Mail of the Dead +2)<br/>
Key items (e.g. keys, letters, the dryads’ acorns)<br/>
Forgeable equipment pieces<br/>
Location unlocks (e.g. Bridge District, Windspear Hills)<br/>
Gold (filler item)

Location checks are:<br/>
Defeating quest and location-specific enemies (e.g. defeating the Otyugh in Irenicus’s Dungeon)<br/>
Completing objectives<br/>
Meeting NPCs (e.g. meeting Yoshimo on floor 2 of Irenicus's Dungeon. Don't have to recruit, just meet)<br/>
Looting entire rooms, and/or crates/barrels/tables/etc (optional)

It’s up to you whether to wait until you receive an equipment before you can use it, or just go ahead and pick up everything and use it regardless. Key items should definitely be locked until you receive them, however, since that’s how the logic is intended to work.

The filler item is 100 Gold. The cheat console command to receive gold is:<br/>
Classic:<br/>
CLUAConsole:AddGold("100")<br/>
or<br/>
Enhanced Edition:<br/>
C:AddGold("100")

<u>The randomizers:</u><br/>
I've mentioned optional randomizers. There are two:<br/>
<a href="https://www.gibberlings3.net/mods/items/item_rand/">Item Randomizer</a> - randomizes monster drops, items in crates, etc. Does not affect quest items.<br/>
<a href="https://www.gibberlings3.net/mods/tweaks/enemy_randomizer/">Enemy randomizer</a> - as the name implies. Does not affect quest enemies. Enemy randomizer may make some check names for the manual more confusing, for example “Clear the Mephit room” may refer to a room that no longer contains Mephits.

Currently, only Irenicus's Dungeon has been implemented. There are plans to make Irenicus’s Dungeon optional so you can use Dungeon-B-Gone to skip it. If you leave Irenicus’s Dungeon too early and missed some checks, you can use the following command to return.<br/>
Classic:<br/>
CLUAConsole:MoveToArea('AR0602')<br/>
Enhanced Edition:<br/>
C:MoveToArea('AR602')

And to leave again, use the same command but 'AR0700' to return to Waukeen’s Promenade.

I'm still working out and testing how anything past chapter 2 will work, but it will probably involve using the cheat console to warp.