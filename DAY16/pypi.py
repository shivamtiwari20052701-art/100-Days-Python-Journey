from prettytable import PrettyTable
table=PrettyTable()
table.field_names=["pokemon","type"]
table.add_row(["pikachu","electric"])
table.add_row(["squirtle","water"])
table.add_row(["charmander","fire"])
table.align="r"
print(table)