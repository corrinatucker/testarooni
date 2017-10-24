import MySQLdb

def connection():
    conn = MySQLdb.connect(host = "localhost", 
                           user = "root", 
                           passwd = "Desipup12", 
                           db = "demo")
    c = conn.cursor()
    
    return c, conn

