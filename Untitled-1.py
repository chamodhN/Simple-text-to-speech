import tkinter as tk
import text_to_speech as speech


def speak_the_text():
    message = entry1.get()
    entry1.delete(0,tk.END)
    speech.speak(message,'en')
window = tk.Tk()
window.title('simple text to speech')
entry1 = tk.Entry(window)
speak = tk.Button(window,text='speak',command=speak_the_text)
speak.pack(side='bottom')
entry1.pack(side='top')

tk.mainloop()