from prettytable import PrettyTable

sample_table = PrettyTable()
sample_table.add_column("Pokemon name", ["Haxorus", "Scatterbug", "Frogadier"])
sample_table.add_column("Type", ["Dragon", "Bug", "Water"])

print(sample_table.align)
print(sample_table)
sample_table.align = 'l'
print(sample_table.align)
print(sample_table)