'''
1.Utwórz zmienną quote i przypisz jej następującą wartość:   'A good programmer is someone who always looks both ways before crossing a one-way street'
2.Wyświetl tekst napisany tylko wielkimi literami
3.Wyświetl tekst zapisany tylko małymi literami
4.Sprawdź czy tekst kończy się słowem 'street'
5.Sprawdź czy tekst jest zapisany wielkimi literami
6.Sprawdź, czy tekst skonwertowany do wielkich liter jest zapisany wielkimi literami (Zastosuj złożenie funkcji)
7.Poszukaj na której pozycji (licząc od zera) znajduje się w tekście słowo (podnapis)  'one'
8.Zamień w tekście słowo (podnapis) 'one' na '1'
9.Zamień w tekście słowo (podnapis) 'one' na '1' a słowo 'both' na 2
10.Rozdziel napis na mniejsze napisy ze względu na znak rozdzielający jakim jest spacja
11.Sprawdź czy napis jest liczbą, liczbą dziesiętną, napisem bez cyfr, napisem z literami i cyframi
'''

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'
print(quote.upper())
print(quote.lower())

quote.endswith('street')

quote.isupper()

quote.upper().isupper()

quote.find('one')

quote.replace('one', '1')

quote.replace('one', '1').replace('both','2')

quote.split(' ')

quote.isdigit()
quote.isdecimal()
quote.isalpha()
quote.isalnum()
