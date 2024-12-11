from django.shortcuts import render


def index(request):
    return render(request, "index.html")

def m3_combat(request):
    return render(request, "m3-combat.html")

def baby_heavy(request):
    return render(request, "baby-heavy.html")

def depo_provera(request):
    return render(request, "depo-provera.html")

def fire_fighting_foam(request):
    return render(request, "fire-fighting-foam.html")

def hair_relaxer(request):
    return render(request, "hair-relaxer.html")

def hernia_mesh(request):
    return render(request, "hernia-mesh.html")

def nec(request):
    return render(request, "nec.html")

def ozempic(request):
    return render(request, "ozempic.html")

def paraquat(request):
    return render(request, "paraquat.html")

def rideshare_assault(request):
    return render(request, "rideshare-assault.html")

def roundup(request):
    return render(request, "roundup.html")

def talcum(request):
    return render(request, "talcum.html")
