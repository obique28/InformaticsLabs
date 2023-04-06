import tkinter as tk

root = tk.Tk()
root.title("Task 1")

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

label1 = tk.Label(root, text='Calculate the average number')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type your numbers')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)
text_label = tk.Label(root, font=('helvetica', 10))


def get_average():
    values = entry1.get()

    lst = []
    font_colour = "black"
    try:
        for value in values.split(","):
            striped_value = value.strip()
            try:
                if striped_value:
                    float_value = float(striped_value)
                    lst.append(float_value)
            except Exception:
                raise Exception(f"This value '{striped_value}' is unsupported. Please enter correct number")
        avg = sum(lst) / len(lst)
        text = f'Average values is: {avg}'
    except Exception as e:
        font_colour = "red"
        text = str(e)
    text_label.config(text=text, fg=font_colour)
    canvas1.create_window(200, 210, window=text_label)


button1 = tk.Button(text='Calculate', command=get_average, bg='brown', fg='white',
                    font=('helvetica', 9, 'bold'))
canvas1.create_window(200, 180, window=button1)

root.mainloop()
