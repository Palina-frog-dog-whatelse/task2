age_of_exhib = int(input('количество лет, проведенных в музее:'))
amount_of_exhibs = int(input('количество экспонатов:'))
age_of_exhib = int(age_of_exhib*365*24*60/5)
amount_of_exhibs_year = int(amount_of_exhibs*5/60/24/365)
amount_of_exhibs_day = int(amount_of_exhibs*5/60/24)
amount_of_exhibs_min = int(amount_of_exhibs*5)
print('экспонатов будет просмотрено',age_of_exhib)
print('лет будет потрачена на простмотр', amount_of_exhibs_year)
print('дней будет потрачена на простмотр', amount_of_exhibs_day)
print('дней будет потрачена на простмотр', amount_of_exhibs_min)



