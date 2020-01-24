import unittest
from RegularExpression import find_max_substring


class TestUM(unittest.TestCase):
    def test_exception(self):
        self.assertRaises(BaseException, find_max_substring, "ab.+", "abc")
        self.assertRaises(BaseException, find_max_substring, "a*+", "abc")
        self.assertRaises(BaseException, find_max_substring, "ab.b*c+", "abc")
        self.assertRaises(BaseException, find_max_substring, "acb..bab.c.*ab.ba.+.+*a.", "abbaa")
        self.assertRaises(BaseException, find_max_substring, "ab+c.aba.*+.bac.+.+*", "babc")

    def test_main(self):
        self.assertEqual(5, find_max_substring("acb..bab.c.*.ab.ba.+.+*a.", "abbaa"))
        self.assertEqual(3, find_max_substring("ab+c.aba.*.bac.+.+*", "babc"))
        self.assertEqual(3, find_max_substring("ab.ba.+*", "bab"))
        self.assertEqual(8, find_max_substring("ab.cb.+ab+*cb.+ac.+.ab.ca.+*b.a.ab*+.+", "abaaabbbcbabc"))
        self.assertEqual(7, find_max_substring("ab.cb.+ab+*cb.+ac.+.ab.ca.+*b.a.ab*+.+", "cbaabba"))
        self.assertEqual(2, find_max_substring("ab*.", "bab"))
        self.assertEqual(11, find_max_substring("a*b*.", "bbbbbaaaaabbbbbbaaaabbbb"))
        self.assertEqual(1, find_max_substring("ab.", "bbbbb"))
        self.assertEqual(9, find_max_substring("ab*.1+*a*b.1+*+", "abbbababa"))
        self.assertEqual(5, find_max_substring("ab*a.+1ab.+.", "bbaab"))
        self.assertEqual(6, find_max_substring("ab.a.1+b*a.b+.1ab*.a.++a*b.1+.", "abbabababba"))
        self.assertEqual(0, find_max_substring("1", "1"))
        self.assertEqual(0, find_max_substring("ab.a.1+b*a.b+.1ab*.a.++a*b.1+.", "1"))
        self.assertEqual(10, find_max_substring("ab.ca.+*ab.c.+ac.ba.c.+*ac.*.ca.+.",  "bbaabcabacbaaa"))
        self.assertEqual(11, find_max_substring("ab.ca.+*ab.c.+ac.ba.c.+*ac.*.ca.+.", "ccacbacacacbb"))
        self.assertEqual(1, find_max_substring("1a.c.*", "ccc"))
        self.assertEqual(0, find_max_substring("ab.c+1+", "1"))


if __name__ == '__main__':
    unittest.main()
