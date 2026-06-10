你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`摩根斯坦利`。标题格式建议：`# 摩根斯坦利：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份摩根斯坦利研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Accounting & Valuation | North America

# AI Ecosystem: Charting Recent Trends

As hyperscaler capital intensity reaches more than 40% of sales, incremental capex revisions are now accompanied by capital raises and/or innovative financing. Long-term purchase commitments of \~\$1tn and lease commitments >\$800bn further support the AI buildout, but add off-BS operating leverage.

## Key Takeaways

Our analysts forecast capex-to-sales ratios of 36%, 44%, and 42% in 2026–28, well above the 32% dot-com fiber peak. Finance leases push headline numbers higher.  
AI is dominating overall investment, with AI-related spend expected to make up more than 50% of R1000 capex in 2026, of which hyperscalers contribute \~90%.  
Among major AI compute players, RPO has nearly tripled in the last year, reaching >\$2tn as customers commit to longer-duration contracts.  
Depreciation is the next margin watch item, with MSFT, ORCL, META, and GOOGL depreciation is expected to exceed \$520bn over three years.  
See full slide deck inside with our most popular AI charts updated for the latest SEC filings.

2026 EXTEL

ALL-AMERICA

RESEARCH POLL

May 26 – June 12, 2026

We appreciate your support

VOTE HERE

![](images/6e6564e0a7b9871dce551bf05a31807368fc668ef656251a23669d7075628ad6.jpg)

Please refer to the slides below for refreshed versions of our key charts from the past year, reflecting an updated view of the AI ecosystem.

MS & CO. LLC

Todd Castagno, CFA, CPA

GVAT Strategist

Todd.Castagno@morganstanley.com +1 212 761-6893

Kate Konetzke, CFA, CPA

GVAT Strategist

Kate.Konetzke@morganstanley.com +1 212 761-3457

Mariah Thompson

GVAT Strategist

Mariah.Thompson@morganstanley.com +1 212 761-1147

Clinton Chang, CFA, CPA

GVAT Strategist

Clinton.Chang@morganstanley.com +1 212 761-1185

2026 EXTEL

ALL-AMERICA

RESEARCH POLL

May 26 – June 12, 2026

VIEW OUR

ANALYSTS >

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

Exhibit 1: MSe expects Hyperscaler capex/sales to surpass dot-com peaks reaching 44% in '27  
![](images/03ed70e10868858685775093d75deeb6f2d1fff41f0ce5766894d16b8d4bfa6f.jpg)

<details>
<summary>line chart</summary>

| Year | Communication Services | Energy | Information Technology | Hypercapers | Hypercapers Mkt (and Finance Leased) |
|------|--------------------------|--------|------------------------|-------------|-------------------------------------|
| 1980 | ~25%                     | ~15%   | ~10%                   | ~10%        | ~5%                                 |
| 1981 | ~24%                     | ~14%   | ~9%                    | ~9%         | ~5%                                 |
| 1982 | ~23%                     | ~13%   | ~8%                    | ~8%         | ~5%                                 |
| 1983 | ~22%                     | ~12%   | ~7%                    | ~7%         | ~5%                                 |
| 1984 | ~21%                     | ~11%   | ~6%                    | ~6%         | ~5%                                 |
| 1985 | ~20%                     | ~10%   | ~5%                    | ~5%         | ~5%                                 |
| 1986 | ~19%                     | ~9%    | ~4%                    | ~4%         | ~5%                                 |
| 1987 | ~18%                     | ~8%    | ~3%                    | ~3%         | ~5%                                 |
| 1988 | ~17%                     | ~7%    | ~2%                    | ~2%         | ~5%                                 |
| 1989 | ~16%                     | ~6%    | ~1%                    | ~1%         | ~5%                                 |
| 1990 | ~15%                     | ~5%    | ~0.5%                  | ~0.5%       | ~5%                                 |
| 1991 | ~14%                     | ~4%    | ~0.3%                  | ~0.3%       | ~5%                                 |
| 1992 | ~13%                     | ~3%    | ~0.2%                  | ~0.2%       | ~5%                                 |
| 1993 | ~12%                     | ~2%    | ~0.1%                  | ~0.1%       | ~5%                                 |
| 1994 | ~11%                     | ~1%    | ~0.05%                 | ~0.05%      | ~5%                                 |
| 1995 | ~10%                     | ~0.5%  | ~0.03%                 | ~0.03%      | ~5%                                 |
| 1996 | ~9%                      | ~0.3%  | ~0.02%                 | ~0.02%      | ~5%                                 |
| 1997 | ~8%                      | ~0.2%  | ~0.01%                 | ~0.01%      | ~5%                                 |
| 1998 | ~7%                      | ~0.1%  | ~0.005%                | ~0.005%     | ~5%                                 |
| 1999 | ~6%                      | ~0.05% | ~0.003%                | ~0.003%     | ~5%                                 |
| 2000 | ~5%                      | ~0.03% | ~0.002%                | ~0.002%     | ~5%                                 |
| 2001 | ~4.5%                    | ~0.02% | ~0.001%                | ~0.001%     | ~5%                                 |
| 2002 | ~4.0%                    | ~0.01% | ~0.0005%               | ~0.0005%    | ~5%                                 |
| 2003 | ~3.5%                    | ~0.005%| ~0.0003%              | ~0.0003%    | ~5%                                 |
| 2004 | ~3.0%                    | ~0.003%| ~0.0002%              | ~0.0002%    | ~5%                                 |
| 2005 | ~2.5%                    | ~0.002%| ~0.0001%              | ~0.0001%    | ~5%                                 |
| 2006 | ~2.0%                    | ~0.001%| ~0.00005%             | ~0.00005%   | ~5%                                 |
| 2007 | ~1.5%                    | ~-0.001| -                      | -           | -                                   |
| 2008 | ~1.0%                    | -      | -                      | -           | -                                   |
| 2009 | -                        | -      | -                      | -           | -                                   |
| 2010 | -                        | -      | -                      | -           | -                                   |
| 2011 | -                        | -      | -                      | -           | -                                   |
| 2012 | -                        | -      | -                      | -           | -                                   |
| 2013 | -                        | -      | -                      | -           | -                                   |
| 2014 | -                        | -      | -                      | -           | -                                   |
| 2015 | -                        | -      | -                      | -           | -                                   |
| 2016 | -                        | -      | -                      | -           | -                                   |
| 2017 | -                        | -      | -                      | -           | -                                   |
| 2018 | -                        | -      | -                      | -           | -                                   |
| 2019 | -                        | -      | -                      | -           | -                                   |
| 2020a-2021e-27 Julya-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27f
| -                          | -      | -                      | -           |
| Dec-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27d|
| Dec-28e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-27e-<lcel><lcel><lcel><lcel><lcel><nl>
</details>

Note: The hyperscalers group includes AMZN, GOOGL, META, MSFT, & ORCL and are excluded from the other sector groups. Only MSFT and ORCL finance lease estimates are included. R1000 excludes Real Estate and Financials.
Source: MS Estimates and Factset.

Exhibit 2: Cons expects Hyperscaler capex to reach 45% of the R1000 in '27 and '28  
![](images/02e888254fe971969381892eda94e9c0ee018d3ba252a9982f19a0ce72d49b11.jpg)

<details>
<summary>area chart</summary>

| Year | All other Sectors ($100M) | Information Technology | Communication Services | Energy | Hyperparameters |
|------|-----------------------------|--------------------------|-------------------------|--------|---------------|
| 2018 | $100,000                    | $100,000                 | $100,000                | $100,000 | $100,000      |
| 2019 | $150,000                    | $150,000                 | $150,000                | $150,000 | $150,000      |
| 2020 | $200,000                    | $200,000                 | $200,000                | $200,000 | $200,000      |
| 2021 | $300,000                    | $300,000                 | $300,000                | $300,000 | $300,000      |
| 2022 | $450,000                    | $450,000                 | $450,000                | $450,000 | $450,000      |
| 2023 | $650,000                    | $650,000                 | $650,000                | $650,000 | $650,000      |
</details>

Note: The hyperscalers group includes AMZN, GOOGL, META, MSFT, & ORCL and are excluded from the other sector groups. R1000 excludes Real Estate and Financials. Estimates are based on consensus.
Source: FactSet.

Exhibit 3: Leases not yet started have hit  
>\$800bn across Hyperscalers...  
![](images/4e8fd8462ac34296786901b22ae15e6ea26c02355b3cbf9ba81be546283eea0c.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | ORCL | MSFT | META | AMZN | GOOGL |
|------|------|------|------|------|-------|
| 2021 |      |      |      |      |       |
| 2022 |      |      |      |      |       |
| 2023 |      |      |      |      |       |
| 2024 |      |      |      |      |       |
| 2025 |      |      |      |      |       |
| 1Q26* | $261bn | $197bn | $183bn | $106bn | $76bn |
</details>

Note: Based on fiscal years. ORCL and MSFT 1Q26 = 3FQ26.
MSFT is covered by Josh Baer. ORCL is covered by Sanjit Singh. GOOGL, META, and AMZN are covered by Brian Nowak.
Source: Company filings and MS.

Exhibit 4: ...while purchase commitments reach close to \$1tn  
![](images/d9bc8c6fcd047bb1cebab95770013a1ee451169e2faf8ede3dd054cbaf1079df.jpg)

<details>
<summary>stacked bar chart</summary>

| Year | GOOGL | MSFT | META | AMZN | NVDA | ORCL |
| --- | --- | --- | --- | --- | --- | --- |
| 2021 |  |  |  |  |  |  |
| 2022 |  |  |  |  |  |  |
| 2023 |  |  |  |  |  |  |
| 2024 |  |  |  |  |  |  |
| 2025 | $332bn | $142bn | $238bn | $104bn | $155bn | $91bn |
| 1Q26* |  |  |  |  |  | $982bn |
</details>

Note: Based on fiscal years. ORCL and MSFT 1Q26 = 3FQ26.
MSFT is covered by Josh Baer. ORCL is covered by Sanjit Singh.
GOOGL, META, and AMZN are covered by Brian Nowak.
Source: Company filings and MS.

Exhibit 5: AI ecosystem has become increasingly interconnected....  
![](images/31dacf2affdb2f385088702fcf958e60d0cee853c6666bdf7c576aaf747c4fce.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  A["OpenAI"] -->|10.04 bp| B["Oracle"]
  A -->|261.2 bp| C["Microsoft"]
  A -->|51.2 bp| D["Corewave"]
  A -->|10.04 bp| E["Amazon"]
  A -->|100 bp| F["AMD"]
  A -->|100 bp| G["Disney"]
  A -->|100 bp| H["Nvidia"]
  A -->|100 bp| I["Data Center Lease"]
  A -->|100 bp| J["Repurchase Agreement"]
  A -->|100 bp| K["Vendor Financing/Favorable Terms"]
  A -->|100 bp| L["Customer"]
  A -->|100 bp| M["Revenue Share"]
  A -->|100 bp| N["Investor"]
  A -->|100 bp| O["Subscription"]
  A -->|100 bp| P["Subscription"]
  A -->|100 bp| Q["Subscription"]
  A -->|100 bp| R["Subscription"]
  A -->|100 bp| S["Subscription"]
  A -->|100 bp| T["Subscription"]
  A -->|100 bp| U["Subscription"]
  A -->|100 bp| V["Subscription"]
  A -->|100 bp| W["Subscription"]
  A -->|100 bp| X["Subscription"]
  A -->|100 bp| Y["Subscription"]
  A -->|100 bp| Z["Subscription"]
  A -->|100 bp| AA["Subscription"]
  A -->|100 bp| AB["Subscription"]
  A -->|100 bp| AC["Subscription"]
  A -->|100 bp| AD["Subscription"]
  A -->|100 bp| AE["Subscription"]
  A -->|100 bp| AF["Subscription"]
  A -->|100 bp| AG["Subscription"]
  A -->|100 bp| AH["Subscription"]
  A -->|100 bp| AI["Subscription"]
  A -->|100 bp| AJ["Subscription"]
  A -->|100 bp| AK["Subscription"]
  A -->|100 bp| AL["Subscription"]
  A -->|100 bp| AM["Subscription"]
  A -->|100 bp| AN["Subscription"]
  A -->|100 bp| AO["Subscription"]
  A -->|100 bp| AP["Subscription"]
  A -->|100 bp| AQ["Subscription"]
  A -->|100 bp| AR["Subscription"]
  A -->|100 bp| AS["Subscription"]
  A -->|100 bp| AT["Subscription"]
  A -->|100 bp| AU["Subscription"]
  A -->|100 bp| AV["Subscription"]
  A -->|100 bp| AW["Subscription"]
  A -->|100 bp| AX["Subscription"]
  A -->|100 bp| AY["Subscription"]
  A -->|100 bp| AZ["Subscription"]
  A -->|100 bp| BA["Subscription"]
  A -->|100 bp| BB["Subscription"]
  A -->|100 bp| BC["Subscription"]
  A -->|100 bp| BD["Subscription"]
  A -->|100 bp| BE["Subscription"]
  A -->|100 bp| BF["Subscription"]
  A -->|100 bp| BG["Subscription"]
  A -->|100 bp| BH["Subscription"]
  A -->|100 bp| BI["Subscription"]
  A -->|100 bp| BJ["Subscription"]
  A -->|100 bp| BK["Subscription"]
  A -->|100 bp| BL["Subscription"]
  A -->|100 bp| BM["Subscription"]
  A -->|100 bp| BN["Subscription"]
  A -->|100 bp| BO["Subscription"]
  A -->|100 bp| BP["Subscription"]
  A -->|100 bp| BQ["Subscription"]
  A -->|100 bp| BR["Subscription"]
  A -->|100 bp| BS["Subscription"]
  A -->|100 bp| BT["Subscription"]
  A -->|100 bp| BU["Subscription"]
  A -->|100 bp| BV["Subscription"]
  A -->|100 bp| BW["Subscription"]
  A -->|100 bp| BX["Subscription"]
  A -->|100 bp| BY["Subscription"]
  A -->|100 bp| BZ["Subscription"]
  A -->|100 bp| CA["Subscription"]
  A -->|100 bp| CB["Subscription"]
  A -->|100 bp| CC["Subscription"]
  A -->|100 bp| CD["Subscription"]
  A -->|100 bp| CE["Subscription"]
  A -->|100 bp| CF["Subscription"]
  A -->|100 bp| CG["Subscription"]
  A -->|100 bp| CH["Subscription"]
  A -->|100 bp| CI["Subscription"]
  A -->|100 bp| CJ["Subscription"]
  A -->|100 bp| CK["Subscription"]
  A -->|100 bp| CL["Subscription"]
  A -->|100 bp| CM["Subscription"]
  A -->|100 bp| CN["Subscription"]
  A -->|100 bp| CO["Subscription"]
  A -->|100 bp| CP["Subscription"]
  A -->|100 bp| CZ["Subscription"]
  A -->|100 bp| DA["Subscription"]
  A -->|100 bp| DB["Subscription"]
  A -->|100 bp| DC["Subscription"]
  A -->|100 bp| ED["Subscription"]
  A -->|100 bp| EF["Subscription"]
  A -->|100 bp| GF["Subscription"]
  A -->|100 bp| DG["Subscription"]
  A -->|100 bp| DH["Subscription"]
  A -->|100 bp| DI["Subscription"]
  A -->|100 bp| DJ["Subscription"]
  A -->|100 bp| DK["Subscription"]
```
</details>

