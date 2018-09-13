def build_person(first_name, last_name, age = ''):
	""" Return a person in dictionary format"""
	person = {'first':first_name, 'last':last_name, 'age':age}
	return person

musician = build_person('mauli','prakash','40')
print musician
