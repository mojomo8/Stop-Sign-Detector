import cv2
from datetime import datetime
from playsound import playsound


StopSignClassifier = cv2.CascadeClassifier('stopsign_classifier.xml')
video = cv2.VideoCapture(0) #NOTE: using the Epoccam app on iPhone to use iPhone as camera


def analyze_video(): #this function takes a frame from the camera, crops it, turns it to grayscale, searches for stop signs, draws a box around found stop signs, and displays time it took to do all this in the console
    start_time = datetime.now()
    ret, image = video.read()
    cropped_image = image[0:250,200:640] #[height,width];640x480 is original capture size (widthxheight) if using the free Epoccam app on iPhone; **if you do not want to crop, you change this line to cropped_image=image but you must also remove the '+200' in line 20
    gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    stop_sign_coordinates = StopSignClassifier.detectMultiScale(gray_image, 1.2, 5, maxSize=(70,70)) #1.2 is scaleFactor; the greater this number, the faster but likely less accurate
                                                                                                     #5 is minNeighbours; the greater this number, the more sure the program has to be that it indeed found a stop sign, so less likelyhood of false positives, but can miss signs if number is too high
    stop_sign_count=0                                                                                #the reason we have a maxSize limit is because sometimes the program misidentifies large objects, such as pointy edges of homes or signage of stores, as stop signs
    for x,y,w,h in stop_sign_coordinates:
        stop_sign_count+=1
        cv2.rectangle(image, (x+200,y), (x+w+200,y+h), (0,255,255), 2) #(0,255,255) is color of box in BGR
    cv2.imshow('video', image)

    print("Detection took: {}s and {} stop signs(s) detected".format((datetime.now() - start_time).total_seconds(), str(stop_sign_count)))
    return stop_sign_count


def quit(): # press the key 'q' to quit and end the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return True
    return False


while True:
    found_stop_sign=analyze_video()
    if found_stop_sign:
        playsound('Tesla Warning.mp3', False)

    while found_stop_sign: #this loop is to try to prevent the warning from playing more than once per stop sign
       found_stop_sign=analyze_video()
       if quit():
           break

    if quit():
        break


video.release()
cv2.destroyAllWindows()
