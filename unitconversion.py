import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random

# Fun facts for display
fun_facts = [
    "Did you know? Lightning is five times hotter than the sun.",
    "Fun Fact: Water expands by 9% when it freezes.",
    "Interesting! A bolt of lightning lasts less than a second but reaches temperatures of 30,000 Kelvins.",
    "Trivia: The Eiffel Tower can be 15 cm taller during the summer.",
    "Quick Fact: Octopuses have three hearts!",
]

# Unit conversion data
units = {
    'Data Size': {
        'Byte': 1,
        'Kilobyte': 1024,
        'Megabyte': 1024 ** 2,
        'Gigabyte': 1024 ** 3,
        'Terabyte': 1024 ** 4
    },
    'Length': {
        'Meter': 1,
        'Kilometer': 1000,
        'Inch': 0.0254,
        'Mile': 1609.34,
        'Centimeter': 0.01,
        'Millimeter': 0.001,
        'Yard': 0.9144,
        'Foot': 0.3048
    },
    'Mass': {
        'Gram': 0.001,
        'Kilogram': 1,
        'Milligram': 1e-6,
        'Microgram': 1e-9,
        'Tonne': 1000,
        'Ounce': 0.0283495,
        'Pound': 0.453592,
        'Stone': 6.35029,
    },
    'Time': {
        'Second': 1,
        'Millisecond': 1e-3,
        'Microsecond': 1e-6,
        'Nanosecond': 1e-9,
        'Minute': 60,
        'Hour': 3600,
        'Day': 86400,
        'Week': 604800,
        'Year': 31557600
    },
    'Speed': {
        'Meter per second': 1,
        'Kilometer per hour': 1000 / 3600,
        'Mile per hour': 1609.34 / 3600,
        'Feet per second': 0.3048,
        'Knots': 1852 / 3600
    },
    'Area': {
        'Square Kilometer': 1_000_000,
        'Square Meter': 1,
        'Square Mile': 2_589_988.11,
        'Square Yard': 0.836127,
        'Square Foot': 0.092903,
        'Square Inch': 0.00064516,
        'Hectare': 10_000,
        'Acre': 4046.86
    }
}

# Initialize conversion history
conversion_history = []

# Function to perform conversion
def convert_units(unit_type, from_unit, to_unit, value):
    if from_unit in units[unit_type] and to_unit in units[unit_type]:
        result = (value * units[unit_type][from_unit]) / units[unit_type][to_unit]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conversion_record = {
            "timestamp": timestamp,
            "unit_type": unit_type,
            "from_unit": from_unit,
            "to_unit": to_unit,
            "value": value,
            "result": result
        }
        conversion_history.append(conversion_record)
        display_fun_fact()  # Show a random fun fact after conversion
        return result
    else:
        raise ValueError("Invalid unit conversion.")

# Display a random fun fact
def display_fun_fact():
    fact = random.choice(fun_facts)
    messagebox.showinfo("Fun Fact", fact)

# Main GUI Application
class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter with Fun Facts")

        # Labels and dropdowns for unit type selection
        tk.Label(root, text="Unit Type:").grid(row=0, column=0, padx=10, pady=5)
        self.unit_type_var = tk.StringVar()
        self.unit_type_menu = tk.OptionMenu(root, self.unit_type_var, *units.keys(), command=self.update_units)
        self.unit_type_menu.grid(row=0, column=1, padx=10, pady=5)

        # Entry and labels for value and units
        tk.Label(root, text="Value:").grid(row=1, column=0, padx=10, pady=5)
        self.value_entry = tk.Entry(root)
        self.value_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="From Unit:").grid(row=2, column=0, padx=10, pady=5)
        self.from_unit_var = tk.StringVar()
        self.from_unit_menu = tk.OptionMenu(root, self.from_unit_var, "")
        self.from_unit_menu.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="To Unit:").grid(row=3, column=0, padx=10, pady=5)
        self.to_unit_var = tk.StringVar()
        self.to_unit_menu = tk.OptionMenu(root, self.to_unit_var, "")
        self.to_unit_menu.grid(row=3, column=1, padx=10, pady=5)

        # Convert button
        self.convert_button = tk.Button(root, text="Convert", command=self.perform_conversion)
        self.convert_button.grid(row=4, column=1, padx=10, pady=10)

    def update_units(self, *args):
        unit_type = self.unit_type_var.get()
        if unit_type in units:
            from_units = list(units[unit_type].keys())
            self.from_unit_menu["menu"].delete(0, "end")
            self.to_unit_menu["menu"].delete(0, "end")
            for unit in from_units:
                self.from_unit_menu["menu"].add_command(label=unit, command=tk._setit(self.from_unit_var, unit))
                self.to_unit_menu["menu"].add_command(label=unit, command=tk._setit(self.to_unit_var, unit))

    def perform_conversion(self):
        try:
            unit_type = self.unit_type_var.get()
            from_unit = self.from_unit_var.get()
            to_unit = self.to_unit_var.get()
            value = float(self.value_entry.get())
            result = convert_units(unit_type, from_unit, to_unit, value)
            messagebox.showinfo("Conversion Result", f"{value} {from_unit} = {result:.3f} {to_unit}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Run the application
root = tk.Tk()
app = ConverterApp(root)
root.mainloop()