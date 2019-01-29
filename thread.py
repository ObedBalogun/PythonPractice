import threading
from queue import Queue
import time

print_lock = threading.Lock() #Lock applied to any print function
#This is the job to be done
def exampleJob(worker):
    time.sleep(0.5)
    with print_lock: #the next line executes only while there is a lock on current thread
        print(threading.current_thread().name, worker)
#core function
#this is what threads and actually runs the job with threads
def threader():
    while True:
        worker = q.get()
        exampleJob(worker)
        q.task_done() #releases thread back to queue

q= Queue()
start_time = time.time()
#creating threads
for x in range(10):
    t = threading.Thread(target = threader) #defines target for each thread
    t.daemon = True #Dies when the main thread dies
    t.start()

#jobs
for worker in range(20): #each thread does two jobs
    q.put(worker)
q.join()

print('Entire job took:', time.time() -start_time)



'''Basically this thread does 20 jobs with 10 threads '''




