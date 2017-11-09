from collections import OrderedDict


class Pricer:
    def __init__(self, file_name):
        file_reader = open(file_name)

        # Get all the lines that
        lines = file_reader.read().splitlines()

        file_reader.close()

        pricing = {}
        for line in lines:
            split = line.split(",")

            # Set the number prefix with the cost inside our dictionary
            pricing[split[0]] = float(split[1])

        self.pricing = pricing

    def find_best_match(self, number):
        best_match = None

        for price in self.pricing:
            if number.startswith(price) and (best_match is None or len(price) > len(best_match)):
                best_match = price

        if best_match is None:
            return None

        return self.pricing[best_match]

    def find_best_matches(self, numbers):
        final_dict = {}

        for number in numbers:
            final_dict[number] = self.find_best_match(number)

        return final_dict


class MultiPricer:
    def __init__(self, file_names):
        self.pricers = []

        for name in file_names:
            self.pricers.append(Pricer(name))

    def find_best_price(self, number):
        best_price = None

        for price in self.pricers:
            cost = price.find_best_match(number)

            if best_price is None or cost < best_price:
                best_price = cost

        return best_price

    def find_best_prices(self, numbers):
        best_prices = {}

        for number in numbers:
            best_price = self.find_best_price(number)

            best_prices[number] = best_price

        return best_prices


if __name__ == "__main__":
    m_test = MultiPricer(['../routes/route-costs-10.txt', '../routes/route-costs-1000000.txt'])

    print(m_test.find_best_prices(['+813023123', '+125313432']))
