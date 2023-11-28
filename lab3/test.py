import os

import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix

test_datagen = ImageDataGenerator(rescale=1. / 255)

test_generator = test_datagen.flow_from_directory(
    os.path.join('lab3', 'dataset', 'test'),
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical',
    shuffle=False)  # Shuffle should be False for evaluation

model = tf.keras.models.load_model(os.path.join('lab3', 'red_panda_classifier.h5'))

steps = np.ceil(test_generator.samples / test_generator.batch_size)
loss, accuracy = model.evaluate(test_generator, steps=steps)
print(f"Test Loss: {loss}")
print(f"Test Accuracy: {accuracy}")

# Get predictions
predictions = model.predict(test_generator, steps=steps)
predicted_classes = np.argmax(predictions, axis=1)

# Get actual labels
actual_classes = test_generator.classes

# Classification report
print(classification_report(actual_classes, predicted_classes, target_names=test_generator.class_indices.keys()))

# Confusion Matrix
print(confusion_matrix(actual_classes, predicted_classes))
