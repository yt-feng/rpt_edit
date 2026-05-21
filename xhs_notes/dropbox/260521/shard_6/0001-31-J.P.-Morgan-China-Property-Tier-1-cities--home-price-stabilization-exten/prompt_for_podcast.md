你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
# China Property

Tier 1 cities' home price stabilization extends into April

The latest NBS data for April shows a continued stabilization trend in home prices: (1) tier-1 cities' secondary price growth remained at +0.4% M/M, with all four cities showing positive growth; (2) 70-city home price decline marginally narrowed in both primary & secondary. Regarding the share price weakness on 18 May (sector -4% vs. HSI -1%), we believe it was mostly due to a lack of major upside surprises from the NBS data, triggering some profit-taking (after all, the sector has outperformed the HSI by 16% over the past month). We remain positive on SOE developers with a strong focus on tier-1 cities (COLI, CR Land & Jinmao).

- 70-city primary home prices - M/M decline narrowed: M/M decline narrowed from -0.21% M/M in March to -0.19% M/M in April. While tier-1 cities continued to outperform (+0.1% M/M) led by Shanghai (+0.4% M/M) (Table 1), home prices in top tier-2 cities also turned marginally positive to +0.07% M/M (the first time since May 2025) (outperformers: Hangzhou +0.4% M/M, Nanjing +0.3% M/M).   
- 70-city secondary home prices - all four tier-1 cities saw positive M/M growth (2nd month in a row): Overall secondary home prices fell $0.23\%$ M/M in April, marginally narrowing from $-0.24\%$ in March. Tier-1 cities recorded positive M/M growth $(+0.4\%)$ for the second consecutive month, with all 4 cities seeing positive growth (Beijing: $+0.4\%$ ; Shanghai $+0.7\%$ ; Guangzhou $+0.2\%$ ; Shenzhen $+0.3\%$ ). We also cross-check the trend with Centraline's tier-1 city secondary home price index, which shows $+0.6\%$ M/M growth (down from $+0.9\%$ M/M but still positive). For the full year of 2026, we expect a soft form of stabilization in secondary home prices among tier-1 cities (particularly Shanghai, where secondary inventory months have notably dropped - Figure 5). This will also be partially supported by a $3\%$ drop in secondary listings in tier-1 cities in April (after a $4\%$ increase in March, partially due to seasonality).   
- Y/Y decline in national sales value narrowed due to a lower base: Residential sales value Y/Y decline narrowed from -15% Y/Y in March to -7% Y/Y in April (Figure 13), in line with top 100 developers' contracted sales (report). That said, the narrowing Y/Y decline is partially due to a lower base. Compared to the 2018-21 average, the decline widened from -40% in March to -53% in April (Table 7). For the full year of 2026, we forecast a 7% Y/Y decline. We expect the Y/Y decline over the next few months will likely stay in the low/mid-single-digit % range due to a lower base.   
- New starts and completions remain weak: New starts fell 27% Y/Y in April (Figure 15), widening from -17% Y/Y in March, due to a weaker land market in 2H25. We expect new starts to remain weak over the next few months due to soft land sales volume in 1Q26. We revise down our full-year new starts forecast to -18% Y/Y, implying a 16% Y/Y decline for the rest of the year. The bright side of weak new starts is the potentially lower new supply in the primary market, which may help stabilize home prices. Meanwhile, completions fell 19% Y/Y (March: -19%) (Figure 16). For FY26, we expect a 19% Y/Y decline, implying a 17% Y/Y decline for the rest of the year.

# Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC

(852) 2800-8513

karl.chan@JPM.com

Venus Choi

(852) 2800-8599

venus.choi@JPM.com

Jocelyn Gao

(852) 2800-8529

jocelyn.gao@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

See page 19 for analyst certification and important disclosures, including non-US analyst disclosures.

# Home Price Trends

Table 1: Tier-1 cities - home price M/M growth (NBS & Centraline) 

