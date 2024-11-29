# Stwórz bazę danych i tabele podstawowe
import mysql.connector as con

db = con.connect(
    host="localhost",
    user="test",
    password="test",
    database="uczelnia"
)

cursor = db.cursor(buffered=True)
print(cursor)

cursor.execute("SHOW DATABASES")
for e in cursor:
    print(e)

# SHOW TABLES
cursor.execute("SHOW TABLES")
print(cursor)
for e in cursor:
    print(e)

# W bazie danych `uczelnia` utwórz następujące tabele z podanymi kolumnami:
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Studenci (student_id INT, imie VARCHAR(50), nazwisko VARCHAR(50), wiek INT, miasto VARCHAR(50))")
print(cursor)
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Kursy (kurs_id INT, nazwa_kursu VARCHAR(100), wydzial_id INT, prowadzacy_id INT)")
print(cursor)
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Wydzialy (wydzial_id INT, nazwa_wydzialu VARCHAR(100), dziekan VARCHAR(50), lokalizacja VARCHAR(100))")
print(cursor)
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Prowadzacy (prowadzacy_id INT, imie VARCHAR(50), nazwisko VARCHAR(50), tytul VARCHAR(50), wydzial_id INT)")
print(cursor)
cursor.execute(
    "CREATE TABLE IF NOT EXISTS Oceny (ocena_id  INT, student_id  INT, kurs_id  INT, ocena DECIMAL(3,2), data_oceny DATE)")
print(cursor)
cursor.execute("CREATE TABLE IF NOT EXISTS Przedmioty (przedmiot_id INT, nazwa_przedmiotu VARCHAR(100), kurs_id INT)")
print(cursor)
# 3. Dodaj dane testowe.
Studenci = [
    ("Oleksandr", "Kovalenko", 21, "Poznan"),
    ("Tetiana", "Vakulenko", 22, "Warszawa"),
    ("Kateryna", "Shewchenko", 21, "Kyiv"),
    ("Olena", "Chajkovska", 22, "Lviv"),
    ("Dmytro", "Lubchenko", 21, "Kharkov"),
]
cursor.executemany(sql, Studenci)
print("Studenci zostali dodani: ", cursor.lastrowid)
