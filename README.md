# discord_notify
[**discord_notify**](https://github.com/MatthewATaylor/discord_notify) is a minimal Discord API webhooks wrapper for easily sending messages to a Discord channel.

## Use Cases
* Remote logging for lengthy Python scripts, such as:
    * Providing notifications during neural network training (e.g. logging validation accuracy after each training epoch)
    * Providing notifications on the status of a Python web server
* Regularly displaying information on a Discord channel without configuring a bot

## Installation
```
pip install discord_notify
```

## Usage
First, you'll need to create a new webhook for one of your Discord channels (Edit Channel > Integrations > Webhooks).

Then you can use this webhook in your code by creating an instance of the `Notifier` class and using the webhook's URL: 
```python
import discord_notify as dn

notifier = dn.Notifier(URL)
```

### Sending Messages Once
Messages can be sent through the webhook by using the `send` method of the `Notifier` class.
```python
notifier.send("Hello, world!", print_message=True)
```
* `print_message` indicates whether or not the provided message should be printed to the console. It defaults to `False`.

### Sending Messages Repeatedly
The send_repeat method can be used to send messages over a regular interval of time.
```python
x = 0
notifier.send_repeat(lambda: x, 1.5, print_message=True)
while x < 100000:
    x += 0.0001
```
The first parameter is a callable that returns the value to send, and the second parameter is the number of seconds to wait between webhook executions.

The method's `daemon` parameter can be set to `False`, forcing the timer thread to be stopped manually with the `stop_repeat` method. This requires a `timer_id` which is returned from `send_repeat`:
```python
x = 0
timer_id = notifier.send_repeat(
    lambda: x, 
    1.5, 
    print_message=True, 
    daemon=False
)
while x < 100000:
    x += 0.0001
    if x > 10000:
        notifier.stop_repeat(timer_id)
```
