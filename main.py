import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load food database
food_db = pd.read_csv("food_database.csv")

# Food aliases for Croatian + English input
food_aliases = {
    "pileća prsa": "Pileća prsa",
    "piletina": "Pileća prsa",
    "chicken breast": "Pileća prsa",
    "chicken": "Pileća prsa",

    "riža": "Riža",
    "rice": "Riža",

    "zobene": "Zobene pahuljice",
    "zobene pahuljice": "Zobene pahuljice",
    "oats": "Zobene pahuljice",
    "oatmeal": "Zobene pahuljice",

    "banana": "Banana",

    "jaje": "Jaje",
    "egg": "Jaje",
    "eggs": "Jaje",

    "whey": "Whey protein",
    "whey protein": "Whey protein",
    "protein": "Whey protein",

    "puretina": "Puretina",
    "turkey": "Puretina",

    "govedina": "Govedina",
    "beef": "Govedina",

    "losos": "Losos",
    "salmon": "Losos",

    "tuna": "Tuna",

    "bjelanjak": "Bjelanjak",
    "egg white": "Bjelanjak",

    "krumpir": "Krumpir",
    "potato": "Krumpir",

    "tjestenina": "Tjestenina",
    "pasta": "Tjestenina",

    "kruh": "Kruh",
    "bread": "Kruh",

    "jabuka": "Jabuka",
    "apple": "Jabuka",

    "brokula": "Brokula",
    "broccoli": "Brokula",

    "špinat": "Špinat",
    "spinach": "Špinat",

    "rajčica": "Rajčica",
    "tomato": "Rajčica",

    "krastavac": "Krastavac",
    "cucumber": "Krastavac",

    "bademi": "Bademi",
    "almonds": "Bademi",

    "kikiriki maslac": "Kikiriki maslac",
    "peanut butter": "Kikiriki maslac",

    "maslinovo ulje": "Maslinovo ulje",
    "olive oil": "Maslinovo ulje",

    "avokado": "Avokado",
    "avocado": "Avokado"
    
}

# Daily totals
total_calories = 0
total_protein = 0
total_carbs = 0
total_fat = 0
daily_log = []

print("=== FITNESS TRACKER APP ===")

while True:
    food_name = input("\nEnter food name (or 'end' to finish): ").lower()

    if food_name == "end":
        break

    if food_name in food_aliases:
        food_name = food_aliases[food_name]
    else:
        print("Food not found in database.")
        continue

    grams = float(input("Enter grams: "))

    food_row = food_db[food_db["food"] == food_name]

    if not food_row.empty:
        calories = (food_row.iloc[0]["calories"] / 100) * grams
        protein = (food_row.iloc[0]["protein"] / 100) * grams
        carbs = (food_row.iloc[0]["carbs"] / 100) * grams
        fat = (food_row.iloc[0]["fat"] / 100) * grams

        total_calories += calories
        total_protein += protein
        total_carbs += carbs
        total_fat += fat

        daily_log.append({
            "food": food_name,
            "grams": grams,
            "calories": calories,
            "protein": protein,
            "carbs": carbs,
            "fat": fat
        })

        print(f"\nAdded: {food_name} ({grams}g)")
        print(f"Calories: {calories:.2f}")
        print(f"Protein: {protein:.2f}g")
        print(f"Carbs: {carbs:.2f}g")
        print(f"Fat: {fat:.2f}g")

print("\n=== DAILY FOOD LOG ===")
for entry in daily_log:
    print(
        f"{entry['food']} | {entry['grams']}g | "
        f"{entry['calories']:.2f} kcal | "
        f"Protein: {entry['protein']:.2f}g | "
        f"Carbs: {entry['carbs']:.2f}g | "
        f"Fat: {entry['fat']:.2f}g"
    )

print("\n=== TOTAL DAILY INTAKE ===")
print(f"Calories: {total_calories:.2f}")
print(f"Protein: {total_protein:.2f}g")
print(f"Carbs: {total_carbs:.2f}g")
print(f"Fat: {total_fat:.2f}g")

macros = ["Protein", "Carbs", "Fat"]
values = [total_protein, total_carbs, total_fat]

plt.bar(macros, values)
plt.title("Daily Macronutrient Intake")
plt.ylabel("Grams")
plt.show()

daily_report = pd.DataFrame(daily_log)

filename = f"daily_report_{datetime.now().strftime('%Y-%m-%d')}.csv"
daily_report.to_csv(filename, index=False)

print(f"\nDaily report saved as: {filename}")