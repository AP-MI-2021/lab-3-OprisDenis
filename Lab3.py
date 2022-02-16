def prime(n):  # verifica daca un numar dat este prim
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    i = 3
    while i ** 2 <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def desc(num):  # verifica daca un numar dat are cifrele in ordine descrescatoare
    if num <= 9:
        return True
    else:
        while num > 9:
            if num % 10 >= num/10 % 10:
                return False
            return True

################################################################################


def get_longest_all_not_prime(lista):
    """
    Determina cea mai lunga subsecventa formata doar din numere care nu sunt prime
    :param lista: O lista de numere naturale
    :return: Cea mai lunga subsecventa formata doar din numere care nu sunt prime
    """
    start = -1
    subsequence_max = []
    for i in range(len(lista)):
        if prime(lista[i]) is False:
            if start == -1:
                start = i
            if len(subsequence_max) < i - start + 1:
                subsequence_max = lista[start:i+1]
        else:
            start = -1

    return subsequence_max


def test_get_longest_all_not_primes():
    assert get_longest_all_not_prime([]) == []
    assert get_longest_all_not_prime([2, 4, 10, 3, 1]) == [4, 10]
    assert get_longest_all_not_prime([1, 7, 3, 4, 5]) == [1]
    assert get_longest_all_not_prime([2, 3, 5, 7, 9, 11, 13, 14, 17, 20]) == [9]

################################################################################



################################################################################


def get_longest_digit_count_desc(lista):
    """
    Determina cea mai lunga subsecventa formata doar din numere ale caror cifre sunt in ordine descrescatoare
    :param lista: O lista de numere naturale
    :return: Cea mai lunga subsecventa formata doar din numere ale caror cifre sunt in ordine descrescatoare
    """
    start = -1
    subsequence_max = []
    for i in range(len(lista)):
        if desc(lista[i]):
            if start == -1:
                start = i
            if len(subsequence_max) < i - start + 1:
                subsequence_max = lista[start:i+1]
        else:
            start = -1
    return subsequence_max


def test_get_longest_digit_count_desc():
    assert get_longest_digit_count_desc([]) == []
    assert get_longest_digit_count_desc([1, 2, 3, 4, 45]) == [1, 2, 3, 4]
    assert get_longest_digit_count_desc([98, 99, 97, 95, 89, 12, 21, 20, 32, 44, 54, 66]) == [
        21, 20, 32, 44, 54, 66]
################################################################################


def main():
    test_get_longest_all_not_primes()
    test_get_longest_digit_count_desc()
    end = False
    lista = []
    while not end:
        print("1. Cititi lista")
        print("2. Determinati cea mai lunga subsecventa de numere care nu sunt prime")
        print("3. Determinati cea mai lunga subsecventa de numere ale caror medie aritmetica este mai mica decat un numar dat")
        print("4. Determinati cea mai lunga subsecventa de numere ale caror cifre sunt in ordine descrescatoare ")
        print("x. Iesire")
        optiune = input("Optiune: ")
        if optiune == '1':
            lista = input("Dati numerele separate prin virgula: ").split(",")

        elif optiune == '2':
            lista_nr = []
            for x in lista:
                lista_nr.append(int(x))
            print(get_longest_all_not_prime(lista_nr))
        elif optiune == '3':
            medie = float(input("Introduceti numarul dorit: "))
            lista_nr = []
            for x in lista:
                lista_nr.append(float(x))
            print(get_longest_average_below(lista_nr, medie))
        elif optiune == '4':
            lista_nr = []
            for x in lista:
                lista_nr.append(int(x))
            print(get_longest_digit_count_desc(lista_nr))
        elif optiune == 'x':
            end = True


if __name__ == '__main__':
    main()
