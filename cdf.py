# -*- coding: utf-8 -*-

import sys
import json
import datetime

file=open(sys.argv[1])
entrades=json.load(file)

li_names=[]
li_dates_course=[]

#Funcion para hacer el split de los argumentos y sacar el date time
#primer argumento el fichero, segundo argumento fecha de inicio mooc
# YYYY-MM-DD y tercer argumento fecha finalización mooc YYYY-MM-DD
def split_date(s_date):
	li_s_date = []
	li_s_date = s_date.split('-')

	year = int (li_s_date[0])
	month = int (li_s_date[1])
	day = int (li_s_date[2])
	date = datetime.date(year,month,day)
		
	return date

#Funcion para calcular los dias de duración del curso,
#almacenamos cada dia en la lista li_dates, luego utilizaremos la lista
#para compararla con los dias de conexion de los estudiantes
def calculate_dates_course (date1, date2):
	day = datetime.timedelta (days=1)

	while date1 <= date2:
		li_dates_course.append(date1)
		date1 = date1 +day
	
	return

#Funcion para calcular el nombre de todos los estudiantes
#no insertamos los estudiantes repetidos
def name_students():
	for t in entrades:
		if len(t)>0:
			if t['username'] not in li_names:
  				li_names.append(t['username']);

  
	li_names.remove("staff")
	li_names.remove("")
	li_names.remove("admin")

	return

#Funcion para calcular los dias que el estudiante ha hecho MOOC.
def calculate_dates_user():
	for line in entrades:
		if len(line)>0:
			if line['username']==name:
				times_name=[]
				one_date=[]
				times_name = line['time'].split('T')
				one_date = times_name[0].split('-')
				year = int(one_date[0])
				month = int(one_date[1])
				day = int(one_date[2])
				date=datetime.date(year,month,day)
				if date not in li_dates_user:
					li_dates_user.append(date)
	return

#Funcion calculo CDF
def cdf_user(i):
	if date in li_dates_user:
		i=i+1
		print i,
		
	else:
		print i,
		
	return i


s1_date=sys.argv[2]
s2_date=sys.argv[3]

date1=split_date(s1_date)
date2=split_date(s2_date)

calculate_dates_course(date1, date2)

name_students()

for name in li_names:
	li_dates_user=[]
	calculate_dates_user()
	i=0
	for date in li_dates_course:
		i=cdf_user(i)

	print("")
	print("")
