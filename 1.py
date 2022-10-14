st_name = input('имя студента:')
st_surname = input('фамилия студента:')
st_date_of_birth = int(input('год рождения студента:'))
print('Имя:',st_name,'Фамилия:', st_surname,'Год рождения:', st_date_of_birth)
b = st_surname
a = st_name
st_name = b
st_surname = a
st_date_of_birth = st_date_of_birth+60
print('Фамилия:',st_name,'Имя:', st_surname, 'Год рождения:',st_date_of_birth)
