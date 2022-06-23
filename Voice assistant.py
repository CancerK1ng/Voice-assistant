import pyttsx3
import wikipedia


Suzi = pyttsx3.init()

In = input('Search Wikipedia/Goodle: ')

res = wikipedia.summary(In, sentences = 2)

  # rate = Suzi.getProperty('rate')
  # Suzi.setProperty('rate', rate - 50)
  # volume = Suzi.getProperty('volume')
  # Suzi.setProperty('volume', 0.6)

print(res)

Suzi.say(res)
Suzi.runAndWait()


