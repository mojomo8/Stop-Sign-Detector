# Stop-Sign-Detector
This Python project uses OpenCV and iPhone as camera to detect stop signs while driving and provide an audible warning if it detected a stop sign.
<p align="center"> 
<img src="https://github.com/mojomo8/Stop-Sign-Detector/blob/master/DetectedSignPic.png">
</p>
## Description
OpenCV is used with the stopsign_classifier.xml file to detect stop signs in the video feed; the detected stops signs have a box drawn around them, and Tesla's warning sound is played when a stop sign is detected. Also, the time it takes to analyze each frame is printed to the console.

## Setup for Testing
To test the program in real-time, I used the free version of the [iOS EpocCam app](https://apps.apple.com/us/app/epoccam-webcam-for-mac-and-pc/id449133483) (the app is also available on the [Google Play Store](https://play.google.com/store/apps/details?id=com.kinoni.webcam2&hl=en_CA)) on my iPhone to use its camera, and connected it via USB to my laptop running the program on PyCharm. If you decide to use the EpocCam app, you will also need to download drivers on your computer found [here](https://www.kinoni.com/). I placed the phone in the lower right side of the windshield using sticky tack. As a note, the time it took to analyze each frame was between 0.008s and 0.015s, with the average being around 0.011s.

## Results of Testing
The [SuccessTestFootage.mp4](https://github.com/mojomo8/Stop-Sign-Detector/blob/master/SuccessTestFootage.mp4) file shows examples of the program working successfully. Note that in these examples, the vehicle speed is not very fast and there aren't too many distracting objects that the classifier may confuse as a stop sign. As well, I had to brake in advance as the program detected the stop sign quite late. Although a higher resolution video would take longer to analyze, perhaps the program may detect stop signs earlier with a higher resolution video stream as the free EpocCam app limits the resolution to 640x480. The [FailTestFootage.mp4](https://github.com/mojomo8/Stop-Sign-Detector/blob/master/FailTestFootage.mp4) file shows examples where the program failed to recognize a stop sign and misidentified a store sign as a stop sign.

## References 
The stopsign classifier file (stopsign_classifier.xml) I used was from [markgaynor's stopsigns repository](https://github.com/markgaynor/stopsigns). Big thank you to [markgaynor](https://github.com/markgaynor).

