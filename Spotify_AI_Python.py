from nltk.corpus import wordnet
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.cache_handler import CacheFileHandler

mood_keywords = {
    "happy": ["happy", "joyful", "excited", "smile", "good"],
    "sad": ["sad", "down", "depressed", "unhappy", "blue"],
    "relaxed": ["relax", "calm", "chill", "peaceful", "easy"],
    "energetic": ["energy", "hype", "party", "dance", "workout"],
    "angry": ["angry", "mad", "frustrated", "rage", "upset"],
    "romantic": ["love", "romantic", "date", "heart"]
}

def detect_mood(user_input):
    user_input = user_input.lower()
    for mood, keywords in mood_keywords.items():
        if any(word in user_input for word in keywords):
            return mood
    return "relaxed"  # default fallback mood


mood_to_spotify = {
    "happy": "happy hits",
    "sad": "sad songs",
    "relaxed": "chill",
    "energetic": "workout",
    "angry": "rock",
    "romantic": "love songs"
}

# Custom cache handler to avoid .cache errors
cache_handler = CacheFileHandler(cache_path=".spotify_cache")

sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id="YOUR ID",
        client_secret="YOUR SECRET",
        cache_handler=cache_handler
    )
)

def get_spotify_playlist(mood):
    # Ensure search query includes "playlist" to refine results
    search_query = f"{mood_to_spotify.get(mood.lower(), 'chill')} playlist"
    results = sp.search(q=search_query, type="playlist", limit=10)
    playlists = []

    for playlist in results.get('playlists', {}).get('items', []):
        if playlist:
            playlists.append({
                "name": playlist.get('name', 'Unknown'),
                "url": playlist.get('external_urls', {}).get('spotify', 'N/A')
            })

    # Fallback if nothing found
    if not playlists:
        fallback_query = "chill playlist"
        fallback_results = sp.search(q=fallback_query, type="playlist", limit=5)
        for playlist in fallback_results.get('playlists', {}).get('items', []):
            playlists.append({
                "name": playlist.get('name', 'Unknown'),
                "url": playlist.get('external_urls', {}).get('spotify', 'N/A')
            })

    return playlists


if __name__ == "__main__":
    user_input = input("How are you feeling? ")
    mood = detect_mood(user_input)
    playlists = get_spotify_playlist(mood)

    print(f"\nDetected mood: {mood.capitalize()}")
    print("Here are some playlists that match your mood:\n")
    for p in playlists:
        print(f"{p['name']} → {p['url']}")
