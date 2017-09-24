import requests
import csv
from bs4 import BeautifulSoup

def getValues_InsertCSV(museum_names):
    count=0;
    with open("Companies.csv", "a") as csvFile:
        contentCSV = csv.writer(csvFile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for values in museum_names:
            if 'museum' in values['href'] and 'info' in values['href'] and count>10:
                #print (values['href'])
                #print (values.text)
                #http: // www.museumsusa.org/museums/info/6186
                #url

                url="http://www.museumsusa.org"+str(values['href'])
                print (url)
                #url="http://www.museumsusa.org/museums/info/16243"
                try:
                    museum_response= requests.get(url)

                    museum_data_response= museum_response.text;
                    soup2 = BeautifulSoup(museum_data_response, "html.parser");

                except:
                    pass;
                #museum_mailing_address = soup2.findAll('div', )
                museum_mailing_address = soup2.findAll("div", {"id": "ctl04_ctl00_icStreetAddress"})
                museum_phone_email = soup2.findAll("div", {"id": "ctl04_ctl00_icPhoneEmailWeb"})  # this includes fax, email, phone #
                museum_type_staff = soup2.findAll("div", {"class": "textbox"})


                row_write=[]
                row_write.append(values.text)
                row_write.append(museum_mailing_address[0].text)


                phone_fax_email=museum_phone_email[0].text
                if 'fax' in phone_fax_email and 'phone' in phone_fax_email:

                    phone_number=phone_fax_email[phone_fax_email.find('phone')+6:phone_fax_email.find('fax')]

                elif 'fax' not in phone_fax_email and 'e-mail' in phone_fax_email and 'phone' in phone_fax_email:

                    phone_number = phone_fax_email[phone_fax_email.find('phone') + 6:phone_fax_email.find('e-mail')]

                elif 'fax' not in phone_fax_email and 'e-mail' not in phone_fax_email and 'web' in phone_fax_email and 'phone' in phone_fax_email:
                    phone_number = phone_fax_email[phone_fax_email.find('phone') + 6:phone_fax_email.find('web')]

                elif 'fax' not in phone_fax_email and 'e-mail' not in phone_fax_email and 'web' not in phone_fax_email and 'phone' in phone_fax_email:
                    phone_number = phone_fax_email[phone_fax_email.find('phone') + 6:]
                else:
                    phone_number='';


                #phone_number=soup2.findAll('span',{'class':'phone'})[0].text
                if 'fax' in phone_fax_email and 'e-mail' in phone_fax_email:
                    fax=phone_fax_email[phone_fax_email.find('fax')+4:phone_fax_email.find('e-mail')]
                elif 'fax' in phone_fax_email and 'e-mail' not in phone_fax_email and 'web' in phone_fax_email:
                    fax = phone_fax_email[phone_fax_email.find('fax') + 4:phone_fax_email.find('web')]
                elif 'fax' in phone_fax_email and 'e-mail' not in phone_fax_email and 'web' not in phone_fax_email:
                    fax=phone_fax_email[phone_fax_email.find('fax') + 4:]
                else:
                    fax=''


                if 'e-mail' in phone_fax_email and 'web' in phone_fax_email:
                    email=phone_fax_email[phone_fax_email.find('e-mail')+7:phone_fax_email.find('web')]
                elif 'e-mail' in phone_fax_email and 'web' not in phone_fax_email:
                    email = phone_fax_email[phone_fax_email.find('e-mail') + 7:]
                else:
                    email=''


                if 'web' in phone_fax_email:
                    web= phone_fax_email[phone_fax_email.find('web')+4:]
                else:
                    web='';

                row_write.append(phone_number)
                row_write.append(fax)
                row_write.append(email)
                row_write.append(web)

                museum_type_staff_text=museum_type_staff[1].text;
                museum_type=museum_type_staff_text[museum_type_staff_text.find('Museum Type(s)')+19:museum_type_staff_text.find('Staff'):].replace('\n\n\n\n',',').replace('\n','')
                row_write.append(museum_type)
                staff_text_list=museum_type_staff_text[museum_type_staff_text.find('Staff')+7:].split('\n\n\n')

                for row in staff_text_list:
                    splitrecords = row.split('\n');
                    if len(splitrecords)==1 and ('phone' not in str(splitrecords[0]) or 'phone' not in str(splitrecords[1])):
                        row_write.append(splitrecords[0])
                        row_write.append('')
                    else:
                        for subrow in row.split('\n'):
                                row_write.append(subrow)


                contentCSV.writerow(row_write)
                print ("test")
            count += 1;





#print (response);
def main():
    #alphabest_list= ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alphabest_list=['RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']
    for alpha in alphabest_list:

        #url = "http://www.museumsusa.org/museums/?k=1271393%2cAlpha%3a"+alpha+"%3bDirectoryID%3a200454"
        url="http://www.museumsusa.org/museums/?k=1271400%2cState%3a"+alpha+"%3bDirectoryID%3a200454"
        print ("main URL:"+url)

        response= requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser");

        museum_names= soup.findAll("a", href=True)#, { "data-column" : "Markets" })
        getValues_InsertCSV(museum_names);

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko)"
        }

        session = requests.Session()
        session.headers.update(headers)
        r = session.get(url)
        #pages =True;
        count_pages=1;
        pages=75

        # if alpha == 'A':
        #     pages = 889
        # elif alpha == 'B':
        #     pages = 917
        # elif alpha == 'C':
        #     pages = 1463
        # elif alpha == 'D':
        #     pages = 534
        # elif alpha == 'E':
        #     pages = 411
        # elif alpha == 'F':
        #     pages = 726
        # elif alpha == 'G':
        #     pages = 641
        # elif alpha == 'H':
        #     pages = 1063
        # elif alpha == 'I':
        #     pages = 274
        # elif alpha == 'J':
        #     pages = 344
        # elif alpha == 'K':
        #     pages = 276
        # elif alpha == 'L':
        #     pages = 715
        # elif alpha == 'M':
        #     pages = 1465
        # elif alpha == 'N':
        #     pages = 665
        # elif alpha == 'O':
        #     pages = 495
        # elif alpha == 'P':
        #     pages = 803
        # elif alpha == 'Q':
        #     pages = 35
        # elif alpha == 'R':
        #     pages = 569
        # elif alpha == 'S':
        #     pages = 1436
        # elif alpha == 'T':
        #     pages = 998
        # elif alpha == 'U':
        #     pages = 268
        # elif alpha == 'V':
        #     pages = 192
        # elif alpha == 'W':
        #     pages = 827
        # elif alpha == 'X':
        #     pages = 4
        # elif alpha == 'Y':
        #     pages = 61
        # elif alpha == 'Z':
        #     pages = 29



        #while (pages):
        for _ in range(pages):
            print (count_pages)
            try:
                soup = BeautifulSoup(r.content, 'html.parser')
                VIEWSTATE = soup.find(id="__VIEWSTATE")['value']
                EVENTVALIDATION = soup.find(id="__EVENTVALIDATION")['value']
                data_in = {
                    '__EVENTTARGET': 'ctl08$ctl00$BottomPager$Next',
                    '__EVENTARGUMENT': "",
                    '__VIEWSTATE': VIEWSTATE,
                    '__EVENTVALIDATION': EVENTVALIDATION,
                    'ctl04$phrase': "",
                    'ctl04$directoryList': "/museums/|/museums/search/"
                }
                r = session.post(url, data=data_in)
                print(r)
                soup_pages = BeautifulSoup(r.text, "html.parser");
                museum_names_pages = soup_pages.findAll("a", href=True)  # , { "data-column" : "Markets" })
                if len(museum_names_pages)<142:
                    pages=False
                else:

                    getValues_InsertCSV(museum_names_pages)
            except:
                pass;


            count_pages+=1;



if __name__=='__main__':
    main()