from bs4 import BeautifulSoup
import requests

# Get the HTML
r = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=")
html_content = r.content

# Parse the HTMLz
soup = BeautifulSoup(html_content, 'lxml')
jobs = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
for job in jobs:
    published_date = job.find('span', class_="sim-posted").span.text
    with open("Latest Job.txt","a") as f:
        if 'few' in published_date:
            CompanyName = job.find('h3', class_="joblist-comp-name").text.replace(' ','')
            KeySkills = job.find('span', class_="srp-skills").text.replace(' ','')
            MoreInfo = job.header.h2.a['href']
            Experience = job.find('ul', class_="top-jd-dtl clearfix").text[12:22]
            JobLocation = job.find('ul', class_="top-jd-dtl clearfix").text[34:]
            f.write('\n')
            f.write(f'Company Name : {CompanyName} \n')
            f.write(f'Job Location : {JobLocation} \n')
            f.write(f'Key Skills : {KeySkills} \n')
            f.write(f'Experience : {Experience} \n')
            f.write(f'More Information : {MoreInfo} \n')
            f.write('-'*150)
        
            print(f'Company Name : {CompanyName} \n')
            print(f'Job Location : {JobLocation} \n')
            print(f'Key Skills : {KeySkills} \n')
            print(f'Experience : {Experience} \n')
            print(f'More Information : {MoreInfo} \n')
            print('-'*150, '\n')