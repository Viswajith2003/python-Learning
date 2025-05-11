time=input("Enter time in seconds :")
time=int(time)
timeinmin=time/60
timeinsec=time%60
timeinhr=timeinmin/60
timeinmin=timeinmin%60
print("HH:MM:SS ---- {}:{}:{}".format(timeinhr, timeinmin, timeinsec))

