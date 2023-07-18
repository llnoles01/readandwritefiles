import csv

with open("sales.csv","r") as sales:
    read_file = csv.reader(sales)
    next (read_file)

    with open("salesreport.csv","w") as sales_copy:
        write_file = csv.writer(sales_copy)
        write_file.writerow(["Customer ID","|","Total"])

        cust_id = " "
        total = 0

        for row in read_file:
            if row [0] != cust_id:
                if cust_id != " ":
                    write_file.writerow([cust_id,round(total,2)])

                print(row[0])
                print(total)
                total = 0
                cust_id = row[0]
            
            subtotal = float(row[3])
            tax = float (row[4])
            freight = float (row[5])

            final_total = subtotal+tax+freight
            total += final_total

        write_file.writerow([cust_id,round(total,2)])