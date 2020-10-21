import os
import sqlite3
import tempfile

global cursor; cursor = None

def createTestDB():
    """
    Used by green to set up the local work process's testdb
    """
    global testdb_name
    global testdb_connection
    global cursor
    testdb_name = 'testdb_{}.db'.format(os.getpid())
    testdb_connection = sqlite3.connect(testdb_name)
    cursor = testdb_connection.cursor()
    cursor.execute(
        "CREATE TABLE magic_powers (name varchar, mana int, damage int)")
    cursor.execute(
            "INSERT INTO magic_powers VALUES ('flamestrike', 40, 300)")
    cursor.execute(
            "INSERT INTO magic_powers VALUES ('blizzard', 30, 200)")

def cleanupTestDB():
    """
    Used by green to clean up the local worker process's testdb
    """
    global testdb_name
    global testdb_connection
    testdb_connection.close()
    os.remove(testdb_name)

def getPowers():
    """
    Set of all available magical powers.
    """
    global cursor
    result = set()
    for row in cursor.execute("SELECT name from magic_powers"):
        result.add(row[0])
    return result
