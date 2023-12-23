import cv2
import numpy as np
# from astype import pandas
from PIL import Image
from django.conf import settings
from .forms import ScannerImageForm
from django import forms
import os
import io
import base64

class Helpers:
    @staticmethod
    def resize(image, width=None, height=None, inter=cv2.INTER_AREA):
        dim = None
        (h, w) = image.shape[:2]
        if width is None and height is None:
            return image
        if width is None:
            r = height / float(h)
            dim = (int(w * r), height)
        else:
            r = width / float(w)
            dim = (width, int(h * r))
        resized = cv2.resize(image, dim, interpolation=inter)
        return resized

    @staticmethod
    def grab_contours(cnts):
        if len(cnts) == 2:
            cnts = cnts[0]
        elif len(cnts) == 3:
            cnts = cnts[1]
        else:
            raise Exception('The length of the contour must be 2 or 3.')
        return cnts

    @staticmethod
    def orders(pts):
        rect = np.zeros((4, 2), dtype="float32")
        s = pts.sum(axis=1)
        rect[0] = pts[np.argmin(s)]
        rect[2] = pts[np.argmax(s)]
        diff = np.diff(pts, axis=1)
        rect[1] = pts[np.argmin(diff)]
        rect[3] = pts[np.argmax(diff)]
        return rect

    @staticmethod
    def transform(image, pts):
        rect = Helpers.orders(pts)
        (tl, tr, br, bl) = rect
        widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
        widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
        maxWidth = max(int(widthA), int(widthB))
        heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
        heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
        maxHeight = max(int(heightA), int(heightB))
        dst = np.array([
            [0, 0],
            [maxWidth - 1, 0],
            [maxWidth - 1, maxHeight - 1],
            [0, maxHeight - 1]], dtype="float32")
        M = cv2.getPerspectiveTransform(rect, dst)
        warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))
        return warped

def scan_document(image_path, request):
    image = cv2.imread(image_path)
    ratio = image.shape[0] / 500.0
    orig = image.copy()
    image = Helpers.resize(image, height=500)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 75, 200)

    cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = Helpers.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5]

    screenCnt = None

    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        if len(approx) == 4: #4
            screenCnt = approx
            break

    cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)

    warped = Helpers.transform(orig, screenCnt.reshape(4, 2) * ratio)

    _, buffer = cv2.imencode('.jpg', cv2.cvtColor(warped, cv2.COLOR_BGR2RGB))
    result_base64 = base64.b64encode(buffer).decode('utf-8')

    request.session['scanned_result'] = result_base64
    
    return result_base64

def main(file_path):
    # title_file = form.cleaned_data['title']
    # image_upload = request.FILES['image_upload']
    # file_path = os.path.abspath(os.path.join(settings.BASE_DIR, 'scanner', 'image', 'bahan', f"{title}{os.path.splitext(image_upload.name)[1]}"))
    warped = scan_document(file_path)

    # img = cv2.cvtColor(warped, cv2.COLOR_BGR2RGB)
    # img = Image.fromarray(Helpers.resize(img, width=500))
    return warped

    # Display the image
    # img.show()

if __name__ == "__main__":
    result_base64 = main(file_path)
    main()
