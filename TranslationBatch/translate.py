from googletrans import Translator
import xml.etree.ElementTree as ET

# Initialize the translator to use only allowed service urls
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.in',
      'translate.google.com.au'
    ])

contentTree = ET.parse('content.xml')
root = contentTree.getroot()

# for data in root.findall('data'):
#     translatedObj = translator.translate(data.find('value').text,dest='hi',src='en')
#     print(translatedObj.origin, translatedObj.text)

for data in root.findall('data'):
    for value in data.iter('value'):
        translatedObj = translator.translate(value.text,dest='hi',src='en')
        value.text = translatedObj.text
        print(value.text, translatedObj.text)

contentTree.write('output.xml')



# translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='hi', src='en')
# for translation in translations:
#     print(translation.origin, ' -> ', translation.text)