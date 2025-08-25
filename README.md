# Mood-Based Spotify Playlist Recommender

This Python script detects your mood based on keywords in your input and suggests matching Spotify playlists.

## Features
- Detects moods like happy, sad, relaxed, energetic, angry, and romantic.
- Searches Spotify for relevant playlists using the Spotify Web API.
- Returns playlist names and links.

## Requirements
- Python 3.7+
- [NLTK](https://www.nltk.org/) (for mood keyword handling)
- [Spotipy](https://spotipy.readthedocs.io/en/2.22.1/) (Spotify API client)

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mood-playlist-recommender.git
   cd mood-playlist-recommender
   ```

2. Install dependencies:
   ```bash
   pip install nltk spotipy
   ```

3. Set up your Spotify API credentials:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/)
   - Create an app and copy your `Client ID` and `Client Secret`.
   - Replace them in the script:
     ```python
     client_id="YOUR_CLIENT_ID"
     client_secret="YOUR_CLIENT_SECRET"
     ```

## Usage
Run the script:
```bash
python mood_playlist.py
```
Enter how you're feeling (e.g., *"I feel sad and lonely"*) and get playlist recommendations.

## Example
```
How are you feeling? I feel excited and good today!
Detected mood: Happy
Here are some playlists for you:

Happy Hits → https://open.spotify.com/playlist/...
Good Vibes → https://open.spotify.com/playlist/...
```

## License
This project is open-source under the [MIT License](LICENSE).
