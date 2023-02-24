from django.shortcuts import render
from . import predictions
import os
import cv2
#import PIL
import numpy as np
import tensorflow as tf
from django.conf import settings
from django.template.response import TemplateResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage


class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name
    


"""
1. The scan function is the main function which is called when the user submits the form.
2. The image is read and passed to the model.
3. The model returns the prediction.
4. The prediction is then passed to the template as a context variable.
5. The template then displays the result. """

def scan(request):
    message = ""
    prediction = ""
    fss = CustomFileSystemStorage()
    try:
        image = request.FILES["image"]
        print("Name", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" + image.name
        # image details
        image_url = fss.url(_image)
        # Read the image
        imag=cv2.imread(path)
        imag1 = cv2.resize(imag,(300,300))
        X = np.array((imag1[np.newaxis])/255)

        # load model
        model = tf.keras.models.load_model(os.getcwd() + './dumbs/densenet_bestqwk.h5')
        score_predict=((model.predict(X).ravel()*model.predict(X[:, ::-1, :, :]).ravel()*model.predict(X[:, ::-1, ::-1, :]).ravel()*model.predict(X[:, :, ::-1, :]).ravel())**0.25).tolist()
        label_predict = np.argmax(score_predict)

        # ----------------
        # LABELS
        # 0 - No diabetic retinopathy
        # 1 - Mild
        # 2 - Moderate
        # 3 - Severe
        # 4 - Proliferative diabetic retinopathy
        # ----------------

        
        prediction = label_predict
        print("improtant::  "+str(label_predict))
        if (prediction == 0):
            prediction = "You don't have diabetic retinopathy"
            message = "We’re very happy for you"
        elif (prediction == 1):
            prediction = "Mild"
            message = "we're sorry for you"
        elif (prediction == 2):
             prediction = "Your diabetic retinopathy is Moderate"
             message = "we're sorry for you"
        elif (prediction == 3):
             prediction = "Your diabetic retinopathy is Severe"
             message = "we're sorry for you"
        elif (prediction == 4):
             prediction = "Your diabetic retinopathy is Proliferative"
             message = "we're sorry for you"
        else:
             prediction = "Unknown"
        
         
        
        return TemplateResponse(
            request,
            "scan-result.html",
            {
                "message": message,
                "image": image,
                "image_url": image_url,
                "prediction": prediction,
            },
        )
    except MultiValueDictKeyError:

        return TemplateResponse(
            request,
            "scan.html",
            {"message": "No Image Selected"},
        )


def home(request):
    return render(request,'index.html')
    

    """ This code does the following:
1. Takes the input from the form
2. Passes the input to the model
3. Renders the result and a message """

def result(request):
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        cho0 = int(request.POST['cho0'])
        cho = int(request.POST['cho'])
        cho1 = int(request.POST['cho1'])
        cho2 = int(request.POST['cho2'])
        cho3 = int(request.POST['cho3'])
        cho4 = int(request.POST['cho4'])
        cho5 = int(request.POST['cho5'])
        cho6 = int(request.POST['cho6'])
        cho7 = int(request.POST['cho7'])
        cho8 = int(request.POST['cho8'])
        cho9 = int(request.POST['cho9'])
        cho11 = int(request.POST['cho11'])
        cho12 = int(request.POST['cho12'])
        cho13 = int(request.POST['cho13'])
        cho14 = int(request.POST['cho14'])
    else:
        return render(request, 'early-result.html', {'result':'Something went wrong'})
    
    #result = predictions.getPredictions(int(request.GET['quantity']),int(request.GET['cho0']),int(request.GET['cho']),int(request.GET['cho1']),int(request.GET['cho2']),int(request.GET['cho3']),int(request.GET['cho4']),int(request.GET['cho5']),int(request.GET['cho6']),int(request.GET['cho7']),int(request.GET['cho8']),int(request.GET['cho9']),int(request.GET['cho11']),int(request.GET['cho12']),int(request.GET['cho13']),int(request.GET['cho14']))
    result = predictions.getPredictions(quantity,cho,cho0,cho1,cho2,cho3,cho4,cho5,cho6,cho7,cho8,cho9,cho11,cho12,cho13,cho14)
    if (result == "You don't have diabetes"):
        message = "we're happy to inform you that "
    else:
        message = "we're sad to inform you that"
    
    print(quantity,cho,cho0,cho1,cho2,cho3,cho4,cho5,cho6,cho7,cho8,cho9,cho11,cho12,cho13,cho14)
    print("result:::::",result)
    return render(request, 'early-result.html', {'result':result,'message':message})