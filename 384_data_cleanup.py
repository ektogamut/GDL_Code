__author__ = 'regrant'

import csv


def remove_dup_and_blank(reader):
    """
    Cleans data given by genescan 384 well to format useful to GDL.
    :param writer: a csv module write object
    :return: a dictionary {patient1: {gene1: [RQ, RQ_Min, RQ_Max], gene2: [RQ, RQ_Min, RQ_Max]},
                           patient2: {gene1: [RQ, RQ_Min, RQ_Max], gene2: [RQ, RQ_Min, RQ_Max]}}
    """
    data_dict = {}
    for sample, gene, rq, rmin, rmax in reader:
        if reader.line_num > 38:
            # print reader.line_num
            if sample not in data_dict and rq:
                data_dict[sample] = {gene: [rq, rmin, rmax]}
            elif sample in data_dict and gene not in data_dict[sample] and rq:
                data_dict[sample][gene] = [rq, rmin, rmax]
    # for item, value in data_dict.items(): print item, value
    return data_dict

def write_data_dict(data_dict):
    """

    :param data_dict:
    :return:
    """
    t_output_csv = open("test_output.csv", 'wb')
    writer = csv.writer(t_output_csv, dialect='excel-tab')
    for sample in data_dict:
        for gene in data_dict[sample]:
            print sample, gene, data_dict[sample][gene]
            writer.writerow([sample, gene, data_dict[sample][gene][0], data_dict[sample][gene][1], data_dict[sample][gene][2]])

    t_output_csv.close()

tab_csv = open("/Users/regrant/GDL Code/Source Files/HI DD/ALL 384 well data HHT-2994 c.csv", 'rb')
t_reader = csv.reader(tab_csv, dialect='excel-tab')

# t_output_csv = open("test_output.csv", 'wb')
# writer = csv.writer(t_output_csv, dialect='excel-tab')
x = remove_dup_and_blank(t_reader)
write_data_dict(x)



tab_csv.close()
