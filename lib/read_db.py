import sqlite3
#from datetime import datetime
import csv, codecs, cStringIO

class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f", 
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([unicode(s).encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)


def read_search(dbase,report):
	db = sqlite3.connect("%s/browser.db" % dbase)
	c = db.cursor()
	c.execute('select search, datetime(date/1000,\'unixepoch\') from searches;')

	writer = UnicodeWriter(open("%s/searches.csv" % report, "wb"))
	writer.writerow(["Search Term", "Date & Time (GMT)"])
	writer.writerows(c)
	#writer.writerow("Note: Only search made through browser")
	c.close()
	db.close()

def read_bookmark(dbase,report):
	db = sqlite3.connect("%s/browser.db" % dbase)
	c = db.cursor()
	c.execute('select title, url, visits, datetime(date/1000,\'unixepoch\') from bookmarks where bookmark = 1;')

	writer = UnicodeWriter(open("%s/bookmarks.csv" % report, "wb"))
	writer.writerow(["Title", "URL", "Visits", "Date & Time (GMT)"])
	writer.writerows(c)
	c.close()
	db.close()

def read_history(dbase,report):
	db = sqlite3.connect("%s/browser.db" % dbase)
	c = db.cursor()
	c.execute('select url, visits, datetime(date/1000,\'unixepoch\') from bookmarks where user_entered = 0 or user_entered=1;')

	writer = UnicodeWriter(open("%s/history.csv" % report, "wb"))
	writer.writerow(["URL", "Visits", "Date & Time (GMT)"])
	writer.writerows(c)
	c.close()
	db.close()

def read_account(dbase, report):
	db = sqlite3.connect("%s/accounts.db" % dbase)
	c = db.cursor()
	c.execute('select * from accounts;')

	writer = UnicodeWriter(open("%s/accounts.csv" % report, "wb"))
	writer.writerow(["ID", "Name", "Type", "Password"])
	writer.writerows(c)
	c.close()
	db.close()