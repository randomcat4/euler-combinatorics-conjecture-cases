# Problem

## Primary Source

Levente Bodnar, Jun Gao, Jared Leon, Xizhi Liu, Oleg Pikhurko, and Shumin Sun,
"The inducibility of 6-vertex graphs," arXiv:2606.00290v3.

The source statement used here is Conjecture 4.7, on physical PDF page 29. The
recursive graphon convention is in Section 4 on physical PDF page 26, and the
induced-density normalization is given earlier in the paper.

## Definitions

Let `F29` be the graph on vertex set `{0,1,2,3,4,5}` with edge set

```text
{03,04,13,15,45}.
```

For a graphon `W`, the labelled induced density is denoted `t(F29,W)`. The
source induced-density normalization is

```text
p(F29,W) = 6! / |Aut(F29)| * t(F29,W).
```

For `F29`, `|Aut(F29)|=10`, so `p(F29,W)=72*t(F29,W)`.

A six-part recursive pattern has six equal-measure parts. Each off-diagonal
cell is constant `0` or `1`. Each diagonal cell is `0`, `1`, or `R`, where `R`
means a scaled recursive copy of the whole graphon. Codes are written as

```text
off=<15 bits>;diag=<six symbols from 0,1,R>.
```

The off-diagonal pair order is

```text
01,02,03,04,05,12,13,14,15,23,24,25,34,35,45.
```

In the displayed 15-bit string, the rightmost bit is the first pair in that
order.

## Public Scope

This case treats only the equality assertion

```text
lambda_F29 = 24/1555
```

in Conjecture 4.7. A single graphon with `p(F29,W)>24/1555` is enough to
disprove that equality.

## Non-Claims

- No value of the true global inducibility `lambda_F29` is claimed.
- No optimality of the displayed witness is claimed.
- No other six-vertex graph case is classified.
- No statement is made about variants with a different graphon convention or normalization.
- Public priority and novelty are not established.
