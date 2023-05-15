import requests
def uploadImage(camid):
    url = "http://usstaging.ivisecurity.com:777/common/uploadFile_1_0"
    fileName = 'D:/Streaming Releated/s3Snapshot/'+camid+'.png'

    payload = {'requestName': 'snapshots',
    'assetName': camid,}
    # 'levels': camid}
    files=[
      ('assetFile',(camid+'.png',open(fileName,'rb'),'image/png'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)