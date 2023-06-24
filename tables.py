import random

n1 = random.randrange(1,10)
n2 = random.randrange(1,10)
ans = input(str(n1) + " X " + str(n2) + " = ")

corr_ans = n1 * n2

if int(ans) == corr_ans:
  print('Awesome')
else:
  print('Aah ... miseed. Correct answer is: ' + str(corr_ans))

