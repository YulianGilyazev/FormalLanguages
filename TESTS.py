import unittest
from RegularExpression import fnd_mx


class TestUM(unittest.TestCase):
    def test_exception(self):
        self.assertRaises(BaseException, fnd_mx, "ab.+", "abc")
        self.assertRaises(BaseException, fnd_mx, "a*+", "abc")
        self.assertRaises(BaseException, fnd_mx, "ab.b*c+", "abc")
        self.assertRaises(BaseException, fnd_mx, "acb..bab.c.*ab.ba.+.+*a.", "abbaa")
        self.assertRaises(BaseException, fnd_mx, "ab+c.aba.*+.bac.+.+*", "babc")

    def test_main(self):
        self.assertEqual(5, fnd_mx("acb..bab.c.*.ab.ba.+.+*a.", "abbaa"))
        self.assertEqual(3, fnd_mx("ab+c.aba.*.bac.+.+*", "babc"))
        self.assertEqual(3, fnd_mx("ab.ba.+*", "bab"))
        self.assertEqual(8, fnd_mx("ab.cb.+ab+*cb.+ac.+.ab.ca.+*b.a.ab*+.+", "abaaabbbcbabc"))
        self.assertEqual(7, fnd_mx("ab.cb.+ab+*cb.+ac.+.ab.ca.+*b.a.ab*+.+", "cbaabba"))
        self.assertEqual(2, fnd_mx("ab*.", "bab"))
        self.assertEqual(11, fnd_mx("a*b*.", "bbbbbaaaaabbbbbbaaaabbbb"))
        self.assertEqual(1, fnd_mx("ab.", "bbbbb"))
        self.assertEqual(9, fnd_mx("ab*.1+*a*b.1+*+", "abbbababa"))
        self.assertEqual(5, fnd_mx("ab*a.+1ab.+.", "bbaab"))
        self.assertEqual(6, fnd_mx("ab.a.1+b*a.b+.1ab*.a.++a*b.1+.", "abbabababba"))


if __name__ == '__main__':
    unittest.main()
