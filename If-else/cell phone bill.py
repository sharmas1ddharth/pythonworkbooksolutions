additional_time = 0.25
additional_text_message = 0.15

minute = float(input("Enter the minutes you talked on phone in a month : "))
text_message = int(input("Enter the number of text messages : "))

final_charge = [0]

if minute > 50 and text_message > 50:
    minute_charge = minute * 0.25
    message_charge = text_message * 0.15
    total_charge = minute_charge + message_charge + 0.44
    tax_charge = total_charge * 5/100
    final_charge = total_charge + tax_charge

elif minute == 50 and text_message == 50:
    total_charge = 15
    tax_charge = total_charge * 5/100
    final_charge = total_charge + tax_charge

print("Your total charge is $", "{:.2f}".format(final_charge), "with extra $0.44 and 5% sales tax")
