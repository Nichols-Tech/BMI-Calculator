from calculator import calculate_bmi, determine_category

def main():
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))

    body_mass_index = calculate_bmi(weight, height)
    print("Your BMI is:", body_mass_index)

    category = determine_category(body_mass_index)
    print("You are", category)

if __name__ == "__main__":
    main()
