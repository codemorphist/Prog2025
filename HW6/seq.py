def convert(s: str) -> int:
    try:
        return int(s)
    except:
        raise Exception(f"Invalid value to convert to integer: '{s}'")


def get_sign(num: int) -> int:
    return 0 if num >= 0 else 1


def count_sign_change(seq: str) -> int:
    seq_list = seq.split(",")
    seq_num = list(map(convert, seq_list))

    if seq_num[-1] != 0:
        raise Exception("Sequence must ending by 0")
    seq_num.pop()

    count = 0
    prev_sing = get_sign(seq_num[0])
    for num in seq_num:
        sing = get_sign(num) 
        if sing != prev_sing:
            count += 1
            prev_sing = sing

    return count


test_number = 1
def test_count(s: str, expect):
    global test_number

    try:
        res = count_sign_change(s)
        if res == expect:
            test_res = "PASS"
        else:
            test_res = "FAILED"
    except Exception as e:
        res = str(e)
        if res == expect:
            test_res = "PASS"
        else:
            test_res = "FAILED"

    print(f"{test_number}: [{test_res}] count_sing_change(\"{s}\") = ({res})")
    if test_res != "PASS":
        print(f"\n\t[expect: {expect}]\n")
    test_number += 1

if __name__ == "__main__":
    test_count("1,-34,8,14,-5,0", 3)
    test_count("1,2 , -3  ,0", 1)
    test_count("1,2 , -3,    0", 1)
    test_count("1,2 , -3,1", "Sequence must ending by 0")
    test_count("1,2 , -3,", "Invalid value to convert to integer: ''")
    test_count("1,  2 , -3,0", 1)
    test_count("1,  2 0 , -3,0", "Invalid value to convert to integer: '  2 0 '")
    test_count("1,-2,,", "Invalid value to convert to integer: ''")
    test_count("1,  abc,8,14,-5,0", "Invalid value to convert to integer: '  abc'")