Note: MSFT, and CRWV are covered by Josh Baer. ORCL is covered by Sanjit Singh. NVDA and AMD are covered by Joseph Moore. AMZN is covered by Brian Nowak. DIS is covered by Sean Diffley. Data as of 3/19/26.
Source: Company Data, MS.

Exhibit 6: .... creating customer concentration within the >\$2tn of RPO reported by major AI players  
![](images/dfc99a80d8c68505adb2d3239f45ace6ff5902d6fb5f0ed5b999f1c9ebed7a26.jpg)

<details>
<summary>stacked bar chart</summary>

| Quarter | MIST   | ORCL   | AMZN   | GODGL  | CRWV   |
|---------|--------|--------|--------|--------|--------|
| FQ-8    | $568bn |        |        |        |        |
| FQ-7    | $624bn |        |        |        |        |
| FQ-6    | $632bn |        |        |        |        |
| FQ-5    | $667bn |        |        |        |        |
| FQ-4    | $748bn |        |        |        |        |
| FQ-3    | $831bn |        |        |        |        |
| FQ-2    | $1,241bn |        |        |        |        |
| FQ-1    | $1,702bn |        |        |        |        |
| FQ0     | $2,116bn |        |        |        |        |
</details>

Note: GOOGL, META, and AMZN are covered by Brian Nowak. CRWV, and MSFT are covered by Josh Baer. ORCL is covered by Sanjit Singh.
Source: Company Filings, MS.

