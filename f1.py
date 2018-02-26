
def main(foo):
	bar = foo
	bar()

if __name__ == '__main__':
	def bar():
		print(1111)

	main(bar)