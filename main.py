# Author: John Sweetall jts6052@psu.edu
# Collaborator: Liam Hooks lrh5428 @psu.edu
# Collaborator: Hunter Fristick hjf5143@psu.edu
# Collaborator: Jacob Henderson jrh6433@psu.edu
# Section: 2
# Breakout: 4


def sum_n(n):
  
  if n == 0:
    return 0 
  else:
    return n + sum_n(n-1)

def print_n(s,n):

  if n == 0:
    return 
  else:
    print(s)
    print_n(n-1)

def run():

  numb = int(input("Enter an integer: "))
  sum1 = sum_n(numb)
  print(f"The sum is {sum1}")
  string1 = str(input("Enter a string: "))
  print_n(string1, numb)

if __name__ == "__main__":
  run()