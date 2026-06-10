import pandas as pd
import os

df = pd.read_csv("test_data.csv")


# TODO 1 : Print basic info:
#    - Total number of tests
#    - Column names and dtypes
#    - First 5 rows
print(f"Total Number Of Tests : {len(df)}")          #Prints Total number of tests
print(f"Column Names : {df.columns}")       #Prints Column names ?
print(f"Column Data Types : {df.dtype}")         #Prints dtypes
print(f"First Five rows : \n {df.head()}")        #Prints First 5 rows

# TODO 2 : Calculate aggregate metrics:
#    - Overall pass rate
#    - Average duration (in ms and seconds)
#    - Slowest test (name and duration)
#    - Fastest test (name and duration)
print(df.describe())    #Prints Statistical Summary (of Numerical Columns Only)

# TODO 3 : Group by module:
#    - Pass rate per module
#    - Average duration per module
#    - Number of tests per module

# TODO 4 : Filter and display:
#    - All failed tests (name, module, duration)
#    - Tests slower than 1500ms
#    - Tests in the "auth" module

# TODO 5 : Add a computed column:
#    - `duration_sec` = duration_ms / 1000

# TODO 6 : Sort and export:
#    - Sort by duration (descending)
#    - Save the result to `output/results_sorted.csv`