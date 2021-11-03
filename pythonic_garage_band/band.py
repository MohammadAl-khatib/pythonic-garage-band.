from abc import ABC, abstractmethod 

class Band:
    instances = []
    def __init__(self,name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos
    
    @classmethod
    def to_list(cls):
        return Band.instances

class Musician :
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def play_solo(self):
        return "instrument sound"

class Guitarist (Musician):
    def __str__(self) :
        return f"My name is {self.name} and I play guitar"

    def __repr__(self) :
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"

class Drummer(Musician):
    def __str__(self) :
        return f"My name is {self.name} and I play drums"

    def __repr__(self) :
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"


class Bassist(Musician):
    def __str__(self) :
        return f"My name is {self.name} and I play bass"

    def __repr__(self) :
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"
        
    def play_solo(self):
        return "bom bom buh bom"

