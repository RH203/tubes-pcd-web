import cv2
import base64

def cartoonize(image):
    img = cv2.imread(image)
    smooth = cv2.bilateralFilter(img, 9, 75, 75)
    lab = cv2.cvtColor(smooth, cv2.COLOR_BGR2LAB)
    l_channel, _, _ = cv2.split(lab)
    edges = cv2.adaptiveThreshold(l_channel, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    
    cartoon = cv2.bitwise_and(smooth, edges)
    
    return cartoon

def read_image(image, request):
    cartoon_image = cartoonize(image)
    
    # Handle the case where encoding fails
    try:
        _, buffer = cv2.imencode('.jpg', cv2.cvtColor(cartoon_image, cv2.COLOR_BGR2RGB))
        cartoon_base64 = base64.b64encode(buffer).decode('utf-8')
    
        request.session['cartoon_result'] = cartoon_base64
        
    except Exception as e:
        
        # Handle the exception (e.g., print the error, log it, or return a default value)
        print(f"Error encoding image: {e}")
        cartoon_base64 = None
    
    return cartoon_base64
