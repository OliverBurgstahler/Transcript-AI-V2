import random
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.proxies import WebshareProxyConfig
import re
import requests

app = Flask(__name__)
CORS(app)

# Proxy list based on the data you provided
PROXIES = [
    {"ip": "38.154.227.167", "port": 5868, "username": "xofzzxzh", "password": "55ttpq0bfwb4"},
    {"ip": "198.23.239.134", "port": 6540, "username": "xofzzxzh", "password": "55ttpq0bfwb4"},
    {"ip": "207.244.217.165", "port": 6712, "username": "xofzzxzh", "password": "55ttpq0bfwb4"},
    {"ip": "107.172.163.27", "port": 6543, "username": "xofzzxzh", "password": "55ttpq0bfwb4"},
    {"ip": "216.10.27.159", "port": 6837, "username": "xofzzxzh", "password": "55ttpq0bfwb4"},
    {"ip": "136.0.207.84", "port": 6661, "username": "xofzzxzh", "password": "55ttpq0bfwb4"},
    {"ip": "64.64.118.149", "port": 6732, "username": "xofzzxzh", "password": "55ttpq0bfwb4"},
    {"ip": "142.147.128.93", "port": 6593, "username": "xofzzxzh", "password": "55ttpq0bfwb4"},
    {"ip": "104.239.105.125", "port": 6655, "username": "xofzzxzh", "password": "55ttpq0bfwb4"},
    {"ip": "206.41.172.74", "port": 6634, "username": "xofzzxzh", "password": "55ttpq0bfwb4"},
]

def pick_random_proxy():
    if not PROXIES:
        return None
    return random.choice(PROXIES)

def extract_video_id(url):
    regex = r"(?:v=|\/)([0-9A-Za-z_-]{11}).*"
    match = re.search(regex, url)
    return match.group(1) if match else None

def test_proxy():
    proxy = pick_random_proxy()
    if not proxy:
        print("No proxies configured, skipping proxy test")
        return

    proxy_url = f"http://{proxy['username']}:{proxy['password']}@{proxy['ip']}:{proxy['port']}"
    proxies = {
        'http': proxy_url,
        'https': proxy_url,
    }
    try:
        r = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=10)
        print(f"Proxy test successful with proxy {proxy['ip']}, your IP via proxy: {r.text}")
    except Exception as e:
        print(f"Proxy test failed with proxy {proxy['ip']}: {e}")

def get_transcript(video_id):
    proxy = pick_random_proxy()
    try:
        if proxy:
            proxy_config = WebshareProxyConfig(proxy['username'], proxy['password'], proxy['ip'], proxy['port'])
            print(f"Using proxy: http://{proxy['username']}:{proxy['password']}@{proxy['ip']}:{proxy['port']}")
            ytt_api = YouTubeTranscriptApi(proxy_config=proxy_config)
            transcript = ytt_api.get_transcript(video_id)
        else:
            print("No proxy config found, trying direct connection.")
            transcript = YouTubeTranscriptApi.get_transcript(video_id)

        return " ".join([t['text'] for t in transcript])
    except Exception as e:
        print(f"Transcript error for video_id={video_id}: {e}")
        return None

@app.route("/")
def home():
    return send_from_directory(".", "youtube_transcript.html")

@app.route("/transcript", methods=["POST"])
def handle_transcript():
    print("Transcript endpoint called")
    data = request.get_json()
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400

    url = data.get("url")
    if not url:
        return jsonify({"error": "No URL provided"}), 400

    video_id = extract_video_id(url)
    print(f"extract_video_id: url={url} -> video_id={video_id}")
    if not video_id:
        return jsonify({"error": "Invalid YouTube URL"}), 400

    transcript_text = get_transcript(video_id)
    if not transcript_text:
        return jsonify({"error": "Transcript not found"}), 404

    return jsonify({"transcript": transcript_text})

@app.route("/debug-env")
def debug_env():
    # Return the current proxy selected for debugging if you want
    return {
        "proxies_count": len(PROXIES)
    }

if __name__ == "__main__":
    print("Starting Flask app...")
    test_proxy()
    print("Routes registered:")
    for rule in app.url_map.iter_rules():
        print(f"  {rule.rule} -> {rule.endpoint}")
    app.run(host='0.0.0.0', port=5000, debug=True)
