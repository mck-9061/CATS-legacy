import random
from discordwebhook import Discord

def post_to_discord(subject, webhook_url, message, routeName):
    photosFile = open("photos.txt", "r")
    photo = random.choice(photosFile.read().split("\n"))
    photosFile.close()

    webhook = Discord(url=webhook_url)

    webhook.post(
        embeds=[{"title": subject,
                 "description": message,
                 "image": {
                     "url": photo},
                 "author": {
                     "name": routeName
                 },
                 "footer": {
                     "text": "Carrier Administration and Traversal System",
                 }
                 }],
    )