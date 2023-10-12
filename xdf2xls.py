import sys
import logging as log

import pyxdf
import pandas as pd
import numpy as np


def desc_to_label(desc):
    s = desc['label'][0]
    try:
        s += f" ({desc['unit'][0]})"
    except IndexError:
        pass
    return s


def xdf2xls(xdf_file: str) -> None:
    log.info(f"Opening {xdf_file}")
    data, header = pyxdf.load_xdf(xdf_file)
    if xdf_file.endswith(".xdf"):
        xls_file = xdf_file[:-4] + ".xls"
    else:
        xls_file = xdf_file + ".xls"
    log.info(f"Writting to {xls_file}")
    with pd.ExcelWriter(xls_file, engine='xlsxwriter') as writer:
        for stream in data:
            df = pd.DataFrame()
            df['timestamps'] = stream['time_stamps']
            y = stream['time_series']
            try:
                descs = stream['info']['desc'][0]['channels'][0]['channel']
            except IndexError:
                print(f"Failed to find channels for {stream['info']['name'][0]}")
                continue
            if isinstance(y, list):
                for yy, desc in zip(zip(*y), descs):
                    df[desc_to_label(desc)] = yy
            elif isinstance(y, np.ndarray):
                df = df.join(pd.DataFrame(y))
                names = {i: desc_to_label(desc) for i, desc in enumerate(descs)}
                df.rename(columns=names, inplace=True)
            sheet_name = stream['info']['name'][0][:31]
            log.info(f"Writting to sheet {sheet_name}")
            df.to_excel(writer, sheet_name=sheet_name, startrow=0, startcol=0)


def main():
    log.basicConfig(format="%(asctime)-15s [%(levelname)-8s]: %(message)s", level=log.INFO)
    try:
        xdf_file = sys.argv[1]
    except IndexError:
        return
    else:
        xdf2xls(xdf_file)


if __name__ == '__main__':
    main()
