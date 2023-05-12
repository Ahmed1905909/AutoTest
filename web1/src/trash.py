from src.test_suite_mang.test_suite_manger import save_test_suite
from src.test_suite_mang.test_suite_manger import update_test_suite
from src.test_suite_mang.test_suite_manger import run_test_suite
import json

test_metadata_json = '{"file":"Temp_calculator","location":"/uploads","class":"TempCalc","constructor":{"parameters":[{"type":"integer","min":-40,"max":140},{"type":"integer","min":-40,"max":60}]},"actions":[{"name":"fahrenheit","type":"assign","parameters":[{"type":"integer","min":-40,"max":140}]},{"name":"celsius","type":"assign","parameters":[{"type":"integer","min":-40,"max":60}]},{"name":"fahrenheit_value","type":"method"},{"name":"celsius_value","type":"method"}]}'
print(run_test_suite('kiro_test',json.loads(test_metadata_json),None))

# update_test_suite(5,"test")
