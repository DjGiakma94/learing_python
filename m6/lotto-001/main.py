# This entrypoint file to be used in development. Start by reading README.md
import lotto
import printer
from unittest import main

lotto.Bill.valid_numbers([1, 4, 6, 8, 33, 45, 68, 70, 78, 90])
lotto.Bill.route_type("Tutte")






# Run unit tests automatically
main(module='test', exit=False)