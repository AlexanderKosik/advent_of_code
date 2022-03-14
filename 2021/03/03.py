def msb_string(lines):
    """ 
    Count Most Significant bits of columns of lines
    """
    result = ""
    for column in zip(*lines)[:-1]:
        print("Line:", column)
        zeros = ones = 0
        for bit in column:
            if bit == "0":
                zeros += 1
            else:
                ones += 1
        result += "1" if zeros < ones else "0"
    return result

with open("full.txt") as f:
    lines = [line for line in f]
    gamma_rate = msb_string(lines)

    i_gamma_rate = int(gamma_rate, base=2)
    print(gamma_rate, i_gamma_rate)

    # invert bits of gamme_rate to receive epsilon_rate
    epsilon_rate = "".join("0" if bit == "1" else "1" for bit in gamma_rate)
    i_epsilon_rate = int(epsilon_rate, base=2)
    print(epsilon_rate, i_epsilon_rate)

    print("Result", i_epsilon_rate*i_gamma_rate)

