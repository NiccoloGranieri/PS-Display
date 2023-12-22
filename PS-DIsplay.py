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

def updateData(psIP, stats, me):
    if pingPS5(psIP) == 0:
        stats.clear()
        stats = list(me.title_stats())
    
    title.value = stats[0].name
    title.after(10000, updateData, (psIP, stats, me))
    
def updatePic(psIP, stats, me):
    if pingPS5(psIP) == 0:
        stats.clear()
        stats = list(me.title_stats())
    
    picture.image = checkImgLibrary(stats[0].name, stats[0].image_url)
    title.after(10000, updatePic, (psIP, stats, me))

if __name__ == "__main__":

    allTitleStats = list(client.title_stats())

    gameName = allTitleStats[0].name
    gameArt = checkImgLibrary(gameName, allTitleStats[0].image_url)

    app = App()
    picture = Picture(app, image = gameArt, align="left")
    title = Text(app, text = gameName, align="right")
    app.set_full_screen()

    picture.after(10000, updatePic, (PS5StaticIP, allTitleStats, client))  # Schedule call to counter() every 1000ms
    title.after(10000, updateData, (PS5StaticIP, allTitleStats, client))  # Schedule call to counter() every 1000ms
    app.display()
