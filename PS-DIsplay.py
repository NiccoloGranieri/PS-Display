from guizero import App, Picture, Text
from psnawp_api import PSNAWP
from PIL import Image
import urllib.request
import os

path = os.getcwd()

with open(os.path.abspath(os.path.join(path, os.pardir)) + '/npsso.txt', 'r') as file:
    npsso = file.read().replace('\n', '')

psnawp = PSNAWP(npsso)
client = psnawp.me()
PS5StaticIP = "192.168.1.200"
global allTitleStats

def pingPS5(ip):
    # Ping PS5 to check if it is on
    response = os.system("ping -c 1 " + ip)
    return response # 0 = on, 1 = off

def checkImgLibrary(title, url):
    # Check if game art is present in images folder
    if os.path.exists(f"images/{title}.png"):
        pass
    else:
        urllib.request.urlretrieve(url, f"images/{title}.jpeg")
        im = Image.open(f"images/{title}.jpeg")
        im.save(f"images/{title}.png", "PNG")
    return f"images/{title}.png"

def updateData(ip):
    global allTitleStats
    if pingPS5(ip) == 0:
        allTitleStats.clear()
        allTitleStats = list(client.title_stats())
    
    picture.value = checkImgLibrary(allTitleStats[0].name, allTitleStats[0].image_url)
    title.value = allTitleStats[0].name

if __name__ == "__main__":

    allTitleStats = list(client.title_stats())

    gameName = allTitleStats[0].name
    gameArt = checkImgLibrary(gameName, allTitleStats[0].image_url)

    app = App()
    picture = Picture(app, image = gameArt, align="left").resize(480, 480)
    title = Text(app, text = gameName, align="right")
    app.set_full_screen()
    
    picture.repeat(10000, updateData(PS5StaticIP))  # Schedule call to counter() every 1000ms
    title.repeat(10000, updateData(PS5StaticIP))  # Schedule call to counter() every 1000ms

    app.display()