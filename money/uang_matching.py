import cv2 
import numpy as np
import os

def translate(image, x, y):
	# Define the translation matrix and perform the translation
	M = np.float32([[1, 0, x], [0, 1, y]])
	shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

	# Return the translated image
	return shifted

def rotate_bound(image, angle):
    # grab the dimensions of the image and then determine the
    # center
    (h, w) = image.shape[:2]
    (cX, cY) = (w // 2, h // 2)
    # grab the rotation matrix (applying the negative of the
    # angle to rotate clockwise), then grab the sine and cosine
    # (i.e., the rotation components of the matrix)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    # compute the new bounding dimensions of the image
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    # adjust the rotation matrix to take into account translation
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    # perform the actual rotation and return the image
    return cv2.warpAffine(image, M, (nW, nH))

def rotate(image, angle, center = None, scale = 1.0):
	# Grab the dimensions of the image
	(h, w) = image.shape[:2]

	# If the center is None, initialize it as the center of
	# the image
	if center is None:
		center = (w / 2, h / 2)

	# Perform the rotation
	M = cv2.getRotationMatrix2D(center, angle, scale)
	rotated = cv2.warpAffine(image, M, (w, h))

	# Return the rotated image
	return rotated

def resize(image, width = None, height = None, inter = cv2.INTER_AREA):
	# initialize the dimensions of the image to be resized and
	# grab the image size
	dim = None
	(h, w) = image.shape[:2]

	# if both the width and height are None, then return the
	# original image
	if width is None and height is None:
		return image

	# check to see if the width is None
	if width is None:
		# calculate the ratio of the height and construct the
		# dimensions
		r = height / float(h)
		dim = (int(w * r), height)

	# otherwise, the height is None
	else:
		# calculate the ratio of the width and construct the
		# dimensions
		r = width / float(w)
		dim = (width, int(h * r))

	# resize the image
	resized = cv2.resize(image, dim, interpolation = inter)

	# return the resized image
	return resized

def uang_matching(image_path):
    # Load template
    template_data = []
    
    template_dir = 'money/image/dataset'
    template_files = [file for file in os.listdir(template_dir) if file.endswith(('.jpg', '.jpeg'))]
    
    print("Template loaded:", template_files)
    
    # Prepare template
    for template_file in template_files:
        template_path = os.path.join(template_dir, template_file)
        tmp = cv2.imread(template_path)

        nominal = template_file.replace('.jpg', '').replace('.jpeg', '')
        template_data.append({"glob": tmp, "nominal": nominal})
    
    # Template matching
    image_test = cv2.imread(image_path)
    image_test_p = cv2.cvtColor(image_test, cv2.COLOR_BGR2GRAY) 

    found = None
    threshold = 0.4
    
    for template in template_data:
        for scale in np.linspace(0.2, 1.0, 20)[::-1]: 
            # scaling uang
            resized = resize(
                image_test_p, width=int(image_test_p.shape[1] * scale))
            r = image_test_p.shape[1] / float(resized.shape[1]) 
            resized = cv2.convertScaleAbs(resized)
            
            # Check if dimensions are valid
            if resized.shape[0] >= template['glob'].shape[0] and \
                    resized.shape[1] >= template['glob'].shape[1]:
                
                # Convert to grayscale
                template_gray = cv2.cvtColor(template['glob'], cv2.COLOR_BGR2GRAY)
                
                # Ensure both images have the correct number of channels
                if len(resized.shape) == 2:
                    resized = cv2.cvtColor(resized, cv2.COLOR_GRAY2BGR)
                
                if len(template_gray.shape) == 2:
                    template_gray = cv2.cvtColor(template_gray, cv2.COLOR_GRAY2BGR)
                
                # Convert to unsigned 8-bit integer
                resized = resized.astype(np.uint8)
                template_gray = template_gray.astype(np.uint8)
                
                # template matching
                result = cv2.matchTemplate(resized, template_gray, cv2.TM_CCOEFF_NORMED)
                (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
                
                if found is None or maxVal > found[0]:
                    found = (maxVal, maxLoc, r, template)

    if found is not None: 
        (maxVal, maxLoc, r, template) = found
        (startX, startY) = (int(maxLoc[0]*r), int(maxLoc[1] * r))
        (endX, endY) = (
            int((maxLoc[0] + template['glob'].shape[1]) * r), int((maxLoc[1] + template['glob'].shape[0]) * r))
        
        if maxVal >= threshold:
            # print("Money:", template['nominal'], "detected")
            cv2.rectangle(image_test, (startX, startY), (endX, endY), (0, 0, 255), 2)
            # cv2.imshow("Result", image_test)

            return template['nominal']
    return None

def main (image_path):
    image = uang_matching(image_path)
    return image

