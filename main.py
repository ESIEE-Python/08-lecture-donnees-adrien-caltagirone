''' Module '''
#### Imports et définition des variables globales
import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """

    with open(filename, 'r', encoding="utf-8") as f:
        r = csv.reader(f, delimiter=';')
        l = list(r)
    return [list(map(int, x)) for x in l]

def get_list_k(data, k):
    ''' Function '''
    return data[k]

def get_first(l):
    ''' Function '''
    return int(l[0])

def get_last(l):
    ''' Function '''
    return l[-1]

def get_max(l):
    ''' Function '''
    return max(l)

def get_min(l):
    ''' Function '''
    return min(l)

def get_sum(l):
    ''' Function '''
    return sum(int(i) for i in l)


#### Fonction principale


def main():
    ''' Function '''
    # pass
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))

    print(get_first(get_list_k(data, 37)))
    print(get_last(get_list_k(data, 37)))
    print(get_max(get_list_k(data, 37)))
    print(get_min(get_list_k(data, 37)))
    print(get_sum(get_list_k(data, 37)))

if __name__ == "__main__":
    main()
