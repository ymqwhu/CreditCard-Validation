# Main function
def main():
    cc_num = input("Enter your credit card number!\n")

    global leng
    leng = len(cc_num)

    card_type(cc_num)

    test(cc_num)

    grab_num(cc_num)

# Testing credit card digits and char
def test(s):
    try:
        int(s)
        if leng in range(17):
            print("\n")
        else:
            print("Digits wrong")
    except ValueError:
        print("Wrong format! Start Over!")

# validating card number
def grab_num(s):

    # grabbing numbers
    c = leng - 2
    pular = []
    while c >= 0:
        pular.append(s[c])
        c = c - 2
    c = leng - 1
    odd = []
    while c >= 0:
        odd.append(s[c])
        c = c - 2

    # converting string to int and double them
    dd_int = []
    for i in pular:
        dd_int.append(int(i)*2)
    # split ten digit and single digit
    counter = 0
    for i in dd_int:
        if i >= 10:
            counter += 1
    sum_pural = sum(dd_int) - counter * 9

    odd_int = []
    for i in odd:
        odd_int.append(int(i))
    # sum and test %10
    sum_all = sum(odd_int)+sum_pural
    if sum_all%10 != 0:
        print("Invaid Entry")
    else:
        print("Legit Entry")

def card_type(n):
    i = 0
    first_two = []
    while i < 2:
        first_two.append(int(n[i]))
        i += 1
    first_two = first_two[0]*10 + first_two[1]

    if str(first_two) in ("34","37"):
        print("AMEX")
    elif str(first_two) in ("51","52","53","54","54"):
        print("MasterCard")
    elif int(int(first_two)/10) == 4:
        print("Visa")
    else:
        print("Unknown")
main()
