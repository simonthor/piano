from pysinewave import SineWave
import time
import tkinter as tk


mainWindow = tk.Tk()
mainFrame = tk.Frame(mainWindow, bg="white")
mainWindow.title("Guitar!")

mainFrame.pack(expand=True, fill=tk.BOTH)

selectedNotes = []
selectedButtons = []


def addToChord(fretPitch, pressedFret):
    selectedNotes.append (fretPitch)
    selectedButtons.append (pressedFret)
    pressedFret.config (bg="red")


def playChord():
    activeSinewaves = []

    for pitchForPlay in selectedNotes:
        sinewave = SineWave(pitch=pitchForPlay)
        activeSinewaves.append (sinewave)
        sinewave.play()

    time.sleep(2)

    for sinewave, button in zip(activeSinewaves, selectedButtons):
        sinewave.stop()
        button.config(bg='grey')

    selectedButtons.clear()
    selectedNotes.clear ()

maxFrets = 6
maxStrings = 6
fretWidth = 100
fretHeight = 25
stringSpacing = 35
openPitch = -7
for stringNumber in range(maxStrings):

    for fretNumber in range(maxFrets):
        note = tk.Button(mainFrame)
        note.place(x=fretNumber * fretWidth, y=(stringNumber) * stringSpacing, height=fretHeight, width=fretWidth)
        note.config(bg="grey", command=lambda fretPitch = openPitch + fretNumber, pressedFret = note: addToChord(fretPitch, pressedFret), text=str(openPitch + fretNumber))

    if stringNumber % 6 == 3:
        openPitch += 4
    else:
        openPitch += 5


playChordButton = tk.Button(text='Play Chord', bg="blue", command=playChord)
playChordButton.place(x=(fretNumber+1)*fretWidth, y=0, height=stringSpacing*maxStrings, width=2*fretWidth)

mainWindow.geometry(f"{maxFrets * fretWidth + 2*fretWidth}x{stringSpacing * maxStrings}")

tk.mainloop()
