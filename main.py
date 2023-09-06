# 1.1 Implement a recurcive function to calculate tha factorial of given number
"""
1! = 1 * 1
2! = 2 * 1!__> 2 * 1
3! = 3 * 2!__>3 * 2 * 1
.
.
10! = 10 * 9!__> 10 * 9 * 8 *...... * 1

formula - n * (n-1)!
"""


def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_rec(n - 1)


number = int(input("Enter the value:"))
rec = fact_rec(number)

print("The factorial of {} is {} .".format(number, rec))
