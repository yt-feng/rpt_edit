You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Leave several meaningful open questions that make readers want the full report.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Natural hooks: if you want readers to join the community or read the full report, the hook should emerge from unresolved analytical questions, not from promotional language.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should identify what the report does not fully answer yet.
- One section should translate the report into a decision framework for readers.
- Final section: naturally invite readers to join the community or read the full report using this CTA: Join the community to read the full report and review the original charts.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# Hong Kong Residential Property Chartbook All the charts you need

Hong Kong Property
Karl Chan $^{AC}$ (852) 2800-8513
karl.chan@JPM.com
JPM Securities (Asia Pacific) Limited/
JPM Broking (Hong Kong) Limited

Venus Choi
(852) 2800-8599
venus.choi@JPM.com
JPM Securities (Asia Pacific) Limited/
JPM Broking (Hong Kong) Limited

Jocelyn Gao
(852) 2800-8529
jocelyn.gao@JPM.com
JPM Securities (Asia Pacific) Limited/
JPM Broking (Hong Kong) Limited

See the end pages of this presentation for important disclosures.

Housing Market – Where we are

## Home price trend (long term)

![](images/8c39a592163d86c9d3c4c70bbf5c408bb7f1acb3358e7c7abc328e85beb419f0.jpg)

## House price trend (past 2 years)

Hong Kong secondary home price index (2024 to 2026 YTD)

![](images/b373f2626eced1512db146d85750bcba820c161bb879eefe42be1b9c471ad2d1.jpg)

## Four stages of real estate cycle since 1994

Hong Kong secondary home price (since 1994)

![](images/91920614be7370dc6359e32b8c2a2f1e3a24b29d793869e5309e35ae09bc334d.jpg)

## Four stages of real estate cycle since 1994

Four stages of real estate cycle (duration and home price change)

<table><tr><td>Start</td><td>End</td><td>Stage</td><td>Duration(Weeks)</td><td>Home Price Chg</td></tr><tr><td>3-Apr-94</td><td>15-Oct-95</td><td>Recession</td><td>80</td><td>-30%</td></tr><tr><td>15-Oct-95</td><td>28-Jan-96</td><td>Early-stage Recovery</td><td>15</td><td>13%</td></tr><tr><td>28-Jan-96</td><td>25-May-97</td><td>Expansion</td><td>69</td><td>65%</td></tr><tr><td>25-May-97</td><td>19-Oct-97</td><td>Plateau</td><td>21</td><td>6%</td></tr><tr><td>19-Oct-97</td><td>24-Aug-03</td><td>Recession</td><td>305</td><td>-69%</td></tr><tr><td>24-Aug-03</td><td>9-Nov-03</td><td>Early-stage Recovery</td><td>11</td><td>13%</td></tr><tr><td>9-Nov-03</td><td>17-Feb-08</td><td>Expansion</td><td>223</td><td>105%</td></tr><tr><td>17-Feb-08</td><td>3-Aug-08</td><td>Plateau</td><td>24</td><td>-4%</td></tr><tr><td>3-Aug-08</td><td>30-Nov-08</td><td>Recession</td><td>17</td><td>-20%</td></tr><tr><td>30-Nov-08</td><td>3-May-09</td><td>Early-stage Recovery</td><td>22</td><td>11%</td></tr><tr><td>3-May-09</td><td>30-Aug-15</td><td>Expansion</td><td>330</td><td>133%</td></tr><tr><td>30-Aug-15</td><td>13-Mar-16</td><td>Recession</td><td>28</td><td>-13%</td></tr><tr><td>13-Mar-16</td><td>2-Oct-16</td><td>Early-stage Recovery</td><td>29</td><td>11%</td></tr><tr><td>2-Oct-16</td><td>5-Aug-18</td><td>Expansion</td><td>96</td><td>34%</td></tr><tr><td>5-Aug-18</td><td>8-Aug-21</td><td>Plateau</td><td>157</td><td>2%</td></tr><tr><td>8-Aug-21</td><td>16-Mar-25</td><td>Recession</td><td>188</td><td>-30%</td></tr><tr><td>16-Mar-25</td><td>8-Feb-26</td><td>Early-stage Recovery</td><td>47</td><td>11%</td></tr><tr><td>8-Feb-26</td><td>28-Jun-26</td><td>Expansion</td><td>20</td><td>8%</td></tr><tr><td rowspan="4" colspan="2">Average</td><td>Early-stage Recovery</td><td>25</td><td>12%</td></tr><tr><td>Expansion</td><td>180</td><td>84%</td></tr><tr><td>Plateau</td><td>67</td><td>1%</td></tr><tr><td>Recession</td><td>124</td><td>-32%</td></tr></table>

