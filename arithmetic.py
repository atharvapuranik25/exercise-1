print("This is a program to calculate the total amount to be paid at a fruit shop as well as splitting the bill.")

apples = input("How many apples did you purchase (input integer):")

cost = input("Cost of 1 apple (in Rupees):")

x = int(apples)
#casting the string apples to integer
y = float(cost)
#casting the string cost to float

print("The amount to be paid to the shopkeeper is Rs.", x*y)

people = input("The bill will be split among how many people (enter only if 2 or above):")

z = int(people)
#casting the string people to integer

print("Each person has to pay Rs.", (x*y)//z)
