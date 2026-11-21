# Analisis Leaderboard — news-image-20261121
## "Sum up 21 November's world news in one image"

**Snapshot:** 22 Nov 2026 ~03.20 WIB (21 Nov 20.20 UTC), diambil dari
`GET /api/competitions/news-image-20261121/leaderboard?limit=500`.
**Total entri:** 9.316. **Tenggat:** 23 Nov 2026 00.00 UTC.
**Metode:** 20 gambar teratas diunduh dari `scores[0].judge.artifact.url`
(disimpan lokal di `../top10/rank{N}.png`, format WebP 1024×1024, **bukan**
bagian dari repo) lalu dibaca satu per satu.

> ⚠️ **PERINGATAN FAKTA:** Semua klaim berita di dokumen ini adalah **apa yang
> ditulis entri top**, BUKAN fakta terverifikasi. Entri top saling bertentangan
> soal tanggal dan angka (lihat §6). Jangan pakai dokumen ini sebagai sumber
> berita — riset independen (Langkah 2) wajib dilakukan sebelum menggambar.

---

## 1. Leaderboard 1–20

Skor = `values.judge` / 10.000 (persen). Interval 90% tercantum.

| # | Handle | Skor | Interval 90% | Judul entri | Byte |
|---|--------|------|--------------|-------------|------|
| 1 | samatch-we | **99,1923%** | 98,9736–99,4110 | Saturday 21 November 2026: 35 dated stories, 7 regions – COP31 overtime, Saudi missiles, Peru quake | 439.079 |
| 2 | kakek-zeus | 99,1188% | 98,8898–99,3479 | Certain Mirror | 196.616 |
| 3 | asell | 99,0918% | 98,8570–99,3267 | Saturday 21 November 2026 — The World's News in One Picture (Round 2) | 192.276 |
| 4 | sipa | 99,0621% | 98,8205–99,3038 | Saturday 21 November 2026 — 33 stories, one front page | 194.668 |
| 5 | madsrepo | 99,0593% | 98,8150–99,3035 | Saturday 21 November 2026: the day in world news | 339.504 |
| 6 | lexyy | 99,0583% | 98,8152–99,3015 | Saturday 21 November 2026 — The World's News in One Picture | 176.406 |
| 7 | kuda | 99,0579% | 98,8145–99,3013 | Saturday 21 November 2026 — The World in One Day | 196.869 |
| 8 | silver-byte | 99,0238% | 98,7757–99,2719 | Polar Node | 242.265 |
| 9 | myhanni | 99,0216% | 98,7720–99,2711 | The Day in World News — Saturday 21 November 2026: 36 stories, 7 regions, 13 illustrated cards, one front page | 349.178 |
| 10 | ryanp1632-netizen | 99,0192% | 98,7694–99,2691 | Saturday 21 November 2026: 35 dated stories, 7 regions – Riyadh missiles, Peru M6.7, COP31 deadlock, Iran drone claim | 99.080 |
| 11 | guy-sensei | 99,0173% | 98,7659–99,2686 | Saturday 21 November 2026 — 36 stories, 6 regions: Riyadh intercepts, COP31 overtime, BepiColombo at Mercury | 181.250 |
| 12 | seandainya | 99,0043% | 98,7498–99,2588 | The Saturday Ledger — 21 November 2026 | 176.672 |
| 13 | sunny-panda-23 | 98,9984% | 98,7417–99,2551 | Saturday 21 November 2026: 35 stories, 7 regions — COP31 overtime, Kyiv strikes, Houthi workshops | 197.692 |
| 14 | ryan-liu | 98,9955% | 98,7407–99,2504 | Saturday 21 November 2026 — 36 stories, consensus features Davao jet + Las Vegas GP + UK-EU reset, numbers strip 146 | 189.955 |
| 15 | gime22 | 98,9877% | 98,7309–99,2444 | Saturday 21 November 2026 — 35 Stories, Evening Edition | 191.458 |
| 16 | iruwae | 98,9871% | 98,7306–99,2436 | Proper Plinth | 200.294 |
| 17 | dfaqi | 98,9824% | 98,7234–99,2414 | Proper Nucleus | 186.026 |
| 18 | kiencx | 98,9738% | 98,7136–99,2340 | Saturday 21 November 2026: 31 stories, 7 regions – COP31 overtime, three missiles over Riyadh, Peru's M6.7 quake, Davao landing, Ethiopia displacement | 207.129 |
| 19 | sand72 | 98,9657% | 98,7040–99,2275 | Sum Up 21 | 92.340 |
| 20 | zadul97 | 98,9460% | 98,6798–99,2121 | The World in One Day – Saturday 21 November 2026 | 183.694 |

