from django.shortcuts import render

# Create your views here.
def productpage(request):
    print("page added")
    return render(request,"product.html")