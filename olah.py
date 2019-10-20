import pandas as pd
import re

pd.set_option('display.max_columns', None)  
namafile = input("Masukkan nama file CSV yang ingin diolah menjadi Dataset Pasangan Kata:\n")
output = 'dataset-pasangankata.csv'
df = pd.read_csv(namafile)
length = len(df)
print("panjang data: "+str(length))
df.drop_duplicates(subset=['Account', 'Post'],keep='first',inplace=True)
length = len(df)
print("setelah baris duplikat dihapus: "+str(length)+"\n")

account = df.Account.drop_duplicates()
datanew = pd.DataFrame(columns=["id_user","username", "word1", "word2", "freqs"])
id_user = 1
idx = 0

for index, username in account.iteritems():
    print("Mengolah data untuk username: "+username)
    dataperacc = df.loc[df['Account'] == username]
    pairs = set()
    allcaptions = ""
    for index, row in dataperacc.iterrows():
        caption = str(row['Post'])
        allcaptions += caption+" "
        capsplit = caption.split()
        panjang = len(capsplit)
        for i in range(panjang-1):
            pairwords = capsplit[i] + " " + capsplit[i+1]
            pairs.add(pairwords)
    allcaptions = allcaptions.replace("\n","")
    occurences = {}
    count = 0
    pairsinallcaptions = []
    allcapsplit = allcaptions.split()
    panjangall = len(allcapsplit)
    for i in range(panjangall - 1):
        pairwords = allcapsplit[i] + " " + allcapsplit[i+1]
        pairsinallcaptions.append(pairwords)
    for j in pairs:
        count = 0
        for k in pairsinallcaptions:
            if j == k:
                count += 1
        occurences[j] = count
    occurences = dict(sorted(occurences.items(), key=lambda x: x[1], reverse=True))
    for key, value in occurences.items():
        words = key.split()
        word1 = re.sub(r"[^a-zA-Z0-9]+", '', words[0])
        word2 = re.sub(r"[^a-zA-Z0-9]+", '', words[1])
        word1 = word1.lower()
        word2 = word2.lower()
        if word1 == '' or word2 == '':
            continue
        data = pd.DataFrame({"id_user":[id_user], "word1":[word1], "word2":[word2], "freqs":[value]}, index=[idx])
        with open(output, 'a', encoding="utf-8", newline='') as f:
            data.to_csv(f, header=f.tell()==0)
        idx += 1
    id_user += 1