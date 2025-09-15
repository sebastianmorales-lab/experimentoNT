from PIL import Image
import os

# Define size and paths
target_size = (512, 512)
input_folder = "sinfondo"
output_folder = "images"

# Create output directory if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Process each image
for filename in os.listdir(input_folder):
    if filename.endswith(".png"):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        try:
            # Open and process image
            with Image.open(input_path) as img:
                # Convert to RGBA
                img = img.convert("RGBA")
                # Resize image
                img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
                # Save resized image
                img_resized.save(output_path)
                print(f"Processed: {filename}")
        except Exception as e:
            print(f"Error processing {filename}: {str(e)}")