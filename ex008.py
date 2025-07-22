#screva um programa que leia um valor em metros e o exiba convertido em km, hm, dam, dm, cm, mm.

msg = """Coloque o valor em metros e vou mostra em
km, hm, dam, dm, cm, mm."""

metro = float(input("Digite o valor em metros: "))

km = metro * 0.001
hm = metro * 0.01
dam = metro * 0.1
dm = metro * 10
cm = metro * 100
mm = metro * 1000

print(f"Km: {km:.3f}\nhm: {hm:.2f}\ndam: {dam:.1f}\ndm: {dm:.0f}\nmm: {mm:.0f}")

