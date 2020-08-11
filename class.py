class bill():
    def __init__(self):
        self.total = 0
        self.items = []


nightout = bill()

eaten = {'tacos': 6, 'pizza': 8, 'beer': 12}

for entry in eaten.keys():
    nightout.items.append(entry)
    nightout.total += eaten[entry]

print('You ate: ')
for item in sorted(nightout.items):
    print(item)
print(f'Your total is ${nightout.total}')