import pandas as pd
from sqlalchemy import create_engine, text

# Gera intervalo de datas
datas = pd.date_range(start='2005-01-01', end='2025-12-31')

# Monta a dimensão tempo
df = pd.DataFrame({
    'data': datas,
    'dia': datas.day,
    'mes': datas.month,
    'ano': datas.year,
    'nome_mes': datas.strftime('%B'),
    'dia_semana': datas.strftime('%A'),
    'fim_de_semana': datas.weekday >= 5
})

# Conexão com PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/dw_sakila')

# Limpa os dados da tabela antes de inserir (mantendo constraints)
with engine.begin() as conn:
    conn.execute(text('DELETE FROM dw.dim_tempo'))

# Insere os dados
df.to_sql('dim_tempo', con=engine, schema='dw', if_exists='append', index=False)

print("✅ Tabela 'dw.dim_tempo' populada com sucesso!")
