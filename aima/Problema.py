import search
#Estado inicial (3,2,1,1)   Estado Final (0,0,0,0)
#Grafo com as ações do problema dos 3 humanos e 3 macacos
graph = {
    (3,2,1,1):[(3,2,0,0), (3,1,0,0), (2,2,0,0), (2,1,1,0)],
    (3,2,0,0):[(3,2,1,1)],
    (3,1,0,0):[(3,2,1,1), (3,1,1,1)],
    (2,2,0,0):[(3,2,1,1), (3,2,0,1)],
    (2,1,1,0):[(3,2,1,1), (3,1,1,1)],
    (3,1,1,1):[(3,1,0,0), (2,1,1,0), (3,0,0,0)],
    (3,2,0,1):[(2,2,0,0)],
    (3,0,0,0):[(3,0,1,1), (3,1,1,1)],
    (3,0,1,1):[(1,0,1,0), (3,0,0,0)],
    (1,0,1,0):[(2,1,1,1), (3,0,1,1)],
    (2,1,1,1):[(1,1,0,0), (1,0,1,0)],
    (1,1,0,0):[(2,1,1,1), (2,2,0,1)],
    (2,2,0,1):[(1,1,0,0), (0,2,0,0)],
    (0,2,0,0):[(2,2,0,1), (0,2,1,1)],
    (0,2,1,1):[(0,2,0,0), (0,1,0,0)],
    (0,1,0,0):[(0,2,1,1), (0,1,1,1), (1,1,0,1)],
    (0,1,1,1):[(0,1,0,0), (0,0,0,0)],
    (1,1,0,1):[(0,1,0,0), (0,0,0,0)],
    (0,0,0,0):[(1,1,0,1), (0,1,1,1), (0,0,1,1), (1,0,1,1)],
    (0,0,1,1):[(0,0,0,0)],
    (1,0,1,1):[(0,0,0,0), (0,0,1,0)],
    (0,0,1,0):[(1,0,1,1)]
}

estado_inicial = (3,2,1,1)
estado_final = (0,0,0,0)

resultado = search.Problem((3,2,1,1), (0,0,0,0), graph)

busca_em_largura = search.breadth_first_graph_search(resultado)
busca_em_profundidade = search.depth_first_graph_search(resultado)
busca_em_profundidade_limitada = search.depth_limited_search(resultado, 20)
busca_em_profundidade_limitada_iterativa = search.iterative_deepening_search(resultado)


solucao = busca_em_largura.solution()
print("Resultado da busca em largura:\n0 º ",estado_inicial)
for i, v in enumerate(solucao):
    print(i+1,"º ", v)
print("\n\n")
solucao = busca_em_profundidade.solution()
print("Resultado da busca em profundidade:\n0 º ",estado_inicial)
for i, v in enumerate(solucao):
    print(i+1,"º ", v)
print("\n\n")
solucao = busca_em_profundidade_limitada.solution()
print("Resultado da busca em profundidade limitada:\n0 º ",estado_inicial)
for i, v in enumerate(solucao):
    print(i+1,"º ", v)
print("\n\n")
solucao = busca_em_profundidade_limitada_iterativa.solution()
print("Resultado da busca em profundidade limitada e iterativa:\n0 º ",estado_inicial)
for i, v in enumerate(solucao):
    print(i+1,"º ", v)
