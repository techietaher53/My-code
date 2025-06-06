subject1 = int(input('enter your maths marks:'))
subject2 = int(input('enter your english marks:'))
subject3 = int(input('enter your science marks:'))

# Check for total percentage

total_percentage = (100*(subject1 + subject2 + subject3))/300

if(total_percentage>=40 and subject1 >= 33 and subject2 >= 33 and subject3 >= 33):
    print('you are passed:', total_percentage)
else:
    print('you are failed:', total_percentage)
