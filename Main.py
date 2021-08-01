from __future__ import print_function
import httplib2
import os
import io
import glob
import shutil
import time
import sys

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
from pathlib import Path

print (
   '......................................................\n'
   '......................Starting........................\n'
   '.................GOOGLE OCR SCANNING..................n\n'
   '......................................................\n'
   '                                                      \n'
   '                                                      \n'
    ' :////////:.                             :////////:`\n'    
    '.ssssssssss/                            .ssssssssss+\n'    
    '.sss```````                               ``````/ss+ \n'   
    '.sss                                            /ss+  \n'  
    '.sss                                            /ss+   \n' 
    '`os+         ``          ```                    -ss:    \n'
    '          :osooso:    ./so+oo/`  +ssoooos+:             \n'
    '        `os/   `+s+  .ss-   -so` +s/    `os:            \n'
    '        :ss     `ss- +s+     ..  +s/````-ss-            \n'
    '        /so      ss: os/         +sooooss+.             \n'
    '        -ss.    -ss. /so`    //` +s/   :so              \n'
    '         :so:--:so-   /so:--os/  +s/    +s+             \n'
    '          `-///:-      .:///:`   -:-    `::`            \n'
    '                                                        \n'
    '`ss+                                            -ss:    \n'
    '.sss                                            /ss+    \n'
    '.sss                                            /ss+    \n'
    '.sss```````                               ``````/ss+    \n'
    '.ssssssssss/                            .ssssssssss+    \n'
    ' -////////:.                             -////////:`    \n'
    '                                                        \n'
                                                         ' \n')
def countdown(t):
    while t > 0:
        print('........................Wait.........................')
        t -= 1
        time.sleep(1)
seconds = int(3)
countdown(seconds)
print("<<<<<<<<<<<<<<<<<<<<<<NONCAPTURE>>>>>>>>>>>>>>>>>>>>>")

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None
# Code is based on https://tanaikech.github.io/2017/05/02/ocr-using-google-drive-api/
# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/drive-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/drive'
CLIENT_SECRET_FILE = 'credentials.json'
APPLICATION_NAME = 'Drive API Python Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    credential_path = os.path.join("./", 'token.json')
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def main():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('drive', 'v3', http=http)

    # imgfile = 'image.jpeg'  # Image with texts (png, jpeg, bmp, gif, pdf)
    # txtfile = 'text.txt'  # Text file outputted by OCR

    current_directory = Path(Path.cwd())
    images_dir = Path(f'{current_directory}/images')
    raw_texts_dir = Path(f'{current_directory}/raw_texts')
   

    # check directory if exists
    if not images_dir.exists():
        images_dir.mkdir()
        print('Images folder is empty.')
        exit()

    if not raw_texts_dir.exists():
        raw_texts_dir.mkdir()
    

    images = Path(f'{current_directory}/images').rglob('*.jpeg')
    for image in images:

        # Get data
        imgfile = str(image.absolute())
        imgname = str(image.name)
        raw_txtfile = f'{current_directory}/raw_texts/{imgname[:-5]}.txt'
        

        mime = 'application/vnd.google-apps.document'
        res = service.files().create(
            body={
                'name': imgname,
                'mimeType': mime
            },
            media_body=MediaFileUpload(imgfile, mimetype=mime, resumable=True)
        ).execute()

        downloader = MediaIoBaseDownload(
            io.FileIO(raw_txtfile, 'wb'),
            service.files().export_media(fileId=res['id'], mimeType="text/plain")
        )
        done = False
        while done is False:
            status, done = downloader.next_chunk()

        service.files().delete(fileId=res['id']).execute()

        print(f"{imgname} Done.")

        
        '....................................\n'
        
if __name__ == '__main__':
    main()

def Ocrcomplete ():
    while t > 0:
        print('........................Wait.........................')
        t -= 1
        time.sleep(1)
seconds = int(3)
countdown(seconds)
print('                            \n' 
'......................................................\n'
'<<<<<<<<<<<<<<OCR SCAN COMPLETE>>>>>>>>>>>>>>>>>>>>>>>\n'
'......................................................')
def All_txts_into_One ():
    while t > 0:
        print('........................Wait.........................')
        t -= 1
        time.sleep(1)
seconds = int(3)
countdown(seconds)
print('                            \n' 
'......................................................\n'
'..............All txt-files Into One..................\n'
'......................................................')


