class Plugin(object):
    """
    Plugin Base Class
    Meant to be inherited for plugins
    """

    def __init__(self):
        self._commands = {}

    def command(self, name, **kwargs):
        """
        Decorator to register a coroutine to a plugin command

        :param name: Command Name
        :return:
        """
        kwargs = {i: kwargs[i] for i in kwargs.keys() if i != "_coro"}

        def command_func(func):
            self._commands[name]["_coro"] = func
            for i in kwargs.keys():
                self._commands[name][i] = kwargs[i]
            return func

        return command_func

    def on_load(self, bot):
        """
        Function to be called when a plugin is loaded into a Bot. Meant to be overridden

        :param bot: Bot Instance into which the Plugin is loaded
        :return:
        """
        pass
