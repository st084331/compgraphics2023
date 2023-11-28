import os
import shutil
from sklearn.model_selection import train_test_split

# Paths
base_dir = 'lab3/dataset'
classes = ['red_panda', 'not_red_panda']
train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'val')
test_dir = os.path.join(base_dir, 'test')


# Function to split and move files
def split_data(class_name, test_size=0.3, val_size=0.5):
    # Full path to the class directory
    source_dir = os.path.join("lab3", class_name)

    # Listing all files
    all_files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

    # Splitting dataset
    train_files, test_val_files = train_test_split(all_files, test_size=test_size, random_state=42)
    val_files, test_files = train_test_split(test_val_files, test_size=val_size, random_state=42)

    # Function to copy files
    def copy_files(files, dest_dir):
        for f in files:
            shutil.copy(os.path.join(source_dir, f), os.path.join(dest_dir, class_name, f))

    # Copying files to respective directories
    copy_files(train_files, train_dir)
    copy_files(val_files, val_dir)
    copy_files(test_files, test_dir)


# Applying the split function to each class
for cls in classes:
    split_data(cls)

print("Dataset organized into train, validation, and test sets.")
