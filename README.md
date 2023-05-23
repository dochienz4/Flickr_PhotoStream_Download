# Flickr_PhotoStream_Download
This is a little assignment I came up with to try to learn how to use selenium at a basic level, hope it doesn't break any laws


In main.py, change the values to yours
```python
# path folder, the folder you manna store all the images, don't let your girl see it :V 
    pathFolder = 'PATH/TO/YOUR/FOLDER/'
# the link to the photo stream on Flickr, one more time, don't let her see it :V
    photoStreamLink = 'PATH/TO/YOUR/LINK/'
# remember to change the value for yourself :V
```
after changed values, run it by your computer :)

# Bug
some cases of wrong response because flickr obfucate the html code so it can't get the normal path with href, there will be times when python will give an error and stop, please find the getlink function at the bottom of the main function, uncomment the if statement and change the value accordingly to continue unfinished files.

```python
for link in photoLink:
    if photoLink.index(link) < 73:
        continue
    print(f'Downloading {photoLink.index(link)}/{len(photoLink)}')
    download_file(getLink(link), pathFolder)
```
