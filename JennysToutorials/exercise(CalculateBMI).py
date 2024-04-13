height = input("Enter your height in m :")
weight = input("Enter you weight in Kg :")

BMI = round(float(weight)/(float(height) ** 2), 2)

print("you BMI is :" + str(BMI))

if 18.5 <= BMI <= 24.9:
    print("Normal range")

elif 17.0 <= BMI <= 18.4:
    print("Underweight (Mild thinness)")

elif 16.0 <= BMI <= 16.9:
    print("Underweight (Moderate  thinness)")

elif BMI < 16.0:
    print("Underweight (Severe  thinness)")

elif 25.0 <= BMI <= 29.9:
    print("Overweight (Pre-obese)")

elif 30.0 <= BMI <= 34.9:
    print("Obese (Class I)")

elif 35.0 <= BMI <= 39.9:
    print("Obese (Class II)")

else:
    print("Obese (Class III)")
