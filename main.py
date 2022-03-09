from STT import SpeechToText
from TTS import TextToSpeech
from Translate import Translator


stt = SpeechToText()
tts = TextToSpeech()
translate = Translator()
    
text = input("Digite o nome do arquivo:\n")
text_reconized = stt.read(text)

print(f'Original -> {text_reconized}')

translated = translate.translate(text_reconized, "pt", "en")

print(f'Translated -> {translated}')

tts.speech(translated)