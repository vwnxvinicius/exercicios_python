def main():
    seq1 = [54, 2, 11, 4, 17, 21, 1]
    print(seq1)
    insertion(seq1)
    print(seq1)
    if seq1.sort() == True:
        print("É crescente")
    else:
        print("Não é crescente")

def insertion(seq):
    for i in range(1, len(seq)):
        value_to_sort = seq[i]
        while seq[i - 1] > value_to_sort and i > 0:
            seq[i], seq[i - 1] = seq[i - 1], seq[i]
            i = i - 1


main()