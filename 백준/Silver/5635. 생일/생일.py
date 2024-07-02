n = int(input())

student_list = []

for _ in range(n):
    n, d, m, y = input().split()
    d = int(d)
    m = int(m)
    y = int(y)
    student_list.append([y, m, d, n])
    
student_list.sort()

print(student_list[-1][3])
print(student_list[0][3])