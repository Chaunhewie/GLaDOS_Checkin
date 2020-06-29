import requests
import os

# server酱开关，填off不开启(默认)，填on同时开启cookie失效通知和签到成功通知
sever = os.environ["SERVE"]
# 填写server酱sckey,不开启server酱则不用填
sckey = os.environ["SCKEY"]
# 填入glados账号对应cookie
cookie = os.environ["COOKIE"]


def start():
    url = "https://glados.rocks/api/user/checkin"
    url2 = "https://glados.rocks/api/user/status"
    referer = "https://glados.rocks/console/checkin"
    check_in = requests.post(url, headers={'cookie': cookie, 'referer': referer})
    state = requests.get(url2, headers={'cookie': cookie, 'referer': referer})

    if 'message' in check_in.text:
        mess = check_in.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        if sever == 'on':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+'，you have ' + time + ' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')


def main_handler(event, context):
    return start()


if __name__ == '__main__':
    start()
