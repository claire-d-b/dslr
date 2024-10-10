from new_student import Student


def main():
    try:
        student = Student(name="Edward", surname="agle")
        print(student)

        student = Student(name="Edward", surname="agle", id="toto")
        print(student)
    except Exception as e:
        raise AssertionError(f"Error: {e}")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
