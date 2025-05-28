# FizzBuzz: Print numbers 1-100, replace multiples of 3 with "Fizz", 5 with "Buzz", both with "FizzBuzz".

# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz", i)
#     elif i%3==0:
#         print("Fizz",i)
#     elif i%5==0:
#         print("Buzz",i)
        
# Reverse a String: Without using built-in methods.


# word="shiva"
# rev_word=""
# for i in word:
#     rev_word=i+rev_word
# print(rev_word)
    


# Palindrome Check: Determine if a string is a palindrome.

# def isPalindrome(word1):

#     return word1==word1[::-1]


# word="manam"
# isPaly=""
# for i in word:
#     isPaly=i+isPaly 
# print(isPaly==word)


# Factorial: Compute factorial of a number (recursive/iterative).
# fact=1
# for i in range(1,6):
#     fact*=i
# print(fact)
    


# Sum of Array: Find the sum of all elements in an array.

# arry=[1,2,3,4,5,6,7]
# print(sum(arry))


# Find Max/Min in Array: Without using Math.max/Math.min.

# arry=[1,3,7,8,11,2,3,4,5,6,7] 
# print(max(arry))
# print(min(arry))

# isMaxNum=0

# for i in arry:
    
#     if isMaxNum<i:
#         isMaxNum=i
# print(isMaxNum)



# Fibonacci Series: Generate the first n Fibonacci numbers.

n=10
a,b=[0,1]
for i in range(n):
    a, b=b, a+b
    print(a)

# Prime Number Check: Determine if a number is prime.

for i in range(2,35):
    isPrime=True
    
    for j in range(2,i):
        if i%j==0:
            isPrime=False
            break
    if isPrime:
        print(i)
    
  
            
        

    

# Remove Duplicates: From an array without Set.

# Capitalize First Letter: Of each word in a sentence.