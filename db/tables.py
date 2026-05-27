# AS TABELAS QUE PRECISAM SER CRIADAS AUTOMATICAMENTE
import psycopg2.extras
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


                    INSERT INTO levels (name, required_score, order_number)
                    VALUES
                        ('calouro', 100, 1),
                        ('veterano', 200, 2),
                        ('mestre', 300, 3),
                        ('doutor', 400, 4),
                        ('chefe_departamento', 500, 5),
                        ('reitor', 600, 6);

                    INSERT INTO tasks (level_id, title, max_score, task_order)
                    VALUES
                        (1, task_01, 00, 1),
                        (1, task_02, 00, 2),
                        (1, task_03, 00, 3),
                        (1, task_04, 00, 4),
                        (1, task_05, 00, 5),
                        (1, task_06, 00, 6),
                        (1, task_07, 00, 7),
                        (1, task_08, 00, 8),
                        (1, task_09, 00, 9),
                        (1, task_10, 00, 10),

                        (2, task_01, 00, 1),
                        (2, task_02, 00, 2),
                        (2, task_03, 00, 3),
                        (2, task_04, 00, 4),
                        (2, task_05, 00, 5),
                        (2, task_06, 00, 6),
                        (2, task_07, 00, 7),
                        (2, task_08, 00, 8),
                        (2, task_09, 00, 9),
                        (2, task_10, 00, 10),
                            
                        (3, task_01, 00, 1),
                        (3, task_02, 00, 2),
                        (3, task_03, 00, 3),
                        (3, task_04, 00, 4),
                        (3, task_05, 00, 5),
                        (3, task_06, 00, 6),
                        (3, task_07, 00, 7),
                        (3, task_08, 00, 8),
                        (3, task_09, 00, 9),
                        (3, task_10, 00, 10),
                            
                        (4, task_01, 00, 1),
                        (4, task_02, 00, 2),
                        (4, task_03, 00, 3),
                        (4, task_04, 00, 4),
                        (4, task_05, 00, 5),
                        (4, task_06, 00, 6),
                        (4, task_07, 00, 7),
                        (4, task_08, 00, 8),
                        (4, task_09, 00, 9),
                        (4, task_10, 00, 10),
                        
                        
                """)


            except (Exception, psycopg2.DatabaseError) as error:
                print(error) 

if __name__ == "__main__":
    create_tables()