"""Export Json output from CLI Analyzer to
Customer Report Format for Multiple Files"""
# Import  Libraries
import json
import csv
import pandas as pd
from pandas.io.json import json_normalize
import save_file

# User Inputs
json_file = input("Enter the Json List:-")
client_name = input("Enter the Client Name:-")
projet_type = input("Enter the Project type with Customer:- ")
project_Name = input("Enter the Projec Name:-")

# Calling File saving class from Save_file Library
jd = save_file.SAVE_FILE_TO_FOLDER(client_name,projet_type, project_Name)
path = jd.save_files()
client_writer = pd.ExcelWriter(
    path + "/" + "CLI_Analayze_Client.xlsx", engine="xlsxwriter"
)
engg_writer = pd.ExcelWriter(path + "/" + "CLI_Analayze_Eng.xlsx", engine="xlsxwriter")

# Read the Json name from CSV file and convert it and save it in Project folder.
with open(path + "/" + "Cli_Analyzer" + json_file, "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file)
    for name in reader:
        f = json.load(open(name[0] + ".json"))
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
        sheetname = name[0]
        client_result.to_excel(client_writer, sheet_name=sheetname + "-cl-")
        engineer_result.to_excel(engg_writer, sheet_name=sheetname + " eng- ")
        print("===============================================================")
        print("Output Saved at " + path)
        print("===============================================================")
    writer.save()
