from bs4 import BeautifulSoup
import sys
import urllib2

url = urllib2.urlopen(sys.argv[1])
html = url.read()

soup = BeautifulSoup(html)

product_title_div = soup.find("div", class_="product_title")
title = product_title_div.a.text
platform = product_title_div.span.a.text

publisher = soup.find("li", class_="summary_detail publisher").a.text
release_date = soup.find("li", class_="summary_detail release_data").find("span", class_="data").text

critics = soup.find("div", class_="details main_details")
critic_score = critics.find("span", class_="score_value").text
critic_outof = critics.find("span", class_="score_total").span.text
critic_count = critics.find("span", class_="count").a.span.text

users = soup.find("div", class_="details side_details")
users_score = users.find("span", class_="score_value").text
raw_users_count = users.find("span", class_="count").a.text
users_count = ""
for c in raw_users_count:
	if c.isdigit(): users_count += c

product_info = soup.find("div", class_="section product_details").find("div", class_="details side_details")
developer = product_info.find("li", class_="summary_detail developer").find("span", class_="data").text
genre = product_info.find("li", class_="summary_detail product_genre").find("span", class_="data").text
rating = product_info.find("li", class_="summary_detail product_rating").find("span", class_="data").text

print "URL: " + url.geturl()
print "Title: " + title.strip()
print "Platform: " + platform.strip()
print "Publisher: " + publisher.strip()
print "Release Date: " + release_date.strip()
print "Critic Score: " + critic_score.strip() + "/" + critic_outof + " (" + critic_count + " critics)"
print "User Score: " + users_score.strip() + " (" + users_count + " users)"
print "Developer: " + developer.strip()
print "Genre: " + genre.strip()
print "Rating: " + rating.strip()