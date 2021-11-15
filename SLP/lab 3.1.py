height = float(input("Please enter your height: "))
weight = float(input("Please enter your weight: "))

BMI = weight / height ** 2

if BMI < 16.00:
    print("starvation")
elif BMI >= 16 and BMI <= 16.99:
    print("emaciation")
elif BMI >= 17 and BMI <= 18.49:
    print("underweight")
elif BMI >= 18.50 and BMI <= 24.99:
    print("correct weight")
elif BMI >= 25.00 and BMI <= 29.99:
    print("overweight")
elif BMI >= 30.00 and BMI <= 34.99:
    print("first degree obesity")
elif BMI >= 35.00 and BMI <= 39.99:
    print("second degree obesity (clinical)")
else:
    print("third degree obesity (extreme)")

optional_weight_min = 18.50 * (height ** 2)
optional_weight_max = 24.99 * (height ** 2)

print("Your normal weight interval is between {} and {}".format(optional_weight_min, optional_weight_max))