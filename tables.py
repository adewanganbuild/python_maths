import random

correct = 0
incorrect = 0
total = 10

for i in range(total):
  n1 = random.randrange(1,10)
  n2 = random.randrange(1,10)
  ans = input(str(n1) + " X " + str(n2) + " = ")

  corr_ans = n1 * n2

  if int(ans) == corr_ans:
    print('Awesome')
    correct+=1
  else:
    print('Aah ... miseed. Correct answer is: ' + str(corr_ans))
    incorrect+=1

print('You got %d correct out of %d' % (correct, total))



