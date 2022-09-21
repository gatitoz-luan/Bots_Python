import pyodbc
from openpyxl import load_workbook
import csv
from datetime import datetime
import time


def get_data_from_RFB(email):
    # buscando dados na RFB
    query = "SELECT\
                RESPONSAVEL_CPF,\
                RESPONSAVEL_NOME,\
                END_LOGRADOURO, \
                END_NUMERO,\
                END_BAIRRO,\
                END_CEP,\
                END_MUNICIPIO,\
                END_UF,\
                DDD1,\
                TELEFONE1,\
                DDD2,\
                TELEFONE2,\
                EMAIL,\
                NOME_EMPRESARIAL,\
                NOME_FANTASIA, \
                DT_ABERTURA_ESTAB,\
                CNAE_PRINCIPAL_COD,\
                OPCAO_MEI,\
                PORTE,\
                SIT_CADASTRAL,\
                CNPJ \
            FROM dbo.VW010_EMPRESAS_RFB \
        WHERE EMAIL IN {0};".format(email)

    try:
        cursor_sql_server.execute(query)
        return cursor_sql_server.fetchall()
    except:
        #em caso de erro atualiza o servidor e consulta novamente
        printConnectionError()
        connectBD()
        get_data_from_RFB(email)


#converte o código de porte
def get_porte(optante_mei, porte_id):
    porte_dict = {
        0: 'Não informado',
        '00': 'Não informado',
        '0': 'Não informado',
        1: 'ME',
        '01': 'ME',
        '1': 'ME',
        3: 'EPP',
        '03': 'EPP',
        '3': 'EPP',
        5: 'Demais',
        '05': 'Demais',
        '5': 'Demais'
    }

    if(optante_mei == 'S'):
        return 'MEI'
    elif porte_id != '' and porte_id is not None and porte_dict[porte_id] is not None:
        return porte_dict[porte_id]
    else:
        return ''

# Definindo Nome fantasia para valores defalt
def get_fantasy_name(razao_social, nome_fantasia):
    if(nome_fantasia is None or nome_fantasia == ''):
        return razao_social
    return nome_fantasia


def connectBD():
    # configurando conexão SQL SERVER
    try:
        print('Iniciando conexão com banco de dados')
        global sql_server_conection
        global cursor_sql_server
        sql_server_conection=pyodbc.connect(r'DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.1.140.172;DATABASE=DH1MVP_HUB;UID=qlik-sebrae-sc;PWD=$3bR@eBISC!2021;')
        cursor_sql_server=sql_server_conection.cursor()
        
        print('Conectado')
    except:
        printConnectionError()
        time.sleep(60)
        connectBD()

# Função de escrever linha no arquivo criado
def Write(enriched_company):
    for j in range (len(enriched_company)):
        newFileWriter.writerow([str(enriched_company[j][0]), 
                                str(enriched_company[j][1]), 
                                str(enriched_company[j][2]), 
                                str(enriched_company[j][3]), 
                                str(enriched_company[j][4]), 
                                str(enriched_company[j][5]), 
                                str(enriched_company[j][6]), 
                                str(enriched_company[j][7]), 
                                str(enriched_company[j][8]), 
                                str(enriched_company[j][9]), 
                                str(enriched_company[j][10]), 
                                str(enriched_company[j][11]), 
                                str(enriched_company[j][12]), 
                                int(enriched_company[j][20]), 
                                str(enriched_company[j][13]), 
                                get_fantasy_name(str(enriched_company[j][13]), str(enriched_company[j][14])), 
                                str(enriched_company[j][15]), 
                                str(enriched_company[j][15])[0:4], 
                                str(enriched_company[j][15])[4:6], 
                                str(enriched_company[j][16]), 
                                get_porte(enriched_company[j][17], 
                                enriched_company[j][18]), 
                                situacao_dict[enriched_company[j][19]]])
# encerra conexão com BD
def closeConnectionDB():
    cursor_sql_server.close()
    sql_server_conection.close()


def printConnectionError():
    print('Erro Conexão: '+datetime.now().strftime("%d/%m/%Y %H:%M:%S"))


#################-----------SCRIPT------------#############
sql_server_conection: Any
cursor_sql_server: Any
connectBD()

print('Iniciando leitura da planilha de emails')

wb=load_workbook(filename='emails.xlsx', read_only=True)  # planilha
ws=wb['script']  # Lendo aba da planilha

# criando csv
with open('cnpjs_enriquecidos_infinito.csv', 'w', newline='') as newFile:
    newFileWriter=csv.writer(newFile)
    email=[]
# cria cabeçalho
    newFileWriter.writerow([
      'CPF', #cpf
      'CONTATO', #contato
      'ENDERECO', # endereco
      'NUMERO', # numero
      'BAIRRO', # bairro
      'CEP',
      'MUNICIPIO',
      'ESTADO',
      'DDD1',
      'TELEFONE1',
      'DDD2',
      'TELEFONE2',
      'EMAIL',
      'CNPJ', 
      'RAZAO SOCIAL', #razao social
      'NOME FANTASIA', 
      'DT_ABERTURA', #Data de abertura
      'ANO_ABERTURA', #ANO de abertura
      'MES_ABERTURA', #MES de abertura
      'CNAE',
      'PORTE', #porte 00 - NAO INFORMADO 01 - MICRO EMPRESA 03 - EMPRESA DE PEQUENO PORTE 05 - DEMAIS
      'SITUACAO' #situacao 01 - NULA 02 - ATIVA 03 - SUSPENSA 04 - INAPTA 08 - BAIXADA
      ])
# transforma código em situação
    situacao_dict ={
        1: 'Não Informada',
        '01': 'Não Informada',
        2: 'Ativa',
        '02': 'Ativa',
        3: 'Suspensa',
        '03': 'Suspensa',
        4: 'Inapta',
        '04': 'Inapta',
        8: 'Baixada',
        '08': 'Baixada'
    }
    # Realiza a busca no arquivo inicial e aculmula uma tupla de valores 
    for row in ws.rows:
        email.append(str(row[0].value))
        if len(email)< 40000:
            continue
        elif len(email)==40000:
            consulta =  tuple(email)            
            email.clear()
        print('consultado')
    # Consulta a tupla de emails no BD
        enriched_company = get_data_from_RFB(consulta)
        print('buscou no banco')
        Write(enriched_company)
        print('escrito')
        
    #para a ultima consulta
    print('ultima consulta')
    consulta =  tuple(email)            
    email.clear()
    enriched_company = get_data_from_RFB(consulta)
    print('buscou no banco')
    Write(enriched_company)
    print('escrito')
   
# fechando conexões e cursores
cursor_sql_server.close()
sql_server_conection.close()

# fechando planilha
wb.close()