print ('                                        \n'
'        -oydmNNNmhs/`                          \n'
'  .sNMmyo//:/+sdNMh/                           \n'
' `oMNy-          .omMd-                        \n'
'`hMm:              `yMN-                       \n'
'+MM-`////``///.-+//  dMm                       \n'
'dMd s:  o/o/  `/o:h` /MM-                      \n'
'hMd +/..s:/+..`/+-y` +MM.                      \n'
'/MM/ ---.  ---... ..`mMh         100% COMPLETE............. \n'
' sMN+`             -dMd.                       \n'
'  /mMd+.`       .:yNMm.                        \n'
'   `+hNNdysoooydmNdsdMd+.-`                    \n'
'      .:oyhhhhyo/-` `/mMNNd/`                  \n'
'                      sMMMMMd/`                \n'
'                       -hMMMMMm+`              \n'
'                         -yMMMMMm+`            \n'
'                           -yMMMMm:            \n'
'                             .yd/              \n'
'                                               \n'
'......................................................')

def All_txts_into_One_complete():
    while t > 0:
        print('........................Wait.........................')
        t -= 1
        time.sleep(1)
seconds = int(3)
countdown(seconds)
print('                            \n' 
'......................................................\n'
'......................................................\n'
'............All txt-files Into One Complete...........\n'
'......................................................\n'
'......................................................')




os.chdir('./raw_texts')
data = ""
outfilename = 'Ebook' + ".txt"

filenames = glob.glob('*.txt')

with open(outfilename, 'wb') as outfile:
    for filename in glob.glob('*.txt'):
        if filename == outfilename:
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)


os.chdir('../')
os.getcwd()

original = r'.\raw_texts\Ebook.txt'
target = r'.\Ebook.txt'

shutil.move(original,target)

def MovetoMaindiretory():
    while t > 0:
        print('........................Wait.........................')
        t -= 1
        time.sleep(1)
seconds = int(3)
countdown(seconds)
print('                            \n' 
'......................................................\n'
'......................................................\n'
'................Ebooks.txt complete...................\n'
'......................................................\n'
'......................................................')


def Delete_raw_texts():
    while t > 0:
        print('........................Wait.........................')
        t -= 1
        time.sleep(1)
seconds = int(3)
countdown(seconds)
print('                            \n'
      '                                                      \n'
'               `-/osyhddddhyso/-`                \n'
'            `/ymMMMMMMMMMMMMMMMMMMmy/`            \n'
'         `+dMMMMMMMMMMMMMMMMMMMMMMMMMMd+`         \n'
'       .sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs.       \n'
'     `sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs`     \n'
'    :NMMMMMMMMMMMMy+/////////+sNMMMMMMMMMMMMm:    \n'
'   +MMMMMMMMMMMMM: :sssssssss+ `mMMMMMMMMMMMMM+   \n'
'  /MMMMMMMMMMMMMN` :sssssssss+  hMMMMMMMMMMMMMM/  \n'
' .MMMMMMMMMd.````               `````oMMMMMMMMMN. \n'
' hMMMMMMMMMMmmh  .sdmmmmmmmmmdy-  ommNMMMMMMMMMMh \n'
'.MMMMMMMMMMMMMm  mMo:dMd:sMN//NM. oMMMMMMMMMMMMMM.\n'
':MMMMMMMMMMMMMm  NM- sMo -Mm  mM- oMMMMMMMMMMMMMM:\n'
'/MMMMMMMMMMMMMm  NM- sMo -Mm  mM- oMMMMMMMMMMMMMM/\n'
':MMMMMMMMMMMMMm  NM- sMo -Mm  mM- oMMMMMMMMMMMMMM:\n'
'`NMMMMMMMMMMMMm  NM- sMo -Mm  mM- oMMMMMMMMMMMMMN`\n'
' oMMMMMMMMMMMMm  NM- sMo -Mm  mM- oMMMMMMMMMMMMMo \n'
' `dMMMMMMMMMMMm  NM: yMy /MN``NM- oMMMMMMMMMMMMd` \n'
'  .mMMMMMMMMMMm  :mMNMMMNMMMMMNo  sMMMMMMMMMMMm.  \n'
'   .dMMMMMMMMMMo`  `.........`   :NMMMMMMMMMMd.   \n'
'     sMMMMMMMMMMMmddddddddddddddNMMMMMMMMMMMs     \n'
'      -hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh-      \n'
'        -yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy-        \n'
'          `/yNMMMMMMMMMMMMMMMMMMMMMMNy/`          \n'
'              -+ydNMMMMMMMMMMMMNdy+-              \n'
'                   `-://////:-`                   \n'
'......................................................\n'
'......................................................\n'
'<<<<<<<<DO YOU WANNA DELETE FILES IN RAW_TEXTS?>>>>>>>\n'
'......................................................\n'
'.......................................................')


