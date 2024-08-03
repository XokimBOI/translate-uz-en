from googletrans import Translator

def tarjima_qil(matn, manba_til='auto', nishon_til='en'):
    tarjimon = Translator()
    tarjima = tarjimon.translate(matn, src=manba_til, dest=nishon_til)
    return tarjima.text

# Foydalanuvchi matn kiritsin
matn = input("Matnni kiriting: ")

# Tarjima qilish
tarjima = tarjima_qil(matn)

print(tarjima)
