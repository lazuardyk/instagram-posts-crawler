import pandas as pd
import time

df = pd.read_csv('dataset-pasangankata.csv')
kata = input("masukkan kata:")
start = time.time()
dfsearch = df.loc[df['word1'] == kata] ## mencari data yang mengandung kata yang diinput
newdf = pd.DataFrame(columns=["word1", "word2", "freqs"])
freqstotalkiri = 0 ## frekuensi total dari tabel word1
freqstotalkanan = 0 ## frekuensi total dari tabel word2
maks = 0 ## hasil perbandingan peluang
hasilpredict = '' ## hasil prediction

for index, row in dfsearch.iterrows():
    freqword = 0
    cariword2 = df.loc[df['word2'] == row['word2']]
    for freq in cariword2.freqs:
        freqword += freq
    freqstotalkanan += freqword
    freqstotalkiri += int(row['freqs'])

for index, row in dfsearch.iterrows():
    
    cari1 = df.loc[(df['word1'] == kata) & (df['word2'] == row['word2'])]
    freq1 = 0
    for freq in cari1.freqs:
        freq1 += int(freq)

    freq2 = 0
    cari2 = df.loc[df['word2'] == row['word2']]
    for freq in cari2.freqs:
        freq2 += int(freq)

    p1 = freq1 / freq2
    p2 = freq2 / freqstotalkanan
    p3 = freqstotalkiri / freqstotalkanan

    rumus = (p1 * p2) / p3
    if rumus > maks:
        maks = rumus
        hasilpredict = row['word2']
print("hasil next word prediction:")
print(kata, hasilpredict)
print()
print("dengan skor:")
print(rumus)
print()
end = time.time()
print("lama waktu proses:")
print(end - start)

