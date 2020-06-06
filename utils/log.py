import coloredlogs
import logging
import verboselogs

# TODO Add Indentation adapter
# FIXME DEBUG level not working


class Log:
    """Wrapper class for coloured and verbuse logs."""
    levels = {}
    default = None

    @classmethod
    def init(cls, default, levels):
        """Set the default and levels and initialize the log manager.

        :param cls: Log class.
        :param default: default log level
        :param levels: log levels
        """
        verboselogs.install()
        coloredlogs.install()
        cls.default = default
        cls.levels = {module: level for module, level in levels}
        for module, level in levels:
            logging.getLogger(module).setLevel(level)

    @classmethod
    def get(cls, name):
        """Return the initialized logger with the module name.

        :param cls: Log class.
        :param name: module name
        :returns: logger instance
        """
        level = cls.levels.get(name, cls.default)
        logger = logging.getLogger(name)
        logger.setLevel(level)
        return logger

    @staticmethod
    def get_levels():
        """Get list of log level names.

        :returns: list of string
        """
        return logging._levelToName.values()
