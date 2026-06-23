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
Asia Insights

Economics - Asia ex-Japan

## China: A property market "K-shape" is materialising

In our recent thematic note (see China: AI boom, property bust and K-shapes, 27 May 2026), we stated that, “As the fruits of AI-driven growth are mainly reaped by a few selected ‘smart’ cities, especially the four top-tier ones, a real property market recovery may only take place in those cities, especially as property restrictions there have been lifted.” Recent housing data show an evident geographic divergence and lend support to our view. Housing prices in a handful of “smart” cities show clear signs of stabilization, while price declines in most lower-tier cities have worsened. On net, overall housing prices have fallen at a faster pace, leading to heightened downward pressures on aggregate domestic demand. This supports our views that the stabilization across a few large cities cannot fully offset the weakness in other cities, and that the AI boom might not be a cure for China’s economic woes, inflicted largely by the property bust. Beijing still may eventually be impelled to step up policy measures to clean up the bad debt in the property sector and speed up fiscal reform to support those cities that have been left behind.

## Clearer signs of price stabilization in "smart" cities, especially those in the top tier

Amid the AI boom, existing home prices in tier-1 cities have shown further signs of stabilization, with three consecutive months of $0.4\%$ m-o-m gains, while a couple of tier-2 cities have improved mildly. Shanghai emerged as the best performer among the NBS 70 surveyed cities, with existing home prices rising by $0.6\%$ m-o-m in May and a cumulative gain of $1.9\%$ from the January lows. Shenzhen reported a $0.6\%$ gain in May, on par with Shanghai, backed by the latest easing of home purchase restrictions. Beijing and Guangzhou also posted consecutive mild price upticks. Hangzhou and Hefei are among the few tier-2 cities showing tentative positive market signals. By contrast, housing price declines worsened in most lower-tier cities, leading to a wider decline in national average housing prices again to $0.26\%$ m-o-m in May, after the price decline narrowed over four straight months to a $0.23\%$ decrease in April.

## Property sales and investment deteriorated in April-May

Despite signs of stabilization in tier-1 cities, national property indicators have broadly worsened in recent months, pointing to a deeper contraction in Q2. Property investment growth deteriorated markedly to $-22.3\%$ y-o-y in April-May from $-11.2\%$ in Q1. Growth of new home sales by floor space fell to $-11.4\%$ y-o-y in April-May from $-10.4\%$ in Q1, while growth of new home sales by value increased to $-8.7\%$ from $-16.7\%$ , likely reflecting the recent stabilization in tier-1 cities, which account for about $5\%$ of the national total by floor space and about $18\%$ by value. In the first five months of this year, new home sales contracted by $10.8\%$ by floor space and $13.5\%$ by value, respectively, worsening from contractions of $8.7\%$ and $12.6\%$ in 2025, $47.7\%$ and $55.5\%$ below levels seen in January-May 2021. The top 100 developers fared worse. Their contract sales dropped by $20.1\%$ y-o-y by floor space and by $15.3\%$ by value in January-May, $84.3\%$ and $77.1\%$ below levels seen in January-May 2021.

## Uneven wealth effects from higher stock indices

The AI boom is being reflected in higher stock prices, especially in tech-related sectors, as tech stocks now account for more than 30% of the total market capitalization of China's A-share market. As financial centers in China, Shanghai and Shenzhen's housing markets should benefit from the stock market rally through two channels: uneven wealth effects from equity price gains and improved compensation for financial professionals amid surging stock trading volumes. Although the buoyant stock markets have had limited nationwide wealth effects and a minimal overall economic impact, as we predicted in September 2025, some wealthy investors likely benefited disproportionately, widening the inequalities within the population.

## Research Analysts

Asia Economics

Jing Wang - NIHK

jing.wang@NOM.com

+852 2252 1011

Ting Lu - NIHK

ting.lu@NOM.com

+852 2252 1306

## A geographic "K-shape" across housing markets is in the making

Amid the AI boom, China's housing prices have displayed rising evidence of a geographic divergence (i.e., K-shape). Tier-1 cities have broadly stabilized, while a few tier-2 cities have improved mildly. In May, four tier-1 cities logged an average $0.4\%$ m-o-m gain in existing home prices for three straight months. Shanghai and Shenzhen led with $0.6\%$ monthly rises, backed by increased transaction volumes and shrinking housing inventories; Beijing and Guangzhou also posted consecutive mild price upticks. Private Centraline price indices further corroborate official price data. Hangzhou and Hefei are among the few tier-2 cities showing tentative positive market signals. By contrast, housing price declines worsened in most lower-tier cities, leading to a wider decline in national average housing prices.

## Shanghai

The financial hub Shanghai stands out as the strongest performer among all tier-1 cities, as well as all 70 cities surveyed by NBS. Its existing home prices rose $0.6\%$ m-o-m in May (Figure 1), extending the uptrend to four consecutive months, with a cumulative gain of $1.9\%$ from the low in January. These steady price gains are firmly backed by robust transaction volumes. On a year-on-year basis, secondary home transaction volumes in Shanghai grew by a moderate $1.3\%$ in Q1, before rising notably to $22.7\%$ in April, $30.9\%$ in May, and maintaining a strong 26.1 growth in the first 20 days of June. On 10 May, Shanghai recorded a secondary home transaction volume of 1,664 units, hitting another five-year high.

