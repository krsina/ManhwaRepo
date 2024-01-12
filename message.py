import discord

class DiscordBot:
    def __init__(self, token, channel_id,books):
        self.token = token
        self.channel_id = channel_id
        self.client = discord.Client(intents=discord.Intents.default())

        # Event handler for when the bot is ready and connected to Discord
        @self.client.event
        async def on_ready():
            print(f'Logged in as {self.client.user.name}')
            print('------')
            channel = self.client.get_channel(int(self.channel_id))
            if channel:
                for book in books:
                    await self.send_message(channel, book.book_title, book.message, book.latest_chapter, book.image_url)
                await self.client.close()

    async def send_message(self, channel, title, description, link, image_url):
        embed = discord.Embed(title=title, description=description)
        embed.add_field(name="Link:", value=link, inline=False)
        embed.set_image(url=image_url)
        await channel.send(embed=embed)