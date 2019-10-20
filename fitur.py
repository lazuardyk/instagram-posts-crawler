import pandas as pd

def userliketerbanyak(dfawal):
    df = dfawal.Account.drop_duplicates()
    maks = 0
    result = ''
    for username in df:
        dataperacc = dfawal.loc[dfawal['Account'] == username]
        likes = 0
        for like in dataperacc.Likes:
            if ',' in str(like):
                like = str(like)
                like = like.replace(',','')
            like = int(like)
            likes += int(like)
        if likes > maks:
            maks = likes
            result = username
    print(result, place_value(maks))

def userkomenterbanyak(dfawal):
    df = dfawal.Account.drop_duplicates()
    maks = 0
    result = ''
    for username in df:
        dataperacc = dfawal.loc[dfawal['Account'] == username]
        jumlahkomen = 0
        for komen in dataperacc.Comments:
            arr = komen.split("',")
            jumlah = len(arr)
            jumlahkomen += jumlah
        if jumlahkomen > maks:
            maks = jumlahkomen
            result = username
    print(result, maks)

def captionterpanjang(dfawal):
    df = dfawal.Post
    maks = 0
    caption = ''
    for i in df:
        if len(str(i)) > maks:
            maks  = len(i)
            caption = i
    print('Panjang caption terpanjang:' , maks)
    print(caption)
    
def commentterpanjang(dfawal):
    df = dfawal.Comments
    maks = 0
    comment = ''
    for i in df:
        if i.startswith('["'):
            arr = i.split('",')
        else:
            arr = i.split("',")
        for j in arr:
            j = j.replace(" '","").replace("['","").replace("']","").replace(' "','').replace('["','').replace('"]','').replace('\\n','')
            if len(j) > maks:
                maks  = len(j)
                comment = j
    print('Panjang comment terpanjang:' , maks)
    print(comment)

def hashtagterbanyak(dfawal):
    df = dfawal.Tag
    maks = 0
    hashtag = ''
    for i in df:
        arr = i.split("',")
        if len(arr) > maks:
            maks  = len(arr)
            hashtag = i
    print('Jumlah hashtag terbanyak:',maks)
    print(hashtag)

def place_value(number): 
    return ("{:,}".format(number)) 

def mostlikedpost(dfawal):
    filled = dfawal.fillna(0)
    df = filled.Likes
    temp = 0
    for like in df:
        if ',' in str(like):
            like = str(like)
            like = like.replace(',','')
        like = int(like)
        if like > temp:
            temp = like
    temp = place_value(temp)
    print('Jumlah like terbanyak:', temp)
    try:
        temp = int(temp)
    except:
        pass
    dfmostliked = dfawal.loc[dfawal['Likes'] == temp]
    print("Caption:", dfmostliked.Post.values[0])
        
def postkomenterbanyak(dfawal):
    df = dfawal.Comments
    maks = 0
    komen = ''
    for i in df :
        arr = i.split("',")
        if len(arr) > maks:
            maks  = len(arr)
            komen = i
    user = dfawal.loc[dfawal['Comments'] == komen]
    for j in user.Account:
        username = j
    print('Jumlah komen terbanyak:' ,maks)
    print(komen)

def pilihfitur(namafile):
    dfawal = pd.read_csv(namafile)
    dfawal.drop_duplicates(subset=['Account', 'Post'],keep='first',inplace=True)
    print(" 1. Caption terpanjang \n 2. Hashtag terbanyak dalam 1 post \n 3. Komen terpanjang\n 4. Komen terbanyak dalam 1 post\n 5. Post dengan likes terbanyak\n 6. User dengan akumulasi likes terbanyak\n 7. User dengan akumulasi comment terbanyak")
    pilih = input("Masukkan nomor fitur yang ingin Anda gunakan:  ")
    if pilih == "1":
        captionterpanjang(dfawal)
    elif pilih == "2" :
        hashtagterbanyak(dfawal)
    elif pilih == "3" :
        commentterpanjang(dfawal)
    elif pilih == "4":
        postkomenterbanyak(dfawal)
    elif pilih == "5":
        mostlikedpost(dfawal)
    elif pilih == "6":
        userliketerbanyak(dfawal)
    elif pilih == "7":
        userkomenterbanyak(dfawal)
    else:
        print("Masukkan nomor fitur yang tersedia di atas")
        pilihfitur()
              
namafile = input("Masukkan nama file CSV:\n")
pilihfitur(namafile)




