import csv
import subprocess
from datetime import datetime
import os

csv_file = 'hadoop_parameterized_tests.csv'
current_datetime = datetime.now().strftime("%m.%d.%y_%H:%M:%S")
log_folder = f"hadoop_puts_logs_{current_datetime}/"
os.makedirs(log_folder)

commands_log="hadoop_commands_executed.log"

with open(csv_file, newline='') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        test_name = row['Fully-Qualified Test Name']
        module_path = row['Module Path']

        command = f"mvn test -Dtest={test_name}[\\*] -pl {module_path}"
        log_file = f"{log_folder}{test_name.replace('#', '_')}.log"
        print("Running command:", command)
        with open(log_file, 'w') as log:
            subprocess.run(command, shell=True, stdout=log, stderr=subprocess.STDOUT)

