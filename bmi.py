def calculate_bmi (height, weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))

    bmi = weight/(height * height)
    print("BMI is " + str(round(bmi,2)))

    if bmi<18.5:
        print("Underweight")
        return -1

    elif 18.5<= bmi <= 25.0:
        print("Normal Weight")
        return 0

    else:
        print("Over Weight")
        return 1

calculate_bmi(weight=52, height = 1.73)
calculate_bmi(weight=100, height = 1.73)

