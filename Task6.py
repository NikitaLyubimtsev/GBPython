ticket_num = input('введите номер билета: ')

if (int(ticket_num[0]) + int(ticket_num[1]) + int(ticket_num[2])) == (int(ticket_num[3]) + int(ticket_num[4]) + int(ticket_num[5])):
    print('yes')
else:
    print('no')