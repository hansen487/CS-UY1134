#Hansen Chen
#hc1941

#Problem C-4.9
def find_max_min(lst, end, maximum=0, minimum=0):
    if end<0:
        return (maximum, minimum)
    else:
        if lst[end]>maximum:
            maximum=lst[end]
        if end==len(lst)-1:
            minimum=lst[end]
        elif lst[end]<minimum:
            minimum=lst[end]
        return find_max_min(lst, end-1, maximum, minimum)

A=[212,22,43,90,55,99,34,23]
print find_max_min(A, len(A)-1)
'''if statements take constant time, and the function recurses N times. Therefore, the runtime is O(n).'''

#Problem C-4.10
#Set counter initially to zero. If the number is greater than 1, quotient divide the number by 2, and increase counter by 1.
# Call the function again, and return the counter when number becomes less than 1. 
'''since the problem runs number//2 times, the problem would have a runtime of O(logn)'''

#Problem C-4.11
#Initialize empty dictionary with the function. Start with the last element, and if it is not in the dictionary, add it to 
#the dictionary and call the function with the preceding element. If it is in the dictionary, return false.
'''Assuming the every single element is distinct, the function would recurse n number of times, making the runtime O(n)'''

#Problem C-4.15
def powerset(lst, counter=0, output=[[]]):
    if output==[[]]:
        counter=len(lst)-1
    if len(lst)==0 or counter<0:
        return output
    else:
        store=lst[counter]
        output.append([store])
        x=[[store]+output[i] for i in range (1, len(output)-1)]
        output+=x
        return powerset(lst, counter-1, output)

print powerset([1,2,3,4,5])
'''Even though the function recurses n times, the list comprehension runs length of output number of times during each recursion. If length of 
output=, then the runtime would equal O(m*n)'''

#Problem C-4.17
def palindrome(string, start=0, stop=0, ispal=True):
    if start==0:
        stop=len(string)-1
    if start<stop-1:
        if string[start]==string[stop]:
            return palindrome(string, start+1, stop-1, ispal)
        else:
            ispal=False
            return ispal
    else:
        return ispal
print palindrome('apples')
print palindrome('racecar')
'''since the function consists of if-else statements, the runtime of this program would be O(n), since the program runs for length of string/2 times.'''

#Problem C-4.20
#Start with the last value. If it is smaller than k, pop it out and insert it in the very beginning of the list. If it is k, do nothing.
#If it reaches k, if the number is greater than k pop and append to the end of the list. Recurse until you reach the first value.
'''since the function recurses through the entire list, the runtime would be O(n)'''
            
    