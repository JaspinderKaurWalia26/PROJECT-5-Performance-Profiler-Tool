# Performance Profiler Tool

## Project Overview
The Performance Profiler Tool is a Python project designed to identify slow functions in the code and provide optimization suggestions.  
It uses Python’s built-in timeit to measure execution time and cProfile to profile functions.


---
## What Does This Project Do?
- Measures execution time of multiple Python functions using `timeit`.  
- Profiles functions using `cProfile` to find slow functions.  
- Generates a **performance report** (`data/outputs/performance_report.txt`) including:
  - Timeit results for each function  
  - cProfile statistics (function calls, cumulative time)  
  - Function-wise optimization suggestions  
 
---

## Technologies Used
- Python 3
- Built-in modules:
  - cProfile
  - timeit 
  - pstats 
  - logging 
  - io
  - os

---

## Project Structure

```
PERFORMANCE_PROFILER_TOOL/
│
├── data/
│   ├── optimization.txt             # Optimization suggestions 
│   │
│   ├── outputs/
│   │   └── performance_report.txt   # Performance analysis report
│   │
│   └── logs/
│       └── app.log                  # Application log file
│
├── src/
│   └── Performance_Profiler/
│       ├── __init__.py              # Package initializer
│       ├── functions.py             # Sample functions to be profiled
│       ├── logger.py                # Logging configuration
│       ├── main.py                  # Main entry point of the profiler
│       ├── profiler_tools.py        # Performance profiling utilities
│       └── timeit_tools.py          # Execution time measurement tools
│
└── README.md               # Project documentation

```

## How to Run
### 1. Clone the repository
```
git clone https://github.com/JaspinderKaurWalia26/PROJECT-5-Performance-Profiler-Tool.git
cd PROJECT-5-Performance-Profiler-Tool
```
### 2. Create a virtual environment (optional)
```
python -m venv venv
```
### 3. Activate the virtual environment
- Windows:
```
venv\Scripts\activate
```
- Linux/Mac:
```
source venv/bin/activate
```
### 4. Install dependencies
```
This project does not require any external dependencies.  
All required modules are part of Python’s standard library.
```
### 5. Run the program
```
python -m src.Performance_Profiler.main
```
### 6. Check outputs

- Performance Report: data/outputs/performance_report.txt

- Logs: logs/app.log

### 7. Optimization Suggestions

File location: data/optimization.txt





