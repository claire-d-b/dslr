from in_out import outer
from in_out import square
from in_out import pow


def main():
    try:
        my_counter = outer(3, square)
        print(my_counter())
        print(my_counter())
        print(my_counter())
        print("---")
        another_counter = outer(1.5, pow)
        print(another_counter())
        print(another_counter())
        print(another_counter())
        # wrong_counter = outer()
        # wrong_counter = outer("phrase", square)
        wrong_counter = (100)
        print(wrong_counter())
    except Exception as e:
        raise AssertionError(f"Error: {e}")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
