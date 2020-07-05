import pandas as pd
import winsound as ws
import tkinter as tk


def playNote(buttonText):
    noteFreq = notes.loc[buttonText, 1]
    ws.Beep(noteFreq, 500)


notes = pd.read_csv('note_frequencies.csv', index_col=0, skiprows=36, nrows=36)
notes.columns = (1,)
print(notes)

mainWindow = tk.Tk()
mainFrame = tk.Frame(mainWindow, bg="white")
mainWindow.title("Piano!")

mainFrame.pack(expand=True, fill=tk.BOTH)

vitEllerSvart = [0,1,0,1,0,0,1,0,1,0,1,0]
whiteCounter = 0
for i, (noteName, noteFreq) in enumerate(notes.iterrows()):
    tile = tk.Button(mainFrame, command=lambda noteName=noteName: playNote(noteName))

    if vitEllerSvart[i % 12]:
        tile.place(x=whiteCounter*20-5, y=0, height=50, width=10)
        tile.config(bg="black")
    else:
        tile.place(x=whiteCounter*20, y=0, height=100, width=20)
        tile.config(bg="white")
        tile.lower()
        whiteCounter += 1

mainWindow.geometry(f"{whiteCounter*20}x100")

tk.mainloop()
