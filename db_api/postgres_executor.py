from typing import Any, overload
import psycopg2
import json
import logging


class PostgresExecutor:

   @overload
   def __init__(self, connection_conf : str) -> None:
      '''
         connection_conf should be str with path to json file with params dict
      ''' 
      pass

   def __init__(self, connection_conf : dict) -> None:
      '''
         connection_conf should be dict with params to postgres connecion
      ''' 
      if type(connection_conf) == type(""):
         with open(connection_conf) as conf_file:
            connection_conf = dict(json.loads(conf_file.read()))
      if "dbname" not in connection_conf\
         or "password" not in connection_conf\
         or "host" not in connection_conf\
         or "user" not in connection_conf :
         raise Exception("Configuration for connection is not set correectly")
      self.conn_cof = connection_conf

   def execute_query(self, query : str) -> list:
      results = []
      try:
         with psycopg2.connect(**self.conn_cof) as connection:
            with connection.cursor() as cursor:
               cursor.execute(query)
               try:
                  results = cursor.fetchall()
               except:
                  logging.warning(f"Couldn't fetch results from query '{query[:50]} ... '")
               connection.commit()
      except Exception as e:
         logging.error(e)
      finally:
         return results

   def get_column_names(self, table_name : str) -> list:
      res = self.execute_query(f"SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{table_name}'")
      if len(res) == 0:
         logging.warning(f"get_column_names returned empty list, no such table '{table_name}'")
      res = [x[0] for x in res]
      return res

   def execute_script_file(self, path : str) -> list:
      script = open(path).read()
      logging.info(f"Executing {path}")
      return self.execute_query(script)


if __name__ == "__main__":
   print("START")
   ex = PostgresExecutor("./dev_postgres_conn.conf.json")
   res = ex.execute_query("SELECT * FROM employee LIMIT 10")
   header = ex.get_column_names("employee")
   print(*header)
   print(*res, sep="\n")
   print("END")
