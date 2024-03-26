import psycopg2

conn = psycopg2.connect(
    dbname="by1wvfyyi5kgu1euhyko",
    user="u1ai5zsuzpe6y74uwyqu",
    password="0BacMZwIRVg5rpsOcndFG1pcHSUba5",
    host="by1wvfyyi5kgu1euhyko-postgresql.services.clever-cloud.com",
    port="50013"
)
print(conn)

cursor = conn.cursor()
print(cursor)
#
# cursor.execute("SELECT * FROM authors")
# autori = cursor.fetchall()
# print(autori)
#
# cursor.execute("SELECT * FROM authors")
# prvy_autor = cursor.fetchone()
# print(prvy_autor)
#
# cursor.execute("SELECT * FROM authors ORDER by author_id DESC")
# posledny_autor = cursor.fetchone()
#
# print(posledny_autor)

# cursor.close()
# conn.close()
#
# cursor.execute("SELECT * FROM authors")
# prvy_autor = cursor.fetchone()
#
# print(prvy_autor)
#
# nejaky_autor = Autor(prvy_autor[0], prvy_autor[1], prvy_autor[2])
# print(nejaky_autor)

# author1 = Author(1, "Jan", "najlepsi autor")
# print(author1)

# cursor = conn.cursor()
#
# cursor.execute("Select * from books where publication_year > %s AND publication_year < %s", (1900, 1950))
# knihy = cursor.fetchall()
#
# print(knihy)
#
# cursor.close()
# conn.close()

# Vypíšte názvy všetkých kníh zo žánru Fantasy. Použite JOIN a Fantasy zadajte
# ako parameter
#
# cursor = conn.cursor()
#
# cursor.execute("SELECT b.title FROM books b inner join genres g on g.genre_id = b.genre_id where g.name = %s", ("Fantasy", ))
# knihy = cursor.fetchall()
#
# print(knihy)
#
# cursor.close()
# conn.close()

# Pridanie clena do databazy:

# cursor = conn.cursor()
#
# first_name = "Patrik"
# last_name = "Dendis"
# email = "patrik@dendis.sk"
#
# cursor.execute("""
# INSERT INTO members (first_name, last_name, email)
# VALUES(%s, %s, %s)
# """, (first_name, last_name, email))
#
# conn.commit()
#
# print("Novy clen bol uspesne pridany.")
#
# cursor.close()
# conn.close()

# Vložte aspoň 3 reálne knihy do databázy aj s autormi:

cursor = conn.cursor()

name = "Jo Nesbo"
bio = "severske detektivky"

cursor.execute(""
INSERT INTO authors (name, bio)
VALUES(%s, %s)
"", (name, bio))

conn.commit()

print("Novy autor bol uspesne pridany.")







