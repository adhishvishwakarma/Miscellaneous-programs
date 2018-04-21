"""
You are given a int[] marks containing the grades you have received so far in a class.
Each grade is between 0 and 10, inclusive.
Assuming that you will receive a 10 on all future assignments, determine the minimum number of future assignments
that are needed for you to receive a final grade of 10. You will receive a final grade of 10
if your average grade is 9.5 or higher.


Definition
Class: AimToTen
Method: need
Parameters: tuple (integer)
Returns: integer
Method signature: def need(self, marks):
Limits
Time limit (s): 840.000
Memory limit (MB): 64
Constraints
- marks has between 1 and 50 elements, inclusive.
- Each element of marks is between 0 and 10, inclusive.


Examples
0)
{9, 10, 10, 9}
Returns: 0
Your average is already 9.5, so no future assignments are needed.
1)
{8, 9}
Returns: 4
In this case you need 4 more assignments. With each completed assignment, your average could increase to 9, 9.25, 9.4 and 9.5, respectively.
2)
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
Returns: 950
3)
{10, 10, 10, 10}
Returns: 0
"""


class AimToTen:
    def __init__(self):
        self.n = 0

    def mean(self, numbers):
        return float(sum(numbers)) / max(len(numbers), 1)

    def need(self, marks):

        if not isinstance(marks, list):
            marks = list(marks)
        if self.mean(marks) >= 9.5:
            return self.n
        else:
            self.n += 1
            marks.append(10)
            return self.need(marks)

x = AimToTen()

print(x.need((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)))