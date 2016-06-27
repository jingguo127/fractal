import turtle
import math
import operator


def cls():
    print "\n" * 100

def cal_sub1(v):
    v_sub = [[0,0],[0,0],[0,0],0]
    
    v_sub[2][0] = v[0][0]+v[3]*0.5
    v_sub[2][1] = v[0][1]
 
    v_sub[0][0] = v[0][0]+v[3]*0.25
    v_sub[0][1] = v[0][1] + v[3]*math.sqrt(3)*0.25

    v_sub[0] = [v_sub[0][0],v_sub[0][1]]

    v_sub[1][0] = v[1][0] - v[3] * 0.25
    v_sub[1][1] = v[0][1] + v[3]*math.sqrt(3)*0.25
    
    v_sub[3] = v[3]*0.5

    return v_sub

def cal_sub2(v):
    v_sub = [[0,0],[0,0],[0,0],0]
    
    v_sub[1][0] = v[2][0] - v[3]*0.25
    v_sub[1][1] = v[2][1]+v[3]*math.sqrt(3)*0.25
    
    v_sub[0][0] = v_sub[1][0] - v[3]*0.5
    v_sub[0][1] = v_sub[1][1]

    v_sub[2][0] = v_sub[1][0] - v[3]*0.25
    v_sub[2][1] = v[2][1]

    v_sub[3] = v[3]*0.5

    return v_sub

def cal_sub3(v):
    v_sub = [[0,0],[0,0],[0,0],0]

    v_sub[0][0] = v[2][0]+0.25*v[3]
    v_sub[0][1] = v[2][1]+v[3]*math.sqrt(3)*0.25

    v_sub[1][0] = v_sub[0][0]+0.5*v[3]
    v_sub[1][1] = v_sub[0][1]

    v_sub[2][0] = v[2][0] + 0.5*v[3]
    v_sub[2][1] = v[2][1]

    v_sub[3] = v[3]*0.5

    return v_sub

def draw_triangle(v):
    brad = turtle.Turtle()
    brad.speed(500000000)
    brad.hideturtle()
    brad.penup()
    brad.goto(v[0])
    brad.pendown()
    brad.goto(v[1])
    brad.goto(v[2])
    brad.goto(v[0])

def draw_triangles(s):
    for e in s:
        draw_triangle(e)

def s_subs(s):

    s_subs = []
    
    for e in s:
        s_subs.append(cal_sub1(e))
        s_subs.append(cal_sub2(e))
        s_subs.append(cal_sub3(e))

    draw_triangles(s)

    return s_subs


window = turtle.Screen()
window.bgcolor("red")


def main(l,n):                

    i = 0
    v = [[l*0.5,l*0.5*math.sqrt(3)],[l*1.5,l*0.5*math.sqrt(3)],[l,0],l]
    s = [v]
    while i < n:
        s = s_subs(s)
        i += 1


l = input("Input the length of the initial triangle's side that you wanna draw (recommande 50-100)")

n = input("Input how many layers do you wanna draw (recommande <6)")

main(l,n)
    
window.exitonclick()
        



    
