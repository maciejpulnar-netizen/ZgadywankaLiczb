import random

def gra():
    # KROPKA: wywołujemy funkcję z modułu random
    liczba_do_odgadniecia = random.randint(1, 100)
    proby = 0
    
    print("--- GRA: ZGADNIJ LICZBĘ (1-100) ---")

    while True: # DWUKROPEK: początek pętli
        try: # TRY: sprawdzamy czy użytkownik wpisuje cyfry
            strzal = int(input("Podaj swoją liczbę: "))
            proby += 1 # Inkrementacja (licznik prób)
            
            if strzal < 1 or strzal > 100:
                print("Mówiłem: od 1 do 100!")
                continue # Wróć na start pętli

            if strzal == liczba_do_odgadniecia:
                print(f"GRATULACJE! Odgadłeś w {proby} próbach.")
                break # Wyjście z pętli
            elif strzal < liczba_do_odgadniecia:
                print("Za mało! Spróbuj wyżej.")
            else:
                print("Za dużo! Spróbuj niżej.")
                
        except ValueError: # EXCEPT: jeśli int() wyrzuci błąd
            print("Błąd! Musisz wpisać liczbę całkowitą.")

gra()