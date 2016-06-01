'''num1 = raw_input("give me the first number:")
num2 = raw_input("give me the second number:")
to_do = raw_input("What do you want to do with these two numbers? choose between 'add','substract','mutiply','divide'")
if to_do == add:
	print num1+num2
elif to_do == substract:
	print abs(num1-num2)
elif to_do == mutiply:
	print num1*num2
elif to_do == divide:
	print num1/num2 and num2/num1
else:
	return "Please choose between 'add','substract','mutiply','divide'"

	

x = raw_input("Give one equation with two numbers, I will solve it:")
y = x.split()
if y[1] == "+":
	return y[0] + y[2]
elif y[1] == "-":
	return y[0] - y[2]
elif y[1] == "*":
	return y[0] * y[2]
elif y[1] == "/":
	return y[0] / y[2]
else:
	return "Did you type it right? "
'''

from sys import argv

num1 = argv[1]
x = argv[2]
num2 = argv[3]
if x == "+":
	print int(num1)+int(num2)
if x == "-":
	print int(num1)-int(num2)
if x == "*":
	print int(num1) * int(num2)
if x == "/":
	print int(num1)/ int(num2)



