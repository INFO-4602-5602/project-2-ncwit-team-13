#!/usr/bin/env python3
import csv

_MAJOR = 'Major Program Name'
_CIP_CODE = 'CIP# Only'


def tag(cip, mpn, d):
    try:
        d[cip][mpn] += 1
    except:
        try:
            d[cip][mpn] = 1
        except:
            d[cip] = { mpn : 1 }


def make_into_fn(majors):
    def fn(row):
        newr = row.copy()
        try:
            newr[_MAJOR] = majors[newr[_CIP_CODE]]
        except:
            newr[_MAJOR] = "Unknown"
        return newr
    return fn


if __name__ == '__main__':
    majors = {}
    with open('NCWIT_DataV2_RawData.csv', 'rU') as csvfile:
        csvreader = csv.DictReader(csvfile)
        fieldnames = csvreader.fieldnames
        rdr = list(csvreader)
    for line in rdr:
        mpn = line[_MAJOR]
        cip = line[_CIP_CODE]
        if cip != '' and mpn != '':
            tag(cip, mpn, majors)
    print(majors)
    actualmajors = {}
    for key in majors.keys():
        majorkeys = list(majors[key].keys())
        maxkey = majorkeys[0]
        maxcnt = majors[key][maxkey]
        for majorkey in majorkeys:
            if majors[key][majorkey] > maxcnt:
                maxcnt = majors[key][majorkey]
                maxkey = majorkey
        actualmajors[key] = maxkey
    print(actualmajors)
    with open('NCWIT_DataV2_NormalizedMajors.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(map(make_into_fn(actualmajors), rdr))
    print("All done!")