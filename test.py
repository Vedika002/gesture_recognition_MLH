
# coding: utf-8

# In[11]:


import numpy as np
from keras.models import model_from_json
import operator
import cv2
import sys, os

# Loading the model
json_file = open("model-bw.json", "r")
model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(model_json)
# load weights into new model
loaded_model.load_weights("model-bw.h5")
print("Loaded model from disk")


# In[85]:


import os
import random

dir = 'test/'
filename = random.choice(os.listdir(dir))
path = os.path.join(dir,filename)
print(filename)


# In[86]:



# In[87]:


x=[]
img1 = cv2.imread(path)
img1 = img1.reshape((50,50,3))
img1 = img1/255.0
x.append(img1)


# In[88]:


X = np.array(x)
import matplotlib.pyplot as plt

cv2.imshow( '',img1)
cv2.waitKey()


# In[89]:


y1=loaded_model.predict(X)


# In[90]:


y1.round()


# In[91]:


flag=0
for i in range(1):

    import cv2

    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    while True:
        try:
            check, frame = webcam.read()
            #print(check) #prints true as long as the webcam is running
            #print(frame) #prints matrix values of each framecd
            cv2.imshow("Capturing", frame)
            key = cv2.waitKey(1)
            if key == ord('s'):
                cv2.imwrite(filename='saved_img.jpg', img=frame)
                webcam.release()
                img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
                img_new = cv2.imshow("Captured Image", img_new)
                cv2.waitKey(1650)
                cv2.destroyAllWindows()
                print("Processing image...")
                img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
                print("Converting RGB image to grayscale...")
                gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
                print("Converted RGB image to grayscale...")
                print("Resizing image to 28x28 scale...")
                img_ = cv2.resize(gray,(28,28))
                print("Resized...")
                img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
                print("Image saved!")

                break
            elif key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break

        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

    x2=[]
    img2 = cv2.imread("saved_img.jpg")
    img2 = cv2.flip(img2,1)
    img2 = cv2.resize(img2,(50,50))
    img2 = img2.reshape((50,50,3))
    img2 = img2/255.0
    x2.append(img2)
    X2 = np.array(x2)
    # data prepsocessing using same method used for training
    y=loaded_model.predict(X2)

    #comparison=
    y1=y1.round()
    y=y.round()
    print(y)
    print(y1)
    comparison=y==y1
    equal_arrays = comparison.all()
    if equal_arrays:
        flag=1
        break


# In[92]:


if flag==1:
    print("Login Sucessfull")
else:
    print("Try Again!")


# In[ ]:
