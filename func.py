from datetime import datetime
# from pandas import ExcelWriter

def DTFormatOpt(s,flist):
    for f in flist:
        try:
            return datetime.strptime(s,f)
        except ValueError:
            pass

    
    
