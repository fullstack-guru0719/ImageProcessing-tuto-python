# import the necessary packages
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="adrian.png",
                help="path to input image")
args = vars(ap.parse_args())

# load the image, display it to our screen, and initialize a list of
# kernel sizes (so we can evaluate the relationship between kernel
# size and amount of blurring)
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (9, 9), (15, 15)]

# loop over the kernel sizes
for (kX, kY) in kernelSizes:
    # apply an "average" blur to the image using the current kernel
    # size
    blurred = cv2.blur(image, (kX, kY))
    cv2.imshow("Average ({}, {})".format(kX, kY), blurred)
    cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# loop over the kernel sizes again
for (kX, kY) in kernelSizes:
    # apply a "Gaussian" blur to the image
    blurred = cv2.GaussianBlur(image, (kX, kY), 0)
    cv2.imshow("Gaussian ({}, {})".format(kX, kY), blurred)
    cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)

# loop over the kernel sizes a final time
for k in (3, 9, 15):
    # apply a "median" blur to the image
    blurred = cv2.medianBlur(image, k)
    cv2.imshow("Median {}".format(k), blurred)
    cv2.waitKey(0)
