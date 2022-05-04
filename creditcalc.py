def annuity_calc(principal:"", payment:"", periods:"", interest:""):
    import math

    # print('What do you want to calculate?')
    # print('type "n" for number of monthly payments,')
    # print('type "a" for annuity monthly payment amount,')
    # print('type "p" for loan principal:')

    calculate_type = ""
    loan_principal = int(principal)
    monthly_payment = int(payment)
    months = int(periods)
    loan_interest = float(interest) / 12 / 100

    if loan_principal == 0 and monthly_payment != 0 and months != 0 and loan_interest != 0: calculate_type = "p"
    if monthly_payment == 0 and loan_principal != 0 and months != 0 and loan_interest != 0: calculate_type = "a"
    if months == 0 and loan_principal != 0 and monthly_payment != 0 and loan_interest != 0: calculate_type = "n"

    if calculate_type == 'n':
        months = math.ceil(
            math.log(monthly_payment / (monthly_payment - loan_interest * loan_principal), 1 + loan_interest))
        overpayment = monthly_payment * months - loan_principal

        if months == 1:
            print('It will take 1 month to repay the loan')
            print("Overpayment:", overpayment)
        elif months == 12:
            print('It will take 1 year to repay the loan')
            print("Overpayment:", overpayment)
        else:
            year = months // 12
            months %= 12
            print(f'It will take {year} years and {months} months to repay this loan!')
            print("Overpayment:", overpayment)

    elif calculate_type == 'a':

        monthly_payment = math.ceil(loan_principal * (loan_interest * math.pow(1 + loan_interest, months) /
                                                      (math.pow(1 + loan_interest, months) - 1)))
        overpayment = monthly_payment * months - loan_principal

        print(f'Your annuity payment = {monthly_payment} !')
        print("Overpayment:", overpayment)

    elif calculate_type == 'p':

        loan_principal = int(monthly_payment / (
                    (loan_interest * math.pow(1 + loan_interest, months)) / (math.pow(1 + loan_interest, months) - 1)))
        overpayment = monthly_payment * months - loan_principal

        print(f'Your loan principal = {loan_principal} !')
        print("Overpayment:", overpayment)


    else:
        print('Incorrect parameters')


def diff_calc(principal:"", periods:"", interest:""):
    import math

    interest = interest / 12 / 100
    overpayment = 0
    for i in range(1, periods+1):
        payment = math.ceil(principal / periods + interest * (principal - principal * (i - 1) / periods))
        overpayment += payment
        print(f"Month {i}: payment is {payment}")
    overpayment -= principal
    print("\nOverpayment =", overpayment)



import argparse

parser = argparse.ArgumentParser(description="This program will calculate annuity or differentiate credits")

parser.add_argument("--type", choices=["annuity", "diff"], help="Choose what type of credit do you want to calculate?")
parser.add_argument("--principal", default=0)
parser.add_argument("--payment", default=0)
parser.add_argument("--periods", default=0)
parser.add_argument("--interest", default=0)
args = parser.parse_args()
calc_args = [args.principal, args.payment, args.periods, args.interest]

if len(calc_args) != 4:
    print("Incorrect parameters")
else:
    if args.type == "annuity":
        annuity_calc(principal=calc_args[0], payment=calc_args[1], periods=calc_args[2], interest=calc_args[3])
    elif args.type == "diff":
        if int(args.principal) * int(args.periods) * float(args.interest) != 0 and int(args.payment) == 0:
            diff_calc(principal=int(calc_args[0]), periods=int(calc_args[2]), interest=float(calc_args[3]))
        else:
            print("Incorrect parameters")
    else:
        print("Incorrect parameters")

