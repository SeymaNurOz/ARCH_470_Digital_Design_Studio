__author__ = "seyma"
__version__ = "2022.01.24"

import rhinoscriptsyntax as rs
import math
import random as rnd

air_all=rs.coerce3dpointlist(air)
water_all=rs.coerce3dpointlist(water)
earth_all=rs.coerce3dpointlist(earth)
fire_all=rs.coerce3dpointlist(fire)
planet_center=rs.coerce3dpoint(planet_center)

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) **2+
                     (p1[1] - p2[1]) **2+
                     (p1[2] - p2[2])**2)

def closest(pt,pt_list):
    closest_index=1000
    min_dist=10000
    for i in range(len(pt_list)):
        c_dist=dist(pt_list[i],pt)
        if c_dist<min_dist:
            min_dist=c_dist
            closest_index=i
    if closest_index!=1000:
        return pt_list[closest_index] 
    else:None


att_dict={}
att_air=[]
att_water=[]
att_earth=[]
att_fire=[]

##first attractor##
##att_numarası grasshopperdan gelsin herr sefrerinde yeniden random alıyordu#
att_0=air_all[x]
if degree>0:
    att_1=air_all[x]
    air_all.remove(att_1)
    att_1=rs.RotateObject(att_1,planet_center,degree)
    att_1=rs.coerce3dpoint(att_1)
    att_dict[att_1]=["air"]

#f_d=following distance
if degree>att2_degree+f_d:
    """att1_att2_creation_p=rs.RotateObject(att_0,planet_center,att2_degree)
    att1_att2_creation_p=rs.coerce3dpoint(att1_att2_creation_p)
    att_2=closest(att1_att2_creation_p,water_all)"""
    att_2=water_all[x]
    water_all.remove(att_2)
    att_2=rs.RotateObject(att_2,planet_center,degree-att2_degree-f_d)
    att_2=rs.coerce3dpoint(att_2)
    att_dict[att_2]=["water"]
if degree>90+att2_degree+f_d*2:
    """att1_att3_creation_p=rs.RotateObject(att_0,planet_center,90)
    att1_att3_creation_p=rs.coerce3dpoint(att1_att3_creation_p)
    att_3=closest(att1_att3_creation_p,earth_all)"""
    att_3=earth_all[x]
    earth_all.remove(att_3)
    att_3=rs.RotateObject(att_3,planet_center,degree-att2_degree-2*f_d-90)
    att_3=rs.coerce3dpoint(att_3)
    att_dict[att_3]=["earth"]
if degree>180+att2_degree+f_d*3:
    """att1_att4_creation_p=rs.RotateObject(att_0,planet_center,180)
    att1_att4_creation_p=rs.coerce3dpoint(att1_att4_creation_p)
    att_4=closest(att1_att4_creation_p,fire_all)"""
    att_4=fire_all[x]
    fire_all.remove(att_4)
    att_4=rs.RotateObject(att_4,planet_center,degree-att2_degree-3*f_d-180)
    att_4=rs.coerce3dpoint(att_4)
    att_dict[att_4]=["fire"]


att_list=att_dict.keys()
att_list=rs.coerce3dpointlist(att_list)
print len(att_list)
for att in att_list:
    if att_dict[att][0]=="air":att_air.append(att)
    elif att_dict[att][0]=="water":att_water.append(att)
    elif att_dict[att][0]=="earth":att_earth.append(att)
    elif att_dict[att][0]=="fire":att_fire.append(att)




####


###
air_normal=[]
water_normal=[]
earth_normal=[]
fire_normal=[]

air_effected_a=[]
water_effected_a=[]
earth_effected_a=[]
fire_effected_a=[]

air_effected_w=[]
water_effected_w=[]
earth_effected_w=[]
fire_effected_w=[]

air_effected_e=[]
water_effected_e=[]
earth_effected_e=[]
fire_effected_e=[]

air_effected_f=[]
water_effected_f=[]
earth_effected_f=[]
fire_effected_f=[]


for airs in air_all:
    closest_att=closest(airs,att_list)
    if closest_att!=None:
        if dist(airs,closest_att)<40: ##değişebilir
            if att_dict[closest_att][0]=="air":
                air_effected_a.append(airs)
            elif att_dict[closest_att][0]=="water":
                air_effected_w.append(airs)
            elif att_dict[closest_att][0]=="earth":
                air_effected_e.append(airs)
            elif att_dict[closest_att][0]=="fire":
                air_effected_f.append(airs)
        else:air_normal.append(airs)
    else:air_normal.append(airs)
    

for waters in water_all:
    closest_att=closest(waters,att_list)
    if closest_att!=None:
        if dist(waters,closest_att)<40: ##değişebilir
            if att_dict[closest_att][0]=="air":
                water_effected_a.append(waters)
            elif att_dict[closest_att][0]=="water":
                water_effected_w.append(waters)
            elif att_dict[closest_att][0]=="earth":
                water_effected_e.append(waters)
            elif att_dict[closest_att][0]=="fire":
                water_effected_f.append(waters)
        else:water_normal.append(waters)
    else:water_normal.append(waters)
for earths in earth_all:
    closest_att=closest(earths,att_list)
    if closest_att!=None:
        if dist(earths,closest_att)<40: ##değişebilir
            if att_dict[closest_att][0]=="air":
                earth_effected_a.append(earths)
            elif att_dict[closest_att][0]=="water":
                earth_effected_w.append(earths)
            elif att_dict[closest_att][0]=="earth":
                earth_effected_e.append(earths)
            elif att_dict[closest_att][0]=="fire":
                earth_effected_f.append(earths)
        else:earth_normal.append(earths)
    else:earth_normal.append(earths)

for fires in fire_all:
    closest_att=closest(fires,att_list)
    if closest_att!=None:
        if dist(fires,closest_att)<40: ##değişebilir
            if att_dict[closest_att][0]=="air":
                fire_effected_a.append(fires)
            elif att_dict[closest_att][0]=="water":
                fire_effected_w.append(fires)
            elif att_dict[closest_att][0]=="earth":
                fire_effected_e.append(fires)
            elif att_dict[closest_att][0]=="fire":
                fire_effected_f.append(fires)
        else:fire_normal.append(fires)
    else:fire_normal.append(fires)


"""        
for i in range(time):
    rs.RotateObjects(air_all,center_air,i,Y_axis)
##tur bitince 

def total_dist(point1,p_list):
    for point1 in p_list:
        dist_toplam=0
        for point2 in p_list:
            dist_toplam+=dist(point1,point2)
    return dist_toplam

##att finding
min_total_dist=1000
index=1000
for i in range(len(air_all)):
    current_td=total_dist(air_all[i],air_all)
    print current_td
    if current_td<min_total_dist:
        min_total_dist=current_td
        index=i
    else:pass
print min_total_dist
print i
        
att_dict={}


#for i in range(time):"""
    

