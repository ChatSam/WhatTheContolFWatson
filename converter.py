import moviepy.editor as mp

clip = mp.VideoFileClip("video.mp4")
clip.audio.write_audiofile("theaudio.wav")