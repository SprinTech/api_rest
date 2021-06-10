import mysql.connector
from sql_authentification import host, user, password

# Create connexion to database
mydb = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database='API_REST'
)

mycursor = mydb.cursor()

# mycursor.execute("SHOW TABLES")

# Create tables
create_tables = False

if create_tables:
    mycursor.execute("""
                     CREATE TABLE Client (
                     id_client INT AUTO_INCREMENT PRIMARY KEY,
                     nom VARCHAR(40) NOT NULL,
                     prenom VARCHAR(40) NOT NULL,
                     mail VARCHAR(255) NOT NULL,
                     telephone VARCHAR(10) NOT NULL)
                     """
                     )

    # Create Message table
    mycursor.execute("""
                     CREATE TABLE Message (
                     id_message INT AUTO_INCREMENT PRIMARY KEY,
                     id_client INT,
                     date DATE,
                     message VARCHAR(120) NOT NULL,
                     sentiment VARCHAR(40) NOT NULL,
                     heureux DECIMAL(5, 4) NOT NULL,
                     surprise DECIMAL(5, 4) NOT NULL,
                     peur DECIMAL(5, 4) NOT NULL,
                     dégoût DECIMAL(5, 4) NOT NULL,
                     colère DECIMAL(5, 4) NOT NULL,
                     tristesse DECIMAL(5, 4) NOT NULL,
                     CONSTRAINT FK_ClientMessage FOREIGN KEY (id_client)
                     REFERENCES Client(id_client))
                     """
                     )

# Create some fictive clients
add_clients = False

if add_clients:
    mycursor.execute("""
                        INSERT INTO API_REST.Client (nom, prenom, mail, telephone)
                        VALUES
                        ('Jacques', 'Dutronc', 'j.dutronc@gmail.com', '0612345678'),
                        ('Melissa', 'Lelieu', 'm.lelieu@gmail.com', '0687562987'),
                        ('Lise', 'Dulilas', 'l.dulilas@gmail.com', '0687235369'),
                        ('Henry', 'Fabre', 'h.fabre@gmail.com', '0679388916'),
                        ('Camille', 'Fleuri', 'c.fleuri@gmail.com', '0735966354');
                    """
                     )
    # Commit change
    mydb.commit()

mycursor.execute("""SELECT * FROM API_REST.Client""")
