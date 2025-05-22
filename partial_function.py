from functools import partial

def calculate_bmi(weight: float, height: float) -> str:
    bmi = weight/(height ** 2)
    return f"Your BMI is {bmi:.2f}"

# set my height once and reuse the function
bmi_for_my_height = partial(calculate_bmi, height=1.82)

# track weight changes over time
print(bmi_for_my_height(weight=float(input("Enter your weight: "))))