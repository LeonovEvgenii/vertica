from tkinter import Tk
from tkinter import Label, Listbox, SINGLE, EXTENDED, END, ACTIVE, Frame, Button, Entry, Text
from tkinter import Toplevel

class Draw_interface(Tk):
	def __init__(self, obj):
		super(Draw_interface, self).__init__()
		self.title("Поставка")
		
		self.frame_fill = Frame(self)

		self.frame_warehouse = Frame(self.frame_fill)
		self.lebel_warehouse = Label(self.frame_warehouse, text = "Список складов")
		self.list_warehouse = Listbox(self.frame_warehouse, selectmode=SINGLE)
		
		self.frame_producer = Frame(self.frame_fill)
		self.lebel_producer = Label(self.frame_producer, text = "Список поставщиков")
		self.list_producer = Listbox(self.frame_producer, selectmode=SINGLE)
		
		self.frame_article = Frame(self.frame_fill)
		self.lebel_article = Label(self.frame_article, text = "Список товаров")
		self.list_article = Listbox(self.frame_article, selectmode=EXTENDED)	
		self.add_article = Button(self.frame_article, text = "Добавить товар")
		self.label_count_article = Label(self.frame_article, text = "Ввод количества")
		self.delete_article = Button(self.frame_article, text = "Удалить товар", width=12)
		self.count_article = Entry(self.frame_article, width=15)

		self.frame_preview = Frame(self)
		self.label_prview = Label(self.frame_preview, text = "Предпросмотр")
		self.text_preview = Text(self.frame_preview, width=88)
		self.buttom_preview = Button(self.frame_preview, text = "Создать документ")
		
		self.frame_text_head = Frame(self.text_preview)

		self.text_preview.window_create(END, window = self.frame_text_head)

		self.label_text_time = Label(self.frame_text_head)
		self.label_text_warehouse = Label(self.frame_text_head)
		self.label_text_producer = Label(self.frame_text_head)
		self.label_text_id = Label(self.frame_text_head)

		

		self.columns = []
		self.tabel = []
		self.row = 5

		self.label_column_number = Label(self.frame_text_head, text = "№ позиции")
		self.label_column_article = Label(self.frame_text_head, text = "SKU")
		self.label_column_count = Label(self.frame_text_head, text = "Количество")
		self.label_column_price = Label(self.frame_text_head, text = "Цена за еденицу")
		self.label_column_summ = Label(self.frame_text_head, text = "Сумма")


		self.place()

		self.get_content()

	def place(self):
		self.frame_fill.pack()

		self.frame_warehouse.pack(side = 'left')
		self.lebel_warehouse.pack()
		self.list_warehouse.pack()

		self.frame_producer.pack(side = 'left')
		self.lebel_producer.pack()
		self.list_producer.pack()

		self.frame_article.pack(side = 'left')
		self.lebel_article.pack()
		self.list_article.pack(side = 'left')
		self.add_article.pack()
		self.label_count_article.pack()
		self.count_article.pack()
		self.delete_article.pack()

		self.frame_preview.pack(side = 'bottom')
		self.label_prview.pack()
		self.text_preview.pack()
		self.buttom_preview.pack()

		self.label_text_time.grid(row = 0, column = 0)
		self.label_text_warehouse.grid(row = 1, column = 0)
		self.label_text_producer.grid(row = 2, column = 0)
		self.label_text_id.grid(row = 3, column = 0)

		self.label_column_number.grid(row = 4, column = 0)
		self.label_column_article.grid(row = 4, column = 1)
		self.label_column_count.grid(row = 4, column = 2)
		self.label_column_price.grid(row = 4, column = 3)
		self.label_column_summ.grid(row = 4, column = 4)

	def get_content(self):
		rez = obj.get_list_warehouse()
		for i in rez:
			self.list_warehouse.insert(END, i)
		
		rez = obj.get_list_producer()
		for i in rez:
			self.list_producer.insert(END, i)

		rez = obj.get_list_article()
		for i in rez:
			self.list_article.insert(END, i)

		import datetime
		time = datetime.datetime.now()
		time_str = "%s : %s : %s" % (time.day, time.month, time.year)
		#self.label_text_time.configuge("time_str") # ??????????????
		self.label_text_time['text'] = time_str
		id = str(obj.get_max_id_for_delivery())
		if len(id)<6:
			i = 6 - len(id)
			while i:
				id = '0' + id
				i -= 1
		self.label_text_id['text'] = id




def loop_event(root, obj):
	root.list_warehouse.bind('<Double-Button-1>', add_warehouse)
	root.list_producer.bind('<Double-Button-1>', add_producer)
	#root.buttom_preview.bind('<Button-1>', create_document)
	root.bind('<Escape>', ex)
	root.add_article.bind('<Button-1>', add_to_table)
	root.delete_article.bind('<Button-1>', delete_to_table)
	root.mainloop()


def add_warehouse(event):
	index = root.list_warehouse.curselection()[0]
	index += 1
	warehouse_str = obj.select_warehouse(index)
	root.label_text_warehouse['text'] = warehouse_str

def add_producer(event):
	index = root.list_producer.curselection()[0]
	index += 1
	producer_str = obj.select_producer(index)
	root.label_text_producer['text'] = producer_str

def add_to_table(event):
	index = root.list_article.curselection()
	value = root.count_article.get()
	#print(dir(root.count_article))
	if index == ():
		win = Toplevel()
		Label(win, text = "Товар не выбран").pack()
		Button(win , text = "ОК", command = win.destroy).pack()
	else:
		index = index[0]

	



	#_text = str(root.row - 4)
	#root.columns.append(Label(root.frame_text_head, text = _text))


	# i = 0
	# while i<5:
	# 	_text = "  стр %s, кол %s  " % (root.row, i)
	# 	root.columns.append(Label(root.frame_text_head, text = _text))
	# 	root.columns[-1].grid(row = root.row, column = i)
	# 	i += 1
	# root.row += 1

def delete_to_table(event):
	pass

def create_document(event):
	print(root.text_preview.get('1.0', END))

def ex(event):	
	root.destroy()
	# import sys #?????
	# sys.exit()


if __name__ == '__main__':
	from db_connection import DB_connector
	obj = DB_connector()
	root = Draw_interface(obj)
	loop_event(root, obj)
	