## MS

June 2026

Global Valuation, Accounting & Tax

## AI Ecosystem

## We are entering a record-setting capital cycle

Hyperscalers are pouring billions into the AI build-out, with finance lease usage pushing capital intensity even higher, well past the dot-com record. Capex estimates continue to revise higher, while sales revisions lag.

## As investment grows, depreciation is set to rise

A sizable increase to depreciation expense could pressure margins if non-depreciation costs don't decline or if sales don't revise higher. But before these investments become expenses, much of the capital will sit in Construction in Progress (CIP), thus delaying earnings and margin impact.

## Billions in lease and purchase commitments are fueling the AI buildout

Hyperscalers are securing capacity amid surging demand through leases and purchase commitments, creating a timing gap between monetization and supplier payment, leading to a rise in DPO among hyperscalers.

## MS North America

MS & Co. LLC

## Todd Castagno, CFA, CPA

GVAT Strategist

(212) 761-6893

Todd.Castagno@morganstanley.com

## Kate Konetzke, CFA, CPA

GVAT Strategist

(212) 761-3457

Kate.Konetzke@morganstanley.com

## Mariah Thompson

GVAT Strategist

(212) 761-1147

Mariah.Thompson@morganstanley.com

## Clinton Chang, CFA, CPA

GVAT Strategist

