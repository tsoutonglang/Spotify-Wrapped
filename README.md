# Spotify Data Analysis
Analyzes your Spotify listening data collected through IFTTTT and stored in Google Sheets
<br>
<br>
<b>WARNING!</b> I have no idea how to stop IFTTTT from logging all of my data into Google Sheets. If you don't want it to log your songs forever, continue at your own risk. (Mine has been logging songs for literal years with no end in sight)

## Python Setup
1. Make sure you have [Python](https://www.geeksforgeeks.org/download-and-install-python-3-latest-version/) installed
2. Install `pandas`: run `pip install pandas` in the terminal. Extra information can be found [here](https://www.geeksforgeeks.org/how-to-install-python-pandas-on-windows-and-linux/)

## IFTTTT Workflow: Setting It Up
1. You will need [this IFTTTT applet](https://ifttt.com/applets/nin7BxVm-keep-a-log-of-your-recently-played-tracks) and connect it to an account with Google Sheets
2. Wait for your data to roll in as you listen to songs!
3. Add a row at the very top with the following headers: "date" "song" "artist" for columns a, b, and c
4. After IFTTTT automatically makes a new spreadsheet or at the end of the year, download the spreadsheet as a .csv file.
6. Run the code! Feel free to customize it for yourself, I usually run this at the end of each month to see my monthly round-up and other cool data facts.

## Credits and Information
This repository would not be possible without the original code from [Liz Stippell](https://github.com/liz-stippell/spotify_data), IFTTTT, Google Sheets.