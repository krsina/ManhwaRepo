import discord
import json

client = discord.Client(intents=discord.Intents.default())

with open('secrets.json') as f:
    secrets = json.load(f)

TOKEN = secrets['DISCORD_KEY'];
MANHWA_CHANNEL_ID = secrets['DISCORD_CHANNEL_ID'];

def discordMessage(book_title, latest_chapter, image_url, message):
    # Create a new Discord client with the specified intents
    # Event handler for when the bot is ready and connected to Discord
    @client.event
    async def on_ready():
        print(f'Logged in as {client.user.name}')
        print('------')
        channel = client.get_channel(int(MANHWA_CHANNEL_ID))
        if channel:
            # Create an embed
            embed = discord.Embed(
                title=book_title,
                description = message
            )
            embed.add_field(name="Link:", value=latest_chapter, inline=False)
            embed.set_image(url=image_url)
            print(image_url)

            # Send the embed to the specified channel
            await channel.send(embed=embed)
            await client.close()
    client.run(TOKEN)