# Make sure your output matches the assignment *exactly*
spend_hour = int(input())

if spend_hour < 2:
    print("That's rare nowadays!")
elif 2 <= spend_hour < 4:
    print("This seems reasonable")
else:
    print("Don't forget to take breaks!")
