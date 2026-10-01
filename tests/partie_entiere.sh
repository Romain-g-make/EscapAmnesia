#!/bin/bash

BASE_URL="http://127.0.0.1:8000"

echo "=================================================="
echo " 🟢 1. DÉMARRAGE DE LA PARTIE (POST /start)"
echo "=================================================="
RESPONSE=$(curl -s -X POST -H "Content-Type: application/json" \
  -d '{"etat":"en_jeu","temps_restant":3600,"niveau_actuel":1}' \
  $BASE_URL/start)

# Extraction stricte de l'UUID de la partie
ID=$(echo "$RESPONSE" | python3 -c "import sys, json; print(json.load(sys.stdin).get('id', ''))")

if [ -z "$ID" ]; then
    echo "❌ Erreur de création de partie."
    exit 1
fi

echo "Partie créée avec succès. ID : $ID"
echo ""

echo "=================================================="
echo " 🗝️ 2. ÉNIGME 1 : LA CHAMBRE (Sortie : 7635)"
echo "=================================================="
echo "--> Inspection de la chambre :"
curl -s -X GET "$BASE_URL/$ID/room/get"
echo -e "\n"

echo "--> Déverrouillage du coffre sous le lit (Injecteur UV / Item #1) :"
curl -s -X PATCH "$BASE_URL/$ID/inventory/addItem/1"
echo -e "\n"

echo "--> Inspection du coffre quantique (Objet #2) :"
curl -s -X GET "$BASE_URL/$ID/objet/inspect/2"
echo -e "\n"

echo "--> Récupération de l'Oculomètre (Item #4) :"
curl -s -X PATCH "$BASE_URL/$ID/inventory/addItem/4"
echo -e "\n"

echo "--> Tentative de déverrouillage de la Porte de la Chambre (Code 7635) :"
curl -s -X PATCH "$BASE_URL/$ID/tryescape/7635"
echo -e "\n"

echo "=================================================="
echo " 🚪 3. ÉNIGME 2 : L'IMMEUBLE (Sortie : 84693)"
echo "=================================================="
echo "--> Récupération de la Pile Lithium-Cristal (Item #6, indice 84) :"
curl -s -X PATCH "$BASE_URL/$ID/inventory/addItem/6"
echo -e "\n"

echo "--> Récupération de la Puce de Déchiffrement (Item #7, indice 693) :"
curl -s -X PATCH "$BASE_URL/$ID/inventory/addItem/7"
echo -e "\n"

echo "--> Insertion de la pile et de la puce dans le Terminal de Décharge (Objet #8) :"
curl -s -X PATCH "$BASE_URL/$ID/objets/interact/8-6"
echo -e "\n"

echo "--> Déverrouillage du Sas du Rez-de-Chaussée (Code 84693) :"
curl -s -X PATCH "$BASE_URL/$ID/tryescape/84693"
echo -e "\n"

echo "=================================================="
echo " 🧠 4. ÉNIGME 3 : ESPACE NEURO-VIRTUEL (Sortie : 101)"
echo "=================================================="
echo "--> Récupération de la Bande de Données Magnétique (Item #11) :"
curl -s -X PATCH "$BASE_URL/$ID/inventory/addItem/11"
echo -e "\n"

echo "--> Insertion de la bande dans l'Analyseur de Neuro-Trauma (Objet #9) :"
curl -s -X PATCH "$BASE_URL/$ID/objets/interact/9-11"
echo -e "\n"

echo "--> Alignement des canaux A, B, C sur 101 (Code 101) :"
curl -s -X PATCH "$BASE_URL/$ID/tryescape/101"
echo -e "\n"

echo "=================================================="
echo " 🏁 5. NETTOYAGE (Suppression de la partie)"
echo "=================================================="
curl -s -X DELETE "$BASE_URL/$ID"
echo "Partie $ID fermée et supprimée."