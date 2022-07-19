import lotto

"""
example:
+-------------------------------+----------+
|             LOTTO             | Ticket 5 |
+-------------------------------+----------+
| Cinquina on Milano                       |
| 22 55 66 45 34 23 67 34 56 45            |
| (Giocata: 12,50)                         |
+-------------------------------+----------+"""

def printer(numbers_of_bill, combination, route):
    card=""
    card+=("+-------------------------------+-------------------+\n")
    card+=(f"|             LOTTO             | Ticket {lotto.Bill.set_number_of_bill(numbers_of_bill)}          |\n")
    card+=("+-------------------------------+-------------------+\n")
    card+=( f"|{lotto.Bill.new_combination(combination)} on                                            |\n")
    card+=(f"|{lotto.Bill.route_type(route)}|\n")
    card+=("+-------------------------------+-------------------+\n")
    
    return card

print(printer(4, "ambo", "Bari"))
    
    