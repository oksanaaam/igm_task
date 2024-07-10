## Project Overview

This project contains Python functions and scripts to perform specific tasks related to processing data and performing computations on integers.  

Here’s a breakdown of what each component does:

- sum_even_numbers.py: Contains a function sum_of_even_numbers that computes the sum of even numbers in a given list of integers.
- processing_csv.py: Provides a function group_by_text_columns to read a CSV file (test-1.csv) and group all values by specified text columns.
- tests: Includes unit tests to verify the functionality of sum_of_even_numbers (test_sum_even_numbers.py) and group_by_text_columns (test_processing_csv.py).

## Requirements

- Python 3.x
- Virtual environment for dependency management


## Setup Instructions

1. Clone the Repository

```
   git clone https://github.com/oksanaaam/igm_task.git
   cd igm_task
```

2. Create and Activate a Virtual Environment

Create a virtual environment to manage your dependencies.
```
   python3 -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows
```

3. Install Dependencies

Install the required Python packages using pip.

   `pip install -r requirements.txt`

4. Run the scripts

For checking grouping python processing_csv.py run:

   `python python processing_csv.py`

For checking sum of even numbers run:

   `python python sum_even_numbers.py`


## Instructions for Running Tests
To run the tests:

Navigate to the directory containing the test files (test_sum_even_numbers.py and test_processing_csv.py) or run:

```
   python -m unittest tests/test_sum_even_numbers.py
   python -m unittest tests/test_processing_csv.py