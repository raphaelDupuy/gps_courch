def min(T):
    min = T[0]
    for noeud in T:
        if (dist := noeud['distance']) != None and dist < min['distance']:
            min = noeud
    return min
import json


T = [{'name': 'COL DE CHANROSSA', 'parent': None, 'distance': 3, 'lock': False}, {'name': 'n2', 'parent': None, 'distance': 6, 'lock': False}, {'name': 'CREUX', 'parent': None, 'distance': 1, 'lock': False}, {'name': 'n4', 'parent': None, 'distance': 6, 'lock': False}, {'name': 'bas Roc merlet', 'parent': None, 'distance': 0, 'lock': False}, {'name': 'haut Pyramides', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n7', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n8', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n9', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n10', 'parent': None, 'distance': None, 'lock': False}, {'name': 'haut Roc mugnier', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n12', 'parent': None, 'distance': None, 'lock': False}, {'name': 'haut SIGNAL', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n14', 'parent': None, 'distance': None, 'lock': False}, {'name': 'haut Chapelets', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n16', 'parent': None, 'distance': None, 'lock': False}, {'name': 'bas Pyramides', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n18', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n19', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n20', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n21', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n22', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n23', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n24', 'parent': None, 'distance': None, 'lock': False}, {'name': 'bas Chapelets', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n26', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n27', 'parent': None, 'distance': None, 'lock': False}, {'name': 'BEL AIR', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n29', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n30', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n32', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n33', 'parent': None, 'distance': None, 'lock': False}, {'name': 'PRAMERUEL', 'parent': None, 'distance': None, 'lock': False}, {'name': 'haut Granges', 'parent': None, 'distance': None, 'lock': False}, {'name': 'bas Signal', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n39', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n40', 'parent': None, 'distance': None, 'lock': False}, {'name': 'bas CREUX NOIRS', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n42', 'parent': None, 'distance': None, 'lock': False}, {'name': 'haut AIGUILLE DU FRUIT', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n44', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n45', 'parent': None, 'distance': None, 'lock': False}, {'name': 'bas SUISSES', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n47', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n48', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n49', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n50', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n51', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n52', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n53', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n54', 'parent': None, 'distance': None, 'lock': False}, {'name': 'bas Belvédère', 'parent': None, 'distance': None, 'lock': False}, {'name': 'haut Belvédère', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n55', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n56', 'parent': None, 'distance': None, 'lock': False}, {'name': 'bas Ariondaz', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n57', 'parent': None, 'distance': None, 'lock': False}, {'name': 'haut PETIT MORIOND', 'parent': None, 'distance': None, 'lock': False}, {'name': 'bas PETIT MORIOND', 'parent': None, 'distance': None, 'lock': False}, {'name': 'haut CREUX NOIRS', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n61', 'parent': None, 'distance': None, 'lock': False}, {'name': 'VIZELLE', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n63', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n64', 'parent': None, 'distance': None, 'lock': False}, {'name': 'haut SAULIRE', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n66', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n67', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n68', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n70', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n71', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n72', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n73', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n74', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n75', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n76', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n77', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n78', 'parent': None, 'distance': None, 'lock': False}, {'name': "haut SOURCES / ROCHER DE L'OMBRE", 'parent': None, 'distance': None, 'lock': False}, {'name': 'n84', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n85', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n89', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n90', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n91', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n92', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n94', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n95', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n96', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n97', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n98', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n99', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n100', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n101', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n102', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n103', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n104', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n105', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n106', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n107', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n108', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n110', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n111', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n112', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n116', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n118', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n119', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n120', 'parent': None, 'distance': None, 'lock': False}, {'name': "bas SOURCES / ROCHER DE L'OMBRE", 'parent': None, 'distance': None, 'lock': False}, {'name': 'n123', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n124', 'parent': None, 'distance': None, 'lock': False}, {'name': 'bas COQS', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n126', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n127', 'parent': None, 'distance': None, 'lock': False}, {'name': 'bas LOZE', 'parent': None, 'distance': None, 'lock': False}, {'name': 'bas VERDONS', 'parent': None, 'distance': None, 'lock': False}, {'name': 'bas JARDIN ALPIN', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n134', 'parent': None, 'distance': None, 'lock': False}, {'name': 'bas BELLECOTE', 'parent': None, 'distance': None, 'lock': False}, {'name': 'haut COSPILLOT', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n132', 'parent': None, 'distance': None, 'lock': False}, {'name': 'le plan du vah', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n130', 'parent': None, 'distance': None, 'lock': False}, {'name': 'verdons', 'parent': None, 'distance': None, 'lock': False}, {'name': 'biollay', 'parent': None, 'distance': None, 'lock': False}, {'name': 'courchevel-village', 'parent': None, 'distance': None, 'lock': False}, {'name': 'saint bon', 'parent': None, 'distance': None, 'lock': False}, {'name': 'bas roys', 'parent': None, 'distance': None, 'lock': False}, {'name': 'haut roys', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n128', 'parent': None, 'distance': None, 'lock': False}, {'name': 'courchevel- village', 'parent': None, 'distance': None, 'lock': False}, {'name': 'chenus', 'parent': None, 'distance': None, 'lock': False}, {'name': 'lozes', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n133', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n135', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n136', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n137', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n138', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n139', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n140', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n141', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n142', 'parent': None, 'distance': None, 'lock': False}, {'name': 'col de la loze', 'parent': None, 'distance': None, 'lock': False}, {'name': 'haut des lanches', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n145', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n146', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n147', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n148', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n149', 'parent': None, 'distance': None, 'lock': False}, {'name': 'plantery', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n151', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n152', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n154', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n155', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n156', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n157', 'parent': None, 'distance': None, 'lock': False}, {'name': 'bas stade', 'parent': None, 'distance': None, 'lock': False}, {'name': 'la tania', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n160', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n161', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n162', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n163', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n164', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n165', 'parent': None, 'distance': None, 'lock': False}, {'name': 'haut epicea', 'parent': None, 'distance': None, 'lock': False}, {'name': 'troika', 'parent': None, 'distance': None, 'lock': False}, {'name': 'meribel', 'parent': None, 'distance': None, 'lock': False}, {'name': 'meribel-mottaret', 'parent': None, 'distance': None, 'lock': False}, {'name': 'meribel-mottaret meribel', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n171', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n172', 'parent': None, 'distance': None, 'lock': False}, {'name': 'n150', 'parent': None, 'distance': None, 'lock': False}, {'name': 'corchevel -le praz', 'parent': None, 'distance': None, 'lock': False}]

