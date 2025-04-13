import cv2
import numpy as np
import os

def generate_textures(num_textures, save_path):
    for i in range(num_textures):
        # Example: create a simple striped pattern
        texture = np.zeros((100, 100, 3), dtype=np.uint8)
        for row in range(texture.shape[0]):
            if row % 10 < 5:
                texture[row, :, :] = np.random.randint(0, 255, (3,), dtype=np.uint8)

        # Save the texture
        filename = f'texture_{i}.png'
        cv2.imwrite(os.path.join(save_path, filename), texture)

# Directory where you want to save the textures
save_path = 'Texture_dataset/Striped'
os.makedirs(save_path, exist_ok=True)

# Generate and save textures
generate_textures(100, save_path)
 