people = [
  {'name': 'Tom', 'age': 22},
  {'name': 'Jill', 'age': 18},
  {'name': 'Alistar', 'age': 28},
 ]
 
people.sort(key=lambda person:person['age'])
for entry in people:
  print(entry)
