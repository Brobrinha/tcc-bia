import speech_recognition as sr
import time
import os

def callback(microfone, audio):
    try:
        global background
        background = microfone.recognize_google(audio,language='pt-BR')

        if 'Bia' in background:
            stop_listening(wait_for_stop=False)
            #mostra pra falar alguma coisa
            print('Olá, como posso ajudar?')
            #armazena o que foi falado
            audio = microfone.listen(source)

            try:
                fala = microfone.recognize_google(audio,language='pt-BR')
                print('Você disse: ' + fala)

                if (('abrir' or 'abra') and ('Google' or 'navegador')) in fala:
                    os.startfile('chrome.exe')
                    print('Abrindo o Google')
                    voz()
                    
                if (('bloco'and'notas') or ('notepad')) in fala:
                    os.startfile('notepad.exe')
                    print('Abrindo o Bloco de Notas')
                    voz()

                if ('parar' and 'programa') in fala:
                    print('Desligando o Sistema...')
                    microfone.__exit__
                    #stop_listening(wait_for_stop = False)
                
                else:
                    print('Desculpe, não consegui entender. Fale novamente por favor.')
                    voz()

            except sr.UnknownValueError():
                print('Não entendi')
            return fala

    except:
        sr.UnknownValueError()
        print('a')
        voz()

def voz():
    global microfone
    global source
    global stop_listening
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        #ajustando microfone
        microfone.adjust_for_ambient_noise(source)

    #microfone em background
    stop_listening = microfone.listen_in_background(source, callback)
    while True: time.sleep(0.1)
    
voz()