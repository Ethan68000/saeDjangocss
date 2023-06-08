
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import EtudForm
from . import models


# Create your views here.
def ajout(request):
        form = EtudForm()
        return render(request, 'etudiants/ajout.html', {"form": form})

def traitement(request):
    rform = EtudForm(request.POST, request.FILES)
    if rform.is_valid():
        rform = rform.save()
        return HttpResponseRedirect("/ecole/alletud")
    else:
        return render(request, 'etudiants/ajout.html', {"form" : rform})

def all(request):
    liste = list(models.Etudiant.objects.all())
    return render(request,'etudiants/all.html', {"liste" : liste})

def affiche(request, id):
    etud = models.Etudiant.objects.get(pk=id)
    return render(request,"etudiants/affiche.html",{"etud": etud})

def update(request, id):
    etud = models.Etudiant.objects.get(pk=id)
    form = EtudForm(etud.dico())
    return render(request, "etudiants/ajout.html", {"form":form, "id":id})

def updatetraitement(request, id):
    rform = EtudForm(request.POST)
    if rform.is_valid():
        etud = rform.save(commit=True)
        etud.id = id
        etud.save()
        return HttpResponseRedirect("/ecole/alletud")
    else:
        return render(request, "etudiants/update.html", {"form":rform, "id": id})

def delete(request, id):
    etud = models.Etudiant.objects.get(pk=id)
    etud.delete()
    return HttpResponseRedirect("/ecole/alletud")