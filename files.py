import contextlib

@contextlib.contextmanager
def myopen(*args, **kwargs):
	fd = None
	try:
		fd = open(*args, **kwargs)
		yield fd
	except Exception as exe:
		print "Got exception %s" % exe
	finally:
		if fd:
			fd.close()


with myopen('myfile.txt', 'w') as fd:
	fd.write('test')
		