Meanwhile, housing prices are underpinned by the sharp decline in housing listings. As of 31 May, data from Anjuke show that Shanghai's active existing home listings have fallen to 309,205 units, which represents nearly a $20\%$ y-o-y drop. Moreover, compared to a few months ago, Shanghai's housing price stabilization was not just supported by small and old existing homes. Statistics from Lianjia revealed a noticeable shift: in May, transactions of housing priced between RMB5-8mn jumped by $9.3\%$ m-o-m, while transactions of properties priced below RMB3mn dipped by $2.6\%$ m-o-m.

## Shenzhen

Property markets in Shenzhen, as another financial hub and headquarters to global tech giants like Huawei, also experienced substantial price appreciation in May, with existing home prices climbing by 0.6% m-o-m, on par with Shanghai. This represents three straight months of expansion and amounts to a cumulative gain of 1.3%. Transaction volumes have staged a notable turnaround: after a 15.3% y-o-y decline in Q1, transaction volume growth turned positive, rising to 1.7% in April and then increasing further to 17.2% in May; it has since held steady at 11.4% in the first 20 days of June. This recovery is partly attributable to further relaxation of home purchase restrictions unveiled on 30 April.

Fig. 1: Existing home prices for tier-1 cities  
![](images/901637014b12881a80feddde57ba13e8f49de2805a30646dd43ffa9fe97e41ad.jpg)  
Note: Existing home prices reported for each tier-1 city are from the NBS. Source: Centraline, NBS, Wind, NOM Global Economics.

Fig. 2: Home prices in Hangzhou and Hefei  
![](images/6d9e1190e26589318480adf5cea38b6f1bcc5534e42b64bd045fc17e9a118153.jpg)  
Source: NBS, Wind, NOM Global Economics.

## Other two tier-1 cities

Housing prices in the remaining two tier-1 cities have also stabilised notably, especially in Beijing. Although Beijing's price change in May stood at a modest gain of $0.1\%$ m-o-m, it has achieved four consecutive months of sequential increases, with a cumulative gain of $1.4\%$ , the second highest among all tier-1 cities. Guangzhou's housing prices have rebounded for three consecutive months, posting a total increase of $0.5\%$ .

## Evidence from private data

Official price trends are well corroborated by more volatile independent market indicators. Based on the Centraline Leading Index (CLI), which is compiled based on existing home prices, home prices in Shanghai, Beijing, Shenzhen and Guangzhou have rebounded by 4.5%, 3.0%, 2.3%, and 0.3%, respectively, in May from their January lows, with an average gain of 2.5% for the four tier-1 cities over this period.

## Housing markets in a couple of tier-2 cities also improved, but mildly

A small number of second-tier cities have also exhibited tentative positive market signals, including Hangzhou and Hefei.

In Hangzhou, the home of DeepSeek and Alibaba, the decline in existing home prices has been narrowing consistently since last November, and the market finally stabilized in May. Notably, the city's new home market has outperformed remarkably: new home price growth turned positive in February and has since continues to rise, with a $0.5\%$ m-o-m gain in May (Figure 2), ranking first among the 70 major monitored cities by the NBS. Given the absence of a substantial pickup in overall transaction volumes, this outstanding new home price growth is presumably driven mainly by high-end luxury property transactions.

In Hefei, which has secured a vital role in robotics and memory fabrication (e.g., CXMT), existing home prices in March posted their first sequential gain in three years, with a 0.2% m-o-m increase, followed with a 0.1% m-o-m gain in April and flat prices in May, showing initial signs of market stabilization. According to Hefei's housing authority, market sentiment picked up notably in March. Floor space of new and existing home sales jumped by 100.4% m-o-m and 112.9%, respectively, in March, with the year-on-year change of existing home sales at 7.9%.

## The overall home price decline widened again in May

Despite steady home price gains of 0.4% in tier-1 cities, average existing home prices for the overall 70 cities declined by 0.26% m-o-m in May (Figure 3), worsening again after price declines narrowed over four straight months to a 0.23% decrease in April. The larger decline was driven by lower-tier cities, as price declines in tier-2 widened to -0.19% m-o-m in May from -0.10% in April, while the declines in tier-3/4 cities remained the deepest and were unchanged at -0.35%.

Among the 70 cities, 10 cities recorded month-on-month increases in existing home prices in May, less than the 12 recorded in April and 13 in March. Although the number of cities reporting year-on-year new home prices gains increased to 16 in May from 14 in March-April and 10 in February, we believe existing home prices might better reflect the home price trends in China, as prices of new home can be distorted by the rising share of luxury housing and regulatory factors.

The home price data for May are largely in line with the Iceberg index, a leading indicator based on the lowest listing housing prices, which recorded a 0.3% m-o-m decline in May, following a 0.4% decrease in April. As the Iceberg index weekly data indicated a decline of 0.4% m-o-m in the first two weeks of June, we see a limited rebound in June.

