"""software should ask how many bills the user want to generate (min: 1, max: 5, 0: exit)

for each bill the software should ask the type of bill (ambata, ambo, terno, quaterna, cinquina) 
and the amount of numbers to generate (max 10 per bill)

for each bill the software should ask the "city" (aka "ruota") of the bill: 
Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia and Tutte 
(for the project purpose completely ignore "ruota nazionale" and the "estratto determinato" play type).

numbers will be randomly generated in the range 1-90 (inclusive)"""
from random import sample

class Bill:
    def __init__(self, number_of_bill, numb, route, combination):
        self.number_of_bill=number_of_bill
        self.numb=numb
        self.route=route
        self.combination=combination
        
        
    def set_number_of_bill(number_of_bill):
        if 0 < number_of_bill < 6:
            return number_of_bill
        else:
            return ("error! numbers of bills are out of range")
 
    def valid_numbers(numb: list):
        numbers=[]
        ticket_numbers=[]
        for x in range (1, 91):
            numbers.append(x)
        for x in numb:
            if x in numbers and len(numb)<=10:
                ticket_numbers.append(x)
            else:
                return("error, numbers not valid!")
        return (ticket_numbers)
        
        
    def route_type(route):
        possible_route= ["Bari", "Cagliari", "Firenze", "Genova", "Milano", "Napoli", "Palermo", "Roma", "Torino", "Venezia", "Tutte"]
        if route in possible_route:
            extraction = {}
            if route != "Tutte":
                extraction_single=[]
                extraction[route] = sample(range(1,91), k=10)
                extraction_single.append(extraction)
                return extraction_single
            elif route == "Tutte":
                counter = 0
                extraction_tutte=[]
                for x in range(1, 11):
                    extraction = {}
                    extraction[possible_route[counter]] = sample(range(1,91), k=10)
                    counter+=1
                    if len(extraction_tutte)<10:
                        extraction_tutte.append(extraction)
            return extraction_tutte

        else:
            return("error, route isn't correct")
        
    def new_combination(combination):
        bet_combination = ['ambata', 'ambo', 'terno', 'quaterna', 'cinquina']
        if combination in bet_combination:
            return combination
        else:
            print(f'{combination} is not valid.')
            raise ValueError
        
           
        
class Ticket:
    
        
    def __init__(self, new_combinaiton, valid_numbers, route_type, set_number_of_bill):
        self.new_combination = new_combinaiton
        self.valid_numbers = valid_numbers
        self.route_type = route_type
        self.set_number_of_bill = set_number_of_bill
        
    def check_winning(new_combinaiton, valid_numbers, route_type, number_of_bills):
        
        #verify if number of bills are correct
        
        print(Bill.set_number_of_bill(number_of_bills))
        
        if new_combinaiton == "ambata":
            counter_2=0
            for x in Bill.route_type(route_type):
                #with a loop search numbers in all routes
                if len(Bill.route_type(route_type)) > counter_2:
                    counter=0
                    for x in valid_numbers:
                        #find your numbers in route's value
                        D1 = Bill.route_type(route_type)[counter_2]
                        for y in D1.values():
                            if x in y:
                                    counter+=1
                    if counter == 1:
                        return ("you win")
                counter_2+=1
            return ("you lose")
                    
        elif new_combinaiton == "ambo":
            counter_2=0
            for x in Bill.route_type(route_type):
                #with a loop search numbers in all routes
                if len(Bill.route_type(route_type)) > counter_2:
                    counter=0
                    for x in valid_numbers:
                        #find your numbers in route's value
                        D1 = Bill.route_type(route_type)[counter_2]
                        for y in D1.values():
                            if x in y:
                                    counter+=1
                    if counter == 2:
                        return ("you win")
                counter_2+=1
            return ("you lose")
            
        elif new_combinaiton == "terno":
            counter_2=0
            for x in Bill.route_type(route_type):
                #with a loop search numbers in all routes
                if len(Bill.route_type(route_type)) > counter_2:
                    counter=0
                    for x in valid_numbers:
                        #find your numbers in route's value
                        D1 = Bill.route_type(route_type)[counter_2]
                        for y in D1.values():
                            if x in y:
                                counter+=1
                    if counter == 3:
                        return ("you win")
                counter_2+=1
            return ("you lose")
            
        elif new_combinaiton == "quaterna":
            counter_2=0
            for x in Bill.route_type(route_type):
                #with a loop search numbers in all routes
                if len(Bill.route_type(route_type)) > counter_2:
                    counter=0
                    for x in valid_numbers:
                        #find your numbers in route's value
                        D1 = Bill.route_type(route_type)[counter_2]
                        for y in D1.values():
                            if x in y:
                                    counter+=1
                    if counter == 4:
                        return ("you win")
                counter_2+=1
            return ("you lose")
            
        elif new_combinaiton == "cinquina":
            counter_2=0
            for x in Bill.route_type(route_type):
                #with a loop search numbers in all routes
                if len(Bill.route_type(route_type)) > counter_2:
                    counter=0
                    for x in valid_numbers:
                        #find your numbers in route's value
                        D1 = Bill.route_type(route_type)[counter_2]
                        for y in D1.values():
                            if x in y:
                                    counter+=1
                    if counter == 5:
                        return ("you win")
                counter_2+=1
            return ("you lose")


            
        

    