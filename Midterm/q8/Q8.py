from keras.models import load_model
from keras_preprocessing.image import load_img
from keras_preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
import numpy as np

from keras.models import load_model

model = load_model('model_saved.h5')


for file in 'test':
    image = load_img(file, target_size=(512, 512))
    img = np.array(image)
    img = img / 512.0
    img = img.reshape(1, 511, 511, 3)
    label = model.predict(img)
    print("Predicted Class (0 - Crops , 1- Weeds): ", label[0][0])