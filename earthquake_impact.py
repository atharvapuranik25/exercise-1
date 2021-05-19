print("This is a program to calculate the intensity of an Earthquake using Richter Scale.")

M = input("Magnitude as measured on Richter scale(between 1 to 10):")

M = float(M)
#casting string "M" to float

#according to richter scale M=log(I/I0)
I = 10**M

print("The intensity of the earthquake is", I)
