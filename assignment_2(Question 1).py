

def last(n):
    return n[-1] 
  
def sort(tuples):
    return sorted(tuples, key=last)
  
input_lst = eval(input("Enter the List : "))

print("Sorted List : ",sort(input_lst))