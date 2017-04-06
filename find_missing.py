def find_missing(array1,array2):
    missingnumber = 0
    
    if len(array1) > len(array2):
        firstarray =  array1
        secondarray = array2
    elif len(array1) == len(array2):
        return missingnumber
    else:
        firstarray =  array2
        secondarray = array1
        
    
    for number in firstarray:
        if not number in secondarray:
            missingnumber = number

    return missingnumber

        
