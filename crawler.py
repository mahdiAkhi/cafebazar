import requests
import json

url = 'https://api.cafebazaar.ir/rest-v1/process/ReviewRequest'

# ('ir.divar', 'divar'), ('com.sheypoor.mobile','sheypoor'), ('ir.basalam.app', 'basalam'),('com.whatsapp', 'whatsapp'),('ir.resaneh1.iptv', 'roobika'), ('ir.eitaa.messenger', 'eitaa'),
# ('ir.android.baham', 'baham'), ('ir.alibaba', 'alibaba'),('com.instagram.android', 'instagram'), ('com.wisgoon.android', 'wisgoon'), ('com.sibche.aspardproject.app','up'), ('ir.sep.sesoot', '724'), ('com.mrbilit.app', 'mrbilit')('cab.snapp.passenger', 'snapp'),
# ('com.supercell.clashofclans', 'clashOfClans'),
apps = [('com.supercell.clashofclans', 'clashOfClans'),
        ('co.palang.QuizOfKings', 'QuizOfKings'), ('com.zoodfood.android', 'zoodfood'), ('taxi.tap30.passenger', 'tap30'), ('com.sibche.aspardproject.app', 'UP'),('ir.hafhashtad.android780','780'),
        ('ir.sep.sesoot','720')]


filters = {'versionCode', 'likedByMe', 'badgeIconURL', 'avatarURL',
           'userRepliesCount', 'userRepliesAvatarUrls', 'isEdited', 'reviewAuditState'}

for app in apps:
    rd=[]
    start, end, step = 0, 100, 100
    payload = {
        "properties": {
            "language": 2,
            "clientID": "klsdj=sdfkjsSFGD5515sdfjlkj0sldk",
            "deviceID": "klsdj=sdfkjsSFGD5515sdfjlkj0sldk",
            "clientVersion": "web"
        },
        "singleRequest": {
            "reviewRequest": {
                "packageName": app[0],
                "start": start,
                "end": end
            }
        }
    }

    try:
        while(end <100000):
            print(f"---{app[1]}--start item {start} to {end}-----")
            res = requests.get(url, json=payload)
            reviews = res.json()['singleReply']['reviewReply']['reviews']
            
            if len(reviews)<1:
                break

            for rev in reviews:
                rev['app']=app[1]
                rd.append({key: val for key, val in rev.items() if key not in filters})
            start = end+1
            end = end + step
            payload['singleRequest']['reviewRequest']['start'] = start
            payload['singleRequest']['reviewRequest']['end'] = end
            print("---------------end------------------")

    except:
        
        file = open(f'{app[1]}.json', 'w')
        json.dump(rd,file)
        print("*****finish with error*****")

    file = open(f'{app[1]}.json', 'w')
    json.dump(rd, file)
