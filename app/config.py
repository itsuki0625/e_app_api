# DB接続先情報の指定は以下を指定
#
# SQLALCHEMY_DATABASE_URI = '<dbms_name>+<driver_name>://<username>:<password>@<host>:<port>/<dbname>'
#
# DBMS: Oracle, Driver: cx_Oracle
# pip install cx_Oracle
# SQLALCHEMY_DATABASE_URI = 'oracle+cx_oracle://'
#
# DMBS: MySQL, Driver: PyMSQL
# pip install PyMySQL
# SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<username>:<password>@<host>:<port>/<dbname>'
#
# DBMS: PostgreSQL, Driver:psycopg2
# pip install psycopg2
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:itkHomePostgresql@127.0.0.1:5432/test2'
#
# DBMS: SQLite, Driver:Pysqlite
# pip install Pysqlite
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_TRACK_MODIFICATIONS = True