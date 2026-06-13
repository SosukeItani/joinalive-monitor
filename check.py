from playwright.sync_api import sync_playwright
import requests
import os

URL = "https://l-tike.com/order/?gLcode=10601&gPfKey=20260224000002147765%2C20260224000002147770&gEntryMthd=02&gScheduleNo=8&gCarrierCd=01&gPfName=ＪＯＩＮ%E3%80%80ＡＬＩＶＥ%E3%80%80２０２６&gBaseVenueCd=15085"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)

    page = browser.new_page()
    page.goto(URL, wait_until="networkidle", timeout=120000)

    text = page.locator("body").inner_text()

    browser.close()

print("18日入場券" in text)

if "18日入場券" in text:
    idx = text.find("18日入場券")
    area = text[idx:idx+500]

    print(area)

    if "予定枚数終了" not in area:
        requests.post(
            os.environ["DISCORD_WEBHOOK"],
            json={
                "content":
                " JOIN ALIVE 18日券の状態が変わった可能性あり！"
            }
        )
