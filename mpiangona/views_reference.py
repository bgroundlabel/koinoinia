from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
    ParGenres,
    ParSitMatr,
    ParFgnFaritra,
    TFoyers,
    TDiakonaMpiahyHdr,
    TDiakonaMpiahyDtl,
    TAdresses,
    ParGeoCommunes,
    ParGeoFokontany,
    ParGeoQuartiers,
)


# ==========================================================
# FONCTION GENERIQUE POUR LES LISTES DE REFERENCE
# ==========================================================

def liste_reference(modele, champs, tri):
    """
    Retourne une liste de données provenant d'un modèle Django.
    Cette fonction est destinée aux endpoints de référence.
    """
    donnees = modele.objects.all().order_by(tri).values(*champs)
    return Response(list(donnees))


# ==========================================================
# 1. GENRES
# Table : par_genres
# URL : /api/references/genres/
# ==========================================================

@api_view(["GET"])
def liste_genres(request):
    return liste_reference(
        ParGenres,
        ["id", "code", "libelle"],
        "id",
    )


# ==========================================================
# 2. SITUATIONS MATRIMONIALES
# Table : par_sit_matr
# URL : /api/references/situations-matrimoniales/
# ==========================================================

@api_view(["GET"])
def liste_situations_matrimoniales(request):
    return liste_reference(
        ParSitMatr,
        ["id", "code", "libelle"],
        "id",
    )


# ==========================================================
# 3. FARITRA
# Table : par_fgn_faritra
# URL : /api/references/faritra/
# ==========================================================

@api_view(["GET"])
def liste_faritra(request):
    return liste_reference(
        ParFgnFaritra,
        ["id", "code", "libelle", "description", "est_visible"],
        "libelle",
    )


# ==========================================================
# 4. FOYERS
# Table : t_foyers
# URL : /api/references/foyers/
# ==========================================================

@api_view(["GET"])
def liste_foyers(request):
    return liste_reference(
        TFoyers,
        [
            "id",
            "numero",
            "chef_id",
            "libelle",
            "est_actif",
            "est_visible",
        ],
        "id",
    )


# ==========================================================
# 5. EQUIPES DIAKONA MPIAHY
# Table : t_diakona_mpiahy_hdr
# URL : /api/references/diakona-mpiahy/
# ==========================================================

@api_view(["GET"])
def liste_diakona_mpiahy(request):
    return liste_reference(
        TDiakonaMpiahyHdr,
        [
            "id",
            "mandat",
            "libelle",
            "est_actif",
            "est_visible",
        ],
        "id",
    )


# ==========================================================
# 6. DETAILS DES EQUIPES DIAKONA MPIAHY
# Table : t_diakona_mpiahy_dtl
# URL : /api/references/diakona-mpiahy-details/
# ==========================================================

@api_view(["GET"])
def liste_diakona_mpiahy_details(request):
    return liste_reference(
        TDiakonaMpiahyDtl,
        [
            "id",
            "hdr_id",
            "diakona_id",
            "description",
            "est_actif",
            "est_visible",
        ],
        "id",
    )


# ==========================================================
# 7. ADRESSES
# Table : t_adresses
# URL : /api/references/adresses/
# ==========================================================

@api_view(["GET"])
def liste_adresses(request):
    return liste_reference(
        TAdresses,
        [
            "id",
            "logement",
            "repere",
            "fgn_faritra_id",
            "fokontany_id",
            "quartier_id",
        ],
        "id",
    )


# ==========================================================
# 8. COMMUNES
# Table : par_geo_communes
# URL : /api/references/communes/
# ==========================================================

@api_view(["GET"])
def liste_communes(request):
    return liste_reference(
        ParGeoCommunes,
        ["id", "code", "nom"],
        "nom",
    )


# ==========================================================
# 9. FOKONTANY
# Table : par_geo_fokontany
# URL : /api/references/fokontany/
# ==========================================================

@api_view(["GET"])
def liste_fokontany(request):
    return liste_reference(
        ParGeoFokontany,
        ["id", "code", "nom", "commune_id"],
        "nom",
    )


# ==========================================================
# 10. QUARTIERS
# Table : par_geo_quartiers
# URL : /api/references/quartiers/
# ==========================================================

@api_view(["GET"])
def liste_quartiers(request):
    return liste_reference(
        ParGeoQuartiers,
        ["id", "code", "nom", "fokontany_id"],
        "nom",
    )