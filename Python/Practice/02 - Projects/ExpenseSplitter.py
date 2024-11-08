def calculate_split(total_amount: float, number_of_people: int, currency: str) -> None:
    if number_of_people < 1:
        raise ValueError('Number of people must exceed 1')
    
    share_per_person: float = total_amount / number_of_people


    print('---------')
    print(f'Total expense amount: {currency}{total_amount:,.2f}')
    print(f'Number of people: {number_of_people}')
    print(f'Each person should pay: {currency}{share_per_person:,.2f}')

def main() -> None:
    try:
        total_amount: float = float(input('Enter total expense amount: '))
        number_of_people: int = int(input('Enter number of people sharing the expense: '))

        calculate_split(total_amount, number_of_people, currency="EUR")

    except ValueError as e:
        print(f'Errpr: {e}')
        

if __name__ == '__main__':
    main()