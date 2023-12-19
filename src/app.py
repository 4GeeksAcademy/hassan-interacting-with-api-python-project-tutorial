import os
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt


# load the .env file variables
load_dotenv()

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

# Authenticate with Spotify
credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=credentials)


artist_id = '55Aa2cqylxrFIXC767Z865'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

# Fetch the top 10 tracks for Lil Wayne
top_tracks = sp.artist_top_tracks(artist_id)

# Extract track information including popularity and duration
top_10_songs = [{'name': track['name'], 
                'popularity': track['popularity'], 
                'duration_ms': track['duration_ms']} for track in top_tracks['tracks'][:10]]

print("Top 10 Songs by Lil Wayne:")
for song in top_10_songs:
    print(song)

df = pd.DataFrame(top_10_songs)

# Sort by popularity in ascending order
sorted_df = df.sort_values(by='popularity', ascending=True)

# Display the top 3 songs
top_3_songs = sorted_df.head(3)
print("Top 3 Songs by Lil Wayne (Sorted by Increasing Popularity):")
print(top_3_songs)


# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(df['duration_ms'], df['popularity'])
plt.title('Song Duration vs Popularity')
plt.xlabel('Duration (milliseconds)')
plt.ylabel('Popularity Score')

# Save the plot as an image file
plt.savefig('duration_vs_popularity.png')
print("Plot saved as 'duration_vs_popularity.png'")