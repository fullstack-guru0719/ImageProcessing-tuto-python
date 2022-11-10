# import the necessary packages
import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image")
args = vars(ap.parse_args())


# load the image, convert it to grayscale, and display it to our
# screen
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# apply a series of erosions
for i in range(0, 3):
    eroded = cv2.erode(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Eroded {} times".format(i + 1), eroded)
    cv2.waitKey(0)

# close all windows to cleanup the screen
cv2.destroyAllWindows()
cv2.imshow("Original", image)
# apply a series of dilations
for i in range(0, 3):
    dilated = cv2.dilate(gray.copy(), None, iterations=i + 1)
    cv2.imshow("Dilated {} times".format(i + 1), dilated)
    cv2.waitKey(0)


# close all windows to cleanup the screen, then initialize a list of
# of kernels sizes that will be applied to the image
cv2.destroyAllWindows()
cv2.imshow("Original", image)
kernelSizes = [(3, 3), (5, 5), (7, 7)]
# loop over the kernels sizes
for kernelSize in kernelSizes:
    # construct a rectangular kernel from the current size and then
    # apply an "opening" operation
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
    cv2.imshow("Opening: ({}, {})".format(
        kernelSize[0], kernelSize[1]), opening)
    cv2.waitKey(0)
