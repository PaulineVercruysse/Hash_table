def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable,key) #to know the bucket where to place the new keyword
    for entry in bucket:
        if entry[0] == key: #keyword already in the hashtable
            entry[1] = value #replace the value associated with the keyword
    bucket.append([key, value]) #keyword not present in the hash table
    return htable
