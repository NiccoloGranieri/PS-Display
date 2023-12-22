psnawp = PSNAWP('')
from guizero import App, Picture, Text
from psnawp_api import PSNAWP
import urllib.request
import os

client = psnawp.me()
PS5StaticIP = "192.168.1.200"
allTitleStats = list()

def pingPS5(ip):
    # Ping PS5 to check if it is on
    response = os.system("ping -c 1 " + ip)
    return response # 0 = on, 1 = off

def checkImgLibrary(title, url):
    # Check if game art is present in images folder
    if os.path.exists(f"images/{title}.png"):
        pass
    else:
        urllib.request.urlretrieve(url, f"images/{title}.png")
    return f"images/{title}.png"

if not allTitleStats:
    allTitleStats = list(client.title_stats())
elif allTitleStats and pingPS5(PS5StaticIP) == 0:
    allTitleStats.clear()
    allTitleStats = list(client.title_stats())

gameName = allTitleStats[0].name
gameArtURL = allTitleStats[0].image_url

gameArt = checkImgLibrary(gameName, gameArtURL)

app = App()
picture = Picture(app, image = gameArt, align="left")
test = Text(app, text = "test", align="right")
app.set_full_screen()
app.display()