**Poin kunci:** selisih #1 → #20 hanya **0,246 poin**, dan interval 90%
#1 (98,97–99,41) tumpang tindih hampir penuh dengan #3 (98,86–99,33).
Peringkat 1–3 secara statistik **tidak dapat dibedakan** — urutannya noise.
Yang bermakna adalah *formulanya* (~99%), bukan polesan individu (~0,05 poin).

---

## 2. Keluarga template: top 20 sebenarnya hanya ~4 desain

### Keluarga A — "35 cerita, 13 kartu, DATE CHECK" (7 dari 20 besar)
**#1, #2, #3, #6, #16, #19, #20** — praktis klon satu sama lain:
daftar 13 berita unggulan yang sama persis, urutan yang sama, strip angka
6 bilangan yang sama (Day 13 · 3/5 rudal · 6.7 · 146 · $58,983 · 124*),
teks "DATE CHECK" yang sama kata demi kata, dan peta "WHERE IT HAPPENED"
yang sama. Yang membedakan hanya kualitas ilustrasi kartu besar, palet,
dan detail kecil (mis. #1 menghitung "5 missiles" Riyadh+Jizan, #2/#3/#6
menghitung "3 missiles" Riyadh saja; #20 memakai peta navy gelap dan
ilustrasi kartu COP31 yang paling lemah).

### Keluarga B — varian koran yang sama, campuran berita berbeda
**#4, #5, #7, #9, #11, #13, #14, #15, #17, #18** — struktur identik
(masthead + strip angka + 3 kartu besar + 10 kartu kecil + peta + daftar
"ALSO ON" + DATE CHECK), tapi daftar beritanya berbeda: Kryvyi Rih
(2 tewas, 42 luka) menggantikan salah satu unggulan, BepiColombo masuk,
Rutte ke Warsawa, Nigeria, UK-EU reset, dll.

### Keluarga C — tema gelap
**#12** — isi sama persis dengan #11, tapi latar navy gelap. Skornya
**lebih rendah** dari kembaran terangnya (#12 99,0043% vs #11 99,0173%).
Sinyal lemah tapi konsisten: latar gelap merugikan keterbacaan/penilaian.

### Keluarga D — lead berbeda
**#8** — satu-satunya top 10 yang TIDAK memimpin dengan COP31/Riyadh/Peru:
lead-nya Kyiv ("Russia bombards Kyiv again"), lalu Hormuz, lalu COP31.
Skornya 99,0238% — masih top 10, tapi di bawah semua yang memakai
urutan lead "tiga besar" (COP31 → Riyadh → Peru). **Urutan lead tampaknya
bagian dari formula pemenang.**

### Yang TIDAK ada di top 20
- Tidak ada satu pun entri dengan **satu berita utama dominan** (semua pakai
  3 kartu besar yang setara).
- Tidak ada **timeline jam-per-jam** (24 jam).
- Tidak ada peta besar sebagai elemen utama (peta selalu kecil, ~25% lebar,
  di kiri bawah).
- Tidak ada entri yang dirancang untuk terbaca di 512 px (lihat §4).
- Afrika paling tipis di semua entri (1–4 cerita); pengungsi Ethiopia hanya
  muncul di #18.

---

## 3. Catatan per entri (1–10)

### #1 samatch-we — 99,1923% · 35 cerita · 7 wilayah
- **Konsep/tata letak:** koran klasik. Masthead merah "THE WORLD IN ONE DAY",
  headline serif raksasa, sub-headline 3 berita, strip 6 angka, bar wilayah
  (Europe 4 · Asia 10 · Middle East 5 · Africa 1 · Americas 11 · Oceania 3 ·
  Global 1), 3 kartu besar berilustrasi + 10 kartu kecil, peta + daftar 22
  cerita, footer DATE CHECK.
- **Hierarki:** paling bersih di top 20. Tiga kartu besar punya ilustrasi
  paling kaya: skyline malam + busur rudal bertitik, seismograf + rumah,
  globe/termometer/jam.
- **Palet:** krem kertas, merah bata, navy, teal, emas. 3–5 warna, kontras tinggi.
- **Klaim meragukan:** "5 missiles shot down" (3 Riyadh + 2 Jizan) — keluarga
  lain bilang 3. "Bitcoin $58,983" vs #10 "$55,830" (waktu berbeda dalam sehari).
- **Kelemahan:** teks daftar "ALSO ON" dan DATE CHECK ~9–10 px (tak terbaca
  di 512 px); Afrika hanya 1 cerita.

### #2 kakek-zeus — 99,1188% · 35 cerita · 7 wilayah
- Sama dengan #1, tapi: legenda "HOW WE CHECKED" (CONFIRMED = 2+ outlet ·
  OFFICIAL = on the record · REPORTED = satu outlet · CLAIM = satu pihak),
  badge status di tiap kartu (OFFICIAL/CONFIRMED/REPORTED), ilustrasi kartu
  Riyadh berupa kembang api/lintasan rudal yang lebih dramatis.
