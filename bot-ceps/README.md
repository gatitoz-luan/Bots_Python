# Bem vindo ao bot-ceps! 		versão=1.1.2
Um software que com base em uma lista base de CEP's Irá retornar uma tabela com todos os os endereços cadastrados nos Correios.


## Situação do projeto:
A partir da versão 1.0 o software foi testado e apresenta um retorno 99% das buscas mas em um processo demorado até então

## Características
[x] Copiar dados de uma planilha inicial  
[x] Buscar dados na API dos Correios  
[x] Gerar data frame  
[x] exportar data frame em um arquivo .csv 

## Dependências 
* 1 arquivo com nome = "base_cep.csv" na mesma pasta que o arquivo executável, esse .csv deve conter os CEP's que serão consultados pelo algoritmo, esses CEP's devem ser organizados com 1 CEP por linha usando apenas a primeira coluna.

* python3.9
  
* pycep_correios
>pip install pycep_correios

* pandas
>pip install pandas

* numpy
>pip install numpy
## Demonstração da Aplicação
#### Ao instalar as dependencias e compilar o código é possível visualizar o data frame
#### O arquivo '.csv' gerado estrutura os dados em uma única coluna, configuração que pode ser corrigida em seu editor de planilhas (Exemplo Excel: Selecionar todos (clicando na coluna A) -> "DADOS" -> 'Texto para colunas' -> "avançar" -> [x] virgula, [ ] tabulação -> avançar -> concluir ).

### TESTES
* Na fase atual estamos com cerca de 99% dos CEP's encontrados, testamos outras API com (ViaCEP, APICEP, BrasilAPI), mas nenhuma apresentou mais resultados, em geral essas api's buscam na base dos correios(usada nesse código) e em outras, mas essa busca extra não trouxe benefícios, apenas mais lentidão.
* Em uma base de 38275 CEP's foram encontrados dados de 38272 CEP's após 345 minutos.

##### Desenvolvido por: Luan Rodrigoda Silva Costa
##### Orientado por: Denner Felipe Silva Ferreira
