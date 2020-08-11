people = [
  {'name': Tom, 'age': 22},
  {'name': Jill, 'age': 18},
  {'name': Alistar, 'age': 28},
 ]
 
 for entry in people.sort(key=lambda person:person['age]'):
    print(entry)
