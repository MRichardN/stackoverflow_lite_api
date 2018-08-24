import psycopg2
 
 
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
         """ CREATE TABLE users (
                user_id SERIAL PRIMARY KEY,
                user_name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
                )
        """,
        """
        CREATE TABLE questions (
            question_id SERIAL PRIMARY KEY,
            language VARCHAR(255) NOT NULL,
            ask TEXT NOT NULL,
            user_id INTEGER REFERENCES users (user_id),
            date_posted DATE NOT NULL DEFAULT CURRENT_DATE
            
        )
        """,
        """
        CREATE TABLE answers (
                id SERIAL PRIMARY KEY,
                answer TEXT NOT NULL,
                user_id INTEGER REFERENCES users (user_id),
                question_id INTEGER REFERENCES questions (question_id)
                ON UPDATE CASCADE ON DELETE CASCADE,
                date_posted DATE NOT NULL DEFAULT CURRENT_DATE
        )
        """)
    conn = None
    try:
        # read the connection parameters
        #params = config()
        # connect to the PostgreSQL server
        #conn = psycopg2.connect(**params)
        	
        conn  = psycopg2.connect(host="localhost",database="stackoverflow", user="postgres", password="root")
       # conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            print(command)
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
        print('tables created')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    create_tables()