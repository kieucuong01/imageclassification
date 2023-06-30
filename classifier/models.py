import cv2
import ssl
import numpy as np
from django.db import models
from PIL import Image

# from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from pathlib import Path

curr_path = str(Path(__file__).resolve().parent)

class Classifier(models.Model):
  image = models.ImageField(upload_to='images')
  result = models.CharField(max_length=250, blank=True)
  date_uploaded = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return 'Image classfied at {}'.format(self.date_uploaded.strftime('%Y-%m-%d %H:%M'))

  
  def save(self, *args, **kwargs):
    try:
      # SSL certificate necessary so we can download weights of the InceptionResNetV2 model
      ssl._create_default_https_context = ssl._create_unverified_context

      test_image = Image.open(self.image)

      model = load_model(curr_path+"/CNN_best_model.h5", compile=False)

      test_image = image.img_to_array(test_image)
      test_image = cv2.resize(test_image, (128, 128))

      test_image = test_image/255
      test_image = np.expand_dims(test_image, axis = 0) 

      result = model.predict(test_image)
      print(result)

      max_prob = max(result[0])

      if max_prob == result[0][0]:
          prediction = 'glass'
      elif max_prob == result[0][1]:
          prediction = 'metal'
      elif max_prob == result[0][2]:
          prediction = 'paper'
      else:
          prediction = 'plastic'


      self.result = prediction

      print('Success')
    except Exception as e:
      print('Classification failed:', e)

    return super().save(*args, **kwargs)



