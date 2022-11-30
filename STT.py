from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from Utils import STT_UTILS as STT


class SpeechToText():
    __authenticator = IAMAuthenticator(STT.API_KEY)
    __stt = SpeechToTextV1(authenticator=__authenticator)
    __stt.set_service_url(STT.API_URL)  
    __NOT_DEFINED = 99
    __DEFAULT_LANGUAGE = 'pt-BR_BroadbandModel'

    def __validate(self):
        self.__authenticator.validate()

    def read(self, file_name, language=__NOT_DEFINED):
        self.__validate()

        if not file_name:
            raise ValueError('Expected file name')
        if ".flac" not in file_name:
            raise ValueError('Expected .flac file')

        if language == self.__NOT_DEFINED:
            language = self.__DEFAULT_LANGUAGE

        with open(join(dirname('__file__'), file_name), 'rb') as audio_file:
            return self.__stt.recognize(
                audio=audio_file,
                content_type='audio/flac',
                model=language
                ).get_result()['results'][0]['alternatives'][0]['transcript']


if __name__ == '__main__':
    stt = SpeechToText()
    print(stt.read("audio.flac"))
