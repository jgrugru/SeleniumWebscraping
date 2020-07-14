
from selenium import webdriver 
from time import sleep 
from selenium.webdriver.chrome.options import Options
import csv

chrome_path = r"C:\Users\jeffg\Desktop\ProgrammingProjects\webscraping\chromedriver.exe"
ch_options = Options()
prefs = {'profile.default_content_setting_values.notifications': 2}
ch_options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(executable_path=chrome_path, chrome_options=ch_options)

driver.get("https://www.nc.gov/employee-directory")
print("Opened nc.gov page")
sleep(1)

firstname_box = driver.find_element_by_xpath('''//*[@id="edit-namefirst"]''')
firstname_box.send_keys('a')
print('firstname Entered')

driver.find_element_by_xpath('''//*[@id="edit-submit-empdir"]''').click()
print("Clicked on apply")
with open('fullEmpDir.csv', mode='a') as f:
    employee_writer = csv.writer(f, delimiter=',')
    while(True):
        posts=[]
        posts = driver.find_elements_by_class_name("views-field")
        print("Found posts")
        count = 3
        while count < len(posts):
            employee_writer.writerow([posts[count].text, posts[count+1].text, posts[count+2].text])
            print(posts[count].text)
            print(posts[count+1].text)
            print(posts[count+2].text)
            count+=3

        driver.find_element_by_class_name("pager-next").click()
        sleep(2)