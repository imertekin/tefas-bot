
# TEFAS Discord Bot

- In this project, TEFAS website has been scrapped and fund information can be obtained instantly via the discord bot.
- The scrap process is carried out with the get_fon function in api.py.
- Ready to deploy to Heroku
- This is first version and I want to add new features in next versions

## Installation

- Clone Project.

```bash
  $ git clone https://github.com/imertekin/tefas-bot.git
```
- Create .env file like sample env and write your Token.

- Install dependencies

```bash
$ pip install -r requirements.txt
```

## Usage/Examples

```bash
$ python main.py
```
- You can '$code' (code = Fund code)

```bash
$TGE
```

```json
{
    "TGE": {
        "Son Fiyat (TL)": "0,081849",
        "Son 1 Ay Getirisi": "%-10,623731",
        "Günlük Getiri (%)": "%-2,2173",
        "Son 3 Ay Getirisi": "%3,729754",
        "Pay (Adet)": "25.979.604.373",
        "Son 6 Ay Getirisi": "%44,143494",
        "Fon Toplam Değer (TL)": "2.126.403.817,06",
        "Son 1 Yıl Getirisi": "%129,416711",
        "ISIN Kodu": "TRYTISB00042",
        "Platform İşlem Durumu": "TEFAS'ta işlem görüyor",
        "İşlem Başlangıç Saati": "09:30",
        "Son İşlem Saati": "17:45",
        "Fon Alış Valörü": "1",
        "Fon Satış Valörü": "3",
        "Min. Alış İşlem Miktarı ": "1.000",
        "Min. Satış İşlem Miktarı ": "1.000",
        "Max. Alış İşlem Miktarı ": " ",
        "Max. Satış İşlem Miktarı ": " ",
        "Giriş Komisyonu": " ",
        "Çıkış Komisyonu": " ",
        "Fonun Faiz İçeriği": " ",
        "Fonun Risk Değeri": "7"
    }
}
```
## Authors

- [@imertekin](https://www.github.com/imertekin)


## License

[MIT](https://choosealicense.com/licenses/mit/)

