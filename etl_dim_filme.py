import pandas as pd
from sqlalchemy import create_engine, text

# Consulta SQL para extrair dados do filme
query = """
    SELECT 
        f.film_id AS id_filme,
        f.title AS titulo,
        f.description AS descricao,
        f.release_year AS ano_lancamento,
        l.name AS idioma,
        f.length AS duracao,
        f.rating AS classificacao
    FROM public.film f
    JOIN public.language l ON f.language_id = l.language_id;
"""

# Conexão com PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/dw_sakila')

# Extrai os dados
df = pd.read_sql(query, con=engine)

# Limpa a tabela antes de inserir
with engine.begin() as conn:
    conn.execute(text("DELETE FROM dw.dim_filme"))

# Insere no DW
df.to_sql('dim_filme', con=engine, schema='dw', if_exists='append', index=False)

print("✅ Tabela 'dw.dim_filme' populada com sucesso!")
