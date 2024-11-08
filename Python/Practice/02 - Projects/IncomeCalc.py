def calculate_finances(monthly_income: float, tax_rate: float, monthly_expenses: float, currency: str) -> None:
    yearly_salary: float = monthly_income * 12
    monthly_tax: float = monthly_income * (tax_rate / 100)
    yearly_tax: float = monthly_tax * 12
    yearly_net_income: float = yearly_salary - yearly_tax
    monthly_net_income: float = monthly_income - monthly_tax
    post_expenses_income: float = monthly_net_income - monthly_expenses
    yearly_post_expenses: float = post_expenses_income * 12

    print("---------------")
    print(f'Monthly income: {currency}{monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Monthly tax: {currency}{monthly_tax:,.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income:,.2f}')
    print(f'Annual salary: {currency}{yearly_salary:,.2f}')
    print(f'Annual paid tax: {currency}{yearly_tax:,.2f}')
    print(f'Annual net income: {currency}{yearly_net_income:,.2f}')
    print(f'After expenses: {currency}{post_expenses_income:,.2f}')
    print(f'Annually after expenses: {currency}{yearly_post_expenses:,.2f}')
    print('---------------')

def main() -> None:
    while True:
        try:
            monthly_income: float = float(input('Enter monthly salary: '))
            tax_rate: float = float(input('Enter your tax rate percentage: '))
            monthly_expense: float = float(input('Enter your monthly expenses: '))
            break
        except:
            print("Invalid input.")

    calculate_finances(monthly_income, tax_rate, monthly_expense, currency='EUR')


if __name__ == '__main__':
    main()
