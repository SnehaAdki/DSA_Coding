import threading
import time

# Create a semaphore with 3 slots
semaphore = threading.Semaphore(3)

def task(thread_id):
    print(f"Thread {thread_id} is waiting to access the resource...")
    semaphore.acquire()  # Wait if necessary
    try:
        print(f"Thread {thread_id} has started accessing the resource.")
        time.sleep(2)  # Simulate some work
        print("Waiting..... ")
    finally:
        print(f"Thread {thread_id} is releasing the resource.")
        semaphore.release()  # Always release

threads = []
for i in range(6):  # More threads than slots
    t = threading.Thread(target=task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()