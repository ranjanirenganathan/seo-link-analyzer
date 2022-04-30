# print_report

def print_report(pages):
    pages = remove_none_values(pages)
    pages_list = sort_pages(pages)
    for page in pages_list:
        url = page[0]
        count = page[1]
        print("Found {} internal links to {}".format(count, url))



# takes a dictionary as input,
# removing any keys from the dictionary that have an associated None value
def remove_none_values(inputdict):
    for key, value in list(inputdict.items()):
        if value is None:
            del inputdict[key]
    return inputdict


def sort_pages(pages):
    data = list(pages.items())
    return sorted(data, key=lambda x: x[1], reverse=True)


