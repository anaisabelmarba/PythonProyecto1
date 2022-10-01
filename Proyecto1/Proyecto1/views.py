from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Django - Coder")

def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :)")

import datetime 
def diaDeHoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es dia: <br> {dia}"
    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    
    documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"
    
    return HttpResponse(documentoDeTexto)

from datetime import date
    
def calcular_nacimiento(request):
    edad_actual = 31 
    anioActual = date.today().year
    nacimiento = date.today().year - edad_actual 
    return HttpResponse(nacimiento)

from django.template import Template, Context

def probandoTemplate(self):
    miHtml = open("C:/Users/Usuario/Desktop/PythonProyecto1/Proyecto1/Proyecto1/Plantillas/template1.html")
    plantillas = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantillas.render(miContexto)
    return HttpResponse(documento)
    
    


    
    
    
    
    
    


