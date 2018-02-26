import psycopg2

class  UserError(Exception):
	def __init__(self, user, password):
		self.__message = "Пользователь %s не найден или пароль не верен" % user 

	def __str__(self):
		return self.__message
		
class  DatabaseError(Exception):
	def __init__(self, dbname):
		self.__message = "База данных %s не найденa" % dbname 

	def __str__(self):
		return self.__message
		
class  NetworkError(Exception):
	def __init__(self, host):
		self.__message = "Ошибка сети" 	

	def __str__(self):
		return self.__message

def getDBConnection(dbname = 'vertica_db', 
					user = 'vertica',
					host = 'localhost',
					password = '123'):
	connection_str = "dbname = '%s' user = '%s' host = '%s' password = '%s'" % (dbname, user, host, password)
	
	try:
		conn = psycopg2.connect(connection_str)
	except psycopg2.OperationalError as e:
		message_str = str(e)
		if message_str.startswith('FATAL:  database'):
			raise DatabaseError(dbname)
		elif message_str.startswith('FATAL:  password'):
			raise UserError(user, password)
		elif message_str.startswith("could not"):
			raise NetworkError(host)
		else:
			raise e
	return conn

def getWarehouseList(conn):
	cur = conn.cursor()
	cur.execute('SELECT * FROM "склад";')
	data = cur.fetchall()
	#print(data)
	rez = []
	for i in data:
		rez.append(i[0])
	#print(rez)
	return rez

if __name__ == '__main__':
	conn = getDBConnection()
	getWarehouseList(conn)