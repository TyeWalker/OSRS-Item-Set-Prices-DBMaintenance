# OSRS-Item-Set-Prices-DBMaintenance

OSRS Item Set Prices App created using Python(3), Flask, and Bootstrap (HTML/CSS + javascript). This programme is designed to track the prices and margin of 
popular item sets. Latest prices update every 2 minutes, one hour volume updates every 55 minutes, and one day volume updates every 24 hours.

Currently it tracks the following item sets:
* Barrows
* Gold-trimmed standard metal (lg)
* Gold-trimmed standard metal (sk)
* Trimmed standard metal (lg)
* Trimmed standard metal (sk)
* God-blessed dragonhide

Before using this programme, please make sure you have Python 3 installed and then set the user agent in **MaintainLatest.py, MaintainVolume.py,** and **OnLaunch.py** 
to your discord username. See [HERE](https://oldschool.runescape.wiki/w/RuneScape:Real-time_Prices#Please_set_a_descriptive_User-Agent!) 
for more info about user agents.

To start using this programme, you will have to import the database into WAMP/XAMP. Simply go into the database folder in root of this project and import osrsprices.sql into WAMP.
Then navigate to the root of the programme in your cmd and run main.py. Then head to the [Flask App](https://github.com/TyeWalker/OSRS-Item-Set-Prices-FlaskApp) and 
download the repository. Setting up the app is explained in the README for that project.
  
_**Please Note:**_
*For the graph to be accurate, the programme will need to run continously, as it constantly fetches the prices from the OSRS wiki API.*
