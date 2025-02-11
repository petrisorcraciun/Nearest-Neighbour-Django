from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import settingsForm
import numpy as np
from PIL import Image
from numpy import linalg as linear
from skimage.io import imread
import cv2 as cv2
import os


def index(request):
    listFolder=[i for i in range(1,41)]
    numberImage=[i for i in range(1,11)]

    im = Image.open( 'staticfiles/avatar1.jpg')
    im.save("NN/static/file.jpg", "JPEG")
    im.save("NN/static/gasita.jpg", "JPEG")

    return render(request, 'index.html', 
    {
        'listFolder': listFolder,
        'numberImage':numberImage
    })

def settings(request):
    if request.method == 'POST':
        
        form = settingsForm(request.POST, request.FILES)
        
        if form.is_valid():
            listFolder=[i for i in range(1,41)]
            numberImage=[i for i in range(1,11)]

            database = form['database'].value()
            training = form['training'].value()
            alg = form['alg'].value()
            norm = form['norm'].value()
            folder = form['folder'].value()
            image = form['image'].value()
            
            imageSel = int(image)
            folderSel = int(folder)
            
            #convert image for display in HTML
            im = Image.open( 'staticfiles/s' + folder + '/' + image + '.pgm')
            im.save("NN/static/file.jpg", "JPEG")
            
            inputPhoto =  imread('staticfiles/s' + folder + '/' + image + '.pgm')
            A = np.zeros((10304,320))

            k = 0
            for i in range(1, 41):
                
                for j in range(1, int(training)+1):
                    a = imread('staticfiles/s' + str(i) + '/' + str(j) + '.pgm')
                    A[:,(i-1)*8+(j-1)] = np.reshape(a,10304,1)

            # Algorithm NN: 
            nrPhotos = np.size(A,1)
            distancesVector = np.zeros((1,nrPhotos))  # vector de distante

            cautat = np.zeros((10304,1))
            cautat[:,0] = np.reshape(inputPhoto,10304,1)
            
            for i in range(0, int(nrPhotos)):
                distancesVector[:,i] = linear.norm(cautat[:,0]-A[:,i],1)
         

            positionPhoto = 0
            minDistancesVector = min(distancesVector[0,:])

            for i in range(0, np.size(distancesVector)):
                if distancesVector[0,i] == minDistancesVector:
                    positionPhoto = i+1


            folderPozaGasita = int(positionPhoto/int(training)) + 1
         
            

            PozaGasita = round(positionPhoto%int(training))

            if (PozaGasita) == 1:
                    PozaGasita = 1
      
                 
            im = Image.open( 'staticfiles/s' + str(folderPozaGasita) + '/' + str(PozaGasita) + '.pgm')
            im.save("NN/static/gasita.jpg", "JPEG")

            return render(request, 'index.html', 
                    {
                        'database':database,
                        'training':training,
                        'alg':alg,
                        'norm':norm,
                        'folder':folder,
                        'image':image,
                      
                        'listFolder': listFolder,
                        'numberImage':numberImage,
                        'im':im,
                        'imageSel':imageSel,
                        'folderSel':folderSel,
                        'a':positionPhoto
                       #min(distancesVector[0,:]) - min 
                      
                    })
    else:
        form = settingsForm()

    return render(request, 'index.html', {'form': form})