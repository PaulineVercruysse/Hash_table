def hashtable_add(htable,key,value):
    bucket = hashtable_get_bucket(htable,key) 
    #get the position (h) where to add the new keyword
    bucket.append([key,value]) 
    #add the keyword and an associated value (value other than h) in the corresponding bucket
    return htable  