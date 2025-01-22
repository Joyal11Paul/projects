import requests
from bs4 import BeautifulSoup

'''-----------------------------------------Step One - Getting to the links--------------------------------------------'''
def fetch_professors(college, course, course_number):
    college = college.lower()
    course = course.upper()
    url = f"https://www.coursicle.com/{college}/courses/{course}/{course_number}"
    return url

url = fetch_professors("binghamton", "Cs", "110")      # Change when necessary

def write_info():
    response = requests.get(url)
    with open("info.html", "w", encoding="utf-8") as f:
        f.write(response.text)

# Call write_info for each new website grab: write_info()

with open("info.html", "r", encoding="utf-8") as f:
    content = f.read()

soup = BeautifulSoup(content, "html.parser")
div = soup.find_all(attrs={"class": "professorLink"})
professor_links = []
professor_names = []

for links in div:
    professor_links.append(links.get('href'))
    professor_names.append(links.string)

'''----------------------------------Step Two - Getting Each Professor's Rating -----------------------------------------------'''

def write_prof(number = 1):
    prof_response = requests.get(professor_links[number])
    with open("prof_info.html", "w", encoding="utf-8") as f:
        f.write(prof_response.text)

# Use write_prof here: write_prof()  # Rewrite when back

with open("prof_info.html", "r", encoding="utf-8") as f:
    content_prof = f.read()

soup = BeautifulSoup(content_prof, "html.parser")
#print(soup.prettify())