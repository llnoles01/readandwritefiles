import csv

with open ("customers.csv","r") as customers:
    read_file = csv.reader(customers)

    with open("customer_country.csv","w") as customers_copy:
        write_file = csv.writer(customers_copy)

        for column in read_file:
            write_file.writerow((column[1],column[2],column[4]))
