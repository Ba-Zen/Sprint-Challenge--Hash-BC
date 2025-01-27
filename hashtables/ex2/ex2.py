#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    #creates hashtable with key-source, value-destination
    for i in range(0, length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    #finds the starting destination to place at the start of route
    route[0] = (hash_table_retrieve(hashtable, "NONE"))

    # finds next destination for each previous source and appends to route
    for i in range(1, length):
        source = route[i-1]
        route[i] = hash_table_retrieve(hashtable, str(source))

    #print(route)
    return route
