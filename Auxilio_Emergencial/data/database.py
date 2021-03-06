from decouple import config
from sqlalchemy import create_engine, Table, Column, String, Integer, Float, MetaData, DateTime

TB_BENEFICIOS = 'TB_STG_AUXEMERGENCIAL_BENEFICIOS'
TB_REGISTRADOS = 'TB_STG_AUXEMERGENCIAL_BENEFICIADOS_REGISTRADOS'
TB_ANONIMOS = 'TB_STG_AUXEMERGENCIAL_BENEFICIADOS_ANONIMOS'
TB_MUNICIPIOS = 'TB_STG_AUXEMERGENCIAL_MUNICIPIOS'
TB_PATH = 'TB_AUX_CAMINHO_CSV'
TB_DATA = 'TB_DIM_DATA'
LOG = 'TB_LOG'

user = config("USER")
senha = config("SENHA")
host = config("HOST")

string_conexao = "mssql+pyodbc://"+user+":"+senha+"@"+host+"\\SQLEXPRESS/GOVBR?driver=ODBC+Driver+17+for+SQL+Server"

global dataserver
dataserver = MetaData()

global engine
engine = create_engine(string_conexao) 

def database_conn():
    stage_beneficios = Table(
        TB_BENEFICIOS
        ,dataserver
        ,Column("ANO_MES", Integer)
        ,Column("COD_MUNICIPIO", Integer)
        ,Column("ENQUADRAMENTO", String(10))
        ,Column("PARCELA", String(3))
        ,Column("TOTAL_PAGO", Float(3))
    )

    stage_registrados = Table(
        TB_REGISTRADOS
        ,dataserver
        ,Column("ANO_MES", Integer)
        ,Column("COD_MUNICIPIO", Integer)
        ,Column("TOTAL_BENEF", Integer)
    )

    stage_anonimos = Table(
        TB_ANONIMOS
        ,dataserver
        ,Column("ANO_MES", Integer)
        ,Column("COD_MUNICIPIO", Integer)
        ,Column("TOTAL_ANONIMOS", Integer)
    )

    stage_municipios = Table(
        TB_MUNICIPIOS
        ,dataserver
        ,Column("COD_MUNICIPIO", Integer)
        ,Column("NOME_MUNICIPIO", String(100))
        ,Column("UF", String(2))
    )

    tabela_log = Table(
        LOG
        ,dataserver
        ,Column("ID", Integer, primary_key=True)
        ,Column("TABELA_JOB", String(50), nullable=False)
        ,Column("DT_INICIO", DateTime)
        ,Column("DT_FIM", DateTime)
        ,Column("STATUS", String(15), nullable=False)
    )

    dataserver.create_all(engine, checkfirst=True)
    
def tables_server():
    for table in dataserver.sorted_tables:
        print(table)

def conexao():
    return engine.connect()

if __name__ == '__main__':
    engine = database_conn()
    tables_server()