import sqlite3

#Create a in_memorty database by using sqlite3
#create a table called "sales" with 4 attributes
con = sqlite3.connect(r'C:\Users\jingjing\Desktop\my_database.db')
query = """ CREATE TABLE sales
            (customer VARCHAR(20),
            product VARCHAR(40),
            amount FLOAT,
            date DATA);
            """

con.execute(query)
con.commit() #always have to use commit() method to save changes, like github

#Insert / add records in the table "sales"
data = [('Richard lucas', 'Notepad', 2.50, '2014-01-02'),('Jenny Kim', 'Binder', 4.15, '2014-01-15'),('Svetlana Crow',\
        'Printer', 155.75, '2014-02-03'),('Stephen Randolph','Computer', 679.40, '2014-02-20')]
statement = "INSERT INTO sales VALUES(?,?,?,?)" #? serves as placeholders for values want to use in SQL command
con.executemany(statement, data)
con.commit()

#Query the sales table all
concur = con.execute("SELECT * FROM sales")
rows = concur.fetchall()

#count the number of rows in the output
row_counter = 0
for row in rows:
    print(row)
    row_counter += 1

print("Number of rows : %d" % (row_counter))