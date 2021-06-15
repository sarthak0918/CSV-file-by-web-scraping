
import requests # it is going to request that site from which we want to scrap thing
from bs4 import BeautifulSoup # what beutiful soup does is it understands Html so it goona sv=crap pf the elements from site for you easily
import pandas
page = requests.get('https://mausam.imd.gov.in')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)  #it is going to print the whole code the site
#print(soup.find_all('a'))# its going to find all links available on the site
# now we will find the forecast of major cities of India

citie = soup.find(id ='today')
#print(cities)
cites = citie.find_all(class_ = 'capital')# now this will find the code of temp of the cities
#print(cites[i].find(class_='').get_text())
#print(cites[i].find(class_='val').get_text())
#print(cites[i].find(class_='minmax').get_text())
#we will write a for loop  for this things
city_names = [city.find(class_='').get_text() for city in cites]
temp = [tempr.find(class_='val').get_text() for tempr in cites]
wind = [winds.find(class_='minmax').get_text() for winds in cites]
print(city_names)
print(temp)
print(wind)
# Now to convert this lists into csv file we can do it with pandas really easily
wetehar_city = pandas.DataFrame(
    {'city':city_names,
     "temp":temp,
     "chance of rain":wind,
     })#here dataframe takes data as dictinarieas
print(wetehar_city)
# convert this into csv
wetehar_city.to_csv('weather.csv')