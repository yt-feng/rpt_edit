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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`GS`。标题格式建议：`# GS：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份GS研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## OIL ANALYST

# Reducing Our Price Forecast on Deal to Reopen Hormuz

- Reducing price forecast. We reduce our oil price forecast following President Trump's announcement of an interim deal that would lift the US blockade, and reopen the Strait of Hormuz after a scheduled deal signing on Friday (Exhibit 1. While full details on the agreement are unclear, we now assume that Persian Gulf exports normalize to pre-war levels by the end of July (vs. end of August previously). We are reducing our 2026Q4 Brent forecast to \$80 (vs. \$90 previously) and to \$75 (vs. \$80 prior) for the 2027 average (Exhibit 1, consistent with our estimate that moving the supply normalization process one month forward reduces the fair value of crude prices for 2026Q4/2027 by around \$10/\$5, respectively. We now expect WTI to average \$75 in 2026Q4 and \$70 in 2027.

Risks around Mideast supply. The risks around our assumption that exports/production from the Persian Gulf recover to their pre-war levels by end-July and October (Exhibit 2), respectively, are two-sided. $^{1}$

☐ The supply recovery might be stronger because:

This normalization in oil exports from Gulf producers to their pre-war level might be achieved with a 12mb/d increase in Hormuz flows from current levels to just 70% of pre-war levels (Exhibit 3). We estimate that Gulf flows have already risen to 11mb/d with increases in both Hormuz flows and redirections (Exhibit 4).  
- Producers such as Saudi Arabia and the UAE might respond more strongly to low OECD commercial stocks (Exhibit 12) this summer with even larger production increases than our above pre-war levels base case.  
- Iran production might rise above pre-war levels on potential sanctions relief (Exhibit 5).

☐ The supply recovery might be weaker because:

\- A potential resumption in regional hostilities/strikes on ships might keep shippers risk-averse, and keep exports and production at low

## Daan Struyven

+1(212)357-4172

daan.struyven@gs.com

GS & Co. LLC

## Yulia Zhestkova Grigsby

+1(646)446-3905

yulia.grigsby@gs.com

GS & Co. LLC

## Alexandra Paulus

+1(212)902-7111

alexandra.paulus@gs.com

GS & Co. LLC

## Filippo Cuscito

+44(20)7051-9073

filippo.cuscito@gs.com

GS International

levels for longer.

- Clearing any potential mines might require significant time (although alternative routes can be used in the meantime).  
- Iran might effectively close the Strait again even after re-opening, for instance if detailed nuclear talks don’t succeed.

■ Resilient 2027 prices vs. large surplus. We now also forecast a somewhat firmer demand recovery (Exhibit 6) in 2026H2-2027 on improved affordability. We forecast resilient 2027 Brent/WTI prices in line with our long-term fair values of \$75/70 despite a large 3.2mb/d 2027 surplus because:

☐ OECD commercial oil stocks are unlikely to reach very high levels following large 2026H1 draws and a structural trend of global strategic stockpiling of over 1mb/d in 2027 (Exhibit 7).

☐ Some security premium compensating for disruption risk is likely to keep a floor under prices.

\- That said, managing the sharpest oil production shock ever of 14mb/d with a smaller-than-expected 5mb/d deficit in Q2 (Exhibit 8) on remarkable flexibility (especially from China demand) and without sustained extreme prices is also likely to cap this security premium (assuming Mideast exports recover fast).

■ Two-sided but still net upside price risks.

☐ Price upside scenario: Brent might rise above \$130 in late 2026 and average \$105 in 2027 (Exhibit 9) assuming Hormuz remains disrupted through 2027 with Gulf countries' exports rising gradually by 10mb/d by Dec27 (with some expansion in allowed Hormuz flows and/or pipeline capacity). $^{2}$

☐ Price downside scenario: Brent might average just under \$70 in 2026Q4 and just under \$60 in 2027 assuming exports normalize by early July, stickier demand losses, and stronger supply. $^{3}$

We See Risks to Our Brent Price Forecast as Two-Sided but Tilted to the Upside on Net  
![](images/565fb557bf02409861ff0967a0f0f1bf0457533fb7268e6f9a9058e9c8a4757c.jpg)

<details>
<summary>line chart</summary>

| Date   | Price Upside ($/bbl) | Base Case ($/bbl) | Price Downside ($/bbl) | Forwards ($/bbl) |
|--------|----------------------|--------------------|-------------------------|-------------------|
| Jan-26 | -                    | -                  | 65                      | -                 |
| Apr-26 | -                    | -                  | 100                     | -                 |
| Jul-26 | 105                  | 85                 | 80                      | 80                |
| Oct-26 | 125                  | 80                 | 70                      | 75                |
| Jan-27 | 135                  | 78                 | 65                      | 75                |
| Apr-27 | 120                  | 75                 | 60                      | 75                |
| Jul-27 | 100                  | 73                 | 55                      | 75                |
| Oct-27 | 85                   | 70                 | 53                      | 75                |
| Jan-28 | 80                   | 68                 | 52                      | 75                |
</details>

Source: GS Global Investment Research

## Reducing Our Price Forecast on Deal to Reopen Hormuz

Exhibit 1: We Are Reducing Our 2026Q4 Brent Forecast to \$80 and to \$75 for the 2027 Average as We Now Assume an Earlier Recovery in Mideast Supply Following a Deal to Reopen Hormuz  
![](images/d83ef47a248fc72a21067cb9d96ec680c19d3799fefebbde3030c0adda5dd170.jpg)

<details>
<summary>line chart</summary>

| Month   | GS Forecast (Old) | Forwards | GS Forecast (New) | Realized |
|---------|-------------------|----------|-------------------|----------|
| May     | ~95               | ~85      | ~90               | ~78      |
| Sep     | ~90               | ~80      | ~85               | ~68      |
| 2026    | ~85               | ~75      | ~80               | ~62      |
| May     | ~105              | ~85      | ~95               | ~105     |
| Sep     | ~95               | ~80      | ~85               | ~90      |
| 2027    | ~90               | ~75      | ~80               | ~85      |
| May     | ~85               | ~75      | ~75               | ~80      |
| Sep     | ~80               | ~75      | ~70               | ~75      |
| 2028    | ~75               | ~75      | ~70               | ~75      |
</details>

Source: ICE, GS Global Investment Research

## Assuming an Earlier Normalization of Gulf Exports by End of July

Exhibit 2: We Now Assume That Oil Exports/Production from Persian Gulf Countries Recovers by End of July/October, Respectively  
![](images/5a491d831cc00f440a37e6125b88a246551d8dfddeed821e7de2cd812c711293.jpg)

<details>
<summary>line chart</summary>

| Year | New (mb/d) | Previous (mb/d) |
|------|------------|-----------------|
| 2025 | 30.0       | 30.0            |
| May  | 31.0       | 31.5            |
| Sep  | 31.5       | 32.0            |
| 2026 | 31.5       | 32.0            |
| May  | 17.0       | 17.5            |
| Sep  | 31.5       | 32.0            |
| 2027 | 32.0       | 32.5            |
| May  | 32.0       | 32.5            |
| Sep  | 32.0       | 32.5            |
| 2028 | 32.0       | 32.5            |
</details>

Included countries: Iran, Iraq, Kuwait, Qatar, Saudi Arabia, United Arab Emirates. Liquids include crude oil and natural gas liquids (NGLs).  
Source: OPEC Secondary Sources, GS Global Investment Research

## Two-Sided Risks to the Mideast Supply Recovery

Exhibit 3: This Normalization in Oil Exports From Gulf Producers to Their Pre-War Level May Be Achieved With a 12mb/d Increase in Hormuz Flows From Current Levels  
![](images/fe9ee3fbbe3542b8188726e80ca2e306dab3faa65a3e5c173dd4c504a7d6de58.jpg)

<details>
<summary>bar chart</summary>

Estimating Early June Hit to Oil Flows from Persian Gulf Countries
| Flow | Pre-War (mb/d) | Flows Over Last 14 Days (mb/d) |
| :--- | :--- | :--- |
| Strait of Hormuz | 20.0 | -1.8 |
| Yanbu | 1.4 | -5.2 |
| Fujairah | 1.7 | -2.4 |
| Botas Ceyhan | 0.0 | -1.4 |
| Total | 23.1 | -0.1 |
| Net Hit | | 12.2 |
</details>

Yanbu is on the west coast of Saudi Arabia, bordering the Red Sea and connected to Saudi eastern oil fields via the East-West pipeline. Fujairah lies east (outside) of the Strait of Hormuz and is connected to Abu Dhabi's onshore fields via the Abu Dhabi Crude Oil Pipeline (ADCOP). The Gulf of Oman connects the Strait to the Arabian Sea (southeast). The Kirkuk-Ceyhan pipeline allows northern Iraqi crude to be pumped through Turkey to the Mediterranean sea.

Source: Kpler, S&P Global Commodities at Sea, GS Global Investment Research

Exhibit 4: Estimated Oil Flows From Persian Gulf Countries Have Trended Up From Less Than 30% of Normal Levels in Early March to Nearly 50% of Normal in Mid-June  
![](images/f8bd9ef786f384cd0e1e741036bb530fc52359badbc2cae46ab6858ad0e82e99.jpg)

<details>
<summary>line chart</summary>

| Date       | Estimated Oil Flows (mb/d) | Percent of Normal |
| ---------- | --------------------------- | ----------------- |
| 2026-Jun   | ~11                         | ~50               |
</details>

Yanbu is on the west coast of Saudi Arabia, bordering the Red Sea and connected to Saudi eastern oil fields via the East-West pipeline. Fujairah lies east (outside) of the Strait of Hormuz and is connected to Abu Dhabi's onshore fields via the Abu Dhabi Crude Oil Pipeline (ADCOP). The Gulf of Oman connects the Strait to the Arabian Sea (southeast). The Kirkuk-Ceyhan pipeline allows northern Iraqi crude to be pumped through Turkey to the Mediterranean sea.

Source: Kpler, S&P Global Commodities at Sea, GS Global Investment Research

Exhibit 5: Potential Sanctions Relief May Raise Iran Production Above Pre-War Levels and Reduce Oil on Water, Which Remains High at Nearly 120mb  
![](images/d30c75ad02666d7aa37ca2e8bedcdd9165c02e5875d4cc521be116a4a07c4ac4.jpg)

<details>
<summary>line chart</summary>

| Year | GS Forecast (m/d) | Realized (m/d) |
|------|------------------|----------------|
| 2012 | ~3.7             | ~3.7           |
| 2014 | ~2.7             | ~2.7           |
| 2016 | ~2.9             | ~2.9           |
| 2018 | ~4.0             | ~4.0           |
| 2020 | ~1.9             | ~1.9           |
| 2022 | ~2.8             | ~2.8           |
| 2024 | ~3.5             | ~3.5           |
| 2026 | ~3.5             | ~3.5           |
| 2028 | ~3.5             | ~3.5           |
</details>

![](images/2f0d0530f13734fafb4c8657c8d570b22cd91124e3519035c6143e496035683d.jpg)

<details>
<summary>area chart</summary>

| Year | Floating Storage (mb) | Oil in Transit (mb) |
|------|------------------------|---------------------|
| 2017 | ~80                    | ~60                 |
| 2018 | ~50                    | ~40                 |
| 2019 | ~30                    | ~20                 |
| 2020 | ~20                    | ~15                 |
| 2021 | ~30                    | ~25                 |
| 2022 | ~40                    | ~35                 |
| 2023 | ~60                    | ~50                 |
| 2024 | ~80                    | ~65                 |
| 2025 | ~100                   | ~80                 |
| 2026 | ~160                   | ~130                |
| 2027 | ~140                   | ~110                |
</details>

Source: Kpler, IEA, GS Global Investment Research

## A Large 2027 Surplus

Exhibit 6: Global Oil Demand Tends to Recover Swiftly Following Oil Supply Shocks But Remain Weak Following Recessions  
![](images/59eb020f8e249a663620da10a1e45ae63e56f6e62328c16b268390c9b2053568.jpg)

<details>
<summary>line chart</summary>

| Months Passed Since the Shock | 2022 (Russia-Ukraine War) | 2011 (Libya Civil War) | 2026 (Iran War) | 2008 (Global Financial Crisis) |
| ----------------------------- | -------------------------- | ----------------------- | --------------- | ------------------------------- |
| -4                            | -1.5                       | -0.5                    | 0.8             | -1.0                            |
| -2                            | 0.5                        | 0.2                     | 0.5             | -0.5                            |
| 0                             | 0.0                        | 0.0                     | 0.5             | 0.5                             |
| 2                             | -0.5                       | -1.0                    | -1.5            | -0.5                            |
| 4                             | -1.5                       | -2.0                    | -4.5            | -1.0                            |
| 6                             | 0.8                        | 0.0                     | 0.5             | -1.5                            |
| 8                             | 1.2                        | 0.5                     | 0.5             | -2.0                            |
| 10                            | 1.0                        | 0.8                     | 0.5             | -2.5                            |
| 12                            | 0.5                        | 0.5                     | 0.5             | -3.0                            |
</details>

Source: IEA, GS Global Investment Research

Exhibit 7: We Assume a Structural Trend of Global Strategic Stockpiling of Over 1mb/d in 2027  
![](images/98769118ed474f274396b951c4e3104dcfa3bd010e0e9de1a5605045111d16a6.jpg)

<details>
<summary>bar chart</summary>

| Category                  | Value (mb/d) |
| ------------------------- | ------------ |
| US SPR                    | 0.1          |
| OECD ex US SPR            | 0.2          |
| China Crude Stocks        | 0.5          |
| Non OECD ex China Crude Stocks | 0.2          |
| Total                     | 1.1          |
</details>

Includes visible and invisible stockpiling. OECD ex US SPR contains both crude and refined products. Structural trend is expected to continue through Sep 2028.  
Source: GS Global Investment Research

Exhibit 8: We Estimate a 5mb/d Q2 Deficit, Which is Smaller Than the 14mb/d Hit to Mideast Liquids Production  
![](images/cbbe34edab0e4a9984e035a777c792b6be3dbb8f93995f22f0c77db580f62194.jpg)

<details>
<summary>bar chart</summary>

| Category | Value (mb/d) |
| --- | --- |
| Mideast Supply Downgrade Since War | 13.9 |
| Surplus, Forecast as of Feb 22 | -2.9 |
| Global ex Mideast Supply Upgrade Since War | -1.4 |
| Global Demand Downgrade Since War | -4.7 |
| Q2 Deficit | 5.0 |
</details>

Source: GS Global Investment Research

## Two Sided Risks But Still Net Upside

Exhibit 9: We See Risks to Our Brent Price Forecast as Two-Sided but Tilted to the Upside on Net  
![](images/29833a65f9784fe3287ccc32a0af7969f74b250a2066f84b965c229ba8642dc7.jpg)

<details>
<summary>line chart</summary>

| Date   | Price Upside ($/bbl) | Base Case ($/bbl) | Price Downside ($/bbl) | Forwards ($/bbl) |
|--------|----------------------|--------------------|-------------------------|-------------------|
| Jan-26 | -                    | -                  | 65                      | -                 |
| Apr-26 | -                    | -                  | 100                     | -                 |
| Jul-26 | 105                  | 85                 | 80                      | 80                |
| Oct-26 | 125                  | 80                 | 70                      | 75                |
| Jan-27 | 135                  | 75                 | 65                      | 75                |
| Apr-27 | 120                  | 70                 | 60                      | 75                |
| Jul-27 | 100                  | 65                 | 55                      | 75                |
| Oct-27 | 85                   | 60                 | 55                      | 75                |
| Jan-28 | 80                   | 55                 | 55                      | 75                |
</details>

Source: GS Global Investment Research

## Appendix

Exhibit 10: We Reduce Our 2026Q4 Brent Forecast to \$80 (vs. \$90 Prior) and Our 2027 Average Forecast to \$75 (vs. \$80 Prior)

<table><tr><td rowspan="2"></td><td colspan="3">Brent ($/bbl)</td><td colspan="3">WTI ($/bbl)</td></tr><tr><td>New GS Forecast</td><td>Old GS Forecast</td><td>Forwards (Nearby Contract Traded That Month)</td><td>New GS Forecast</td><td>Old GS Forecast</td><td>Forwards (Nearby Contract Traded That Month)</td></tr><tr><td>2025</td><td>68</td><td>68</td><td></td><td>65</td><td>65</td><td></td></tr><tr><td>2026</td><td>85</td><td>90</td><td>83</td><td>80</td><td>85</td><td>78</td></tr><tr><td>2027</td><td>75</td><td>80</td><td>75</td><td>70</td><td>75</td><td>71</td></tr><tr><td>2028</td><td>71</td><td>75</td><td>74</td><td>66</td><td>70</td><td>69</td></tr><tr><td>2029</td><td>74</td><td>75</td><td>72</td><td>69</td><td>70</td><td>67</td></tr><tr><td>2030</td><td>75</td><td>75</td><td>71</td><td>70</td><td>70</td><td>66</td></tr><tr><td>2031-2035</td><td>75</td><td>75</td><td>68</td><td>70</td><td>70</td><td>61</td></tr><tr><td>1Q25</td><td>75</td><td>75</td><td>75</td><td>71</td><td>71</td><td>71</td></tr><tr><td>2Q25</td><td>67</td><td>67</td><td>67</td><td>64</td><td>64</td><td>64</td></tr><tr><td>3Q25</td><td>68</td><td>68</td><td>68</td><td>65</td><td>65</td><td>65</td></tr><tr><td>4Q25</td><td>63</td><td>63</td><td>63</td><td>59</td><td>59</td><td>59</td></tr><tr><td>1Q26</td><td>78</td><td>78</td><td>76</td><td>72</td><td>72</td><td>72</td></tr><tr><td>2Q26</td><td>98</td><td>100</td><td>96</td><td>93</td><td>95</td><td>92</td></tr><tr><td>3Q26</td><td>84</td><td>94</td><td>80</td><td>79</td><td>88</td><td>76</td></tr><tr><td>4Q26</td><td>80</td><td>90</td><td>78</td><td>75</td><td>85</td><td>74</td></tr><tr><td>1Q27</td><td>78</td><td>86</td><td>77</td><td>74</td><td>81</td><td>72</td></tr><tr><td>2Q27</td><td>76</td><td>82</td><td>76</td><td>71</td><td>77</td><td>71</td></tr><tr><td>3Q27</td><td>73</td><td>78</td><td>75</td><td>69</td><td>73</td><td>71</td></tr><tr><td>4Q27</td><td>71</td><td>75</td><td>74</td><td>66</td><td>70</td><td>70</td></tr><tr><td>Jan-26</td><td>65</td><td>65</td><td></td><td>60</td><td>60</td><td></td></tr><tr><td>Feb-26</td><td>69</td><td>69</td><td></td><td>65</td><td>65</td><td></td></tr><tr><td>Mar-26</td><td>100</td><td>100</td><td></td><td>91</td><td>91</td><td></td></tr><tr><td>Apr-26</td><td>102</td><td>102</td><td></td><td>98</td><td>98</td><td></td></tr><tr><td>May-26</td><td>

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be

supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
