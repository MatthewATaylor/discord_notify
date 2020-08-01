import threading
import asyncio

import discord


class Notifier:
    """
    Wrapper for sending messages with a Discord bot
    """
    def __init__(self, channel_id, token):
        self.channel_id = channel_id
        self.token = token
        self.client = discord.Client()
        self.message_queue = []

    def __start(self):
        async def on_ready():
            channel = self.client.get_channel(self.channel_id)
            print("Notifier bot ready in channel: " + channel.name)
            self.client.loop.create_task(self.__send_messages())
        self.client.event(on_ready)
        self.client.run(self.token)

    def start(self):
        """
        Start Discord bot in a separate thread
        """
        bot_thread = threading.Thread(target=self.__start, daemon=True)
        bot_thread.start()
        print("Bot starting up...")

    async def __send_messages(self):
        """
        Look through message_queue for messages to send
        """
        while True:
            i = 0
            length = len(self.message_queue)
            while i < length:
                await self.__send(self.message_queue.pop(0))
                i += 1
            await asyncio.sleep(1)

    async def __send(self, message):
        channel = self.client.get_channel(self.channel_id)
        await channel.send(message)

    def send(self, message):
        """
        Add message to queue of messages to send
        """
        self.message_queue.append(message)

    def log(self, message):
        """
        Add message to queue of messages to send and
        print message to console
        """
        self.send(message)
        print(message)
