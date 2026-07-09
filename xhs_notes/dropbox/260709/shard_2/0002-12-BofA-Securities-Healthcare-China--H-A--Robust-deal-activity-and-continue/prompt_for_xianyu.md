你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
# Healthcare - China (H/A)

# Robust deal activity and continued R&D progress driving healthcare re-rating

Price Objective Change

## CSPC: another collaboration with AstraZeneca

On 2 July, CSPC announced a collaboration agreement with AstraZeneca (AZ) to leverage CSPC's siRNA drug-discovery and extrahepatic targeted-delivery platforms. CSPC and AZ will co-develop PCCs for two renal disease targets. AZ will have the option to obtain exclusive global, or ex-China, rights for each preclinical candidate, while CSPC will retain China rights to one candidate. CSPC will receive an upfront payment of US\$30mn and is eligible for up to US\$540mn/US\$1.2bn in development/sales milestone payments plus potential single-digit royalties. We add the US\$30mn upfront payment to our estimates and raise our 2027 revenue/NP estimate by 0.8%/2.0%, as well as lift our long-term sales estimates. Our PO increases to HK\$7.6 from HK\$6.8. However, we reiterate our Underperform rating on CSPC given continued sales pressure on its key marketed drugs.

## Gushengtang: footprint expansion through acquisitions

On 5 July, Gushengtang (GST) announced the acquisitions of Shahe Hospital and Beijing Hongyang Hospital. The acquisitions will expand the company's medical institution network and strengthen its presence in Beijing. Mgmt. expects the acquired hospitals to generate synergies with GST's existing medical institutions and online healthcare platform. The transactions will be funded by proceeds from the company's recent share placement and convertible bond issuance, as well as internal cash resources. We maintain our Buy rating and HK\$32.60 PO on GST.

## Innovent: commercialization deal with Lilly on CDK4/6

Recently, Innovent announced a commercialization agreement with Lilly for Verzenios (abemaciclib) in mainland China. Under the agreement, Innovent will be responsible for the product's imports, marketing, distribution, and promotion. Verzenios was the first CDK4&6 inhibitor to be included in the NRDL in 2021 and has since secured reimbursement coverage for both early and advanced breast cancer indications. To reflect the revenue contribution from abemaciclib from 2H26, we lift our 2026/27/28 revenue estimates by 3.3%/5.3%/4.7%. Consequently, we raise our DCF-derived PO to HK\$119.2 (from HK\$116.8) and reiterate our Buy rating given the company's enriched commercial products portfolio and solid in-house R&D capabilities.

## Hengrui: multiple innovative drug R&D updates

Hengrui has announced multiple R&D updates recently. It disclosed that the marketing application for SHR-A1811's third indication (1L/2L HER2-low mBC) has been accepted by NMPA and granted priority review. In addition, Hengrui received clinical trial approvals for several innovative drug candidates, including HRS-4508 (for breast and lung cancers), SHR-6914 (for PCa), HRS-7525 (for solid tumor), and several combo therapies. Although we are concerned about the potential impact on generics from the new round of anti-corruption campaign, especially in low-tier cities, we still believe its sales growth on innovative drugs portfolio can achieve 30% growth in 2026E. We reiterate our Buy rating and RMB\$72.70 PO on Hengrui.

## 07 July 2026

Equity
China
Healthcare

David Li >>
Research Analyst
BofA (Hong Kong)
+852 3508 4531
davidbo.li@bofa.com

Sandra Sun >>
Research Analyst
BofA (Hong Kong)
sandra.sun@bofa.com

Ethan Cui >>
Research Analyst
BofA (Hong Kong)
ethan.cui@bofa.com

## Exhibit 1: PO changes

We lift CSPC's and Innovent's POs

<table><tr><td>Company</td><td>Currency</td><td>Old PO</td><td>New PO</td></tr><tr><td>CSPC</td><td>HK$</td><td>6.8</td><td>7.6</td></tr><tr><td>Innovent</td><td>HK$</td><td>116.8</td><td>119.2</td></tr></table>

Source: BofA Global Research  
BofA GLOBAL RESEARCH

## Abbreviations:

siRNA: Small interfering ribonucleic acid

PCC: Pre-clinical Candidate

GST: Gushengtang

CDK4/6: Cyclin-Dependent Kinase 4/6

NRDL: National Reimbursement Drug List

HER2: Human Epidermal Growth Factor Receptor 2

mBC: Metastatic Breast Cancer

1/2L: first/second-line

NMPA: National Medical Products Administration

PCa: prostate cancer

EGFR: Epidermal Growth Factor Receptor

ADC: Antibody-Drug Conjugate

NSCLC: Non-Small Cell Lung Cancer

NP: Net Profit

