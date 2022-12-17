import os.path

import openai
import random
import os
from os import path

openai.api_key = ''
from gpt import GPT
from gpt import Example
gpt = GPT(engine="davinci",
          temperature=0.7,
          max_tokens=250)
gpt.add_example(Example('create a new chrome driver and go to google.com, then select the search button.',
                        'driver = webdriver.Chrome()\n'
                        'driver.get("google.com")\n'
                        'driver.find_element_by_id("lst-id").click()\n'))
gpt.add_example(Example('create a new chrome driver and go to ebay.com, then select the sell link.',
                        'driver = webdriver.Chrome()\n'
                        'driver.get("ebay.com")\n'
                        'driver.find_element_by_css_selector("#gh-p-2>a").click()\n'))
gpt.add_example(Example('create a new definition called do_do_stuf with a new chrome driver and go to Walmart.com and then select the Pickup & Delivery link.',
                        'def do_stuff():\n'
                        'driver = webdriver.Chrome()\n'
                        'driver.get("Walmart.com")\n'
                        'driver.find_element_by_xpath("//*[@id="header-tabs]/div/a[1]/span").click()\n'))
gpt.add_example(Example('create a new definition called dont_stuf with a new firefox driver and go to amazon.com and then select the language dropdown.',
                        'def dont_do_stuff():\n'
                        'driver = webdriver.FireFox()\n'
                        'driver.get("amazon.com.com")\n'
                        'driver.find_element_by_css_selector("#icp-nav-flayout > span.ipc-nav-link-inner > span.ipc-nav-link-language").click()\n'))

prompt = "creat a new definition called ai_gen_script with a new Chrome driver and go to amazon.com and selsect the cart."
output = gpt.submit_request(prompt)
#print(output.choices[0].text)
codeGen = output.choices[0].text
name = "AI_Generated"
foldername = os.path.dirname(os.path.dirname(__file__)) + "/Selenium_GPT3/"
pathname = path.join(foldername,name.lower() + '.py')
with open(pathname, 'w') as pyfile:
    pyfile.write((str.format("from selenium import webdriver")))
    pyfile.write('\n')
    pyfile.write(codeGen.split(' ',1)[1])


