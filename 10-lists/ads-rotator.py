from os import system
from time import sleep
ads = [
    "ads 1 blabla",
    "ads 2 blabla",
    "ads 3 blabla",
    "ads 4 blabla"
]
ads_duration  = [
    3.0,
    4.0,
    5.0,
    4.0
]
#hw1 apply the correct  duration
while True:
    ad = ads.pop(0)
    ad_d =ads_duration.pop(0)
    system('cls')
    print(">> ", ad, " <<")
    sleep(ad_d)
    ads.append(ad)
    ads_duration.append(ad_d)