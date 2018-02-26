from db_connection import DB_connector
from interface import Draw_interface

if __name__ == '__main__':
	
		obj = DB_connector()
		root = Draw_interface(obj)		
		root.mainloop()
	 