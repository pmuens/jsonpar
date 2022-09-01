import src as jsonpar


def demo():
    json = '{"foo":{"bar":[1,2,3]}}'

    parsed = jsonpar.from_string(json)
    print("Parsed: {}".format(parsed))

    stringified = jsonpar.to_string(parsed)
    print("Stringified: {}".format(stringified))


if __name__ == "__main__":
    demo()
