from playsound import playsound
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from Utils import TTS_UTILS as TTS


class TextToSpeech():
    __authenticator = IAMAuthenticator(TTS.API_KEY)
    __text_to_speech = TextToSpeechV1(
        authenticator=__authenticator
    )
    __text_to_speech.set_service_url(TTS.API_URL)
    __NOT_DEFINED = 99
    __DEFAULT_VOICE = 'pt-BR_IsabelaV3Voice'

    def __validate(self):
        self.__authenticator.validate()

    def list_voices(self):
        self.__validate()
        return self.__text_to_speech.list_voices().get_result()

    def __try_detect_language(self, target_language):
        if target_language == self.__NOT_DEFINED:
            return self.__DEFAULT_VOICE

        all_voices = self.list_voices()
        return next(
            (
                voice['name']
                for voice in all_voices['voices']
                if target_language in voice['language']
            ),
            self.__DEFAULT_VOICE,
        )

    def speech(self, text, file_name=__NOT_DEFINED,
               voice=__NOT_DEFINED, language=__NOT_DEFINED, play_after=True):
        if file_name == self.__NOT_DEFINED:
            file_name = f'{text.replace(" ", "_")}.mp3'
        if voice == self.__NOT_DEFINED:
            voice = self.__try_detect_language(language)

        with open(file_name, 'wb') as audio_file:
            audio_file.write(
                self.__text_to_speech.synthesize(
                    text=text,
                    voice=voice,
                    accept='audio/mp3'
                ).get_result().content)

        if play_after:
            playsound(file_name)


if __name__ == '__main__':
    tts = TextToSpeech()
    tts.speech("oi, eu sou isaac")
#    tts.speech("oi, eu sou isaac", language="en")
#   print(tts.list_voices())
