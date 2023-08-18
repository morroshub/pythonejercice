# Alive by year


'''' 1 - Devuelva un listado que tenga todos los años desde el 1999 hasta el año actual y que diga cuantas personas estuvieron
 vivas en cada año. Ejemplo: 
 
 {
	"1999" : 18,
	"2000" : 15, 
	...
}

 '''


import datetime

List_Usuarios = [{"Name":"Triston Mcgrath","Dates":{"birth":"1913-05-10","death":"1919-02-19"}},{"Name":"Savion Fritz","Dates":{"birth":"1962-05-06","death":"1985-11-08"}},{"Name":"Anabel Duran","Dates":{"birth":"1958-04-18","death":"1989-11-14"}},{"Name":"Johan Potter","Dates":{"birth":"1982-05-10","death":"1995-03-01"}},{"Name":"Eden Bridges","Dates":{"birth":"1936-09-12","death":"1956-01-28"}},{"Name":"Armani Heath","Dates":{"birth":"1946-03-26","death":"1978-05-05"}},{"Name":"Dwayne Bird","Dates":{"birth":"1963-11-21","death":"1977-03-24"}},{"Name":"Isis Sanchez","Dates":{"birth":"1921-07-14","death":"1972-08-12"}},{"Name":"Jaiden Guzman","Dates":{"birth":"1926-10-28","death":"1933-11-06"}},{"Name":"Giana Golden","Dates":{"birth":"1960-01-30","death":"1979-10-12"}},{"Name":"Jaylene Casey","Dates":{"birth":"1943-12-11","death":"1947-01-28"}},{"Name":"Helena Khan","Dates":{"birth":"1942-05-13","death":"1967-12-29"}},{"Name":"Brooklynn Costa","Dates":{"birth":"1920-10-24","death":"1977-04-18"}},{"Name":"Catherine Moon","Dates":{"birth":"1910-08-22","death":"1933-04-21"}},{"Name":"Jaqueline Christensen","Dates":{"birth":"1919-03-19","death":"1987-08-17"}},{"Name":"Raiden Hatfield","Dates":{"birth":"1909-09-20","death":"1923-06-15"}},{"Name":"Abril Day","Dates":{"birth":"1918-12-11","death":"1969-03-18"}},{"Name":"Jaylen Santos","Dates":{"birth":"1923-08-02","death":"1967-02-10"}},{"Name":"Makai Potter","Dates":{"birth":"1962-09-21","death":"1988-04-01"}},{"Name":"Vance Pierce","Dates":{"birth":"1996-08-01","death":"1998-02-06"}},{"Name":"Jason Manning","Dates":{"birth":"1912-07-06","death":"1950-10-09"}},{"Name":"Emmett Moss","Dates":{"birth":"1953-10-28","death":"1984-09-12"}},{"Name":"Kianna Gilbert","Dates":{"birth":"1914-04-19","death":"1965-04-23"}},{"Name":"Charity Austin","Dates":{"birth":"1959-09-03","death":"1971-01-22"}},{"Name":"Orlando Pena","Dates":{"birth":"1987-10-09","death":"1995-09-12"}},{"Name":"Bryson Sheppard","Dates":{"birth":"1946-07-28","death":"1972-11-25"}},{"Name":"Haylie Zimmerman","Dates":{"birth":"1900-10-10","death":"1959-02-11"}},{"Name":"Lorena Cummings","Dates":{"birth":"1969-05-30","death":"1969-08-04"}},{"Name":"America Gilbert","Dates":{"birth":"1943-06-30","death":"1951-02-22"}},{"Name":"Gordon Bell","Dates":{"birth":"1941-07-13","death":"1980-12-31"}},{"Name":"Annabelle Hull","Dates":{"birth":"1956-07-27","death":"1984-07-11"}},{"Name":"Elsie Hanson","Dates":{"birth":"1936-11-12","death":"1994-09-23"}},{"Name":"Aiden Stanley","Dates":{"birth":"1926-12-25","death":"1954-11-21"}},{"Name":"Miley Bond","Dates":{"birth":"1927-04-17","death":"1994-09-05"}},{"Name":"Nikolas Ochoa","Dates":{"birth":"1910-02-12","death":"1997-12-13"}},{"Name":"Elise Robertson","Dates":{"birth":"1964-02-06","death":"1984-05-12"}},{"Name":"Winston Burns","Dates":{"birth":"1935-09-30","death":"1983-03-13"}},{"Name":"Vanessa Mcpherson","Dates":{"birth":"1909-04-24","death":"1934-07-25"}},{"Name":"Liberty Escobar","Dates":{"birth":"1983-04-17","death":"1990-02-12"}},{"Name":"Ian Solomon","Dates":{"birth":"1906-07-09","death":"1977-01-19"}},{"Name":"Amir Cunningham","Dates":{"birth":"1906-03-29","death":"1973-08-18"}},{"Name":"Milo Graham","Dates":{"birth":"1914-12-10","death":"1999-11-09"}},{"Name":"Davion Chase","Dates":{"birth":"1946-04-23","death":"1963-02-23"}},{"Name":"Elaina Hanna","Dates":{"birth":"1918-03-03","death":"1964-05-04"}},{"Name":"Nehemiah Roberson","Dates":{"birth":"1997-09-12","death":"1999-08-14"}},{"Name":"Mckenzie Dodson","Dates":{"birth":"1944-10-04","death":"1972-06-09"}},{"Name":"Madyson Graham","Dates":{"birth":"1917-02-07","death":"1921-03-11"}},{"Name":"Heaven Graves","Dates":{"birth":"1940-01-06","death":"1966-03-31"}},{"Name":"Ariel Blackburn","Dates":{"birth":"1916-12-17","death":"1917-10-13"}},{"Name":"Angel Sanford","Dates":{"birth":"1910-06-04","death":"1957-09-20"}},{"Name":"Antony Walters","Dates":{"birth":"1976-05-18","death":"1987-01-02"}},{"Name":"Brooklyn Bullock","Dates":{"birth":"1949-07-23","death":"1997-09-30"}},{"Name":"Marisol Kent","Dates":{"birth":"1903-05-30","death":"1908-10-20"}},{"Name":"Madalyn Avery","Dates":{"birth":"1910-10-30","death":"1975-12-01"}},{"Name":"Justus Bean","Dates":{"birth":"1935-01-11","death":"1991-06-19"}},{"Name":"Sophia Tyler","Dates":{"birth":"1967-11-07","death":"1979-04-18"}},{"Name":"Janiah Brewer","Dates":{"birth":"1935-01-05","death":"1966-06-10"}},{"Name":"Johan Gilmore","Dates":{"birth":"1974-10-05","death":"1982-12-09"}},{"Name":"Evelin Schmidt","Dates":{"birth":"1969-08-02","death":"1994-11-15"}},{"Name":"Antonio Sparks","Dates":{"birth":"1963-11-01","death":"1990-07-22"}},{"Name":"Karson Francis","Dates":{"birth":"1909-02-14","death":"1990-07-20"}},{"Name":"Jaron Hogan","Dates":{"birth":"1912-06-01","death":"1995-01-22"}},{"Name":"Alessandro Le","Dates":{"birth":"1925-07-06","death":"1939-08-09"}},{"Name":"Braelyn Yoder","Dates":{"birth":"1918-08-24","death":"1942-11-29"}},{"Name":"Lexie Duffy","Dates":{"birth":"1943-01-25","death":"1943-03-08"}},{"Name":"Alijah Swanson","Dates":{"birth":"1916-10-13","death":"1973-02-27"}},{"Name":"Emerson Christian","Dates":{"birth":"1925-07-29","death":"1966-08-19"}},{"Name":"Hadassah Bender","Dates":{"birth":"1919-07-08","death":"1929-11-10"}},{"Name":"Gretchen Banks","Dates":{"birth":"1917-03-11","death":"1924-01-28"}},{"Name":"Jaelynn Davies","Dates":{"birth":"1937-07-05","death":"1996-06-12"}},{"Name":"Fernando Kirk","Dates":{"birth":"1952-04-27","death":"1988-06-03"}},{"Name":"Gerardo Salas","Dates":{"birth":"1926-09-15","death":"1964-08-04"}},{"Name":"Rosemary Barber","Dates":{"birth":"1904-08-03","death":"1918-05-29"}},{"Name":"Daniela Austin","Dates":{"birth":"1978-04-27","death":"1986-03-06"}},{"Name":"Landen Holden","Dates":{"birth":"1942-05-06","death":"1957-01-28"}},{"Name":"Conrad West","Dates":{"birth":"1922-11-29","death":"1996-08-28"}},{"Name":"Genevieve Mcfarland","Dates":{"birth":"1926-05-28","death":"1993-11-20"}},{"Name":"Blaine Tapia","Dates":{"birth":"1919-11-15","death":"1977-11-18"}},{"Name":"Humberto Mckee","Dates":{"birth":"1937-02-21","death":"1981-04-27"}},{"Name":"Remington Potts","Dates":{"birth":"1963-10-21","death":"1972-03-27"}},{"Name":"Payton Campbell","Dates":{"birth":"1965-11-22","death":"1992-03-08"}},{"Name":"Marvin Malone","Dates":{"birth":"1932-09-26","death":"1948-05-25"}},{"Name":"Rylee Trujillo","Dates":{"birth":"1906-02-20","death":"1918-04-01"}},{"Name":"Alaina Hays","Dates":{"birth":"1942-04-12","death":"1999-10-22"}},{"Name":"Jermaine Nielsen","Dates":{"birth":"1915-07-02","death":"1944-11-25"}},{"Name":"Allen Alvarado","Dates":{"birth":"1952-05-25","death":"1958-11-13"}},{"Name":"Tianna Sosa","Dates":{"birth":"1953-01-18","death":"1998-06-04"}},{"Name":"Sydney Mathews","Dates":{"birth":"1902-02-17","death":"1911-07-07"}},{"Name":"Lucy Ferrell","Dates":{"birth":"1930-06-21","death":"1982-06-02"}},{"Name":"Porter Mccarty","Dates":{"birth":"1920-12-03","death":"1994-01-04"}},{"Name":"James Pratt","Dates":{"birth":"1956-09-24","death":"1961-04-14"}},{"Name":"Zane Mckenzie","Dates":{"birth":"1976-04-19","death":"1986-02-08"}},{"Name":"Koen Pitts","Dates":{"birth":"1946-05-30","death":"1993-11-15"}},{"Name":"Ivy Murray","Dates":{"birth":"1931-09-09","death":"1946-10-03"}},{"Name":"Nola Lindsey","Dates":{"birth":"1941-08-19","death":"1946-10-05"}},{"Name":"Lyric Downs","Dates":{"birth":"1948-07-16","death":"1986-12-06"}},{"Name":"Danielle Haynes","Dates":{"birth":"1932-08-23","death":"1944-12-15"}},{"Name":"Raegan Love","Dates":{"birth":"1960-02-20","death":"1971-08-14"}},{"Name":"Kristian Cobb","Dates":{"birth":"1955-09-09","death":"1978-04-23"}},{"Name":"Sylvia Clements","Dates":{"birth":"1912-04-09","death":"1946-05-07"}}]

Anio_Actual = datetime.datetime.now().year
Filtro_Anio = 1999


year_count = {}

for year in range(Filtro_Anio, Anio_Actual + 1):
    count = 0
    for Usuario in List_Usuarios:
        birth_year = int(Usuario["Dates"]["birth"][:4])
        death_year = int(Usuario["Dates"]["death"][:4])
        if birth_year <= year <= death_year:
            count += 1
    year_count[str(year)] = count

print(year_count)

'''2 - Pueda recibir por parámetro un año particular y devuelva la cantidad de personas vivas en ese año y sus nombres.
Ejemplo:

{
	"year" : 1990,
	"peopleAlive" : 3,
	"Names": ["John", "Laura", "Bill"]
}'''

def get_eoplep_alive(year):
    people_alive = []
    for user in List_Usuarios:
        birth_year = int(user["Dates"]["birth"][:4])
        death_year = int(user["Dates"]["death"][:4])
        if birth_year <= year <= death_year:
            people_alive.append(user["Name"])
    return people_alive


current_year = datetime.datetime.now().year
year = 1978

people_alive = get_people_alive(year)

result = {
    "year": year,
    "peopleAlive": len(people_alive),
    "Names": people_alive
}

print(result)





