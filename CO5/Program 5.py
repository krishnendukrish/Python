import csv
f = open("fruits.csv","w")
writer = csv.DictWriter(f,fieldnames=["Fruit", "Count"])
writer.writeheader()
writer.writerow({"Fruit":"Apple", "Count":"1"})
writer.writerow({"Fruit":"Banana", "Count":"2"})
f.close()
c = 0
f = open("fruits.csv")
reader = csv.DictReader(f)
for row in reader:
  if c == 0:
    print(f'{"".join(row)}')
    print(f'{row["Fruit"]},{row["Count"]}')
f.close()
