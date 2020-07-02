"""Export Json output from CLI Analyzer to
Customer Report Format for Multiple Files"""
# Import  Libraries

import json
import pandas as pd
from pandas.io.json import json_normalize
import save_file

# User Inputs
json_file = input("Enter the File Name:-")
client_name = input("Enter the Cleint Name:-")
projet_type = input("Enter the Project type with Customer:- ")
project_Name = input("Enter the Projec Name:-")

# Calling File saving class from Save_file Library
jd = save_file.SAVE_FILE_TO_FOLDER(client_name,projet_type, project_Name)
path = jd.save_files()
# Open Jason FIle and Load it

f = json.load(open(path + "/" + "Cli_Analyzer" + json_file + ".json"))
# we Import data only from message Object in Json file.
df = pd.json_normalize(f["messages"])
# we Import data only specific fields from messages for client.
client_result = df.loc[:, ["name", "type", "severityClass"]]
client_columns = [
    "TITLE",
    "TYPE",
    "SEVIERITY",
]
client_result.columns = client_columns
# we Import data only specific fields from messages for Engineer.
engineer_result = df.loc[:, ["content", "snippets",]]
engineer_result_columns = [
    "CONTENT",
    "SNIPPETS",
]
engineer_result.columns = engineer_result_columns
# Save File in Project Folder.
sheetname = json_file.lower()
client_result.to_excel(path + "/" + json_file + "cl" + ".xlsx", sheet_name=sheetname)
engineer_result.to_excel(path + "/" + json_file + "eng" + ".xlsx", sheet_name=sheetname)
print("===============================================================")
print("Output Saved at " + path)
print("===============================================================")
