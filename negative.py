import cv2

def create_negative_image(img_path, output_path):
    """
    Creating negative image from input image 
    """
    img = cv2.imread(img_path)
    if img is None:
        print(f"Error: Could not load image {img_path}")
        return False
    
    if len(img.shape) == 2:
        gray = img
    else:
        # we dont have to work with three R G B
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    

    negative_gray = 255 - gray
    
    
    cv2.imwrite(output_path, negative_gray)
    print(f"Negative image saved: {output_path}")
    return True

# Please test me
if __name__ == "__main__":
    img = cv2.imread('inp/saravana_grey.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    negative_gray = 255 - gray
    cv2.imwrite('out/negative_gray.jpg', negative_gray)
