import tkinter as tk
from tkinter import messagebox

# ---------- Functions ----------

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Enter values greater than 0")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            status = "Underweight"
        elif bmi < 25:
            status = "Normal Weight"
        elif bmi < 30:
            status = "Overweight"
        else:
            status = "Obese"

        result_label.config(
            text=f"BMI Value : {bmi:.2f}\nHealth Status : {status}"
        )

    except ValueError:
        messagebox.showerror("Error", "Please enter numeric values only")


def clear_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")


def show_info():
    messagebox.showinfo("About", "This is a Simple BMI Calculator App")


# ---------- Window ----------
window = tk.Tk()
window.title("BMI Calculator")
window.geometry("400x400")
window.configure(bg="lightblue")

# ---------- Title ----------
tk.Label(
    window,
    text="BMI CALCULATOR",
    font=("Arial", 18, "bold"),
    bg="lightblue"
).pack(pady=10)

# ---------- Weight ----------
tk.Label(window, text="Weight (kg):", bg="lightblue").pack()
weight_entry = tk.Entry(window, width=25)
weight_entry.pack(pady=10)

# ---------- Height ----------
tk.Label(window, text="Height (m):", bg="lightblue").pack()
height_entry = tk.Entry(window, width=25)
height_entry.pack(pady=10)

# ---------- Buttons ----------
tk.Button(
    window,
    text="Calculate BMI",
    command=calculate_bmi,
    bg="green",
    fg="white"
).pack(pady=10)

tk.Button(
    window,
    text="Clear",
    command=clear_fields,
    bg="orange"
).pack(pady=5)

tk.Button(
    window,
    text="About",
    command=show_info,
    bg="blue",
    fg="white"
).pack(pady=5)

# ---------- Result ----------
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 12),
    fg="blue",
    bg="lightblue"
)
result_label.pack(pady=10)

# ---------- Run ----------
window.mainloop()
