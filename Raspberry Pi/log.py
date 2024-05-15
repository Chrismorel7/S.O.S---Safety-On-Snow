import datetime as dt

def log(filepath: str, message: str):
    dtime = dt.datetime.now()
    date = str(dtime.date())
    time = str(dtime.time())

    file = open(filepath, 'a')
    infos = date + "," + time + "\tDEBUG: " + message + "\n"
    print(infos)
    file.write(infos)
    file.close()