tickets = input().replace(" ", "")
tickets = tickets.split(",")
special_symbols = ["@", "#", "$", "^"]

for ticket in tickets:
    result = 0
    if len(ticket) == 20:
        for symbol in special_symbols:
            if 20 * symbol in ticket:
                print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
                break

            first_half = ticket[:len(ticket) // 2]
            second_half = ticket[len(ticket) // 2:]
            symbols = symbol * 6

            if symbols in first_half and symbols in second_half:
                result = 6

                for index in range(7, 11):
                    symbols = symbol * index
                    if symbols in first_half and symbols in second_half:
                        result += 1

                print(f'ticket "{ticket}" - {result}{symbol}')
                break

        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")
