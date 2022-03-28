def str_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
    print(f"String", s)
    print("No. of Upper Characters:", d["UPPER_CASE"])
    print("No. of Lower Characters:", d["LOWER_CASE"])
str_test("The quick Brow Fox")

