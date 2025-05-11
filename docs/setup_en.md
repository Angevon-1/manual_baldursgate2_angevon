# Manual Randomizer Setup Guide

## Required Software

- The latest [version of Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases) (not pre-release)
- Baldur's Gate 2: Shadows of Amn, classic or Enhanced Edition
- The latest BG2 apworld from this github's releases page. (NONE YET)
- (optional) The latest version of the [Universal Tracker](https://github.com/FarisTheAncient/Archipelago/releases) apworld.

## Installation Procedures

Install the latest Archipelago version from the link above. <br/>
Install Baldur's Gate 2: Shadows of Amn. Classic or Enhanced Edition will work. Mods can be used, but modded content is not included in randomization at this time.<br/>
Download the apworld from this github's releases page.<br/>
Double-click the apworld to automatically install it into Archipelago's custom_worlds folder.<br/>
(optional) Download and then double-click the tracker.apworld from the Universal Tracker link.<br/>
Open the Archipelago Launcher and click "Generate Template Options". A folder will open. Find the yaml file that corresponds to this game.<br/>
Open the yaml in a text editor and change options as needed.<br/>
Place the yaml, along with any other yamls to be included in the multiworld, into the "Players" subfolder in the Archipelago folder.<br/>
In the Archipelago launcher, click "Generate". If all goes well, the generator will create a zip in the "output" subfolder. This is your multiworld data.<br/>
Upload the zip to [Archipelago](https://archipelago.gg/uploads) for hosting, or set up a localhost.

## Joining a MultiWorld Game

In the Archipelago launcher, launch the Manual Client.<br/>
Use the dropdown next to Manual Game ID to choose what manual you are using.<br/>
Use the Server box to input your connection info. The format is Slotname:password@archipelago.gg:#####<br/>
where Slotname is the Player name you put in the yaml, password is the server password ("None" if the server doesn't have one), and ##### is the port. <br/>
If everything is right, press Connect and you'll be connected.

## Multiplayer Manual

Open the Manual tab of the Manual Client. On the left is a list of items you've received, and on the right are all the game's location checks.<br/>
Checks that are logically available are highlighted green if Universal Tracker is installed.<br/>
When you've completed a check, click it to send it to the server as complete.<br/>
When you've achieved the goal condition, click the GOAL button to mark the world as complete.

## Game Troubleshooting

Needs content.