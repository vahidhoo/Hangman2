vertical = int(input())
horizontal = int(input())

if vertical == 1 and horizontal == 1:
    print(3)
elif vertical == 1 and horizontal == 8:
    print(3)
elif vertical == 8 and horizontal == 1:
    print(3)
elif vertical == 8 and horizontal == 8:
    print(3)
elif vertical > 1 and horizontal == 1:
    print(5)
elif vertical > 1 and horizontal == 8:
    print(5)
elif vertical == 1 and horizontal > 1:
    print(5)
elif vertical == 8 and horizontal > 1:
    print(5)
else:
    print(8)
