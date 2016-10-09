import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1
from nltk.tokenize import sent_tokenize, word_tokenize

#demo one
#alchemy_language = AlchemyLanguageV1(api_key='997e434e4c331defcf021d503ead65bd15c3e944');
alchemy_language = AlchemyLanguageV1(api_key='bd86c39918b7ddd88da6e9dfdc2d23133650e398');


def processTranscript(filename):
  #todo: take in the filename as an input
  filename = "F:\\Hack\\transcript.txt"

  file = open(filename)

  data = file.read()

  #break the transcript file into sentences
  sentenceList = sent_tokenize(data)

  #searchable dictionary
  searchableText = dict();

  counter = 0;

  for sentence in sentenceList:

    jsonObj = json.dumps(alchemy_language.keywords(text=sentence,max_items=1))

    jsonData = json.loads(jsonObj)

    key = jsonData['keywords'][0]['text']
    searchableText[key] = counter;

    counter += 1
    print(searchableText)
    break;

  return searchableText

def mapKeyWordToTime(searchableText,searchQuery):

  for key in searchableText.keys():
    if (key == searchQuery):
      print ("detection!")

      return searchableText[key]


text= processTranscript("sd");
nume= mapKeyWordToTime(text,"term semantics")

print(nume)