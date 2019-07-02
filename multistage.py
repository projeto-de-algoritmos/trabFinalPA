#!/usr/bin/env python
# coding: utf-8

import collections as ct
import graphviz as gv

# # Algoritmo de menor distância

INF=999999999999 # valor arbitrário para infinito


# # Implementando lista de adjagência
graph = ct.defaultdict(list)

# implementamos a lista de adjacência por meio de vetores
# para cada vetor temos suas conexões, primeiro valor é qual ele se conecta e segundo o peso dessa conexão
cities = {
    'Seattle': 0,
    'Newport': 1,
    'San Francisco': 2,
    'USC': 3,
    'Boise': 4,
    'Salt Lake': 5,
    'Las Vegas': 6,
    'Tucson': 7,
    'Casper': 8,
    'Denver': 9,
    'Albuquerque': 10,
    'El Paso': 11,
    'Pierre': 12,
    'Lincoln': 13,
    'Amarillo': 14,
    'San Antonio': 15,
    'Minneapolis': 16,
    'Kansas City': 17,
    'Ft. Smith': 18,
    'Houston': 19,
    'Chicago': 20,
    'St. Louis': 21,
    'Nashville': 22,
    'New Orleans': 23,
    'Pittsburg': 24,
    'Roanoke': 25,
    'Charlotte': 26,
    'Tallahassee': 27,
    'MIT': 28,
    'Washington': 29,
    'Daytona Beach': 30,
    'Wilmington': 31
}
inv_cities = {
    0:'Seattle',
    1:'Newport',
    2:'San Francisco',
    3:'USC',
    4:'Boise',
    5:'Salt Lake',
    6:'Las Vegas',
    7:'Tucson',
    8:'Casper',
    9:'Denver',
    10:'Albuquerque',
    11:'El Paso',
    12:'Pierre',
    13:'Lincoln',
    14:'Amarillo',
    15:'San Antonio',
    16:'Minneapolis',
    17:'Kansas City',
    18:'Ft. Smith',
    19:'Houston',
    20:'Chicago',
    21:'St. Louis',
    22:'Nashville',
    23:'New Orleans',
    24:'Pittsburg',
    25:'Roanoke',
    26:'Charlotte',
    27:'Tallahassee',
    28:'MIT',
    29:'Washington',
    30:'Daytona Beach',
    31:'Wilmington'
}
# Algoritmo de menor distância
graph[cities['Seattle']] = [(494, cities['Boise'])]
graph[cities['Newport']] = [(561, cities['Boise'])]
graph[cities['San Francisco']] = [(648, cities['Boise']), (748, cities['Salt Lake']), (630, cities['Las Vegas'])]
graph[cities['USC']] = [(275, cities['Las Vegas']), (528, cities['Tucson'])]
graph[cities['Boise']] = [(669, cities['Casper'])]
graph[cities['Salt Lake']] = [(402, cities['Casper']), (493, cities['Denver']), (609, cities['Albuquerque'])]
graph[cities['Las Vegas']] = [(576, cities['Albuquerque']), (724, cities['El Paso'])]
graph[cities['Tucson']] = [(452, cities['Albuquerque']), (320, cities['El Paso'])]
graph[cities['Casper']] = [(347, cities['Pierre']), (635, cities['Lincoln'])]
graph[cities['Denver']] = [(667, cities['Lincoln']), (424, cities['Amarillo'])]
graph[cities['Albuquerque']] = [(288, cities['Amarillo']), (714, cities['San Antonio'])]
graph[cities['El Paso']] = [(421, cities['Amarillo']),  (555, cities['San Antonio'])]
graph[cities['Pierre']] = [(478, cities['Minneapolis']), (598, cities['Kansas City'])]
graph[cities['Lincoln']] = [(438, cities['Minneapolis']), (567, cities['Ft. Smith'])]
graph[cities['Amarillo']] = [(613, cities['Kansas City']), (539, cities['Ft. Smith'])]
graph[cities['San Antonio']] = [(635, cities['Ft. Smith']), (199, cities['Houston'])]
graph[cities['Minneapolis']] = [(465, cities['Chicago']), (593, cities['St. Louis'])]
graph[cities['Kansas City']] = [(527, cities['Chicago']), (256, cities['St. Louis'])]
graph[cities['Ft. Smith']] = [(545, cities['St. Louis']), (501, cities['Nashville']), (601, cities['New Orleans'])]
graph[cities['Houston']] = [(635, cities['Nashville']), (352, cities['New Orleans'])]
graph[cities['Chicago']] = [(532, cities['Pittsburg']), (717, cities['Roanoke'])]
graph[cities['St. Louis']] = [(659, cities['Pittsburg']), (689, cities['Roanoke'])]
graph[cities['Nashville']] = [(435, cities['Roanoke']), (434, cities['Charlotte']), (495, cities['Tallahassee'])]
graph[cities['New Orleans']] = [(725, cities['Charlotte']), (388, cities['Tallahassee'])]
graph[cities['Pittsburg']] = [(680, cities['MIT']), (259, cities['Washington'])]
graph[cities['Roanoke']] = [(750, cities['MIT']), (233, cities['Washington']), (669, cities['Daytona Beach'])]
graph[cities['Charlotte']] = [(397, cities['Washington']), (206, cities['Wilmington']), (480, cities['Daytona Beach'])]
graph[cities['Tallahassee']] = [(496, cities['Wilmington']), (316, cities['Daytona Beach'])]

west=[cities['Seattle'], cities['Newport'], cities['San Francisco'], cities['USC']]
east=[cities['MIT'], cities['Washington'], cities['Wilmington'], cities['Daytona Beach']]

dist=ct.defaultdict(lambda:0)
path=ct.defaultdict(lambda:0)

for u in reversed(sorted(graph.keys())):
    dist[u]=INF
    for weight, node in graph[u]:
        # print(u, '--', node, '=', weight)
        if (dist[u] > weight+dist[node]):
            # print('u = ', u, ' node = ', node, ' weight = ', weight, ' dist[u] = ', dist[u], ' dist[node] = ', dist[node])
            dist[u]=weight+dist[node]
            path[u]=node

# identificar o menor caminho para plotagem
path_list = []
# print(dist)

weights = [(dist[w], w) for w in west]
# print(min(weights))
cost, init = min(weights)
print('Cost = ', cost)
print('Path = {', end='')
print(init, end='')
path_list.append(init)
while init not in east:
    init = path[init]
    path_list.append(init)
    print(' --', init, end='')
print('}')

for e in east:
    graph[e]=[]

dot = gv.Digraph(comment='Multistage Graph')
dot.attr(rankdir='LR')

for nodes in graph:
    temp = []
    temp.append(nodes)

    if(set(temp).intersection(path_list)):
        dot.node(str(inv_cities[nodes]), str(inv_cities[nodes]), color='blue')
    else:
        dot.node(str(inv_cities[nodes]), str(inv_cities[nodes]), color='red')

    for v,u in graph[nodes]:
        if(nodes in path_list and u in path_list):
            dot.edge(str(inv_cities[nodes]), str(inv_cities[u]), label=str(v), color='blue')
        else:
            dot.edge(str(inv_cities[nodes]), str(inv_cities[u]), label=str(v))

dot.render('output.gv', view=True)
# print(dot.source)





