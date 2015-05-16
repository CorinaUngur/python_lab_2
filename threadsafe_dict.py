import threading

def apply_lock(func):
	def wrapper(inst, *args, **kwargs):
		with inst._lock:
			return func(*args, **kwargs)
	return wrapper	

class threadsafeDict(dict):
	_lock = threading.Lock()
	@apply_lock
	def __get_item__(self, key):
		return super(threadsafeDict, self).__getitem__(key)
	@apply_lock
	def __set_item__(self, key, val):
		return super(threadsafeDict, self).__setitem__(key, val)

#with open('nume_fisier', 'w') as f:
#	f.write('tes')


mydict = threadsafeDict()
mydict['test'] = 10
print mydict['test']

