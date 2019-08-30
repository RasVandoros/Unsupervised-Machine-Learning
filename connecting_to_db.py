import psycopg2

# Connect to an existing database
connection = psycopg2.connect(host="htgt-db", port="5441", dbname="lims2_local_gv3", user="lims2", password="team87", sslmode='require')

# Open a cursor to perform database operations
cur = conn.cursor()

# Close communication with the database
cur.close()
conn.close()
