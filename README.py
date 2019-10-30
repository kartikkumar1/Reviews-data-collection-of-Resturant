# Reviews-data-collection-of-Resturant
#Data collection of all the reviews of a restaurant from Tripadvisor.in('https://www.tripadvisor.in/Restaurant_Review-g59644-#d4810291-Reviews-Slammin_Sammy_s-White_Sulphur_Springs_West_Virginia.html')
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

filename= "Reveiw_Data_file.csv"

f=  open(filename,"a+")

headers = "Rating,Review Date,Review Paragraph,Review Title,Site\n"

f.write(headers)


my_url = 'https://www.tripadvisor.in/Restaurant_Review-g59644-d4810291-Reviews-Slammin_Sammy_s-White_Sulphur_Springs_West_Virginia.html'

while (1):
    uClient = uReq(my_url) #Open connction and grabbing html
    page_html = uClient.read() #storing it in a variable
    uClient.close()  # closing connection

    page_soup = soup( page_html,"html.parser" ) #html parsing

    containers = page_soup.findAll("div",{"class":"review-container"}) # grabs each reviews

    for container in containers:
        rating= str(container.find("span",{"class":"ui_bubble_rating"}))
        a=""
        for i in rating:
            if i.isdigit():
                a=a+i
        rating=int(a)

        if rating>40:
            rating=5
        elif rating>30:
            rating=4
        elif rating>20:
            rating=3
        elif rating>10:
            rating=2
        else:
            rating=1

            
        date = str(container.find("span",{"class":"ratingDate"})["title"])
        rev_p=str(container.div.div.p.text)
        rev_p=rev_p.replace(","," ")
        rev_p=rev_p.replace("\n"," ")
        rev_t=str( container.find("span",{"class":"noQuotes"}).text)
        rev_t=rev_t.replace(","," ")
        rev_t=rev_t.replace("\n"," ")
        site=str(container.img)
        website= container.img["data-lazyurl"]
        website1=""
        count=0
        for i in website:
            if count==0 and i=='.':
                count=1
            elif count == 1 and i == '.':
                count=2
            elif count == 1 and i != '.':
                website1=website1+i



        f.write(str(rating)+","+date+","+rev_p+','+rev_t+','+website1+"\n")
        
    


    link = page_soup.find( attrs={"class":"nav next taLnk ui_button primary"} )
    try:
        link = link.get('href')
    except Exception as e:
        break
    else:
        pass
    finally:
        pass
    my_url = "https://www.tripadvisor.in"+str(link)

f.close()