<table><tr><td></td><td>May-25</td><td>Jun-25</td><td>Jul-25</td><td>Aug-25</td><td>Sep-25</td><td>Oct-25</td><td>Nov-25</td><td>Dec-25</td><td>Jan-26</td><td>Feb-26</td><td>Mar-26</td><td>Apr-26</td></tr><tr><td colspan="13">Primary (NBS)</td></tr><tr><td>Beijing</td><td>-0.4%</td><td>-0.3%</td><td>0.0%</td><td>-0.4%</td><td>0.2%</td><td>-0.1%</td><td>-0.5%</td><td>-0.4%</td><td>-0.3%</td><td>0.2%</td><td>0.0%</td><td>-0.2%</td></tr><tr><td>Shanghai</td><td>0.7%</td><td>0.4%</td><td>0.3%</td><td>0.4%</td><td>0.3%</td><td>0.3%</td><td>0.1%</td><td>0.2%</td><td>0.0%</td><td>0.2%</td><td>0.3%</td><td>0.4%</td></tr><tr><td>Guangzhou</td><td>-0.8%</td><td>-0.5%</td><td>-0.3%</td><td>-0.2%</td><td>-0.6%</td><td>-0.8%</td><td>-0.5%</td><td>-0.6%</td><td>-0.6%</td><td>0.0%</td><td>0.3%</td><td>0.1%</td></tr><tr><td>Shenzhen</td><td>-0.4%</td><td>-0.6%</td><td>-0.6%</td><td>-0.4%</td><td>-1.0%</td><td>-0.7%</td><td>-0.9%</td><td>-0.5%</td><td>-0.4%</td><td>-0.3%</td><td>0.2%</td><td>0.1%</td></tr><tr><td>Tier-1 Primary (NBS)</td><td>-0.2%</td><td>-0.2%</td><td>-0.2%</td><td>-0.2%</td><td>-0.3%</td><td>-0.3%</td><td>-0.5%</td><td>-0.3%</td><td>-0.3%</td><td>0.0%</td><td>0.2%</td><td>0.1%</td></tr><tr><td colspan="13">Secondary (NBS)</td></tr><tr><td>Beijing</td><td>-0.8%</td><td>-1.0%</td><td>-1.1%</td><td>-1.2%</td><td>-0.9%</td><td>-1.1%</td><td>-1.3%</td><td>-1.3%</td><td>-0.2%</td><td>0.3%</td><td>0.6%</td><td>0.4%</td></tr><tr><td>Shanghai</td><td>-0.7%</td><td>-0.7%</td><td>-0.9%</td><td>-1.0%</td><td>-1.0%</td><td>-0.9%</td><td>-0.8%</td><td>-0.6%</td><td>-0.4%</td><td>0.2%</td><td>0.4%</td><td>0.7%</td></tr><tr><td>Guangzhou</td><td>-0.8%</td><td>-0.7%</td><td>-1.0%</td><td>-0.9%</td><td>-0.8%</td><td>-0.9%</td><td>-1.2%</td><td>-1.0%</td><td>-0.7%</td><td>-0.5%</td><td>0.2%</td><td>0.2%</td></tr><tr><td>Shenzhen</td><td>-0.5%</td><td>-0.5%</td><td>-0.9%</td><td>-0.8%</td><td>-1.0%</td><td>-0.9%</td><td>-1.0%</td><td>-0.6%</td><td>-0.6%</td><td>-0.4%</td><td>0.4%</td><td>0.3%</td></tr><tr><td>Tier-1 Secondary (NBS)</td><td>-0.7%</td><td>-0.7%</td><td>-1.0%</td><td>-1.0%</td><td>-0.9%</td><td>-0.9%</td><td>-1.1%</td><td>-0.9%</td><td>-0.5%</td><td>-0.1%</td><td>0.4%</td><td>0.4%</td></tr><tr><td colspan="13">Secondary (Centaline)</td></tr><tr><td>Beijing</td><td>-0.9%</td><td>-1.6%</td><td>-1.5%</td><td>-1.8%</td><td>-2.1%</td><td>-1.9%</td><td>-1.9%</td><td>-1.9%</td><td>-0.5%</td><td>1.2%</td><td>1.5%</td><td>0.2%</td></tr><tr><td>Shanghai</td><td>-1.4%</td><td>-1.4%</td><td>-1.7%</td><td>-1.7%</td><td>-1.5%</td><td>-2.2%</td><td>-2.0%</td><td>-2.8%</td><td>-0.5%</td><td>0.9%</td><td>1.0%</td><td>1.6%</td></tr><tr><td>Guangzhou</td><td>-1.0%</td><td>-1.4%</td><td>-1.2%</td><td>-1.8%</td><td>-1.4%</td><td>-2.0%</td><td>-1.9%</td><td>-1.3%</td><td>-0.8%</td><td>-1.5%</td><td>0.8%</td><td>-0.3%</td></tr><tr><td>Shenzhen</td><td>-1.1%</td><td>-0.5%</td><td>-1.1%</td><td>-1.0%</td><td>-1.5%</td><td>-0.5%</td><td>-1.0%</td><td>-1.6%</td><td>-1.3%</td><td>0.9%</td><td>0.1%</td><td>1.0%</td></tr><tr><td>Tier-1 Secondary (Centaline)</td><td>-1.1%</td><td>-1.2%</td><td>-1.4%</td><td>-1.6%</td><td>-1.6%</td><td>-1.6%</td><td>-1.7%</td><td>-1.9%</td><td>-0.8%</td><td>0.4%</td><td>0.9%</td><td>0.6%</td></tr></table>

