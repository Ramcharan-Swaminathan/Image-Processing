import cv2

def convert_to_grayscale(img_path, output_path):
    """
    This will convert color image to grayscale, so it wil be ezy to process :)
    """
    img = cv2.imread(img_path)
    if img is None:
        print(f"Error: Could not load image {img_path}")
        return False
    
    # this pic ain't got no color fr
    if len(img.shape) == 2:
        print(f"Image {img_path} is already grayscale")

        cv2.imwrite(output_path, img)
    else:
        # ok converting now
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(output_path, gray)
    
    print(f"Grayscale image saved: {output_path}")
    return True

# please test me
if __name__ == "__main__":
    # (-_ゝ-)
    convert_to_grayscale('inp/saravana.jpg', 'out/saravana_grayscale.jpg')
