import argparse as arg

ap = arg.ArgumentParser()
ap.add_argument("-n", "--name", required = True, help="name of the user")

args = vars(ap.parse_args())

print("hello {}".format(args["name"]))
print(args)