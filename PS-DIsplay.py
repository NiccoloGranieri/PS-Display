# from psnawp_api import PSNAWP

psnawp = PSNAWP('')

# # This is you
# client = psnawp.me()

# print("Online ID")
# print(client.online_id)
# print("Account ID")
# print(client.account_id)

# print("Baldur's Gate 3 Trophies")
# for trophy_title in client.trophy_titles_for_title(title_ids=['PPSA14002_00']):
#     print(trophy_title)

# print("Play Times")
# titles_with_stats = client.title_stats()
# print(list(titles_with_stats))

from guizero import App

app = App(title="Hello world")
app.display()