## Estimate changes

## CSPC

Separately, CSPC has initiated two Phase III studies for SYS6010 (EGFR ADC) in NSCLC recently. We add the US\$30mn upfront payment to our estimate and raise our 2027 revenue/NP estimates by 0.8%/2.0%. As the partnered candidates remain at the preclinical stage, we do not include any revenue contribution from these candidates in our estimates. We also raise our SYS6010 NSCLC penetration assumptions from 2029 and lift our revenue estimates for the product, reflecting its broader Phase III development plan. Overall, we lift our PO to HK\$7.6 from HK\$6.8. We reiterate our Underperform rating given continued sales pressure on CSPC's key marketed drugs.

## Exhibit 2: Estimate changes

We raise 2027E revenue/NP by 0.8%/2.0%

<table><tr><td></td><td colspan="3">New</td><td colspan="3">Old</td><td colspan="3">% Change (New vs Old)</td></tr><tr><td>(RMB mn)</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Total Revenue</td><td>34,906</td><td>25,493</td><td>27,155</td><td>34,906</td><td>25,281</td><td>27,155</td><td>0.0%</td><td>0.8%</td><td>0.0%</td></tr><tr><td>COGS</td><td>(8,884)</td><td>(8,624)</td><td>(9,232)</td><td>(8,884)</td><td>(8,620)</td><td>(9,232)</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>Gross profit</td><td>26,022</td><td>16,868</td><td>17,923</td><td>26,022</td><td>16,661</td><td>17,923</td><td>0.0%</td><td>1.2%</td><td>0.0%</td></tr><tr><td>Selling and distribution costs</td><td>(6,458)</td><td>(6,118)</td><td>(6,246)</td><td>(6,458)</td><td>(6,067)</td><td>(6,246)</td><td>0.0%</td><td>0.8%</td><td>0.0%</td></tr><tr><td>Administrative expenses</td><td>(956)</td><td>(892)</td><td>(950)</td><td>(956)</td><td>(885)</td><td>(950)</td><td>0.0%</td><td>0.8%</td><td>0.0%</td></tr><tr><td>R&amp;D expense</td><td>(5,829)</td><td>(5,353)</td><td>(5,838)</td><td>(5,829)</td><td>(5,309)</td><td>(5,838)</td><td>0.0%</td><td>0.8%</td><td>0.0%</td></tr><tr><td>Financing expenses</td><td>(31)</td><td>(25)</td><td>(19)</td><td>(31)</td><td>(25)</td><td>(19)</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>Profit Before Tax</td><td>13,638</td><td>5,371</td><td>5,815</td><td>13,638</td><td>5,266</td><td>5,815</td><td>0.0%</td><td>2.0%</td><td>0.0%</td></tr><tr><td>Tax expense</td><td>(2,387)</td><td>(940)</td><td>(1,018)</td><td>(2,387)</td><td>(922)</td><td>(1,018)</td><td>0.0%</td><td>2.0%</td><td>0.0%</td></tr><tr><td>Net Income</td><td>11,082</td><td>4,364</td><td>4,725</td><td>11,082</td><td>4,279</td><td>4,725</td><td>0.0%</td><td>2.0%</td><td>0.0%</td></tr><tr><td>Adjusted net income</td><td>11,127</td><td>4,411</td><td>4,774</td><td>11,127</td><td>4,326</td><td>4,774</td><td>0.0%</td><td>2.0%</td><td>0.0%</td></tr><tr><td>Basic EPS</td><td>0.97</td><td>0.38</td><td>0.41</td><td>0.97</td><td>0.37</td><td>0.41</td><td>0.0%</td><td>2.0%</td><td>0.0%</td></tr><tr><td>Fully diluted EPS</td><td>0.97</td><td>0.38</td><td>0.41</td><td>0.97</td><td>0.37</td><td>0.41</td><td>0.0%</td><td>2.0%</td><td>0.0%</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="3">changes in percentage point</td></tr><tr><td>Gross margin (%)</td><td>74.5%</td><td>66.2%</td><td>66.0%</td><td>74.5%</td><td>65.9%</td><td>66.0%</td><td>0.0</td><td>0.3</td><td>0.0</td></tr><tr><td>Selling expense % of sales</td><td>-18.5%</td><td>-24.0%</td><td>-23.0%</td><td>-18.5%</td><td>-24.0%</td><td>-23.0%</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>G&amp;A % of sales</td><td>-2.7%</td><td>-3.5%</td><td>-3.5%</td><td>-2.7%</td><td>-3.5%</td><td>-3.5%</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>R&amp;D expenses as % of sales</td><td>-16.7%</td><td>-21.0%</td><td>-21.5%</td><td>-16.7%</td><td>-21.0%</td><td>-21.5%</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Tax rate (%)</td><td>-17.5%</td><td>-17.5%</td><td>-17.5%</td><td>-17.5%</td><td>-17.5%</td><td>-17.5%</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Net margin (%)</td><td>31.7%</td><td>17.1%</td><td>17.4%</td><td>31.7%</td><td>16.9%</td><td>17.4%</td><td>0.0</td><td>0.2</td><td>0.0</td></tr><tr><td>%yoy Growth</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>34.2%</td><td>-27.0%</td><td>6.5%</td><td>34.2%</td><td>-27.6%</td><td>7.4%</td><td>0.0</td><td>0.6</td><td>-0.9</td></tr><tr><td>Net income</td><td>185.5%</td><td>-60.6%</td><td>8.3%</td><td>185.5%</td><td>-61.4%</td><td>10.4%</td><td>0.0</td><td>0.8</td><td>-2.2</td></tr></table>

Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

