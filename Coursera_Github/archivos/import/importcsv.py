import csv
a_list = ['Pedro', 'Florencia', 'Matías', 'Jorge', 'María', 'Inés']
with open('E:\\123.csv', 'a') as csvfile:
	writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE, quotechar='|', doublequote=False)
	writer.writerows(a_list)