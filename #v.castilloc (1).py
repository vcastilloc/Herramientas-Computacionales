NumberTest = 7
test=True
for i in range(2, NumberTest):
 if NumberTest%i==0:
  print("The number is not prime")
  test=False
  break
if test:
  print("The number is prime")
  



