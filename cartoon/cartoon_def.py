import cv2


def cartoonize (image):
  img = image
  smooth = cv2.bilateralFilter(img, 9, 75, 75)
  gray = cv2.cvtColor(smooth, cv2.COLOR_BGR2GRAY)
  edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN, cv2.THRESH_BINARY, 9, 9) # Option gaussian or mean
  cartoon = cv2.bitwise_and(smooth, smooth, mask=edges)
  return cartoon

