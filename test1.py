import datetime


fromTime = datetime.datetime.strptime("2017-02-06 12:00:00,00","%Y-%m-%d %H:%M:%S,%f")
toTime = datetime.datetime.strptime("2017-02-07 22:30:00,00", "%Y-%m-%d %H:%M:%S,%f")


logs = open('/home/sarwesh17/Downloads',"r").readlines()

totalPREDTime = 0
totalCORRTime = 0
totalRSOTime = 0
imageCount = 0
imageCount1 = 0
imageCount2 = 0


for log in logs:
   try:
      currentTime = datetime.datetime.strptime(log[1:24], "%Y-%m-%d %H:%M:%S,%f")
      if fromTime <= currentTime <= toTime:
         if log.find('Correctness Processing thread') != -1:
            if log.find('started') != -1:
               imageName = log[log.find('image: ')+7:log.find('request id')-2]
               imageTime = log[1:24]
               startTime = datetime.datetime.strptime(imageTime,"%Y-%m-%d %H:%M:%S,%f")
            if log.find('completed') != -1:
               imageName = log[log.find(' for image - ')+12:log.find('restaurant id')-2]
               imageTime = log[1:24]
               endTime = datetime.datetime.strptime(imageTime, "%Y-%m-%d %H:%M:%S,%f")
               T = (endTime-startTime).seconds + (endTime-startTime).microseconds/1000000.0
               # print T
               totalCORRTime += T
               imageCount2 += 1
   except:
      continue
Avg2 = totalCORRTime/imageCount2
print Avg2



for log in logs:
   try:
      currentTime = datetime.datetime.strptime(log[1:24], "%Y-%m-%d %H:%M:%S,%f")
      if fromTime <= currentTime <= toTime:
         if log.find('Prediction Processing') != -1 and not log.find('Line Item') != -1:
            if log.find('started') != -1:
               imageName21 = log[log.find('image:')+7:log.find('request id')-2]
               imageTime21 = log[1:24]
               startTime21 = datetime.datetime.strptime(imageTime21,"%Y-%m-%d %H:%M:%S,%f")
            if log.find('completed') != -1:
               imageName21 = log[log.find(' for image - ')+12:log.find('restaurantId')-2]
               imageTime22 = log[1:24]
               endTime21 = datetime.datetime.strptime(imageTime22,"%Y-%m-%d %H:%M:%S,%f")
               T1 = (endTime21-startTime21).seconds + (endTime21-startTime21).microseconds/1000000.0
               # print T1
               totalPREDTime += T1
               imageCount1 += 1
   except:
      continue

Avg1 = totalPREDTime/imageCount1
print Avg1



for log in logs:
   try:
      currentTime = datetime.datetime.strptime(log[1:24],"%Y-%m-%d %H:%M:%S,%f")
      if fromTime <= currentTime <= toTime:
         if log.find('RSO Processing') != -1:
            if log.find('started') != -1:
               imageName = log[log.find('for image - ')+12:log.find('restaurantId')-2]
               imageTime11 = log[1:24]
               startTime22 = datetime.datetime.strptime(imageTime11,"%Y-%m-%d %H:%M:%S,%f")
            if log.find('completed') != -1:
               imageName = log[log.find(' image:')+7:log.find('restaurantId')-2]
               imageTime12 = log[1:24]
               endTime22 = datetime.datetime.strptime(imageTime12,"%Y-%m-%d %H:%M:%S,%f")
               T = (endTime22-startTime22).seconds + (endTime22-startTime22).microseconds/1000000.0
               # print T
               totalRSOTime += T
               imageCount += 1
   except:
      continue
Avg = totalRSOTime/imageCount
print Avg
