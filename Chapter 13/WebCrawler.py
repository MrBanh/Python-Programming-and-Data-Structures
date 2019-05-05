import urllib.request


def main():
    url = input("Enter a URL: ").strip()
    crawler(url)


def crawler(startingURL):
    list_of_pending_URLS = []
    list_of_traversed_URLS = []

    list_of_pending_URLS.append(startingURL)
    while len(list_of_pending_URLS) > 0 and len(list_of_traversed_URLS) <= 100:
        url_string =list_of_pending_URLS[0]
        del list_of_pending_URLS[0]
        if url_string not in list_of_traversed_URLS:
            list_of_traversed_URLS.append(url_string)
            print("Craw", url_string)

            for s in get_sub_URLS(url_string):
                if s not in list_of_traversed_URLS:
                    list_of_traversed_URLS.append(s)


def get_sub_URLS(url_string):
    list = []

    try:
        input = urllib.request.urlopen(url_string)
        text = input.read().decode()
        current = 0
        current = text.find("http:", current)
        while current > 0:
            end_index = text.find('\"', current)
            if end_index > 0:
                list.append(text[current : end_index])
                current = text.find("http:", end_index)
            else:
                current = -1
    except Exception as ex:
        print("Error:", ex)

    return list


main()
