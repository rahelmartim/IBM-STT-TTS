from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from Utils import TRANSLATOR_UTILS as TRANSLATOR


class Translator():
    __authenticator = IAMAuthenticator(TRANSLATOR.API_KEY)
    __language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=__authenticator
    )
    __language_translator.set_service_url(TRANSLATOR.API_URL)
    __SEPARATOR = '-'

    def __validate(self):
        self.__authenticator.validate()

    def list_languages(self):
        self.__validate()
        return self.__language_translator.list_languages().get_result()

    def search_language_code(self, language_name):
        all_languages = self.list_languages()
        for language in all_languages['languages']:
            if language['language_name'].lower() == language_name.lower():
                return language['language']
        return None

    def translate(self, text, source, target):
        self.__validate()
        if not (source+target+text):
            raise ValueError('Expected source and target')
        return self.__language_translator.translate(
                            text=text,
                            model_id=source+self.__SEPARATOR+target
                            ).get_result()['translations'][0]['translation']


if __name__ == '__main__':
    translator = Translator()
#    print(translator.search_language_code('urdu'))
#    print(translator.list_languages())
    print(translator.translate("olá, eu sou isaac", "pt", "en"))
