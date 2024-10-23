import datetime
from datetime import datetime
from locale import setlocale, LC_ALL


#  setup data
SET_LOCALE = "PT_br.utf-8"
FORMATE_DATE = "%A, %d de %B de %Y,  %H:%M:%S"
setlocale(LC_ALL, SET_LOCALE)
dt = datetime.now()
DATA_FORMATADA = dt.strftime(FORMATE_DATE)

# banco de dados
BANCO_DE_DADOS = "banco_cliente.sqlite3"


if __name__ == "__main__":
    print(DATA_FORMATADA)
