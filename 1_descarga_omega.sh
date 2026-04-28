#!/bin/bash

echo "1. Consultando VizieR TAP mediante ADQL para Omega Centauri..."

# Consulta ADQL (Omega Centauri)
ADQL="SELECT Source, RA_ICRS, DE_ICRS, pmRA, pmDE, Gmag, BPmag, RPmag FROM \"I/355/gaiadr3\" WHERE 1=CONTAINS(POINT('ICRS', RA_ICRS, DE_ICRS), CIRCLE('ICRS', 201.697, -47.479, 0.5))"

# Codificar espacios
URL_ADQL=$(echo $ADQL | sed 's/ /+/g')

# Endpoint TAP
TAP_URL="https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync?request=doQuery&lang=ADQL&format=csv&query="

# Descarga
wget -O omega_bruto.csv "$TAP_URL$URL_ADQL"
