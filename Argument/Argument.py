from argparse import ArgumentParser


def GetArgument():
    parser = ArgumentParser()
    parser.add_argument("-t",
                        "--target",
                        )
    parser.add_argument("-h",
                        "--host_name",
                        )
    parser.add_argument("-u",
                        "--user_name",
                        )
    parser.add_argument("-m",
                        "--mode",
                        choices=["Main", "Sub"]
                        )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = GetArgument()

    print(args)
