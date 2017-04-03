from django.shortcuts import render
from cms_put.models import Pages
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def show(request):
    content = Pages.objects.all()
    response = ""
    for entry in content:
        response = entry.name + ": " + entry.page + "<br>" + response
    return HttpResponse(response)


@csrf_exempt
def entry(request, resource):
    if request.method == "GET":
        try:
            entry = Pages.objects.get(name=resource)
            return HttpResponse(entry.page)
        except Pages.DoesNotExist:
            response = "No existe esa página. Puedes crearla:"
            response += "<form action='/" + resource + "' method=POST>"
            response += "Nombre: <input type='text' name='nombre'>"
            response += "<br>Página: <input type='text' name='page'>"
            response += "<input type='submit' value='Enviar'></form>"
    elif request.method == "POST":
        nombre = request.POST['nombre']
        page = request.POST['page']
        pagina = Pages(name=nombre, page=page)
        pagina.save()
        response = "Se ha creado la página " + nombre
    elif reques.method == "PUT":
        try:
            page = Pages.objects.get(name=resource)
            response = "Ya hay una página con ese nombre"
        except Pages.DoesNotExist:
            page = request.body
            pagina = Pages(name=resource, page=page)
            pagina.save()
            response = "Se ha creado la página " + resource
    else:
        response = "Error. Método no soportado."
    return HttpResponse(response)


def error(request):
    response = "El recurso solicitado no existe"
    return HttpResponse(response)
