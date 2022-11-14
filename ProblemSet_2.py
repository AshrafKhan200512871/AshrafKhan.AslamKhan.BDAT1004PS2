#!/usr/bin/env python
# coding: utf-8

# # BDAT 1004 – Data Programming 

# ## Submitted by Ashraf Khan

# ### Question 1
# ### What value is displayed when the last expression (a) is evaluated? Explain your answer by indicating what happens in every executed statement

# In[32]:


a = 0
def b():
 global a    
 a = c(a)   
def c(a):
 return a + 2
b()
b()
b()
a


# Explanation:
# 
# b(): a's value is 0 so as c(a)=a+2 then  0+2=2 noe global a's value gets changed to 2
# 
# b(): a's value is 2 now  so as c(a)=a+2 then  2+2=4 now global a's value gets changed to 4 
# 
# b(): a's value is 4 now  so as c(a)=a+2 then  4+2=6 now global a's value gets changed to 6
# 
# So as in third step a=6 (global value is being changed from 0 to 6 when b() is being executed till last step)

# ### Question 2
# 
# ### Function fileLength(), given to you, takes the name of a file as input and returns the length of the file:

# In[5]:


import os

def fileLength(fileName):
        try:    
            file_size = os.path.getsize('Filelenght.txt')
            print("File Size is :", file_size, "bytes")

        except IOError:                                  
            print('File ' + fileName + ' not found.')    
                                                   
fileLength('Filelength.txt')  
fileLength('filelent.txt')     
        


# ## Question 3
# 
# ### Now write a class named Kangaroo as a subclass of Marsupial that inherits all the attributes of Marsupial and also:
# ### a. extends the Marsupial init constructor to take, as input, the coordinates x and y of the Kangaroo object, 
# ### b. supports method jump that takes number values dx and dy as input and moves the kangaroo by dx units along the x-axis and by dy units along the yaxis,  
# ### c. overloads the str operator so it behaves as shown below.

# In[3]:


class Marsupial:
    def __init__(self):
        self.myLst = []
        
    def put_in_pouch(self,item):       
        self.myLst.append(item)
        
    def pouch_contents(self):          
        return self.myLst

class Kangaroo(Marsupial):
    def __init__(self,x,y):        
        Marsupial.__init__(self)
        self.x = x
        self.y = y
        
    def jump(self,dx,dy):          
        self.x += dx
        self.y += dy
        
    def __str__(self):            
        return 'I am a Kangaroo located at co-ordinates ({},{})'.format(self.x,self.y)
    
    
m = Marsupial()
m.put_in_pouch('doll')
m.put_in_pouch('firetruck')
m.put_in_pouch('kitten')
m.pouch_contents()

k = Kangaroo(0,0)
print(k)

k.put_in_pouch('doll')
k.put_in_pouch('firetruck')
k.put_in_pouch('kitten')
km=k.pouch_contents()
print(km)

k.jump(1,0)
k.jump(1,0)
k.jump(1,0)

print(k)


# ### Question 4 
# ### Write function collatz() that takes a positive integer x as input and prints the Collatz sequence starting at x.

# In[5]:


def collatz(x):
    if x == 1:               
        return [x]
    elif x%2==0:             
        return [x] + collatz(int(x/2))
    else:                    
        return [x] + collatz(int(x*3+1))

y=collatz(1)
z=collatz(10)
print("collatz(1)")
print(*y,sep = "\n")
print("\ncollatz(10)")
print(*z, sep = "\n")


# ## Question 5
# ### Write a recursive method binary() that takes a non-negative integer n and prints the binary representation of integer n

# In[1]:


