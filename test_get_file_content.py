from functions.get_files_info import get_file_content


def run_tests():
    print("=== Testing get_file_content ===")

    # Test 1: Lorem Ipsum (Truncation Check)
    # Note: Ensure you have created 'calculator/lorem.txt' with > 10k chars first!
    print("\n1. Testing 'lorem.txt' truncation:")
    lorem_result = get_file_content("calculator", "lorem.txt")

    # We don't print the whole thing (it's huge), just the status
    if "truncated at" in lorem_result:
        print("SUCCESS: Truncation message found.")
        print(f"Tail of file: ...{lorem_result[-50:]}")
    else:
        print("FAIL: Truncation message NOT found.")
        print(f"Total length: {len(lorem_result)}")

    # Test 2: Valid File (main.py)
    print("\n2. Result for 'main.py':")
    print(get_file_content("calculator", "main.py"))

    # Test 3: Valid File in Subdirectory (pkg/calculator.py)
    print("\n3. Result for 'pkg/calculator.py':")
    print(get_file_content("calculator", "pkg/calculator.py"))

    # Test 4: Restricted file (Security check)
    print("\n4. Result for '/bin/cat' (Should be Error):")
    print(get_file_content("calculator", "/bin/cat"))

    # Test 5: Missing file
    print("\n5. Result for 'pkg/does_not_exist.py' (Should be Error):")
    print(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    run_tests()
