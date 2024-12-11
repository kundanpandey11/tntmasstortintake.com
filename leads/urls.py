from django.urls import path
from .views import (
    index,
    m3_combat,
    baby_heavy,
    depo_provera,
    fire_fighting_foam,
    hair_relaxer,
    hernia_mesh,
    nec,
    ozempic,
    paraquat,
    rideshare_assault,
    roundup,
    talcum,
)

urlpatterns = [
    path("", index, name="index"),  # Render index.html at root
    path("m3-combat/", m3_combat, name="m3_combat"),
    path("baby-heavy/", baby_heavy, name="baby_heavy"),
    path("depo-provera/", depo_provera, name="depo_provera"),
    path("fire-fighting-foam/", fire_fighting_foam, name="fire_fighting_foam"),
    path("hair-relaxer/", hair_relaxer, name="hair_relaxer"),
    path("hernia-mesh/", hernia_mesh, name="hernia_mesh"),
    path("nec/", nec, name="nec"),
    path("ozempic/", ozempic, name="ozempic"),
    path("paraquat/", paraquat, name="paraquat"),
    path("rideshare-assault/", rideshare_assault, name="rideshare_assault"),
    path("roundup/", roundup, name="roundup"),
    path("talcum/", talcum, name="talcum"),
]
