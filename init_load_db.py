import psycopg2

conn = psycopg2.connect(dbname='university', user='postgres', 
                        password='password', host='localhost')
cursor = conn.cursor()

for init_script_name in ["./sql/db_design.sql", "./sql/load_mocks.sql", "./sql/create_constraints.sql"]:
    script = open(init_script_name).read()
    print(f"Executing {init_script_name}")
    cursor.execute(script)
    conn.commit()
    
cursor.close()
conn.close()