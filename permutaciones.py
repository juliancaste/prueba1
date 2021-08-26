import itertools
inp_list = [1, 2,3]

def permuta(lista):
    permutations = list(itertools.permutations(lista))
    print(permutations)


permuta(inp_list)