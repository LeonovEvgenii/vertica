from tkinter import *
import datetime
from random import randint

class Tk_test(Tk):
	def __init__(self):
		super(Tk_test, self).__init__()		
		self.title("Выгрузка со склада")
		
		#self.table = []

		# self.listbox1=Listbox(height=5,width=15,selectmode=SINGLE)
		# list1=[u"Москва",u"Санкт-Петербург",u"Саратов",u"Омск"]
		# for i in list1:
		# 	self.listbox1.insert(END,i)
		# self.listbox1.pack()
		#self.button=Button(self,text='ok')
		#self.button.pack()

		self.lebel_warehouse = Label(self, text = "Список складов")
		self.list_warehouse = Listbox(self, selectmode=SINGLE)
		self.predpros_label = Label(self, text = "Предпросмотр")
		self.predpros_text = Text(self)
		self.lebel_warehouse.pack()
		self.list_warehouse.pack()
		self.predpros_label.pack()
		self.predpros_text.pack()
		self.after_idle(self.head)
		#Button(self, text='ok', command = self.fill).pack()

	def head(self):
		time = datetime.datetime.now()
		self.predpros_text.insert(0.0, "%s : %s : %s" % (time.day, time.month, time.year))

	def load_data():
		pass

	# def fill(self):
	# 	while self.table:
	# 		self.table[0].pack_forget()
	# 		del(self.table[0])

	# 	for i in range(randint(0,100)):
	# 		self.table += [Label(self, text = 'label %s' % randint(0,100))]
	# 		self.table[-1].pack()




if __name__ == '__main__':
	obj = Tk_test()
	obj.mainloop()
