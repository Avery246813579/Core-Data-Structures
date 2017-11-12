from collections import OrderedDict


class Router:
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
        """ Finds the best match for a number (most matching starting characters)

        Average: O(nm)
            n = number or prices
            m = length of the number

        :return:    A cost as a float
        """
        best_match = None
        best_length = -1

        for prefix in self.pricing:
            # If the prefix is not long enough we continue out
            # if len(prefix) < best_length:
            #     continue
            #
            # # If the route is our phone number break out
            # if number == prefix:
            #     best_match = prefix
            #     break

            # If our number starts with the route prefix and our best match is not set or our current prefix is greater
            # then the last match then we set our current prefix to our best match
            if number.startswith(prefix) and (best_match is None or len(prefix) > best_length):
                best_match = prefix
                best_length = len(prefix)

        # If we never got a best match return nothing
        if best_match is None:
            return None

        # Return the price of our best match
        return self.pricing[best_match]

    def find_best_matches(self, numbers):
        """ Find the best match for a list of numbers

        Average: O(nmp)
            n = number or prices
            m = length of the number
            p = numbers we are checking

        :return:    A dictionary of the best match cost for all the numbers
        """
        best_prices = {}

        # Go through our numbers and get the best match and add it to our return list
        for number in numbers:
            # Add our number and it's best price to our dictionary
            best_prices[number] = self.find_best_match(number)

        return best_prices


class MultiPricer:
    def __init__(self, file_names):
        self.routers = []

        # Create a route for all our files
        for name in file_names:
            self.routers.append(Router(name))

    def find_best_price(self, number):
        """ Find the best price of a number in all our routes

        Average: O(nmr)
            n = number or prices
            m = length of the number
            r = number of routers

        :return:    A cost as a float
        """
        best_price = None

        # Go through all our routes
        for route in self.routers:
            # Find the best match from our router
            cost = route.find_best_match(number)

            # If our best price is not assigned or if our price is lower then we set the best price to the current
            if best_price is None or cost < best_price:
                best_price = cost

        return best_price

    def find_best_prices(self, numbers):
        """ Get the best price for a list of numbers from all our routes.

         Average: O(nmrp)
            n = number or prices
            m = length of the number
            r = number of routers
            p = the length of numbers

         :return:   A dictionary of best prices
         """
        best_prices = {}

        # Four every number, let's find the bet price for it then store it in our dictionary
        for number in numbers:
            best_price = self.find_best_price(number)

            best_prices[number] = best_price

        return best_prices

    def find_and_save_file(self, read_name, write_name):
        """ Gets the costs of all the numbers in a list then creates a new list with that pricing

        Average: O(nmrp)
            n = number or prices
            m = length of the number
            r = number of routers
            p = the length of numbers

        :param read_name:       File we want to read the numbers from
        :param write_name:      File we want to write to with the solution


        :return:
        """
        reader = open(read_name)
        numbers = reader.read().splitlines()
        reader.close()

        best_prices = self.find_best_prices(numbers)

        writer = open(write_name, 'w+')

        for number in best_prices:
            if best_prices[number] is None:
                writer.write(number + ',0\n')
            else:
                writer.write(number + ',' + str(best_prices[number]) + '\n')

        writer.close()


if __name__ == "__main__":
    m_test = MultiPricer(['../routes/route-costs-10.txt', '../routes/route-costs-1000000.txt'])

    # Takes like 2 seconds
    # m_test.find_and_save_file('../routes/phone-numbers-10.txt', '../routes/costs-phone-numbers-10.txt')

    # Takes like 12 seconds
    m_test.find_and_save_file('../routes/phone-numbers-100.txt', '../routes/costs-phone-numbers-100.txt')

    # Takes a long time :)
    # m_test.find_and_save_file('../routes/phone-numbers-1000.txt', '../routes/costs-phone-numbers-1000.txt')