Source: NBS, Centaline

Figure 1: Tier-1 cities - secondary home price index (NBS & Centraline) with major nationwide easing/narrative change   
![](images/c7ba6de86a04781560ab3131bc77f81dc6f7d4926a899337b520172791c11671.jpg)

<details>
<summary>line</summary>

| Date     | Tier 1 cities (NBS) | Tier 1 cities (Centraline) | Shanghai (NBS) | Shanghai (Centraline) |
|----------|---------------------|---------------------------|----------------|-----------------------|
| Sep-21   | 100                 | 100                       | 100            | 100                   |
| Dec-21   | ~98                 | ~97                       | ~101           | ~101                  |
| Mar-22   | ~99                 | ~98                       | ~102           | ~102                  |
| Jun-22   | ~100                | ~100                      | ~103           | ~103                  |
| Sep-22   | ~99                 | ~98                       | ~104           | ~104                  |
| Dec-22   | ~97                 | ~95                       | ~103           | ~95                   |
| Mar-23   | ~98                 | ~96                       | ~104           | ~96                   |
| Jun-23   | ~97                 | ~97                       | ~105           | ~97                   |
| Sep-23   | ~95                 | ~95                       | ~104           | ~95                   |
| Dec-23   | ~93                 | ~90                       | ~103           | ~90                   |
| Mar-24   | ~90                 | ~85                       | ~102           | ~85                   |
| Jul-24   | ~88                 | ~75                       | ~101           | ~75                   |
| Oct-24   | ~85                 | ~70                       | ~100           | ~70                   |
| Jan-25   | ~83                 | ~70                       | ~99            | ~70                   |
| Apr-25   | ~82                 | ~68                       | ~98            | ~68                   |
| Jul-25   | ~80                 | ~65                       | ~97            | ~65                   |
| Oct-25   | ~78                 | ~63                       | ~96            | ~63                   |
| Jan-26   | ~75                 | ~62                       | ~95            | ~62                   |
| Apr-26   | ~73                 | ~61                       | ~94            | ~61                   |
</details>

Source: NBS, Centraline

Figure 2: Tier-1 cities - secondary home price M/M growth (NBS vs. Centraline)   
![](images/9592c35f52a62f765897e7ac376bf10a1319c23cec86cd2fdaff1e243101f023.jpg)

<details>
<summary>line</summary>

| Date    | NBS   | Centraline |
|---------|-------|-----------|
| Oct-21  | -0.5% | -0.8%     |
| Jan-22  | 0.2%  | -0.3%     |
| Apr-22  | 0.1%  | 0.5%      |
| Jul-22  | -0.1% | -0.6%     |
| Oct-22  | -0.3% | -0.9%     |
| Jan-23  | 0.4%  | -0.7%     |
| Apr-23  | 0.6%  | 0.8%      |
| Jul-23  | -0.5% | -1.2%     |
| Oct-23  | -0.8% | -1.5%     |
| Jan-24  | -1.0% | -1.8%     |
| Apr-24  | -0.7% | -1.3%     |
| Jul-24  | -0.9% | -1.6%     |
| Oct-24  | -0.6% | -1.4%     |
| Jan-25  | 0.1%  | -0.8%     |
| Apr-25  | -0.4% | -1.1%     |
| Jul-25  | -0.6% | -1.3%     |
| Oct-25  | -0.8% | -1.5%     |
| Jan-26  | -0.5% | -1.7%     |
| Apr-26  | 0.3%  | 0.6%      |
</details>

