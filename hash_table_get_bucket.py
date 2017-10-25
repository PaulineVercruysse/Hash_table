#part1#

def hash_string(keyword,buckets):
    h = 0 
    for c in keyword: #for all the characters of the string
        h = (h + ord(c) ) % buckets 
    return h 

#part 2#

def hashtable_get_bucket(htable,keyword):
    return htable[hash_string(keyword,len(htable))] 
#return the list in the htable corresponding to the h value of the keyword obtained by hash_string
