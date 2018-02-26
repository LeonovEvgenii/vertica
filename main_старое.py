from dbconnection import getDBConnection, getWarehouseList
from docdbinterface import DocDBInterface

def showMessage(eroro):
	import sys
	print(eroro, file = sys.stderr)


if __name__ == '__main__':
	try:
		conn = getDBConnection()
		rez = getWarehouseList(conn)

		root = DocDBInterface(conn, rez)
		root.mainloop()
	except Exception as e:
		showMessage(str(e))
