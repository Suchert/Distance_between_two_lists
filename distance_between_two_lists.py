import random

'''
Function take two lists filled with numberical data to calculate minimal distance between them,
where distance is defined as abs(list_A[i] - list_B[j])
'''
def distance_between_two_lists(list_A,list_B):
    #using set to check if list contains same elements (distance between lists = 0 then)
    sameElements = [element for element in list_A if element in set(list_B)]
    
    if sameElements:
        result = 0
        print(f"Distance between lists is equal to {result}")
        return result
    
    #checking if any list is empty
    elif not list_A or not list_B:
        return ("One of lists is empty")
    
    else:
        #creating iterators: "i" for list_A and "j" for list_B
        i = 0
        j = 0
        
        #sorting lists
        list_A.sort() 
        list_B.sort() 
        
        #checking length of input lists
        lenList_A = len(list_A) 
        lenList_B = len(list_B)
        
        #setting up result variable
        result = abs(list_A[i] - list_B[j])
    
    #iterating thru all elements of both lists
    while (i < lenList_A and j < lenList_B): 
        
        #updating "result" variable
        if (abs(list_A[i] - list_B[j]) < result): 
            result = abs(list_A[i] -list_B[j]) 
            
        #iterating stepwise thru all elements list_A  
        if (list_A[i] < list_B[j]): 
            i += 1
        
        #iterating stepwise thru all elements list_B  
        else: 
            j += 1
    
    #et voila
    print(f"Distance between lists is equal to {result}")
    
    return result  



'''
Fuction creates list_A and list_B within prescribed boundaries:
start_list_A, end_list_A, start_list_B, end_list_B and with numer of elements = listLen.
Returns lists: list_A and list_B
'''
def randomListCreator(listLen = 1000,
                      start_list_A= -10000, 
                      end_list_A = 0, 
                      start_list_B = -10,
                      end_list_B = 5000):
    
    #create empty lists
    list_A = []
    list_B = []
    
    #iterating thru prescribed list lenght
    for i in range(listLen):
        
        n = random.randint(start_list_A,end_list_A)
        m = random.randint(start_list_B,end_list_B)
        list_A.append(n)
        list_B.append(m)
    
    #prints shape of lists
    print(f"Random list_A with length {listLen} and range [{start_list_A},{end_list_A}] has been created ")
    print(f"Random list_B with length {listLen} and range [{start_list_B},{end_list_B}] has been created ")
    #returns input for distance_between_two_lists
    return list_A, list_B


#Lists creation
list_A, list_B = randomListCreator()

#checking if fuction works, printing the result
result = distance_between_two_lists(list_A,list_B)
