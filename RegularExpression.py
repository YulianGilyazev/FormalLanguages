import string
import numpy as np


class DpArrays:
    is_substring = []
    is_suf = []
    is_pref = []
    is_inside = []
    has_empty_string = bool

    def __init__(self, arrays_size):
        self.is_substring = np.zeros((arrays_size, arrays_size))
        self.is_suff = np.zeros((arrays_size, arrays_size))
        self.is_pref = np.zeros((arrays_size, arrays_size))
        self.is_inside = np.zeros((arrays_size, arrays_size))
        self.has_empty_string = 0


def concatenate(stack, u):
    if len(stack) < 2:
        raise Exception("IncorrectRegularExpression")
    left_arg = stack[-2]
    right_arg = stack[-1]
    front_stack_mem = DpArrays(len(u))
    for i in range(len(u)):
        for j in range(i, len(u)):
            if left_arg.has_empty_string and right_arg.is_substring[i][j]:
                front_stack_mem.is_substring[i][j] = True
            if right_arg.has_empty_string and left_arg.is_substring[i][j]:
                front_stack_mem.is_substring[i][j] = True
            if left_arg.is_pref[i][j]:
                front_stack_mem.is_pref[i][j] = True
            if right_arg.is_pref[i][j] and left_arg.has_empty_string:
                front_stack_mem.is_pref[i][j] = True
            if right_arg.is_suff[i][j]:
                front_stack_mem.is_suff[i][j] = True
            if left_arg.is_suff[i][j] and right_arg.has_empty_string:
                front_stack_mem.is_suff[i][j] = True
            if right_arg.is_inside[i][j]:
                front_stack_mem.is_inside[i][j] = True
            if left_arg.is_inside[i][j]:
                front_stack_mem.is_inside[i][j] = True
            for k in range(i, j):
                if left_arg.is_substring[i][k] and right_arg.is_substring[k + 1][j]:
                    front_stack_mem.is_substring[i][j] = True
                if left_arg.is_substring[i][k] and right_arg.is_pref[k + 1][j]:
                    front_stack_mem.is_pref[i][j] = True
                if left_arg.is_suff[i][k] and right_arg.is_substring[k + 1][j]:
                    front_stack_mem.is_suff[i][j] = True
                if left_arg.is_suff[i][k] and right_arg.is_pref[k + 1][j]:
                    front_stack_mem.is_inside[i][j] = True
    stack.pop(-1)
    stack.pop(-1)
    front_stack_mem.has_empty_string = (
        left_arg.has_empty_string and right_arg.has_empty_string
    )
    stack.append(front_stack_mem)


def unite(stack, u):
    if len(stack) < 2:
        raise Exception("IncorrectRegularExpression")
    left_arg = stack[-2]
    right_arg = stack[-1]
    for i in range(len(u)):
        for j in range(len(u)):
            left_arg.is_substring[i][j] = max(
                [left_arg.is_substring[i][j], right_arg.is_substring[i][j]]
            )
            left_arg.is_suff[i][j] = max(
                [left_arg.is_suff[i][j], right_arg.is_suff[i][j]]
            )
            left_arg.is_pref[i][j] = max(
                [left_arg.is_pref[i][j], right_arg.is_pref[i][j]]
            )
            left_arg.is_inside[i][j] = max(
                [left_arg.is_inside[i][j], right_arg.is_inside[i][j]]
            )
    stack.pop(-1)
    stack.pop(-1)
    left_arg.has_empty_string = max(
        [left_arg.has_empty_string, right_arg.has_empty_string]
    )
    stack.append(left_arg)


def add_empty_string_re(stack, u):
    front_stack_mem = DpArrays(len(u))
    front_stack_mem.has_empty_string = 1
    stack.append(front_stack_mem)


def add_one_symbol_re(stack, u, cur_symb):
    front_stack_mem = DpArrays(len(u))
    for i in range(len(u)):
        if u[i] == cur_symb:
            front_stack_mem.is_substring[i][i] = True
            front_stack_mem.is_suff[i][i] = True
            front_stack_mem.is_pref[i][i] = True
            front_stack_mem.is_inside[i][i] = True
    front_stack_mem.has_empty_string = 0
    stack.append(front_stack_mem)


def closure(stack, u):
    arg = stack[-1]
    cnt = len(u) + 1
    while cnt > 0:
        cnt -= 1
        for i in range(len(u)):
            for j in range(i, len(u)):
                for k in range(i, j):
                    if arg.is_substring[i][k] and arg.is_substring[k + 1][j]:
                        arg.is_substring[i][j] = True
                    if arg.is_substring[i][k] and arg.is_pref[k + 1][j]:
                        arg.is_pref[i][j] = True
                    if arg.is_suff[i][k] and arg.is_substring[k + 1][j]:
                        arg.is_suff[i][j] = True
                    if arg.is_suff[i][k] and arg.is_pref[k + 1][j]:
                        arg.is_inside[i][j] = True
    stack.pop(-1)
    arg.has_empty_string = 0
    stack.append(arg)


def find_max_substring_size(regular_expression, word):
    stack = []
    for cur_symb in regular_expression:
        if cur_symb.isalpha():
            add_one_symbol_re(stack, word, cur_symb)
        if cur_symb == "1":
            add_empty_string_re(stack, word)
        if cur_symb == "*" or cur_symb == "∗":
            closure(stack, word)
        if cur_symb == "+":
            unite(stack, word)
        if cur_symb == ".":
            concatenate(stack, word)
    if len(stack) > 1:
        raise Exception("IncorrectRegularExpression")
    table = stack[0].is_inside
    max_size = 0
    if word == "1":
        return 0
    for i in range(len(word)):
        for j in range(len(word)):
            if j - i + 1 > max_size and table[i, j]:
                max_size = j - i + 1
    return max_size


def main():
    regular_expression, word = read_input()
    print(find_max_substring_size(regular_expression, word))


if __name__ == "__main__":
    main()
