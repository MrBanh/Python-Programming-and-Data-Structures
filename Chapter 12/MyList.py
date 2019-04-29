class MyList(list):
    def __init__(self):
        super().__init__()

    def indexOf(self, element, fromIndex):
        for i in range(fromIndex, len(self)):
            if self[i] == element:
                return i
        return -1

    def lastIndexOf(self, element, fromIndex):
        for i in range(0, fromIndex):
            if self[i] == element:
                return i
        return -1


def main():
    list1 = MyList()
    list1.append("Chicago")
    list1.append("Detroit")
    list1.append("Denver")
    list1.append("Chicago")
    list1.append("Atlanta")
    list1.append("New York")
    list1.append("Seattle")
    list1.append("Dallas")
    list1.append("Atlanta")
    list1.append("New York")

    print(list1)
    index = int(input("Enter index: "))
    element = input("Enter element: ")
    print("The index of element", element, "after index", index,
        "is", list1.indexOf(element, index))
    print("The index of last element", element, "before index", index,
        "is", list1.lastIndexOf(element, index))

main()
