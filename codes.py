from matplotlib.pyplot import get
import requests
import schedule
import time
import json

oldCodes = []

def getCodes():
    url = requests.get("https://www.toxworx.com/jsonfile/ttw.json")
    text = url.text
    data = json.loads(text)
    loadedCodes = data[0]["codes"]
    newCodes = []
    for code in loadedCodes:
        if code["code"] not in oldCodes:
            newCodes.append(code["code"])
            oldCodes.append(code["code"])
    return newCodes

def sendCodes():
    codes = getCodes()
    if len(codes) > 0:
        print("Sending codes")
        print(codes)
        print("-----------")
        return codes
    else:
        print("No new codes")
        print("-----------")
        return []

schedule.every(10).minutes.do(sendCodes)
schedule.every().hour.do(sendCodes)
schedule.every().day.at("10:30").do(sendCodes)

sendCodes()
sendCodes()

while 1:
    schedule.run_pending()
    time.sleep(1)