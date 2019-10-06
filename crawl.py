import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import emoji
import random

def login(username, password):
    global driver
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(1)
    uname = driver.find_element_by_xpath('//input[@name="username"]')
    uname.clear()
    uname.send_keys(username)
    pwd = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
    pwd.clear()
    pwd.send_keys(password)
    login = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
    driver.execute_script('arguments[0].click();', login)
    time.sleep(2)

def give_emoji_free_text(text):
    return emoji.get_emoji_regexp().sub(r'', text)

def place_value(number): 
    return ("{:,}".format(number)) 

def crawlwithlogin(link):
    global driver
    global datasetfilename
    driver.get(link)
    if "Page Not Found" in driver.title:
        return "limit"
    username = link.replace("https://www.instagram.com/","").replace("/","")
    try:
        followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span')
    except:
        return "unable"
    followers = followers.get_attribute('title')
    link = driver.find_elements_by_xpath('//div/a')
    linkpost = []
    iterasi = 0
    for i in link:
        if iterasi >= 10:
            break
        if "https://www.instagram.com/p/" in i.get_attribute("href"):
            linkpost.append(i.get_attribute("href"))
            iterasi += 1

    likeslist = []
    captionlist = []
    usernamelist = []
    allcomments = []
    allhastags = []
    
    for post in linkpost:
        time.sleep(1)
        driver.get(post)
        try: ##jika terdapat views pada post, maka post adalah video
            views = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/span/span')
            button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/span[@role="button" and contains(., "views")]')
            driver.execute_script('arguments[0].click();', button)
            try:
                likes = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/div[4]/span')
            except:
                likes = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/div[4]')
            jumlahlike = likes.text
            if 'like' in jumlahlike: ## like cuma satu
                jumlahlike = jumlahlike.replace(' like', '')
            try:
                caption = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/span')
            except: ## jika tidak ada caption
                continue
            comments = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul//ul/div/li/div/div[1]/div[2]/span')
            listcomment = []
            for comment in comments:
                listcomment.append(give_emoji_free_text(comment.text))
            likeslist.append(jumlahlike)
            usernamelist.append(username)
            ab = caption.text
            captionwithoutemoji = give_emoji_free_text(ab)
            wordlist = captionwithoutemoji.split()
            hastags = []
            for word in wordlist:
                if word.startswith('#'):
                    hastags.append(word)
            allhastags.append(hastags)
            captionlist.append(captionwithoutemoji)
            allcomments.append(listcomment)
        except: ##jika tidak terdapat views pada post (error), maka post adalah foto
            try:
                caption = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/span')
            except: ##jika tidak ada caption
                continue
            try: ##jika ada kata2 liked by, maka likes ditambah satu
                likedby = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/a')
                likesfind = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/button/span')
                likesfin = likesfind.text.replace(',','')
                likes = int(likesfin) + 1
                likes = place_value(likes)
                jumlahlike = str(likes)
            except:
                try:
                    likes = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/button/span')
                except:
                    try:
                        likes = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[2]/div/div/button')
                    except:
                        continue
                jumlahlike = likes.text
                if 'like this' in jumlahlike: ##jika ada kata2 "like this" berarti like 0
                    jumlahlike = "0"
                if 'like' in jumlahlike:
                    jumlahlike = jumlahlike.replace(' like', '')
            comments = driver.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/div[1]/ul//ul/div/li/div/div[1]/div[2]/span')
            listcomment = []
            for comment in comments:
                listcomment.append(give_emoji_free_text(comment.text))
            likeslist.append(jumlahlike)
            usernamelist.append(username)
            ab = caption.text
            captionwithoutemoji = give_emoji_free_text(ab)
            wordlist = captionwithoutemoji.split()
            hastags = []
            for word in wordlist:
                if word.startswith('#'):
                    hastags.append(word)
            allhastags.append(hastags)
            captionlist.append(captionwithoutemoji)
            allcomments.append(listcomment)
    data = pd.DataFrame({"Account":usernamelist, "Post":captionlist, "Tag":allhastags, "Likes":likeslist, "Comments":allcomments})
    with open(datasetfilename, 'a', encoding="utf-8", newline='') as f:
        data.to_csv(f, header=f.tell()==0, index=False)
    return "sukses"

def crawlbanyakuser(arrlink):
    if len(arrlink) > 1:
        for link in arrlink:
            time.sleep(2)
            new = crawlwithlogin(link)
            print(link+" "+new)
            if new == "limit":
                return "limit"
        return "sukses"
    else:
        new = crawlwithlogin(arrlink[0])
        print(link+" "+new)
        if new == "limit":
            return "limit"
        return "sukses"