(212) 761-1185

Clinton.Chang@morganstanley.com

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

## MS

June 2026

FOUNDATION

GVAT

AI Ecosystem Capital Flows  
![](images/07a265017bda9346675ca54468de1a046f2a8cd0986d608da75579885640c04f.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
  Disney -->|TBD26| OpenAI
  OpenAI -->|TBD16| 

[中间内容因长度限制已省略]

ardas, Tel. No.: +91-22-61181000 or Email: tejarshi.hardas@morganstanley.com; Grievance officer details: Mr. Tejarshi Hardas, Tel. No.: +91-22-61181000 or Email: msic-compliance@morganstanley.com. MS India Company Private Limited (MSICPL) may use AI tools in providing research services. All recommendations contained herein are made by the duly qualified research analysts; in Canada by MS Canada Limited; in Germany and the European Economic Area where required by MS Europe S.E., authorised and regulated by Bundesanstalt fuer Finanzdienstleistungsaufsicht (BaFin) under the reference number 149169; in the US by MS & Co. LLC, which accepts responsibility for its contents. MS & Co. International plc, authorized by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority, disseminates in the UK research that it has prepared, and research which has been prepared by any of its affiliates, only to persons who (i) are investment professionals falling within Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the "Order"); (ii) are persons who are high net worth entities falling within Article 49(2)(a) to (d) of the Order; or (iii) are persons to whom an invitation or inducement to engage in investment activity (within the meaning of section 21 of the Financial Services and Markets Act 2000, as amended) may otherwise lawfully be communicated or caused to be communicated. RMB MS Proprietary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products. MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

The following authors are neither Equity Research Analysts/Strategists nor Fixed Income Research Analysts/Strategists and are not opining on or expressing recommendations on equity or fixed income securities: Todd Castagno, CFA, CPA; Clinton Chang, CFA, CPA.

© 2026 MS
"""