Note: Key nationwide policy easing / government's narrative change on housing market is shown as green. Source: NBS, Centaline

Table 2: Tier-1 cities - annual home price growth 

<table><tr><td></td><td>2021</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026 YTD</td><td>vs. peak</td></tr><tr><td colspan="8">Primary (NBS)</td></tr><tr><td>70-city</td><td>2.0%</td><td>-2.3%</td><td>-0.9%</td><td>-5.8%</td><td>-3.1%</td><td>-0.7%</td><td>-13.4%</td></tr><tr><td>Tier-1 average</td><td>4.6%</td><td>2.6%</td><td>-0.2%</td><td>-4.0%</td><td>-1.7%</td><td>0.3%</td><td>-6.9%</td></tr><tr><td>Beijing</td><td>5.4%</td><td>5.5%</td><td>2.1%</td><td>-5.5%</td><td>-2.0%</td><td>-0.3%</td><td>-8.4%</td></tr><tr><td>Shanghai</td><td>4.1%</td><td>4.2%</td><td>4.4%</td><td>4.9%</td><td>5.0%</td><td>0.9%</td><td>0.0%</td></tr><tr><td>Guangzhou</td><td>6.3%</td><td>0.3%</td><td>-2.6%</td><td>-10.4%</td><td>-4.3%</td><td>-0.2%</td><td>-17.7%</td></tr><tr><td>Shenzhen</td><td>3.5%</td><td>-0.1%</td><td>-3.1%</td><td>-7.3%</td><td>-3.8%</td><td>-0.4%</td><td>-16.0%</td></tr><tr><td colspan="8">Secondary (NBS)</td></tr><tr><td>70-city</td><td>0.9%</td><td>-3.8%</td><td>-4.1%</td><td>-8.1%</td><td>-6.1%</td><td>-0.9%</td><td>-22.5%</td></tr><tr><td>Tier-1 average</td><td>5.4%</td><td>0.5%</td><td>-3.4%</td><td>-6.8%</td><td>-6.9%</td><td>0.7%</td><td>-17.4%</td></tr><tr><td>Beijing</td><td>7.8%</td><td>4.9%</td><td>-1.2%</td><td>-6.2%</td><td>-6.9%</td><td>1.1%</td><td>-15.4%</td></tr><tr><td>Shanghai</td><td>6.7%</td><td>3.5%</td><td>-3.3%</td><td>-5.0%</td><td>-4.6%</td><td>0.9%</td><td>-13.3%</td></tr><tr><td>Guangzhou</td><td>6.8%</td><td>-0.3%</td><td>-4.4%</td><td>-12.7%</td><td>-7.3%</td><td>-0.8%</td><td>-24.7%</td></tr><tr><td>Shenzhen</td><td>1.5%</td><td>-3.7%</td><td>-2.5%</td><td>-9.5%</td><td>-4.8%</td><td>-0.3%</td><td>-21.0%</td></tr><tr><td colspan="8">Secondary (Centaline)</td></tr><tr><td>Tier-1 average</td><td>10.4%</td><td>-4.2%</td><td>-12.2%</td><td>-12.7%</td><td>-12.5%</td><td>1.1%</td><td>-39.5%</td></tr><tr><td>Beijing</td><td>14.3%</td><td>5.3%</td><td>-11.4%</td><td>-13.5%</td><td>-13.3%</td><td>2.5%</td><td>-36.5%</td></tr><tr><td>Shanghai</td><td>14.3%</td><td>-5.9%</td><td>-11.8%</td><td>-13.3%</td><td>-13.1%</td><td>3.0%</td><td>-37.5%</td></tr><tr><td>Guangzhou</td><td>12.6%</td><td>-3.9%</td><td>-11.4%</td><td>-13.7%</td><td>-14.5%</td><td>-1.7%</td><td>-40.9%</td></tr><tr><td>Shenzhen</td><td>0.5%</td><td>-12.1%</td><td>-14.1%</td><td>-10.1%</td><td>-9.2%</td><td>0.7%</td><td>-43.2%</td></tr></table>

