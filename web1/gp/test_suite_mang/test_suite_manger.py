import mysql.connector
import json
import subprocess
import os

from gp.genetic_algorithm_2 import generate_best_test_suite

# establish connection
conn = mysql.connector.connect(
    user='root', 
    # password='root',
    host='127.0.0.1', database='auto_test'
)


def save_test_suite(name, metadata_json):
    cursor = conn.cursor()

    # define data to insert

    json_data = json.dumps(metadata_json)  # convert data to JSON string

    # execute query
    query = "INSERT INTO test_suite (name, metadata_json) VALUES (%s,%s)"
    cursor.execute(query, (name,json_data,))

    # get ID of inserted row
    id = cursor.lastrowid

    # commit changes
    conn.commit()

    # close cursor and connection
    cursor.close()
    # conn.close()
    return id

def update_test_suite(id,result_html_path):
    # create cursor
    cursor = conn.cursor()

    # define SQL statement to update row
    sql = "UPDATE test_suite SET generated_results = %s WHERE id = %s"

    # define values to update
    values = (result_html_path, id)

    # execute update statement with values
    cursor.execute(sql, values)

    # commit changes to database
    conn.commit()
    cursor.close()
    # conn.close()


def run_test_suite(name, metadata_json,python_class):
    saved_id = save_test_suite(name,metadata_json)
    print("saved_id : "+str(saved_id))
    test_suite_file_path = generate_best_test_suite(metadata_json)
    print("test_suite_file_path : " + test_suite_file_path)
    result_html_path = "result_"+str(saved_id)+".html"
    subprocess.run(["pytest", "--html=" +os.getcwd()+"/gp/templates/gp/"+result_html_path,test_suite_file_path])
    update_test_suite(saved_id,result_html_path)
    return result_html_path


