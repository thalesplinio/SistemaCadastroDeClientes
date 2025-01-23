import os
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
_pasta_banco = "data"
os.makedirs(_pasta_banco, exist_ok=True)
BANCO_DE_DADOS = os.path.join(_pasta_banco, "databanco_cliente.sqlite3")

if __name__ == "__main__":
    print(DATA_FORMATADA)
