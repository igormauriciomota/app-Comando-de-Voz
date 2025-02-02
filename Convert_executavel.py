'''______________________________Converter python em exe______________________________'''

# Converter python em exe

#pip install pyinstaller

#Terminal: pyinstaller nomedoarquivo.py (diretório, Extras/Voz_executável_e_comandos_extras.py)
#Terminal: pyinstaller --onefile nomedoarquivo.py

# >> pyinstaller --onefile Convert_executavel.py

#Contendo janelas: Terminal: pyinstaller --onefile -w nomedoarquivo.py

import os

import pyttsx3
import speech_recognition as sr


class Comandos:
    def __init__(self):
        # Inicializa o sintetizador de voz uma vez
        self.engine = pyttsx3.init()
        self.rec = sr.Recognizer()

    def assistente_ouvir(self):
        with sr.Microphone() as source:
            print('Fale...')
            self.rec.pause_threshold = 0.6
            try:
                audio = self.rec.listen(source)
                print('Reconhecendo voz...')
                palavras = self.rec.recognize_google(audio, language='pt-br').lower()
                print(f"Frase dita: '{palavras}'")
                return palavras
            except sr.UnknownValueError:
                print('Não foi possível entender o áudio.')
            except sr.RequestError:
                print('Erro na conexão com o serviço de reconhecimento de voz.')
        return None

    def assistente_falar(self, falar):
        self.engine.say(falar)
        self.engine.runAndWait()

    def assistente_acoes(self):
        while True:
            frase = self.assistente_ouvir()
            if frase:
                if "bloco de notas" in frase:
                    print("Abrindo bloco de notas...")
                    self.assistente_falar("Abrindo bloco de notas!")
                    os.system("start notepad")

                elif "navegador" in frase:
                    print("Abrindo navegador...")
                    self.assistente_falar("Abrindo navegador!")
                    os.system("start https://www.google.com.br/")

                elif "word" in frase:
                    print("Abrindo Word...")
                    self.assistente_falar("Abrindo Word!")
                    os.system("start winword")

                elif "excel" in frase:
                    print("Abrindo Excel...")
                    self.assistente_falar("Abrindo Excel!")
                    os.system("start excel")


if __name__ == '__main__':
    assistente = Comandos()
    assistente.assistente_acoes()
