#!/usr/bin/env python3
import csv

F_ENROLLED = "Totals, Female: Total Declared Majors (Tot. F)"
M_ENROLLED = "Totals, Male: Total Declared Majors (Tot. M)"
F_LEFT_INST = "Totals, Female: Left Institution (not graduated) (Tot. F)"
M_LEFT_INST = "Totals, Male: Left Institution (not graduated) (Tot. M)"
I_TYPE = "NCWIT Participant"
D_TYPE = "What degrees does your institution offer?"


def is_bad(row):
    m, f, t = row['m_attrition'], row['f_attrition'], row['t_attrition']
    return m < 0 or m > 1 or f < 0 or f > 1 or t < 0 or t > 1


if __name__ == '__main__':
    vals = {}
    attritions = []
    with open('NCWIT_DataV2_NormalizedMajors.csv', 'rU') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            try:
                year = int(line['School Year'][0:4])
                major = line['Major Program Name']
                if major == '' or major is None: raise ValueError
                institution = line['Institution']
                vals[(year, major, institution)] = {
                    I_TYPE : line[I_TYPE] if line[I_TYPE] != "Academic Alliance, Academic Alliance" else "Academic Alliance",
                    D_TYPE : line[D_TYPE],
                    F_ENROLLED : int(line[F_ENROLLED]),
                    M_ENROLLED : int(line[M_ENROLLED]),
                    F_LEFT_INST : int(line[F_LEFT_INST]),
                    M_LEFT_INST : int(line[M_LEFT_INST])
                }
            except ValueError:
                pass
    for k in vals.keys():
        mk = (k[0]-1, k[1], k[2])
        if vals.__contains__(mk):
            try:
                f_left, m_left = vals[k][F_LEFT_INST], vals[k][M_LEFT_INST]
                f_en, m_en = vals[mk][F_ENROLLED],vals[mk][M_ENROLLED]
                m_attrition = m_left/m_en
                f_attrition = f_left/f_en
                t_attrition = (m_left + f_left)/(m_en + f_en)
                attritions.append({
                    'year' : k[0],
                    'major' : k[1],
                    'institution' : k[2],
                    'm_attrition' : m_attrition,
                    'f_attrition' : f_attrition,
                    't_attrition' : t_attrition,
                    'participant' : vals[k][I_TYPE],
                    'degrees' : vals[k][D_TYPE],
                    'f_en' : f_en,
                    'm_en' : m_en,
                    'c_en' : m_en + f_en,
                })
            except ZeroDivisionError:
                pass
        else:
            pass
    
    fieldnames = ['year', 'major', 'institution', 'm_attrition', 'f_attrition', 't_attrition', 'participant', 'degrees', 'f_en', 'm_en', 'c_en']

    clean = list(filter(lambda row: not is_bad(row), attritions))
    with open('NCWIT_cleaned_attrition.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(clean)
    print("All done.")
