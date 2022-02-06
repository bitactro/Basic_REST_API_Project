from os import curdir
import sqlite3
class ConDB:
    def __init__(self) -> None:
        con = sqlite3.connect("appdb.db")
        con.row_factory =sqlite3.Row
        cur= con.cursor()

    def getCursor(self):
            return self.cur
    def closeConnection(self):
            return self.cur
    


            
        

        
