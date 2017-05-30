import pymssql

DEV_MS_SQL_SERVER = ''
DEV_MS_SQL_DB = ''
DEV_DB_USER = ''
DEV_DB_PASSWORD = ''


conn = pymssql.connect(DEV_MS_SQL_SERVER, DEV_DB_USER, DEV_DB_PASSWORD, DEV_MS_SQL_DB)

cursor = conn.cursor()

query = """SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = %s"""
params = """'COMMON_env_details'"""
print('Here')
cursor.execute(query, params)

print('came here')
print(cursor)
for row in cursor:
    print('Came here')
    print(row)

cursor.close()