import psycopg2

class DB_connector(object):
	def __init__(self, dbname = 'vertica_db', 
						user = 'vertica',
						host = 'localhost',
						password = '123'):	
		super(DB_connector, self).__init__()
		self.connection_str = "dbname = '%s' user = '%s' host = '%s' password = '%s'" % (dbname, user, host, password)
		self.number_of_delivery = 0
		try:
			self.conn = psycopg2.connect(self.connection_str)
		except psycopg2.OperationalError as e:
			print(e)

	def get_list_warehouse(self):
		data = self.execute_sql('SELECT * FROM "склад";')
		return [i[1] for i in data]

	def select_warehouse(self, _id):
		data = self.execute_sql('SELECT "название" FROM "склад" WHERE id = %(id)s;' % {'id': _id})
		return data[0][0]

	def select_warehouse_id(self, nam):
		data = self.execute_sql('SELECT "id" FROM "склад" WHERE "название" = \'%(nam)s\';' % {'nam': nam})
		return data[0][0]

	def get_list_producer(self):
		data = self.execute_sql('SELECT * FROM "поставщик";')
		return [i[1] for i in data]

	def select_producer(self, _id):
		data = self.execute_sql('SELECT "название" FROM "поставщик" WHERE id = %(id)s;' % {'id': _id})
		return data[0][0]

	def select_producer_id(self, nam):
		data = self.execute_sql('SELECT "id" FROM "поставщик" WHERE "название" = \'%(nam)s\';' % {'nam': nam})
		return data[0][0]

	def get_list_article(self):
		data = self.execute_sql('SELECT "название" FROM "товар";')
		return [i[0] for i in data]

	def select_article(self, _id):
		data = self.execute_sql('SELECT "название" FROM "товар" WHERE id = %(id)s;' % {'id': _id})
		return data[0][0]

	def select_article_id(self, nam):
		data = self.execute_sql('SELECT "id" FROM "товар" WHERE "название" = \'%(nam)s\';' % {'nam': nam})
		return data[0][0]

	def get_price_for_article(self, _id = "1"):
		data = self.execute_sql('SELECT "цена" FROM "товар" WHERE "id" = \'%(id)s\';' % {'id': _id})
		return data[0][0]

	def get_max_id_for_delivery(self):
		data = self.execute_sql('SELECT nextval(\'"поставка_id_seq"\');')
		self.number_of_delivery = data[0][0]
		return self.number_of_delivery

	def write_to_delivery(self, warehouse, producer, data, number):
		sql = 'insert into "поставка" ("склад", "поставщик", "дата", "номер") values \
		(%(warehouse)s, %(producer)s, \'%(data)s\', %(number)s);'\
		 % {'warehouse': warehouse, 'producer': producer, 'data': data, 'number': number}
		self.execute_sql(sql)


	def write_to_delivery_article(self, delivery, article, count):
		sql = 'insert into "поставка товара" ("поставка", "товар", "количество") values \
		(%(delivery)s, %(article)s, \'%(count)s\');'\
		 % {'delivery': delivery, 'article': article, 'count': count}
		self.execute_sql(sql)

	def execute_sql(self, sql):
		cur = self.conn.cursor()
		#print("Выполняется запрос: " + sql)
		#print(sql)
		cur.execute(sql)
		data = None
		try:
			data = cur.fetchall()
		except psycopg2.ProgrammingError:
			pass
		finally:
			self.conn.commit()
			cur.close()
			#self.conn.close()
			return data


if __name__ == '__main__':
	obj = DB_connector()
	#print(obj.get_max_id_for_delivery())
	#obj.write_to_delivery_article(1, 1, 1)
	obj.get_list_warehouse()
