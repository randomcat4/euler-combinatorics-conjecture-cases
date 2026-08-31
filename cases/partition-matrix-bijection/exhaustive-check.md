# Exhaustive check

Run the checker from this directory with Python 3:

```text
python verify_bijection.py
```

Expected final output:

```text
full-class counts n=0..8: 1,1,2,4,10,28,88,304,1144
n source target dist-profile
1 1 1 1:1
2 1 1 2:1
3 3 3 2:2,3:1
4 7 7 3:6,4:1
5 21 21 3:6,4:14,5:1
6 67 67 4:36,5:30,6:1
7 237 237 4:24,5:150,6:62,7:1
8 907 907 5:240,6:540,7:126,8:1
PASS: exhaustive structural bijection and both inverses verified for n<=8
```

The program checks the structural maps, their inverses, exact image equality, and the statistic profile for every object through size eight. This is a calibration and regression test. It does not replace the all-order argument in [proof.md](proof.md).
