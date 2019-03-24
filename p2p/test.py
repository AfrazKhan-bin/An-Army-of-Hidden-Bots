intThreads = 2
arrJobs = [1, 2]
queue = Queue()

def create_threads():
    for _ in range(intThreads):
        objThread = threading.Thread(target=work)
        objThread.daemon = True
        objThread.start()
    queue.join()


def work():  # do jobs in the queue
    while True:
        intValue = queue.get()
        if intValue == 1:
            create_socket()
            socket_bind()
            socket_accept()
        elif intValue == 2:
            while True:
                time.sleep(0.2)
                
        queue.task_done()
        queue.task_done()
        sys.exit(0)


def create_jobs():
    for intThread in arrJobs:
        queue.put(intThread)  # put thread id into list
#     queue.join()

# import time
# starttime=time.time()
# while True:
# 	print ("tick")
#   	time.sleep(60.0 - ((time.time() - starttime) % 60.0))