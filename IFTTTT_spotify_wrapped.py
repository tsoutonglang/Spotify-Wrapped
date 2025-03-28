### 2025 version

import pandas as pd
import re
from datetime import datetime
from collections import Counter

# Insert Google Sheet link between quotes
WRAP = ""
# WRAP2 = ""

current_datetime = datetime.now()
current_month = current_datetime.strftime("%B") # Automatically computes current month if you want to do it monthly
current_month = "2025"

google_sheets_link = WRAP
# google_sheets_link2 = WRAP2

def convert_google_sheet_url(url):
    # Regular expression to match and capture the necessary part of the URL
    pattern = r'https://docs\.google\.com/spreadsheets/d/([a-zA-Z0-9-_]+)(/edit#gid=(\d+)|/edit.*)?'

    # Replace function to construct the new URL for CSV export
    # If gid is present in the URL, it includes it in the export URL, otherwise, it's omitted
    replacement = lambda m: f'https://docs.google.com/spreadsheets/d/{m.group(1)}/export?' + (f'gid={m.group(3)}&' if m.group(3) else '') + 'format=csv'

    # Replace using regex
    new_url = re.sub(pattern, replacement, url)

    return new_url

# at a later time -> 
# convert csv files into lists
# make the list into a dataframe

pandas_url = convert_google_sheet_url(google_sheets_link)
wrapped_df = pd.read_csv(pandas_url)
# pandas_url = convert_google_sheet_url(google_sheets_link2)
# df2 = pd.read_csv(pandas_url)
# wrapped_df = pd.concat([df, df2], ignore_index=True)

if wrapped_df.date.str.contains(f'{current_month}').any():
    wrapped = (wrapped_df[wrapped_df.date.str.contains(f'{current_month}')])
    print(f"JANUARY SONG NUMBER: {len(wrapped_df[wrapped_df.date.str.contains('January')])} (ROUGHLY {3*len(wrapped_df[wrapped_df.date.str.contains('January')]) / 60} HOURS)")
    print(f"FEBRUARY SONG NUMBER: {len(wrapped_df[wrapped_df.date.str.contains('February')])} (ROUGHLY {3*len(wrapped_df[wrapped_df.date.str.contains('February')]) / 60} HOURS)")
    print(f"MARCH SONG NUMBER: {len(wrapped_df[wrapped_df.date.str.contains('March')])} (ROUGHLY {3*len(wrapped_df[wrapped_df.date.str.contains('March')]) / 60} HOURS)")
    print(f"APRIL SONG NUMBER: {len(wrapped_df[wrapped_df.date.str.contains('April')])} (ROUGHLY {3*len(wrapped_df[wrapped_df.date.str.contains('April')]) / 60} HOURS)")
    print(f"MAY SONG NUMBER: {len(wrapped_df[wrapped_df.date.str.contains('May')])} (ROUGHLY {3*len(wrapped_df[wrapped_df.date.str.contains('May')]) / 60} HOURS)")
    print(f"JUNE SONG NUMBER: {len(wrapped_df[wrapped_df.date.str.contains('June')])} (ROUGHLY {3*len(wrapped_df[wrapped_df.date.str.contains('June')]) / 60} HOURS)")
    print(f"JULY SONG NUMBER: {len(wrapped_df[wrapped_df.date.str.contains('July')])} (ROUGHLY {3*len(wrapped_df[wrapped_df.date.str.contains('July')]) / 60} HOURS)")
    print(f"AUGUST SONG NUMBER: {len(wrapped_df[wrapped_df.date.str.contains('August')])} (ROUGHLY {3*len(wrapped_df[wrapped_df.date.str.contains('August')]) / 60} HOURS)")
    print(f"SEPTEMBER SONG NUMBER: {len(wrapped_df[wrapped_df.date.str.contains('September')])} (ROUGHLY {3*len(wrapped_df[wrapped_df.date.str.contains('September')]) / 60} HOURS)")
    print(f"OCTOBER SONG NUMBER: {len(wrapped_df[wrapped_df.date.str.contains('October')])} (ROUGHLY {3*len(wrapped_df[wrapped_df.date.str.contains('October')]) / 60} HOURS)")
    print(f"NOVEMBER SONG NUMBER: {len(wrapped_df[wrapped_df.date.str.contains('November')])} (ROUGHLY {3*len(wrapped_df[wrapped_df.date.str.contains('November')]) / 60} HOURS)")
    print("")

counts_artist = Counter(wrapped.artist)
counts_song = Counter(wrapped.song)

print(f"I LISTENED TO {len(wrapped)} SONGS IN 2025 (ROUGHLY {3*len(wrapped)} MINUTES OR {3*len(wrapped) / 60} HOURS OR {3*len(wrapped) / 60 / 60} DAYS) \n")
print(f"I LISTENED TO {len(counts_artist.items())} DIFFERENT ARTISTS IN 2025\n")
print(f"I LISTENED TO {len(counts_song.items())} DIFFERENT SONGS IN 2025")
print("_________________________________________________________\n")

# Provides your top ten artists, if you want all artists more >= 10, change range to commented
print("MY TOP TEN ARTISTS ON SPOTIFY OF 2025")

most_popular_artist = dict()
for key, value in counts_artist.items():
    if value >= 10: # Looks at how many artists you've listened to more than ten times
        most_popular_artist[key] = value
most_popular_artist = (dict(sorted(most_popular_artist.items(), key=lambda x:x[1], reverse = True)))
keys_list_artist = list(most_popular_artist.keys())
values_list_artist = list(most_popular_artist.values())

for i in range(0, 10): #range(len(keys_list_artist)):
   print(values_list_artist[i], keys_list_artist[i])

print("_________________________________________________________\n")

print("MY TOP TEN SONGS ON SPOTIFY OF 2025")

most_popular_song = dict()
for key, value in counts_song.items():
    if value >= 2: # Looks at how many songs you've listened to more than two times
        most_popular_song[key] = value
most_popular_song = (dict(sorted(most_popular_song.items(), key=lambda x:x[1], reverse = True)))
keys_list_song = list(most_popular_song.keys())
values_list_song = list(most_popular_song.values())

# Provides top ten songs, if you want all songs >= 15, change range(len(keys_list_song)):
for i in range(0, 10):
    print(values_list_song[i], keys_list_song[i])

# for key, value in counts_artist.items():
#     if value == 1: # Counts artists you've only played one time
#         most_popular_artist[key] = value

# for key, value in counts_song.items():
#     if value == 1: # Counts number of songs only played one time
#         most_popular_song[key] = value


# most_popular_artist = (dict(sorted(most_popular_artist.items(), key=lambda x:x[1], reverse = True)))
# most_popular_song = (dict(sorted(most_popular_song.items(), key=lambda x:x[1], reverse = True)))

# keys_list_artist = list(most_popular_artist.keys())
# values_list_artist = list(most_popular_artist.values())

# keys_list_song = list(most_popular_song.keys())
# values_list_song = list(most_popular_song.values())

# print("_________________________________________________________\n")
# print(f"I LISTENED TO {len(keys_list_artist)} ARTISTS ONLY ONE TIME IN 2025")
# print(f"I LISTENED TO {len(keys_list_song)} SONGS ONLY ONE TIME IN 2025")

# artist_counts = Counter(wrapped['artist'])
# count_taylor_swift = artist_counts["Taylor Swift"] # Can change "Taylor Swift" to any artist
# count_seventeen = artist_counts["Seventeen"]
# print(f"TAYLOR SWIFT COUNT: {count_taylor_swift}")
# print(f"SEVENTEEN COUNT: {count_seventeen}")