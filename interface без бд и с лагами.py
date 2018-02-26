from tkinter import Tk
from tkinter import Label, Listbox, SINGLE, EXTENDED, END, ACTIVE, Frame, Button, Entry, Text
from tkinter import Toplevel, Canvas, Scrollbar
import rows_table

class Draw_interface(Tk):
	def __init__(self, obj):
		super(Draw_interface, self).__init__()
		self.obj = obj

		

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
		self.list_article = Listbox(self.frame_article, selectmode=SINGLE)	
		self.add_article = Button(self.frame_article, text = "Добавить товар")
		self.label_count_article = Label(self.frame_article, text = "Ввод количества")
		self.delete_article = Button(self.frame_article, text = "Удалить товар", width=12)
		self.count_article = Entry(self.frame_article, width=15)

		self.frame_preview = Frame(self)
		self.label_prview = Label(self.frame_preview, text = "Предпросмотр")
		self.frame_canvas_scroll = Frame(self.frame_preview)
		self.canvas = Canvas(self.frame_canvas_scroll, background="#ffffff", width=600)
		self.vsb = Scrollbar(self.frame_canvas_scroll, orient="vertical", command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.vsb.set)
		self.frame_content = Frame(self.canvas)
		
		self.buttom_preview = Button(self.frame_preview, text = "Создать документ")
		
		self.label_text_time = Label(self.frame_content)
		self.label_text_warehouse = Label(self.frame_content)
		self.label_text_producer = Label(self.frame_content)
		self.label_text_id = Label(self.frame_content)
		
		self.table = []
		self.row = 5

		self.label_column_number = Label(self.frame_content, text = "№ позиции")
		self.label_column_article = Label(self.frame_content, text = "SKU")
		self.label_column_count = Label(self.frame_content, text = "Количество")
		self.label_column_price = Label(self.frame_content, text = "Цена за еденицу")
		self.label_column_summ = Label(self.frame_content, text = "Сумма")

		self.place()

		self.get_content()

		self.loop_event()

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

		self.frame_preview.pack()
		self.label_prview.pack()
		self.frame_canvas_scroll.pack()
		self.canvas.pack(side = 'left')
		self.frame_content.pack()
		self.vsb.pack(side="left", fill="y")
		self.canvas.create_window((4,4),window=self.frame_content, anchor="nw")
		self.buttom_preview.pack(side="bottom")

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
		rez = self.obj.get_list_warehouse()
		for i in rez:
			self.list_warehouse.insert(END, i)
		
		rez = self.obj.get_list_producer()
		for i in rez:
			self.list_producer.insert(END, i)

		rez = self.obj.get_list_article()
		for i in rez:
			self.list_article.insert(END, i)

		import datetime
		time = datetime.datetime.now()
		time_str = "%s : %s : %s" % (time.day, time.month, time.year)
		#self.label_text_time.configuge("time_str") # ??????????????
		self.label_text_time['text'] = time_str
		id = str(self.obj.get_max_id_for_delivery())
		if len(id)<6:
			i = 6 - len(id)
			while i:
				id = '0' + id
				i -= 1
		self.label_text_id['text'] = id

	def loop_event(self):
		self.list_warehouse.bind('<Double-Button-1>', self.add_warehouse)
		self.list_producer.bind('<Double-Button-1>', self.add_producer)
		self.buttom_preview.bind('<Button-1>', self.create_document)
		self.bind('<Escape>', self.ex)
		self.add_article.bind('<Button-1>', self.add_to_table)
		self.delete_article.bind('<Button-1>', self.delete_to_table)

	def add_warehouse(self, event):
		index = self.list_warehouse.curselection()[0]
		index += 1
		warehouse_str = self.obj.select_warehouse(index)
		self.label_text_warehouse['text'] = warehouse_str

	def add_producer(self, event):
		index = self.list_producer.curselection()[0]
		index += 1
		producer_str = self.obj.select_producer(index)
		self.label_text_producer['text'] = producer_str

	def add_to_table(self, event):
		index = self.list_article.curselection()
		value = self.count_article.get()
		if index == ():
			win = Toplevel()
			Label(win, text = "Товар не выбран").pack()
			Button(win , text = "ОК", command = win.destroy).pack()
			return None
		else:
			index = index[0] + 1

		k = 0 + 1
		count = len(self.table)		
		while k < count:
			if self.table[k]['text'] == self.obj.select_article(index):
				win = Toplevel()
				Label(win, text = "Товар уже есть в списке").pack()
				Button(win , text = "ОК", command = win.destroy).pack()
				return None
			k += 5

		if value == "":
			win = Toplevel()
			Label(win, text = "Колличество не введено").pack()
			Button(win , text = "ОК", command = win.destroy).pack()
			return None
		
		_text = str(self.row - 4)
		self.table.append(Label(self.frame_content, text = _text))

		_text = self.obj.select_article(index)
		self.table.append(Label(self.frame_content, text = _text))

		_text = int(value)
		self.table.append(Label(self.frame_content, text = _text))
		
		_text = self.obj.get_price_for_article(index)
		self.table.append(Label(self.frame_content, text = _text))

		_text = int(float(_text)) * int(value)
		self.table.append(Label(self.frame_content, text = _text))

		j = (self.row - 4) * 5
		k = j - 5
		i = 0

		while k < j:

			self.table[k].grid(row = self.row, column = i)
			k += 1
			i += 1

		self.row += 1				

	def delete_to_table(self, event):
		index = self.list_article.curselection()
		value = self.count_article.get()
		if index == ():
			win = Toplevel()
			Label(win, text = "Товар не выбран").pack()
			Button(win , text = "ОК", command = win.destroy).pack()
			return None
		else:
			index = index[0] + 1

		if value == "":
			win = Toplevel()
			Label(win, text = "Колличество не введено").pack()
			Button(win , text = "ОК", command = win.destroy).pack()
			return None
		
		k = 0 + 1		
		count = len(self.table)
		i = 0
		while k < count:			
			if self.table[k]['text'] == self.obj.select_article(index):
				s = i * 5
				e = s + 5
				while s < e:
					self.table[s].grid_forget()
					s += 1
				s = i * 5
				n = 0
				while n < 5:
					del(self.table[s])
					n += 1
				self.row = self.row - 1
				count -= 5
			i += 1
			k += 5

	def create_document(self, event):
		dic = {"time":self.label_text_time['text'],
				"warehouse":self.label_text_warehouse['text'],
				"producer":self.label_text_producer['text'],
				"id":self.label_text_id['text'],
				"number":self.label_column_number['text'],
				"article":self.label_column_article['text'],
				"count":self.label_column_count['text'],
				"price":self.label_column_price['text'],
				"summ":self.label_column_summ['text']
		}

		tabel_str = ""
		
		count = len(self.table) / 5
		k = 0

		while k < count:
			tabel_str += "<tr>"
			j = 0
			while j<5:
				tabel_str += "<th>%s</th>" % (self.table[j + k * 5]['text'])
				j += 1
			tabel_str += "</tr>"
			k += 1
		tabel_str += "</table>"

		content = """
			<h3 align = "center">Поставка</h3>
			<p>%(time)s</p>
			<p>%(warehouse)s</p>
			<p>%(producer)s</p>
			<p>%(id)s</p>
			<table>
			<tr><th>%(number)s</th><th>%(article)s</th><th>%(count)s</th><th>%(price)s</th><th>%(summ)s</th></tr>
			""" % dic

		content += tabel_str

		open("document.odt","w").write(content)

	def ex(self, event):	
		self.destroy()
		# import sys #?????
		# sys.exit()

if __name__ == '__main__':
	from db_connection import DB_connector
	obj = DB_connector()
	root = Draw_interface(obj)
	root.mainloop()
	