curs = 0
for noeud in T:
    if noeud['name'] == 'PRAMERUEL':
        print(curs)
    curs += 1



















# Bckp

# import json
# import heapq

# with open('data/data_final.json', 'r') as f:
#     data = json.load(f)

# node = data['noeuds'][0]

# def get_depart(node_name):
#     pistes = []
#     for piste in data['pistes']:
#         if piste['noeud_depart'] == node_name:
#             pistes.append(piste)
#     return pistes

# def get_arrivée(node_name):
#     pistes = []
#     for piste in data['pistes']:
#         if piste['noeud_fin'] == node_name:
#             pistes.append(piste)
#     return pistes

# def noeuds():
#     curs = 0
#     for noeud in data['noeuds']:
#         print(f"[{curs}] {noeud['name']}")
#         curs += 1

# def get_min(T):
#     min = T[0]
#     for noeud in T:
#         if (dist := noeud['distance']) != None and dist < min['distance']:
#             min = noeud
#     return min

# def dijkstra(node_depart, node_arrivée):
#     if node_depart == node_arrivée:
#         print('\nFaites un tour sur vous même, bravo vous êtes arrivés.')
#     else:
#         T = []
#         trajet = []
#         for noeud in data['noeuds']:
#             T.append({'name': noeud['name'],
#                       'parent': None,
#                       'distance': None,
#                       'lock': False})
#         T[node_depart]['distance'] = 0
#         T[node_depart]['lock'] = True
#         while T[node_arrivée]['lock'] != True:
#             min = get_min(T)
#             for piste in (get_depart(min['name'])):
#                 print(piste['longueur'])
#                 for noeud in T:
#                     if noeud['name'] == piste['noeud_fin']:
#                         noeud['parent'] = min['name']
#                         noeud['distance'] = min['distance'] + piste['longueur']
#                         print(noeud['name'])
#             min['lock'] = True

#         print(T)
            




# difficulté = int(input('Quel type de skieur êtes-vous ?\n[0] Débutant\n[1] Intermédiaire\n[2] Expérimenté\n     >>'))
# noeuds()
# node_depart = int(input('Où vous situez vous ?\n     >>'))
# node_arrivée = int(input('\nOù souhaitez vous vous rendre ?\n     >>'))

# dijkstra(node_depart, node_arrivée)
