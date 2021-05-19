print("This is a program that calculates the temperature that a person feels because of the wind, also known as the wind chill factor.")

T = input("Temperature of the Wind (in degree fahrenheit):")
T = float(T)
#casting the string "temp" to float

V = input("Wind Speed (in miles per hour):")
V = float(V)
#casting the string "wind_speed" to float

#formula for calculating the wind chill factor is 35.74 + 0.6215T – 35.75 (V^0.16) + 0.4275T (V^0.16)

wind_chill = 35.74 + (0.6215 * T) - (35.75 * (pow(V, 0.16))) + ((0.4275 * T) * (pow(V, 0.16)))

wind_chill = str(wind_chill)
#casting float "wind_chill" to string

print("The wind chill is ", wind_chill + " degree F.")
