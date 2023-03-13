sample_list=[1, 2, 3, 4, 5, 6, 7]

def triple(x):
    return x*3

result=map(triple,sample_list)

print(list(result))
    

## output : [3, 6, 9, 12, 15, 18, 21]    
