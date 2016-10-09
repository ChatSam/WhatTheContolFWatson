import numpy as np
import cv2
import json
from os.path import join, dirname
from watson_developer_cloud import AlchemyLanguageV1
from nltk.tokenize import sent_tokenize, word_tokenize
import time
import sys

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

  counter = 1;

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


def seekVideo(searchUnit,searchSpace,filepath):

    #load the file
    cap = cv2.VideoCapture(filepath)

    # gets the no of frames in the video
    nFrames = int(cap.get(7))

    frameUnit = nFrames/searchSpace

    # the frame the video needs to be played at
    seekFrame = frameUnit*searchUnit

    # the frame the video needs to be played at
    cap.set(1, seekFrame)

    # gets the no of frames in the video
    nFrames = int(cap.get(7))

    iterations = nFrames - seekFrame

    for i in range(int(iterations)):
        ret, frame = cap.read()

        cv2.imshow('video', frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            print("breaks!")
            break

    cap.release()
    cv2.destroyAllWindows()

time.sleep(5)
seekVideo(4,10,'testVid.mp4')
sys.exit()
time.sleep(5)
seekVideo(7,10,'testVid.mp4')

#text= processTranscript("sd");
#nume= mapKeyWordToTime(text,"term semantics")

#print(nume)

