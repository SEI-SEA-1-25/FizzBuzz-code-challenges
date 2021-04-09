# Return an array containing the numbers from 1 to N, where N is the parametered value. N will never be less than 1 (in C#, N might be less then 1).

# Replace certain values however if any of the following conditions are met:

# If the value is a multiple of 3 & 5: use the value "FizzBuzz" instead
# If the value is a multiple of 3: use the value "Fizz" instead
# If the value is a multiple of 5: use the value "Buzz" instead

def fizzbuzz(n):
  # empty list to return
  fb_list = []
  # itereate up to n
  for i in range(1, n + 1):
  # use module to find if they are a multiple of 3 or 5
  # if i % 3 == 0 and i % 5 == 0:
  if i % 15 == 0: 
    fb_list.append('FizzBuzz')
  elif i % 3 == 0: 
    fb_list.append('Fizz')
  elif i % 5 == 0: 
    fb_list.append('Buzz')
  else: 
    fb_list.append(i)
  
  return fb_list

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.

def solution(number):
  # running total
  total = 0
  # 
  for i in range(1, number):
  if i % 3 == 0 or i % 5 == 0: 
    total += i

  return total

def recursive_solve(number, total = 0, i = 0):
  # base case
  if i >= number:
  return total
  
  if i % 3 == 0 or i % 5 == 0:
  total += i
  
  recursive_solve(number, total, i + 1)

# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

def find_it(seq):
  # hash table to store numbers
  hash = {}
  # count how many times each number appears
  for number in seq:
    if number not in hash: 
      hash[number] = 1 
    else:
      hash[number] += 1

  # find the one odd number
  for number in hash:
    if hash[number] % 2 != 0: return number