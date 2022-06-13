# CATS (Carrier Advanced Traversal System)
CATS is a flight computer to help guide your Fleet Carrier in Elite Dangerous
across many thousands of light years automatically.

It does this by navigating the Carrier menu and selecting the destination,
as well as restocking the depot with Tritium after every jump.

## Features
- Automatic jump plotting
- Tritium restocking
- Route time estimations
- Keeps track of jump time (in case a jump is longer than 15 minutes)
- Discord integration

## Installation
The script requires Python 3.9 to be installed.
The required Python modules can be installed by running:

``pip install -r requirements.txt``

in the directory of the downloaded files.

Tesseract also needs to be installed in order to read the jump time.
Here's an installation guide: 
https://medium.com/quantrium-tech/installing-and-using-tesseract-4-on-windows-10-4f7930313f82

(Note: if ``tesseract --version`` doesn't work on the command line after setting the environment variable, try rebooting your PC.)

## Setup
Run ``python main.py`` in the directory of the downloaded files. It should create a settings file, which you should edit before running again.

### The settings file
- ``webhook_url``: The webhook URL for Discord integration. Google "discord webhook" if you don't know what that means.
- ``journal_directory``: The directory that contains your Elite Dangerous journal files. Normally 
``C:/Users/[Your username]/Saved Games/Frontier Developments/Elite Dangerous/``.
Make sure you use forward slashes, and a slash at the end. If there are any spaces, keep them in there, don't use quotes.
- ``tritium_slot``: How many up presses are required to reach tritium in your carrier's cargo hold from the transfer menu.
Please note - this is different depending if there's already tritium in your ship's cargo hold or not. Please put at least 1t of tritium in your ship's cargo hold before measuring this.
- ``route_file``: e.g ``route.txt``. Put a file with this name in the same directory, containing a list of systems in order you want the carrier to jump to.
Make sure this file doesn't have any leading or trailing blank lines, and that all the systems are valid.

### The photos file
This contains links to photos that can be used by the Discord embed - one will be selected randomly when any message is sent.
By default, it contains pictures of my carrier (Satellite Five). Change to pictures of your own carrier, or anything else, if you want.