'''
Program-3:Find Last Element Of List Method-2
'''
numbers=(1,2,3,4,50)
#first calculate the length of list and subtract from 1 
length_of_list=len(numbers) #len() will return length of list which is 5
#we have to subtract it by 1 to find last element 5-1=4=numbers[length_of_list-1]=numbers[5-1]=numbers[4]=5
print(numbers[length_of_list-1])
