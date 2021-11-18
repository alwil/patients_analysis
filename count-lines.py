'''
This module counts counts the number of lines in standard input
Input: A string from a system standard input
Output: A string with thetotal number of lines
'''

import sys
count=0

for line in sys.stdin:
    count+=1
print(count,'lines in standard input')

