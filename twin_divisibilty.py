def twin_divisibility(n1, n2):
    """Returns a list of numbers between 10 and 3780 which are divisible by n1 but not n2.
    """
    r_list = []
    for i in range(10, 3781):
        if i % n1 == 0 and i % n2 != 0:
            r_list.append(i)
    return r_list