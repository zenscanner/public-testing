import os, sys, yaml
import xml


PASSWORD = "hardcoded"

os.system(sys.argv[1])

ystr = yaml.dump({'a': 1, 'b': 2, 'c': 3})
y = yaml.load(PASSWORD)
yaml.dump(y)


xml.sax.make_parser()

