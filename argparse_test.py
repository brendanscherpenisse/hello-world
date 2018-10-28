import argparse
# https://docs.python.org/3/library/argparse.html
parser = argparse.ArgumentParser(description='Test function')
parser.add_argument("filename", help="Specify .kml or .shp file name",
                    type=str)
parser.add_argument("-r", "--resample", help="Resample DEM? False by default.",action='store_true')
parser.add_argument("-d", "--dem", help="Which DEM?",type=str,choices=('SRTM1','SRTM3','SRTM30'),default='SRTM1')

args = parser.parse_args()
print(args)
print(args.filename)
if args.resample:
    print(args.resample)
else:
    print(args.resample)
print(args.dem)


# def str2bool(v):
#     if v.lower() in ('yes', 'true', 't', 'y', '1'):
#         return True
#     elif v.lower() in ('no', 'false', 'f', 'n', '0'):
#         return False
#     else:
#         raise argparse.ArgumentTypeError('Boolean value expected.')
