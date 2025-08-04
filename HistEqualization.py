import cv2

def histogram_equalization(img_path, output_path):
    """
    Applying histogram equalization to input image
    please use only grayscale images for this 
    """
    img = cv2.imread(img_path)
    if img is None:
        print(f"Error: Could not load image {img_path}")
        return False
    
    # Check if image is already grayscale or convert to grayscale
    if len(img.shape) == 2:
        # Already grayscale
        gray = img
    else:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    height, width = gray.shape
    
    # creating the  histogram
    hist = {}
    for y in range(height):
        for x in range(width):
            pixel_value = int(gray[y, x])
            hist[pixel_value] = hist.get(pixel_value, 0) + 1
    
    total_pixels = height * width

    # Normalizing the histogram
    n_hist = {k: v / total_pixels for k, v in hist.items()}
    
    # Calculatethat  CDF
    cdf = {}
    cumulative = 0.0
    for i in range(256):
        prob = n_hist.get(i, 0)
        cumulative += prob
        cdf[i] = cumulative
    
    cdf_min = min([v for v in cdf.values() if v > 0])
    #applying the s formula
    new_dic = {}
    for key in range(256):
        new_dic[key] = int(((cdf[key] - cdf_min) / (1 - cdf_min)) * 255 + 0.5) #anyway cdf_max is always 1 so we dont need to calculate it ig

    # Applying histogram equalization
    for y in range(height):
        for x in range(width):
            gray[y, x] = new_dic[int(gray[y, x])]
    
    # Saving the equalized image
    cv2.imwrite(output_path, gray)
    print(f"Histogram equalized image saved: {output_path}")
    return True

# Original code for testing
if __name__ == "__main__":
    img = cv2.imread('grey/negative_gray.jpg')
    #780×1,040 = 8,11,200  pixels

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    height, width = gray.shape

    hist = {}

    for y in range(height):
        for x in range(width):
            pixel_value = int(gray[y, x])
            hist[pixel_value] = hist.get(pixel_value, 0) + 1

    total_pixels = height * width

    n_hist = {k: v / total_pixels for k, v in hist.items()}

    print(n_hist)

    cdf = {}
    cumulative = 0.0

    for i in range(256):
        prob = n_hist.get(i, 0)
        cumulative += prob
        cdf[i] = cumulative

    cdf_min = min([v for v in cdf.values() if v > 0])

    new_dic = {}
    for key in range(256):
        new_dic[key] = int(((cdf[key] - cdf_min) / (1 - cdf_min)) * 255 + 0.5)

    for y in range (height):
        for x in range(width):
            gray[y,x] = new_dic[int(gray[y,x])]

    cv2.imwrite('out/neg_equal_output.jpg', gray)

