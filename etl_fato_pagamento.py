import pandas as pd
from sqlalchemy import create_engine, text

# Conexão com o PostgreSQL
engine = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/dw_sakila')

# Query base com os joins entre tabelas
query = """
    SELECT
        p.payment_id          AS id_pagamento,
        c.customer_id         AS id_cliente,
        f.film_id             AS id_filme,
        s.store_id            AS id_loja,
        d.id_tempo            AS id_tempo,
        p.amount              AS valor
    FROM payment p
    JOIN rental r ON p.rental_id = r.rental_id
    JOIN inventory i ON r.inventory_id = i.inventory_id
    JOIN film f ON i.film_id = f.film_id
    JOIN customer c ON p.customer_id = c.customer_id
    JOIN staff sf ON p.staff_id = sf.staff_id
    JOIN store s ON sf.store_id = s.store_id
    JOIN dw.dim_tempo d ON d.data = DATE(p.payment_date);
"""

# Carrega os dados do banco de origem
df = pd.read_sql(query, con=engine)

# Limpa a tabela fato antes de inserir os dados
with engine.begin() as conn:
    conn.execute(text("DELETE FROM dw.fato_pagamento"))

# Insere os dados na tabela fato

df.to_sql('fato_pagamento', con=engine, schema='dw', if_exists='append', index=False)

print("\U00002705 Tabela 'dw.fato_pagamento' populada com sucesso!")
