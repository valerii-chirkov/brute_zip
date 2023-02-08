from patterns import list_of_patterns
from comb_engine import all_subsets, filter_subsets
from zip_engine import try_extract


src_from = '/path/to/your_zip.zip'
src_to = '/path/to/you_zip_unlocked'

# your patterns to shuffle and combine
patterns = all_subsets(ss=list_of_patterns)

# filter your patterns (e.g. set the required length or required start-word of the password)
patterns_filtered = filter_subsets(list_of_ss=patterns, startswith='', len_min=40, len_max=80)

if __name__ == '__main__':
    # if the extraction is successful-you will get your password in console and in a file,
    # also src_to will be filled with unzipped files
    for pattern in patterns_filtered:
        try_extract(pattern, src_from, src_to)
