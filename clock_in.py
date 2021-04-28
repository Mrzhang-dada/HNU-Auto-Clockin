from aip import AipOcr
import requests
import json
import argparse
import re

# 初始化变量
parser = argparse.ArgumentParser()
parser.add_argument('--username', type=str, default=None)
parser.add_argument('--password', type=str, default=None)
parser.add_argument('--province', type=str, default=None)
parser.add_argument('--city', type=str, default=None)
parser.add_argument('--county', type=str, default=None)
parser.add_argument('--app_id', type=str, default=None)
parser.add_argument('--api_key', type=str, default=None)
parser.add_argument('--secret_key', type=str, default=None)
args = parser.parse_args()

# 初始化OCR识别API
OCRClient = AipOcr(args.app_id, args.api_key, args.secret_key)

def captchaOCR():
    captcha = ''
    while len(captcha) != 4:
        token = json.loads(requests.get('https://fangkong.hnu.edu.cn/api/v1/account/getimgvcode').text)['data']['Token']
        captcha = OCRClient.basicGeneralUrl(f'https://fangkong.hnu.edu.cn/imagevcode?token={token}')['words_result'][0]['words']
    return token, captcha

def login():
    login_url = 'https://fangkong.hnu.edu.cn/api/v1/account/login'
    token, captcha = captchaOCR()
    login_info = {"Code":args.username,"Password":args.password,"VerCode":captcha,"Token":token}
    
    set_cookie = requests.post(login_url, json=login_info).headers['set-cookie']
    regex = r"\.ASPXAUTH=(.*?);"
    ASPXAUTH = re.findall(regex, set_cookie)[2]

    headers = {'Cookie': f'.ASPXAUTH={ASPXAUTH}; TOKEN={token}'}
    return headers

def setLocation():
    location = json.loads(requests.get(f'http://api.tianditu.gov.cn/geocoder?ds={{"keyWord":\"{args.province+args.city+args.county}\"}}&tk=2355cd686a32d016021bffbc4a69d880').text)["location"]
    real_address = "湖南大学天马学生公寓4区2栋" # 在此填写详细地址
    return location["lon"], location["lat"], real_address

def main():
    clockin_url = 'https://fangkong.hnu.edu.cn/api/v1/clockinlog/add'
    headers = login()
    lon, lat, real_address = setLocation()
    clockin_data = {"InsulatedAddress":"null",
                    "IsDiagnosis":"0",
                    "IsInCampus":"1",
                    "IsInsulated":"0",
                    "IsNormalTemperature":"null",
                    "IsSuspected":"0",
                    "IsTouch":"null",
                    "IsUnusual":"null",
                    "IsViaHuBei":"null",
                    "IsViaWuHan":"null",
                    "Longitude":lon,
                    "Latitude":lat,
                    "ModifyFields":"null",
                    "MorningTemp":"36",
                    "NightTemp":"36",
                    "RealAddress":real_address,
                    "RealCity":args.city,
                    "RealCounty":args.county,
                    "RealProvince":args.province,
                    "Temperature":"36.5"
                    "TouchInfo":"null",
                    "UnusualInfo":"null",
                    "dailyinfo":{"IsVia":"0","DateTrip":""},
                    "tripinfolist":[]
                    "toucherinfolist":[]
                    }

    clockin = requests.post(clockin_url, headers=headers, json=clockin_data)

    if clockin.status_code == 200:
        if '成功' in clockin.text or '已提交' in clockin.text:
            isSucccess = 0
    else:
        isSucccess = 1
    print(json.loads(clockin.text)['msg'])

    return isSucccess

for i in range(10):
    try:    
        main()
        break
    except:
        continue
