import csv
with open("movie.csv", "w",newline='') as file:
 write = csv.writer(file)
 write.writerow(["Sl No", "Movie", "Rating"])
 write.writerow(["1", "Twilight", "3"])
 write.writerow(["2", "Loard of Rings", "2"])
with open("movie.csv") as csvfile:
 data = csv.DictReader(csvfile)
 for r in data:
   print(r['Sl No'], r['Movie'])
