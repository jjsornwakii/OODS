high, weight = input("Enter your High and Weight : ").split()
BMI = float(weight) / float(pow(float(high),2))
if BMI < 18.5 :
    print("Less Weight")
elif 18.50 <= BMI  < 23 :
    print("Normal Weight")
elif 23 <= BMI  < 25 :
    print("More than Normal Weight")
elif 25 <= BMI  < 30 :
    print("Getting Fat")
else :
    print("Fat")
