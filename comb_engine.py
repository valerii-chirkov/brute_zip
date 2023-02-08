from itertools import chain, combinations


def all_subsets(ss: list) -> chain:
    return chain(*map(lambda x: combinations(ss, x), range(3, len(ss)+1)))


def filter_subsets(list_of_ss: list | chain, startswith: str, len_min: int, len_max: int):
    ss_filtered = list()
    for subset in list_of_ss:
        stt: str = ''.join(subset)
        if startswith:
            if stt.startswith(startswith):
                pass
        if len_min and len_max:
            if len_min <= len(stt) <= len_max:
                ss_filtered.append(stt)
    return ss_filtered
