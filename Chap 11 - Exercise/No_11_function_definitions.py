####### 11A_i: Addition of sparce vectors: (see alternative 1 in main exercise)
## Alternative 2:

##def sparse_add(vector1, vector2):
##    """ (dict of {int: int}, dict of {int: int}) -> dict of (int: int}
##
##    Return a dictionary representing the sum of sparse vectors vector1 and
##    vector2.
##
##    >>> sparse_add({0: 1, 6: 3}, {1: 2, 4: 5, 6: 9})
##    {0: 1, 1: 2, 4: 5, 6: 12}
##    >>> sparse_add({1: 3, 3: 4}, {2: 4, 3: 5, 5: 6})
##    {1: 3, 2: 4, 3: 9, 5: 6}
##    """
##
##    total_vector = {}
##
##    for vector in vector1, vector2:
##        for key, value in vector.items():
##            if key in total_vector:
##                total_vector[key] = total_vector[key] + value
##            else:
##                total_vector[key] = value
##    return total_vector

##NB: to add more than two sparse vectors define as following:
## def sparse_add(List_of_dict): # i.e put all the dictionaries in a list and loop
                               # over them.


## Alternative 3 (longer method): Addition of sparse vector:

##def sparse_add(vector1, vector2):
##
##    vector_all  = {}
##    vector_total = {}
##    for vector in vector1, vector2:
##        for key, value in vector.items():
##            if key in vector_all:
##                vector_all[key].append(value)
##            else:
##                vector_all[key] = [value]
##    
##
##    for index, num_list in vector_all.items():
##        sum_list = sum(num_list)
##        vector_total[index] = sum_list
##        
##    return vector_total
        


######## 11A_ii: (a): Addition of List of vectors
##vector1 = [1, 0, 0, 0, 0, 0, 3, 0, 0, 0]
##vector2 = [0, 2, 0, 0, 5, 0, 9, 0, 0, 0]
##
##total_vector = []
##
##for i in range(len(vector1)):
##    total_vector.append(vector1[i] + vector2[i])
##
##print (total_vector)

######### 11A_i: (b): Converting list to sparce vectors:
## 
##vector1 = [1, 0, 0, 0, 0, 0, 3, 0, 0, 0]
##
##index_to_num = {}
##for i in range(len(vector1)):
##    if vector1[i] != 0:
##        index_to_num.update({i:vector1[i]})
##print (index_to_num)

## Alternative: converting list to sparse vectors:

vector1 = [1, 0, 0, 0, 0, 0, 3, 0, 0, 0]

index_to_num = {}
for i in range(len(vector1)):
    if vector1[i] != 0:
        index_to_num[i] = vector1[i]

print (index_to_num)

                               
                               

######## 11B_i: dot_product of sparce_vectors. (see alternative 1 in main exercise)
##alternative 2: very long method)
##                               
##def sparse_dot(vector1, vector2):
##    
##    vector_all  = {}
##    vector_total = {}
##    for vector in vector1, vector2:
##        for key, value in vector.items():
##            if key in vector_all:
##                vector_all[key].append(value)
##            else:
##                vector_all[key] = [value]
##    
##    
##    addup_list = []
##    inner_product = 1
##    dot_product = 0 
##    for key, value_list in vector_all.items():
##        if len(value_list) > 1:
##            for v in value_list:
##                inner_product = inner_product * v
##            addup_list.append(inner_product)
##            inner_product = 1
##            dot_product = sum(addup_list)
##    return dot_product


## 11B_ii: dot_product with List

##vector1 = [1, 0, 0, 0, 0, 0, 3, 0, 0, 0]
##vector2 = [0, 2, 0, 0, 5, 0, 9, 0, 0, 0]

##vector1 = [1, 2, 3]
##vector2 = [4, 5, 6]
##
##dot_list = []
##
##for i in range(len(vector1)):
##    dot_list.append(vector1[i] * vector2[i])
##print (dot_list)
##
##dot_product = sum(dot_list)
##print (dot_product)

               
               
                               
                                 
               
    
        
        
    


    

            
            
    