def getLinksofFollowers(link, limit):
    global driver
    driver.get(link)
    time.sleep(2)
    if "Page Not Found" in driver.title:
        return ["limit"]
    username = link.replace("https://www.instagram.com/","").replace("/","")
    followerscount = driver.find_element_by_xpath('//a/span')
    followerscount = followerscount.get_attribute('title')
    if followerscount == '':
        return ["private"]
    if ',' in followerscount:
        followerscount = followerscount.replace(",","")
    if limit < int(followerscount):
        limitgan = limit
    else:
        limitgan = int(followerscount)
    followersbutton = driver.find_element_by_xpath('//ul/li[2]/a')
    driver.execute_script('arguments[0].click();', followersbutton)
    time.sleep(2)
    unamelist = []
    followersList = driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
    numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    actionChain = webdriver.ActionChains(driver)
    while (numberOfFollowersInList < limitgan):
                time.sleep(2)
                followersList = driver.find_element_by_css_selector('div[role=\'dialog\'] ul')
                tes = driver.find_elements_by_xpath('/html/body/div[3]/div/div[2]/ul/div//li/div')
                try:
                    tes[-1].click()
                except:
                    return getLinksofFollowers(link, limit)
                actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))
    followers = []
    for user in followersList.find_elements_by_css_selector('li'):
        userLink = user.find_element_by_css_selector('a').get_attribute('href')
        followers.append(userLink)
        if (len(followers) == limitgan):
            break
    return followers

def main(arrakun, first, limitfoll):
    global driver
    firstperson = "https://www.instagram.com/"+first+"/"
    iakun = 1
    akunawal = arrakun[0]
    strsplit = akunawal.split(":")
    user = strsplit[0]
    print("Memakai akun: "+user)
    pwd = strsplit[1]
    driver = webdriver.Chrome('chromedriver.exe')
    pd.set_option('display.max_columns', 500)
    login(user,pwd)
    followers = getLinksofFollowers(firstperson, limitfoll)
    if followers[0] == "private":
        print("Akun pertama di private atau tidak punya followers, silahkan masukkan username yang lain!")
        return
    while followers[0] == "limit":
        if iakun == len(arrakun):
            print("Semua akun sudah limit. Program akan berhenti..")
            return
        driver.quit()
        print("Akun akan diganti karena akun sebelumnya limit..")
        pilihakun = arrakun[iakun]
        strsplit = pilihakun.split(":")
        user = strsplit[0]
        print("Memakai akun: "+user)
        pwd = strsplit[1]
        driver = webdriver.Chrome('chromedriver.exe')
        login(user,pwd)
        followers = getLinksofFollowers(firstperson, limitfoll)
        if followers[0] == "private":
            print("Akun pertama di private atau tidak punya followers, silahkan masukkan username yang lain!")
            return
        iakun += 1
    crawlwithlogin(firstperson)
    temp = followers
    i = 0
    while True:
        hasil = crawlbanyakuser(followers)
        while hasil == "limit":
            if iakun == (len(arrakun) - 1):
                print("Semua akun sudah limit. Program akan berhenti..")
                return
            driver.quit()
            print("Akun akan diganti karena akun sebelumnya limit..")
            pilihakun = arrakun[iakun]
            strsplit = pilihakun.split(":")
            user = strsplit[0]
            print("Memakai akun: "+user)
            pwd = strsplit[1]
            driver = webdriver.Chrome('chromedriver.exe')
            login(user,pwd)
            hasil = crawlbanyakuser(followers)
            iakun += 1
        followers = getLinksofFollowers(temp[random.randint(0, len(temp) - 1)], limitfoll)
        while followers[0] == "private":
            followers = getLinksofFollowers(temp[random.randint(0, len(temp) - 1)], limitfoll)
        while followers[0] == "limit":
            if iakun == (len(arrakun) - 1):
                print("Semua akun sudah limit. Program akan berhenti..")
                return
            driver.quit()
            print("Akun akan diganti karena akun sebelumnya limit..")
            pilihakun = arrakun[iakun]
            strsplit = pilihakun.split(":")
            user = strsplit[0]
            print("Memakai akun: "+user)
            pwd = strsplit[1]
            driver = webdriver.Chrome('chromedriver.exe')
            login(user,pwd)
            followers = getLinksofFollowers(temp[random.randint(0, len(temp) - 1)], limitfoll)
            iakun += 1
        temp = followers
        i += 1

limitfoll = 500
datasetfilename = "dataset-posts.csv"

print("Silahkan buat file txt yang berisi akun instagram dengan format email:password\nJika lebih dari satu akun, pisahkan dengan baris baru\n")
x = input("Nama file akun (misal: akun.txt):\n")
a = open(x, 'r')
arrakun = [line.rstrip('\n') for line in a]
jumlah = len(arrakun)
print("Total Akun: ",jumlah)
print("\nSilahkan tentukan username pertama yang ingin di scrape, username ini akan jadi acuan untuk scrapping akun yang ada di followersnya\n")
first = input("Username akun pertama yang ingin discrape (tanpa @):\n")
main(arrakun, first, limitfoll)
driver.quit()
