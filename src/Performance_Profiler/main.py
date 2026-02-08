import logging
from .functions import sum_large_numbers, add, star_triangle
from .timeit_tools import timeit_functions
from .profiler_tools import profile_functions
from .logger import setup_logger

# logging configuration
setup_logger()

def main():
    functions = [sum_large_numbers, add, star_triangle]

    # Using timeit
    try:
        logging.info("Starting timeit")
        timeit_functions(functions, number=10)
    except Exception as e:
        logging.error(f"Error occurred during timeit: {e}")

    # Using cProfile
    try:
        logging.info("Starting cProfile performance profiling")
        profile_functions(functions)
    except Exception as e:
        logging.error(f"Error occurred during profiling: {e}")

    logging.info("Performance profiling completed. Check performance_report.txt for details.")

if __name__ == "__main__":
    main()
