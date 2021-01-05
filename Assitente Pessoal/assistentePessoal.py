import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import sys
import pyjokes
import os
import webbrowser
import re
import threading
import time
from googlesearch import search
import subprocess
import pyautogui
import winapps 

global language
language = 2
listener = sr.Recognizer()
engine = pyttsx3.init('sapi5')
"""escolhe o idioma do assistente"""
def detect_language():
    global language
    """por enquanto só tem 3 linguas 0 - homem ingles, 1 - mulher ingles, 2 - mulher portugues e eu deixo 2 como default
    also eu tirei esses valores de uma funcao do pyttsx3 onde ele lista as voices que ele possui"""
    language = 2
    novaLinguagem = input()
    if novaLinguagem == 'english':
        language = 1
    elif novaLinguagem == 'english male':
        language = 0

def standby():
    """fica ouvindo o mic mas não faz nada até reconhece a palavra de ativação"""
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[language].id)
    ouvirAlexo = 'error'
    while ouvirAlexo == 'error':
        try:
            with sr.Microphone() as source:
                if language == 1 or language == 0:
                    voice = listener.listen(source)
                    ouvirAlexo = listener.recognize_google(voice)
                    ouvirAlexo = ouvirAlexo.lower()
                    print(ouvirAlexo)
                    if 'my guy' in ouvirAlexo:
                        talk('ye')
                        run_alexa()
                if language == 2:
                    voice = listener.listen(source)
                    ouvirAlexo = listener.recognize_google(voice, language='pt-BR')
                    ouvirAlexo = ouvirAlexo.lower()
                    print(ouvirAlexo)
                    if 'ativar' in ouvirAlexo:
                        talk('fala túu')
                        run_alexa()
        except:
            pass
"""FUNCIONA MAS PRECISA ARRUMAR ALGUNS DETALHES"""
def abre_programa(nomePrograma):
    application = nomePrograma
    """procura o nome do programa dado para ver se ele está instalado no pc mas as vezes o programa não está na lista de apps instalados
    also tem programas tipo o Unity que o caminho de instalação é none e ai não da pra abrir"""
    for app in winapps.search_installed(application):
        application = str(app.install_location)
    
    """tem programa que o launcher é Overwatch Launcher.exe e outros que é só Chrome.exe então faço a verificação para os dois casos
    não posso abrir qualquer .exe porque na pasta do app tem o desinstalador que é um .exe e ai não é pra rodar nesse caso"""
    noLauncher = application+"\\"+nomePrograma
    noLauncher = noLauncher.replace("\\", "AUXILIAR")
    noLauncher = noLauncher.replace("AUXILIAR", "AUXILIAR\\")
    noLauncher = noLauncher.replace("AUXILIAR", "\\")

    nomeExecutavel = nomePrograma+" launcher.exe"
    launcher = application + "\\"+nomeExecutavel
    launcher = launcher.replace("\\", "AUXILIAR")
    launcher = launcher.replace("AUXILIAR", "AUXILIAR\\")
    launcher = launcher.replace("AUXILIAR", "\\")
    try:
        subprocess.Popen(noLauncher)
        talk("abrindo")
    except:
        try:
            subprocess.Popen(launcher)
            talk("abrindo")
        except:
            talk("programa não encontrado")


def take_command():
    command = 'error'
    while command == 'error':
        try:
            with sr.Microphone() as source:
                if language == 1:
                    voice = listener.listen(source)
                    ouvirAlexo = listener.recognize_google(voice)
                    ouvirAlexo = ouvirAlexo.lower()
                    #command = ouvirAlexo.replace('my guy', '')
                    print(ouvirAlexo)
                if language == 2:
                    voice = listener.listen(source)
                    ouvirAlexo = listener.recognize_google(voice, language='pt-BR')
                    ouvirAlexo = ouvirAlexo.lower()
                    #command = ouvirAlexo.replace('ativar', '')
                    print(ouvirAlexo)
        except:
            pass

    return command

