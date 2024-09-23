import datetime
import os
from PIL import Image, ImageDraw, ImageFont
from instagrapi import Client
#from instagrapi.exceptions import LoginRequired
import logging
from quoteGen import quote
from date import ist_date

#Image Generator#
bg = Image.open("bg.jpg")
font = ImageFont.truetype("font.ttf", size=200)
template = ImageDraw.Draw(bg)

initial_date = datetime.date(2024,6,22)
today = ist_date()
day = (today - initial_date).days

content = f"Day {day}\nWithout You"
template.multiline_text((500,500), content ,font = font, align="center", anchor="mm")

bg.save("out.jpg")
####################################

#Instagram Bot#
username = os.environ['USERNAME']
password = os.environ['PASSWORD']

logger = logging.getLogger()
client = Client()
#client.set_proxy('10.93.51.117:8080')
client.delay_range = [1, 3]
client.load_settings("session.json")
client.login(username, password)
client.get_timeline_feed()

caption = quote()
upload = client.photo_upload("out.jpg", caption)

print("Successfully Uploaded", caption, sep="\n")
os.remove("out.jpg")