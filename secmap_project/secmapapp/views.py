from django.shortcuts import render
def nativemap(request):
    return render(request,'secmapapp/nativemap.html')
def canarabank(request):
    return render(request,'secmapapp/canarabank.html')
def mine(request):
    return render(request,'secmapapp/mine.html')
def neyvelibusstand(request):
    return render(request,'secmapapp/neyvelibusstand.html')
def NLCschool(request):
    return render(request,'secmapapp/NLCschool.html')
def stantonychruch(request):
    return render(request,'secmapapp/stantonychruch.html')