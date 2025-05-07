# Manual Randomizer Setup Guide

## Required Software

- The latest [version of Archipelago](https://github.com/ArchipelagoMW/Archipelago/releases) (not pre-release)
- Baldur's Gate 2: Shadows of Amn, classic or Enhanced Edition

## Installation Procedures

Install the latest Archipelago version from the link above. 
Install Baldur's Gate 2: Shadows of Amn. Classic or Enhanced Edition will work. Mods can be used, but modded content is not included in randomization at this time.
Download the apworld from this github's releases page.
Double-click the apworld to automatically install it into Archipelago's custom_worlds folder.
Open the Archipelago Launcher and click "Generate Template Options". A folder will open. Find the yaml file that corresponds to this game.
Open the yaml in a text editor and change options as needed.
Place the yaml, along with any other yamls to be included in the multiworld, into the "Players" subfolder in the Archipelago folder.
In the Archipelago launcher, click "Generate". If all goes well, the generator will create a zip in the "output" subfolder. This is your multiworld data.
Upload the zip to [Archipelago](archipelago.gg) for hosting, or set up a localhost.

## Joining a MultiWorld Game

In the Archipelago launcher, launch the manual client.
Use the dropdown next to Manual Game ID to choose what manual you are using.
Use the Server box to input your connection info. The format is Slotname:password@archipelago.gg:#####
where Slotname is the Player name you put in the yaml, password is the server password ("None" if the server doesn't have one), and ##### is the port. 
If everything is right, press Connect and you'll be connected.

## Multiplayer Manual

Open the Manual tab of the Manual Client. On the left is a list of items you've received, and on the right are all the game's location checks.
Checks that are logically available are highlighted green.
When you've completed a check, click it to send it to the server as complete.
When you've achieved the victory condition, click the Victory!! button to mark the world as complete.

## Game Troubleshooting

Needs content.