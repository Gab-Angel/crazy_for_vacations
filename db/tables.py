# AS TABELAS QUE PRECISAM SER CRIADAS AUTOMATICAMENTE
import psycopg2
from db.conn import connection



def create_tables():
    with connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS levels (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(30) NOT NULL UNIQUE,
                        required_score INT NOT NULL,
                        order_number INT NOT NULL UNIQUE
                    );


                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        nick_name VARCHAR(30) NOT NULL,
                        current_level_id INT REFERENCES levels(id),
                        total_score INT DEFAULT 0,
                        bets INT DEFAULT 0,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );


                    CREATE TABLE IF NOT EXISTS tasks (
                        id SERIAL PRIMARY KEY,
                        level_id INT NOT NULL REFERENCES levels(id),
                        title VARCHAR(30) NOT NULL,
                        max_score INT NOT NULL,
                        task_order INT NOT NULL
                    );


                    CREATE TABLE IF NOT EXISTS user_levels (
                        id SERIAL PRIMARY KEY,
                        user_id INT NOT NULL REFERENCES users(id),
                        level_id INT NOT NULL REFERENCES levels(id),
                        achieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        UNIQUE(user_id, level_id)
                    );


                    CREATE TABLE IF NOT EXISTS user_tasks (
                        id SERIAL PRIMARY KEY,
                        user_id INT NOT NULL REFERENCES users(id),
                        task_id INT NOT NULL REFERENCES tasks(id),
                        score INT DEFAULT 0,
                        completed BOOLEAN DEFAULT FALSE,
                        completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                            
                    CREATE TABLE IF NOT EXISTS items (
                        id SERIAL PRIMARY KEY,
                        type VARCHAR(30) CHECK (type IN (
                            'achievements', 'items')),
                        category VARCHAR(30) NOT NULL,
                        name VARCHAR(35) NOT NULL,
                        rarity VARCHAR(20) CHECK (rarity IN (
                            'comum', 'raro', 'epico', 'lendario')),
                        amount_uses INT NOT NULL DEFAULT 1, 
                        description TEXT NOT NULL
                    );
                            

                    CREATE TABLE IF NOT EXISTS vaults (
                        id SERIAL PRIMARY KEY,
                        user_id INT NOT NULL REFERENCES users(id),
                        items_id INT NOT NULL REFERENCES items(id),
                        achieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                            
                    CREATE TABLE IF NOT EXISTS bag (
                        id SERIAL PRIMARY KEY,
                        user_id INT NOT NULL REFERENCES users(id),
                        items_id INT NOT NULL REFERENCES items(id),
                        achieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                                   
                 """)


            except (Exception, psycopg2.DatabaseError) as error:
                print(error) 



def insert_in_tables():
    with connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                    INSERT INTO levels (name, required_score, order_number)
                    VALUES
                        ('calouro', 200, 1),
                        ('veterano', 500, 2),
                        ('mestre', 1100, 3),
                        ('doutor', 2000, 4),
                        ('chefe_departamento', 3000, 5),
                        ('reitor', 3500, 6);

                    INSERT INTO tasks (level_id, title, max_score, task_order)
                    VALUES
                        (1, 'task_01', 20, 1),
                        (1, 'task_02', 25, 2),
                        (1, 'task_03', 25, 3),
                        (1, 'task_04', 30, 4),
                        (1, 'task_05', 20, 5),
                        (1, 'task_06', 25, 6),
                        (1, 'task_07', 25, 7),
                        (1, 'task_08', 30, 8),
                        (1, 'task_09', 25, 9),
                        (1, 'task_10', 25, 10),

                        (2, 'task_01', 20, 1),
                        (2, 'task_02', 25, 2),
                        (2, 'task_03', 20, 3),
                        (2, 'task_04', 30, 4),
                        (2, 'task_05', 25, 5),
                        (2, 'task_06', 25, 6),
                        (2, 'task_07', 25, 7),
                        (2, 'task_08', 25, 8),
                        (2, 'task_09', 30, 9),
                        (2, 'task_10', 30, 10),
                        (2, 'task_11', 30, 11),
                        (2, 'task_12', 30, 12),
                        (2, 'task_13', 30, 13),
                        (2, 'task_14', 30, 14),
                        (2, 'task_15', 35, 15),
                            
                        (3, 'task_01', 40, 1),
                        (3, 'task_02', 35, 2),
                        (3, 'task_03', 30, 3),
                        (3, 'task_04', 35, 4),
                        (3, 'task_05', 35, 5),
                        (3, 'task_06', 30, 6),
                        (3, 'task_07', 30, 7),
                        (3, 'task_08', 30, 8),
                        (3, 'task_09', 30, 9),
                        (3, 'task_10', 30, 10),
                        (3, 'task_11', 30, 11),
                        (3, 'task_12', 50, 12),
                        (3, 'task_13', 50, 13),
                        (3, 'task_14', 50, 14),
                        (3, 'task_15', 50, 15),
                        (3, 'task_16', 50, 16),
                        (3, 'task_17', 60, 17),
                        (3, 'task_18', 60, 18),
                        (3, 'task_19', 60, 19),
                        (3, 'task_20', 60, 20),
                            
                        (4, 'task_01', 00, 1),
                        (4, 'task_02', 00, 2),
                        (4, 'task_03', 00, 3),
                        (4, 'task_04', 00, 4),
                        (4, 'task_05', 00, 5),
                        (4, 'task_06', 00, 6),
                        (4, 'task_07', 00, 7),
                        (4, 'task_08', 00, 8),
                        (4, 'task_09', 00, 9),
                        (4, 'task_10', 00, 10);
                        
                    
                            
                    INSERT INTO items (type, category, name, rarity, amount_uses, description)
                    VALUES  
                        ('items', 'score', 'atestado médico', 'epico', 1,
                        'Use para não perder pontos em uma task'),
                        ('items', 'score', 'teste1', 'comum', 1,
                        'teste1'),
                        ('items', 'score', 'teste2', 'raro', 1,
                        'teste2'),
                        ('items', 'score', 'teste3', 'lendario', 1,
                        'teste3'),
                        ('achievements', 'objeto', 'Caneta do Reitor', 'lendario', 1,
                        'Caneta perdida pelo Reitor da UFS, vale mais do que você imagina'),
                        ('achievements', 'score', 'teste4', 'comum', 1,
                        'teste'),
                        ('achievements', 'score', 'teste5', 'raro', 1,
                        'teste'),
                        ('achievements', 'score', 'teste6', 'epico', 1,
                        'teste');
                """)


            except (Exception, psycopg2.DatabaseError) as error:
                print(error) 



def delete_tables():
     with connection() as conn:
        with conn.cursor() as cur:
            try: 
                cur.execute("""
                    TRUNCATE TABLE
                        user_tasks,
                        user_levels,
                        tasks,
                        users,
                        levels,
                        items,
                        vaults,
                        bag
                    RESTART IDENTITY CASCADE;
                """)

            except (Exception, psycopg2.DatabaseError) as error:
                print(error)



if __name__ == "__main__":
    # create_tables()
    # insert_in_tables()
    delete_tables()
    ...