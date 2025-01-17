import pymysql
import src.data_service.dbutils as dbutils
import src.data_service.RDBDataTable as RDBDataTable

# The REST application server app.py will be handling multiple requests over a long period of time.
# It is inefficient to create an instance of RDBDataTable for each request.  This is a cache of created
# instances.
_db_tables = {}
_conn = pymysql.connect(
    host= "localhost",
    port= 3306,
    user = "dbuser",
    password="dbuserdbuser",
    db="lahman2019clean",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

def get_rdb_table(table_name, db_name, key_columns=None, connect_info=None):
    """

    :param table_name: Name of the database table.
    :param db_name: Schema/database name.
    :param key_columns: This is a trap. Just use None.
    :param connect_info: You can specify if you have some special connection, but it is
        OK to just use the default connection.
    :return:
    """
    global _db_tables

    # We use the fully qualified table name as the key into the cache, e.g. lahman2019clean.people.
    key = db_name + "." + table_name

    #Do not create the RDB table directly, th function will do this for you.
    # Have we already created and cache the data table?
    result = _db_tables.get(key, None)
    print('[DTA] result {0}'.format(result))
    # We have not yet accessed this table.
    if result is None:

        # Make an RDBDataTable for this database table.
        result = RDBDataTable.RDBDataTable(table_name, db_name, key_columns, connect_info)
        print('[DTA]get result {0}'.format(result))

        # Add to the cache.
        _db_tables[key] = result

    return result


#########################################
#
#
# YOU HAVE TO IMPLEMENT THE FUNCTIONS BELOW.
#
#
# -- TO IMPLEMENT --
#########################################

def get_databases():
    """

    :return: A list of databases/schema at this endpoint.
    """
    #Run query, get a list of database and return.
    # -- TO IMPLEMENT --
    #sql call here.
    #result = ["db1", "db2", "db3"]
    sql = "select " + "DATABASE()"

    res, d = dbutils.run_q(sql, conn=_conn)

    print('res, d = {0} {1}'.format(res, d))
    return d


def get_tables(dbname):
 #Run query, get a list of database and return.
    # -- TO IMPLEMENT --
    #sql call here.
    #result = ["db1", "db2", "db3"]

    sql = "select TABLE_NAME from INFORMATION_SCHEMA.TABLES where "
    sql += """TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='%s'""" % (dbname)

    res, table = dbutils.run_q(sql, conn=_conn)

    return table











