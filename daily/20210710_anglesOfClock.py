# Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock

# def calcAngle(h, m):
#   # Fill this in.

# print calcAngle(3, 30)
# # 75
# print calcAngle(12, 30)
# # 165

def calcAngle(h, m):
    if h==12:
        h=0
    if m==60:
        m=0
        h +=1
        if h>12:
            h = h - 12
    angleHour = 0.5 * (h*60 +m)
    angleminute = 6 * m
    
    angle = abs(angleHour - angleminute)

    angle = min(360 -angle, angle)
    return angle

print(calcAngle(3,30))
print(calcAngle(12,30))