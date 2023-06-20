import logging


class CallCountDecorator:
    """A decorator that counts the number of times a function is called."""

    def __init__(self):
        self.count = 0

    def __call__(self, func):
        """
        Decorates a function and counts the number of times it is called.

        Args:
            func (callable): The function to decorate.

        Returns:
            callable: The decorated function.
        """

        def wrapper(*args, **kwargs):
            """
            Wrapper function that tracks the number of function calls and raises an exception if it exceeds a limit.

            Args:
                *args: Positional arguments passed to the decorated function.
                **kwargs: Keyword arguments passed to the decorated function.

            Returns:
                Any: The result of the decorated function call.
            """
            if self.count > 2:
                raise Exception('too many calls')
            self.count += 1
            return func(*args, **kwargs)

        return wrapper


class ArgumentsCountDecorator:
    """A decorator that prints the number of arguments of a function."""

    def __call__(self, func):
        """
        Decorates a function and prints the number of arguments it accepts.

        Args:
            func (callable): The function to decorate.

        Returns:
            callable: The decorated function.
        """

        def wrapper(*args, **kwargs):
            """
            Wrapper function that prints the number of arguments of the decorated function.

            Args:
                *args: Positional arguments passed to the decorated function.
                **kwargs: Keyword arguments passed to the decorated function.

            Returns:
                Any: The result of the decorated function call.
            """
            print(f"Number of arguments in the function: {func.__code__.co_argcount}")
            return func(*args, **kwargs)

        return wrapper


def logger(exception, mode):
    logger = logging.getLogger("my_logger")
    logger.setLevel(logging.ERROR)

    if mode == "console":
        console_handler = logging.StreamHandler()
        logger.addHandler(console_handler)
    elif mode == "file":
        file_handler = logging.FileHandler("logs.log")
        logger.addHandler(file_handler)
    else:
        raise ValueError("No matching mode")

    def decorator(input_func):
        def wrapper(*args, **kwargs):
            try:
                return input_func(*args, **kwargs)
            except exception as e:
                logger.error(str(e))

        return wrapper

    return decorator
