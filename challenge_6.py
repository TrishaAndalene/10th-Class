'''
[1] Buat 3 dictionary, simpan ke list nama variabel people, keynya harus sm valuenya terserah, key nya min 2, print semuanya cuman jangan ada list atau dictionarynya kayak di 47_alien
[2] buat dictionary dengan variabel cities, minimal ada 2, buatin dictionary untuk tiap kotanya misalnya ibukota dan funfact, cetak semuanya tp jangan keliatan dictionarynya
[3] buat dictionary obat2an, nama obatnya jadi key, buat dictionary di dalamnya untuk simpen informasi terkait kegunaan obatnya, harga, dan efek samping. untuk info efek samping itu harus 2 atau list. Cetak semua informasi tentang obat2an nya
'''

#[1]
person_0 = {'name' : 'Asla', 'age' : 10, 'occupation' : 'student'}
person_1 = {'name' : 'Vnev', 'age' : 23, 'occupation' : 'college student'}
person_2 = {'name' : 'Ciel', 'age' : 29, 'occupation' : 'doctor'}

people = [person_0, person_1, person_2]

for person in people:
	print(f"\n{person['name'].title()}")
	age = person['age']
	occupation = person['occupation']
	print(f"- Age : {age}")
	print(f"- Occupation : {occupation}")

#[2]
cities = {
	'China' : {
		'landmark' : 'great wall of China',
		'fun fact' : 'A country with the most population'
	},
	'Paris' : {
		'landmark' : 'Eiffel Tower',
		'fun fact' : 'Paris is known for its superiority in fashion'
	},
	'Australia' : {
		'landmark' : 'Sydney Opera House',
		'fun fact' : 'Australia is the country and the continent itself'
	}
}

for key, value in cities.items():
	print(f'\n [{key.title()}]')
	landmark = value['landmark'].title()
	funfact = value['fun fact']
	print(f'\tLandmark : {landmark}')
	print(f'\tFun fact : {funfact}')

#[3]
medicines = {
	'paracetamol' : {
		'utility' : 'relieve fever',
		'price' : 10_000,
		'side effects' : ['back pain', 'sore throat', "rash's appearance"] 
	},
	'antihistamine' : {
		'utility' : 'reduce allergies impact',
		'price' : 25_000,
		'side effect' : ['dizziness', 'headache', 'stomache']
	},
	'mylanta' : {
		'utility' : "treating stomache due to stomach's acid",
		'price' : 15_000,
		'side effect' : ['no appetite', 'nauseous', 'constipation']
	}
}

for medicine, info in medicines.items():

	print(f"\n{medicine.title()}")

	for m_info, data in info.items():

		print(f"\t{m_info}")
		if type(data) == list:
			for item in data:
				print(f"\t\t- {item}")
		else:
			print(f"\t\t- {data}")