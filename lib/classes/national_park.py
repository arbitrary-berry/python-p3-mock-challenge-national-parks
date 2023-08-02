# from classes.trip import Trip

# class NationalPark:

#     def __init__(self, name):
#         self.name = name

#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, name):
#         if type(name) == str and not hasattr(self, "name"):
#             self._name = name
#         else: 
#             raise Exception

#     def trips(self):
#         return [trip for trip in Trip.all if trip.national_park == self]
    
#     def visitors(self):
#         return [*set([trip.visitor for trip in self.trips()])]
    
#     def total_visits(self):
#         return len(self.trips())
    

#     #######################bonus below
#     def best_visitor(self):
#                 return max(
#             self.visitors(), 
#             key=lambda v :len([trip for trip in self.trip() if trip.visitor == v]))
#         # max_visitor = None
#         # max_visits = 0
#         # for visitor in self.visitor():
#         #     v_visits = len([trip for trip in self.trips() if trip.visitor == visitor])
#         #     if v_visits > max_visits:
#         #         max_visits = v_visits
#         #         max_visitor = visitor
#         # return max_visitor

#     @classmethod
#     def most_visited(cls):
#         return max(cls.all, key=lambda park: park.total_visits())



from classes.trip import Trip

class NationalPark:

    all = []

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

    def visitors(self):
        return list(set([trip.visitor for trip in self.trips()]))
        # return [*set([trip.visitor for trip[ in self.trips()])]
    
    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        return max(set([trips.visitor for trips in self.trips()]), key=[trips.visitor for trips in self.trips()].count)
        #OR
        # if not self.trips():
        #     return None
        # visitors = self.visitors()
        # max_visits = 0
        # best_visitor = None

        # for visitor in visitors:
        #     num_visits = len(visitor.trips())
        #     if num_visits > max_visits:
        #         max_visits = num_visits
        #         best_visitor = visitor
        # return best_visitor

    @classmethod
    def most_visited(cls):
        return max(set([trips.national_park for trips in Trip.all]), key=[trips.national_park for trips in Trip.all].count)


