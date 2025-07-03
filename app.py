import random
import os
from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig
import re
import requests

app = Flask(__name__)
CORS(app)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# Proxy list based on the data you provided
PROXIES = [
    {"ip": "38.154.227.167", "port": 5868, "username": "xofzzxzh", "password": "55ttpq0bfwb4"},
    {"ip": "198.23.239.134", "port": 6540, "username": "xofzzxzh", "password": "55ttpq0bfwb4"},
    {"ip": "207.244.217.165", "port": 6712, "username": "xofzzxzh", "password": "55ttpq0bfwb4"},
    {"ip": "107.172.163.27", "port": 6543, "username": "xofzzxzh", "password": "55ttpq0bfwb4"},
    {"ip": "216.10.27.159", "port": 6837, "username": "xofzzxzh", "password": "55ttpq0bfwb4"},
    {"ip": "136.0.207.84", "port": 6661, "username": "xofzzxzh", "password": "55ttpq0bfwb4"},
    {"ip": "104.223.160.151", "port": 5930, "username": "xofzzxzh", "password": "55ttpq0bfwb4"}
]

def get_transcript(video_id):
    for proxy in PROXIES:
        try:
            config = WebshareProxyConfig(
                proxy_host=proxy["ip"],
                proxy_port=proxy["port"],
                proxy_username=proxy["username"],
                proxy_password=proxy["password"]
            )
            transcript = YouTubeTranscriptApi.get_transcript(video_id, proxies=config.get_proxy())
            return transcript
        except Exception as e:
            continue
    return {"error": "Unable to fetch transcript with available proxies."}

@app.route("/transcript", methods=["POST"])
def transcript():
    data = request.get_json()
    url = data.get("url", "")
    video_id_match = re.search(r"(?:v=|youtu\.be/)([\w-]{11})", url)
    if not video_id_match:
        return jsonify({"error": "Invalid YouTube URL"}), 400
    video_id = video_id_match.group(1)
    transcript_data = get_transcript(video_id)
    return jsonify(transcript_data)

@app.route("/")
def index():
    return render_template('youtube_transcript.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