## Innovent

Exhibit 3: Estimate changes

We lift 2026/27/28E revenue by 3.3%/5.3%/4.7%

<table><tr><td></td><td colspan="3">New</td><td colspan="3">Old</td><td colspan="3">% Change (New vs Old)</td></tr><tr><td>(RMB mn)</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>Total Revenue</td><td>18,453</td><td>25,001</td><td>27,688</td><td>17,871</td><td>23,749</td><td>26,447</td><td>3.3%</td><td>5.3%</td><td>4.7%</td></tr><tr><td>COGS</td><td>-2,566</td><td>-4,443</td><td>-4,974</td><td>-2,450</td><td>-4,193</td><td>-4,726</td><td>4.8%</td><td>6.0%</td><td>5.3%</td></tr><tr><td>Gross profit</td><td>15,886</td><td>20,558</td><td>22,714</td><td>15,421</td><td>19,557</td><td>21,721</td><td>3.0%</td><td>5.1%</td><td>4.6%</td></tr><tr><td>R&amp;D expense</td><td>-4,613</td><td>-4,500</td><td>-4,569</td><td>-4,468</td><td>-4,275</td><td>-4,364</td><td>3.3%</td><td>5.3%</td><td>4.7%</td></tr><tr><td>SG&amp;A expense</td><td>-9,226</td><td>-12,000</td><td>-13,014</td><td>-8,935</td><td>-11,400</td><td>-12,430</td><td>3.3%</td><td>5.3%</td><td>4.7%</td></tr><tr><td>Other income/expense</td><td>400</td><td>400</td><td>400</td><td>400</td><td>400</td><td>400</td><td></td><td></td><td></td></tr><tr><td>Operating income</td><td>996</td><td>2,861</td><td>3,776</td><td>966</td><td>2,686</td><td>3,571</td><td>3.0%</td><td>6.5%</td><td>5.7%</td></tr><tr><td>Other income/expenses</td><td>167</td><td>250</td><td>277</td><td>162</td><td>237</td><td>264</td><td>3.3%</td><td>5.3%</td><td>4.7%</td></tr><tr><td>Finance costs</td><td>-88</td><td>-95</td><td>-95</td><td>-88</td><td>-95</td><td>-95</td><td>0.0%</td><td>0.0%</td><td>0.0%</td></tr><tr><td>Profit Before Tax</td><td>1,075</td><td>3,015</td><td>3,957</td><td>1,041</td><td>2,828</td><td>3,740</td><td>3.3%</td><td>6.6%</td><td>5.8%</td></tr><tr><td>Tax expense</td><td>-140</td><td>-392</td><td>-514</td><td>-135</td><td>-368</td><td>-486</td><td>3.3%</td><td>6.6%</td><td>5.8%</td></tr><tr><td>Net Income</td><td>935</td><td>2,623</td><td>3,443</td><td>905</td><td>2,460</td><td>3,254</td><td>3.3%</td><td>6.6%</td><td>5.8%</td></tr><tr><td>Basic EPS</td><td>0.56</td><td>1.56</td><td>2.05</td><td>0.54</td><td>1.47</td><td>1.94</td><td>3.3%</td><td>6.6%</td><td>5.8%</td></tr><tr><td>Fully diluted EPS</td><td>0.54</td><td>1.51</td><td>1.98</td><td>0.52</td><td>1.41</td><td>1.87</td><td>3.3%</td><td>6.6%</td><td>5.8%</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td colspan="3">(changes in percentage points)</td></tr><tr><td>Gross margin (%)</td><td>86%</td><td>82%</td><td>82%</td><td>86%</td><td>82%</td><td>82%</td><td>-0.2</td><td>-0.1</td><td>-0.1</td></tr><tr><td>R&amp;D expense % of sales</td><td>-25%</td><td>-18%</td><td>-17%</td><td>-25%</td><td>-18%</td><td>-17%</td><td>0.0</td><td>0.0</td><td>0.0</td></tr></table>

