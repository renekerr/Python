# Porcentaje panadero
harina_porcentaje = 100
agua_porcentaje = 70
mmadre_porcentaje = 20
sal_porcentaje = 2

h = int(input('Harina (g): '))
a = (h * agua_porcentaje)/100
mm = (h * mmadre_porcentaje)/100
s = (h * sal_porcentaje)/100

print('Ingredientes')
print(f'\t Harina {h:.0f} g')
print(f'\t Agua {a:.0f} g')
print(f'\t Masa madre {mm:.0f} g')
print(f'\t Sal {s:.0f} g')




