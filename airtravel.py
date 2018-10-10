# -*- coding: utf-8 -*-
"""Demonstration of class
Created on Thu Aug  9 16:13:17 2018

@author: 130873
"""

class Flight:
    
    
    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
        if not number[:2].isupper():
            raise ValueError("Invalid airline code in '{}'".format(number))
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))  
        self._number = number    
        self._aircraft = aircraft
        
        rows,seats = self._aircraft.seating_plan()
        self._seating = [None]+[{str(row)+letter:None for letter in seats} \
                        for row in rows]
            
        
    def flight_number(self):
        return self._number
        
        
    def airline(self):
        return self._number[:2]
    
    
    def aircraft_model(self):
        return self._aircraft.model()
    
    
    def _validate_seat(self,seat):
        """ Validate if provided seat to a passanger is a vlid one or not
        
        Args:
            seat: a seat designator such as "12A"
            passenger: passenger name 
            
        Raises:     
            ValueError: if seat is unavailable
        """
        rows,seats = self._aircraft.seating_plan()
        
        if seat[-1] not in seats:
            raise ValueError("Invalid seat number {}".format(seat))
            
        try:
            row = int(seat[:-1])
        except ValueError:
            raise ValueError("Invalid row number {}".format(seat))
            
        if row not in rows:
            raise ValueError("roq doesnt exist {}".format(row))
            
        return row,seat
    
    
    def allocate_seat(self,seat,passenger):
        """ Allocate a seat to a passanger from seating plan
        
        Args:
            seat: a seat designator such as "12A"
            passenger: passenger name 
            
        Raises:     
            ValueError: if seat is unavailable
        """

        row, seat = self._validate_seat(seat) 
        
        if self._seating[row][seat] is not None:
            raise ValueError("Seat {} occupied. can not be assigned".\
                             format(seat))
            
        self._seating[row][seat] = passenger 
        
     
    def reallocate_seat(self,from_seat,to_seat):
        """Re-allocating a passenger to new seat
        
        Args:
            from_seat: Already assigned seat number
            to_seat: The new seat number of the passenger
        """
        from_row, from_seat = self._validate_seat(from_seat)
        if self._seating[from_row][from_seat] is None:
            raise ValueError("No passenger to relocate from seat {}".\
                             format(from_seat))
        
        to_row, to_seat = self._validate_seat(to_seat)
        if self._seating[to_row][to_seat] is not None:
            raise ValueError("Seat {} already occupied".format(to_row))
        
        self._seating[to_row][to_seat] = self._seating[from_row][from_seat]
        self._seating[from_row][from_seat] = None
        
        
    def available_seat(self):
        """ This function returns number of unoccupied seats"""
        return sum(sum(1 for name in row.values() if name is None)
            for row in self._seating if row is not None)
        
        
    def print_boarding_pass(self,pass_printer):
        """ This function initiate printing of boarding passes"""
        for passenger, seat in sorted(self._passenger_seats()):
            pass_printer(passenger,seat,self.flight_number(),\
                         self.aircraft_model())
            
            
    def _passenger_seats(self):
        """ An iterable series of allocated seat and passenger name """
        for row in self._seating:
            if row is not None:
                for seat,name in row.items():
                    if name is not None:
                        yield (name,seat)       
           
    
#class Aircraft:
#    
#
#    def __init__(self,registration,model,row_num,seat_per_row):
#        self._registration =registration
#        self._model = model
#        self._row_num = row_num
#        self._seat_per_row = seat_per_row
#        
#        
#    def registration(self):
#        return self._registration
#    
#    
#    def model(self):
#        return self._model
#    
#    
#    def seating_plan(self):
#        return(range(1,self._row_num+1),"ABCDEFGHJK"[:self._seat_per_row])
#        
                        
class Aircraft:
    
    def __init__(self,registration): 
        self._registration = registration
        
        
    def registration(self):
        return self._registration
    
    
    def num_seats(self):
        rows, seats = self.seating_plan()
        return len(rows)*len(seats)
    

class Airbus319(Aircraft):

    
    def model(self):
        return "Airbus 319"
    
    
    def seating_plan(self):
        return range(1,23),"ABCDEF"
    

class Boeing777(Aircraft):
    
    
    def model(self):
        return "Boeing 777"
    
    
    def seating_plan(self):
        return range(1,56),"ABCDEFGHJK"
            
        
def console_boarding_pass_printer(passenger,seat,flight_number,aircraft):
    output = "| Name: {0}"      \
             "  Flight: {1}"    \
             "  Seat: {2}"      \
             "  Aircraft: {3}"  \
             " |".format(passenger,flight_number,seat,aircraft)
    banner = "+" + "-" * (len(output)-2)+ "+"
    border = "|" + " " * (len(output)-2)+ "|"
    lines  = [banner, border, output, border, banner]
    card   = '\n'.join(lines)
    print(card)
    print()    
        

#def make_flight():
#    f = Flight("SN060",Aircraft("GU-EUPT","Airbus A319",22,6))
#    f.allocate_seat("12A","Indranil Mondal")
#    f.allocate_seat("12B","Esha Ghosh")
#    f.allocate_seat("12C","Nilesh Mondal")
#    f.allocate_seat("12D","Paresh Mondal")
#    f.allocate_seat("12E","Malati Mondal")
#    f.allocate_seat("21F","Nilmoni Mondal")
#    return f
    
def make_flights():
    f = Flight("BA758",Airbus319("GU-EUPT"))
    f.allocate_seat("12A","Indranil Mondal")
    f.allocate_seat("12B","Esha Ghosh")
    f.allocate_seat("12C","Nilesh Mondal")
    f.allocate_seat("12D","Paresh Mondal")
    f.allocate_seat("12E","Malati Mondal")
    f.allocate_seat("21F","Nilmoni Mondal")
    
    g = Flight("AF72",Boeing777("F-GSPS"))
    g.allocate_seat("32A","Indranil Mondal")
    g.allocate_seat("32B","Esha Ghosh")
    g.allocate_seat("32C","Nilesh Mondal")
    g.allocate_seat("32D","Paresh Mondal")
    g.allocate_seat("32E","Malati Mondal")
    g.allocate_seat("32F","Nilmoni Mondal")
    
    return f, g
    

    
    
