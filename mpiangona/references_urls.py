from django.urls import path

from . import views_reference as views


urlpatterns = [
    path(
        "genres/",
        views.liste_genres,
        name="reference-genres",
    ),

    path(
        "situations-matrimoniales/",
        views.liste_situations_matrimoniales,
        name="reference-situations-matrimoniales",
    ),

    path(
        "faritra/",
        views.liste_faritra,
        name="reference-faritra",
    ),

    path(
        "foyers/",
        views.liste_foyers,
        name="reference-foyers",
    ),

    path(
        "diakona-mpiahy/",
        views.liste_diakona_mpiahy,
        name="reference-diakona-mpiahy",
    ),

    path(
        "diakona-mpiahy-details/",
        views.liste_diakona_mpiahy_details,
        name="reference-diakona-mpiahy-details",
    ),

    path(
        "adresses/",
        views.liste_adresses,
        name="reference-adresses",
    ),

    path(
        "communes/",
        views.liste_communes,
        name="reference-communes",
    ),

    path(
        "fokontany/",
        views.liste_fokontany,
        name="reference-fokontany",
    ),

    path(
        "quartiers/",
        views.liste_quartiers,
        name="reference-quartiers",
    ),
]