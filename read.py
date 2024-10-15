#import cv2 as cv
#img=cv.imread('images/cat.jpg')
#cv.imshow('cat',img)
#cv.waitKey(0)

#Reading the image:
"""1.cv.imread('path_to_image.jpg'): This function reads the image from the specified file path ('path_to_image.jpg'). 
The image is loaded as a NumPy array in BGR format.
Displaying the image:
2.cv.imshow('Image Window', img): Opens a window named 'Image Window' and displays the image inside it.
Waiting for a key press:
3.cv.waitKey(0): The program waits indefinitely until any key is pressed. After the key press, the program continues.
Closing the window:
4.cv.destroyAllWindows(): Closes all the windows opened by OpenCV.
"""

import cv2 as cv
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()


"""Reading the video:

1.cv.VideoCapture('path_to_video.mp4'): This function captures the video from the specified file ('path_to_video.mp4'), which you should replace with your actual video file path.
Looping through video frames:

2.capture.read(): Reads each frame of the video. It returns two values:
isTrue: A boolean value indicating if the frame was read successfully (True if there are more frames, False if the video has ended).
frame: The current frame of the video.
Displaying the video:

3.cv.imshow('Video', frame): Displays each frame in a window called 'Video'.
Exit the loop:

4.cv.waitKey(20): Pauses for 20 milliseconds between frames. The function waits for a key press and returns the pressed key's ASCII value.
if cv.waitKey(20) & 0xFF == ord('d'): The video will stop playing when the 'd' key is pressed.
Releasing resources:

5.capture.release(): Releases the video capture object when the video is finished or the user exits the loop.
cv.destroyAllWindows(): Closes all OpenCV windows."""