## Home prices trend (annual)

Annual Hong Kong secondary home price growth  
![](images/48e97797222107cf34aab87d960ac3a6483a9620220a8e81cb6cbc6ac445e2bb.jpg)

## Is this a dead cat bounce?

Historical home price change in (1) early-stage recovery; (2) “dead cat bounce” (i.e., home price rebound which was temporary and did not last)

![](images/41a99f145a5f02da6dc23b5ac5596caee5911dd3420990a5192680b0a52eda39.jpg)  
Source: Centraline, JPM  
Note: The duration on the horizontal axis refers to the number of weeks since the first home price rebound.

High-frequency data

## Sales volume staying sustainably robust

Hong Kong residential transaction volume (primary & secondary)  
![](images/2703c462d99161850aca930b01096e735ab66ac0d289e6bbbdd6188ac7ca5893.jpg)

## Weekly secondary sales volume has moderated

Weekly secondary transactions in 35 major estates  
![](images/0d66f55ba13160542c835c06c84cedcb9fb10936476759557f48d882f02317c4.jpg)

## Sell-through rates have moderated due to more aggressive pricing

## First-day sell-through rates of primary launches over the past month

<table><tr><td>Project</td><td></td><td>Location</td><td>Lead Developer</td><td>Launch Date</td><td>ASP (HK$ psf)</td><td>Units launched</td><td>Units sold</td><td>Sell- through</td><td>vs. previous phase</td><td>vs. secondary prices</td></tr><tr><td>Lime SPARK</td><td>形璿</td><td>Tsuen Wan</td><td>SHKP</td><td>23-May-26</td><td>18 - 20K</td><td>87</td><td>87</td><td>100%</td><td>3%</td><td>22%</td></tr><tr><td>Highwood Ph5</td><td>壹沐2期</td><td>To Kwa Wan</td><td>Henderson</td><td>23-May-26</td><td>20 - 27K</td><td>35</td><td>29</td><td>83%</td><td>1%</td><td>26%</td></tr><tr><td>Lime SPARK</td><td>形璿</td><td>Tsuen Wan</td><td>SHKP</td><td>30-May-26</td><td>18 - 20K</td><td>52</td><td>52</td><td>100%</td><td>3%</td><td>26%</td></tr><tr><td>Highwood Ph6</td><td>壹沐2期</td><td>To Kwa Wan</td><td>Henderson</td><td>31-May-26</td><td>22 - 27K</td><td>23</td><td>5</td><td>22%</td><td>13%</td><td>35%</td></tr><tr><td>Pavilia Rosa</td><td>澈蘊</td><td>Kowloon Tong</td><td>NWD</td><td>4-Jun-26</td><td>30 - 36K</td><td>65</td><td>40</td><td>62%</td><td>-</td><td>29%</td></tr><tr><td>The Headland Residences</td><td>海德園</td><td>Chai Wan</td><td>Swire Prop</td><td>9-Jun-26</td><td>16 - 19K</td><td>78</td><td>41</td><td>53%</td><td>-1%</td><td>15%</td></tr><tr><td>Pavilia Rosa</td><td>澈蘊</td><td>Kowloon Tong</td><td>NWD</td><td>12-Jun-26</td><td>30 - 36K</td><td>28</td><td>16</td><td>57%</td><td>-</td><td>29%</td></tr><tr><td>One Victoria Cove Ph4</td><td>首岸4期</td><td>Hung Hom</td><td>Henderson</td><td>14-Jun-26</td><td>20 - 23K</td><td>80</td><td>59</td><td>74%</td><td>-2%</td><td>18%</td></tr><tr><td>One Victoria Cove Ph4</td><td>首岸4期</td><td>Hung Hom</td><td>Henderson</td><td>18-Jun-26</td><td>20 - 23K</td><td>53</td><td>5</td><td>9%</td><td>-2%</td><td>18%</td></tr><tr><td>La Montagne Ph4B</td><td>海盈山4B期</td><td>Wong Chuk Hang</td><td>Kerry</td><td>18-Jun-26</td><td>28 - 32K</td><td>75</td><td>34</td><td>45%</td><td>5%</td><td>13%</td></tr><tr><td>Average</td><td></td><td></td><td></td><td></td><td></td><td>576</td><td>368</td><td>64%</td><td>3%</td><td>23%</td></tr></table>

