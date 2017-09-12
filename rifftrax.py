#Load all file names into array
import os
riffDir = "D:\Videos\Rifftrax\Rifftrax Shorts"
rawFiles = os.listdir(riffDir)
files = [x for x in rawFiles if x.lower().endswith(('.avi','.mkv','.mp4','.divx','.wmv'))]

#Define Record object
class Record:
    def __init__(self,season,episode,name):
        if len(season) == 1:
            self.season = '0' + season
        else: 
            self.season = season
        if len(episode) == 1:
            self.episode = '0' + episode
        else:   
            self.episode = episode
        self.name = name

#Create array to store objects
records = []

#Read, parse rifftrax.txt and fill array
with open('rifftrax.txt','r') as key:
    for line in key:
        if line[:7] != 'Special':
            season = line[:1]
            season = season.strip()
            episode = line[4:7]
            episode = episode.strip()
            name = line[7:]
            name = name.strip()
            if name[-1:].isdigit():
                name = name[:-10]
            name = name.strip()
            rec = Record(season,episode,name)
            records.append(rec)

#Function to match name and produce new file name
def findName(test_name):
    out = ''
    print('Testing: %s' % test_name)
    for rec in records:
        if(len(rec.name) > 3):
            if(rec.name[:3] == 'The'):
                if(rec.name[4:].lower() in test_name.lower()):
                    out = 'S' + rec.season + 'E' + rec.episode + ' - ' + rec.name
                    print('Found match!: %s' % rec.name)
            else:
                if(rec.name.lower() in test_name.lower()):
                    out = 'S' + rec.season + 'E' + rec.episode + ' - ' + rec.name
                    print('Found match!: %s\n' % rec.name)
    return out

#Check files and set new name
for filename in files:
    if len(filename) > 0:
        fixedName =  findName(filename)
        if len(fixedName) > 0:
            temp = filename.split('.')
            extension = temp[len(temp)-1]
            oldName = riffDir + '\\' + filename
            newName = riffDir + '\\' + fixedName + '.' + extension
            #Leave disabled till sure of matches
            #os.rename(oldName,newName)