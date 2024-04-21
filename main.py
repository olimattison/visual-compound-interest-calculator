import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


def calculate_compound_interest():
    try:
        P = float(principal_entry.get())
        r = float(rate_entry.get()) / 100
        t = float(time_entry.get())
        n = float(compound_entry.get())

        if P <= 0 or r < 0 or t <= 0 or n <= 0:
            raise ValueError("All inputs must be positive numbers.")

        times = np.arange(0, t + 1, 1 / n)
        amounts = P * (1 + r / n) ** (n * times)

        ax.clear()
        global line
        line, = ax.plot(times, amounts, label=f"P={P}, r={r * 100}%, t={t}, n={n}")
        ax.set_title('Compound Interest Growth Over Time')
        ax.set_xlabel('Time (years)')
        ax.set_ylabel('Amount ($)')
        ax.set_ylim([0, max(amounts) * 1.1])
        ax.legend()
        canvas.draw_idle()
        clear_error()
    except ValueError as e:
        print(f"input error: {e}")
        display_error("please fix your input")
    except Exception as e:
        print(f"an unexpected error occurred: {e}")
        display_error("unexpected error")


def on_motion(event):
    try:
        if event.inaxes == ax and len(line.get_xdata()) > 0:
            x, y = event.xdata, event.ydata
            distances = np.sqrt((line.get_xdata() - x)**2 + (line.get_ydata() - y)**2)
            index = np.argmin(distances)
            x, y = line.get_xdata()[index], line.get_ydata()[index]
            coords_label.configure(text=f"Time: {x:.2f} years, Amount: ${y:.2f}")
    except Exception as e:
        print(f"Unexpected error: {e}")


def display_error(message):
    error_label.configure(text=message)
    error_label.grid()


def clear_error():
    error_label.configure(text="")
    error_label.grid_remove()


app = ctk.CTk()
app.title("Compound Interest Calculator")

frame_left = ctk.CTkFrame(app)
frame_left.grid(row=0, column=0, padx=20, pady=20)

ctk.CTkLabel(frame_left, text="Principal ($):").grid(row=0, column=0)
principal_entry = ctk.CTkEntry(frame_left, placeholder_text="Principal ($)")
principal_entry.grid(row=0, column=1, pady=10)

ctk.CTkLabel(frame_left, text="Annual Rate (%):").grid(row=1, column=0)
rate_entry = ctk.CTkEntry(frame_left, placeholder_text="Annual Rate (%)")
rate_entry.grid(row=1, column=1, pady=10)

ctk.CTkLabel(frame_left, text="Time (years):").grid(row=2, column=0)
time_entry = ctk.CTkEntry(frame_left, placeholder_text="Time (years)")
time_entry.grid(row=2, column=1, pady=10)

ctk.CTkLabel(frame_left, text="Compounds per Year:").grid(row=3, column=0)
compound_entry = ctk.CTkEntry(frame_left, placeholder_text="Compounds per Year")
compound_entry.grid(row=3, column=1, pady=10)

calculate_button = ctk.CTkButton(frame_left, text="Calculate", command=calculate_compound_interest)
calculate_button.grid(row=4, column=0, columnspan=2, pady=20)

coords_label = ctk.CTkLabel(frame_left, text="Hover over the graph for details")
coords_label.grid(row=5, column=0, columnspan=2, pady=20)

error_label = ctk.CTkLabel(frame_left, text="", text_color="red")
error_label.grid(row=6, column=0, columnspan=2, pady=20)

frame_right = ctk.CTkFrame(app)
frame_right.grid(row=0, column=1, padx=20, pady=20)

fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
line, = ax.plot([], [], picker=5)
canvas = FigureCanvasTkAgg(fig, master=frame_right)
canvas.draw()
canvas.get_tk_widget().pack()
canvas.mpl_connect('motion_notify_event', on_motion)


app.mainloop()
