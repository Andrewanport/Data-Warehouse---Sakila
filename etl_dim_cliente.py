import pandas as pd
from sqlalchemy import create_engine, text

# Conexão com o PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/dw_sakila')

# Consulta SQL para extrair dados da tabela de origem
query = '''
    SELECT 
        customer_id AS id_cliente,
        UPPER(first_name || ' ' || last_name) AS nome_cliente,
        email,
        active AS ativo,
        store_id AS id_loja,
        create_date AS data_criacao
    FROM public.customer
'''

# Lê os dados do banco
df = pd.read_sql_query(query, con=engine)

# Converte a coluna 'ativo' para booleano
df['ativo'] = df['ativo'].astype(bool)

# Limpa os dados da tabela de destino antes de inserir
with engine.begin() as conn:
    conn.execute(text('DELETE FROM dw.dim_cliente'))

# Insere os dados
df.to_sql('dim_cliente', con=engine, schema='dw', if_exists='append', index=False)

print("✅ Tabela 'dw.dim_cliente' populada com sucesso!")
