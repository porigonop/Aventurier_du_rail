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
        
        ferm_trans = Graph()

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
