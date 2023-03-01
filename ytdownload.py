#youtube downloader
#dependancies ......pip3 install pytube(make sure you got this)
#it simple just look through it
# you gotta have to change the directory path and set according to your system
import pytube
import requests
import tqdm
import os

path = "/home/kali/Desktop/Hits"

def Download(link):
    file =pytube.YouTube(link)
    d_file=file.streams.get_highest_resolution()
    try:
        print("starting download")
        d_file.download(output_path=path)
    except:
        print("******************************An Error occured******************************")
    print("Download Succesfull........")
    print("Hurray my Code works.......Hurray")

link = input("Please enter the download link........")

Download(link)
