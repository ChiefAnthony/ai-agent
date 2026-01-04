from functions.get_files_info import get_files_info


def run_tests():
    print("=== Testing get_files_info ===")

    # Test 1: Current directory (.)
    print("\n1. get_files_info('calculator', '.'):")
    print(get_files_info("calculator", "."))

    # Test 2: Subdirectory (pkg)
    print("\n2. get_files_info('calculator', 'pkg'):")
    print(get_files_info("calculator", "pkg"))

    # Test 3: Outside path Absolute (/bin) - Should fail
    print("\n3. get_files_info('calculator', '/bin'):")
    print(get_files_info("calculator", "/bin"))

    # Test 4: Outside path Relative (../) - Should fail
    print("\n4. get_files_info('calculator', '../'):")
    print(get_files_info("calculator", "../"))


if __name__ == "__main__":
    run_tests()
