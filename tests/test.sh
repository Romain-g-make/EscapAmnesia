# 1. Démarrer la partie
curl -X POST -H "Content-Type: application/json" -d '{"etat":"en_jeu","temps_restant":60,"niveau_actuel":1}' http://127.0.0.1:8000/start

# Définir l'ID reçu de la commande précédente
ID=$(curl -X POST -H "Content-Type: application/json" -d '{"etat":"en_jeu","temps_restant":60,"niveau_actuel":1}' http://127.0.0.1:8000/start)

# 2. Objets et salle
curl -X GET http://127.0.0.1:8000/$ID/room/get
curl -X GET http://127.0.0.1:8000/$ID/indice
curl -X GET http://127.0.0.1:8000/$ID/objet/get
curl -X GET http://127.0.0.1:8000/$ID/objet/inspect/1

# 3. Inventaire
curl -X PATCH http://127.0.0.1:8000/$ID/inventory/addItem/1
curl -X PATCH http://127.0.0.1:8000/$ID/inventory/addItem/2
curl -X GET http://127.0.0.1:8000/$ID/inventory/showInventory
curl -X DELETE http://127.0.0.1:8000/$ID/inventory/removeItem/1

# 4. Interaction et échappement
curl -X PATCH http://127.0.0.1:8000/$ID/objets/interact/1-2
curl -X PATCH http://127.0.0.1:8000/$ID/tryescape/1234

# 5. Supprimer la partie
curl -X DELETE http://127.0.0.1:8000/$ID