#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    #sets up hashtable with weight as key and index of the value
    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)

    for i in range(0, length):
        #finds what the key weight would be for item i 
        key_weight = limit - weights[i]

        # if key weight exists
        if hash_table_retrieve(ht, key_weight):
            #if i is the greater value, returns it as the first item in tuple
            if i > hash_table_retrieve(ht, key_weight):
                return (i, hash_table_retrieve(ht, key_weight))
                #else if i is the lower value it returns as second item in tuple
            else: 
                return (hash_table_retrieve(ht, key_weight), i)
    # if key does not exist--return None
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
