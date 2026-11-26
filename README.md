# 恰有一个降点的错排：首项期望

**证明署名：** Chain.Ren · 独立研究 · [完整证明](PROOF.md) · 版本日期：2026-11-26

[固定版本证明](https://github.com/Asakitan/one-descent-derangement/blob/proof-v1.0.0/PROOF.md) · [GitHub Release 与公开时间](https://github.com/Asakitan/one-descent-derangement/releases/tag/proof-v1.0.0) · [引用信息](CITATION.cff)

从 $n$ 元、恰有一个降点的所有错排中均匀抽样，首项期望为 $3-2^{-(n-2)}$（$n\ge2$）。一次性证明两个 OEIS 条目的第一列猜想。

[A332009 · 分子](https://oeis.org/A332009) · [A332010 · 分母](https://oeis.org/A332010) · [完整证明](PROOF.md) · [MIT 许可证](LICENSE)

## 复核

```sh
python -B verify.py
```

Python 3.9+，仅用标准库。脚本逐个枚举 $n=2,\ldots,8$ 的排列核验完整首项分布；一般 $n$ 的结论由双射证明。

本仓库给出可复核证明；不主张已经核定首证优先权。
