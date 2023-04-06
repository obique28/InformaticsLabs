import tkinter as tk

root = tk.Tk()
root.title("Task 2")

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Перевірка атестата на відзнаку')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Введіть середній бал')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)
text_label = tk.Label(root, font=('helvetica', 10))

def get_average():
    canvas1.delete()
    value = entry1.get()

    striped_value = value.strip()
    font_colour = "black"
    if striped_value:
        try:
            mark = float(striped_value)
            if mark > 12 or mark < 1:
                text = "Please enter float value between [0.000001 and 12]"
                font_colour = "red"
            elif mark >= 10:
                text = "Атестат з відзнакою"
            else:
                text = "Атестат без відзнаки"

        except Exception:
            text = f"Це значення '{striped_value}' не підтримується. Введіть правильне число"
            font_colour = "red"

        text_label.config(text=text, fg=font_colour)
        canvas1.create_window(200, 210, window=text_label)


button1 = tk.Button(text='Розрахувати', command=get_average, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
