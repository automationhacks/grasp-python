import pymssql

DEV_MS_SQL_SERVER = '10.132.55.163'
DEV_MS_SQL_DB = 'auto_prod'
DEV_DB_USER = 'jenkins'
DEV_DB_PASSWORD = 'letmein'


conn = pymssql.connect(DEV_MS_SQL_SERVER, DEV_DB_USER, 
                       DEV_DB_PASSWORD, DEV_MS_SQL_DB)

cursor = conn.cursor(as_dict=True)

query = """SELECT * FROM INTEG_RESULTS_HISTORY ORDER BY LAST_RUN DESC"""
cursor.execute(query)

f = open(file='out', mode='w')

for row in cursor:
    # step_ = row['step_input'].replace('"', '\"') if row['step_input'] else 'None'
    # result_ = "1" if row['result'] else "0"
    # remarks_ = row['remarks'].replace('"', '\\"')

    # params = row.copy()
    # params.update({'step_input': step_, 'result': result_, 'remarks': remarks_})

    output_log = """{last_run} "{zid}" {uuid} "{pve_env}" "{pve_db}" "{ext_env}" "{integ_env}" {result}\n""".format(**row)
    f.write(output_log)

cursor.close()
f.close()
