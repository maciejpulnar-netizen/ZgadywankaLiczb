import random  # KROPKA: użyjemy random.randint() do losowania

def gra():
    # Losujemy liczbę z zakresu 1-100
    liczba_do_odgadniecia = random.randint(1, 100)
    proby = 0
    
    print("--- GRA: ZGADNIJ LICZBĘ (1-100) ---")

    while True: # DWUKROPEK i PĘTLA: gra trwa do skutku
        try: # TRY: bo użytkownik może wpisać literę zamiast liczby
            strzal = int(input("Podaj swoją liczbę: ")) # BRAK SPACJI przed (
            proby += 1 # To samo co: proby = proby + 1
            
            if strzal < 1 or strzal > 100: # WARUNEK: zakres
                print("Mówiłem: od 1 do 100! Tracisz szansę.")
                continue

            if strzal == liczba_do_odgadniecia: # IF: sukces
                print(f"GRATULACJE! Odgadłeś w {proby} próbach.")
                break # WYJŚCIE z pętli
            elif strzal < liczba_do_odgadniecia: # ELIF: za mało
                print("Za mało! Spróbuj wyżej.")
            else: # ELSE: za dużo
                print("Za dużo! Spróbuj niżej.")
                
        except ValueError: # EXCEPT: obsługa błędnego wpisu
            print("Błąd! Musisz wpisać liczbę całkowitą.")
            continue

# Uruchomienie gry
gra()