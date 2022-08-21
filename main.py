from code.db import Db
import config

db = Db()
db.makeTable('text', 'id integer PRIMARY KEY, name text')
db.dropTable('text')


if __name__ == "__main__":
   pass