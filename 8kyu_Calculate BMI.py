def bmi(weight, height):

    bmi = weight/ (height * height)
    if bmi <= 18.5:
        return "Underweight"

    if bmi <= 25.0:
        return "Normal"

    if bmi <= 30.0:
        return "Overweight"

    if bmi > 30:
        return "Obese"

if __name__ == "__main__":

    bmi(2, 2)