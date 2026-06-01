# 1116. Print Zero Even Odd
# Medium
# Topics
# premium lock icon
# Companies
# You have a function printNumber that can be called with an integer parameter and prints it to the console.

# For example, calling printNumber(7) prints 7 to the console.
# You are given an instance of the class ZeroEvenOdd that has three functions: zero, even, and odd. The same instance of ZeroEvenOdd will be passed to three different threads:

# Thread A: calls zero() that should only output 0's.
# Thread B: calls even() that should only output even numbers.
# Thread C: calls odd() that should only output odd numbers.
# Modify the given class to output the series "010203040506..." where the length of the series must be 2n.

# Implement the ZeroEvenOdd class:

# ZeroEvenOdd(int n) Initializes the object with the number n that represents the numbers that should be printed.
# void zero(printNumber) Calls printNumber to output one zero.
# void even(printNumber) Calls printNumber to output one even number.
# void odd(printNumber) Calls printNumber to output one odd number.
 

# Example 1:

# Input: n = 2
# Output: "0102"
# Explanation: There are three threads being fired asynchronously.
# One of them calls zero(), the other calls even(), and the last one calls odd().
# "0102" is the correct output.
# Example 2:

# Input: n = 5
# Output: "0102030405"


from typing import Callable
import threading


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_sem = threading.Semaphore(1) #unlocked released
        self.even_sem = threading.Semaphore(0)
        self.odd_sem = threading.Semaphore(0)
        
        
	# printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.zero_sem.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.even_sem.release()
            else:
                self.odd_sem.release()
        
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2,self.n+1,2):
            self.even_sem.acquire()
            printNumber(i)
            self.zero_sem.release()
        
        
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n+1,2):
            print("In.. odd")
            self.odd_sem.acquire()
            print("Acquired")
            printNumber(i)
            print("release zero" )
            self.zero_sem.release()
        
        
zeo = ZeroEvenOdd(5)
t1 = threading.Thread(target=zeo.zero, args=[lambda x: print(x, end="")])
t2 = threading.Thread(target=zeo.even, args=[lambda x: print(x, end="")])
t3 = threading.Thread(target=zeo.odd,  args=[lambda x: print(x, end="")])
t1.start(); t2.start(); t3.start()
t1.join();  t2.join();  t3.join()