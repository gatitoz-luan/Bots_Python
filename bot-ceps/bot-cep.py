
# Bibliotecas
from pycep_correios import get_address_from_cep, WebService
import pandas as pd
import numpy as np

# Criar um DataFrame 
df_final = pd.read_csv('base_cep.csv')
df = []
df = pd.DataFrame(columns = ['Estado', 'Cidade', 'Bairro', 'Rua', 'Complemento', 'CEP'])
df.head()
col_list = list(df_final['cep'])            #numero de consultas


for i in range(0,len(col_list)):    
    try:
        address = get_address_from_cep(str(col_list[i]), webservice=WebService.CORREIOS)    #busca na API
        lista = [address['uf'], address['cidade'], address['bairro'], address['logradouro'], address['complemento'], col_list[i]]   #selecão de dados
        if address['uf'] == 'SC':
            df.loc[i] = lista
    except:
        print(i)
        print('Não existe CEP', col_list[i])
        
print(df)
df.to_csv("CEP_SC.csv",encoding = 'ISO-8859-1')          