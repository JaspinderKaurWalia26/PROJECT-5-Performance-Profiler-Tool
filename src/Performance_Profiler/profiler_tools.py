import cProfile
import pstats
import logging
from io import StringIO

def profile_functions(function_list, output_file="data/outputs/performance_report.txt"):
   
    # Creating a cProfile profiler object
    profiler = cProfile.Profile()
    # Start profiling
    profiler.enable()
    # Running all functions
    for func_name in function_list:
        try:
            func_name()
        except Exception as e:
            logging.error(f"Error occurred while profiling {e}")
    # Stop profiling
    profiler.disable()
    # Creating a pstats.Stats object to analyze the profiler data
    stats = pstats.Stats(profiler)
    # Sorting by cumulative time
    stats.sort_stats('cumtime')  
    # Using StringIO to capture the text output
    output = StringIO()
    stats.stream = output
    # Printing stats into StringIO
    stats.print_stats()  

    # Saving the profiling report to a text file
    with open(output_file, "a") as file:
        file.write(output.getvalue())

    
