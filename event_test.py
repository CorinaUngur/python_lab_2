import multiprocessing

myqueue = multiprocessing.Queue()


def count():
	for i in xrange(10):
		myqueue.put(i)

workers = []

for i in xrange(3):
	worker = multiprocessing.Process(target = count)
	#worker.setDaemon(True)
	worker.start()
	workers.append(worker)

for w in workers:
		w.join()

while not myqueue.empty():
	print myqueue.get()
