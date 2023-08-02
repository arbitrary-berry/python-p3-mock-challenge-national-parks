from classes.trip import Trip


class NationalPark:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and not hasattr(self, "name"):
            self._name = name
        else:
            raise Exception
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
        pass

    def visitors(self):
        from classes.visitor import Visitor
        return [*set([trip.visitor for trip in Visitor.all if trip.national_park == self])]

    def total_visits(self):
        pass

    def best_visitor(self):
        pass

    @classmethod
    def most_visited(cls):
        pass
