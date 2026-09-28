words=["apple","banana","berry","apricot","pear","peach"]

result={}

for word in words:
    first_letter = word[0]
    
    if first_letter not in result:
        
        result[first_letter] =[]
    
    result[first_letter].append(word)


print(result)



#smallest value without using sorting and with duplicates

arr=[3,5,4,5,32,2,78,32,89,76,23,34,78,34]

k=int(input('Enter k:'))


#remove duplicates
distinct=list(set(arr))

#findk smallest
for i in range(k):
    smallest=min(distinct)
    distinct.remove(smallest)

print("the", k, "Smallest value is:", smallest)