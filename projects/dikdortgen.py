import random
adet = 20
liste = [(random.randint(0,100),random.randint(1,100))for _ in range (adet)]
print(liste)
distance_list=list()
min_mesafe=100
max_mesafe=0

for point1 in liste:
    temp_list = list()
    for point2 in liste :
        temp_mes = ((point1[0]-point2[0])**2 + (point1[1]-point2[1])**2)**0.5
        temp_list.append(temp_mes)
        if temp_mes > max_mesafe:
            max_mesafe=temp_mes
            max_points=[point1,point2]
        if temp_mes < min_mesafe and point1!=point2:
            min_mesafe= temp_mes
            min_points=[point1,point2]
    distance_list+=[temp_list]
max_points.sort()
print("min mesafesi olan noktalar: {} , max mesafesi olan noktalar : {} ".format(min_points,max_points))
max_sayac=0
min_sayac=0
MaxX=max_points[0][0],max_points[1][0]
Maxy=max_points[0][1],max_points[1][1]
MinX=max_points[0][0],max_points[1][0]
MinY=max_points[0][1],max_points[1][1]

intersect_maxp=list()
intersect_minp=list()
for point in liste:
    if min(MaxX)<=point[0]<=max(MaxX) and min(Maxy)<=point[1]<=max(Maxy):
        max_sayac+=1
        intersect_maxp.append(point)
    if min(MinX)<=point[0]<=max(MinX) and min(MinY)<=point[1]<=max(MinY):
        min_sayac+=1
        intersect_minp.append(point)
print("max dikdörtgen içerisindeki nokta sayisi", max_sayac)
print("max kesişimler: {}".format(intersect_maxp))
print("min dikdörtgen içerisindeki nokta sayisi", min_sayac)
print("min kesişimler: {}".format(intersect_minp))