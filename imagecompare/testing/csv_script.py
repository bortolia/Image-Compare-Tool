import csv

with open('file.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	file_header = next(csv_reader)

	#for row in csv_reader:
	#	print(row)

	file_header.append('similar')
	file_header.append('elapsed')

	with open('new_file.csv', 'w') as new_file:
		csv_writer = csv.writer(new_file)

		csv_writer.writerow(file_header)

		for row in csv_reader:
			row.append(0)
			row.append(0.5)
			csv_writer.writerow(row)

