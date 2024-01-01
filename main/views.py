from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, "main.html")


def todos(request):
    return render(request, "todos.html")