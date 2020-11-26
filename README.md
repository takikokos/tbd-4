##DEV

Usefull commands:

    - `./venv/lib/python3.8/site-packages/PySide2/Designer` to run qt designer
    - `pyside2-uic "mainwindow.ui" -o "mainwindow_ui.py"` to create .py file from .ui (remember to rename ui class  to MainWindow_UI)
    - `pip install -r requirements.txt` install from requirements.txt
    - `docker run --name psql -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres` run posgresql docker image