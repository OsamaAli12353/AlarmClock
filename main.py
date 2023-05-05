import datetime
import winsound
from tkinter import *


def set_time():
    global alarm_time
    hours = int(hours_text.get("1.0", END))
    minutes = int(minutes_text.get("1.0", END))
    input_time = datetime.datetime.now().replace(hour=hours, minute=minutes, second=0, microsecond=0)

    if input_time < datetime.datetime.now():
        #add 24 hours on the inputtime
        input_time += datetime.timedelta(hours=24)

    alarm_time = input_time
    update_label()


def cancel_alarm():
    global alarm_time
    alarm_time = None
    my_label.config(text="Alarm canceled")


def update_label():
    global alarm_time
    if alarm_time:
        remaining_time = alarm_time - datetime.datetime.now()

        if remaining_time.total_seconds() <= 0:
            my_label.config(text="Time's up!")
            # play a sound
            winsound.PlaySound("alarm-clock-short-6402.mp3", winsound.SND_FILENAME)
        else:
            hours, remaining_minutes = divmod(int(remaining_time.total_seconds()), 3600)
            minutes, seconds = divmod(remaining_minutes, 60)

            my_label.config(text="Remaining time: {:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
            root.after(1000, update_label)


root = Tk()
root.title("Alarm Clock")
root.geometry("400x300")

time_frame = Frame(root)
time_frame.pack(pady=20)

hours_text = Text(time_frame, width=5, height=1, font=("Arial", 16))
hours_text.pack(side=LEFT, padx=5)

minutes_text = Text(time_frame, width=5, height=1, font=("Arial", 16))
minutes_text.pack(side=LEFT, padx=5)

button_frame = Frame(root)
button_frame.pack()

set_time_button = Button(button_frame, text="Set Alarm", font=("Arial", 16), command=set_time)
set_time_button.grid(row=0, column=0, padx=20)

cancel_button = Button(button_frame, text="Cancel Alarm", font=("Arial", 16), command=cancel_alarm)
cancel_button.grid(row=0, column=1, padx=20)

my_label = Label(root, text='', font=("Arial", 16))
my_label.pack(padx=20)

alarm_time = None

root.mainloop()
