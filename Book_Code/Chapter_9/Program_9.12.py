# Program 9.12: Write Python Program to Save Dictionary in Python Pickle

import pickle


def main():
    bbt = {'cooper': 'sheldon'}
    with open('filename.pickle', 'wb') as handle:
        pickle.dump(bbt, handle)
    with open('filename.pickle', 'rb') as handle:
        bbt = pickle.load(handle)
        print(f"Unpickling {bbt}")


if __name__ == "__main__":
    main()