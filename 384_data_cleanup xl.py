"""
This is a small script designed to cleanup data fro 284 well genescan assays,
which gives repetitive data. Additionally, this script will flag
outliers.
"""

import csv
from Tkinter import Tk
from tkFileDialog import askopenfilename, asksaveasfilename
import xlrd, xlwt
from numpy import mean, std




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


def average_cts(sample_dict):
    """

    :param sample_dict:
    :return:
    """
    ct_dict = dict(sample_dict)

    for sample, targets in ct_dict.items():
        for target, cts in targets.items():
            # print cts
            ct_dict[sample][target] = {}
            ct_dict[sample][target]["ave_ct"] = mean(cts)
            ct_dict[sample][target]["std"] = std(cts)

    for item, value in ct_dict.items(): print item, value
    return ct_dict





def get_data():
    """
    Takes a file path to an .xls file and returns a dictionary containing sample names and the replicate
    Ct values for the each target assay.  For example, the BWR methylated assay contains
    ICR1_CBS2 and ICR2 M and UM, where Methylated = M and  Unmethylated = UM
    :return: {"sample_name":{"ICR1_CBS2 M":[###, ###, ...], "ICR1_CBS2 UM":[###, ###, ...],...}
    """
    # Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    # filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    filename = '/Users/regrant/GDL Code/BWR_METHYL_292_06_12_15_RG.xls'
    workbook = xlrd.open_workbook(filename)
    results = workbook.sheet_by_name("Results")
    sample_dict = dict()
    count = 0
    for rowx in range(results.nrows):
        # print results.row(rowx)
        if type(results.row_values(rowx)[2]) == float:
            count += 1
            sample, target, ct = results.row_values(rowx)

            if sample not in sample_dict:
                sample_dict[sample] = {}
            if target not in sample_dict[sample]:
                sample_dict[sample][target] = [ct]
            else:
                sample_dict[sample][target].append(ct)
                if len(sample_dict[sample][target]) > 3:
                    print 'SHIT'

    # for x, y in sample_dict.items(): print x, y
    return sample_dict

if __name__ == '__main__':
    average_cts(get_data())

# clean_data()