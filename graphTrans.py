#!/usr/bin/env python3
from BooleanMatrix import BooleanMatrix
class GraphTrans:
    """This class is a new type for describing the graphs
    """
    def __init__(self):
        """this allow the graph to be create 
        it is empty at the begin
                self.nodes is a set wich contains all the node
                self.edges is a list of every edge in the graph
                self.adjency_list is a dictionnary wich have nodes as
                key and the node linked as values
        """
        self.nodes = set()
        self.edges = list()
        self.adjency_list = dict()

    def add_a_node(self, node_name):
        """add a new node in the node set and refresh the adjency_list
                node_name is a string which contain the new node 
        comming into the graph
        """
        if node_name in self.nodes:
            print("ce node est deja dans le graphe")
            return False
        self.nodes.add(node_name)
        self.adjency_list[node_name] = list()
    
    def add_an_edge(self, from_node, to_node):
        """add en edge between from_node to the node to_node
                from_node is a string which contain the parent node
                to_node is a string which contain the link's child
        """
        if not(from_node in self.nodes):
            raise NameError("node aren't in the graph : " + str(from_node)) 
            return False
        if not(to_node in self.nodes):
            raise NameError("node aren't in the graph : " + str(to_node)) 
            return False
        self.edges.append((from_node, to_node))
        self.adjency_list[from_node].append(to_node)
        
    def __str__(self):
        """allow the user to display the graph in a print()
        """
        nodes = ""
        for node in self.nodes:
            nodes += str(node) + ", \n"
        
        edges = ""
        for edge in self.edges:
            edges += str(edge[0]) + "---->" + str(edge[1]) + "\n"
        
        return \
        "*************************\n"\
        "*  Display of the graph *\n"\
        "*************************\n"\
        "Nodes :\n"\
        "------------\n" +\
        nodes[:len(nodes)-1] +"\n"+\
        "Edges :\n"\
        "------------\n"+\
        edges +"\n" +\
        "=========================\n"

    def breadth_first_search(self, departure):
        """
        return a dictionnary that have node as key and node as value 
        the node in value is the parent of the node in the key
        
        use the fifo methode to determine which one is the next to look at.
        
            departure is the first starting point of the course
        """
        colors = {}
        for node in self.nodes:
            colors[node] = "white"
            
        parents = {}
        fifo = []
        fifo.append(departure)
        colors[departure] = "grey"
        parents[departure] = None
        
        for node in sorted(self.nodes):

            while fifo != []:
                in_progress = fifo[0]
                fifo.pop(0)
                for neighbour \
                        in sorted(self.adjency_list[in_progress]):
                    if colors[neighbour] == "white":
                        parents[neighbour] = in_progress
                        colors[neighbour] = "grey"
                        fifo.append(neighbour)
                colors[in_progress] = "black"
                
                
            
            if colors[node] != "white":
                continue
            colors[node] = "grey"
            parents[node] = None
            fifo.append(node)
            
        return parents
        
    def recursive(self,\
                colors, \
                lifo = [], \
                departure = None, \
                parents = {}):
                
        """
         useful for depth_first_search to always look at the last
         in and change the focus with every new neighbour found
         
         it allow to go to the next node and keep the current in another 
         iteration
        """
                
        if departure != None:
            lifo = []
            lifo.append(departure)
            parents = {}
            colors[departure] = "grey"
            parents[departure] = None
        departure = None
        
        if lifo != []:
            in_progress = lifo[-1]
            lifo.pop()
            for neighbour \
                    in sorted(self.adjency_list[in_progress]):
                if colors[neighbour] == "white":
                    parents[neighbour] = in_progress
                    colors[neighbour] = "grey"
                    lifo.append(neighbour)
                    colors[in_progress] = "black"
                    parents, colors = self.recursive(lifo = lifo, \
                                            colors = colors, \
                                            departure = None, \
                                            parents = parents)
                
            if lifo == []:
                return parents, colors
    
    def depth_first_search(self, departure):
        """
        return a dictionnary that have node as key and node as value 
        the node in value is the parent of the node in the key

        use the lifo methode to determine which one is the next to look at.

            departure is the starting point of the course
        """
        colors = {}
        parents_list = []
        parents = {}
        for node in self.nodes:
            colors[node] = "white"
        in_queue, colors = self.recursive(colors = colors,\
                                            departure = departure)
        parents_list.append(in_queue)
        for node in sorted(self.nodes):
            if node in parents or colors[node] != "white":
                continue
            in_queue, colors = self.recursive(colors = colors,\
                                                departure = node)
            parents_list.append(in_queue)
            
        for parents_ in parents_list:
            for key in parents_:
                parents[key] = parents_[key]
        return parents
        
    def is_bipartite(self):
        """
        this methode attribut a colors at each node in the graph, 
        based on the parent/child combinaison given by the
        breadth_first_search methode it while give a different color to the
        child and the parent, if there is a problem in the attribution then
        the graph isn't bipartite, after that, if it succed,
        all the node have a color and we just have to test with the list of
        edges if they all have a different colors

        return True or False
        """
        parents = self.breadth_first_search(sorted(list(self.nodes))[0])
        
        
        colors = {}
        for key in sorted(list(parents)):
            
            if parents[key] == None:
                continue
                
            if  key in colors and \
                parents[key] in colors and\
                colors[key] != colors[parents[key]]:
                return False
                
            if key in colors:
                colors[parents[key]] = - colors[key]
                continue
                
            if parents[key] in colors:
                colors[key] = - colors[parents[key]]
                continue
            
            

            colors[key] = 1
            colors[parents[key]] = -1
        
        
        for edge in self.edges:
            from_node, to_node = edge
            if colors[from_node] == colors[to_node]:
                return False
                
        return True
    
    def articulation_point(self):
        """
        find every articulation point in a non-oriented graph,
        with the simple algorythm that use the facts that this point
        will have 2 sons or more in a depth course algorythm
        so the method test every point and test if it has more than
        2sons
        
        return a list of node
        """
        articulation_point = []
        for root in self.nodes:
            course = self.depth_first_search(root)
            if len([node for node in course.values() \
                        if node == root]) >= 2:
                articulation_point.append(root)
        return articulation_point
            
            
        
        return articulation_point
    
    def is_non_oriented(self):
        """ return True if non oriented
            return False if oriented
         """
        for elt in self.edges:
            if not ((elt[1], elt[0]) in self.edges):
                return False
        return True
        
    def connected_component(self):
        """ return a list of list with every connected component
        """
        list_nodes = list(self.nodes)
        if not self.is_non_oriented():
            raise TypeError("graph must be non oriented")
            return False
            
        parent = self.breadth_first_search(list_nodes[0])
        answer = []
        in_elt = False
        for key in parent:
            in_elt = False
            
            for elt in answer:
                if parent[key] in elt:
                    elt.append(key)
                    in_elt = True
                    
            if not in_elt:
                answer.append([key])
                
        return answer
       
    def is_connected(self):
        """ return True if connexe
            return False if not
        """
        return True if len(self.connected_component()) == 1 else False
        
    def is_oriented(self):
        """return True if the grpah is oriented
        False if non oriented
        """
        return not self.is_non_oriented()
        
    
    def transitive_closure_V1(self):
        """
        Renvoie le graph correspondant à la fermeture transitive du graph self.
        La méthode utilisée est celle du calcul successif des puissances de M
        (M + M^2 + ... + M^n).
        
        :exemple:
        --------
        
        >>>graph1 = Graph()
        >>>for i in range(4):
                graph1.add_a_node(str(i))
        >>>graph1.add_an_edge('0', '1')
        >>>graph1.add_an_edge('1', '3')
        >>>print(graph1)
        ************************
        * Display of the graph *
        ************************
        Nodes:
        ------

        1, 2, 3, 0

        Edges:
        ------

        0 ---> 1
        1 ---> 3
        =========================

        >>>print(graph1.transitive_closure_V1())
        ************************
        * Display of the graph *
        ************************
        Nodes:
        ------

        1, 2, 3, 0

        Edges:
        ------

        0 ---> 1
        0 ---> 3
        1 ---> 3
        =========================
        
        """

        
        if len(self.nodes) == 0:
            raise ValueError("On ne peut pas calculer la fermeture transitive"
                             + " d'un graph sans sommets")
        
        
        # On calcule d'abord M la matrice booléenne associée au graph self. 
         
        # Creation de nodes. nodes est une list contenant les sommets du graph
        # self. nodes est trié par python en utilisant:
        #   -le nombre dans la table ascii pour les chaines de caractères
        #   -l'ordre des nombres pour les nombres 
        nodes = list(self.nodes)
        nodes.sort()
        
        # Coefficients va contenir les coefficients de M la matrice associée au
        # graph self.
        coefficients = []

        # remplissage de coefficients.
        # Parcours des lignes de la matrice.
        for i in nodes:
            ligne = []
            #Parcours des colonnes de la matrice
            for j in nodes:
                # Ajout de 1 si le graph contient l'arrête i -> j
                if [i, j] in self.edges:
                    ligne.append(1)
                else:
                    ligne.append(0)
                    
            # Ajout de la ligne à coefficients.        
            coefficients.append(ligne)

        # M est la matrice booléenne associée au graph self.
        M = BooleanMatrix(coefficients)
        
        # Calcul de matrix_ferm_trans la matrice de la fermeture transitive du
        # graph self.

        # Initialisation de matrix_ferm_trans.
        matrix_ferm_trans = M
        
        A = M # A va contenir les puissances de M successivement jusqu'a M^n
        for i in range(len(M.coefficients)-1):
            A = M.multiply(A)
            matrix_ferm_trans.add(A)

        
        # Création de ferm_trans la fermeture transitive du graph self à partir
        # de matrix_ferm_trans
        
        ferm_trans = GraphTrans()

        # ferm_trans reprend les mêmes sommets que le graph self.
        for node in nodes:
            ferm_trans.add_a_node(node)

        # On parcours les lignes de la matrice de la fermeture transitive.
        for ligne in range(len(matrix_ferm_trans.coefficients)):
            
            # On parcours les colonnes de la matrice de la fermeture transitive.
            for colonne in range(len(matrix_ferm_trans.coefficients)):
                
                # Si le coefficient dans la matrice est égal à 1 on ajoute à
                # ferm_trans l'arrête allant du sommet associé à la ligne vers le
                # sommet associé à la colonne.
                if matrix_ferm_trans.coefficients[ligne][colonne] == 1:
                    ferm_trans.add_an_edge(nodes[ligne], nodes[colonne])


        return ferm_trans
