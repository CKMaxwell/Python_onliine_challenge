# 20200706 - Grading Students
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    ans = []
    for i in range(len(grades)):
        check = 5 - (grades[i] % 5)
        if grades[i] < 38:
            ans.append(grades[i])
        elif check >= 3:
            ans.append(grades[i])
        elif check < 3:
            ans.append(grades[i] + check)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
