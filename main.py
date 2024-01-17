import moduls.Courses
import moduls.Students
import moduls.Database_manager
from moduls.Database_manager import DatabaseManager



if __name__ == '__main__':
    db_host = 'localhost'
    db_user = 'root'
    db_passwd = 'Javohir2002+'
    db_name = 'library'

    db_manager = DatabaseManager(host=db_host, user=db_user, passwd=db_passwd, database=db_name)

    cursor = db_manager.cursor
    query = """CREATE TABLE IF NOT EXISTS students 
                (student_id INT AUTO_INCREAMENT PRIMARY KEY,
                name VARCHAR(25),
                email VARCHAR(25),
                enrolled_cou

    )

    """
    cursor.fetchall()

