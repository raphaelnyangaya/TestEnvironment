# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "jupyter",
# META     "jupyter_kernel_name": "python3.11"
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

table_name = "sales"

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/dimension_customer.csv")
# df now is a Spark DataFrame containing CSV data from "Files/dimension_customer.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

df = spark.read.parquet("Files/yellow_tripdata_2022-01.parquet")
# df now is a Spark DataFrame containing parquet data from "Files/yellow_tripdata_2022-01.parquet".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

from pyspark.sql.functions import *

# Read the new sales data
df = spark.read.format("csv").option("header","true").load("Files/new_data/*.csv")

## Add month and year columns
df = df.withColumn("Year", year(col("OrderDate"))).withColumn("Month", month(col("OrderDate")))

# Derive FirstName and LastName columns
df = df.withColumn("FirstName", split(col("CustomerName"), " ").getItem(0)).withColumn("LastName", split(col("CustomerName"), " ").getItem(1))

# Filter and reorder columns
df = df["SalesOrderNumber", "SalesOrderLineNumber", "OrderDate", "Year", "Month", "FirstName", "LastName", "EmailAddress", "Item", "Quantity", "UnitPrice", "TaxAmount"]

# Load the data into a table
df.write.format("delta").mode("append").saveAsTable(table_name)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/dimension_customer.csv")
# df now is a Spark DataFrame containing CSV data from "Files/dimension_customer.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

conn = notebookutils.data.connect_to_artifact("BIG_DATE", "optional_workspace_id", "optional_lakehouse_type")
df = conn.query("SELECT * FROM sys.schemas;")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

# from deltalake import DeltaTable
# table_path = "abfss://17865aab-61cf-48c0-aec0-4320f4200b00@onelake.dfs.fabric.microsoft.com/d8f78a60-53eb-479b-8b35-7db20c9e3cd6/Tables/dbo/Ranked_Customers" # replace with your table abfss path
# storage_options = {"bearer_token": notebookutils.credentials.getToken("storage"), "use_fabric_endpoint": "true"}
# dt = DeltaTable(table_path, storage_options=storage_options)
# limited_data = dt.to_pyarrow_dataset().head(1000).to_pandas()
# display(limited_data)

# import duckdb
# table_name = dt.to_pyarrow_dataset()
# display(duckdb.sql(" SELECT * from table_name limit 1000 ").df())

# If the table is too large and might cause an Out of Memory (OOM) error,
# you can try using the code below. However, please note that delta_scan with default lakehouse is currently in preview.
import duckdb
display(duckdb.sql("select * from delta_scan('/lakehouse/default/Tables/bigdeltatable') limit 1000 ").df())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

notebookutils.fs.ls("abfss://17865aab-61cf-48c0-aec0-4320f4200b00@onelake.dfs.fabric.microsoft.com/d8f78a60-53eb-479b-8b35-7db20c9e3cd6/Files/new_data")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }

# CELL ********************

notebookutils.notebook.runMultiple("DP700 Notebook")

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "jupyter_python"
# META }
