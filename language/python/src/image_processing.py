import cv2 as cv
import imutils

"""
imutils.translate(workspace, 25, -75)
imutils.rotate(bridge, angle=angle, center=(cx, cy))
imutils.resize(workspace, width=width)
imutils.skeletonize(gray, size=(3, 3))
imutils.url_to_image(url)

# automatic canny edge detection(using computed median)
# lower = int(max(0, (1.0 - sigma) * v))
# upper = int(min(255, (1.0 + sigma) * v))
auto = imutils.auto_canny(blurred)
"""