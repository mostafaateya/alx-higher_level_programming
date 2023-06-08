#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    ss = dir(hidden_4)
    for s in ss:
        if s[:2] != "__":
            print(s)
