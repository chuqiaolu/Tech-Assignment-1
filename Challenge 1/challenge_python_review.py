import math
def print_squares():
    '''
    this is to print the square of each number
    '''
    int=[1,2,3,4,5,6,7,8,9,10]
    print([x**2 for x in int])
    return

def average(list):
    '''
    because this function want us to check is the correct type is passed, I add
    several if else statement to test its type before calculating average
    '''
    sum=0
    for terms in list:
        if isinstance(terms,int)or isinstance(terms,float):
            continue
        else:
            return
    for terms in list:
        sum=sum+terms  
    if len(list)==0:
        return 0
    else:
        return sum/(len(list))     

def is_prime(aint):
    '''
    for this is prime function, I just barely check if it% 2 to itself-1 is 0,
    if so return true
    '''
    for num in range(2,aint-1):
        div=aint%num
        if div==0:
            return False
    return True

def prime_100():
    '''
    for this function, I just call is prime 100 times to ints from 1 to 100 separately
    '''
    alist=[]
    print(alist)
    for num in range(1,100):
        if is_prime(num):
            alist.append(num)
    print(alist)
    return alist

def count_letters(astring):
    '''
    I define a way to check if aletter is punctuation or blank space. If so, continue
    to next loop. if not, add it to the dictionnary 
    '''
    adict={}
    for aletter in astring:
        if aletter ==' 'or aletter =='.'or aletter =='!':
            continue
        if aletter in adict:
            adict[aletter.lower()] += 1
        else:
            adict[aletter.lower()] = 1
    return adict

def filter_strings(alist):
    '''
    in this function, we should develop an algorithm to filter different strings,
    in my case, I will first filter out the string with less than 5 chars. Then check
    if they have aeiou, if so, append it to the result and break to check next string
    '''
    result=[]
    for astring in alist:
        if len(astring)>=5:
            for aletter in astring:
                if aletter=='a'or aletter=='e'or aletter=='i'or aletter=='o'or aletter=='u':
                    result.append(astring)
                    break
    return result

def is_palindrome(number):
    '''
    in this question, I just simply first convert the number into string and 
    flip the string and test if it is equal to the original one
    '''
    if str(number)==str(number)[::-1]:
        return True
    else:
        return False

if __name__ == '__main__':  
    print(count_letters("The quick brown fox jumps over the lazy dog."))
    print(count_letters("Web serving with FastAPI!"))
    print(filter_strings({"jjjjj","adwddaw","uiqwdhiuqwhbd","wud","hello, ece140A"}))
    print(filter_strings({"ok","adwddallllw"}))
    print(filter_strings({"ok","aeio"}))
    print(filter_strings({"nope!","adwiiii999"}))
    print(is_palindrome(1234567.7654321))
    print(is_palindrome(-0.123))





    
 
    


