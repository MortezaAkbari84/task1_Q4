x = input("If you want to see temperture in Fahrenheit choose F otherwise choose C for Celsius :")

if x == "C" :
    temp = float(input("enter temperture in Fahrenheit :"))
    temp = (temp-32)/1.8
    print("your temperture in Celsius is ",temp)

elif x == "F" :
    temp = float(input("enter temperture in Celsius :"))
    temp = (1.8 * temp) + 32
    print("your temperture in Fahrenheit is ",temp)
