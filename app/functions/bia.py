import speech_recognition as sr
import pyttsx3
import time
import os
import psutil

vozSistema = pyttsx3.init()

def callback(microfone, audio):
    
    try:
        global background
        background = microfone.recognize_google(audio,language='pt-BR')

        if 'Bia' in background:
            print('Olá, como posso ajudar?')
            stop_listening(wait_for_stop=False)
            #mostra pra falar alguma coisa
            audio = microfone.listen(source)

            try:
                fala = microfone.recognize_google(audio,language='pt-BR')
                fala = fala.upper()
                print('Você disse: ' + fala)

                #Códigos para Ligar:
                if fala in ['ABRIR GOOGLE', 'ABRIR O GOOGLE', 'ABRA O GOOGLE', 'ABRA O CHROME']:
                    os.startfile('chrome.exe')
                    vozSistema.say('Ok, estou abrindo o Google para você')
                    print('Abrindo o Google')
                    vozSistema.runAndWait()
                    voz()
                    
                if fala in ['ABRIR BLOCO DE NOTAS', 'ABRIR O BLOCO DE NOTAS', 'ABRIR O NOTEPAD', 'ABRIR NOTEPAD', 'ABRA O BLOCO DE NOTAS', 'ABRA O NOTEPAD']:
                    os.startfile('notepad.exe')
                    print('Abrindo o Bloco de Notas')
                    #vozSistema.say('Abrindo o Bloco de Notas')
                    #vozSistema.runAndWait()
                    voz()

                if fala in ['ABRIR O ARQUIVO EXEMPLO']:
                    os.startfile(r'C:\Users\User\Downloads\tcc-bia\python\exemplo.docx')
                    print('''Abrindo arquivo Word "Exemplo.docx" ''')
                    voz()

                if ('jogo' and 'silencioso') in fala:
                    os.startfile(r'C:\Users\User\Downloads\tcc-bia\python\mia-e-o-mundo-silêncioso.lnk')
                    print('Abrindo o jogo: Mia e o mundo silêncioso')
                    voz()

                #Códigos para desligar:
                if fala in ['FECHAR O GOOGLE', 'FECHAR GOOGLE', 'FECHAR CHROME', 'FECHAR O CHROME']:
                    fecha = "chrome.exe" in (i.name() for i in psutil.process_iter())
                    if (fecha==True):
                        os.system("taskkill /im chrome.exe")
                        print("Fechando o Google")
                    else:
                        print("Não está aberto")
                    voz()
                
                if fala in ['FECHAR BLOCO DE NOTAS', 'FECHAR NOTEPAD']:
                    os.system("taskkill /im notepad.exe")
                    print('Fechando o Bloco de Notas')

                if fala in ['FECHAR EXEMPLO']:
                    os.system("taskkill /im exemplo.docx")
                    print('''Fechando o Arquivo "Exemplo" ''')

                if fala in ['FECHAR JOGO']:
                    os.system("taskkill /im mia-e-o-mundo-silêncioso.lnk")
                    print('''Fechando o Jogo "Mia e o Mundo Silêncioso"''')

                if fala in ['PARAR PROGRAMA']:
                    print('Desligando o Sistema')
                    microfone.__exit__
                    #stop_listening(wait_for_stop = False)

                else:
                    print('Desculpe, não consegui entender. Fale novamente por favor.')
                    voz()

            except sr.UnknownValueError():
                print('Não entendi')
                voz()
            return fala
            
    except:
        sr.UnknownValueError()
        print('Aguardando comando...')
        voz()

def voz():
    
    # escutando voz:
    global microfone
    global source
    global stop_listening
    # voz do sistema: 
    ###global vozSistema
    
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        #ajustando microfone
        microfone.adjust_for_ambient_noise(source)

    #microfone em background
    stop_listening = microfone.listen_in_background(source, callback)
    while True: time.sleep(0.1)

voz()