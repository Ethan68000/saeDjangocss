from django.urls import path
from . import absenceviews, coursviews, enseignantviews, groupeviews, etudiantviews

urlpatterns = [
    path('ajoutens/<int:id>/', enseignantviews.ajout),
    path('traitementens/<int:id>/', enseignantviews.traitement),
    path('allens/', enseignantviews.all),
    path("afficheens/<int:id>/", enseignantviews.affiche),
    path("updateens/<int:id>/", enseignantviews.update),
    path("updatetraitementens/<int:id>/", enseignantviews.updatetraitement),
    path("deleteens/<int:id>", enseignantviews.delete),

    path('ajoutabs/<int:id>/', absenceviews.ajout),
    path('traitementabs/<int:id>/', absenceviews.traitement),
    path('allabs/', absenceviews.all),
    path("afficheabs/<int:id>/", absenceviews.affiche),
    path("updateabs/<int:id>/", absenceviews.update),
    path("updatetraitementabs/<int:id>/", absenceviews.updatetraitement),
    path("deleteabs/<int:id>", absenceviews.delete),

    path('ajoutcours/<int:id>/', coursviews.ajout),
    path('traitementcours/<int:id>/', coursviews.traitement),
    path('allcours/', coursviews.all),
    path("affichecours/<int:id>/", coursviews.affiche),
    path("updatecours/<int:id>/", coursviews.update),
    path("updatetraitementcours/<int:id>/", coursviews.updatetraitement),
    path("deletecours/<int:id>", coursviews.delete),

    path('ajoutgrp/<int:id>/', groupeviews.ajout),
    path('traitementgrp/<int:id>/', groupeviews.traitement),
    path('allgrp', groupeviews.all),
    path("affichegrp/<int:id>/", groupeviews.affiche),
    path("updategrp/<int:id>/", groupeviews.update),
    path("updatetraitementgrp/<int:id>/", groupeviews.updatetraitement),
    path("deletegrp/<int:id>", groupeviews.delete),

    path('ajoutetud/<int:id>/', etudiantviews.ajout),
    path('traitementetu/<int:id>/', etudiantviews.traitement),
    path('alletud/', etudiantviews.all),
    path("afficheetud/<int:id>/", etudiantviews.affiche),
    path("updateetud/<int:id>/", etudiantviews.update),
    path("updatetraitementetud/<int:id>/", etudiantviews.updatetraitement),
    path("deleteetud/<int:id>", etudiantviews.delete),
]