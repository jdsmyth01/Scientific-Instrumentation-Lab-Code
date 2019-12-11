from bottle import route, run, request
import spotipy
import json
import os
from spotipy import oauth2

if os.path.exists("spotify_freq.txt"):
    os.remove("spotify_freq.txt")

PORT_NUMBER = 8080
SPOTIPY_CLIENT_ID = '3e4b87aabf2441b3b29a942835e80ccb'
SPOTIPY_CLIENT_SECRET = 'cfd3b6407ee34359b0647f0beb00a428'
SPOTIPY_REDIRECT_URI = 'http://localhost:8080'
SCOPE = 'user-library-read'
CACHE = '.spotipyoauthcache'
# current song URI: Astral Plane by Valerie June
SONG_URI = 'spotify:track:1ISGSSgVnZhyiOGSI8itNa'

sp_oauth = oauth2.SpotifyOAuth( SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET,SPOTIPY_REDIRECT_URI,scope=SCOPE,cache_path=CACHE )

@route('/')
def index():

    access_token = ""

    token_info = sp_oauth.get_cached_token()

    if token_info:
        print "Found cached token!"
        access_token = token_info['access_token']
    else:
        url = request.url
        code = sp_oauth.parse_response_code(url)
        if code:
            print "Found Spotify auth code in Request URL! Trying to get valid access token..."
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']

    if access_token:
        print "Access token available! Trying to get user information..."
        sp = spotipy.Spotify(access_token)
        # grab audio analysis of desired track
        analysis = sp.audio_analysis(SONG_URI)
        params = analysis["track"]
        print(params.get("tempo"))
        file = open("spotify_freq.txt", "w+")
        file.write(str(params.get("tempo")))
        print("Successfully extracted parameters!");
        print("Press Ctrl+C to quit");
        results = sp.current_user()
        return results

    else:
        return htmlForLoginButton()

def htmlForLoginButton():
    auth_url = getSPOauthURI()
    htmlLoginButton = "<a href='" + auth_url + "'>Login to Spotify</a>"
    return htmlLoginButton

def getSPOauthURI():
    auth_url = sp_oauth.get_authorize_url()
    return auth_url

run(host='', port=8080)
