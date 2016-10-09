import numpy as np
import cv2

#load the file
cap = cv2.VideoCapture('sample.avi')

# the frame the video needs to be played at
seekFrame = int(input("Enter: "))
cap.set(1, seekFrame)

#gets the no of frames in the video
nFrames = int(cap.get(7))

iterations = nFrames - seekFrame

for i in range(iterations):

    ret, frame = cap.read()

    cv2.imshow('video',frame)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        print ("breaks!")
        break

cap.release()
cv2.destroyAllWindows()


#video = cv2.VideoCapture('sample.avi')
# A loop to play the video file. This can also be a while loop until a key
# is pressed. etc.
