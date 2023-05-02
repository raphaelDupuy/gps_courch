import json

with open('data/data_final.json', 'r') as f:
    data = json.load(f)


def get_depart(node_name):
    pistes = []
    for piste in data['pistes']:
        if piste['noeud_depart'] == node_name:
            pistes.append(piste)
    return pistes

def get_arrivée(node_name):
    pistes = []
    for piste in data['pistes']:
        if piste['noeud_fin'] == node_name:
            pistes.append(piste)
    return pistes

def get_node_index(node_name):
    for i, node in enumerate(data['noeuds']):
        if node['name'] == node_name:
            return i

def noeuds():
    curs = 0
    for noeud in data['noeuds']:
        print(f"[{curs}] {noeud['name']}")
        curs += 1

def get_min(T, depart):
    if T[depart]['lock']:
        min = {'distance': None}
    else:
        return T[depart]
    for noeud in T:
        if (dist := noeud['distance']) != None and not noeud["lock"]:
            if (dist_min := min['distance']) != None:
                if dist_min > dist:
                    min = noeud
            else:
                min = noeud
    return min

def dijkstra(node_depart, node_arrivee):
    if node_depart == node_arrivee:
        print('\nFaites un tour sur vous-même, bravo vous êtes arrivé.')
    else:
        T = []
        trajet = []

        for noeud in data['noeuds']:
            T.append({'name': noeud['name'],
                      'parent': None,
                      'distance': None,
                      'lock': False})

        T[node_depart]['distance'] = 0
        T[node_depart]['lock'] = True
        min = T[node_depart]
        
        # tant que le noeud d'arrivée n'est pas lock
        while T[node_arrivee]['lock'] != True:
            print('ici min;', min['name'])

            # pour les pistes ayant pour départ le min
            for piste in get_depart(min['name']):
                print(piste['name'])

                # on trouve les voisins de min
                for noeud in T:
                    if noeud['name'] == piste['noeud_fin']:
                        if noeud['distance'] is None:
                            print('is None')
                            noeud['distance'] = min['distance'] + piste['longueur']
                            noeud['parent'] = min['name']
                            
                        elif noeud['distance'] > min['distance'] + piste['longueur']:
                            noeud['parent'] = min['name']
                            noeud['distance'] = min['distance'] + piste['longueur']
                            print('ici')

            min['lock'] = True
            min = get_min(T, node_depart)
            print('min', get_min(T, node_depart))
                            

            

        # Calcul du trajet final
        while True:
            trajet.append(T[node_arrivee]['name'])
            if T[node_arrivee]['parent'] is not None:
                node_arrivee = get_node_index(T[node_arrivee]['parent'])
            else:
                break
        trajet.reverse()
        print(trajet)
            




difficulté = int(input('Quel type de skieur êtes-vous ?\n[0] Débutant\n[1] Intermédiaire\n[2] Expérimenté\n     >>'))
noeuds()
node_depart = int(input('Où vous situez vous ?\n     >>'))
node_arrivée = int(input('\nOù souhaitez vous vous rendre ?\n     >>'))

dijkstra(node_depart, node_arrivée)

