import csv
import pandas


class CsvReader:
	data = []

	def __init__(self, filepath):
		with open(filepath) as text_data:
			csv_data = csv.DictReader(text_data, delimiter=',')
			for row in csv_data:
				# print('row: ', row)
				self.data.append(row)
		pass

	def return_data_as_objects(self, class_name):
		objects = []
		for row in self.data:
			objects.append(ClassFactory(class_name, row))
		return objects


def ClassFactory(class_name, dictionary):
	return type(class_name, (object,), dictionary)
