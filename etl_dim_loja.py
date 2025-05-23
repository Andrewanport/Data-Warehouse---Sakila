import pandas as pd
from sqlalchemy import create_engine, text

# Query para extrair dados da dimensão loja
query = """
    SELECT 
        store_id AS id_loja,
        address AS endereco,
        city AS cidade,
        country AS pais
    FROM public.store s
    JOIN public.address a ON s.address_id = a.address_id
    JOIN public.city c ON a.city_id = c.city_id
    JOIN public.country co ON c.country_id = co.country_id;
"""

# Conexão com o PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/dw_sakila')

# Carrega os dados
df = pd.read_sql(query, con=engine)

# Limpa tabela antes de inserir
with engine.begin() as conn:
    conn.execute(text("DELETE FROM dw.dim_loja"))

# Insere no DW
df.to_sql(name='dim_loja', con=engine, schema='dw', if_exists='append', index=False)

print("✅ Tabela 'dw.dim_loja' populada com sucesso!")