Source: HKET, HKEJ, Centraline, Midland

## Developers are pricing more aggressively

Hong Kong residential – average price premium (primary over secondary)

![](images/3366fedfcde2f80345b9c343ea0fa22b53b9d6d1cb60df2f70f2c8e7528c406c.jpg)

## Developers are buying lands more confidently

Summary of recent land acquisitions and estimated margin

<table><tr><td>Date</td><td>Land Site</td><td>Developer</td><td>Location</td><td>Est. No. of units</td><td>Price (HK$psf GFA)</td><td>Est. margin based on latest ASP</td><td>Implied ASP with a 15% margin (HK$psf SA)</td><td>% increase required from latest ASP</td></tr><tr><td>18-Nov-25</td><td>Tsuen Wan Town 441</td><td>Chinachem</td><td>Tsuen Wan</td><td>780</td><td>5,692</td><td>16%</td><td>15,374</td><td>-4%</td></tr><tr><td>6-Nov-25</td><td>Tuen Mun A16</td><td>SHKP</td><td>Tuen Mun</td><td>1,280</td><td>4,991</td><td>13%</td><td>13,044</td><td>0%</td></tr><tr><td>7-Jan-26</td><td>New Kowloon 6674</td><td>Sino/Great Eagle</td><td>Choi Hung</td><td>570</td><td>4,339</td><td>19%</td><td>13,455</td><td>-7%</td></tr><tr><td>10-Feb-26</td><td>NKIL 6675</td><td>COLI</td><td>Kowloon Bay</td><td>470</td><td>6,352</td><td>8%</td><td>20,026</td><td>5%</td></tr><tr><td>16-Feb-26</td><td>Inland 860</td><td>Kerry Prop</td><td>Shau Kei Wan</td><td>300</td><td>9,343</td><td>3%</td><td>24,593</td><td>12%</td></tr></table>

## Banks are revising up valuations

Centa Valuation Index (CVI) vs. secondary home price 1m rolling W/W

![](images/079d31f8c46e7f4d98c9349ab2fbe2a00ef9f97a1ee76cfd591d915277de50a0.jpg)

Secondary listings have dropped from the peak, but have rebounded recently

Secondary listings (properties for sale) on Centaline

![](images/c70dbea1b102416f9db339f636e645634afe06b3c5f4b81c019b8d72185f9374.jpg)

## No. of viewing appointments staying strong

Weekend viewing appointment volume (in 15 housing estates) 美联15大屋苑周末预约看房量  
![](images/d6d57197925042c97b468c5bb384277c1776fd1215f6044019ec502174dffc81.jpg)

Home price drivers

## Home price drivers

Correlation with HK home prices Y/Y  
![](images/3df3cecd44cc29d07a566f640c0f2f9e21f8f728597b9012e344c416b765e4ed.jpg)

Hong Kong secondary home price index (CCL) versus Hang Seng Index (absolute)  
![](images/cc9491c9af78ed7cafb3d8d50332d44e69d6fc4af2e2da017a8c670401a259f0.jpg)

## Stock market

