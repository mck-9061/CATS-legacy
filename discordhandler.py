import random
from discord_webhook import DiscordWebhook, DiscordEmbed

global lastSent
global lastHook
global lastEmbed

def post_to_discord(subject, webhook_url, message, routeName):
    photosFile = open("photos.txt", "r")
    photo = random.choice(photosFile.read().split("\n"))
    photosFile.close()

    webhook = DiscordWebhook(url=webhook_url, rate_limit_retry=True)

    embed = DiscordEmbed(title=subject, description=message)
    embed.set_image(url=photo)
    embed.set_author(name=routeName)
    embed.set_footer(text="Carrier Administration and Traversal System")

    webhook.add_embed(embed)

def post_with_fields(subject, webhook_url, message, routeName, carrierStage, maintenanceStage):
    global lastSent
    global lastHook
    global lastEmbed

    photosFile = open("photos.txt", "r")
    photo = random.choice(photosFile.read().split("\n"))
    photosFile.close()

    webhook = DiscordWebhook(url=webhook_url, rate_limit_retry=True)

    embed = DiscordEmbed(title=subject, description=message)
    embed.set_image(url=photo)
    embed.set_author(name=routeName)
    embed.set_footer(text="Carrier Administration and Traversal System")

    embed.add_embed_field(name="Jump stage", value=carrierStage)
    embed.add_embed_field(name="Maintenance stage", value=maintenanceStage)

    lastEmbed = embed

    webhook.add_embed(embed)

    lastSent = webhook.execute()
    lastHook = webhook

def update_fields(carrierStage, maintenanceStage):
    global lastSent
    global lastHook
    global lastEmbed

    lastHook.remove_embeds()

    lastEmbed.del_embed_field(0)
    lastEmbed.del_embed_field(0)

    lastEmbed.add_embed_field(name="Jump stage", value=carrierStage)
    lastEmbed.add_embed_field(name="Maintenance stage", value=maintenanceStage)

    lastHook.add_embed(lastEmbed)

    lastHook.edit(lastSent)
