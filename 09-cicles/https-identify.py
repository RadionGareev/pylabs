#inroduce URL
url          = input("introduce your url\n")


#check  the url contain

if url[0:5] == 'https':
    print("the connection is secure")
if url[0:5] == 'http:':
    print("the connection is unsecure")
if "md" in url:
    print(" the website is MD ")
if "?" in url:
    print(" the link contain '?' parameter")