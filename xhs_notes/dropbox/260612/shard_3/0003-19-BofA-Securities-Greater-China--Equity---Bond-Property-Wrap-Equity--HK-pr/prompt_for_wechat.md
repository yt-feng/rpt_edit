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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`美国银行`。标题格式建议：`# 美国银行：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份美国银行研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## HK primary residential sales pace slows

HK has recorded \~240 primary residential transactions so far in June, a slowdown versus the 2,000+ monthly average over the past five months, as developers appear to be pacing new launches more cautiously. We attribute the deceleration to a negative wealth effect from recent local equity market weakness, renewed concerns over US rate hikes, and uncertainty stemming from Mainland China's newly announced offshore investment rules; we expect the latter overhang to persist near term until clearer implementation details emerge. — Karl Choi (Equity Research)

## Central govt' financing subsidy to aid urban renewal

At a policy briefing held by the State Council, the Vice Minister stated that RMB 97bn from the central budget and RMB 160bn ultra-long-term special government bonds will be allocated to support local governments' urban renewal in 2026. Compared with the annual urban renewal investment exceeding RMB 3tn, the bulk of funding will be borne by local governments — including through special purpose bonds and policy bank lending. We continue to expect the incremental impact of the latest urban renewal program to be relatively minor. — Karl Choi (Equity Research)

## China HY: yield +18bp to 9.6%; HK IG: sprd -3bp to 61bp

In the past week, the average yield of China HY property bonds (ex. VNKRLE) widened 18bp WoW to 9.58%, which represents 162bp tightening YTD. There was no new issuance in the sector during past week, with YTD net redemption remaining at US\$1.4bn. For sector news, Beijing released implementation guidelines to promote high-quality urban development. Vanke received approval from banks to extend RMB1.184bn loans in total per Debtwire. Separately, United Overseas Bank (UoB) has assumed control of Midtown Manhattan's Bush Tower after Vanke defaulted on a US\$120mn loan per Octus. For HK, the average OAS of HK IG property bonds tightened 3bp WoW to 61bp. We are now OW LASUDE '26 (see report) which can offer an attractive alpha opportunity amid the HK property market recovery. Our OW is driven by (1) still decent upside based on Debtwire-reported LME terms and (2) c.1x interest coverage with gradual deleveraging backed by further asset & property sales. We also acknowledge the company's commitment to addressing its debt issue, reflected by its proactive asset sales. Key things to watch: completion of CCB Tower sale, progress in LME talks & further property/ asset sales. – Sirius Chan (Credit Research)

## 10 June 2026

Cross Asset Research

Greater China

Real Estate/Property

## Credit Research

## Sirius Chan

Research Analyst

BofA (Hong Kong)

+852 3508 3100

sirius.chan@bofa.com

## Joyce Liang

Research Analyst

BofA (Singapore)

joyce.liang@bofa.com

## Xiang Gao, CFA

Research Analyst

BofA (Singapore)

xiang.gao@bofa.com

## Suyang Lu

Research Analyst

BofA (Hong Kong)

suyang.lu@bofa.com

## Equity Research

Karl Choi, CFA >>

Research Analyst

BofA (Hong Kong)

+852 3508 3108

karl.choi@bofa.com

## Fan Tso, CFA >>

Research Analyst

BofA (Hong Kong)

fan.tso@bofa.com

## Eric Du >>

Research Analyst

BofA (Hong Kong)

eric.du@bofa.com

OAS: option adjusted spread

YTD: year-to-date

VNKRLE: China Vanke

NDRC: National Development and Reform Commission

Southbound: Mainland investors who invest in HK-listed stocks through stock connect program

CN: China

CREIS: China Real Estate Index System

See Exhibit 9 and 10 for list of tickers and corresponding issuer names.

## Southbound interest summary

Exhibit 1: Southbound interest summary on property names  
Southbound interest in China developers edged down slightly in May

<table><tr><td>Stock code</td><td>Company name</td><td>10/27/2025</td><td>11/24/2025</td><td>12/31/2025</td><td>1/30/2026</td><td>2/28/2026</td><td>3/31/2026</td><td>4/30/2026</td><td>5/31/2026</td><td>MTD</td><td>Stake % as</td></tr><tr><td colspan="2">China developers</td><td>Stake %</td><td>Stake %</td><td>Stake %</td><td>Stake %</td><td>Stake %</td><td>Stake %</td><td>Stake %</td><td>Stake %</td><td>Chg pts</td><td>% of free float</td></tr><tr><td>817</td><td>China Jinmao</td><td>16.77</td><td>17.04</td><td>17.76</td><td>17.31</td><td>17.76</td><td>18.75</td><td>19.31</td><td>19.02</td><td>(0.29)</td><td>39.47</td></tr><tr><td>119</td><td>Poly Property</td><td>27.37</td><td>27.34</td><td>27.32</td><td>27.35</td><td>26.46</td><td>25.31</td><td>23.07</td><td>20.89</td><td>(2.18)</td><td>40.26</td></tr><tr><td>3900</td><td>Greentown</td><td>28.23</td><td>30.09</td><td>30.48</td><td>30.57</td><td>30.32</td><td>30.95</td><td>31.13</td><td>30.47</td><td>(0.66)</td><td>80.87</td></tr><tr><td>81</td><td>COGO</td><td>14.83</td><td>15.07</td><td>14.50</td><td>15.25</td><td>15.25</td><td>15.65</td><td>16.34</td><td>16.78</td><td>0.44</td><td>38.99</td></tr><tr><td>2202</td><td>China Vanke</td><td>52.21</td><td>55.82</td><td>59.38</td><td>58.07</td><td>57.41</td><td>60.37</td><td>60.68</td><td>60.89</td><td>0.21</td><td>69.47</td></tr><tr><td>1813</td><td>KWG</td><td>6.69</td><td>6.64</td><td>6.55</td><td>6.53</td><td>6.52</td><td>6.50</td><td>6.49</td><td>6.48</td><td>(0.01)</td><td>15.55</td></tr><tr><td>272</td><td>Shui On</td><td>11.75</td><td>11.78</td><td>11.76</td><td>11.81</td><td>11.62</td><td>11.12</td><td>10.95</td><td>10.88</td><td>(0.07)</td><td>25.15</td></tr><tr><td>2777</td><td>Guangzhou R&amp;F</td><td>10.16</td><td>9.80</td><td>9.54</td><td>9.16</td><td>9.01</td><td>8.72</td><td>8.55</td><td>8.38</td><td>(0.17)</td><td>19.19</td></tr><tr><td>1030</td><td>Seazen</td><td>19.83</td><td>19.57</td><td>19.91</td><td>19.40</td><td>20.53</td><td>21.57</td><td>21.94</td><td>22.29</td><td>0.35</td><td>63.89</td></tr><tr><td>410</td><td>SOHO</td><td>14.20</td><td>14.11</td><td>13.95</td><td>13.85</td><td>13.78</td><td>13.62</td><td>13.58</td><td>13.55</td><td>(0.03)</td><td>37.57</td></tr><tr><td>960</td><td>Longfor</td><td>9.51</td><td>9.93</td><td>10.61</td><td>10.89</td><td>10.92</td><td>11.54</td><td>11.76</td><td>11.80</td><td>0.04</td><td>32.99</td></tr><tr><td>3380</td><td>Logan</td><td>7.68</td><td>7.70</td><td>7.43</td><td>7.87</td><td>8.20</td><td>8.46</td><td>8.67</td><td>9.10</td><td>0.43</td><td>36.64</td></tr><tr><td>604</td><td>Shenzhen Investment</td><td>4.04</td><td>3.12</td><td>3.50</td><td>3.54</td><td>3.42</td><td>3.76</td><td>3.69</td><td>3.57</td><td>(0.12)</td><td>13.88</td></tr><tr><td>123</td><td>Yuexiu</td><td>14.15</td><td>13.84</td><td>12.66</td><td>12.66</td><td>13.15</td><td>13.30</td><td>13.57</td><td>14.26</td><td>0.69</td><td>41.07</td></tr><tr><td>3377</td><td>Sino-Ocean</td><td>6.50</td><td>6.35</td><td>6.31</td><td>5.96</td><td>5.92</td><td>5.82</td><td>5.75</td><td>5.36</td><td>(0.39)</td><td>8.92</td></tr><tr><td>688</td><td>COLI</td><td>5.14</td><td>5.47</td><td>5.49</td><td>6.36</td><td>6.75</td><td>6.64</td><td>6.80</td><td>6.90</td><td>0.10</td><td>15.74</td></tr><tr><td>813</td><td>Shimao</td><td>0.96</td><td>0.95</td><td>0.95</td><td>0.81</td><td>0.81</td><td>0.80</td><td>0.76</td><td>0.74</td><td>(0.02)</td><td>1.77</td></tr><tr><td>2007</td><td>Country Garden</td><td>14.43</td><td>14.92</td><td>15.33</td><td>16.76</td><td>17.18</td><td>17.60</td><td>17.77</td><td>18.03</td><td>0.26</td><td>28.67</td></tr><tr><td>1109</td><td>CR Land</td><td>9.78</td><td>10.44</td><td>10.52</td><td>11.03</td><td>11.87</td><td>12.45</td><td>12.51</td><td>12.82</td><td>0.31</td><td>31.70</td></tr><tr><td>3383</td><td>Agile</td><td>7.65</td><td>7.57</td><td>7.41</td><td>7.08</td><td>6.99</td><td>6.91</td><td>6.85</td><td>6.77</td><td>(0.08)</td><td>16.22</td></tr><tr><td>3883</td><td>Aoyuan</td><td>3.72</td><td>3.68</td><td>3.60</td><td>3.59</td><td>3.57</td><td>3.55</td><td>3.48</td><td>3.44</td><td>(0.04)</td><td>4.68</td></tr><tr><td>1966</td><td>China SCE</td><td>6.36</td><td>6.05</td><td>6.01</td><td>5.98</td><td>5.96</td><td>5.92</td><td>5.89</td><td>5.83</td><td>(0.06)</td><td>15.18</td></tr><tr><td>1908</td><td>C&amp;D</td><td>7.19</td><td>7.38</td><td>9.25</td><td>9.88</td><td>12.04</td><td>13.47</td><td>15.40</td><td>15.69</td><td>0.29</td><td>37.27</td></tr><tr><td colspan="2">Average</td><td>13.01</td><td>13.25</td><td>13.49</td><td>13.55</td><td>13.71</td><td>14.03</td><td>14.13</td><td>14.08</td><td>(0.04)</td><td>31.09</td></tr><tr><td colspan="2">HK players</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>17</td><td>New World</td><td>5.55</td><td>5.24</td><td>4.82</td><td>4.65</td><td>4.84</td><td>4.61</td><td>4.52</td><td>4.59</td><td>0.07</td><td>8.44</td></tr><tr><td>683</td><td>Kerry Prop</td><td>5.40</td><td>5.39</td><td>5.25</td><td>5.02</td><td>4.80</td><td>4.68</td><td>4.51</td><td>4.06</td><td>(0.45)</td><td>10.21</td></tr><tr><td>1113</td><td>CKA</td><td>3.33</td><td>3.37</td><td>3.40</td><td>3.35</td><td>3.24</td><td>1.88</td><td>1.67</td><td>1.48</td><td>(0.19)</td><td>3.51</td></tr><tr><td>16</td><td>SHKP</td><td>2.30</td><td>2.57</td><td>2.30</td><td>2.34</td><td>2.40</td><td>2.46</td><td>2.49</td><td>2.38</td><td>(0.11)</td><td>6.66</td></tr><tr><td>41</td><td>Great Eagle</td><td>2.61</td><td>2.61</td><td>2.71</td><td>2.74</td><td>2.68</td><td>2.57</td><td>2.50</td><td>2.45</td><td>(0.05)</td><td>15.33</td></tr><tr><td>101</td><td>Hang Lung Prop</td><td>7.69</td><td>7.92</td><td>7.96</td><td>7.01</td><td>6.44</td><td>5.95</td><td>5.80</td><td>5.75</td><td>(0.05)</td><td>16.08</td></tr><tr><td>4</td><td>Wharf</td><td>0.17</td><td>0.16</td><td>0.16</td><td>0.15</td><td>0.15</td><td>0.15</td><td>0.15</td><td>0.14</td><td>(0.01)</td><td>0.45</td></tr><tr><td>1997</td><td>Wharf REIC</td><td>1.09</td><td>1.11</td><td>1.14</td><td>1.06</td><td>1.08</td><td>1.08</td><td>1.07</td><td>1.02</td><td>(0.05)</td><td>2.10</td></tr><tr><td>12</td><td>Henderson</td><td>1.31</td><td>1.53</td><td>1.78</td><td>1.56</td><td>1.68</td><td>1.75</td><td>1.80</td><td>1.53</td><td>(0.27)</td><td>5.64</td></tr><tr><td>1972</td><td>Swire Prop</td><td>1.89</td><td>1.99</td><td>2.17</td><td>2.01</td><td>1.96</td><td>2.05</td><td>2.13</td><td>2.06</td><td>(0.07)</td><td>12.35</td></tr><tr><td>83</td><td>Sino Land</td><td>1.36</td><td>1.47</td><td>1.48</td><td>1.38</td><td>1.27</td><td>1.31</td><td>1.36</td><td>1.24</td><td>(0.12)</td><td>3.13</td></tr><tr><td>14</td><td>Hysan</td><td>3.04</td><td>3.18</td><td>3.12</td><td>3.12</td><td>2.93</td><td>2.81</td><td>2.82</td><td>2.61</td><td>(0.21)</td><td>4.57</td></tr><tr><td>10</td><td>Hang Lung Group</td><td>1.69</td><td>1.67</td><td>1.67</td><td>1.61</td><td>1.60</td><td>1.59</td><td>1.59</td><td>1.54</td><td>(0.05)</td><td>3.41</td></tr><tr><td>1686</td><td>SUNeVision</td><td>5.15</td><td>5.00</td><td>3.74</td><td>7.24</td><td>6.44</td><td>5.59</td><td>5.00</td><td>4.16</td><td>(0.84)</td><td>16.46</td></tr><tr><td colspan="2">Average</td><td>3.04</td><td>3.09</td><td>2.98</td><td>3.09</td><td>2.97</td><td>2.75</td><td>2.67</td><td>2.50</td><td>(0.17)</td><td>7.74</td></tr><tr><td colspan="2">HK conglo/port/logistics</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>1</td><td>CK Hutchison</td><td>3.13</td><td>3.15</td><td>3.10</td><td>2.73</td><td>2.55</td><td>2.39</td><td>2.34</td><td>2.21</td><td>(0.13)</td><td>3.19</td></tr><tr><td>66</td><td>MTR CORPORATION</td><td>0.44</td><td>1.22</td><td>1.57</td><td>1.83</td><td>2.21</td><td>2.20</td><td>2.20</td><td>2.07</td><td>(0.13)</td><td>8.13</td></tr><tr><td>19</td><td>Swire Pacific</td><td>1.39</td><td>1.65</td><td>1.34</td><td>1.28</td><td>1.39</td><td>1.38</td><td>1.40</td><td>1.35</td><td>(0.05)</td><td>3.13</td></tr></table>

Source: CCASS; BofA Global Research  
BofA GLOBAL RESEARCH

## Greater China property – Equity/bond performance

Exhibit 2: China Property Developers' bond yields vs. share prices The average bond yield widened 18bp WoW to $9.58\%$ , and the share price $-0.9\%$ WoW.  
![](images/cc248b86d5209c6215740b4d747f5b94ad8bc2042b992e276e0ded8942fcca31.jpg)

<details>
<summary>line chart</summary>

| Date   | Developers' shr px (LHS) | Average bond yield (RHS) |
|--------|---------------------------|---------------------------|
| Jun-14 | ~100                      | ~10                       |
| Jun-16 | ~150                      | ~15                       |
| Jun-18 | ~250                      | ~20                       |
| Jun-20 | ~200                      | ~30                       |
| Jun-22 | ~100                      | ~70                       |
| Jun-24 | ~50                       | ~50                       |
| Jun-26 | ~50                       | ~10                       |
</details>

Source: BofA Global Research, Bloomberg, ICE Index. MTD = month to date. Shr px = share price. LHS = left hand side. RHS = right hand side. Note: exclude VNKRLE (Vanke) from bond universe from 31 Dec 2025.  
BofA GLOBAL RESEARCH

Exhibit 3: Hong Kong property issuers' bond spreads vs. share prices The average bond spread (OAS) tightened 3bp WoW to 61bp and the share price -7.2% WoW.  
![](images/e601b50f878fc9fc3d86555c8a3613e33186f19c71e0a17194df62c9565f6995.jpg)

<details>
<summary>line chart</summary>

| Date   | HK Property Share Price (LHS) | Bond OAS (bp) |
|--------|-------------------------------|---------------|
| Jan'12 | 100                           | 150           |
| Jun-26 | -50                           | 50            |
</details>

Source: BofA Global Research, Bloomberg, ICE Index. MTD = month to date. LHS = left hand side. RHS = right hand side  
BofA GLOBAL RESEARCH

Exhibit 4: YTM (%) of benchmark bonds for select Chinese HY property developers The average yield of benchmark bonds widened 10bp WoW on average basis.  
![](images/94a2bcf5399174e0cb207a8d5ec74db030285e281e01a23ca368096c1f992b85.jpg)

<details>
<summary>bar chart</summary>

| Category | Value |
|---|---|
| CHIMAO '29 | 6.8 |
| FUTLAN '28 | 12.5 |
| GRNCH '28 | 7.5 |
| GRNCH '29 | 7.7 |
| LNGFOR '27 | 9.3 |
| LNGFOR '29 | 9.9 |
| LNGFOR '32 | 10.0 |
</details>

Source: Bloomberg, BofA Global Research  
BofA GLOBAL RESEARCH

Exhibit 5: Z-spread (bp) of benchmark bonds for select Hong Kong IG Property issuers The average z-spread of benchmark bonds widened 3bp WoW on average basis.  
![](images/525d10653348e0f87ab6a5ceed58e45d1eb6f04855a20020e1fb5d120545175a.jpg)

<details>
<summary>bar chart</summary>

| Category | Value |
|---|---|
| CKHH '30 | 64 |
| HYSAN '27 | 98 |
| HYSAN '29 | 91 |
| NANFUN '28 | 111 |
| NANFUN '30 | 117 |
| SWIRE '29 | 53 |
| SWIRE '32 | 68 |
| WREICL '28 | 68 |
| WREICL '30 | 84 |
</details>

Source: Bloomberg, BofA Global Research

BofA GLOBAL RESEARCH

Exhibit 6: Top 100 developers contracted sales trend Top-100 developers' contracted sales value (attributable) was down by $36\%$ YoY in Nov.  
![](images/a6ec49b71d13da297c52b7fcbf4283ed61bb2e12eec09f874d1891481c06e881.jpg)

<details>
<summary>bar-line hybrid</summary>

| Month | Top 100 (attributable) (RMB bn) | Top SOEs + Binjiang (RMB bn) | Top 100 (attributable) YoY - RHS (%) | Quality SOEs + Binjiang (YoY) - RHS (%) |
| --- | --- | --- | --- | --- |
| Apr-21 | 820 | 200 | 45 | 0 |
| May-21 | 850 | 210 | 35 | -5 |
| Jun-21 | 900 | 220 | 30 | -10 |
| Jul-21 | 760 | 230 | 25 | -15 |
| Aug-21 | 700 | 240 | 20 | -20 |
| Sep-21 | 710 | 250 | 15 | -25 |
| Oct-21 | 690 | 260 | 10 | -30 |
| Nov-21 | 780 | 270 | 5 | -35 |
| Dec-21 | 400 | 280 | 0 | -40 |
| Jan-22 | 350 | 290 | -5 | -45 |
| Feb-22 | 380 | 300 | -10 | -50 |
| Mar-22 | 360 | 310 | -15 | -55 |
| Apr-22 | 390 | 320 | -20 | -60 |
| May-22 | 410 | 330 | -25 | -65 |
| Jun-22 | 430 | 340 | -30 | -70 |
| Jul-22 | 450 | 350 | -35 | -75 |
| Aug-22 | 470 | 360 | -40 | -80 |
| Sep-22 | 490 | 370 | -45 | -85 |
| Oct-22 | 510 | 380 | -50 | -90 |
| Nov-22 | 530 | 390 | -55 | -95 |
| Dec-22 | 550 | 400 | -60 | -100 |
| Jan-23 | 570 | 410 | -65 | -105 |
| Feb-23 | 590 | 420 | -70 | -110 |
| Mar-23 | 610 | 430 | -75 | -115 |
| Apr-23 | 630 | 440 | -80 | -120 |
| May-23 | 650 | 450 | -85 | -125 |
| Jun-23 | 670 | 460 | -90 | -130 |
| Jul-23 | 690 | 470 | -95 | -135 |
| Aug-23 | 710 | 480 | -100 | -140 |
| Sep-23 | 730 | 490 | -105 | -145 |
| Oct-23 | 750 | 500 | -110 | -150 |
| Nov-23 | 770 | 510 | -115 | -155 |
| Dec-23 | 790 | 520 | -120 | -160 |
| Jan-24 | 810 | 530 | -125 | -165 |
| Feb-24 | 830 | 540 | -130 | -170 |
| Mar-24 | 850 | 550 | -135 | -175 |
| Apr-24 | 870 | 560 | -140 | -180 |
| May-24 | 890 | 570 | -145 | -185 |
| Jun-24 | 910 | 580 | -150 | -190 |
| Jul-24 | 930 | 590 | -155 | -195 |
| Aug-24 | 950 | 600 | -160 | -200 |
| Sep-24 | 970 | 610 | -165 | -205 |
| Oct-24 | 990 | 620 | -170 | -210 |
| Nov-24 | 1010 | 630 | -175 | -215 |
| Dec-24 | 1030 | 640 | -180 | -220 |
</details>

Source: CRIC; BofA Global Research  
Top SOE developers: COLI, CRL, Poly, CMSK, C&D, Yuexiu, Jinmao

BofA GLOBAL RESEARCH

## Exhibit 7: Dictionary for equity tickers

Below are the company names of related equity tickers

Equity tickers

<table><tr><td>16 HK</td><td>Sun Hung Kai Properties (SHKP)</td></tr><tr><td>66 HK</td><td>MTR Corp</td></tr><tr><td>2202 HK</td><td>Vanke</td></tr><tr><td>1686 HK</td><td>SUNeVision</td></tr><tr><td>002244 CH</td><td>Binjiang</td></tr><tr><td>001979 CH</td><td>China Merchants Shekou (CMSK)</td></tr><tr><td>688 HK</td><td>China Overseas Land &amp; Investment (COLI)</td></tr><tr><td>1109 HK</td><td>China Resources Land (CR Land)</td></tr><tr><td>1908 HK</td><td>C&amp;D Int&#x27;l</td></tr><tr><td>817 HK</td><td>Jinmao</td></tr><tr><td>960 HK</td><td>Longfor</td></tr><tr><td>3990 HK</td><td>Midea</td></tr><tr><td>600048 CH</td><td>Poly Real Estate</td></tr><tr><td>1030 HK</td><td>Seazen</td></tr><tr><td>1918 HK</td><td>Sunac</td></tr><tr><td>123 HK</td><td>Yuexiu Property</td></tr></table>

Source: BofA Global Research

Company name

<table><tr><td>Sun Hung Kai Properties (SHKP)</td></tr><tr><td>MTR Corp</td></tr><tr><td>Vanke</td></tr><tr><td>SUNeVision</td></tr><tr><td>Binjiang</td></tr><tr><td>China Merchants Shekou (CMSK)</td></tr><tr><td>China Overseas Land &amp; Investment (COLI)</td></tr><tr><td>China Resources Land (CR Land)</td></tr><tr><td>C&amp;D Int&#x27;l</td></tr><tr><td>Jinmao</td></tr><tr><td>Longfor</td></tr><tr><td>Midea</td></tr><tr><td>Poly Real Estate</td></tr><tr><td>Seazen</td></tr><tr><td>Sunac</td></tr><tr><td>Yuexiu Property</td></tr></table>

BofA GLOBAL RESEARCH

## Exhibit 8: Dictionary for credit tickers mentioned

Credit tickers mentioned in the report.

Credit Ticker

<table><tr><td>CHJMAO</td><td>China Jinmao</td></tr><tr><td>FTLNHD</td><td>New Metro Global Ltd</td></tr><tr><td>FUTLAN</td><td>Seazen Group Ltd<

[中间内容因长度限制已省略]

ions, conclusion, or information contained herein (including any investment recommendations, estimates or price targets) without first obtaining express permission from an authorized officer of BofA.

Materials prepared by BofA Global Research personnel are based on public information. Facts and views presented in this material have not been reviewed by, and may not reflect information known to, professionals in other business areas of BofA, including investment banking personnel. BofA has established information barriers between BofA Global Research and certain business groups. As a result, BofA does not disclose certain client relationships with, or compensation received from, such issuers. To the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
