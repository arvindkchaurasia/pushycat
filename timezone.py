import datetime
import pytz
import time

t = time.time()
print("time is: ", t)

ct = time.ctime()
print("ctime is: ", ct)

local_time = time.localtime()
print("Local time is: ", local_time)

gm_time = time.gmtime()
print("GM time is:", gm_time)

mk_time = time.mktime(local_time)
print("Mk time is: ", mk_time)

asc_time = time.asctime()
print("ASC TIME: ", asc_time)

print()
print()
start = time.time()

print("Since beginning of time which is 1 Jan 1970:", time.time())
print("Unix corrected time:", time.asctime())
now = time.gmtime()
#time.sleep(3)
now1 = time.asctime()
print("time now is: ", now1)



stop = time.time()

time_taken = stop - start
print("time taken:", time_taken)

print("GMT time:", time.gmtime())



#tnow_utc = datetime.datetime.now(tz=pytz.UTC)

#print("Time now is: ", tnow)

time_pacific = datetime.datetime.now()
time_pacific_tz = pytz.timezone("Us/Pacific")
print("Pacific coast time is: ", time_pacific )

time_pacific = time_pacific_tz.localize(time_pacific)

dt_east = time_pacific.astimezone(pytz.timezone("US/Eastern"))

dt_mountain = time_pacific.astimezone(pytz.timezone("Us/Mountain"))
print("Mountain time is: ", dt_mountain)

#time_zone_east = pytz.timezone("Us/Eastern")
#teast = time_zone_east.localize(tnow)

print("East coast time is: ", dt_east)

print("Enter the time in the following format 00, 23 hrs and 00,59 min")
print(" 14:23 for 2 on 23 min")

t=input()
hour, min = t.split(":")

print("you entered: ", hour, " h", min, "min")
input_time_hr = hour
input_time_min = min
#time_24_hr = time.strftime("%H %M")

#print("Entered time in 24 hr clock is" , time_24_hr)

time_entered = input_time_hr + " : " +  input_time_min
print(type(time_entered))
print(time_entered)
#print("East coast time is: ", east_coast_time)
#time_east_coast =
#x = time.strftime("%m/%d/%Y")
#print(x)

#y = "05 February 2020"
#s = time.strptime(y, "%d %B %Y")
#print(s)
