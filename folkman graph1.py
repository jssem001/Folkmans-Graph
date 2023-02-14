import networkx as nx
import matplotlib.pyplot as plt 
#import pandas as pd


G = nx.Graph()
#Add nodes to your graph
G.add_node('a')
G.add_node('b')
G.add_node('c')
G.add_node('d')
G.add_node('e')
G.add_node('f')
G.add_node('g')
G.add_node('h')
G.add_node('i')
G.add_node('j')
G.add_node('k')
G.add_node('l')

#Add Edges to your graph 
G.add_edge('a','b'), G.add_edge('a','d'), G.add_edge('a','f'),
G.add_edge('a','h'), G.add_edge('b','c'), G.add_edge('b','k'), 
G.add_edge('b','i'), G.add_edge('c','d'), G.add_edge('c','h'),
G.add_edge('c','f'), G.add_edge('d','i'), G.add_edge('d','k'),
G.add_edge('e','f'), G.add_edge('e','h'), G.add_edge('f','g'),
G.add_edge('g','h'), G.add_edge('i','j'), G.add_edge('i','l'),
G.add_edge('j','k'), G.add_edge('k','l'), G.add_edge('e','g'),
G.add_edge('j','l')






nx.draw(G, with_labels = True, font_weight= 'bold')
plt.show() 

