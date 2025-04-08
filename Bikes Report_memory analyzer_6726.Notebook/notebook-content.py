# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   }
# META }

# MARKDOWN ********************

# #### Import the Semantic Link library

# CELL ********************

# Ensure semantic-link>=0.9.2 is installed
from packaging.version import Version
from importlib.metadata import version

sempy_version = version('semantic-link-sempy')

if Version(sempy_version) < Version("0.9.2"):
    get_ipython().run_line_magic('pip', 'install semantic-link==0.9.2')

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

import sempy.fabric as fabric

dataset = "Bikes Report" # Enter the name or ID of the semantic model
workspace = "TEST ENVIRONMENT" # Enter the workspace name or ID in which the semantic model exists

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Run the Memory Analyzer on your semantic model

# CELL ********************

fabric.model_memory_analyzer(dataset=dataset, workspace=workspace)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# #### Learn more about notebooks in Fabric
# Notebooks in Fabric empower you to use code and low-code solutions for a wide range of data analytics and data engineering tasks such as data transformation, pipeline automation, and machine learning modeling.
# 
# * To edit this notebook, switch the mode from **Run** only to **Edit** or **Develop**.
# * You can safely delete this notebook after running it. This won’t affect your semantic model.
# 
# 
# For more information on capabilities and features, check out [Microsoft Fabric Notebook Documentation](https://learn.microsoft.com/fabric/data-engineering/how-to-use-notebook).

