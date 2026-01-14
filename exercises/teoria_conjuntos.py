def combine_set_unique_elements(first_set, second_set):
    return set(first_set + second_set)

def set_difference(first_set, second_set):
    # A - B = {x | x in A and x not in B}
    set_unique = combine_set_unique_elements(first_set, second_set)
    difference = [i for i in set_unique if i in first_set and i not in second_set]
    return difference

def intersection_sets(first_set, second_set):
    # A and B = {x | x in A and x in B}
    set_unique = combine_set_unique_elements(first_set, second_set)
    intersection = [i for i in set_unique if i in first_set and i in second_set]
    return intersection

def union_sets(first_set, second_set):
    # A or B = {x | x in A or x in B}
    set_unique = list(combine_set_unique_elements(first_set, second_set))
    return set_unique

def main():
    A = [i for i in range(10)]
    B = [i for i in range(0, 10, 2)]

    difference = set_difference(A, B)
    intersection = intersection_sets(A, B)
    union = union_sets(A, B)

    print(f'El conjunto A es {A} y el conjunto B es {B}.')
    print(f'La diferencia de A y B es {difference}.')
    print(f'La intersección de A y B es {intersection}.')
    print(f'La unión de A y B es {union}.')

if __name__ == '__main__':
    main()
