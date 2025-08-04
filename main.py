import cv2
import os
from negative import create_negative_image
from HistEqualization import histogram_equalization
from grayscale_converter import convert_to_grayscale

def main():
    """
    Main function to process all images in inp folder
    """
    inp_folder = "inp"
    output_folder = "out"
    grey_folder = "grey"
    
    # handling if folders not there
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"Created output folder: {output_folder}")
    
    if not os.path.exists(grey_folder):
        os.makedirs(grey_folder)
        print(f"Created grey folder: {grey_folder}")
    
    # Get all image files from inp folder
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    image_files = []
    
    if os.path.exists(inp_folder):
        for file in os.listdir(inp_folder):
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_files.append(file)
    else:
        print(f"Error: {inp_folder} folder not found!")
        return
    
    if not image_files:
        print(f"No image files found in {inp_folder} folder!")
        return
    
    print(f"Found {len(image_files)} image(s) to process:")
    for img_file in image_files:
        print(f"  - {img_file}")
    
    for img_file in image_files:
        input_path = os.path.join(inp_folder, img_file)
        base_name = os.path.splitext(img_file)[0]
        
        # normal -> grayscale 
        grayscale_output = os.path.join(grey_folder, f"{base_name}_grayscale.jpg")
        convert_to_grayscale(input_path, grayscale_output)
        
        # grayscale -> negative
        negative_output = os.path.join(output_folder, f"{base_name}_negative.jpg")
        create_negative_image(grayscale_output, negative_output)
        
        # grayscale -> histogram equalization
        hist_eq_output = os.path.join(output_folder, f"{base_name}_hist_eq.jpg")
        histogram_equalization(grayscale_output, hist_eq_output)
        

    print("\ndone cooking the pixels 🍳🖼️")

if __name__ == "__main__":
    main()
