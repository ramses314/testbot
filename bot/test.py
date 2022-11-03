import schedule


def gren():
    print(8812)

def main():

    schedule.every(1).seconds.do(gren)

    while True:
        schedule.run_pending()


if __name__ == "__main__":
    main()