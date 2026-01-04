from functions.write_file import write_file


def run_tests():
    print("=== Testing write_file ===")

    # Test 1: Overwrite existing file
    print("\n1. Writing to 'lorem.txt':")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    # Test 2: New file in subdirectory (Checks if makedirs works)
    print("\n2. Writing to 'pkg/morelorem.txt':")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    # Test 3: Security Violation (Should fail)
    print("\n3. Writing to '/tmp/temp.txt':")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))


if __name__ == "__main__":
    run_tests()
