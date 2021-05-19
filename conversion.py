print("This is a program to convert Temperature Value in Celsius to Farenheit.")

celsius = input("Temperature Value in degree Celsius:")

c = float(celsius)
#casting string "celsius" to float
f = (c * 1.8) + 32
#converting celsius value to fahrenheit
f = str(f)
#casting float "f" to string
print("Temperature in Fahrenheit will be", f + " degrees.")
