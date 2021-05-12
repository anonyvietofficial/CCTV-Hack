import requests,re,os
import time
import sys
from os import system
from platform import platform
from time import sleep
import os

print("Welcome to camera-hack!")
print("Chon Quoc gia ban muon xem Camera:")
print("""
1. Russian Federation                        
2. United States                           
3. Japan                                        
4. Canada                                     
5. New Zealand                           
6. Ukraine                       
7. Germany                       
8. Austria                       
9. Spain                       
10. Turkey 
11. Hong Kong
12. Greece
13. Portugal
14. Singapure
15. Columbia
16. Vietnam quyet tam chien thang dai dich Covid
""")
num = int(input("country : "))
if num == 1:
        print("\n")		
        os.system(delet)
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,82):
			
                url = ("https://www.insecam.org/en/bycountry/RU/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)

                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()

                     count += 1
        except:
            print ("") 
if num == 2:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,720):
			
                url = ("https://www.insecam.org/en/bycountry/US/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")
if num == 3:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,232):
			
                url = ("https://www.insecam.org/en/bycountry/JP/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")
if num == 4:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,38):
			
                url = ("https://www.insecam.org/en/bycountry/CA/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")             
if num == 5:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,5):
			
                url = ("https://www.insecam.org/en/bycountry/NZ/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")             
if num == 6:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,2):
			
                url = ("https://www.insecam.org/en/bycountry/UK/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;37m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ") 
if num == 7:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,107):
			
                url = ("https://www.insecam.org/en/bycountry/DE/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")
if num == 8:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,48):
			
                url = ("https://www.insecam.org/en/bycountry/AT/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                     count += 1
        except:
            print (" ")           
if num == 9:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,39):
			
                url = ("https://www.insecam.org/en/bycountry/ES/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")  
if num == 10:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,54):
			
                url = ("https://www.insecam.org/en/bycountry/TR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")             
if num == 11:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,7):
			
                url = ("https://www.insecam.org/en/bycountry/HK/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")  
if num == 12:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,8):
			
                url = ("https://www.insecam.org/en/bycountry/GR/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")           
if num == 13:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,7):
			
                url = ("https://www.insecam.org/en/bycountry/PT/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ")        
if num == 14:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,7):
			
                url = ("https://www.insecam.org/en/bycountry/SG/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()

                     count += 1
        except:
            print (" ")      
if num == 15:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:68.0) Gecko/20100101 Firefox/68.0'}       
            for page in range (0,6):
			
                url = ("https://www.insecam.org/en/bycountry/CO/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ") 
if num == 16:
        print("\n")		
        try:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}       
            for page in range (0,6):
			
                url = ("https://www.insecam.org/en/bycountry/VN/?page="+str(page))
            
                res = requests.get(url, headers=headers)
                findip = re.findall('http://\d+.\d+.\d+.\d+:\d+', res.text)
                count = 0
                                
                for _ in findip:
                     hasil = findip[count]

                     print ("\033[1;31m",hasil)
                     f = open('logs.txt' , 'a')
                     f.write(f'{findip}' + '\n')
                     f.close()
                 
                     count += 1
        except:
            print (" ") 

print("IP duoc luu tai file logs.txt")
print("""
See more: https://anonyviet.com
""")
