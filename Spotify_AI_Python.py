from nltk.corpus import wordnet
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Simple mood classification by keywords
mood_keywords = {
    "happy": ["happy", "joyful", "excited", "smile", "good"],
    "sad": ["sad", "down", "depressed", "unhappy", "blue"],
    "relaxed": ["relax", "calm", "chill", "peaceful", "easy"],
    "energetic": ["energy", "hype", "party", "dance", "workout"],
    "angry": ["angry", "mad", "frustrated", "rage", "upset"],
    "romantic": ["love", "romantic", "date", "heart"]
}

def detect_mood(user_input):
    user_input = user_input.lower()   # make all text lowercase so matching works regardless of case
    for mood, keywords in mood_keywords.items():   # loop through each mood and its list of keywords
        if any(word in user_input for word in keywords):   # check if ANY keyword for that mood is found in the user’s text
            return mood   # if found, return the mood (like "happy", "sad", etc.)
    return "relaxed"  # default




mood_to_spotify = {
    "happy": "happy hits",
    "sad": "sad songs",
    "relaxed": "chill",
    "energetic": "workout",
    "angry": "rock",
    "romantic": "love songs"
}


sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id="YOUR CLIENT ID",
        client_secret="YOUR SECRET" 
    ))


def get_spotify_playlist(mood):
    search_query = mood_to_spotify.get(mood.lower(), "chill")
    results = sp.search(q=search_query, type="playlist", limit=5)
    playlists = []
    
    for playlist in results.get('playlists', {}).get('items', []):
        if playlist:  # make sure it's not None , which caused an error
            playlists.append({
                "name": playlist.get('name', 'Unknown'),
                "url": playlist.get('external_urls', {}).get('spotify', 'N/A')
            })
    return playlists


if __name__ == "__main__":
    user_input = input("How are you feeling?")
    mood = detect_mood(user_input)
    playlists = get_spotify_playlist(mood)

    print(f"\nDetected mood: {mood.capitalize()}")
    print("Here are some playlists for you:\n")
    for p in playlists:
        print(f"{p['name']} → {p['url']}")