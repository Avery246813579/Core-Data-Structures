from collections import OrderedDict

class Price:
    def __init__(self, file):
        file_reader = open(file)

        lines = file_reader.read().splitlines()

        pricing = {}
        for line in lines:
            split = line.split(",")

            pricing[split[0]] = float(split[1])

        self.pricing = OrderedDict(sorted(pricing.items()))


if __name__ == "__main__":
    price = Price('../routes/route-costs-10.txt')
    print(price.pricing)
