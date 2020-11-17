import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia
import playsound
warnings.filterwarnings('ignore')

def recordAudio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('rekni neco')
        audio = r.listen(source)
    
    data = ''
    try:
        data = r.recognize_google(audio, language="cs")
        print('rekl si: '+data)
    except sr.UnknownValueError:
        print('neco se pokozilo')
    except sr.RequestError as e:
        print('pokazilo se :'+e)
    return data

def assistentresponse(text):
    print(text)
    myobj = gTTS(text= text, lang='cs', slow=False)
    myobj.save('asisv.mp3')
    playsound.playsound('asisv.mp3', True)
    os.remove('asisv.mp3')
def wakeworld(text):
    WAKE_WORDS = ['péťo', 'hej péťo', 'Hej Péťo']
    text = text.lower()
    for phrase in WAKE_WORDS:
        if phrase in text:
            print('>')
            return True
    print('<')
    return False 
def getdate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    monthnum = now.month
    daynum = now.day
    mounth_names = ['leden', 'únor', 'březen', 'duben', 'květen', 'červen', 'červenec', 'srpen', 'září', 'říjen', 'listopad', 'prosinec']
    return 'dnes je '+ mounth_names[monthnum - 1]+' '+str(daynum)

def privitani(text):
    imputp = ['ahoj','čau', 'Ahoj']
    outputp = ['ahoj','ahoj jak se máš']
    for word in text.split():
        if word.lower() in imputp:
            return random.choice(outputp)
    return ''


def vtip():
    assistentresponse('tahle funkce ještě není dodělaná. pokud chcete přidat nějaký vtip napište mému vývojáři.')
    vtipy = ['Manželka volá manželovi do práce a manžel rychle říká: Hele, my tu teď máme strašně moc práce, takže nemám čas. A v tom manželka vtrhne manželovi do řeči a říká. Já mám pro tebe jednu dobrou a špatnou zprávu. Tak mi teda řekni aspoň tu dobrou. říká manžel. A manželka říká: fungují nám airbagy!!!!',
            'Manželka: Uz vím co bych chtela k narozeninám. Přeju si ten nový mobil! Manžel: A nemužeš si přát něco splnitelnějšího? Manželka: Tak stačilo by mi kdybys tolik nechlastal!!!! Manžel: A chceš k němu i nabiječku?']

    
    responce = random.choice(vtipy)
    return responce






assistentresponse('ahoj jsem Péťa tvoje osobní asistentka.')
#hlavní příkazy
while True:
    text = recordAudio()
    responce = ''
    if (wakeworld(text) == True):
        responce = responce + privitani(text)
        if('Jaký je den' in text):
            get_date = getdate()
            responce = responce + '' + get_date
        if('jak se máš' in text):
            slova = ['mám se dobře', 'mám se fajn', 'jde to']
            responce = random.choice(slova)
        if('děkuji' in text):
            responce = 'nemáš zač'
        if('Wikipedie' in text):
            responce = 'tahle funkce ještě není dostupná'
        if('Kdo tě vyrobil' in text):
            print('mobilex1122')
        if('Řekni mi vtip' in text):
            responce = vtip()
        if('co umíš' in text):
            responce = 'umím ti říct vtip, kolikátého je a pozdravit tě. výce funkcí výjde v budoucnu. pokud máte nápad na novou funkcy napyšte mému vývojářy'
        if responce != '':
            assistentresponse(responce)