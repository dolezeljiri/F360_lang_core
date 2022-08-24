
from ast import arg
from unittest import expectedFailure
import config
import sqlite3
from sqlite3 import Error
from code.log import Log


class Db():

    def __init__(self, ) -> None:
        self.con = self.connect()
        self.cur = self.cursor()

    def connect(self):
        try:
            Log.writeLog("INFO", "Success connection to database {}".format(config.sqliteName))
            return sqlite3.connect(config.sqliteName)
        except Error:
            Log.writeLog("ERROR", Error)

    def cursor(self):
        return self.con.cursor()
           

    def makeTable(self, nameTable, argument):
        try:
            self.cur.execute('CREATE TABLE {} ({})'.format(nameTable, argument))
            self.con.commit()
            Log.writeLog('INFO', 'Tabulka {} byla úspěšně vytvořena.'.format(nameTable))
        except Error:
            Log.writeLog("ERROR", Error)

    def dropTable(self, nameTable):
        try:
            self.cur.execute('DROP TABLE {}'.format(nameTable))
            self.con.commit()
            Log.writeLog('INFO', 'Tabulka {} byla úspěšně smazána.'.format(nameTable))
        except Error:
            Log.writeLog('ERROR', Error)

    def insert(self, nameTable, args):
        pass
    
    def select(nameTable, args):
        pass

    def update():
        pass
    

