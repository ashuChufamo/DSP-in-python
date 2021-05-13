from threading import Thread, Lock, current_thread, Semaphore, BoundedSemaphore
from time import sleep
from queue import Queue
# balance = 200

# def withdraw(amount: int, lock:Lock):
#     lock.acquire()
#     global balance
#     balance-=amount
#     # lock.release()
#     print(balance)
    

# def print_hello(name, other, index):
#     print("Running in ",current_thread().name)
#     sleep(1)
#     # print('Hello world', name, other, index)

# thread_names= []
# def requestHandler(l: Lock, s: Semaphore):
#     s.acquire()
#     name = current_thread().name
    
#     l.acquire()
#     thread_names.append(name)#has to be locked 
#     l.release()
    
#     # Process some stuff
#     sleep(0.5)
    
#     l.acquire()
#     thread_names.remove(name)
#     print(current_thread().name)
#     l.release()
    
#     s.release()

# lock = Lock()
# s = Semaphore(10)
# threads = []
# # for amount in [30, 50, 60]:

# def run_first(s: Semaphore):
#     print("running run_first")
#     s.release
    
# def run_second(s: Semaphore):
#     s.acquire
#     print("running run_second")
    
def producer(queue : Queue):
    for i in range(100):
        queue.put(i)

def consumer(queue : Queue):
    while True:
        next_item= queue.get()
        if (next)_item == "QUIT"):
            print("Quitting")
            break 
        print("Processing ", next_item, "result ", next_item*next_item)
        print("Processed by", current_thread().name)
        
q= Queue()
for i in range(100):
    Thread(target=consumer, args=[q]).start()
    
producers= []
for i in range(2):
    thread = Thread(target=consumer, args=[q])
    thread.start()
    producers.append(thread)
    
for producer in producers:
    producer.join()

for i in range:
    q.put("QUIT")
# Thread(target=run_second,args=[s]).start()
# Thread(target=run_second,args=[s]).start()


# for amount in range(100):
#     # thread = Thread(target=print_hello, args=['mister', 'another' ,i ], name=f"my thread-{i}.")#String interpolation
#     # thread = Thread(target=withdraw, args=[amount,lock])
#     thread = Thread(target=requestHandler, args=[lock, s])
#     thread.start()
#     #threads.append(thread)

# for thread in threads:
#     thread.join()
    
# # print("In the main thread")
# #print('Final balance', balance)