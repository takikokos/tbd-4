## Unexpected functionallity

- click on cell to edit value inside
- click delete button to delete selected rows
- click add button to add row, id will be generated automatically, so no need to enter first value
- click update button to update remote database and commit all the made changes (all from above will be lost otherwise)
- click on column name to order by this column

Foramt for configuration file :

```json
{
    "dbname" : "university", 
    "user" : "postgres", 
    "password" : "password", 
    "host" : "localhost"
}
```

## Development hints

Mocks have some artifacts and wrong data after generating, so that load_mocks.sql fixes it.

Usefull commands (should be run from root project folder):

- `./venv/lib/python3.8/site-packages/PySide2/Designer` to run qt designer
- `pyside2-uic "mainwindow.ui" -o "mainwindow_ui.py"` to create .py file from .ui (remember to rename ui class  to MainWindow_UI)
- `pip install -r requirements.txt` install from requirements.txt
- `docker run -v `pwd`/mocks:/mocks --name psql -e POSTGRES_PASSWORD=password -e POSTGRES_DB=university -e POSTGRES_USER=postgres -d -p 5432:5432 postgres` run posgresql docker image
- run init_load_db.py to create all the tables and load mocks into them
- run `pyinstaller main.py` to generate executable
