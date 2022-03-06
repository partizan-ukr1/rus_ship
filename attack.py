import os
from argparse import ArgumentParser
import time

parser = ArgumentParser()
parser.add_argument("-t", "--targets", dest="targets")
parser.add_argument("-c", "--connection", dest="connection", type=int, default=500)

args, unknown = parser.parse_known_args()
targets = args.targets
connection = args.connection
duration = 60*60*24

startTime = time.time()
while time.time() < startTime + duration :
    targetList = targets.split(",")
    for target in targetList :
        os.system("docker run -ti --rm alpine/bombardier -c %d -d 59s -l %s" % (connection, target))
