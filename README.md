# OpenBot
A simple discord.py extension
## Installation
#### Requirements:
```setuptools```
```discord.py```
```Python 3.5+```

#### Installation
This tutorial assumes you use Python 3.5. Replace `python3.5` with your version name to change python installations
##### With `pip`
```python3.5 -m pip install discord-openbot```
##### Manually
```git clone https://github.com/jcb1317/OpenBot.git```
```python3.6 setup.py install```

## Introduction
#### Your first Bot (w/ Plugin)
```
import openbot

my_plugin = openbot.Plugin()

@my_plugin.command("ping")
async def ping(bot, msg):
    await bot.reply("Pong!")
    
bot = openbot.Bot("!")
bot.load_plugins(my_plugin)
bot.run("YOUR_TOKEN") # Replace YOUR_TOKEN with your token obtained from https://discordapp.com/developers/applications/me
```
