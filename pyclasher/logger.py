from logging import Logger


class PyClasherLogger:
    logger: Logger | None

    def __init__(self, logger: Logger | None):
        if logger is None:
            self.logger = None
        else:
            self.logger = logger.getChild("PyClasher")
        return

    def debug(self, debug_message: str):
        if self.logger is not None:
            self.logger.debug(debug_message)
        return

    def info(self, info_message: str):
        if self.logger is not None:
            self.logger.info(info_message)
        return

    def warning(self, warning_message: str):
        if self.logger is not None:
            self.logger.warning(warning_message)
        return

    def critical(self, critical_message: str):
        if self.logger is not None:
            self.logger.critical(critical_message)
        return

    def exception(self, exception_message: str):
        if self.logger is not None:
            self.logger.exception(exception_message)
        return

    def error(self, error_message: str):
        if self.logger is not None:
            self.logger.error(error_message)
        return

    def fatal(self, fatal_message: str):
        if self.logger is not None:
            self.logger.fatal(fatal_message)
        return

    def __call__(self, function):
        def wrapper(*args, **kwargs):
            self.debug(f"started {function.__name__}")
            try:
                result = function(*args, **kwargs)
            except Exception as exception:
                self.error(str(exception))
                raise exception
            self.debug(f"ended {function.__name__}")
            return result
        return wrapper

    def start_logging(self):
        self.logger.propagate = True
        return

    def stop_logging(self):
        self.logger.propagate = False
        return
