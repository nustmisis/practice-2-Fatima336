#<b>Задание 2</b>

#Использую только переменную S. нерезание (S[1:2]) и конкатенацию (string + string)
#выведите переменную  S = slam

S = "spaml"
S = 'spaml'
S = S.replace(S[1:2], '')
S = S[0] + S[3] + S[1] + S[2]
print(S)