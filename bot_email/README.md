# Bem vindo ao bot-emails! 		versão=1.1.1
Um software que com base em uma lista de emails's retorna uma tabela com os dados empresariais selecionados do banco de dados da Receita Federal.

## Situação do projeto:
A partir da versão 1.0 o software está em pleno funcionamento

## Características
[x] Copiar dados de uma planilha inicial  
[x] Buscar dados no banco de dados da Receita Federal  
[x] Gerar um arquivo .csv  

## Dependências 
* 1 arquivo com nome = "emails.xlsx" na mesma pasta que o arquivo executável, esse .xlsx deve conter os emails que serão consultados pelo algoritmo, esses emails devem ser organizados com 1 email por linha usando apenas a primeira coluna.

* python3.9
  
* datetime
>pip install datetime

* pyodbc
>pip install pyodbc

* openpyxl
>pip install openpyxl

* csv
>pip install csv

* time
>pip install time

## Demonstração da Aplicação
#### Ao instalar as dependencias e compilar o código é gerado um arquivo 'cnpjs_enriquecidos_infinito.csv' com estrutura de uma única coluna, configuração que pode ser corrigida em seu editor de planilhas (Exemplo Excel: Selecionar todos (clicando na coluna A) -> "DADOS" -> 'Texto para colunas' -> "avançar" -> [x] virgula, [ ] tabulação -> avançar -> concluir ).

### TESTES
* Na fase atual é possivel obter os dados selecionados no banco de dados.
* Nos testes o desempenho foi em consultar cerca de 500.000 emails, sendo concluído em aproximadamente de 20 minutos.

##### Desenvolvido por: Luan Rodrigoda Silva Costa
##### Orientado por: Denner Felipe Silva Ferr