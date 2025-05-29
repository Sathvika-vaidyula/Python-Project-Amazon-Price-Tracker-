from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

# Twilio Credentials
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token_secret'
twilio_number = '+12694619412'  # Your Twilio phone number
your_phone_number = '+919390586610'  # Your personal phone number to receive SMS

# Product URL to track
url = "https://appbrewery.github.io/instant_pot/"

# Fetch the page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Extract price text and convert to float
price_text = soup.find(class_="a-offscreen").get_text()
price_without_currency = price_text.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

# Extract product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

# Your target buy price
BUY_PRICE = 100

# Send SMS if price drops below BUY_PRICE
if price_as_float < BUY_PRICE:
    message_body = f"{title} is on sale for {price_text}!\nCheck it out: {url}"

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_body,
        from_=twilio_number,
        to=your_phone_number
    )
    print("SMS sent!")
    print(f"Message SID: {message.sid}")
else:
    print("Price is still too high, no SMS sent.")
