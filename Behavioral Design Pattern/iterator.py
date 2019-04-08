def count_to(count):

    numbers_in_german = ["eins","zwei","drei","vier","funf"]

    iterator = zip( range(count), numbers_in_german )

    for position, number in iterator:
        yield number

# Test the generator
for num in count_to(4):
    print("{}". format(num))