## Exhibit 3: Estimate changes

We lift 2026/27/28E revenue by 3.3%/5.3%/4.7%

<table><tr><td></td><td colspan="3">New</td><td colspan="3">Old</td><td colspan="3">% Change (New vs Old)</td></tr><tr><td>SG&amp;A % of sales</td><td>-50%</td><td>-48%</td><td>-47%</td><td>-50%</td><td>-48%</td><td>-47%</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Operating margin (%)</td><td>5%</td><td>11%</td><td>14%</td><td>5%</td><td>11%</td><td>14%</td><td>0.0</td><td>0.1</td><td>0.1</td></tr><tr><td>Tax rate (%)</td><td>-13%</td><td>-13%</td><td>-13%</td><td>-13%</td><td>-13%</td><td>-13%</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Net margin (%)</td><td>5%</td><td>10%</td><td>12%</td><td>5%</td><td>10%</td><td>12%</td><td>0.0</td><td>0.1</td><td>0.1</td></tr><tr><td>% yoy</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Revenue</td><td>41%</td><td>35%</td><td>11%</td><td>37%</td><td>33%</td><td>11%</td><td>4.5</td><td>2.6</td><td>-0.6</td></tr></table>

Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

## Exhibit 4: Stocks mentioned

Prices and ratings for stocks mentioned in this report

<table><tr><td>BofA Ticker</td><td>Bloomberg ticker</td><td>Company name</td><td>Price</td><td>Rating</td></tr><tr><td>CHJTF</td><td>1093 HK</td><td>CSPC Pharmaceutical</td><td>HK$ 8.23</td><td>C-3-7</td></tr><tr><td>GSHTF</td><td>2273 HK</td><td>Gushengtang</td><td>HK$ 30.78</td><td>C-1-7</td></tr><tr><td>XMOKF</td><td>600276 CH</td><td>Hengrui Medicine</td><td>CNY 56.77</td><td>B-1-7</td></tr><tr><td>IVBXF</td><td>1801 HK</td><td>Innovent</td><td>HK$ 90.5</td><td>C-1-9</td></tr></table>

Source: BofA Global Research  
BofA GLOBAL RESEARCH

## Price objective basis & risk

## CSPC Pharmaceutical (CHJTF)

Our DCF model for CSPC derived a PO of HK\$7.6. Our assumption of the DCF model includes a 5% debt-to-asset ratio, a 4.0% risk free rate, 7.0% market premium, and 5.0% cost of debt. We apply beta of 0.8 and arrive at 9.6% cost of equity and 9.3% WACC. We estimate a 1.5% terminal growth for the company.

Upside risks to our PO are: strong performance of newly launched products, lower-than-expected impact from VBP and NRDL price cut, better-than-expected clinical progress and results.

Downside risks to our PO are: price-cut pressure from VBP on new drugs, failure in clinical trials.

## Gushengtang (GSHTF)

We use discounted cash flow to arrive at a PO of HK\$32.6. We use a debt to asset ratio of 5%, a risk free rate of 4%, a market premium of 7%, and a beta of 1.1 to arrive at a 11.7% cost of equity. We also apply a 5% cost of debt. We use a WACC of 11.4% and a terminal growth of 1.5%.

Downside risks: 1) policy and regulatory risks on TCM and healthcare service providers, 2) intense competition, 3) failure in recruiting professionals, 4) data protection risks, 5) soft consumption environment in China and weak demand for TCM services.

## Hengrui Medicine (XMOKF)

Our PO of RMB72.7 is based on a DCF model. Our assumption of the DCF model includes a 0% debt-to-asset ratio, a 2.0% risk free rate, 7.0% market premium, and 5.1% cost of debt. We apply beta of 0.69 and arrive at 6.8% cost of equity. We estimate a

## 3.5% terminal growth for the company.

Downside risks to our PO are (1) setback in drug development and a delay in product approvals, (2) slow sales ramp-up of new products, (3) increasing pricing risk from VBP (4) stiffer competition for PD-1 and other drugs, and (5) slow overseas expansion.

Upside risks to our PO are: (1) higher-than-expected net profit margin and (2) faster-than-expected progress of pipeline candidates.

## Innovent (IVBXF)

We derive our PO of HK\$119.2 from a DCF model, assuming a WACC of 9.6% and a terminal growth rate of 4%. The DCF is based on PD-1, biosimilars, mazdutide and a few other drugs' commercial sales as well as revenue estimate of key pipeline assets including IBI363 and others.

Downside risks: co

[中间内容因长度限制已省略]

the extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.

may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.
"""
