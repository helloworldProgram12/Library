import mysql.connector
con=mysql.connector.connect(
   host="localhost",
   username="root",
   password="WJ28@krhps",
   database="Library"
)

crsr=con.cursor()