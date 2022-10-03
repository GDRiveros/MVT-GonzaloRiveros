from django.shortcuts import render

# Create your views here.

from django.template import loader, Context
from django.http import HttpResponse
from AppMVT.models import Familiares
#from datetime import datetime


def ver_familiares(request):
    template = loader.get_template("template.html")

    #nacimiento_familiar1 = datetime(1979, 12, 5)
    #nacimiento_familiar2 = datetime(1978, 5, 8)
    #nacimiento_familiar3 = datetime(1945, 8, 17)


    familiar1 = Familiares(
        nombre="Luciana",
        apellido="Slutzker",
        numero_de_telefono= 1182967848,
        fecha_de_nacimiento= "1979-12-05"               #nacimiento_familiar1.strftime("%Y - %m - %d")
    )

    familiar2 = Familiares(
        nombre="Leonardo",
        apellido="Riveros",
        numero_de_telefono= 1155356478,
        fecha_de_nacimiento= "1978-05-08"                #nacimiento_familiar2.strftime("%Y - %m - %d")
    )

    familiar3 = Familiares(
        nombre="Vilma",
        apellido="Galafassi",
        numero_de_telefono= 47986514,
        fecha_de_nacimiento= "1945-08-17"                 #nacimiento_familiar3.strftime("%Y - %m - %d")
    )

    familiar1.save() #Guardando los familiares en la base de datos
    familiar2.save()
    familiar3.save()

    dict_de_context = {
        "familiar1": familiar1,
        "familiar2": familiar2,
        "familiar3": familiar3
    }

    result = template.render(dict_de_context)

    return HttpResponse(result)
