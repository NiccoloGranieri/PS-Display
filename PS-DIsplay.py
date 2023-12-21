from guizero import App, Picture
# from psnawp_api import PSNAWP
# import urllib.request

psnawp = PSNAWP('')

# # This is you
# client = psnawp.me()

# titles_with_stats = list(client.title_stats())

# img = titles_with_stats[0].image_url
# urllib.request.urlretrieve(img, "test.jpg")

app = App()
picture = Picture(app, image="images/test.gif")
app.display()


# import rawg
# import asyncio

# async def requests():
#     async with rawg.ApiClient(rawg.Configuration(api_key={'key': '666f1797f3294cf8890bbcf67f143776'})) as api_client:
#         # Create an instance of the API class
#         api = rawg.GamesApi(api_client)

#         # Making requests
#         coros = [api.games_read(id=name) for name in ['baldurs-gate-3']]

#         # Waiting for requests
#         for coro in asyncio.as_completed(coros):
#             game: rawg.GameSingle = await coro
#             print('——————————————————————————————————————————————')
#             print('        Name |', game.name)
#             print('    Released |', game.released)
#             print('      Rating |', game.rating)
#             print('Achievements |', game.achievements_count)
#             print('     Website |', game.website)
#             print('  Metacritic |', game.metacritic)
#             print('  Metacritic |', game.background_image)
#             print('——————————————————————————————————————————————')
#             print()

            


# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(requests())