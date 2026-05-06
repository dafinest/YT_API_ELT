import requests
import json
import os
from dotenv import load_dotenv
from pathlib import Path



load_dotenv(dotenv_path="./.env")

CHANNEL_HANDLE = "MrBeast"
API_KEY = os.getenv("API_KEY")

def get_playlist_id():

    try:
        Url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"

        response = requests.get(Url)
        response.raise_for_status()

        data = response.json()
        # print(json.dumps(data, indent=4))

        channel_items = data['items'][0]

        channel_playlistID = channel_items['contentDetails']['relatedPlaylists']['uploads']

        print(channel_playlistID)
        return channel_playlistID

    except requests.exceptions.RequestException as e:
        raise e
        

if __name__ == "__main__":
    get_playlist_id()
        
