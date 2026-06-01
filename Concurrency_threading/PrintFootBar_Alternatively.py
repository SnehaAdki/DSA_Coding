# 1115. Print FooBar Alternately
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Suppose you are given the following code:

# class FooBar {
#   public void foo() {
#     for (int i = 0; i < n; i++) {
#       print("foo");
#     }
#   }

#   public void bar() {
#     for (int i = 0; i < n; i++) {
#       print("bar");
#     }
#   }
# }
# The same instance of FooBar will be passed to two different threads:

# thread A will call foo(), while
# thread B will call bar().
# Modify the given program to output "foobar" n times.

 

# Example 1:

# Input: n = 1
# Output: "foobar"
# Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar().
# "foobar" is being output 1 time.
# Example 2:

# Input: n = 2
# Output: "foobarfoobar"
# Explanation: "foobar" is being output 2 times.
 


from typing import Callable
import threading


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_sem = threading.Semaphore(1)
        self.bar_sem = threading.Semaphore(0)


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.foo_sem.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_sem.release()
        


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.bar_sem.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_sem.release()


fb = FooBar(3)
t1 = threading.Thread(target=fb.foo, args=[lambda: print("foo", end="")])
t2 = threading.Thread(target=fb.bar, args=[lambda: print("bar", end="")])
t1.start(); t2.start()
t1.join();  t2.join()