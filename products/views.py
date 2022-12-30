from django.shortcuts import render

# Create views 
def index(request):
  return render(request, 'products/index.html')
