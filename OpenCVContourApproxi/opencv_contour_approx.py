# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="shape.png",
                help="path to input image")
args = vars(ap.parse_args())


# load the image and display it
image = cv2.imread(args["image"])
# cv2.imshow("Image", image)
# convert the image to grayscale and threshold it
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 200, 255,
                       cv2.THRESH_BINARY_INV)[1]
# cv2.imshow("Thresh", thresh)
# cv2.waitKey(0)


# find the largest contour in the threshold image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key=cv2.contourArea)
# draw the shape of the contour on the output image, compute the
# bounding box, and display the number of points in the contour
output = image.copy()
cv2.drawContours(output, [c], -1, (0, 255, 0), 3)
(x, y, w, h) = cv2.boundingRect(c)
text = "original, num_pts={}".format(len(c))
cv2.putText(output, text, (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX,
            0.9, (0, 255, 0), 2)
# show the original contour image
print("[INFO] {}".format(text))
# cv2.imshow("Original Contour", output)
# cv2.waitKey(0)


# to demonstrate the impact of contour approximation, let's loop
# over a number of epsilon sizes
for eps in np.linspace(0.001, 0.05, 10):
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, eps * peri, True)
    # draw the approximated contour on the image
    output = image.copy()
    cv2.drawContours(output, [approx], -1, (0, 255, 0), 3)
    text = "eps={:.4f}, num_pts={}".format(eps, len(approx))
    cv2.putText(output, text, (x, y - 15), cv2.FONT_HERSHEY_SIMPLEX,
                0.9, (0, 255, 0), 2)
    # show the approximated contour image
    print("[INFO] {}".format(text))
    cv2.imshow("Approximated Contour", output)
    cv2.waitKey(0)
