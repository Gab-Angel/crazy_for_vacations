# AS TABELAS QUE PRECISAM SER CRIADAS AUTOMATICAMENTE
import psycopg2.extras
from db.conn import connection



def create_tables():
    with connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS users (
                        id SERIAL PRIMARY KEY,
                        nick_name VARCHAR(30) NOT NULL,
                        current_level_id INT,
                        total_score INT NOT NULL,
                        bets INT NOT NULL,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                            

                    CREATE TABLE IF NOT EXISTS levels (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(20) NOT NULL,
                        required_score INT NOT NULL,
                        order_number INT NOT NULL,
                    );
                            

                    INSERT INTO levels (name, required_score, order_number)
                    VALUES  ('calouro', 100, 1),
                            ('veterano', 200, 2),
                            ('mestre', 300, 3),
                            ('doutor', 400, 4),
                            ('chefe_departamento', 500, 5),
                            ('reitor', 600, 6)


                    CREATE TABLE IF NOT EXISTS user_tasks (
                        id SERIAL PRIMARY KEY,  
                        user_id INT FOREIGN KEY (user_id) REFERENCES users(id),
                        task_id INT FOREIGN KEY (task_id) REFERENCES tasks(id),
                        score INT NOT NULL,
                        completed BOOL NOT NULL,
                        completed_at TIMESTAMP DEFAUL CURRENT_TIMESTAMP
                    );
                             
                            
                    CREATE TABLE IF NOT EXISTS user_levels(
                        id SERIAL PRIMARY KEY,  
                        user_id FOREIGN KEY (user_id) REFERENCES users(id),
                        level_id FOREIGN KEY (level_id) REFERENCES levels(id),
                        achieved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                    

                    CREATE TABLE IF NOT EXISTS tasks(
                        id SERIAL PRIMARY KEY,  
                        level_id FOREIGN KEY (level_id) REFERENCES levels(id),
                        title VARCHAR(30) NOT NULL
                        max_score INT NOT NULL,
                        task_order INT NOT NULL,
                    );
                            

                    INSERT INTO tasks (level_id, title, max_score, task_order)
                    VALUES  (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),
                            (),       
                """)


            except (Exception, psycopg2.DatabaseError) as error:
                print(error)