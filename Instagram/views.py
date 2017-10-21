from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def suma(request):
    numero1 = request.POST['num1']
    numero2 = request.POST['num2']
    resultado = numero1 + numero2
    context = {'resultado' : resultado}
    return render (request, resultado, context)
