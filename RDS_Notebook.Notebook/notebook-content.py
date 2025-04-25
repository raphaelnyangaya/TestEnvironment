# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "104bbd2e-02ef-4389-a650-166fadd98460",
# META       "default_lakehouse_name": "RDS_Retail_Solution1_LH_silver",
# META       "default_lakehouse_workspace_id": "17865aab-61cf-48c0-aec0-4320f4200b00",
# META       "known_lakehouses": [
# META         {
# META           "id": "104bbd2e-02ef-4389-a650-166fadd98460"
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

df = spark.read.format("csv").option("header","true").load("Files/TEST_V1.csv")
# df now is a Spark DataFrame containing CSV data from "Files/TEST_V1.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

delta_table_path = "abfss://17865aab-61cf-48c0-aec0-4320f4200b00@onelake.dfs.fabric.microsoft.com/104bbd2e-02ef-4389-a650-166fadd98460/Tables/AttendanceStatus" 
df.write.format("delta").mode("overwrite").option("mergeSchema", "true").save(delta_table_path)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("SELECT * FROM AttendanceStatus LIMIT 1000")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.table("AttendanceStatus")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from pyspark.sql.functions import lit

# Example: add a column with default value
df_new = df.withColumn("CreatedDate", lit("default_value"))

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df_new.write.mode("overwrite").option("overwriteSchema", "true").saveAsTable("AttendanceStatus")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.sql("""SELECT * FROM AttendanceStatus
where CreatedDate=(select max(CreatedDate) from AttendanceStatus)
""")
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
