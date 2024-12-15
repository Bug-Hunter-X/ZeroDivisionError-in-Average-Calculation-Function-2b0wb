# Python Average Calculation with Empty List Handling

This repository demonstrates a common Python coding error: the `ZeroDivisionError` that occurs when trying to calculate the average of an empty list.  The initial `bug.py` file contains the error, while the solution is in `bugSolution.py`.  This example highlights the importance of input validation and error prevention in robust code.

**Bug:**
The original code does not handle the case where an empty list is passed as input to the `calculate_average` function, resulting in a `ZeroDivisionError`. 

**Solution:**
The corrected code checks for an empty list before performing the division, returning 0 in that case.