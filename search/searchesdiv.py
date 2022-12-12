from time import process_time


def search(hash_set):
    # tests: 10000+1 | 20000+1 | 25000+1
    #  time: 1.45s   | 5.91    | 9.33s
    res = {}
    for i in hash_set:
        divisors = [div for div in range(1, i+1) if i % div == 0]
        if len(divisors) == 4:
            res.update({i: divisors})
    return res


def search_v2(hash_set):
    # tests: 10000+1 | 20000+1 | 25000+1
    #  time: 2.02s   |  7.81s  | 12.0s
    res = {}
    def search_divs(num):
        divs = []
        for i in range(1, num+1):
            if num % i == 0:
                divs.append(i)
            if len(divs) > 4:
                return None
        return divs
    for i in hash_set:
        if search_divs(i) != None:
            res.update({i: search_divs(i)})
    return res


def search_v3(hash_set, count_divs):
    #  count_divs: 4
    #  hash_set  : 10000+1 | 20000+1 | 25000+1 | 250000+1
    #  time_v1   : 0.16s   | 0.45s   | 0.64s   | 19.44s
    #  time_v2   : 0.12s   | 0.33s   | 0.45s   | 11.58s
    #  time_v3   : 0.08s   | 0.19s   | 0.23s   | 6.16s

    ''' time_v1 - обычная версия search_divs()
        time_v2 - версия с отсекателем списка line 51
        time_v3 - версия v2 с единичным возовом search_divs(i) для проверки

        функция примает список = hash_set чисел и возвращает среди них такие,
        количество делителей у которых = count_divs
    '''
    res = {}
    def search_divs(num):
        div = 1
        divisors = []
        while div ** 2 <= num:
            if num % div == 0:
                divisors.append(div)
                if div != num // div:
                    divisors.append(num // div)
            if len(divisors) > count_divs:
                return None
            div += 1
        divisors.sort()
        return divisors
    for i in hash_set:
        divisors = search_divs(i)
        if divisors != None:
            res.update({i: divisors})
    return res



len_iter = 10**10
obj = (i for i in range(10**7))
start_time = process_time()
res = search_v3(obj, 4)
print(f'[$Finished in {round(process_time() - start_time, 2)}s]')