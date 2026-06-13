import requests
import hashlib
import os

URL = "https://joinalive.jp/2026/tickets/schedule/"

html = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=30
).text

current_hash = hashlib.md5(html.encode()).hexdigest()

HASH_FILE = "last_hash.txt"

try:
    with open(HASH_FILE, "r") as f:
        old_hash = f.read().strip()
except:
    old_hash = ""

if old_hash and old_hash != current_hash:
    requests.post(
        os.environ["DISCORD_WEBHOOK"],
        json={
            "content":
            " JOIN ALIVEチケットページに変更がありました！\nhttps://joinalive.jp/2026/tickets/schedule/"
        }
    )

with open(HASH_FILE, "w") as f:
    f.write(current_hash)

print("監視完了")
