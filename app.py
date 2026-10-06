# CITY SOLAR ENERGY - 100% FREE AI BOT
# CEO: 03492850290
# PHONE ID: 1107765231834912

from flask import Flask, request
import requests

app = Flask(__name__)

PHONE_NUMBER_ID = "1107765231834912"
WHATSAPP_TOKEN =  # <-- YOUR FULL TOKEN "EAAPvgbEjVyABSrjakpd2GlyZCyxZBR57acyyTgp6ZAD2vJigZAfL2Wpu0MrftNm3c1kg0sKuqyaSk2WuEeWeOT97IVX7btvZCEqplHw2JZCZCFHtT9vG4m3ZCRZALmuPAFSMU67sf98JUTdxieQyFCFascCHZCgXCPZCEiYbIcB2puIu9cOja08ybxAiFipZBSpWzbucNauHkCZAIXMWKRdM7oWVRAtZCAAtSZB1FP8BDF7ZBfCbaGYvJpfZBqBsZAZBHeM6nbshf0ApSynZBeOA4NLU2cLFP9ZC5MX4ZD"
VERIFY_TOKEN = "citysolar123"

def get_reply(user_msg):
    msg = user_msg.lower()
    if "salam" in msg or "hello" in msg or "hi" in msg:
        return "Wa Alaikum Salam! ☀️\nWelcome to CITY SOLAR ENERGY\nOfficial Distributor of OMEGA\n\nWe deal in: Omega, Inverex, Growatt, Longi\n\nBataiye kis cheez ki price chahiye?\nCEO Ihtesham: 03492850290"
    elif "omega" in msg:
        return "✅ OMEGA Official Distributor\nAvailable: 3KW, 4KW, 6KW, 10KW\nBest Price: Call CEO 03492850290\nShop: Biha Road Ditpani Stapp Opposite Masjid"
    elif "price" in msg or "rate" in msg:
        return "Price daily update hoti hai sir 📈\n1. Omega Inverter\n2. Solar Panel\n3. Full System\nCEO Ihtesham: 03492850290"
    elif "location" in msg or "address" in msg:
        return "📍 CITY SOLAR ENERGY\nBiha Road, Ditpani Stapp Opposite Masjid\nCEO: 03492850290"
    else:
        return "Shukria CITY SOLAR ENERGY se rabta ka ☀️\nCEO Ihtesham jald reply karega: 03492850290"

@app.route("/")
def home():
    return "Bot Running - CITY SOLAR ENERGY - CEO 03492850290"

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")
        return "Failed"
    if request.method == "POST":
        try:
            data = request.json
            msg_data = data['entry'][0]['changes'][0]['value']['messages'][0]
            from_num = msg_data['from']
            text = msg_data['text']['body']
            reply = get_reply(text)
            url = f"https://graph.facebook.com/v20.0/{PHONE_NUMBER_ID}/messages"
            headers = {"Authorization": f"Bearer {WHATSAPP_TOKEN}"}
            payload = {"messaging_product": "whatsapp", "to": from_num, "text": {"body": reply}}
            requests.post(url, headers=headers, json=payload)
        except:
            pass
        return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
