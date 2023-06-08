from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import AbsForm
from . import models


# Create your views here.
def ajout(request):
        form = AbsForm()
        return render(request, 'absence/ajout.html', {"form": form})

def traitement(request):
    rform = AbsForm(request.POST)
    if rform.is_valid():
        abs = rform.save()
        abs.save()
        return HttpResponseRedirect("/ecole/allabs")
    else:
        return render(request, 'absence/ajout.html', {"form" : rform})

def all(request):
    liste = list(models.Absence.objects.all())
    return render(request,'absence/all.html', {"liste" : liste})

def affiche(request, id):
    abs = models.Absence.objects.get(pk=id)
    return render(request,"absence/affiche.html", {"abs": abs})

def update(request, id):
    abs = models.Absence.objects.get(pk=id)
    form = AbsForm(abs.dico())
    return render(request, "absence/ajout.html", {"form":form, "id":id})

def updatetraitement(request, id):
    if request.method == "POST":
        rform = AbsForm(request.POST, request.FILES)
        if rform.is_valid():
            abs = rform.save(commit=False)
            abs.idabsence = id
            abs.save()
            return HttpResponseRedirect("/ecole/allabs")
        else:
            return render(request, "absence/update.html", {"form":rform, "id": id})

def delete(request, id):
    abs = models.Absence.objects.get(pk=id)
    abs.delete()
    return HttpResponseRedirect("/ecole/allabs")