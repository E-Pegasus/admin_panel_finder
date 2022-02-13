import requests
import time
import datetime
import sys

#read a file that holds possible directoris
theFile = open('link.txt','r+')
adminLinks = theFile.readlines()
theFile.close()
#length of directories to be brute
linkSize = len(adminLinks)

#the main function to get connect, write log
def findLinks(siteName, writeLog= False):
    
    if writeLog :
        theLogFile = open('log.txt','a+')
    x=0
    try:
        for link in adminLinks:
            x = x+1
        
            try:
                url = siteName+'/'+link
                url = url.rstrip('\r\n')
                result = requests.get(url)
                time.sleep(1)
                
            except requests.exceptions.MissingSchema:
                    print('invalid url example: http://www.google.com, https://Ethiopia.com or test.com:8080')
                    break
            except requests.exceptions.InvalidSchema as err:
                    print(str(err))
                    break
            except requests.exceptions.HTTPError:
                    print('Error: Invalid Http Response')
                    break

            except requests.exceptions.ConnectionError:
                    print('Error: Please Connect To Network')
                    break
                    
            except requests.exceptions.Timeout as to:
                    print('Error: '+ to)
                    break

            #status code after requst have made
            code = result.status_code
            #successfull request, returned 200 OK display
            view1 ='''
                -------------------------------------------------------------------------------
            >| {x}/{linkSize}
                |
                |=> {link}
                |
                |==>{code}
                |==>NO
                -------------------------------------------------------------------------------
            '''.format(x=x, linkSize=linkSize, link=url, code=code)
            #display for result returned non 200 like 404
            view2 = \
            '''
                =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=>
            >||{x}/{linkSize}
                ||                       
                ||=> {link}
                ||=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=>
                ||==>{code}
                ||==> YES
                =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=>
            '''.format(x=x, linkSize=linkSize, link=url, code=code)

            #only reports 200 ok replays, if you want others reults please check log
            if code != 200:
                print(view1)

            else:
                print(view2)
                
            #loging the results on file for further investigation 
            if writeLog:
                log = '\n\ndate: {day}\nurl: {url}\nstatus: {code}\n{head} \n\n'.format(day=str(datetime.datetime.utcnow()), url=url, code=code, head=str(result.headers))
                theLogFile.write(log)
                

            
    except KeyboardInterrupt:
        print('\nThanks for choosing us goodbye!')
    if writeLog:
        theLogFile.close()




def mainDisplay():
    banner = \
    ''' 
    ************************************************
    *            E T H I O P I A N                 *
    *            P E G A S U S                     *
    *                                              *
    *                                              *
    ************************************************
    '''
    help = '''
        usage: python3 <url> <options>

        options:
        -i: write log on file
        -h: display help

        example:
        admin_finder.py https://google.com -l
        admin_finder.py http://192.168.0.0
        admin_finder.py http://e-pegasus.net:8000

        '''
    print(banner)
    userArguments = sys.argv
    
    if '-l' in userArguments or '--log' in userArguments:
        writeLog = True
    else:
        writeLog = False

   
    if '-h' in str(userArguments) or '--help' in str(userArguments) or len(userArguments) < 2 :
        print(help)
    else:
        if str(userArguments[1]).startswith('http'):
            siteName = userArguments[1]
            findLinks(siteName,writeLog)
        else:
            print(help)
        
mainDisplay()
