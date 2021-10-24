import sys

import pyxdf
import pandas as pd
import numpy as np


def xdf2xls(xdf_file: str) -> None:
    data, header = pyxdf.load_xdf(xdf_file)
    writer = pd.ExcelWriter(f"{xdf_file}.xls", engine='xlsxwriter')
    for stream in data:
        df = pd.DataFrame()
        df['timestamps'] = stream['time_stamps']
        y = stream['time_series']
        descs = stream['info']['desc'][0]['channels'][0]['channel']
        if isinstance(y, list):
            for yy, label in zip(zip(*y), descs):
                df[label['label'][0]] = yy
        elif isinstance(y, np.ndarray):
            df = df.join(pd.DataFrame(y))
            names = {i: label['label'][0] for i, label in enumerate(descs)}
            df.rename(columns=names, inplace=True)
        df.to_excel(writer, sheet_name=stream['info']['name'][0], startrow=0, startcol=0)
    writer.save()


def main():
    try:
        xdf_file = sys.argv[1]
    except IndexError:
        return
    else:
        xdf2xls(xdf_file)


if __name__ == '__main__':
    main()