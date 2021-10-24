# XDF2XLS

Simple script to convert [XDF](https://github.com/sccn/xdf) files to Microsoft Excel's [XLS](https://en.wikipedia.org/wiki/Microsoft_Excel#File_formats).

You probably don't want to use this script, because
* Why on earth would you want raw experiment data in Excel?
* I didn't test it
* I hardcoded stuff
* Really, are you sure you don't want to use [pyxdf](https://github.com/xdf-modules/pyxdf) instead?

If after that you still want to use this script, I'd advise you to reconsider you life choices that led you to this point.

## How to run

```
xdf2xls.py data.xdf
```

If you're on Windows, you can also just drag and drop your `xdf` file on the Python script.

It'll generate an `xls` file somewhere on your computer. Most likely near where the `xdf` file was, but maybe not?

My best advice is to not run the script at all.
