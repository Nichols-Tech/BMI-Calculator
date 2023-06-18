WEIGHT_PROMPT = "Enter your weight in kg: "
HEIGHT_PROMPT = "Enter your height in cm: "
UNDERWEIGHT_THRESHOLD = 18.5
NORMAL_THRESHOLD = 25
OVERWEIGHT_THRESHOLD = 30

weight = float(input(WEIGHT_PROMPT))
height = float(input(HEIGHT_PROMPT))

body_mass_index = weight / (height/100)**2
body_mass_index = round(body_mass_index, 2)
print("Your BMI is:", body_mass_index)

if body_mass_index < UNDERWEIGHT_THRESHOLD:
    print("Underweight")
elif UNDERWEIGHT_THRESHOLD <= body_mass_index < NORMAL_THRESHOLD:
    print("Normal")
elif NORMAL_THRESHOLD <= body_mass_index < OVERWEIGHT_THRESHOLD:
    print("Overweight")
else:
    print("Obese")

