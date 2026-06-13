import requests
import os

URL = "https://l-tike.com/order/?gLcode=10601&gPfKey=20260224000002147765%2C20260224000002147770&gEntryMthd=02&gScheduleNo=8&gCarrierCd=01&gPfName=ＪＯＩＮ%E3%80%80ＡＬＩＶＥ%E3%80%80２０２６&gBaseVenueCd=15085"

html = requests.get(
    URL,
    headers={"User-Agent": "Mozilla/5.0"}
).text

if "18日入場券" not in html:
    requests.post(
        os.environ["DISCORD_WEBHOOK"],
        json={"content": " JOIN ALIVE監視失敗。ページ構造が変わった可能性があります。"}
    )
else:
    idx = html.find("18日入場券")
    area = html[idx:idx+2000]

    if "予定枚数終了" not in area:
        requests.post(
            os.environ["DISCORD_WEBHOOK"],
            json={"content": " JOIN ALIVE 18日券の状態が変わった可能性あり！今すぐ確認！"}
        )
