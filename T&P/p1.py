import pandas as pd


# print(pd.__version__)
# Create YearWise Sheet
def main1():
    dataset = pd.read_csv("Student.csv")
    # print dataset
    data = dataset.get_values()
    table = [a[3] for a in data]
    table1, table2, table3, table4 = [], [], [], []
    for a in data:
        if a[3] == '1st':
            table1.append(a)
        elif a[3] == '2nd':
            table2.append(a)
        elif a[3] == '3rd':
            table3.append(a)
        elif a[3] == '4th':
            table4.append(a)
    print table1
    # print table2
    df = pd.DataFrame(table1)
    export_csv = df.to_csv(r'firstyear.csv', index=None, header=False)
    df = pd.DataFrame(table2)
    export_csv = df.to_csv(r'secondyear.csv', index=None, header=False)
    df = pd.DataFrame(table3)
    export_csv = df.to_csv(r'thirdyear.csv', index=None, header=False)
    df = pd.DataFrame(table4)
    export_csv = df.to_csv(r'fourthyear.csv', index=None, header=False)
    print df


import re as RE
import os


def main():
    fin_name = raw_input("Enter File SRC :")
    try:
        dataset = pd.read_csv(fin_name)
        read_AOI = str(raw_input("Enter Area of Interest :"))
        # print(dataset[7])
        print dataset.head(10)
        data = dataset.get_values()
        table = [a[7] for a in data]
        print table
        # x.split('; |, |\\*|\\n')
        AOI = [RE.split(';|,|\*|\n|, | ,|\r', x) for x in table]
        AOI_Array = []
        print AOI[0][0]
        for i in range(len(AOI)):
            for j in range(len(AOI[i])):
                if AOI[i][j].lower().find(read_AOI.lower()) != -1:
                    # print(j, type(j)),
                    AOI_Array.append(data[i])
                    print(data[i], i, AOI[i])
                # if AOI_Array.index(j) == -1:
                # AOI_Array.append(j)
            # print ''
        print AOI_Array
        df = pd.DataFrame(AOI_Array)
        export_csv = df.to_csv(r'' + os.path.splitext(fin_name)[0] + read_AOI + '.csv', index=None, header=False)
        print df
    except:
        print "File Not Exist"

    # choice = raw_input("Enter Priority Choice")


# if j not 'python'
if __name__ == '__main__':
    # main1()
    main()
