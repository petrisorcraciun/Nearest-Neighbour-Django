from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import settingsForm
import numpy as np


def index(request):
    listFolder=[i for i in range(1,41)]
    numberImage=[i for i in range(1,11)]
    return render(request, 'index.html', 
    {
        'listFolder': listFolder,
        'numberImage':numberImage
    })

def settings(request):
    if request.method == 'POST':
        
        form = settingsForm(request.POST, request.FILES)
        
        if form.is_valid():

            A = (10304,320)
            a = np.zeros(A)

            folders = []

            listFolder=[i for i in range(1,41)]

            database = form['database'].value()
            training = form['training'].value()
            alg = form['alg'].value()
            norm = form['norm'].value()

            return render(request, 'index.html', 
                    {
                        'database':database,
                        'training':training,
                        'alg':alg,
                        'norm':norm,
                      
                        'listFolder': listFolder
                    })
    else:
        form = settingsForm()

    return render(request, 'index.html', {'form': form})