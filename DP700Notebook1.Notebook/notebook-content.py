# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "d8f78a60-53eb-479b-8b35-7db20c9e3cd6",
# META       "default_lakehouse_name": "BIG_DATA",
# META       "default_lakehouse_workspace_id": "17865aab-61cf-48c0-aec0-4320f4200b00",
# META       "known_lakehouses": [
# META         {
# META           "id": "d8f78a60-53eb-479b-8b35-7db20c9e3cd6"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# Reading data from files

# CELL ********************

df=spark.read.format("csv").option("header","true").load("Files/new_data/Sales.csv")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.createOrReplaceTempView("df1")
df2=spark.sql('''select * from df1''')


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC select * from df1

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
