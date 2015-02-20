__author__ = 'regrant'

import csv
from Tkinter import Tk
from tkFileDialog import askopenfilename, asksaveasfilename


def remove_dup_and_blank(reader):
    """
    Cleans data given by genescan 384 well to format useful to GDL.
    :param writer: a csv module write object
    :return: a set [(patient1, gene1, RQ, RQ_Min, RQ_Max),
                    (patient1, gene2, RQ, RQ_Min, RQ_Max),
                    (patient2, gene1, RQ, RQ_Min, RQ_Max)]

    """
    data_set = set([])
    for sample, gene, rq, rmin, rmax in reader:
        if reader.line_num > 38:
            if rq:
                data_set.add((sample, gene, rq, rmin, rmax))
    return data_set


def write_data(data_set):
    """
    Takes data set from remove dup and blank and writes to a new csv file.
    Also flags any samples where the rmax/rmin are +- 0.2 away from RQ.
    :param data_set:
    :return: nothing
    """
    filename = asksaveasfilename(defaultextension='csv')
    t_output_csv = open(filename, 'wb')
    writer = csv.writer(t_output_csv, dialect='excel-tab')
    outlier_set = set([])
    for row in data_set:
        writer.writerow(row)
        if row[2] == 'RQ':
            continue
        rq, rmin, rmax = float(row[2]), float(row[3]), float(row[4])
        if abs(rq - rmin) > 0.2 or abs(rq - rmax) > 0.2:
            outlier_set.add(row)

    writer.writerow([])
    writer.writerow(['Outlier Samples: |RQ - Rmin| > 0.2 or |RQ - Rmax| > 0.2'])
    for outlier in outlier_set:
        writer.writerow(outlier)

    t_output_csv.close()


def clean_data():
    """
    Runs remove dup and blank as well as writes data
    """
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    tab_csv = open(filename)
    t_reader = csv.reader(tab_csv, dialect='excel-tab')
    x = remove_dup_and_blank(t_reader)
    write_data(x)


    tab_csv.close()
    return

clean_data()