def run_alexa():
    command = take_command()
    
    if language == 1:
        if 'play' in command:
            song = command.replace('play', '')
            talk('ok, playing' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('It is currently '+time)
        elif 'wikipedia' in command or 'who is' in command:
            talk('Give me one moment while I look it up')
            command = command.replace('wikipedia', '')
            command = command.replace('who is', '')
            info = wikipedia.summary(command, 1)
            talk(info)
        elif 'turn off' in command:
            talk('turning off')
            global killPrograma
            killPrograma = 1
        elif 'how much for' in command:
            talk('more than you can afford')
        elif 'open' in command:
            talk('I will open that on your default browser')
            command = command.replace('open', '')
            resultados = []
            for j in search(command, tld="co.in", num=1, stop=1, pause=2): 
                resultados.append(j)
            webbrowser.open_new_tab(resultados[0])
        elif 'search' in command and 'google' in command:
            talk("Sure, give me a second")
            command = command.replace('search', '')
            command = command.replace('google', '')
            command = re.sub(r"\bfor\b",'', command)
            pywhatkit.search(command)
        elif 'send' in command and 'on whats' in command:
            command = command.replace('send','')
            mensagem = command.replace('on whats', '')
            talk("Who should I send to")
            command = take_command()
            talk("Might not be the best idea, but ok")
            if 'lucas' in command:
                threadNova = threading.Thread(target=mandar_mensagem_whats, args=("HERE GOES WHATSAPP NUMBER", mensagem))
                threadNova.start()
            if 'leonardo' in command:
                threadNova = threading.Thread(target=mandar_mensagem_whats, args=("NÃO DEIXAR OS NÚMEROS NA HORA DE PUBLICAR", mensagem))
                threadNova.start()
            if 'adriana' in command:
                threadNova = threading.Thread(target=mandar_mensagem_whats, args=("WHATS NUMBER", mensagem))
                threadNova.start()
        elif 'start' in command:
            if 'unity' in command:
                subprocess.Popen("C:\\Program Files\\Unity\\Hub\\Editor\\2019.4.17f1\\Editor\\Unity.exe")
        else:
            talk('I did not get that')
    if language == 2:
        if 'toca' in command:
            song = command.replace('toca', '')
            talk('ok, tocando' + song)
            pywhatkit.playonyt(song)
        elif 'horas' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            talk('Agora são '+time)
        elif 'wikipédia' in command or 'quem é' in command:
            talk("Deixa eu descobrir que eu te conto")
            wikipedia.set_lang('pt')
            command = command.replace('wikipedia', '')
            command = command.replace('quem é', '')
            info = wikipedia.summary(command, 1)
            talk(info)
        elif 'desliga' in command:
            talk('desligando')
            global encerrarPrograma
            encerrarPrograma = 1
        elif 'quanto custa' in command:
            talk('bem mais do que você tem na carteira')
        elif command == 'abre o site de anime':
            talk('Abrindo no seu browser principal')
            webbrowser.open_new_tab('https://m.wcostream.com/subbed-anime-list')
        elif 'abre o site' in command or 'abra o site' in command or 'abrir o site' in command:
            talk('Abrindo no seu browser principal')
            command = command.replace('abre o site', '')
            command = command.replace('abra o site', '')
            command = command.replace('abrir o site', '')
            resultados = []
            for j in search(command, tld="co.in", num=1, stop=1, pause=2): 
                resultados.append(j)
            webbrowser.open_new_tab(resultados[0])
        elif 'procura' in command and 'google' in command:
            talk('procurando')
            command = command.replace('procura', '')
            command = command.replace('google', '')
            command = re.sub(r"\bno\b",'', command)
            pywhatkit.search(command)
        elif 'manda' in command and 'no whats' in command:
            command = command.replace('manda','')
            mensagem = command.replace('no whats', '')
            talk("Para quem")
            command = take_command()
            if 'lucas' in command:
                threadNova = threading.Thread(target=mandar_mensagem_whats, args=("NUMERO ZAP ZAP", mensagem))
                threadNova.start()
            if 'leonardo' in command:
                threadNova = threading.Thread(target=mandar_mensagem_whats, args=("NUMERO ZAP ZAP", mensagem))
                threadNova.start()
            if 'adriana' in command:
                threadNova = threading.Thread(target=mandar_mensagem_whats, args=("NUMERO ZAP ZAP", mensagem))
                threadNova.start()
        elif 'iniciar' in command:
            command = command.replace("iniciar ", "")
            talk("Tentando abrir o programa "+command)
            abre_programa(command)
        elif 'atualiza' in command:
            if 'call of duty' in command:
                command = "Modern Warfare"
                abre_programa(command)
                codAberto = None
                while codAberto == None:
                    codAberto = pyautogui.locateOnScreen('cod.png')
                botaoUpdate = pyautogui.locateOnScreen('update_button_cod.png')
                if(botaoUpdate != None):
                    pyautogui.click(botaoUpdate)
                    talk("atualizando")
                else:
                    talk('jogo já atualizado')
        elif 'fechar' in command:#ainda não funciona 100%
            """fecha a maior janela que também possui o X branco/cinza, precisa de mais imagens para verificação
            consegue fechar o app da blizzard e o visual studio code por enquanto"""
            pyautogui.click(pyautogui.locateCenterOnScreen('X.png', confidence=.55))
        else:
            talk('Eu não entendi, será que você poderia repetir?')
            run_alexa()

def talk(text):
    engine.say(text)
    engine.runAndWait()

"""função para o futuro onde eu quero poder usar o teclado enquanto falo com o assistente"""
def controle_teclado():
    global encerrarPrograma
    encerrarPrograma = 0
    encerrado = ''
    while encerrado != 'kill':
        encerrado = input()

def loop_assistente():
    global encerrarPrograma, killPrograma
    encerrarPrograma = 0
    killPrograma = 0
    while encerrarPrograma == 0:
        standby()
        if killPrograma == 1:
            break


def mandar_mensagem_whats(pessoa, mensagem):
    timeHora = datetime.datetime.now().hour
    timeMin = datetime.datetime.now().minute
    pywhatkit.sendwhatmsg(pessoa, mensagem, timeHora, timeMin+1, wait_time = 10)

#threads para poder usar o teclado ao mesmo tempo que utiliza o mic para reconhecer comandos
#thread1 = threading.Thread(target=controle_teclado, args=())
#thread1.start()
#detect_language()
loop_assistente()