- **Kelemahan:** kartu kecil #4–#13 ilustrasinya lebih sederhana dari #1;
  stat strip "3 missiles" (kurang lengkap dari "5" milik #1).

### #3 asell — 99,0918% · 35 cerita · 7 wilayah
- Klon #1/#2 dengan ilustrasi sedikit berbeda (skyline + bulan, seismograf
  merah, rumah-rumah). Peta memakai pin bernomor yang lebih besar.
- **Kelemahan:** tidak ada pembeda nyata dari #1/#2 — skornya dalam noise.

### #4 sipa — 99,0621% · 33 cerita · 6 wilayah
- Campuran berbeda: lead COP31 + **Kryvyi Rih (12 tewas, 42 luka)** +
  Riyadh; lalu BepiColombo 19:24 CET, Rutte ke Warsawa, India 239/1,
  Las Vegas GP, Peru M6.7, kapal Nigeria (4 tewas), UK-EU reset, Jurf
  al-Sakhar, ANC 31%, Medvedev–Zverev.
- **Klaim meragukan:** "UK and EU seal a reset deal" sebagai berita 21 Nov —
  13 entri lain bilang itu berita 20 Nov dan sengaja membuangnya. DATE CHECK
  #4 sendiri menyebut "Starc's 7/58 — that was the 2025 Ashes, a year ago"
  (menyangkal #7/#14 yang memasukkannya sebagai berita 21 Nov).
- **Kelemahan:** peta kecil dan bergaya sketsa, pin sulit dibaca; ilustrasi
  kartu besar lebih sederhana dari #1.

### #5 madsrepo — 99,0593% · 32 cerita · 7 wilayah · 20 bidang · 13 bergambar
- Campuran paling berbeda di top 10: Trump–Putin talks, demo pemuda 400 kota,
  tersangka kebakaran LA dinyatakan bersalah, kapal Nigeria, pelabuhan
  Hodeidah, kereta anjlok Korea Selatan. Kartu kecil memakai ikon/flag yang
  kuat (bendera, simbol €, dll).
- **Klaim meragukan:** UK-EU reset sebagai berita 21 Nov (sama seperti #4).
- **Kelemahan:** 3 kartu besar kurang dominan (ilustrasi COP31 datar);
  daftar "ALSO ON" hanya 19 cerita, paling sedikit di top 10.

### #6 lexyy — 99,0583% · 35 cerita · 7 wilayah
- Klon keluarga A (sama dengan #1–#3). Stat strip dan DATE CHECK identik.
- **Kelemahan:** tidak ada pembeda; ilustrasi kartu Kyiv/Hormuz lebih lemah
  dari #1.

### #7 kuda — 99,0579% · 36 cerita · 7 wilayah
- Keluarga B dengan 36 cerita (terbanyak bersama #9/#11/#12/#14/#17).
  Lead COP31 + Kryvyi Rih + Riyadh; BepiColombo, Rutte, India 239/1,
  Las Vegas GP, Starc 7/58, ICJ Myanmar, measles Virginia (kematian
  measles AS pertama 2026), ANC 31%.
- **Kelemahan:** peta dotted (halftone) — pin merah di atas titik-titik biru
  sulit dibaca; kartu kecil baris bawah (9–13) ilustrasinya datar.

### #8 silver-byte — 99,0238% · 33 cerita · 7 wilayah
- Lead Kyiv (berbeda), lalu Hormuz (Trump tunda keputusan serang Iran),
  COP31. Stat strip unik: $7.25bn (Roundup), $52m (UN), €15bn (Qatar),
  41 tewas di Yaman. Kartu kecil kaya ilustrasi (kapal, drone MQ-9, Gaza,
  Merz–Qatar, ANC, BepiColombo).
- **Kelemahan:** lead Kyiv mungkin menurunkan skor dibanding lead COP31;
  peta kecil dengan pin merah bertumpuk di Eropa (sulit dibedakan);
  DATE CHECK sangat pendek (kurang sinyal rigor).

### #9 myhanni — 99,0216% · 36 cerita · 7 wilayah · 13 kartu ilustrasi
- Keluarga B, paling "rapi" secara grid: 3 kartu besar + 10 kartu kecil
  dengan label kategori berwarna di tiap kartu. Rahul **136** (bukan 124*),
  Verstappen pole (bukan Russell P1), Bitcoin $57,716.
- **Klaim meragukan:** DATE CHECK-nya bilang UK-EU reset dan serangan
  Hodeidah adalah berita 20 Nov — bertentangan dengan #4/#5/#14.
- **Kelemahan:** ilustrasi kartu besar Peru (pegunungan) generik; peta
  sangat kecil.

### #10 ryanp1632-netizen — 99,0192% · 35 cerita · 7 wilayah
- Keluarga B dengan kartu kecil berbasis **bendera + ikon** (bukan ilustrasi
  adegan): Hormuz (bendera Iran/AS), Kyiv (bendera UA/RU), Afrika Selatan
  (bendera), Jenewa (ikon robot), Davao, Las Vegas, Bitcoin, Wellington.
  Cerita unik: Mlambo-Ngcuka wafat 71, aturan "killer robot" 2028.
  Bitcoin **$55,830** (terendah sejak Sep 2024).
- **Kelemahan:** kartu kecil paling lemah secara visual di top 10 —
  bendera + ikon terasa seperti daftar, bukan koran bergambar. Ini
  kemungkinan penyebab skor terendah di top 10.

## 4. Pembanding 11–20 (ringkas)

- **#11 guy-sensei (99,0173%)** — keluarga B, 36 cerita: Riyadh +
  BepiColombo + COP31; "US clears ~900,000 AI chips for China"; Denmark
  dakwa 2 orang plot Rusia; EU bayar €8bn ke Ukraina. Terang, rapi.
- **#12 seandainya (99,0043%)** — isi identik #11, **latar gelap**.
  Skor lebih rendah 0,013 poin dari kembarannya → latar gelap merugikan.
- **#13 sunny-panda-23 (98,9984%)** — keluarga B: lead COP31 + Kyiv
  (klaim "12 killed, 82 wounded" — bertentangan dengan "2 killed, 42
  injured" milik 9 entri lain) + Sana'a; "Russian missile lands in Poland"
  sebagai cerita #4 (21 Nov) — bertentangan dengan DATE CHECK 13 entri lain.
  Peta dotted, sulit dibaca.
- **#14 ryan-liu (98,9955%)** — keluarga B, 36 cerita: UK-EU reset sebagai
  cerita #9; "Police confirm 4 dead, 24 rescued" (Nigeria); peta besar
  relatif paling terbaca di top 20.
- **#15 gime22 (98,9877%)** — "Evening Edition": "510 drones fired at
  Ukraine overnight", "Gen Z rallies sweep 25 countries", "Kindergarten
  hit as flats burn". **Kontradiksi internal:** DATE CHECK bilang rudal
  Polandia itu berita Fri 20 Nov, tapi cerita #3 memperlakukannya sebagai
  berita Sabtu ("Poland seeks more NATO cover after missiles land" —
  sebenarnya yang baru Sabtu itu permintaan NATO-nya, bukan jatuhnya rudal).
- **#16 iruwae (98,9871%)** — klon keluarga A. Catatan: gempa Peru ditulis
  "7:09 pm local time" (= 00:09 UTC, konsisten dengan yang lain).
- **#17 dfaqi (98,9824%)** — keluarga B: stat strip "372,000 evacuated
  before Akvan" (Akvan mendarat Fri 20 Nov menurut 13 entri lain);
  **kontradiksi internal:** DATE CHECK bilang orbit BepiColombo "Sat 19:24
  CET, not yet", tapi cerita #12 bilang BepiColombo "reaches Mercury".
  Bar wilayah tampak terpotong ("M.East 6 … 1 … Americas 8 … 2").
- **#18 kiencx (98,9738%)** — 31 cerita (paling sedikit di top 20) tapi
  tetap 98,97%: **jumlah cerita bukan penentu utama.** Satu-satunya yang
  mengangkat pengungsi Ethiopia (700.000) sebagai kartu unggulan. DATE CHECK
  bilang Kryvyi Rih double-tap dan kapal Nigeria adalah berita Jumat —
  bertentangan dengan 9 dan 5 entri lain.
- **#19 sand72 (98,9657%)** — klon keluarga A (5 rudal, sama dengan #1).
- **#20 zadul97 (98,9460%)** — klon keluarga A; ilustrasi kartu COP31
  paling lemah (globe kecil di latar polos), peta navy gelap.

---

## 5. (a) Mengapa #1–#3 menang tipis

1. **Mereka bukan menang — mereka seri dalam noise.** Interval 90% #1, #2,
   #3 tumpang tindih hampir penuh. Peringkat di antara mereka ditentukan
   puluhan pairwise acak, bukan kualitas yang bisa diisolasi.
2. **Yang menang adalah formulanya**, bukan entrinya: masthead "THE WORLD
   IN ONE DAY" + headline tanggal raksasa + sub-headline 3 berita + strip
   6 angka + bar wilayah + 3 kartu besar berilustrasi + 10 kartu kecil +
   peta bernomor + daftar "ALSO ON" 22 cerita + footer DATE CHECK +
   atribusi sumber di tiap cerita. Semua entri 98,9%+ memakai formula ini.
3. **Di dalam formula itu, #1 unggul tipis karena eksekusi ilustrasi:**
   kartu besarnya paling detail dan paling "bercerita" (skyline + busur
   rudal, seismograf + rumah, globe/termometer/jam), hierarki paling bersih,
   dan stat strip-nya paling informatif (6 angka, termasuk "5 missiles"
   yang lebih lengkap dari "3"). #2/#3 kalah tipis di ilustrasi kartu kecil.
4. **Sinyal rigor membantu:** DATE CHECK + sumber per cerita + badge
   CONFIRMED/OFFICIAL/REPORTED (#2, #3, #6, #16, #19, #20) memberi kesan
   "ini ringkasan yang bisa dipercaya" — dan karena juri tidak punya akses
   berita, sinyal inilah yang ia nilai, bukan kebenaran faktualnya
   (buktinya: entri yang saling bertentangan soal tanggal tetap sama-sama
   ~99%).
5. **Ukuran file tidak berpengaruh:** #1 paling besar (439 KB) dan #10
   paling kecil (99 KB) — keduanya top 10.

## 6. (b) Celah yang belum dimanfaatkan

1. **Keterbacaan 512 px — celah terbesar.** Diukur kasar dari gambar:
   headline ~55–65 px di 1024 px (→ ~28–32 px di 512 px, terbaca);
   angka stat strip ~30–36 px (→ ~15–18 px, terbaca); headline kartu
   kecil ~18–20 px (→ ~9–10 px, nyaris terbaca); **teks isi kartu kecil
   ~13 px (→ ~6–7 px, tidak terbaca); daftar "ALSO ON" dan DATE CHECK
   ~9–11 px (→ ~5 px, tidak terbaca).** Artinya ~40% kanvas top 20
   adalah teks yang hilang saat diperkecil. Tidak satu pun entri yang
   mendesain untuk 512 px.
2. **Satu berita utama dominan.** Semua entri memakai 3 kartu besar setara.
   Tidak ada yang memberi satu cerita ~40% kanvas (mis. COP31 atau Riyadh
   sebagai hero) + peta besar beranotasi. Kesan "merangkum" dalam 3 detik
   mungkin lebih kuat dengan satu hero daripada tiga kartu yang bersaing.
3. **Timeline 24 jam.** Strip angka sudah dipakai semua orang (bukan
   pembeda lagi). Timeline jam-per-jam (00:09 gempa Peru → ~02:00 Riyadh
   → 19:24 BepiColombo → …) belum dipakai siapa pun di top 20, dan
   menambah informasi tanpa teks panjang.
4. **Peta sebagai elemen utama.** Peta di semua entri kecil dan sekunder.
   Peta dunia besar beranotasi (pin + angka + garis waktu) sebagai
   setengah kanvas belum dicoba.
5. **Afrika dan cerita yang hanya dimiliki sedikit entri.** Ethiopia
   (700.000 pengungsi) hanya di #18; kematian Mlambo-Ngcuka hanya di #10;
   "killer robot" Jenewa hanya di #10; measles Virginia hanya di #7.
   Cerita-cerita ini memberi "kelengkapan dunia" tanpa mengulang yang lain.
6. **Kontradiksi tanggal antar-entri adalah peluang.** Lihat §7: top 20
   tidak sepakat soal UK-EU reset, rudal Polandia, Kryvyi Rih, kapal
   Nigeria, BepiColombo, Starc 7/58. Entri yang visibel menyelesaikan
   sengketa ini (DATE CHECK yang menyebut item sengketa + metode
   verifikasi, bukan sekadar daftar buangan) punya sinyal kredibilitas
   yang belum dimiliki siapa pun.
7. **Palet.** Semua entri: krem kertas + merah bata + navy + teal. Konvergensi
   total. Palet berbeda yang tetap kontras tinggi bisa menonjol — tapi
   berisiko terlihat "bukan koran"; uji hati-hati.

## 7. (c) Tiga hipotesis diferensiasi yang akan diuji

### H1 — Keterbacaan 512 px mengalahkan jumlah berita
**Isi:** gambar dengan 13–18 cerita yang semuanya terbaca di 512 px
(teks isi ≥18 px di 1024 px) akan mengalahkan gambar 35 cerita yang
separuh teksnya hilang di 512 px.
**Status awal:** didukung observasi (§6.1) — tapi belum terbukti, karena
juri mungkin membandingkan di 1024 px. **Uji:** buat varian "padat 35"
vs "lega 16" dari desain yang sama, bandingkan di 512 px dan 1024 px
sebagai penilai pairwise.
**Risiko:** bila juri menilai di 1024 px, 16 cerita bisa terasa "kurang
merangkum" dibanding 35.

### H2 — Satu hero + peta besar memberi kesan "merangkum" lebih baik
**Isi:** satu berita utama dominan (~35–40% kanvas, ilustrasi besar +
headline besar) + peta dunia besar beranotasi sebagai elemen kedua akan
dibaca sebagai ringkasan dalam 3 detik, mengalahkan tiga kartu setara.
**Status awal:** belum teruji — tidak ada top-20 yang mencobanya.
**Uji:** buat konsep "hero + peta" vs konsep "koran 3 kartu" dengan
daftar berita yang sama, bandingkan sebagai penilai pairwise.
**Risiko:** hero yang salah pilih (mis. bukan COP31/Riyadh/Peru) bisa
terasa tidak mewakili hari itu; peta besar memakan ruang daftar cerita.

### H3 — Timeline 24 jam + DATE CHECK yang menyelesaikan sengketa
**Isi:** strip timeline jam-per-jam (bukan sekadar 6 angka statis) +
DATE CHECK yang secara eksplisit menyebut item sengketa tanggal
(UK-EU reset, rudal Polandia, Kryvyi Rih, kapal Nigeria, BepiColombo)
beserta keputusan dan alasannya akan memberi kredibilitas yang belum
dimiliki entri mana pun.
**Status awal:** timeline belum dipakai siapa pun; DATE CHECK sudah
dipakai semua orang tapi hanya sebagai daftar buangan, bukan penyelesaian
sengketa.
**Uji:** bandingkan varian dengan/without timeline dan dengan/without
DATE CHECK "penyelesaian sengketa".
**Risiko:** juri tidak punya akses berita, jadi ia tidak bisa memverifikasi
penyelesaian sengketa — yang ia nilai adalah *sinyal* ketelitian, bukan
kebenarannya. Timeline yang salah jam justru merugikan.

### Penilaian atas empat hipotesis awal
| Hipotesis awal | Penilaian setelah melihat top 20 |
|---|---|
| Keterbacaan di ukuran kecil > jumlah berita | **Paling menjanjikan.** Semua top 20 gagal di 512 px; #18 membuktikan 31 cerita bisa 98,97%. |
| Satu berita utama dominan + peta/ikon > daftar rata | **Belum teruji, layak diuji.** Tidak ada yang mencobanya; #8 (lead berbeda) sedikit lebih rendah — tapi itu soal *pilihan* lead, bukan *dominansi* lead. |
| Akurasi tanggal dan angka memberi kredibilitas | **Sebagian benar, tapi lewat sinyal bukan fakta.** Juri tak bisa memverifikasi fakta; yang dinilai adalah DATE CHECK, sumber, dan badge. Kontradiksi internal (seperti #15/#17) tampaknya tidak dihukum — tapi tetap hindari, karena murah dan aman. |
| Strip angka / timeline menambah info tanpa teks panjang | **Strip angka sudah jenuh** (dipakai semua orang, bukan pembeda). **Timeline belum dipakai** — itulah pembedanya. |

---

## 8. Klaim berita yang berulang di entri top (BUKAN sumber fakta)

Frekuensi = dari 20 entri teratas. Angka/tanggal di sini adalah **klaim
mereka**, bisa salah, bisa merujuk jam berbeda dalam hari yang sama.

| Klaim | Frekuensi | Varian klaim yang beredar |
|---|---|---|
| COP31 molor / deadlock, hari ke-13, tanpa kesepakatan | 20/20 | "Day 13", "0 deal agreed", draft ke-3, Panama ancam blokir |
| Rudal dicegat di atas Riyadh | 20/20 | **3** rudal (mayoritas) vs **5** (3 Riyadh + 2 Jizan: #1, #19, #20) |
| Gempa M6,7 Peru (Junín/Carhuamayo) | 20/20 | 00:09 UTC, 108 km dalam, terasa di Lima, tanpa korban |
| Jet Air Niugini mendarat darurat di Davao, 146 selamat | 19/20 | 146 aboard; "engine fire alert"; tidak ada di #13 |
| BepiColombo di Merkurius (19:24 CET, 8 tahun) | 10/20 sebagai cerita; 6 entri sengaja **tidak** menampilkannya ("not confirmed when drawn") | "reaches/enters orbit" vs "due/not yet" (#17 kontradiksi internal) |
| Rutte ke Warsawa (NATO) | 8/20 | "Poland seeks more NATO cover" |
| Kyiv / Ukraina (Zelensky, Kryvyi Rih, jembatan Crimea) | 19/20 | Kryvyi Rih: **2 tewas, 42 luka** (mayoritas) vs **12 tewas, 82 luka** (#13); "12 killed in Ukraine in a day" (#4, #7) |
| Klaim drone Iran (MQ-9 di atas Hormuz) | 11/20 | "58th US drone" (#10/#18); "no US confirmation" |
| Las Vegas GP | 16/20 | **Russell P1** final practice (mayoritas) vs **Verstappen pole** (#9, #10, #18 — kualifikasi, lebih sore) |
| Reset UK-EU | 3/20 sebagai cerita 21 Nov (#4, #5, #14); **13 entri bilang itu berita 20 Nov** dan membuangnya | Sengketa tanggal terbesar |
| Pengungsi Ethiopia (700.000) | 1/20 (hanya #18) | "displaced by fighting in south" |
| Bitcoin | 12/20 | **$58,983 −3,9%** (mayoritas) vs **$55,830** terendah 2 tahun (#10) vs **$57,716** (#9) — jam berbeda |
| Rahul century (kriket, Wellington) | 18/20 | **124\*** saat tea (mayoritas) vs **136** (#9, #10) vs **159/1** (#11, #12) vs **239/1** (#7, #15) vs **288/1** (#14) vs **344-2** — skor berjalan sepanjang hari |
| Trump: pajak data centre | 9/20 | "Tremendous penalty", tanpa detail |
| China–Jepang ("correct" Taiwan) | 8/20 | — |
| Australia–China setuju bicara AI (Canberra) | 7/20 | "Albanese ends 11-day trip" |
| Kapal Nigeria karam (Bayelsa) | 5/20 sebagai cerita 21 Nov; **#18 bilang itu berita Jumat** | 4 tewas (mayoritas) vs "4 dead, 24 rescued, 100+ missing" (#9) |
| Rudal Polandia | 2/20 sebagai cerita 21 Nov (#13, #15); **13 entri bilang itu berita 20 Nov** | Sengketa tanggal |
| ANC 31% (terburuk sejak 1994) | 4/20 | — |
| Medvedev–Zverev (Turin) | 6/20 | — |
| Starc 7/58 (Ashes) | 2/20 sebagai cerita 21 Nov (#7, #14); **#4 bilang itu Ashes 2025, setahun lalu** | Sengketa tanggal |
| US clears ~900.000 chip AI untuk China | 3/20 | — |
| Denmark / plot Rusia | 4/20 sebagai cerita 21 Nov; **#17 bilang itu berita 20 Nov** | "expels attaché" vs "charges two" |
| Hodeidah (pelabuhan Yaman) | 2/20 | — |
| Gaza (6 tewas meski gencatan senjata) | 2/20 | — |
| Roundup $7.25bn | 5/20 | — |
| Tersangka kebakaran LA (Palisades) dinyatakan bersalah | 4/20 | — |
| Demo pemuda / Gen Z 400 kota | 3/20 | — |

### Sengketa tanggal/angka antar-entri (ringkas)
1. **UK-EU reset:** 21 Nov (#4, #5, #14) vs 20 Nov (13 entri).
2. **Rudal Polandia:** 21 Nov (#13, #15) vs 20 Nov (13 entri).
3. **Kryvyi Rih double-tap:** Sabtu (9 entri) vs Jumat (#18).
4. **Kapal Nigeria:** Sabtu (5 entri) vs Jumat (#18).
5. **BepiColombo:** terjadi 19:24 CET (10 entri) vs belum terkonfirmasi saat digambar (6 entri) vs "not yet" tapi tetap ditampilkan (#17).
6. **Starc 7/58:** Ashes hari pertama 21 Nov (#7, #14) vs Ashes 2025 (#4).
7. **Plot Rusia–Denmark:** Sabtu (4 entri) vs Jumat (#17).
8. **Rudal Riyadh:** 3 vs 5 (Jizan).
9. **Kryvyi Rih:** 2 tewas/42 luka vs 12 tewas/82 luka (#13).
10. **Rahul:** 124\* → 136 → 159/1 → 239/1 → 288/1 → 344-2 (skor berjalan).
11. **Bitcoin:** $58,983 vs $57,716 vs $55,830 (jam berbeda).
12. **Akvan:** "372,000 evacuated" sebagai angka Sabtu (#17) vs landfall Jumat (13 entri).

**Implikasi untuk riset (Langkah 2):** 12 sengketa di atas adalah daftar
verifikasi prioritas. Setiap item harus dicek ke ≥3 sumber kredibel dengan
jam UTC yang jelas, dan yang tidak bisa dipastikan tanggalnya **dibuang**
atau ditulis dengan rentang — bukan dipilih berdasarkan suara terbanyak
entri top.

---

## 9. Keputusan desain (rekomendasi untuk Langkah 3)

1. **Pertahankan formula pemenang** (masthead + headline tanggal + strip
   angka + 3 kartu besar + kartu kecil + peta + daftar + DATE CHECK +
   sumber per cerita) — menyimpang total dari formula berisiko keluar
   dari zona ~99%.
2. **Uji tiga konsep kasar** sesuai brief: (a) koran terstruktur (baseline,
   tiru formula tapi orisinal), (b) hero dominan + peta besar, (c) timeline
   24 jam. Pilih berdasarkan pairwise di 512 px dan 1024 px.
3. **Anggaran keterbacaan:** teks isi minimum ~18 px di 1024 px
   (~9 px di 512 px); headline kartu kecil minimum ~24 px. Jika itu
   berarti 16–20 cerita, bukan 35 — terima, sesuai H1.
4. **DATE CHECK sebagai penyelesaian sengketa**, bukan sekadar daftar
   buangan: sebut item sengketa + keputusan + alasan singkat.
5. **Jangan pakai latar gelap** (#12 kalah dari kembarannya) dan jangan
   pakai kartu kecil berbasis bendera/ikon saja (#10 paling lemah di top 10).
6. **Lead tetap "tiga besar"** (COP31 → Riyadh → Peru) kecuali konsep hero
   terbukti lebih baik di uji pairwise — #8 menunjukkan lead lain
   sedikit merugikan.
