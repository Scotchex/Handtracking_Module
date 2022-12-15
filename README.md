# Handtracking_Module
This is a hand tracking module, you can call the functions;
findHands() : takes in the video capture i.e. findHands(img)
findPosition(): takes in image, and a second arguement 'draw' if you are using both findHands() & findPosition() make sure to set one of 
them to draw = False otherwise you will end up drawing on the hands twice which might affect performance.
You can use it with pretty much anything you want.
It requires opencv and mediapipe
