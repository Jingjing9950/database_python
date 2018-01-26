import sqlite3
import csv
#Create a in_memorty database by using sqlite3
#create a table called "sales" with 4 attributes
con = sqlite3.connect(r'C:\Users\jingjing\Desktop\Suppliers.db')
c = con.cursor()
creat_table = """ CREATE TABLE IF NOT EXISTS Suppliers
            (Supplier Name VARCHAR(20),
            Invoice Number VARCHAR(40),
            Part Number VARCHAR(20),
            Cost FLOAT,
            Purchase Date DATE);
            """

c.execute(creat_table)
con.commit() #always have to use commit() method to save changes, like github


#Insert / add records in the table "sales"
input_file = csv.reader(open('supplier.csv', 'r'), delimiter = ",")
header = next(input_file)
for rows in input_file:
    data = []
    for row_index in range(len(rows)):
        data.append(rows[row_index])
    c.execute("INSERT INTO Suppliers VALUES(?,?,?,?,?)", data)

con.commit()


#Query the sales table all
read_table = con.execute("SELECT * FROM Suppliers")
rows_list = read_table.fetchall()

#count the number of rows in the output
row_counter = 0
for row in rows_list:
    print(row)
    row_counter += 1

print("Number of rows : %d" % (row_counter))