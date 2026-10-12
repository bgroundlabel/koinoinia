from django.http import JsonResponse
from .models import TMpiangona

def liste_mpiangona(request):
    donnees = list(
       TMpiangona.objects.values()
    )
    return JsonResponse(donnees, safe=False)