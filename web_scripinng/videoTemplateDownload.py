import requests
import os
from urllib.parse import urlparse

import asyncio
import time
import json
def call_download(delay, data):
    
    # {
    #     "title": "206_birthday",
    #     "video_thumb": "http://flickapp9.com/Infiapp/AdminPanelV4/video1thumb/1576231858_thumbnail.jpg",
    #     "video_link": "http://flickapp9.com/Infiapp/AdminPanelV4/video1data/1576231789_output.mp4",
    #     "video_zip": "http://flickapp9.com/Infiapp/AdminPanelV4/video1zip/206_birthday.zip",
    #     "category": "Birthday"
    #     }


    # print(data)
    imageName = data["title"]
    videoUrl = data["video_zip"]
    video_thumb = data["video_thumb"]
    video_sample = data["video_link"]

    imgName=os.path.basename(data["title"])
    video_thumbName = os.path.basename(data["video_thumb"])
    video_sampleName = os.path.basename(data["video_link"])

    videoName = os.path.basename(videoUrl)
    if not os.path.exists("videoTemplate"):
        os.mkdir("videoTemplate")
    path = "videoTemplate/"+os.path.splitext(imgName)[0]
    # print(path)
    try:
        if not os.path.exists(path):
            os.mkdir(path)
       
        if not os.path.exists(path+"/"+video_thumb):
            print(video_thumbName)
            # with urllib.request.urlopen(video_thumb) as response, open(path+"/"+imgName, 'wb') as out_file:
            #     data = response.read() # a `bytes` object
            #     out_file.write(data)
            #     print( "%s downloaded!\n"%imgName )
            r = requests.get(video_thumb, stream = True) 
            with open(path+"/"+video_thumbName, 'wb') as f: 
                for chunk in r.iter_content(chunk_size = 1024*1024): 
                    if chunk: 
                        f.write(chunk) 
            print( "%s downloaded!\n"%video_thumbName )
        if not os.path.exists(path+"/"+video_sample):
            print(video_sampleName)
            r = requests.get(video_sample, stream = True) 
            with open(path+"/"+video_sampleName, 'wb') as f: 
                for chunk in r.iter_content(chunk_size = 1024*1024): 
                    if chunk: 
                        f.write(chunk) 
            print( "%s downloaded!\n"%video_sampleName )    
        if not os.path.exists(path+"/"+videoName):
            print(videoUrl)
            r = requests.get(videoUrl, stream = True) 
            with open(path+"/"+videoName, 'wb') as f: 
                for chunk in r.iter_content(chunk_size = 1024*1024): 
                    if chunk: 
                        f.write(chunk) 
            print( "%s downloaded!\n"%videoName )
        # with urllib.request.urlopen(url+data['video'].path) as response, open(path+"/"+videoName, 'wb') as out_file:
        #     data = response.read() # a `bytes` object
        #     out_file.write(data)
        #     print(path)
    except OSError as error: 
        # pass
        print(error)  

async def callVideoList(videosList):
    loop = asyncio.get_event_loop()
    for item in videosList:
        print(item["title"])
        try:
            await loop.run_until_complete(call_download(5000,item))
        except Exception as e:
            pass
    pass

async def main():

    videosList = []
    # await callVideoList(videosList)
    try:
        with open('test.json') as f:
            videosList = json.load(f)
        await callVideoList(videosList)
    except Exception as e:
        print(e)
        pass

asyncio.run(main())
