#!/usr/bin/env python3
import csv

# y is the BOM showing up in the key please no
_ID = '\ufeffRecord#'
_MAJOR_PROGRAM_NAME = 'Major Program Name'
_YEAR = 'School Year'
_TOT_M = 'Totals, Male: Total Declared Majors (Tot. M)'
_TOT_F = 'Totals, Female: Total Declared Majors (Tot. F)'
_F_GPA = 'Totals, Female: Cumulative GPA (Tot. F)'
_M_GPA = 'Totals, Male: Cumulative GPA (Tot. M)'

_OUTPUT_FIELDNAMES = ['ID', 'Major', 'Year', 'M_GPA', 'F_GPA', 'COMBINED_GPA', 'M_EN', 'F_EN', 'C_EN']


def row_into(row):
    try:
        id = int(row[_ID])
        mpn = row[_MAJOR_PROGRAM_NAME]
        year = int(row[_YEAR][:4])
        fgpa = float(row[_F_GPA])
        mgpa = float(row[_M_GPA])
        menrolled = int(row[_TOT_M])
        fenrolled = int(row[_TOT_F])
        return {
            'ID': id,
            'Major': mpn,
            'Year': year,
            'M_GPA': mgpa,
            'F_GPA': fgpa,
            'COMBINED_GPA': ((mgpa * menrolled) + (fgpa * fenrolled)) / (menrolled + fenrolled),
            'M_EN' : menrolled,
            'F_EN' : fenrolled,
            'C_EN' : menrolled + fenrolled
        }
    except KeyError:
        print("Discarded row because a key did not exist")
    except ValueError:
        print("Discarded row because of value conversion error: ")

    return None


if __name__ == '__main__':
    with open('NCWIT_DataV2_NormalizedMajors.csv', 'rU') as csvinfile:
        reader = csv.DictReader(csvinfile)
        with open('NCWIT_DataV2_GPAData.csv', 'w') as csvoutfile:
            writer = csv.DictWriter(csvoutfile, fieldnames=_OUTPUT_FIELDNAMES)
            writer.writeheader()
            writer.writerows(list(filter(
                lambda row: row is not None,
                map(row_into, list(reader))
            )))
    print("All done.")
