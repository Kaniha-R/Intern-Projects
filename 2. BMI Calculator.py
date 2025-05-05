def calculate_bmi(weight,height):
    bmi=weight/(height**2)
    return bmi

def classify_bmi(bmi):
    if bmi<18.5:
        return "Underweight"
    elif bmi<25:
        return "Normal"
    elif bmi<30:
        return "Overweight"
    else:
        return "Obese"
    
try:
    weight=float(input("Enter your weight in kg: "))
    height=float(input("Enter your height in meters: "))
    if weight<=0 or height<=0:
        print("Enter positive values for weight and height.")
    else:
        bmi=calculate_bmi(weight,height)
        category=classify_bmi(bmi)
        print(f"Your BMI is {bmi:.2f}.Category: {category}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
    