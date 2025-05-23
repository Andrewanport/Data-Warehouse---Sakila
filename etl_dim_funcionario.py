import pandas as pd
from sqlalchemy import create_engine, text

# Conexão com PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/dw_sakila')

# Query atualizada
query = """
    SELECT 
        staff_id AS id_funcionario,
        UPPER(first_name || ' ' || last_name) AS nome_funcionario,
        email,
        store_id AS id_loja,
        active::boolean AS ativo,
        last_update AS data_contratacao
    FROM public.staff;
"""

# Carrega os dados
df = pd.read_sql(query, con=engine)

# Limpa tabela antes de inserir
with engine.begin() as conn:
    conn.execute(text("DELETE FROM dw.dim_funcionario"))

# Insere no DW
df.to_sql('dim_funcionario', con=engine, schema='dw', if_exists='append', index=False)

print("✅ Tabela 'dw.dim_funcionario' populada com sucesso!")