Hong Kong secondary home price index (CCL) Y/Y versus Hang Seng Index Y/Y  
![](images/0a461f451d32f3873852e2505fabf3c61e8c0684816dbe35d170eca5629a0b87.jpg)

Hong Kong secondary home price index (CCL) Y/Y versus inventory month  
![](images/26edd2d41345ec1417713a5dec9401f310d119dc8530c667195d28d5d4ac1735.jpg)

Hong Kong residential inventory months  
![](images/ceba7bf8ec73c48d217ee56d2a3c4f081b479e8fa00adda6ba99b36b521f23a3.jpg)

<table><tr><td colspan="2">Hong Kong private residential supply in next 3-4 years versus 2026E primary sales volume</td></tr><tr><td>Private residential supply for next 3-4 years</td><td>101,000 Under construction / planningPotential launches over the next yearNo. of unsold units</td></tr><tr><td>2026E primary sales volume</td><td>22,000</td></tr></table>

Hong Kong private residential inventory year based on potential supply in next 3-4 years  
![](images/30be66eb5593bc9085cfc62f3cbd05f0e7a46f266143ce83b5312c86081b4c4c.jpg)

## Mortgage rate

HK mortgage rate / 1M HIBOR / Prime Rate vs. US Fed Fund Rate

![](images/2dcd228beafda9472210f35939e59bdf4723ce88764e90ab6066ba293cc94467.jpg)

HK gross rental yield over mortgage rate versus secondary home price  
![](images/ca2c5a2adfaa5dd810fe751e467dbc6da9cb4491f06c57194c3e4253749c4f9f.jpg)

## Mainland Chinese buyers in HK residential market

![](images/ec82ca4df187c9ba6dfad967abbfd409997aa0196d722a2ae1f4fb38cebf01c7.jpg)  
Source: Centraline

## Mainland Chinese buyers in HK residential market

Percentage of Mainland Chinese buyers for private residential (by value)

![](images/6b1b19791491479cc0141e9d6451d3a2c174cf3c798b3da5179274b757014c54.jpg)  
Source: Centraline  
Note: "Mainland Chinese buyers" are defined as homebuyers with a Putonghua pingyin in the last name.

Source: Centraline

Note: “Mainland Chinese” is defined here using the Mandarin pinyin of the buyer’s last name and does not distinguish the buyer’s current residence or identity. As a result, “Mainland Chinese” who are residing in Hong Kong—as well as local Hong Kong residents with Mandarin-pinyin last names—are also classified as “Mainland Chinese” in this dataset.

## Mainland Chinese buyers in HK residential market

Percentage of Mainland Chinese buyers in private residential sales (by value)

![](images/7bfc2db5a74544cc5279db590c540d7e4659bf791c7815bfed3f494f8588d824.jpg)

## Mainland Chinese buyers in HK residential market

Percentage of Mainland Chinese buyers in private residential sales (by volume)

![](images/d73f4d0eb8a010892136c5040e8e4c4f6b89f61063592753dd85ab2ad354d6e2.jpg)

## Mainland Chinese buyers in HK residential market

HK private residential market - % of buyers who are NOT holders of Hong Kong Identity Card (HKID)

<table><tr><td rowspan="2"></td><td colspan="4">Individual buyers who are not HKID holders</td></tr><tr><td>Volume (units)</td><td>as % of total</td><td>Value (HK$ bn)</td><td>as % of total</td></tr><tr><td>FY20/21</td><td>110</td><td>0.1%</td><td>1.1</td><td>0.2%</td></tr><tr><td>FY21/22</td><td>153</td><td>0.2%</td><td>1.6</td><td>0.2%</td></tr><tr><td>FY22/23</td><td>168</td><td>0.3%</td><td>1.6</td><td>0.4%</td></tr><tr><td>FY23/24</td><td>700</td><td>1.6%</td><td>6.8</td><td>2.0%</td></tr><tr><td>FY24/25</td><td>2,997</td><td>5.5%</td><td>31.3</td><td>7.2%</td></tr></table>

