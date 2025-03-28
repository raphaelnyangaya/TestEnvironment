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

# CELL ********************

# MAGIC %%pyspark
# MAGIC df=spark.read.load('Files/new_data/Sales.csv',format='csv',header=True)
# MAGIC display(df.limit(20))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

TaxCharged=df.select("CustomerName","TaxAmount").where(df["CustomerName"]=="Melanie Sanchez").groupBy("CustomerName").count()
display(TaxCharged)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

TaxCharged.write.mode("overwrite").parquet('Files/new_data/Sales3.csv')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df2=spark.read.parquet('Files/new_data/Sales2.parquet/part-00000-47bb84dd-6f8d-4668-9d8e-46118f9ffafe-c000.snappy.parquet')
display(df2)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.createOrReplaceTempView('Twenty')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.write.format('delta').saveAsTable('Sales3')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_sales3=spark.sql("SELECT * from Sales3 ")
display(df_sales3.limit(10))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC SELECT * from Sales3 where item='Half-Finger Gloves, L'

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from matplotlib import pyplot as plt
data = spark.sql("""
    SELECT item, COUNT(salesordernumber) AS ItemCount 
    FROM sales3  
    GROUP BY item  
    ORDER BY ItemCount DESC 
    LIMIT 10
""").toPandas()
plt.clf()
fig=plt.figure(figsize=(12,8))
plt.bar(x=["item"],height=data["ItemCount"],color='orange')
plt.xlabel("Item")
plt.ylabel("Count")
plt.title("Top 10 Items by Order Count")
plt.xticks(rotation=45)  # Rotate labels if needed
plt.show()




# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC 
# MAGIC DESCRIBE HISTORY Sales

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }
