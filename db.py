import sqlite3

DB_PATH=('emails.db')


def get_connection():
    return sqlite3.connect(DB_PATH)


def db_init():
    conn=get_connection()
    cursor=conn.cursor()




    cursor.execute(

        '''
        CREATE TABLE IF NOT EXISTS `inbox`(
        `id`  INTEGER PRIMARY KEY,
        `email` TEXT,
        `sender` TEXT,
        `receipient` TEXT,
        `date` TIMESTAMP
        )
        '''
    )


if __name__ =='__main__':
    db_init()