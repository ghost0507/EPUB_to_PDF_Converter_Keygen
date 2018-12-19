#
# * Program: SysTools EPUB to PDF Converter
# * Release: Simple Keygen
# * Created with: Python 3.7.x
#

import hashlib, re, random, datetime, os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
def IsValidEmail(inputEmail):
  if re.match("^(([\\w-]+\\.)+[\\w-]+|([a-zA-Z]{1}|[\\w-]{2,}))@((([0-1]?[0-9]{1,2}|25[0-5]|2[0-4][0-9])\\.([0-1]?[0-9]{1,2}|25[0-5]|2[0-4][0-9])\\.([0-1]?[0-9]{1,2}|25[0-5]|2[0-4][0-9])\\.([0-1]?[0-9]{1,2}|25[0-5]|2[0-4][0-9])){1}|([a-zA-Z]+[\\w-]+\\.)+[a-zA-Z]{2,4})$", inputEmail):
    return True
  else:
    return False

def getMD5(inputText):
  return hashlib.md5(inputText.encode('utf-8')).hexdigest()

validEmail = False
while not (validEmail):
  userEmail = input("Enter your email: ")
  if(IsValidEmail(userEmail)):
    validEmail = True
  else:
    cls()

localDate = (datetime.datetime.now() + datetime.timedelta(days=2)).strftime("%d-%m-%Y")
dataToSend = ""
if(random.randint(0,1)):
  dataToSend = userEmail + "_" + localDate + "_" + "SysTools EPUB to PDF Converter"
else:
  dataToSend = userEmail + "_" + localDate
print("Product key: " + getMD5(dataToSend))
