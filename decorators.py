import functools

def my_decorator(functie):
	@functools.wraps(functie)
	def wrapper(*args, **kwargs):
		print 'Iniante de functie %s' % functie.func_name
		functie(*args, **kwargs)
		print 'Dupa functie %s' % functie.func_name
	
	return wrapper


def f():
	print 'Hello workd din f'
@my_decorator
def f1(a):
	print a
	raise Exception("my message")

#f1 = my_decorator(f1)
