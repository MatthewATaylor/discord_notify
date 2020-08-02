# discord_notify
discord_notify turns a Discord bot into a powerful remote logging tool. It serves as a wrapper for [discord.py](https://discordpy.readthedocs.io/en/latest/), allowing for simple, synchronous Discord messaging to your own channels.

## Installation
Run the following:
```
pip install discord_notify
```

## Usage
First, you'll need to [create a Discord bot](https://discordpy.readthedocs.io/en/latest/discord.html) and add it to one of your servers. 

Then you can use this bot in your code by starting an instance of the `Notifier` class: 
```python
import discord_notify as dn

notifier = dn.Notifier(
    DISCORD_CHANNEL_ID,
    DISCORD_TOKEN
)
notifier.start()
```
The `DISCORD_CHANNEL_ID` is the ID of the channel for messages to be sent to. To find this, first enable developer mode in Discord (User Settings > Appearance > Advanced > Developer Mode). Then right click on the channel to use and press "Copy ID."

The `DISCORD_TOKEN` is the token of the bot you created.

### Sending Messages
Messages can be sent to the given Discord channel by using the `send` and `log` methods of the `Notifier` class.
```python
notifier.send("Hello, world!")
notifier.log("Hello again!")
```
* `send` sends a message to the Discord channel.
* `log` both sends a message to the Discord channel and prints that message to the console.

## Use Cases
* Remote logging for lengthy tasks
    * Providing notifications during neural network training (e.g. logging validation accuracy after each training epoch)
    * Providing notifications on the status of a Python web server
* 
