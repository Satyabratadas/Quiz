m1 = '''1. If one zero of the quadratic polynomial x² + 3x + k is 2, then the value of k is
(a) 10
(b) -10
(c) 5
(d) -5'''

m2 = '''2. If the zeroes of the quadratic polynomial x2 + (a + 1) x + b are     2 and -3, then
(a) a = -7, b = -1
(b) a = 5, b = -1
(c) a = 2, b = -6
(d) a – 0, b = -6'''

m3 = '''3. The number of polynomials having zeroes as -2 and 5 is
(a) 1
(b) 2
(c) 3
(d) more than 3'''

m4 = '''4. The zeroes of the quadratic polynomial x2 + 99x + 127 are
(a) both positive
(b) both negative
(c) one positive and one negative
(d) both equal'''

m5 = '''5. The zeroes of the quadratic polynomial x² + kx + k, k? 0,
(a) cannot both be positive
(b) cannot both be negative
(c) are always unequal
(d) are always equal'''

p1 = '''1. Light Reflection and Refraction Class 10 MCQ With Answers Pdf Question 1. An object is placed at a distance of 0.25 m
in front of a plane mirror. The distance between the object and image will be
(a) 0.25 m
(b) 1.0 m
(c) 0.5 m
(d) 0.125 m'''

p2 = '''2.MCQ On Light Class 10 Question 2. The angle of incidence for a ray of light having zero reflection angle is
(a) 0
(b) 30°
(c) 45°
(d) 90°'''

p3 = '''3.MCQ Questions On Light Class 10 Question 3. For a real object, which of the following can produce a real image?
(a) Plane mirror
(b) Concave mirror
(c) Concave lens
(d) Convex mirror
'''

p4 = '''4.MCQ On Reflection Of Light Class 10 Question 4. Which of the following mirror is used by a dentist to examine a small cavity?
(a) Convex mirror
(b) Plane mirror
(c) Concave mirror
(d) Combination of convex and concave mirror'''

p5 = '''5.MCQ On Reflection And Refraction Of Light With Answers Pdf Question 5. An object at a distance of 30 cm from a
concave mirror gets its image at the same point. The focal length of the mirror is
(a) – 30 cm
(b) 30 cm
(c) – 15 cm
(d) +15 cm'''                                   # questions as string in a variable


math = {m1 : 'b',m2: 'c', m3 : 'd',m4 : 'a',m5 : 'a'}
physics = {p1 : 'c',p2 : 'a',p3 : 'b',p4 : 'c',p5 : 'c'}              #declare question in a string

name = input("Enter Your Name : ")
print("Hello",name,"This is your Quiz_world \n")
user = int(input("Choose 1: for math solve 2: for physics solution : "))
user_point = 0

if (user == 1):
    for i in math:
        print(i)
        skip = input("Are you skip the question?? y/n : ")
        if skip == 'y':
            continue
        ans = input("Enter the ans : ")
        if ans == math[i]:
            print("Correct Answer, You get 1 point \n")
            user_point = user_point + 1
            print("Score is :- ",user_point)
        else:
            print("Wrong Answer, You lost 1 point \n")
            user_point = user_point - 1
            print("Score is :- ",user_point)
        
        quit = input("Do you want to quit ?? y/n : ")
        if quit == "y":
            break
else:    
        for i in physics:
            print(i)
            skip = input("Are you skip the ans?? y/n : ")
            if skip == 'y':
                continue
            ans = input("Enter the ans : ")
            if ans == physics[i]:
                print("Correct Answer, You get 1 point \n")
                user_point = user_point + 1
                print("Score is :- ",user_point)
            else:
                print("Wrong Answer, You lost 1 point \n")
                user_point = user_point - 1
                print("Score is :- ",user_point)
            
            quit = input("Do you want to quit ?? y/n : ")
            if quit == "y":
                break

print("Final Score is - ",user_point)
        





