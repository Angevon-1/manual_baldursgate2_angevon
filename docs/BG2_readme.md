<b>This readme expects you to have knowledge of both Archipelago and Manual. If you don't, please see [the Archipelago readme](Archipelago_README.md) first!</b>

Baldur's Gate 2: Shadows of Amn is a classic isometric-style RPG with a cast of memorable characters in the Forgotten Realms setting. It is among the handful of BioWare games that started the genre of “real-time with pause” combat mechanics later seen in Dragon Age. 

Conveniently, BG2 has randomizers available, and an extensive, easy to use cheat console. This manual will require use of the cheat console and/or save editing, but the randomizers are optional.

There are two versions of the game: classic and Enhanced Edition. The steps to enable the cheat console depend on the version. Classic has been discontinued for sale on digital storefronts, but some may still have the CDs, so I'll include the instructions for completion's sake. Enhanced Edition is available on many digital storefronts. 

<u>For classic:</u><br/>
Open the Baldur.ini file (located in the BG2 installation directory).
Find the line [Program Options] and add the text Debug Mode=1 underneath.
Save and close the file.

<u>For Enhanced Edition:</u><br/>
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