## Mainland Chinese buyers in HK residential market

HK private residential market - % of corporate buyers (以公司名义购入)

![](images/73bc6c26dd0c27703178ea68802d85f8e7b60b04470c53af7565f691f868a3f8.jpg)  
Source: Midland

## Mainland Chinese buyers in HK residential market

## Personal cross-boundary remittance regulations from Mainland China to Hong Kong SAR

<table><tr><td>Category</td><td>Quota</td><td>Details</td></tr><tr><td>Facilitative foreign exchange arrangement</td><td>US$50,000 per person per year</td><td>Directly conduct currency conversion at Mainland banks with identity document and remit outside the Mainland.</td></tr><tr><td>購匯便利化額度</td><td></td><td>If a remitter prefers not to use the quota / the conversion quota is reached, remitter shall provide the bank with supporting documents for verification of the use of funds (e.g. travel, study abroad, daily life, and medical care.)</td></tr><tr><td>Payment Connect 跨境支付通</td><td>Follow the facilitative foreign exchange arrangement (US$50,000 per year)</td><td>Real-time and small-value cross-boundary remittances at participating institutions in the Mainland</td></tr><tr><td>Withdraw cash using debt/credit cards issued in Mainland</td><td>Annual limit of RMB100,000, and a daily limit of RMB10,000</td><td></td></tr><tr><td>Cross-border cash carrying</td><td>Rmb 20,000 per person per trip; or USD 5,000 for foreign currency</td><td></td></tr></table>

Source: HKMA

## Mainland Chinese buyers in HK residential market

% of Mainland Chinese buyers (by volume) vs. secondary home price index (CCL)

% of Mainland Chinese buyers

Secondary home prices

![](images/1b00a8fa95358623e46c3bf7079bd3b81071b90de73bcc9f6da6aa19557d311c.jpg)  
Source: Centraline  
Note: “Mainland Chinese” is defined here using the Mandarin pinyin of the buyer’s last name and does not distinguish the buyer’s current residence or identity. As a result, “Mainland Chinese” who are residing in Hong Kong—as well as local Hong Kong residents with Mandarin-pinyin last names—are also classified as “Mainland Chinese” in this dataset.

## Mainland Chinese buyers in HK residential market

## No. of approved visas under various talent recruitment schemes

No. of visas granted  
![](images/8bb43a993ce5ab6efecbfcb68a585e37d1639da6de3d7036119765e56809fbd9.jpg)

Top Talent Pass Scheme

General Employment Policy

■ Immigration Arrangements for Non-local Graduates (IANG)

## ■ Quality Migrant Admission Scheme

■ Admission Scheme for Mainland Talents and Professionals

## Districts with the most “Mainland Chinese” buyers in Hong Kong

Top 5 districts ranked by no. of Mainland Chinese buyers (primary units) since the lifting of the additional stamp duties (Mar 2024 to Feb 2026)

<table><tr><td>District</td><td></td><td>Total</td><td>Primary</td><td>Secondary</td></tr><tr><td>Kai Tak</td><td>啟德</td><td>3,050</td><td>2,786</td><td>264</td></tr><tr><td>Wong Chuk Hang</td><td>黃竹坑</td><td>1,162</td><td>1,131</td><td>31</td></tr><tr><td>Cheung Sha Wan / Sham Shui Po</td><td>長沙灣/深水埗</td><td>1,376</td><td>838</td><td>538</td></tr><tr><td>Tseung Kwan O</td><td>將軍澳</td><td>1,544</td><td>777</td><td>767</td></tr><tr><td>Central &amp; Western</td><td>中西區</td><td>1,971</td><td>731</td><td>1,240</td></tr></table>

Note: For projects involving a consortium, we assume an equal split among the developers.

## Exposure to Kai Tak

Developers' exposure in Kai Tak Runway Area based on attributable number of unsold units  
![](images/d47811dc55b20197201e7ae1cf79210b7cc84f5c814d90894a9154bacc50076f.jpg)

## Other supportive factors – Structural population growth