## Property sales and investment data remained in a steep contraction

As tier-1 cities account for a small portion of national new home sales, especially by floor space, the stabilization in those cities is not sufficient to fully offset the national property downturn.

Indeed, property investment growth worsened to -24.3% y-o-y in May from -20.1% in April, below the market consensus forecast of -15.0% but close to our more cautious forecast of -20.0%. New home sales growth fell to -13.1% y-o-y by floor space and to -9.5% by value in May from -9.5% and -7.7%, respectively, in April. For other major property indicators, growth of new home starts, new home completions and funds for property investment reached -24.6% y-o-y, -19.9% and -21.5%, respectively, in May, compared with -26.6%, -18.8% and -21.8% in April.

Fig. 3: Existing home prices: K-shape in the making  
![](images/532a08e8281be2a5cb2c7710aab79cd05bc48c17b74d17538bc4a24fcb09e81f.jpg)  
Source: NBS, Wind, NOM Global Economics.

Fig. 4: New home sales volume: CRIC's top 100 developers  
![](images/78b8774a67ddfd8525fb3d36e2d64cf6bedd491ab486f03bc66286911617a9c8.jpg)  
Note: January and February data are presented as the same value as an average of these two months to smooth out LNY distortions.  
Source: CRIC, NOM Global Economics.

April-May data point to a likely deterioration in Q2. Growth of property investment worsened markedly to $-22.3\%$ y-o-y in April-May from $-11.2\%$ in Q1. Growth of new home sales by floor space fell to $-11.4\%$ y-o-y in April-May from $-10.4\%$ in Q1, while growth of new home sales by value increased to $-8.7\%$ from $-16.7\%$ , likely due to the recent stabilization in tier-1 cities, which account for about $5\%$ of the national total by floor space and about $18\%$ by value.

In the first five months of this year, new home sales by floor space and new home sales by value contracted by 10.8% and 13.8%, respectively, worsening from -8.7% and -12.6% in 2025, 47.7% and 55.5% below January-May 2021 levels.

Contract sales of the top 100 developers painted a gloomier picture. In detail, by floor space, sales growth fell slightly to $-13.8\%$ y-o-y in May from $-13.5\%$ in April (Figure 4), while by value, sales growth increased markedly to $-0.2\%$ y-o-y in May from $-8.9\%$ in April, with their year-to-date changes at $-20.1\%$ and $-15.3\%$ , respectively. Developers' contract sales by floor space and by value are $84.3\%$ and $77.1\%$ , respectively, below January-May 2021 levels.

## Wealth effects from rising stock indices

The AI boom is resulting in higher stock prices, especially for tech-related sectors. At the 2026 Lujiazui forum on 17 June, Wu Qing, chairman of the China Securities Regulatory Commission, said that tech stocks now account for more than $30\%$ of the total market capitalization of China's A-share market, and tech companies make up $45\%$ of listed firms with a market cap exceeding RMB100bn. As financial centers in China, housing markets in Shanghai and Shenzhen should benefit from the stock market rally through two channels: uneven wealth effects from equity price gains and improved compensation for financial professionals amid surging stock trading volumes.

\- On wealth effects, from July 2025 to 18 June 2026, the Wind All-A Index, a holistic benchmark tracking the overall performance of all A-shares listed on the Shanghai, Shenzhen and Beijing stock exchanges, increased by $33.2\%$ (Figure 5), which should have driven some wealth effects. The stock price retreat in March due to the Middle East conflict has already been fully recouped. According to Bloomberg, the stock rally was mainly driven by funds from high net-worth individuals, rather than inflows from household savings. Although the stock market rally in H2 2025 resulted in limited nationwide wealth effects and a minimal overall economic impact, as we predicted in September 2025, some wealthy investors likely benefited disproportionately.

\- The surge in stock trading likely pushed up overall brokerage revenues, even though commission rates have declined over the last decade, and boosted the incomes of

financial professionals. Daily average of stock trading volumes surged to new highs of RMB2.8trn in Q2 (as of 18 June) and RMB2.6trn in Q1 2026 (Figure 6), after jumping to RMB2.0trn in Q4 and RMB2.1trn in Q3 from RMB1.2trn in Q2 2025.

Fig. 5: Rising stock indices  
![](images/6bc959787fb0089753812d05c60b84be2c6dc4975a9a9fa8397a3c1720af1170.jpg)  
Source: Wind, NOM Global E

[中间内容因长度限制已省略]

ed or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than ‘Authorised Persons’, ‘Exempt Persons’ or ‘Institutions’ located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, “Offshore Issuers”) that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

## NOM Securities Co., Ltd.

Financial instruments firm registered with the Kanto Local Finance Bureau (registration No. 142)

Member associations: Japan Securities Dealers Association; Investment Management Association of Japan; The Financial Futures Association of Japan; Type II Financial Instruments Firms Association; and Japan Security Token Offering Association.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page:

http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
