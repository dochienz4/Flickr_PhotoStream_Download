from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()


# get vertical size of web content
# credit: https://www.selenium.dev/documentation/webdriver/actions_api/wheel/#scroll-by-given-amount
def getRectVertical():
    footer = driver.find_element(By.TAG_NAME, "footer")
    return footer.rect['y']

# download a file using requests
def download_file(url:str, saveFolder:str):
    filename = url.split('/')[-1]
    print(f'Downloading filename: {filename}...')
    response = requests.get(url)
    open(f'{saveFolder}/{filename}', 'wb').write(response.content)

# this function run well, don't touch it anymore :)
# Adabra Kedavra, I wish i only need to write this once...
def getLink(siteURL:str):
    siteCode = requests.get(siteURL).content.decode("utf-8")
    filt = 'https:' + siteCode.split(',"key":"o","src":"')[1].split('"}}')[0].replace('\\', '')
    return filt.split('_o')[0] + '_o_d' + filt.split('_o')[1]

#  this fuction is used to scroll the wheel into the bottom, flickr using lazyload so it make sure that everything is loaded
# same credit with getRectVertical funcion :)
def scrollAction(rect, counter = 5):
    ActionChains(driver).scroll_by_amount(0, rect).perform()
    sleep(1) # sleep for a little while to make sure data is loaded
    if counter > 0:
        scrollAction(getRectVertical(), counter - 1)
            

# the fuction which everybody should know about :V im joke :)
def main():
    # path folder, the folder you manna store all the images, don't let your girl see it :V 
    pathFolder = 'PATH/TO/YOUR/FOLDER/'

    # the link to the photo stream on Flickr, one more time, don't let her see it :V
    photoStreamLink = 'PATH/TO/YOUR/LINK/'
    
    # remember to change the value for yourself :V
    photoLink = []

    # start the pain :)
    driver.get(photoStreamLink)
    scrollAction(getRectVertical())

    # get all 100 link
    overlay = driver.find_elements(By.CLASS_NAME, "overlay")
    for link in overlay:
        photoLink.append(link.get_attribute('href'))
    driver.close()

    for link in photoLink:
        # if photoLink.index(link) < 86:
        #     continue
        print(f'Downloading {photoLink.index(link)}/{len(photoLink)}')
        download_file(getLink(link), pathFolder)

if __name__ == '__main__':
    main()
