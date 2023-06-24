import random
import datetime

correct = 0
incorrect = 0
total = 5
total_time = 0;

for i in range(total):
  n1 = random.randrange(1,10)
  n2 = random.randrange(1,10)
  start = datetime.datetime.now()

  try:
    ans = int(input(str(n1) + " X " + str(n2) + " = "))
  except ValueError:
    print("That wasn't a number!")
    incorrect+=1
    continue

  end = datetime.datetime.now()
  total_time = end - start

  corr_ans = n1 * n2

  if ans == corr_ans:
    print('Awesome')
    correct+=1
  else:
    print('Aah ... miseed. Correct answer is: ' + str(corr_ans))
    incorrect+=1

print('You got %d correct out of %d in %s' % (correct, total, str(total_time)))