![](images/35253e1f3d3ba7086da0cfc4af01d8b0a30044212952063db71ad8a19d45e3dd.jpg)

Hong Kong annual private residential sales volume

## Other supportive factors – Pent-up demand to be released

![](images/c3bd1699a5f0d172cd4ebe78fb4d75720c65933bbc847bb090f83175ddba0930.jpg)

## Other supportive factors – Renters turned buyers

Centaline Rental Index (CRI)

![](images/c08eba75311789ddbf6f07e8cff5beae22ddb895cf0bb47e386356753ceb54b4.jpg)  
Source: Centraline

## Other supportive factors – Renters turned buyers

Centaline Rental Index (CRI) seasonality (Jan = 100)

![](images/68c9250e9dc2998e474344525e9d03e1b108571be043ec9cacbc1a99b8704570.jpg)

% of renters out of households who live in private housing

% of renters out of households who live in private housing

'000 households

![](images/24eabc92a0696793da4cc29ad97bddb90d3d72ffa930cf57d416c98cc6140d6b.jpg)

Other Key Charts

## Medium to long-term supply

## HK Government's housing demand and supply 10-year forecast (2026/27 – 2035/36)

<table><tr><td colspan="2"></td><td>Upper range</td><td>Mid-point</td><td>Lower range</td></tr><tr><td>a)</td><td>Net increase in number of households</td><td>207,600</td><td>194,000</td><td>180,400</td></tr><tr><td>b)</td><td>Households displaced by redevelopment</td><td>52,500</td><td>52,500</td><td>52,500</td></tr><tr><td>c)</td><td>Inadequately housed households</td><td>127,500</td><td>127,500</td><td>127,500</td></tr><tr><td>d)</td><td>Miscellaneous factors</td><td>36,500</td><td>36,500</td><td>36,500</td></tr><tr><td></td><td>Gross housing demand</td><td>424,100</td><td>410,500</td><td>396,900</td></tr><tr><td></td><td>Total housing supply target</td><td>432,800</td><td>419,100</td><td>405,200</td></tr></table>

## Public and private housing supply over last 20 years

Historical completion of public housing

![](images/7db513f88fbbd76d788aaf6c8e9579ef5b4eb1de5ce0435706219e7a598d0c8c.jpg)  
Historical completion of private housing

![](images/07fb311672be279606c48b5bc42d19fc7ebbbca89fac168e9db2e92f536dfb13.jpg)

## Sellable resources by developer

Sellable resources by developer

![](images/8a4b471222686c3f41a5fbbe774455dd56d6f41501f5653141ba88afcedbd9d5.jpg)

Pipeline of primary launches  
1-year pipeline of primary launches by district  
![](images/9d46bc2946259657e980fe6218230298d63807bae910fe83da2c1de36acf98be.jpg)

Pipeline of primary launches in 2026 (Hong Kong Island)

<table><tr><td>District</td><td>Project</td><td>Developer</td><td>Units</td></tr><tr><td>Wong Chuk Hang</td><td>The Southside Ph6A &amp; 6B</td><td>Wheelock/MTR</td><td>617</td></tr><tr><td>Wong Chuk Hang</td><td>The Southside (La Montagne) Ph4B</td><td>Kerry/Sino/Swire/MTR</td><td>368</td></tr><tr><td>Chai Wan</td><td>Headland Residence Ph2</td><td>Swire/CMC</td><td>258</td></tr><tr><td>Sheung Wan</td><td>Elgin Street</td><td>Henderson</td><td>250</td></tr><tr><td>Sai Ying Pun</td><td>Kwai Heung Street</td><td>Far East/URA</td><td>200</td></tr><tr><td>Ap Lei Chau</td><td>PORTO</td><td>Wang On</td><td>174</td></tr><tr><td>Wan Chai</td><td>Queen&#x27;s Road East</td><td>Swire</td><td>162</td></tr><tr><td>North Point</td><td>F

[中间内容因长度限制已省略]

re therefore subject to change without notice. Periodic updates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any

## Disclosures

reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised July 04, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.
"""
