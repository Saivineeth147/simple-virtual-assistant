from tkinter import *
import wikipedia
import wolframalpha
import speech_recognition as sr
import pyaudio
import pyspeech

class gui:

 def __init__(self):
        frame=Frame(root,width=600,height=0)
        frame.pack()
        self.label_1 = Label(root, text="Ask your Question:")
        self.entry_1 = Entry(root)
        self.entry_1.bind("<Return>",self.virtual)
        self.label_1.pack(side=LEFT,pady=20)
        self.entry_1.pack(side=LEFT,fill=X,pady=20,padx=10,expand=TRUE)
        self.entry_1.focus_set()

 def virtual(self,event):


   r = sr.Recognizer()
   with sr.Microphone() as source:
                  audio = r.listen(source)
   try:

     self.entry_1.insert(0,r.recognize_google(audio)) # press enter and then start speaking 
   except sr.UnknownValueError:
                   print("google speech could not understand audio")
   except sr.RequestError as e:
                   print("Could not request results from Google Speech Recognition service; {0}".format(e))

   value = self.entry_1.get()
   value = value.lower()
   try:
                   app_id = "some api" # add your APi
                   client = wolframalpha.Client(app_id)
                   res = client.query(value)
                   answers = next(res.results).text
                   print(answers)

   except:
                  print(wikipedia.summary(value,sentences=2))

root=Tk()
root.wm_title("Hi,i am Karen your personal assistant")
b=gui()
root.mainloop()
