Do your own Hash Table, principle of a python dictionary
===================


----------
A **hash table** is the principle used for **Python dictionary**. Through the online class of Udacity "[Intro to computer science](https://www.udacity.com/course/intro-to-computer-science--cs101)", you learn how to built your own hash table to understand the principle of Python dictionary. 

### Principles
The hash tables will **map a keyword to a value**. This value will give us the **position where to find faster this keyword into a database** without having to scan all the keywords of the database. A **hash table** can be compared to a **index in a library: the keyword is a book and the value is the number of the shelf**. By knowing the value, we could find faster the place of the book into the library without having to check all the shelfs. For the programmation **the shelf will be called a bucket, containing one or several keyword(s)**. 

In a python dictionary, the number a bucket is predefined. However in this programation we will define the number of bucket.  

----------

Code
-------------

#### **FIRST**: set up an empty hash table
In order to place the keyword in the buckets of the hash table, we need to set up a set of empty buckets by the procedure: `make_hash_table`
There will be the number of buckets desired as input. The output will be an empty hash table, called table, with the corresponding number of buckets. Each bucket is a list.

We use the built-in Python function `range(start_number, end_number)`
```
range(0, nbuckets):
```
This function takes two numbers as input and as output gives a list of numbers from start_number to (end_number)-1 by increasing everytime of 1.
Example:
```
range(0, 5):
```
returns
```
[0, 1, 2, 3, 4]
```
#### **SECOND**: obtaining the bucket of a keyword 

The procedure is taking 2 inputs: a hash table and a keyword and will return as output the value of the bucket where the keyword could occur. 
This procedure is split in 2 small procedures: `hash_string` and `hashtable_get_bucket` pooled togteher in the file hashtable_get_bucket.py .

##### `hash_string`
The procedure of `hash_string` is to calculate the value (`h`) that will correspond to the bucket of a keyword given as input. There is also the size of the hash table (number of buckets = `buckets`) as input.

In hash table in general, the keywords have to be spread evenly through the index. 
In our case to calculate the value of h, we use the buildin Python operations: `ord` and `%`.

`ord`: a one letter string turns into a number.

`%`: modulus, returns the modulus of a division.

 We first calculate the sum of `ord` of the whole keyword and we take the modulus (`%`) of the division of this sum by the number of bucket to get the value h.
 
##### `hashtable_get_bucket`
This procedure will take as input an hash table (`htable`) and a `keyword`. This will return the bucket (a list) where the keyword will be located. The returned bucket (list) could be empty or with other words depending of the input hash table.  

#### **THIRD**: adding a new keyword to the hash table
 
The procedure `hashtable_add` allows to add a new keyword into its corresponding bucket into a given hash table. 

There are 3 inputs: a hash table `htable`, a new keyword `key`, a number associated with the keyword `value`(value not having link with h). This procedure will return the new hash table `htable`.

#### **FOURTH**: being able to check if the keyword is already in the hash table

The procedure `hashtable_lookup` is taking as input a hash table `htable`and a keyword `key` to check if the keyword is in the hash table. 

If the keyword is present, the procedure will return the value associated with the keyword (`value` from previously). If the keyword is not in the hash table, `None` will be returned.

#### **FIVE**: update the value associated with the keyword

The procedure `hashtable_update` is used if the user wants to change the value (`value`) associated with the keyword. The procedure has as input a hash table `htable`, the keyword to change the value `key` and the new value to associate `value`. 

First it calculates the number of the `bucket` corresponding to the keyword. Then, it checks in this bucket if the keyword is present. If it is the case, the value associated with the keyword is changed. Finally, if the keyword `key` is not present, the keyword is added with its value.




