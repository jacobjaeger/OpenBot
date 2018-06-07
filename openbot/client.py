from .errors import MalformedArguments
import discord
import inspect


class Bot(discord.Client):
    """
    The openbot Bot
    This Bot inherits from discord.Client, so you can use all of its methods.
    The only thing you should not do is customize on_message
    """

    def __init__(self, prefix, *plugins):
        super(Bot, self).__init__()
        self.prefix = prefix
        self._commands = {}
        for plugin in plugins:
            for command in plugin._commands.keys():
                self._commands[command] = plugin._commands[command]
            plugin.on_load(self)

    async def on_message(self, message):
        """
        openbot Implementation of on_message.
        This is called when a message is written in a channel that the bot has access to
        Calls the command that was sent if it is in openbot.Bot._commands.keys()

        :param message: the message object provided by discord
        :return: Nothing
        """
        if not message.content.startswith(self.prefix):
            return
        args = message.content.split(" ")
        if not len(args[0]) > len(self.prefix):
            return
        invoke = args[0][len(self.prefix):]
        if invoke in self._commands.keys():
            await (self._commands[invoke])(self, message)

    def command(self, name, **kwargs):
        """
        Decorator to register a coroutine to a bot command

        :param name: Command Name
        :return:
        """
        kwargs = {i: kwargs[i] for i in kwargs.keys() if i != "_coro"}

        def command_func(func):
            self._commands[name] = {}
            self._commands[name]["_coro"] = func
            for i in kwargs.keys():
                self._commands[name][i] = kwargs[i]
            return func

        return command_func

    def load_plugins(self, *plugins):
        """
        Command to load a plugin after __init__ was called


        :param plugin: openbot.Plugin object
        :return:
        """

        for plugin in plugins:
            for command in plugin._commands.keys():
                self._commands[command] = plugin._commands[command]
            plugin.on_load(self)

    async def reply(self, message):
        """
        Sends a Message into the channel the Command this is called from was called
        Can only be called directly from a command

        :param message: The text that should be sent
        :return: discord.Message; The message that was sent
        """
        tlargs = inspect.getargs(inspect.currentframe().f_back.f_code).args
        if not len(tlargs) == 2:
            raise MalformedArguments(
                "A Bot Command has to take two arguments (openbot.Bot, discord.Message)")
        try:
            channel = inspect.currentframe().f_back.f_locals[tlargs[1]].channel
        except:
            raise MalformedArguments("Second argument is not an Instance of discord.Message")
        msg = await self.send_message(channel, message)
        return msg

    async def wait_for_answer(self, timeout=None, check=None, content=None):
        """
        Wait for an Answer from the person in the channel who invoked the calling command.
        Can only be called directly from a command

        :param timeout: Optional Timeout, as described in the official discord.py Documentation
        :param check: Optional Check, as described in the official discord.py Documentation
        :param content: Optional Content Check, as described in the official discord.py Documentation
        :return: discord.Message
        """
        tlargs = inspect.getargs(inspect.currentframe().f_back.f_code).args
        if not len(tlargs) == 2:
            raise MalformedArguments(
                "A Bot Command has to take two arguments (openbot.Bot, discord.Message)")
        try:
            msg = inspect.currentframe().f_back.f_locals[tlargs[1]]
        except:
            raise MalformedArguments("Second argument is not an Instance of discord.Message")
        return await self.wait_for_message(author=msg.author, channel=msg.channel, timeout=timeout, content=content,
                                           check=check)
