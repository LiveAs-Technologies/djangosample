from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, "index.php")
def what(request):
	return render(request, "what.php")