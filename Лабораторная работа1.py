#Лабораторная работа1, вариант 3, Козлова Маргарита 48 гр.
def hamming_distance(s, t):
#s: Первая строка.
#t: Вторая строка.
  if len(s) != len(t):
    print("Строки должны быть одинаковой длины.")
    return -1 #если количество символов строке не совпадает

  distance = {s[i]!=t[i]: distance+=1}


  return distance #если количество символов в строке совпадает, то ищем количество точечных мутаций
# Пример использования:
s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"
distance = hamming_distance(s, t)

if distance != -1:
    print("Расстояние Хэмминга:", distance)

    
    messages = {n > 0: "Положительное", n < 0: "Отрицательное"}
    print(messages.get(True, "Ноль"))

    distance = sum(c1 != c2 for c1, c2 in zip(s, t))

