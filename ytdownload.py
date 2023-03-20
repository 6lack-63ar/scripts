#youtube downloader
#dependancies ......pip3 install pytube(make sure you got this)
#it simple just look through it
# you gotta have to change the directory path and set according to your system
import pytube
import requests
import tqdm
import os


def Download(link):
   
    
    try:
        print("starting download")
         file =pytube.YouTube(link)
         sd_file=file.streams.get_highest_resolution()
    except:
        print("******************************An Error occured******************************")
    print("Download Succesfull........")
    print("Hurray my Code works.......Hurray")

link = input("Please enter the download link........")

Download(link)
