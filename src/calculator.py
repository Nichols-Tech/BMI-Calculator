from constants import UNDERWEIGHT_THRESHOLD, NORMAL_THRESHOLD, OVERWEIGHT_THRESHOLD

def calculate_bmi(weight, height):
    return round(weight / (height/100)**2, 2)

def determine_category(bmi):
    if bmi < UNDERWEIGHT_THRESHOLD:
        return "Underweight"
    elif UNDERWEIGHT_THRESHOLD <= bmi < NORMAL_THRESHOLD:
        return "Normal"
    elif NORMAL_THRESHOLD <= bmi < OVERWEIGHT_THRESHOLD:
        return "Overweight"
    else:
        return "Obese"
      
