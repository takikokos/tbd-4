from typing import Any, Dict, List


UPDATE_QUERY = \
'''
UPDATE {table_name}
SET {updating_fields_str}
WHERE {id_column} = {sql_id}
'''

DELETE_QUERY = \
'''
DELETE FROM {table_name} 
WHERE {id_column} in {removing_ids_str}
'''

SELECT_ALL_QUERY =\
'''
SELECT *
FROM {table_name}
'''

INSERT_QUERY =\
'''
INSERT INTO {table_name} {columns_str}
VALUES {values_str}
'''

def generate_delete_query(table_name : str, id_column : str, removin_ids : List[str]) -> str:
    '''
        generates query str to delete all the rows from table_name where 
        column named id_column equals values from removin_ids
    '''
    removing_ids_str = "(" + ", ".join(removin_ids) + ")"
    return DELETE_QUERY.format(table_name = table_name, id_column = id_column, removing_ids_str = removing_ids_str)

def generate_update_query(table_name : str, changes : Dict[str, Any], id_column : str, sql_id : str) -> str:
    '''
        generate query str to update all the rows from table_name
        where id_column = sql_id

        changes : dict where keys are column names and values are new values
        for these columns
    '''
    updating_fields = ""
    for column, value in changes.items():
        updating_fields += f"{column} = {repr(value) if value is not None else 'null'}, "
    updating_fields = updating_fields.rstrip(", ")
    return  UPDATE_QUERY.format(table_name = table_name, 
                                updating_fields_str = updating_fields, 
                                id_column = id_column,
                                sql_id = sql_id)

def generate_insert_query(table_name : str, columns : List[str], values : List[str]) -> str:
    '''
        1st value and 1st column will be ignored (autoincrement id)
    '''
    values_fixed = [f"{repr(value) if value != '' else 'null'}" for value in values]
    values_str = "(" + ", ".join(values_fixed[1:]) + ")"
    columns_str = "(" + ", ".join(columns[1:]) + ")"
    return INSERT_QUERY.format(table_name = table_name, values_str = values_str, columns_str = columns_str)