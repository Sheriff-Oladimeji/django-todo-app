from django.shortcuts import render

# Create your views here.
def Main(request):
    return render(request, "main.html")


def Todos(request):
    return render(request, "todos.html")