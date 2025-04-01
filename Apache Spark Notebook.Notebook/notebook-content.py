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

# Welcome to your new notebook
# Type here in the cell editor to add code!


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM BIG_DATA.dbo.dimension_city_1 LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df.write.format("delta").mode("overwrite").saveAsTable("BIG_DATA.dbo.dimension_city_2_delta")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df1 = spark.sql("SELECT CityKey,City,LatestRecordedPopulation FROM BIG_DATA.dbo.dimension_city_2_delta LIMIT 1000")
display(df1)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df1.write.format("delta").mode("overwrite").saveAsTable("BIG_DATA.dbo.Dim2_City")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
