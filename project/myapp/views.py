from django.shortcuts import render

# Create your views here.
def Productos(request):
    ejemplo = 'Entrevista'
    return render(request, 'producto-list.html',{
        'ejemplo': ejemplo
    })