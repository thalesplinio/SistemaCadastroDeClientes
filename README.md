# Cadastro de Clientes
[![NPM](https://img.shields.io/npm/l/react)]((https://github.com/thalesplinio/cadastroDeClientes/blob/main/LICENSE)) </br>
Pequena aplicação para cadastrar clientes, usando Python e sqlite3 com interface gráfica.
> Status: Em desenvolvimento.

## Sobre o Projeto:
>Este projeto foi feito para fins de estudo, desenvolvido pra cadastrar clientes de empresas substituindo assim o uso de planilhas Excel. </br>
>Cadastro, visualização, pesquisa, alteração e remoção de registro. </br>
>usando banco de dados SQLite3 com a possibilidade de exportar esses registros em formato excel e pdf.

## Tecnologias e bibliotecas utilizadas.
- Python 3.12.3
- API [ViaCep](https://viacep.com.br/)
- SQLite3

## Iniciando o projeto.
> Baixe o projeto e antes de iniciar crie um ambiente virtual
- Para Linux.  
~~~python
# Criando ambiente virtual
python3 -m venv venv

# Ativando o ambiente virtual
source venv/bin/activate
~~~

- Para Windows
~~~python
# Criando ambiente virtual
python -m venv venv

# Ativando o ambiente virtual
venv/bin/activate
~~~
- Instale as dependências do projeto contidas em requirements.txt
~~~python
# No terminal execute
pip install -r requirements.txt
~~~
- <em>Tudo pronto agora inicie o projeto</em>

## Apresentação do projeto.
### Tela inicial.
> Essa é a tela inicial do projeto, aqui é aonde vamos inserir os dados do cliente.  
> No campo CEP, estou usando uma API 'viacep' para coletar os dados recebidos, quando o usuário insere um cep válido os campos
> (Endereço, Bairro, Cidade e Estado) são preenchidos automaticamente e aparece um ✅ 'check' informando visualmente que o cep foi encontrado.
> E se o usuário preencher um cep que não for válido nada acontece.