'''
    Ensure that paths from load_mocks are available for postgres instance
'''

from db_api.postgres_executor import PostgresExecutor


ex = PostgresExecutor("./dev_postgres_conn.conf.json")
for init_script_name in ["./sql/db_design.sql", "./sql/load_mocks.sql", "./sql/create_constraints.sql", "./sql/create_views.sql"]:
    ex.execute_script_file(init_script_name)