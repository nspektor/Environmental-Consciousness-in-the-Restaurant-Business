# Convert Yelp Data JSON files to CSV files
#
# Run instructions:
#
# $ python3 json_to_csv.py big_yelp_data/business.json
# AND
# $ python3 json_to_csv.py big_yelp_data/review.json
#
#
# note: this is assuming you have business.json in a folder titled big_yelp_data in your current directory
# this is how I have it and it is not pushed to github thanks to .gitignore, so if you have it in a different directory,
# edit .gitignore accordingly
#
#
# Convert Yelp Academic Dataset from JSON to CSV
# https://github.com/tothebeat/Yelp-Challenge-Dataset/blob/master/convert.py
# By Paul Butler, No Rights Reserved

import json
import sys

import pandas as pd
from glob import glob

filename = sys.argv[1]


def convert(x):
    ''' Convert a json string to a flat python dictionary
    which can be passed into Pandas. '''
    ob = json.loads(x)
    new_ob = dict(ob)
    for k, v in ob.items():
        if isinstance(v, list):
            new_ob[k] = ','.join(v)
        elif isinstance(v, dict):
            for kk, vv in v.items():
                new_ob['%s_%s' % (k, kk)] = vv
            del new_ob[k]
    return new_ob


for json_filename in glob(filename):
    csv_filename = '%s.csv' % json_filename[:-len('.json')]
    print('Converting %s to %s' % (json_filename, csv_filename))
    f = open(json_filename, "r")
    df = pd.DataFrame([convert(line) for line in f])
    df.to_csv(csv_filename, encoding='utf-8', index=False)
    print("done")