def binary(n):
    if n == 0:
        return 0
    else:
        binary(n//2)
    print(n % 2,end = '')

Nbr = int(input("Enter your Number: "))
binary(Nbr)


# ### Question 6
# ### Implement a class named HeadingParser that can be used to parse an HTML document, and retrieve and print all the headings in the document.

# In[21]:


from html.parser import HTMLParser

class HeadingParser(HTMLParser):
    Headers = ["h1", "h2"]
    current = -1

    def handle_starttag(self, tag, attrs):      
        if tag in HeadingParser.Headers:         
            HeadingParser.current = HeadingParser.Headers.index(tag)
    
    def handle_endtag(self, tag):                
        if tag == HeadingParser.Headers[HeadingParser.current]:          
            HeadingParser.current = -1
            
    def handle_data(self, data):
        if HeadingParser.current >= 0:
            print(" " * HeadingParser.current + data)


# In[23]:


infile = open("w3c.html","r")
content = infile.read()
infile.close()
hp = HeadingParser()
hp.feed(content)


# ### --------------------------------------------------------------------------------------------------------------------------------------------------------------
# 

# In[19]:


import sqlite3
con = sqlite3.connect('ipydb.db')
cur = con.cursor()
cur.execute("CREATE TABLE cityWeather (City text, Country text, Season text,Temperature float,Rainfall float)")


# In[20]:


cur.execute("INSERT INTO cityWeather VALUES ('Mumbai', 'India', 'Winter',24.8,5.9)")


# In[21]:


cur.execute("INSERT INTO cityWeather VALUES ('Mumbai', 'India', 'Spring',28.4,16.2)")
cur.execute("INSERT INTO cityWeather VALUES ('Mumbai', 'India', 'Summer',27.9,1549.4 )")
cur.execute("INSERT INTO cityWeather VALUES ('Mumbai', 'India', 'Fall',27.6,346.0)")
cur.execute("INSERT INTO cityWeather VALUES ('London', 'United Kingdom', 'Winter',4.2,207.7 )")
cur.execute("INSERT INTO cityWeather VALUES ('London', 'United Kingdom', 'Spring',8.3,169.6)")
cur.execute("INSERT INTO cityWeather VALUES ('London', 'United Kingdom', 'Summer',15.7,157.0)")
cur.execute("INSERT INTO cityWeather VALUES ('London', 'United Kingdom', 'Fall',10.4,218.5)")
cur.execute("INSERT INTO cityWeather VALUES ('Cairo', 'Egypt', 'Winter',13.6,16.5)")
cur.execute("INSERT INTO cityWeather VALUES ('Cairo', 'Egypt', 'Spring',20.7,6.5)")
cur.execute("INSERT INTO cityWeather VALUES ('Cairo', 'Egypt', 'Summer',27.7,0.1)")
cur.execute("INSERT INTO cityWeather VALUES ('Cairo', 'Egypt', 'Fall',22.2,4.5)")


# In[22]:


cur.execute('SELECT * FROM cityWeather')
cur.fetchall()


# ### Question 8
# ### Write SQL queries on the below database table that return:
# ### a) All the temperature data.

# In[25]:


cur.execute('SELECT temperature FROM cityWeather')
A=cur.fetchall()
for item in A:
    print(item)


# ### b) All the cities, but without repetition.
# 

# In[26]:


cur.execute('SELECT DISTINCT City FROM cityWeather')
B=cur.fetchall()
for item in B:
    print(item)


# ### c) All the records for India.

# In[27]:


cur.execute("SELECT * FROM cityWeather WHERE Country='India'")
C=cur.fetchall()
for item in C:
    print(item)


# ### d) All the Fall records.

# In[28]:


cur.execute("SELECT * FROM cityWeather WHERE Season='Fall'")
D=cur.fetchall()
for item in D:
    print(item)


# ### e) The city, country, and season for which the average rainfall is between 200 and 400 millimeters.
# 

# In[29]:


cur.execute("SELECT City,country,Season FROM cityWeather WHERE Rainfall BETWEEN 200 AND 400")
E=cur.fetchall()
for item in E:
    print(item)


# ### f) The city and country for which the average Fall temperature is above 20 degrees, in increasing temperature order.

# In[30]:


cur.execute("SELECT City,country FROM cityWeather WHERE Season='Fall' AND temperature > 20 ORDER BY temperature ASC")
F=cur.fetchall()
for item in F:
    print(item)


# ### g) The total annual rainfall for Cairo
# 

# In[31]:


cur.execute("SELECT SUM(Rainfall) FROM cityWeather WHERE City='Cairo'")
G=cur.fetchall()
for item in G:
    print(item)


# # h) The total rainfall for each season.

# In[32]:


cur.execute("SELECT SUM(Rainfall) FROM cityWeather GROUP BY Season")
H=cur.fetchall()
for item in H:
    print(item)


# ###  Question 9 
# ### Suppose list words is defined as follows: words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog'] Write list comprehension expressions that use list words and generate the following lists:

# In[26]:


words = ['The', 'quick', 'brown', 'fox', 'jumps', 'over','the', 'lazy', 'dog']


# ### a)

# In[27]:


a = [elements.upper() for elements in words]
print (a)


# ### b)

# In[28]:


b = [elements.lower() for elements in words]
print(b)


# ### c)

# In[29]:


c = [len(elements) for elements in words]
print(c)


# ### d)

# In[30]:


d = [[elements.upper(),elements.lower(),len(elements)] for elements in words]
print(d)


# ### e)

# In[31]:


e = [elements for elements in words if len(elements)>=4]
print(e)

