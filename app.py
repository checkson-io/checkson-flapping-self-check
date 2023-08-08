import sys
import os
import requests

checkson_dir = os.environ['CHECKSON_DIR']
persistent_dir = f"{checkson_dir}/persistent"
result_file = f"{persistent_dir}/result"


def write_result(result):
    if not os.path.exists(persistent_dir):
        os.makedirs(persistent_dir)

    with open(result_file, "w") as f:
        f.write(str(result))


def read_last_result():
    if not os.path.exists(result_file):
        return False
    with open(result_file) as f:
        return "True" in f.read()


def main():
    last_result = read_last_result()
    result = not last_result
    write_result(result)

    if result:
        print("Check successful")
        sys.exit(0)
    else:
        print("Check unsuccessful")
        sys.exit(1)


if __name__ == "__main__":
    main()
