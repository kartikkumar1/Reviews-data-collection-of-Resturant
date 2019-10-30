This program pulls in all the reviews related data of a resturant from the website tripadvisor.in and store it in a .csv file.
Below are the steps of its working:

1) First we make a file Reveiw_Data.csv in write and append mode.

2) We give the URL of the resturant in the code.

3)In a while(1) loop we start the connection of URl, store it and the close it.

4) With the help of library bs4(beautifulSoup), we parse the stored data in html format.

5)Through code inspection I found out that all reviews on the page are contained in  class "review-container". I store it in Containers.

6)We the take out every element(review) from the containers.

7)First, we find Rating which is stored in class "ui_bubble_rating".

8)Then we make the values of 0 to 50 into 1 to 5 using if elif condition.

9)We then find Date of Rating through class "ratingDate" and its attribute "title", store it in date.

10)Then We find the Review  paragraph section and make it free of spaces and tabs using replace function.

11)Then we find the Review Title and the do the same as above, to make data clean.

12) Then we find the website name using class img and attribute "data-lazyurl".

13)I had made the data clean by using for  and if loops therefore we only get site's name.

14)Then we write in the file, all the collected data.

15)Through bs4 funciton find we find the attributs of next button of the page, because it points to the next page.

16)I have made a excepion handelling because at the last page it would throw an error. Which would be used to exit the while(1) loop.

17)If the 16. point dosent happen the we add the next page link to the existing link.

18)And due to the loop, it would go on to the next page for the same process.

19)When it reaches the last page, it will break out of loop and the file wil be closed.

20)A .csv file would be created after the completion of the script which would contain the parsed data.
