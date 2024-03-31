from forex_python.converter import CurrencyRates
import tkinter as tk

window = tk.Tk()
window.title("Currency Converter")
window.geometry("700x400")
window.configure(background="lightblue")

# Function to handle currency conversion
def convert_currency():
    try:
        amount = float(amount_entry.get())
        cur1 = from_currency_entry.get().upper()
        cur2 = to_currency_entry.get().upper()
        converter = CurrencyRates()
        result = converter.convert(cur1, cur2, amount)
        result_label.config(text=f"{result:.2f} {cur2}")
    except ValueError:
        result_label.config(text="Invalid amount")
    except Exception as e:
        result_label.config(text=str(e))

# Function to handle Enter key press event
def on_enter_pressed(event):
    convert_currency()

# Styling options
font_style = "Arial"
label_font_size = 18
entry_font_size = 14
button_font_size = 14

# Labels
label1 = tk.Label(window, text="Currency Converter", font=(font_style, label_font_size, "bold"), bg="red", fg="white")
label1.place(x=50, y=30)

label2 = tk.Label(window, text="Enter amount:", font=(font_style, label_font_size), bg="lightblue")
label2.place(x=50, y=80)

label3 = tk.Label(window, text="From Currency:", font=(font_style, label_font_size), bg="lightblue")
label3.place(x=50, y=120)

label4 = tk.Label(window, text="To Currency:", font=(font_style, label_font_size), bg="lightblue")
label4.place(x=50, y=160)

# Entry fields
amount_entry = tk.Entry(window, font=(font_style, entry_font_size))
amount_entry.place(x=230, y=85)
amount_entry.focus_set()  # Set focus to the amount entry field by default

from_currency_entry = tk.Entry(window, font=(font_style, entry_font_size))
from_currency_entry.place(x=230, y=125)

to_currency_entry = tk.Entry(window, font=(font_style, entry_font_size))
to_currency_entry.place(x=230, y=165)

# Conversion button
convert_button = tk.Button(window, text="Convert", command=convert_currency, font=(font_style, button_font_size, "bold"))
convert_button.place(x=230, y=210)

# Result label
result_label = tk.Label(window, text="", font=(font_style, label_font_size, "bold"), fg="blue", bg="lightblue")
result_label.place(x=50, y=260)

# Bind Enter key to perform conversion when entry fields are focused
amount_entry.bind("<Return>", on_enter_pressed)
from_currency_entry.bind("<Return>", on_enter_pressed)
to_currency_entry.bind("<Return>", on_enter_pressed)

window.mainloop()
