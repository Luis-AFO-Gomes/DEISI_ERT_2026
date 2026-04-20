import pyodbc
import configparser
from pathlib import Path
import platform

class dao:
    __conn_str: str
    __db_connection: pyodbc.Connection|None

    def __init__(self):
        config = configparser.ConfigParser()
        ini_path = Path(__file__).resolve().parent / "config" / "config.ini"
        print(f"Loading configuration from: {ini_path}")
        config.read(ini_path, encoding="utf-8")
    
        self.__conn_str = (f"DRIVER={{{config['myMSSQLdb']['driver']}}};"
            f"SERVER={config['myMSSQLdb']['host']};"
            f"DATABASE={config['myMSSQLdb']['db']};"
            f"UID={config['myMSSQLdb']['user']};"
            f"PWD={config['myMSSQLdb']['pass']};"   
            f"Encrypt={config['myMSSQLdb']['encrypt']};"
            f"TrustServerCertificate={config['myMSSQLdb']['trust_server_certificate']};"
        )

        print("Connecting to database...")  
        print(f"Connection string: {self.__conn_str}")
        try:
            self.__db_connection = pyodbc.connect(self.__conn_str)
            print("Connection established successfully.")
        except pyodbc.Error as e:
            print(f"Error connecting to database: {e}")
            self.__db_connection = None

    def __del__(self):
        if self.__db_connection:
            self.__db_connection.close()
            print("Database connection closed.")

    def __str__(self) -> str:
        return f"DAO(Connection String: {self.__conn_str})"            

    def connect(self) -> pyodbc.Connection|None:
        return self.__db_connection

    def cursor(self) -> pyodbc.Cursor|None:
        if self.__db_connection:
            return self.__db_connection.cursor()
        return None

    def val_env(self):
        print(f"plataform:{platform.architecture()}")
        print(f"drivers: {pyodbc.drivers()}")

        config = configparser.ConfigParser()
        ini_path = Path(__file__).resolve().parent / "config" / "config.ini"
        config.read(ini_path, encoding="utf-8")

        # print("Loaded files:", config)
        print("Sections:", config.sections())

        print(f"driver: {config['myMSSQLdb']['driver']}")


