import os
import hashlib
from PIL import Image

def calculate_hash(image_path):
    with open(image_path, 'rb') as f:
        image_data = f.read()
        return hashlib.md5(image_data).hexdigest()

image_directory = 'images'
image_hashes = {}

for filename in os.listdir(image_directory):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        image_path = os.path.join(image_directory, filename)
        image_hash = calculate_hash(image_path)
        
        if image_hash in image_hashes:
            os.remove(image_path)
        else:
            image_hashes[image_hash] = filename