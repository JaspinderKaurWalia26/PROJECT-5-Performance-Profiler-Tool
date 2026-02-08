import timeit
import logging
from .logger import setup_logger

# logging configuration
setup_logger()
# Measuring execution time of functions using timeit
def timeit_functions(function_list, number=10):
    for function in function_list:
        try:
            time_taken = timeit.timeit(lambda: function(), number=number)
            logging.info(f"{function.__name__} took {time_taken:.5f} seconds for {number} runs")
        except Exception as e:
            logging.error(f"Error occurred while executing {function.__name__}: {e}")
    