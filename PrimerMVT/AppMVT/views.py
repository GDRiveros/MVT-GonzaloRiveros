from django.shortcuts import render

# Create your views here.

from django.template import loader, Context
from django.http import HttpResponse
from AppMVT.models import Familiares


def ver_familiares(request):
    template = loader.get_template("template.html")

    familiar1 = Familiares(
        nombre="Luciana",
        apellido="Slutzker",
        numero_de_telefono= 1182967848,
        fecha_de_nacimiento="1979-12-05"
    )

    familiar2 = Familiares(
        nombre="Leonardo",
        apellido="Riveros",
        numero_de_telefono= 1155356478,
        fecha_de_nacimiento="1978-05-08"
    )

    familiar3 = Familiares(
        nombre="Vilma",
        apellido="Galafassi",
        numero_de_telefono= 47986514,
        fecha_de_nacimiento="1945-08-17"
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
