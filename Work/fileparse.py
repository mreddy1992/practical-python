# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=None, silence_errors=True):
	'''
	Parse a CSV file into a list of records
	'''
	if select and not has_headers:
		raise RuntimeError("select argument requires column headers")

	with open(filename) as f:
		# use delimiter as an argument
		if not delimiter:
			rows = csv.reader(f)
		else:
			rows = csv.reader(f, delimiter = delimiter)

		# If the file has headers, read the file headers
		if has_headers:
			headers = next(rows)

		# If a column selector is given, find indices of the speicified columns.
		# Also narrow the set of headers used for resulting dictionaries
		if select:
			indices = [headers.index(colname) for colname in select]
			headers = select
		else:
			indices = []

		records = []
		for row_index, row in enumerate(rows):
			if not row:
				continue
			# Filter the row if specific columns were selected
			if indices:
				row = [row[index] for index in indices]

			# Perform type conversion if types is given
			if types:
				try:
					row = [func(val) for func, val in zip(types, row)]
					# Make a dictionary if the input file has headers
					if has_headers:
						record = dict(zip(headers, row))
						records.append(record)
					else:
						records.append(tuple(row))
				except ValueError as e:
					if not silence_errors:
						print(f'Row {row_index+1}: Coulnot convert {row}')
						print(f'Row {row_index+1}: Reason {e}')

			
	return records

