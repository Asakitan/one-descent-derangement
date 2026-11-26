# 项目状态

从 $n$ 元、恰有一个降点的所有错排中均匀抽样，首项期望为 $3-2^{-(n-2)}$（$n\ge2$）。一次性证明两个 OEIS 条目的第一列猜想。

投稿前校对已明确分数约分的边界：$n=2$ 时分母为 1；奇数分子的论证适用于 $n\ge3$。数值公式不变。

Python 3.9+，仅用标准库。脚本逐个枚举 $n=2,\ldots,8$ 的排列核验完整首项分布；一般 $n$ 的结论由双射证明。

[首页](README.md) · [证明](PROOF.md) · [工作记录](docs/session-log/README.md)

**公开证明版本：** [proof-v1.0.1](https://github.com/Asakitan/one-descent-derangement/releases/tag/proof-v1.0.1)，版本日期 2026-11-26；署名 Chain.Ren（独立研究）。
