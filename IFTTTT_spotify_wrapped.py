### 2025 Wrapped

import pandas as pd
from datetime import datetime
from collections import Counter

current_datetime = datetime.now()
current_month = current_datetime.strftime("%B") # Automatically computes current month if you want to do it monthly
current_month = "2025"

# import .csv into a dataframe
# insert the directory with your .csv files in between the quotes
wrapped_df = pd.read_csv("")

# repeat import for as many sheets as needed
df = pd.read_csv("")
wrapped_df = pd.concat([wrapped_df, df])

# if you need to check if it was added correctly
# print(wrapped_df)
print("""♡ ∩_∩ 
(„•֊•„)♡ 
￣U U￣￣￣￣￣￣￣￣￣￣￣￣
2025 Spotify Wrapped\n""")

# how many songs and roughly how many hours you listened to Spotify
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

# Provides your top ten artists
most_popular_artist = dict()
for key, value in counts_artist.items():
    if value >= 10: # Looks at how many artists you've listened to more than ten times
        most_popular_artist[key] = value
most_popular_artist = (dict(sorted(most_popular_artist.items(), key=lambda x:x[1], reverse = True)))
keys_list_artist = list(most_popular_artist.keys())
values_list_artist = list(most_popular_artist.values())

# Provides your top ten songs
most_popular_song = dict()
for key, value in counts_song.items():
    if value >= 2: # Looks at how many songs you've listened to more than two times
        most_popular_song[key] = value
most_popular_song = (dict(sorted(most_popular_song.items(), key=lambda x:x[1], reverse = True)))
keys_list_song = list(most_popular_song.keys())
values_list_song = list(most_popular_song.values())

# count_seventeen = artist_counts["Seventeen"]
# print(f"SEVENTEEN COUNT: {count_seventeen}")

print(f"I LISTENED TO {len(wrapped)} SONGS IN 2025 (ROUGHLY {3*len(wrapped)} MINUTES OR {3*len(wrapped) / 60} HOURS OR {3*len(wrapped) / 60 / 60} DAYS)")
print(f"I LISTENED TO {len(counts_artist.items())} DIFFERENT ARTISTS IN 2025")
print(f"I LISTENED TO {len(counts_song.items())} DIFFERENT SONGS IN 2025")
print("\n________⋆.˚✮🎧✮˚.⋆________\n")
print("MY TOP TEN ARTISTS ON SPOTIFY OF 2025")
for i in range(0, 10): #range(len(keys_list_artist)):
   print(values_list_artist[i], keys_list_artist[i])
print("\n________⋆.˚✮🎧✮˚.⋆________\n")
print("MY TOP TEN SONGS ON SPOTIFY OF 2025")
for i in range(0, 10):
    print(values_list_song[i], keys_list_song[i])
print("\n￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")