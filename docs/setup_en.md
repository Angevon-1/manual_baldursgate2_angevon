# Manual Randomizer Setup Guide

## Required Software

- The latest [version of Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases) (not pre-release)
- Baldur's Gate 2: Shadows of Amn, classic or Enhanced Edition. The PC version is recommended, but there is support for console releases as well.
- The latest BG2 apworld from this github's releases page. (NONE YET)
- (optional) The latest version of the [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases) apworld.

## Installation Procedures

1. Install the latest Archipelago version from the link above. 
2. Install Baldur's Gate 2: Shadows of Amn. Classic or Enhanced Edition will work. Mods can be used, but modded content is not included in randomization at this time.
3. Download the apworld from this github's releases page. (NONE YET)
4. Double-click the apworld to automatically install it into Archipelago's custom_worlds folder.
5. (optional) Download and then double-click the tracker.apworld from the Universal Tracker link.
6. Open the Archipelago Launcher and click "Generate Template Options". A folder will open. Find the yaml file that corresponds to this game.
7. Open the yaml in a text editor and change options as needed.
8. Place the yaml, along with any other yamls to be included in the multiworld, into the "Players" subfolder in the Archipelago folder.
9. In the Archipelago launcher, click "Generate". If all goes well, the generator will create a zip in the "output" subfolder. This is your multiworld data.
10. Upload the zip to [Archipelago](https://archipelago.gg/uploads) for hosting, or set up a localhost.

## Joining a MultiWorld Game

1. In the Archipelago launcher, launch the Manual Client.
2. Use the dropdown next to Manual Game ID to choose what manual you are using.
3. Use the Server box to input your connection info. The format is Slotname:<span>password</span>@archipelago.gg:#####
where Slotname is the Player name you put in the yaml, password is the server password ("None" if the server doesn't have one), and ##### is the port. If you're using a localhost, use "localhost" instead of archipelago.gg. In this case, ##### is your localhost port.
4. If everything is right, press Connect and you'll be connected.

## Tracking your items and locations

1. Open the Manual tab of the Manual Client. On the left is a list of items you've received, and on the right are all the game's location checks.
2. Checks that are logically available are highlighted green if Universal Tracker is installed.
3. When you've completed a check, click it to send it to the server as complete.
4. When you've achieved the goal condition, click the GOAL button to mark the world as complete.

## Game Troubleshooting

See the [faq](faq.md) for common questions related to this manual. You are also welcome to open issues on this github or contact me (Angevon) in the Discord thread on the manual Discord server.