# Zadanie 1 moduł 3

Lista_zakupow = {
        "piekarnia": ["chleb", "bułka", "pączek"],
        "warzywniak":["marchew","seler","rukola"]}

print("Lista zakupów")
for sklepy in Lista_zakupow:
    print(f"Idę do {sklepy.capitalize()} kupuję tu następujące rzeczy: {[produkty.capitalize() for produkty in Lista_zakupow[sklepy]]}")
print(f"W sumie kupuję {sum(map(len, Lista_zakupow.values()))} produktów")

print("Pozdrowienia")