import argparse
# argument parsing: https://docs.python.org/3/library/argparse.html
# abstract methods: https://pymotw.com/3/abc/
# from abc import ABCMeta, abstractmethod
# class Vehicle(object):
#     """A vehicle for sale by Jeffco Car Dealership.
#
#
#     Attributes:
#         wheels: An integer representing the number of wheels the vehicle has.
#         miles: The integral number of miles driven on the vehicle.
#         make: The make of the vehicle as a string.
#         model: The model of the vehicle as a string.
#         year: The integral year the vehicle was built.
#         sold_on: The date the vehicle was sold.
#     """
#
#     __metaclass__ = ABCMeta
#
#     base_sale_price = 0
#     wheels = 0
#
#     def __init__(self, miles, make, model, year, sold_on):
#         self.miles = miles
#         self.make = make
#         self.model = model
#         self.year = year
#         self.sold_on = sold_on
#         super().__init__()
#
#     def sale_price(self):
#         """Return the sale price for this vehicle as a float amount."""
#         if self.sold_on is not None:
#             return 0.0  # Already sold
#         return 5000.0 * self.wheels
#
#     def purchase_price(self):
#         """Return the price for which we would pay to purchase the vehicle."""
#         if self.sold_on is None:
#             return 0.0  # Not yet sold
#         return self.base_sale_price - (.10 * self.miles)
#
#     @abstractmethod
#     def vehicle_type(self):
#         """"Return a string representing the type of vehicle this is."""
#         print('not here?')
#         pass
#
# class Car(Vehicle):
#     """A car for sale by Jeffco Car Dealership."""
#
#     base_sale_price = 8000
#     wheels = 4
#
#     def vehicle_type(self):
#         """"Return a string representing the type of vehicle this is."""
#         return 'car'

# v = Car(0, 'Honda', 'Accord', 2014, None)

# for sc in Vehicle.__subclasses__():
#     print(sc.__name__)

class Parser(object):

    def __init__(self, filename, resample, dem):
        self.filename = filename
        self.resample = resample
        self.dem = dem

    def print_all(self):
        print(self.filename,self.resample,self.dem)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Test function')
    parser.add_argument("filename", help="Specify .kml or .shp file name",
                        type=str)
    parser.add_argument("-r", "--resample", help="Resample DEM? False by default.",action='store_true')
    parser.add_argument("-d", "--dem", help="Which DEM?",type=str,choices=('SRTM1','SRTM3','SRTM30'),default='SRTM1')

    args = parser.parse_args()

Parser(args.filename, args.resample, args.dem).print_all()




# def str2bool(v):
#     if v.lower() in ('yes', 'true', 't', 'y', '1'):
#         return True
#     elif v.lower() in ('no', 'false', 'f', 'n', '0'):
#         return False
#     else:
#         raise argparse.ArgumentTypeError('Boolean value expected.')
