# put your python code here
# first event variables
first_event_hour = abs(int(input('')))
first_event_minute = abs(int(input('')))
first_event_second = abs(int(input('')))

# second event variables
second_event_hour = abs(int(input('')))
second_event_minute = abs(int(input('')))
second_event_second = abs(int(input('')))

differences_between_moments = ((second_event_hour - first_event_hour) * 3600) + (
    (second_event_minute - first_event_minute) * 60) + (second_event_second - first_event_second)

print(differences_between_moments)