print("\Are You Ok \"" + "\" ? (y/n) ", end="")

qwery = input()
files = glob.glob('./raw_texts/*.txt', recursive=True)
for f in files:
       if qwery=='y':

         try:
            os.remove(f)
            print('......................................................\n'
'......................................................\n'
'<<<<<<<<<<<<<<<ALL TxT Deleted Sucessfully!>>>>>>>>>>>\n'
'......................................................\n'
'.......................................................')          
         except IOError:
            print("\nThe file \"" + "\" is not available!")
         else:
            print("\nExiting...")



       
def Delete_Images():
    while t > 0:
        print('........................Wait.........................')
        t -= 1
        time.sleep(1)
seconds = int(3)
countdown(seconds)
print('                            \n'
      '                                                      \n'
'               `-/osyhddddhyso/-`                \n'
'            `/ymMMMMMMMMMMMMMMMMMMmy/`            \n'
'         `+dMMMMMMMMMMMMMMMMMMMMMMMMMMd+`         \n'
'       .sNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs.       \n'
'     `sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs`     \n'
'    :NMMMMMMMMMMMMy+/////////+sNMMMMMMMMMMMMm:    \n'
'   +MMMMMMMMMMMMM: :sssssssss+ `mMMMMMMMMMMMMM+   \n'
'  /MMMMMMMMMMMMMN` :sssssssss+  hMMMMMMMMMMMMMM/  \n'
' .MMMMMMMMMd.````               `````oMMMMMMMMMN. \n'
' hMMMMMMMMMMmmh  .sdmmmmmmmmmdy-  ommNMMMMMMMMMMh \n'
'.MMMMMMMMMMMMMm  mMo:dMd:sMN//NM. oMMMMMMMMMMMMMM.\n'
':MMMMMMMMMMMMMm  NM- sMo -Mm  mM- oMMMMMMMMMMMMMM:\n'
'/MMMMMMMMMMMMMm  NM- sMo -Mm  mM- oMMMMMMMMMMMMMM/\n'
':MMMMMMMMMMMMMm  NM- sMo -Mm  mM- oMMMMMMMMMMMMMM:\n'
'`NMMMMMMMMMMMMm  NM- sMo -Mm  mM- oMMMMMMMMMMMMMN`\n'
' oMMMMMMMMMMMMm  NM- sMo -Mm  mM- oMMMMMMMMMMMMMo \n'
' `dMMMMMMMMMMMm  NM: yMy /MN``NM- oMMMMMMMMMMMMd` \n'
'  .mMMMMMMMMMMm  :mMNMMMNMMMMMNo  sMMMMMMMMMMMm.  \n'
'   .dMMMMMMMMMMo`  `.........`   :NMMMMMMMMMMd.   \n'
'     sMMMMMMMMMMMmddddddddddddddNMMMMMMMMMMMs     \n'
'      -hMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh-      \n'
'        -yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNy-        \n'
'          `/yNMMMMMMMMMMMMMMMMMMMMMMNy/`          \n'
'              -+ydNMMMMMMMMMMMMNdy+-              \n'
'                   `-://////:-`                   \n'
'......................................................\n'
'......................................................\n'
'<<<<<<<<<DO YOU WANNA DELETE FILES IN IMAGES?>>>>>>>>>\n'
'......................................................\n'
'.......................................................')
print("\Are You Ok \"" + "\" ? (y/n) ", end="")

qwery = input()
files = glob.glob('./images/*.jpeg', recursive=True)
for f in files:
       if qwery=='y':

         try:
            os.remove(f)
            print('......................................................\n'
'......................................................\n'
'<<<<<<<<<<<<<<<ALL IMGs Deleted Sucessfully!>>>>>>>>>>>\n'
'......................................................\n'
'.......................................................')          
         except IOError:
            print("\nThe file \"" + "\" is not available!")
         else:
            print("\nExiting...")
