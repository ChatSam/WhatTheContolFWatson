import pyaudio
import wave
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
import ibmiotf.device
import tkinter as tk


options = {
 "org": "nuqfq3",
 "type": "Austin",
 "id": "austinid",
 "auth-method": "token",
 "auth-token": "wW?XHc1W)26v4Br0U3"
}

client = ibmiotf.device.Client(options)
client.connect()




def myCommandCallback(cmd):
  print("Command received: %s" % cmd.data)
  if cmd.command == "setInterval":
    if 'interval' not in cmd.data:
      print("Error - command is missing required information: 'interval'")
    else:
      interval = cmd.data['interval']
  elif cmd.command == "print":
    if 'message' not in cmd.data:
      print("Error - command is missing required information: 'message'")
    else:
      print(cmd.data['message'])

speech_to_text = SpeechToTextV1(
    username='07907351-58fd-4451-a777-b5251c93a0fd',
    password='hZL4JeOmOpVW'
    )



run=input ("Press Enter to cast a spell")



with open(join(dirname(__file__), 'theaudio.wav'), 'rb') as audio_file:
    client.commandCallback = myCommandCallback
    transcript=json.dumps(speech_to_text.recognize(audio_file, content_type='audio/wav', continuous=True), indent=2)
    client.publishEvent("transcript", "json", {'transcript':transcript})
    jsonData = json.loads(transcript)
    mystring = ''
    for i in jsonData:
        key = jsonData['results'][0]['alternatives'][1]['transcript']
        mystring += key
    print(transcript)
    print(key)

