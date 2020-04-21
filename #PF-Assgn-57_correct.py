'''
Created on 21-Apr-2020

@author: ila roy
'''
#PF-Assgn-57
def check_prime(number):
    factor=[]
    #remove pass and write your logic here. if the number is prime return true, else return false
    for i in range(2,number+1):
        if number%i==0 :
            factor.append(i)
    if len(factor)==1 and factor[0]==number:
        return True
    else:
        return False
    

def rotations(num):
    #remove pass and write your logic here. It should return the list of different combinations of digits of the given number.
    #Rotation should be done in clockwise direction. For example, if the given number is 197, the list returned should be [197, 971, 719]
    list1=[]
    list1.append(num)
    str_num=str(num)
    for i in range(0,len(str_num)-1):
        str_num=str_num[1:]+str_num[0]
        list1.append(int(str_num))
    return list1

def get_circular_prime_count(limit):
    count=0 
    flag=0 
    #remove pass and write your logic here.It should return the count of circular prime numbers below the given limit.
    for i in range(2,limit):
        if len(str(i))==1:
            if check_prime(i):
                count+=1 
        elif len(str(i))==2:
            if check_prime(i):
                rev_str1=str(i)[::-1]
                if check_prime(int(rev_str1)):
                    count+=1
                    rev_str1=""
        else:
            x=rotations(i)
            for i in x:
                if check_prime(i):
                    flag=1  
                else:
                    flag=0 
                    break
            if flag==1:
                count+=1 
    return count 
        

#Provide different values for limit and test your program

print(get_circular_prime_count(500))
