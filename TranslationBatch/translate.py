from googletrans import Translator
translator = Translator()
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.in',
    ])
#translatedObj = translator.translate("Hello World !!!", 'hi','en')

translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='hi')
for translation in translations:
    print(translation.origin, ' -> ', translation.text)