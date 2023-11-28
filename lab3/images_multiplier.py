import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from tensorflow.keras.utils import save_img

# Directory where your original images are stored
original_images_dir = 'lab3/images'

# Directory to save augmented images
augmented_images_dir = 'lab3/augmented_images'
os.makedirs(augmented_images_dir, exist_ok=True)

# Data Augmentation configuration
datagen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Function to augment images
def augment_image(file_name, save_dir, num_augmented_images=5):
    img_path = os.path.join(original_images_dir, file_name)
    img = load_img(img_path)
    img_array = img_to_array(img)
    img_array = img_array.reshape((1,) + img_array.shape)

    i = 0
    for batch in datagen.flow(img_array, batch_size=1, save_to_dir=save_dir, save_prefix='aug', save_format='jpeg'):
        i += 1
        if i >= num_augmented_images:
            break

# Augment each image in the original directory
for file_name in os.listdir(original_images_dir):
    if file_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        augment_image(file_name, augmented_images_dir)

print("Data augmentation completed.")
