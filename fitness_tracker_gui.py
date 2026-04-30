import tkinter as tk
from tkinter import messagebox
import pandas as pd
from datetime import datetime

food_db = pd.read_csv("food_database.csv")

daily_log = []

total_calories = 0
total_protein = 0
total_carbs = 0
total_fat = 0


def add_food():
    global total_calories, total_protein, total_carbs, total_fat

    food_name = food_entry.get()
    grams = grams_entry.get()

    if not food_name or not grams:
        messagebox.showerror("Error", "Please enter food name and grams.")
        return

    try:
        grams = float(grams)
    except ValueError:
        messagebox.showerror("Error", "Grams must be a number.")
        return

    translations = {
        "piletina": "Chicken Breast",
        "chicken": "Chicken Breast",

        "riža": "Rice",
        "riza": "Rice",
        "rice": "Rice",

        "zobene": "Oats",
        "zobena": "Oats",
        "oats": "Oats",

        "banana": "Banana",

        "jaje": "Egg",
        "jaja": "Egg",
        "egg": "Egg",
        "eggs": "Egg",

        "whey": "Whey Protein",
        "protein": "Whey Protein"
    }

    food_name = translations.get(food_name.lower(), food_name)

    food_row = food_db[food_db["food"].str.lower() == food_name.lower()]

    if food_row.empty:
        messagebox.showerror("Error", "Food not found in database.")
        return

    calories = (food_row.iloc[0]["calories"] / 100) * grams
    protein = (food_row.iloc[0]["protein"] / 100) * grams
    carbs = (food_row.iloc[0]["carbs"] / 100) * grams
    fat = (food_row.iloc[0]["fat"] / 100) * grams

    total_calories += calories
    total_protein += protein
    total_carbs += carbs
    total_fat += fat

    result_text.insert(
        tk.END,
        f"{food_name} | {grams}g | {calories:.2f} kcal | "
        f"P: {protein:.2f}g | C: {carbs:.2f}g | F: {fat:.2f}g\n"
    )

    totals_label.config(
        text=f"Total Calories: {total_calories:.2f} | "
             f"Protein: {total_protein:.2f}g | "
             f"Carbs: {total_carbs:.2f}g | "
             f"Fat: {total_fat:.2f}g"
    )

    food_entry.delete(0, tk.END)
    grams_entry.delete(0, tk.END)

def save_report():
    if not daily_log:
        messagebox.showwarning("Warning", "No data to save.")
        return

    report = pd.DataFrame(daily_log)
    filename = f"daily_report_{datetime.now().strftime('%Y-%m-%d')}.csv"
    report.to_csv(filename, index=False)

    messagebox.showinfo("Success", f"Report saved as {filename}")

root = tk.Tk()
root.title("Fitness Tracker App")
root.geometry("900x700")


title_label = tk.Label(root, text="Fitness Tracker", font=("Arial", 20))
title_label.pack(pady=10)


food_label = tk.Label(root, text="Food Name:")
food_label.pack()
food_entry = tk.Entry(root, width=40)
food_entry.pack()


grams_label = tk.Label(root, text="Grams:")
grams_label.pack()
grams_entry = tk.Entry(root, width=20)
grams_entry.pack()


add_button = tk.Button(root, text="Add Food", command=add_food)
add_button.pack(pady=10)

save_button = tk.Button(root, text="Save Report", command=save_report)
save_button.pack()

result_text = tk.Text(root, height=20, width=100)
result_text.pack()


totals_label = tk.Label(
    root,
    text="Total Calories: 0 | Protein: 0g | Carbs: 0g | Fat: 0g",
    font=("Arial", 12)
)
totals_label.pack(pady=20)


root.mainloop()