Source: NBS, Centraline

Figure 3: Centraline secondary asking price index vs NBS secondary home price index M/M in tier-1 cities   
![](images/a5cc75c26dff20bf7c26639f8641e2ceabf79c6245047ba03bf20b608735e5ed.jpg)

<details>
<summary>line</summary>

| Date    | Tier-1 cities' secondary asking price index | Tier-1 cities' secondary home price M/M change |
|---------|---------------------------------------------|--------------------------------------------------|
| May-23  | ~28                                         | ~25                                              |
| Jun-23  | ~22                                         | ~20                                              |
| Jul-23  | ~25                                         | ~22                                              |
| Aug-23  | ~28                                         | ~28                                              |
| Sep-23  | ~30                                         | ~30                                              |
| Oct-23  | ~20                                         | ~25                                              |
| Nov-23  | ~18                                         | ~20                                              |
| Dec-23  | ~19                                         | ~18                                              |
| Jan-24  | ~20                                         | ~20                                              |
| Feb-24  | ~25                                         | ~25                                              |
| Mar-24  | ~28                                         | ~28                                              |
| Apr-24  | ~16                                         | ~18                                              |
| May-24  | ~25                                         | ~25                                              |
| Jun-24  | ~26                                         | ~26                                              |
| Jul-24  | ~25                                         | ~25                                              |
| Aug-24  | ~20                                         | ~20                                              |
| Sep-24  | ~25                                         | ~25                                              |
| Oct-24  | ~37                                         | ~35                                              |
| Nov-24  | ~30                                         | ~30                                              |
| Dec-24  | ~28                                         | ~28                                              |
| Jan-25  | ~25                                         | ~25                                              |
| Feb-25  | ~30                                         | ~30                                              |
| Mar-25  | ~28                                         | ~30                                              |
| Apr-25  | ~25                                         | ~25                                              |
| May-25  | ~20                                         | ~20                                              |
| Jun-25  | ~18                                         | ~18                                              |
| Jul-25  | ~16                                         | ~16                                              |
| Aug-25  | ~18                                         | ~18                                              |
| Sep-25  | ~16                                         | ~16                                              |
| Oct-25  | ~18                                         | ~18                                              |
| Nov-25  | ~16                                         | ~16                                              |
| Dec-25  | ~18                                         | ~18                                              |
| Jan-26  | ~20                                         | ~20                                              |
| Feb-26  | ~25                                         | ~25                                              |
| Mar-26  | ~30                                         | ~30                                              |
| Apr-26  | ~35                                         | ~35                                              |
| May-26  | ~30                                         | ~30                                              |
</details>

Source: Centraline, Wind, NBS.   
Note: The asking price index represents the percentage of projects with home price increases. For example, an index of 20 means that 20% of projects raise prices (while 80% do not).

# Inventory

Figure 4: Tier-1 cities - primary inventory volume and inventory months   
![](images/5fb4e29c71110ec279242928d0ead305dfd432cdd707966079e36ebb1c8f67e2.jpg)

<details>
<summary>line</summary>

| Date    | Tier-1 cities primary inventory volume (mn sqm) | Shanghai primary inventory volume (mn sqm) | Tier-1 cities inventory month (min) | Tier-1 cities inventory month (max) | Shanghai inventory month (min) |
|---------|--------------------------------------------------|------------------------------------------|-------------------------------------|-------------------------------------|-------------------------------|
| Apr-15  | ~32                                              | ~12                                      | ~20                                 | ~24                                 | ~8                            |
| Oct-15  | ~30                                              | ~10                                      | ~15                      

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 19 May 2026 02:05 AM HKT

Disseminated 19 May 2026 02:05 AM HKT
"""
