import random
from time import time

correct = 0
incorrect = 0
total = 10
total_time = 0;

for i in range(total):
  n1 = random.randrange(3,16)
  n2 = random.randrange(2,11)
  start = int(time() * 1000)

  try:
    ans = int(input(str(n1) + " X " + str(n2) + " = "))
  except ValueError:
    print("That wasn't a number!")
    incorrect+=1
    end = int(time() * 1000)
    total_time = end - start
    continue

  end = int(time() * 1000)
  total_time += end - start

  corr_ans = n1 * n2

  if ans == corr_ans:
    print('Awesome')
    correct+=1
  else:
    print('Aah ... miseed. Correct answer is: ' + str(corr_ans))
    incorrect+=1

print('You got %d correct out of %d in %s secs' % (correct, total, str(total_time/1000)))



