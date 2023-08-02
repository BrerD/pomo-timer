## Animedoro Timer App
## By Brer D.

## Library Imports
import datetime
import time
import tkinter as tk
import tkinter.ttk as ttk

## Main GUI
root = tk.Tk()
root.geometry('200x350')
root.title('Animedoro Timer')


## Global Variables
total_pom = 0
breaks = 0

studymin = tk.IntVar()
breakmin = tk.IntVar()

## Timer Functions

def pomo_timer(studymin, breakmin):
    
    global breaks
    global total_pom
    
    study = studymin
    breaktime = breakmin
    
    # Start the timer.
    start = datetime.datetime.now()

    # While the timer is running, print the current time.
    while datetime.datetime.now() < start + datetime.timedelta(minutes=int(study)):
        time_label.configure(text= datetime.datetime.now())


    
    # Take a break.
    time.sleep(breaktime)
    breaks +=1
    t_pom_label.configure(text="Total Pomodoros: " + str(total_pom))
    t_break_label.configure(text="Total Breaks: " + str(breaks))

    

def start_pomodoro():
    global pomo_timer
    global total_pom
    root.config(cursor="arrow")
    total_pom += 1
    study = studymin.get()
    break_min = breakmin.get()
    pomo_timer(study,break_min)
    if study == True:
        animedorotimerdisplay.configure(text="Time To Study!")
    elif study == False:
        animedorotimerdisplay.configure(text="Take A Break!")
    else:
        animedorotimerdisplay.configure(text="I'm Ready When You Are")
    
    
    
def progress_bar (studymin, breakmin):
    total_time = studymin + breakmin
    study_remain = studymin - total_time
    break_remain = breakmin - total_time
    per_of_study = study_remain / total_time * 100
    per_of_break = break_remain / total_time * 100
    perStu = str(int(per_of_study))
    perBre = str(int(per_of_break))
    phasetimerdisplay.start()
    
    ## Update the progress bar
    if datetime.datetime.now() < datetime.timedelta(minutes=studymin):
        phasetimerdisplay.step(float(perStu)/100)
            
    else:
        phasetimerdisplay.step(float(perBre)/100)
    phasetimerdisplay.stop()
        
## Timer Frame

timer_frame = tk.Frame(root)
timer_frame.pack(pady=10)

# Study Minutes Label and Entry Box
study_label = tk.Label(timer_frame, justify="center", text="Study Time :")
study_label.pack(padx=20)
# create a variable to store the input value of study minutes
study_entrybox = tk.Entry(timer_frame, width=10, textvariable=studymin)
study_entrybox.pack()

# Study Minutes Label and Entry Box
break_label = tk.Label(timer_frame, justify="center", text="Break Time :")
break_label.pack(padx=20)
# create a variable to store the input value of study minutes
break_entrybox = tk.Entry(timer_frame, width=10, textvariable=breakmin)
break_entrybox.pack()

animedorotimerdisplay = tk.Label(root, text="")
animedorotimerdisplay.pack()
phasetimerdisplay = ttk.Progressbar(root, orient="horizontal", mode="indeterminate", length=200)
phasetimerdisplay.pack()

# Animedoro Button
animedoro_button = tk.Button(root, text="Let's Begin", underline="1", command=start_pomodoro)
animedoro_button.pack()

## Total Pomodoros Label
t_pom_label = tk.Label(root, text="Total Pomodoros: " + str(total_pom), justify="center")
t_pom_label.pack(padx=5)
t_break_label = tk.Label(root,justify="center",text="Total Breaks: " + str(breaks))
t_break_label.pack(padx=5)

## Time Label
time_label = tk.Label (root, justify="center", text="")
time_label.pack(padx=5)

root.mainloop()