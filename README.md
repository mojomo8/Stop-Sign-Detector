# Stop-Sign-Detector
This Python project uses OpenCV and iPhone as camera to detect stop signs while driving and provide an audible warning if it detected a stop sign. 

## Setup for Testing
To test the program in real-time, I used the free version of the [iOS EpocCam app](https://apps.apple.com/us/app/epoccam-webcam-for-mac-and-pc/id449133483) (the app is also available on the [Google Play Store](https://play.google.com/store/apps/details?id=com.kinoni.webcam2&hl=en_CA)) on my iPhone to use its camera, and connected it via USB to my laptop running the program. If you decide to use the EpocCam app, you will also need to download drivers on your computer found [here](https://www.kinoni.com/). I placed the phone in the lower right side of the windshield using sticky tack. As a note, the time it took to analyze each frame was between 0.008s and 0.015s, with the average being around 0.011s.
