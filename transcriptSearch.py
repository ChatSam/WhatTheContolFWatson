import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1
from nltk.tokenize import sent_tokenize, word_tokenize

alchemy_language = AlchemyLanguageV1(api_key='997e434e4c331defcf021d503ead65bd15c3e944');


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

    searchableText[counter] = jsonData['keywords'][0]['text']

    print(jsonData)

    break;


