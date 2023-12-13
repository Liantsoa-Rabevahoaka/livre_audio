import pyttsx3
from PyPDF2 import PdfReader

droid = pyttsx3.init()
droid.say('Bonjour Jojo, je suis un android de la 3eme generation et je suis Alexia')
droid.say('Maintenant tu peux te relaxer et ecouter tranquillement')

livre = open('test.pdf', 'rb')
lecture = PdfReader(livre)
pages = len(lecture.pages)
print(pages)

page_number = 2  # Choisir le numéro de la page que vous souhaitez lire (commençant à 0 pour la première page)
debut_lecture = lecture.pages[page_number]
texte = debut_lecture.extract_text()
droid.say(texte)
droid.runAndWait()
