A, B, C = sorted(map(float, input().split()), reverse=True)

As = A * A
Bs = B * B
Cs = C * C

i = 1

while i != 0:
    if A >= B + C:
        print("NAO FORMA TRIANGULO")
        break
    if As == Bs + Cs:
        print("TRIANGULO RETANGULO")
    if As > Bs + Cs:
        print("TRIANGULO OBTUSANGULO")
    if As < Bs + Cs:
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
        break
    if A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")
    i = 0
