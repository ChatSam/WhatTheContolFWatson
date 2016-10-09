import pyaudio
import wave
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
import ibmiotf.device
import tkinter as tk


options = {
 "org": "88hc9i",
 "type": "Laptop1",
 "id": "Laptop1",
 "auth-method": "token",
 "auth-token": "Ni)F&1z7UItwQLX@)&"
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

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "speech.wav"


while True:
	run=input ("Press Enter to cast a spell")
	p = pyaudio.PyAudio()
	stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)

	print("* recording")

	frames = []

	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	wf.setnchannels(CHANNELS)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(RATE)
	wf.writeframes(b''.join(frames))
	wf.close()


	with open(join(dirname(__file__), 'speech.wav'), 'rb') as audio_file:
		client.commandCallback = myCommandCallback
		transcript=json.dumps(speech_to_text.recognize(audio_file, content_type='audio/wav', continuous=True), indent=2)
		client.publishEvent("transcript", "json", {'transcript':transcript})
		print(transcript)

