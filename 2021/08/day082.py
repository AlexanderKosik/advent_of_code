import collections

def decoder(numbers, result_mapping, input_string):
    result = ""
    for word in input_string.split():
        trans_result = {value:key for key, value in result_mapping.items()}
        searched = ""
        for char in word:
            searched += trans_result[char]
        searched = "".join(sorted(searched))
        result += str(numbers[searched])
    return int(result)



with open('input.txt') as f:
    total = 0
    for line in f:
        input, target_data = line.split("|")
        length_map = collections.defaultdict(list)

        for element in input.split():
            length_map[len(element)].append(element)

        numbers = {
            "abcefg": 0,
            "cf": 1,
            "acdeg": 2,
            "acdfg": 3,
            "bcdf": 4,
            "abdfg": 5,
            "abdefg": 6,
            "acf": 7,
            "abcdefg": 8,
            "abcdfg": 9,
        }

        result = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
        }

        elements = input.split()
        #print(elements)
        #print(length_map)

        three = set(length_map[3][0])
        two = set(length_map[2][0])
        four = set(length_map[4][0])
        # Calculate the a
        # By: Searching an element with length 3 (target is the '7') and sub elem with length 2
        # (the '1')
        result['a'] = three.difference(two).pop()

        # Calculate the g
        # Search an elem with length 5 (target is the '5') and substract every elem of the 4 and a
        four_and_a = set(four)
        four_and_a.add(result['a'])
        for elem_length_5 in length_map[5]:
            candidate = set(elem_length_5).difference(four_and_a)
            if len(candidate) == 1:
                result['g'] = candidate.pop()

        # Calculate the d
        # By: searching an elem with length 5 (target is the '3') and substracting a, g, and every element
        # of the 1
        for elem_length_5 in length_map[5]:
            substract = set(length_map[2][0])
            substract.add(result['a'])
            substract.add(result['g'])
            candidate = set(elem_length_5).difference(substract)
            if len(candidate) == 1:
                result['d'] = candidate.pop()

        # Calculate the b
        # By: searching an elem with length 6 (target is the '9') and substracting a, g, d and every element of the 1
        for elem_length_6 in length_map[6]:
            substract = set(length_map[2][0])
            substract.add(result['a'])
            substract.add(result['g'])
            substract.add(result['d'])
            candidate = set(elem_length_6).difference(substract)
            if len(candidate) == 1:
                result['b'] = candidate.pop()

        # Calculate the f
        # By: searching an elem with length 5 (target is the '5') and substracting a, b, g, d 
        for elem_length_5 in length_map[5]:
            substract = set(result['b'])
            substract.add(result['a'])
            substract.add(result['g'])
            substract.add(result['d'])
            candidate = set(elem_length_5).difference(substract)
            if len(candidate) == 1:
                result['f'] = candidate.pop()

        # Calculate the c
        # By: searching an elem with length 2 and substract f
        result['c'] = set(length_map[2][0]).difference(set(result['f'])).pop()

        # Calculate the e
        # By: searching an elem with length 7 and substract every element except e
        result['e'] = set(length_map[7][0]).difference(set((result['a'], result['b'],
            result['c'], result['d'], result['f'], result['g']))).pop()

        total += decoder(numbers, result, target_data) 
    print(total)
