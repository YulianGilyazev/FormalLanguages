import string
import numpy as np

def concatenate(st, u):
    if len(st) < 2:
        raise Exception("IncorrectRegularExpression")
    left_arg = st[-2]
    right_arg = st[-1]
    ans = np.zeros((len(u), len(u)))
    ans_suf = np.zeros((len(u), len(u)))
    ans_pref = np.zeros((len(u), len(u)))
    ans_in = np.zeros((len(u), len(u)))
    for i in range(len(u)):
        for j in range(i, len(u)):
            if left_arg[0] and right_arg[1][i][j]:
                ans[i][j] = True
            if right_arg[0] and left_arg[1][i][j]:
                ans[i][j] = True
            if left_arg[3][i][j]:
                ans_pref[i][j] = True
            if right_arg[3][i][j] and left_arg[0]:
                ans_pref[i][j] = True
            if right_arg[2][i][j]:
                ans_suf[i][j] = True
            if left_arg[2][i][j] and right_arg[0]:
                ans_suf[i][j] = True
            if right_arg[4][i][j]:
                ans_in[i][j] = True
            if left_arg[4][i][j]:
                ans_in[i][j] = True
            for k in range(i, j):
                if (left_arg[1][i][k] and right_arg[1][k + 1][j]):
                    ans[i][j] = True
                if (left_arg[1][i][k] and right_arg[3][k + 1][j]):
                    ans_pref[i][j] = True
                if (left_arg[2][i][k] and right_arg[1][k + 1][j]):
                    ans_suf[i][j] = True
                if (left_arg[2][i][k] and right_arg[3][k + 1][j]):
                    ans_in[i][j] = True
    st.pop(-1)
    st.pop(-1)
    st.append([(left_arg[0] and right_arg[0]), ans, ans_suf, ans_pref, ans_in,])


def unite(st, u):
    if len(st) < 2:
        raise Exception("IncorrectRegularExpression")
    left_arg = st[-2]
    right_arg = st[-1]
    for i in range(len(u)):
        for j in range(len(u)):
            left_arg[1][i][j] = max([left_arg[1][i][j], right_arg[1][i][j]])
            left_arg[2][i][j] = max([left_arg[2][i][j], right_arg[2][i][j]])
            left_arg[3][i][j] = max([left_arg[3][i][j], right_arg[3][i][j]])
            left_arg[4][i][j] = max([left_arg[4][i][j], right_arg[4][i][j]])
    st.pop(-1)
    st.pop(-1)
    left_arg[0] = max([left_arg[0], right_arg[0]])
    st.append(left_arg)


def add_empty_string_re(st, u):
    dp = np.zeros([len(u), len(u)])
    dp_suf = np.zeros([len(u), len(u)])
    dp_pref = np.zeros([len(u), len(u)])
    dp_in = np.zeros([len(u), len(u)])
    st.append([1, dp, dp_suf, dp_pref, dp_in])


def add_one_symbol_re(st, u, cur_symb):
    dp = np.zeros([len(u), len(u)])
    dp_suf = np.zeros([len(u), len(u)])
    dp_pref = np.zeros([len(u), len(u)])
    dp_in = np.zeros([len(u), len(u)])
    for i in range(len(u)):
        if u[i] == cur_symb:
            dp[i][i] = True
            dp_suf[i][i] = True
            dp_pref[i][i] = True
            dp_in[i][i] = True
    st.append([0, dp, dp_suf, dp_pref, dp_in])


def closure(st, u):
    arg = st[-1]
    cnt = len(u) + 10
    while cnt > 0:
        cnt -= 1
        for i in range(len(u)):
            for j in range(i, len(u)):
                for k in range(i, j):
                    if arg[1][i][k] and arg[1][k + 1][j]:
                        arg[1][i][j] = True
                    if arg[1][i][k] and arg[3][k + 1][j]:
                        arg[3][i][j] = True
                    if arg[2][i][k] and arg[1][k + 1][j]:
                        arg[2][i][j] = True
                    if arg[2][i][k] and arg[3][k + 1][j]:
                        arg[4][i][j] = True
    st.pop(-1)
    arg[0] = True
    st.append(arg)


def find_max_substring(s, u):
    st = []
    for cur_symb in s:
        if cur_symb.isalpha():
            add_one_symbol_re(st, u, cur_symb)
        if cur_symb == "1":
            add_empty_string_re(st, u)
        if cur_symb == "*" or cur_symb == "∗":
            closure(st, u)
        if cur_symb == "+":
            unite(st, u)
        if cur_symb == ".":
            concatenate(st, u)
    if len(st) > 1:
        raise Exception("IncorrectRegularExpression")
    table = st[0][4]
    max_size = 0
    if u == "1":
        return 0
    for i in range(len(u)):
        for j in range(len(u)):
            if j - i + 1 > max_size and table[i, j]:
                max_size = j - i + 1
    return max_size


def main():
    s, u = input().split()
    print(find_max_substring(s, u))


if __name__ == "__main__":
    main()
