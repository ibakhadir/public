def loan_calc():
        import math

        print('What do you want to calculate?')
        print('type "n" for number of monthly payments,')
        print('type "a" for annuity monthly payment amount,')
        print('type "p" for loan principal:')

        calculate_type = input()

        if calculate_type == 'n':

            print('Enter the loan principal:')
            loan_principal = int(input())

            print('Enter the monthly payment:')
            monthly_payment = int(input())

            print('Enter the loan interest:')
            loan_interest = float(input()) / 12 / 100

            months = math.ceil(math.log(monthly_payment / (monthly_payment - loan_interest * loan_principal), 1 + loan_interest))

            if months == 1:
                print('It will take 1 month to repay the loan')
            elif months == 12:
                print('It will take 1 year to repay the loan')
            else:
                year = months // 12
                months %= 12
                print(f'It will take {year} years and {months} months to repay this loan!')

        elif calculate_type == 'a':

            print('Enter the loan principal:')
            loan_principal = float(input())

            print('Enter the number of periods:')
            months = int(input())

            print('Enter the loan interest:')
            loan_interest = float(input()) / 12 / 100

            monthly_payment = math.ceil(loan_principal * (loan_interest * math.pow(1 + loan_interest, months) /
                                                (math.pow(1+loan_interest, months) - 1)))
            print('Your monthly payment =', monthly_payment)

        elif calculate_type == 'p':

            print('Enter the annuity payment:')
            monthly_payment = float(input())

            print('Enter the number of periods:')
            months = int(input())

            print('Enter the loan interest:')
            loan_interest = float(input()) / 12 / 100

            loan_principal = int(monthly_payment / ((loan_interest * math.pow(1 + loan_interest, months)) / (math.pow(1 + loan_interest, months) - 1)))
            print(f'Your loan principal = {loan_principal} !')


        else:
            print('Please, inter correct type of calculation:')


loan_calc()