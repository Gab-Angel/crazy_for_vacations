import psycopg2
from db.conn import connection


def create_user(nick_name: str):
    with connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                    INSERT INTO users (
                        nick_name,
                        current_level_id
                    )   
                    VALUES  (%s, 1)
                    RETURNING id;
                            
                """,
                (nick_name,)
                )

                data = cur.fetchone()
                id = data["id"]

                return id

            except (Exception, psycopg2.DatabaseError) as error:
                conn.rollback()
                raise error


def update_level(user_id: int, level_id: int):
    with connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""    
                            
                    UPDATE users
                    SET current_level_id = %s
                    WHERE id = %s;
                            
                """,
                (level_id, user_id,)
                )

                if cur.rowcount == 0:
                    raise ValueError(f"UPDATE LEVEL: User with id {user_id} not found.")
                
            except psycopg2.errors.ForeignKeyViolation:
                conn.rollback()
                raise ValueError(f"Level with id {level_id} not found.")
            except (Exception, psycopg2.DatabaseError) as error:
                conn.rollback()
                raise error


def update_score(user_id: int, score):
    with connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                            
                    UPDATE users
                    SET total_score = total_score + %s
                    WHERE id = %s;

                """,
                (score, user_id)
                )
                
                if cur.rowcount == 0:
                    raise ValueError(f"UPDATE SCORE: User with id {user_id} not found.")

            except (Exception, psycopg2.DatabaseError) as error:
                conn.rollback()
                raise error


def register_user_tasks(
        user_id: int,
        task_id: int,
        completed: bool = True
    ):
    with connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                    INSERT INTO user_tasks (
                        user_id,
                        task_id,
                        score,
                        completed
                    )
                    SELECT %s,   id,  max_score,  %s
                    FROM tasks
                    WHERE id = %s;
                """,
                (user_id, completed, task_id,)            
                )

                if cur.rowcount == 0:
                    raise ValueError(f"Task with id {task_id} not found.")
                
            except (Exception, psycopg2.DatabaseError) as error:
                conn.rollback()
                raise error


def get_data_user(user_id):
    with connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                    SELECT u.nick_name, l.name AS level_name, u.total_score, u.bets 
                    FROM users u
                    JOIN levels l ON u.current_level_id = l.id
                    WHERE u.id = %s;
                """,
                (user_id,)
                )

                data = cur.fetchone()

                if data is None:
                    raise ValueError(f"User with id {user_id} not found.")

                return data

            except (Exception, psycopg2.DatabaseError) as error:
                conn.rollback()
                raise error


def update_user_bets(user_id: int, bets: int):
    with connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                    UPDATE users
                    SET bets = bets + %s
                    WHERE id = %s
                """,
                (bets, user_id,)   
                )

                if cur.rowcount == 0:
                    raise ValueError(f"UPDATE USER BETS: User with id {user_id} not found.")

            except (Exception, psycopg2.DatabaseError) as error:
                conn.rollback()
                raise error


def get_random_items(rarity):
    with connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                    SELECT * FROM items
                    WHERE rarity = %s
                    ORDER BY RANDOM()
                    LIMIT 1;
                """,
                (rarity,)            
                )
                
                item = cur.fetchone()

                if item is None:
                    raise ValueError(f"Item not found.")

                return item

            except (Exception, psycopg2.DatabaseError) as error:
                conn.rollback()
                raise error


def insert_item_vaults(items_id: int, user_id: int):
    with connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                    INSERT INTO vaults (user_id, items_id)
                    VALUES  (%s, %s);
                """,
                (user_id, items_id,)            
                )

                if cur.rowcount == 0:
                    raise ValueError(f"Error inserting item into vault.")
                
            except (Exception, psycopg2.DatabaseError) as error:
                conn.rollback()
                raise error
    

def insert_item_bag(items_id: int, user_id: int):
    with connection() as conn:
        with conn.cursor() as cur:
            try:
                cur.execute("""
                    INSERT INTO bag (user_id, items_id)
                    VALUES  (%s, %s);
                """,
                (user_id, items_id,)            
                )

                if cur.rowcount == 0:
                    raise ValueError(f"Error inserting item into bag.")
                
            except (Exception, psycopg2.DatabaseError) as error:
                conn.rollback()
                raise error


if __name__ == "__main__":
    create_user('angel')
    # update_level(5, 1)
    # update_score(5, 100)
    # register_user_tasks(1, 7)
    # print(get_data_user(2))
    # update_user_bets(1, -50)
    
    ...