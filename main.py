from tkinter import Entry, Label, Button, Tk, END

FONT = ("Arial", 12, "normal")


def convert_miles_to_kms():
    kms = float(miles_entry.get()) * 1.609344
    output_label.config(text=f"{'%.2f' % kms}")


window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

miles_entry = Entry(width=7)
miles_entry.grid(column=1, row=0)
miles_entry.insert(END, string="0")

miles_label = Label(text="miles", font=FONT)
miles_label.grid(column=2, row=0)

equals_label = Label(text="is equal to", font=FONT)
equals_label.grid(column=0, row=1)

output_label = Label(text="0", font=FONT)
output_label.grid(column=1, row=1)

kms_label = Label(text="KMs", font=FONT)
kms_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=convert_miles_to_kms)
calculate_button.grid(column=1, row=2)

window.mainloop()
