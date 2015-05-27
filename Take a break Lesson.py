import time
import webbrowser

break_time = 3600
breaks = 0

while breaks < 3:
    time.sleep(break_time)
    webbrowser.open("https://www.youtube.com/watch?v=VrKNb5uwjxQ")
    breaks +=1
