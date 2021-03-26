def sort_unique_alphanumeric(str):
    """Removes all duplicate whitespace separated words from the string and sorts it alphanumerically.
    """
    split_str = str.split()
    split_str.sort()
    unique_split_str = set(split_str)
    ' '.join(unique_split_str)
    return unique_split_str