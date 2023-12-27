import cv2
import base64

def cartoonize(image):
    img = cv2.imread(image)
    smooth = cv2.bilateralFilter(img, 9, 75, 75)
    gray = cv2.cvtColor(smooth, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 9, 9)
    cartoon = cv2.bitwise_and(smooth, smooth, mask=edges)
    return cartoon

def read_image(image, request):
    cartoon_image = cartoonize(image)
    
    # Handle the case where encoding fails
    try:
        _, buffer = cv2.imencode('.jpg', cv2.cvtColor(cartoon_image, cv2.COLOR_BGR2RGB))
        cartoon_base64 = base64.b64encode(buffer).decode('utf-8')
    except Exception as e:
        # Handle the exception (e.g., print the error, log it, or return a default value)
        print(f"Error encoding image: {e}")
        cartoon_base64 = None
    
    request.session['cartoon_result'] = cartoon_base64
    return cartoon_base64
