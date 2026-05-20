你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  ✅ 三大情景框架：DCF、P/ARR、EV/Sales
  ✅ 关键变量分析
  ✅ 估值逻辑、假设、终值占比等核心内容覆盖
  ✅ 适合准备 AI 相关面试、研究 AI 估值的同学
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
# Key takeaways

- Warsh is Fed B/S critic; he won't change much. Focus on (1) size (2) composition   
- Size = big drop unlikely. Composition = Fed UST WAM shorter but won't matter much   
- Blue sky: bank SRP at IOR + reporting changes = reserve buffer drop. Blue sky may be more impactful vs conventional views

# By Mark Cabana & Katie Craig

Exhibit 1: Fed balance sheet liabilities (\$tn)   
Currency, reserves, and TGA make up the largest shares of the Fed's liabilities   
![](images/ccea59cf7c85dbcb01d121c384792e6b68322bf9eb2296326462dfff63265f08.jpg)

<details>
<summary>bar_stacked</summary>

| Year | Currency | Reserves | TGA | Foreign RRP | ON RRP | Other |
|---|---|---|---|---|---|---|
| 2008 | 0.7 | 0.1 | 0.0 | 0.0 | 0.0 | 0.0 |
| 2010 | 0.8 | 1.5 | 0.0 | 0.0 | 0.0 | 1.0 |
| 2012 | 0.9 | 2.0 | 0.0 | 0.0 | 0.0 | 1.5 |
| 2014 | 1.0 | 3.0 | 0.5 | 0.5 | 0.5 | 2.5 |
| 2016 | 1.1 | 3.5 | 1.0 | 1.0 | 1.0 | 3.0 |
| 2018 | 1.2 | 3.5 | 1.5 | 1.5 | 1.5 | 3.5 |
| 2020 | 1.3 | 3.5 | 2.0 | 2.0 | 2.0 | 4.0 |
| 2022 | 1.4 | 4.5 | 2.5 | 2.5 | 3.5 | 5.0 |
| 2024 | 1.5 | 4.5 | 2.5 | 2.5 | 3.5 | 4.5 |
| 2026 | 1.6 | 4.5 | 2.5 | 2.5 | 3.5 | 4.5 |
</details>

Source: Bloomberg   
BofA GLOBAL RESEARCH

# Warsh & Fed balance sheet: all hat, almost no cattle

Kevin Warsh is now Senate confirmed as the new Fed Chair. A frequent client Q: "what will Warsh do on the Fed balance sheet?" Our A: "not much". We elaborate below.

Clients should focus on 2 aspects of Fed sheet: (1) size (2) composition. Size likely won't change much, composition will. We expect neither to matter much for markets.

Size: after Fed sheet normalized in Q4 '25, total size now determined by liabilities (Exhibit 1). The Fed has 3 big liabilities: (1) currency (2) TGA (3) reserves. Warsh will likely only be able to marginally move needle on reserve demand via liquidity de-reg.

Composition: Warsh will keep letting MBS reinvest in UST bills. He will likely accelerate Fed UST WAM reduction. UST unlikely to offset WAM impact, so market impact = nil.

Most important Q: Warsh reserve regime preference: ample or scarce? Our A: ample.

Blue sky: we propose new Fed regime with bank SRP=IOR. It could move needle.

Bottom line: Warsh impact on Fed B/S will be small & have minimal impact on markets.

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.

BofA does and seeks to do business with issuers covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

# 18 May 2026

Rates and Currencies Research Global

# Global Rates & Currencies Research MLI (UK)

# Mark Cabana, CFA

Rates Strategist

BofAS

+1 646 743 7013

mark.cabana@bofa.com

# Katie Craig

Rates Strategist

BofAS

+1 646 743 7016

katie.craig@bofa.com

# Oliver Levingston

FX and Rates Strategist

BofA (Hong Kong)

+852 3508 4631

oliver.levingston@bofa.com

See Team Page for List of Analysts

# Liquid Insight

Recent Publications

14-May-26 Global government bond supply update: same same, but different

13-May-26 Fading the USD Vibe-cession

12-May-26 Occam's razor applies in rates

11-May-26 US rates: hike risk underpriced

7-May-26 April jobs: Fed hike pricing in the balance

6-May-26 German 2027 draft budget – regular procedures, irregular budgets 06 May 2026

5-May-26 Dollar on mute

4-May-26 ECB balance sheet update

30-Apr-26 RBA preview: Front-loading as the path of least resistance

29-Apr-26 ECB preview: on hold, but not for long

BofA GLOBAL RESEARCH

# Warsh & Fed B/S: size & composition

Incoming Fed Chair Warsh is a longstanding critic of the Fed balance sheet. We expect he would quickly establish “working groups” to examine ways to shrink Fed sheet. Warsh will try to impact 2 parts of Fed B/S: (1) size (2) composition. Market impact likely small.

# Fed balance sheet size

Central bank balance sheet sizes, once right sized, are determined by their liabilities. The Fed right sized its sheet via QT until money markets reflected tightness in Q4 '25.

To reduce sheet further the Fed needs to shrink one of its key 3 liabilities: (1) currency (2) TGA (3) reserves. We offer thoughts (TL;DR: reserves are the only shot; Exhibit 2).

Exhibit 2: Fed balance sheet composition (\$bn)   
Fed assets = mostly UST assets, Fed liabilities = mostly reserves + currency 

<table><tr><td colspan="4">Assets</td><td colspan="6">Liabilities</td></tr><tr><td>Total</td><td>USTs</td><td>Agy MBS</td><td>Other</td><td>Reserves</td><td>Currency</td><td>UST Cash Balance</td><td>Foreign RRP</td><td>ON RRP</td><td>Other</td></tr><tr><td>6779.9</td><td>4450.2</td><td>1981.1</td><td>348.6</td><td>3117.4</td><td>2458.0</td><td>807.4</td><td>322.6</td><td>3.7</td><td>70.7</td></tr><tr><td>%</td><td>66%</td><td>29%</td><td>5%</td><td>46%</td><td>36%</td><td>12%</td><td>5%</td><td>0%</td><td>1%</td></tr></table>

Source: Bloomberg   
BofA GLOBAL RESEARCH

Currency: central banks believe currency is an “exogenous” liability. Exogenous liabilities are beyond the central banks control. To reduce currency the Fed could tax or eliminate currency / large denomination bills (ECB cut EUR500 notes). It won’t happen in the US.

TGA: UST cash balance could be reduced. UST has signaled minimal interest or desire to reduce TGA (TGA expected to rise: end Q2 \$900b, end Q3 \$950b). UST could consider marginal adjustments, such as excess cash investment in repo or TT&L (see: TGA repo investment & TT&L). TGA repo may happen but impact small. TT&L very unlikely.

Reserves: lower reserves are Warsh best shot to reduce sheet. There are 2 conventional ways for Warsh to reduce reserves (1) bank unfriendly (2) bank friendly.

Bank unfriendly: Warsh can tell banks that reserves are capped or tiered (tier = some reserves not fully paid IOR). Reserve caps or tiers would make banks sub-optimally liquid. Sub-optimally liquid banks likely less willing to take risk (i.e. less market making, less loan growth willingness). Less bank risk = slower economy. Warsh unlikely to do it.

Bank friendly: Warsh likely to pursue bank friendly ways to reduce reserve demand via de-reg. This will include allowing banks to pre-pledge collateral to Fed discount window for instant monetization. Pre-pledging collateral will expand bank HQLA. More HQLA = fewer reserves needed. We estimate reserve drop of \$200-500b (\~10% total) & slow.

Bank friendly approach will shift the “reserve demand curve”. Lower reserve demand will first put downward pressure on funding (Exhibit 3). Fed can later grow sheet slower / reduce sheet to normalize funding (Exhibit 4). Importantly, bank de-reg reserve demand drop will not tighten fin conditions (FCI). If no FCI tightening, no need for rate cuts.

Other: foreign repo pool adjustment is possible but small peas. Warsh could lower or cap foreign RRP rate to push cash out of Fed into repo or bills. We have long argued this would diminish USD reserve currency status & hurt national interest (see: RRP & national interest). Warsh may see smaller sheet > national interest. We advise otherwise.

Warsh will also likely have a high bar to intervene in disorderly markets. His initial intuition is likely to remain out of markets but could be forced to act depending on extent of market dysfunction (he did support Fed emergency actions post GFC). Warsh market invention bar will be high but not insurmountable depending on shock extent.

Size summary: Warsh likely to find Fed B/S reduction hard via conventional means. Best shot is via bank liquidity de-reg, impact modest & slow. Liquidity de-reg & initial funding ease will not justify Fed rate cuts. Blue sky may be more impactful or Fed B/S reduction.

Exhibit 3: Stylized Fed reserve demand and supply curves if reserve demand curve shifts left. If reserve demand curve shifts left due to de-reg, it will place downward pressure on funding rates   
![](images/17ff47130cbdee2ea5a8ca710f8d927d07c75aebe3bace9efa33d3ca3482d907.jpg)

<details>
<summary>line</summary>

| Reserve balances | Money market rates |
| ---------------- | ------------------ |
| R1               | TGCR current      |
| R1               | TGCR new           |
| R1               | Downward pressure on funding |
| R1               | IORB               |
</details>

Source: BofA Global Research. Note: Dark gray shaded area signifies "ample" reserves in current reserve demand environment, light gray in new reserve demand environment.   
BofA GLOBAL RESEARCH   
If funding rates decline, the Fed can reduce the supply of reserves and bring money market rates back up to IORB but maintain "ample" reserves

Exhibit 4: Stylized Fed reserve demand and supply curves if reserve demand curve shifts left and Fed reduces supply of reserves

![](images/3bf65640028215635f84797382f3c28ce9a9dc8b8dbc1f8c5fc298033f869c92.jpg)

<details>
<summary>line</summary>

| Reserve balances | Money market rates |
| ---------------- | ------------------ |
| R2               | TGCR new           |
| R1               | TGCR current       |
| IORB             | Fed reduces supply of reserves (upper) |
</details>

Source: BofA Global Research. Note: Dark gray shaded area signifies "ample" reserves in current reserve demand environment, light gray in new reserve demand environment.   
BofA GLOBAL RESEARCH

# Fed balance sheet composition

Warsh will also likely further adjust the composition of Fed assets in two ways (1) return to mostly Treasury portfolio (2) shorten WAM of Fed's UST holdings. Both are happening now. Warsh likely to speed WAM shortening, but it won't impact markets b/c mechanics.

Mostly UST portfolio: Fed is slowly reducing their \$2tn in MBS at a pace of \$10-\$20b/m by allowing maturing and prepaid MBS to roll-off & reinvest in T-bills. Fed unlikely to sell MBS (unless they were bought directly by Fannie or Freddie, which we see as low likelihood). Fed MBS roll-off practice to remain & is well priced by markets.

WAM: Fed is shortening WAM by purchasing T-bills via RMPs and MBS reinvestment (Exhibit 5). Warsh can speed Fed UST WAM reduction by shifting maturing coupon reinvestments into shorter-dated tenors (we assume 2-3y coupons in Exhibit 5). Warsh WAM shortening highly unlikely to see Fed asset sales. Market impact = small.

Market impact will be small due to WAM shortening mechanics. Recall, Fed UST coupon maturities are currently reinvested at auction into new-issue USTs. Fed reinvestment is proportional to UST auction amounts, thereby investing in-line with UST market. The Fed matches maturing USTs with USTs that settle on same day (i.e. mid-month maturities invested in 3/10/30Y USTs, end-month maturities invested in 2/5/7Y USTs).

Warsh will likely change this process by reinvesting in the shortest tenor new issue UST coupons. For example, in a mid-month settlement Fed will no longer rollover into 3/10/30Y issues but instead reinvest in all 3Y notes (example in Exhibit 6). Importantly, Fed reinvestments are an “add on” at auction. “Add on” means that the total size & composition of UST debt outstanding is increased by size of the Fed reinvestment.

The Fed's "add on" into 2 or 3Y notes will shorten WAM of total UST market. The key Q then becomes: will the US Treasury offset the mechanical UST WAM shortening from Fed reinvestments? Our A: no. If we are right, Fed WAM shortening has zero impact on UST market or fin conditions. No FCI impact = no reason for Warsh to cut rates.

Composition summary: Fed B/S composition changes are unlikely to matter for markets. The MBS maturity & reinvest practice already in place & priced. Fed shortening of their UST WAM will not have a market impact unless Bessent surprisingly offsets.

Exhibit 5: Fed WAM and WAM projection scenarios (months)   
Fed WAM has already started to decline due to RMPs and MBS reinvestments into T-bills but shifting coupon reinvestments into short-dated tenors would speed up this decline   
![](images/5b3fd81fb76e9452b28bac29f3a069f62215d9382711404275e6ab14e071f320.jpg)

<details>
<summary>line</summary>

| Year | Fed WAM | Current trend projection | 2y-3y reinvestment |
|------|---------|--------------------------|-------------------|
| 2004 | ~35     | -                        | -                 |
| 2008 | ~80     | -                        | -                 |
| 2012 | ~75     | -                        | -                 |
| 2016 | ~100    | -                        | -                 |
| 2020 | ~90     | -                        | -                 |
| 2024 | ~105    | ~100                     | ~100              |
| 2028 | -       | ~85                      | ~75               |
</details>

Source: BofA Global Research, FRBNY   
BofA GLOBAL RESEARCH

Exhibit 6: Stylized example of Fed reinvestment practice (\$bn)   
Fed current invests pro rata across curve, we expect this will be shortened 

<table><tr><td colspan="3">Current Practice</td><td colspan="3">Future Possible Practice</td></tr><tr><td colspan="3">UST Auction Size</td><td colspan="3">UST Auction Size</td></tr><tr><td>3Y</td><td>10Y</td><td>30Y</td><td>3Y</td><td>10Y</td><td>30Y</td></tr><tr><td>50</td><td>25</td><td>25</td><td>50</td><td>25</td><td>25</td></tr><tr><td colspan="3">Fed Maturing</td><td colspan="3">Fed Maturing</td></tr><tr><td></td><td>10</td><td></td><td></td><td>10</td><td></td></tr><tr><td colspan="3">Fed UST Auction Add On</td><td colspan="3">Fed UST Auction Add On</td></tr><tr><td>3Y</td><td>10Y</td><td>30Y</td><td>3Y</td><td>10Y</td><td>30Y</td></tr><tr><td>5</td><td>2.5</td><td>2.5</td><td>10</td><td>0</td><td>0</td></tr><tr><td colspan="3">UST Size Outstanding</td><td colspan="3">UST Size Outstanding</td></tr><tr><td>3Y</td><td>10Y</td><td>30Y</td><td>3Y</td><td>10Y</td><td>30Y</td></tr><tr><td>55</td><td>27.5</td><td>27.5</td><td>60</td><td>25</td><td>25</td></tr></table>

Source: BofA Global Research   
BofA GLOBAL RESEARCH

# Warsh big Q: ample or scarce? Our A: ample, all the way

Most important Warsh B/S Q (to us): does Warsh support ample or scarce reserves? Our A: ample. Recall, Fed definitions of ample & scarce, for a given move in reserves: ample = limited money market movement; scarce = large money market movement.

We strongly believe Warsh would support ample; if not, he would likely be forced to support it. Ample benefit = easy to implement, ensures banking system flush with cash, limits money market volatility, & supports modestly easier financial conditions. Ample cost = slightly larger balance sheet. Scarce benefits & costs are opposite of ample.

We expect Warsh will support ample because it underpins easy financial conditions. We believe Trump cares much more about easy financial conditions than size of Fed B/S. Warsh expected to have open ear for Trump policy preferences.

Warsh will likely be forced to accept ample by rest of Fed. The Fed formally adopted an ample reserve regime in 2019 and all members of Fed leadership support. Some are quite vocal & colorful in support. Specifically, Fed Governor Waller reportedly said in a NABE Feb '26 speech: "You don't want banks searching under sofa cushions for money every night... That is incredibly inefficient and stupid." Quote last word stands out to us.

Ample vs scarce summary: Warsh very likely to support ample.

# Blue sky: set bank SRP = IOR to reduce reserve buffer

Warsh will likely be looking for other ideas to reduce the balance sheet. We offer a novel approach, which Dallas Fed President Logan has previously referenced: bank SR

[中间内容因长度限制已省略]

rt containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.

# Research Analysts

# US

# Ralph Axel

Rates Strategist

BofAS

+1 646 743 7011

ralph.axel@bofa.com

# Paul Ciana, CMT

Technical Strategist

BofAS

+1 646 743 7014

paul.ciana@bofa.com

# John Shin

FX Strategist

BofAS

+1 646 855 2582

joong.s.shin@bofa.com

# Mark Cabana, CFA

Rates Strategist

BofAS

+1 646 743 7013

mark.cabana@bofa.com

# Bruno Braizinha, CFA

Rates Strategist

BofAS

+1 646 743 7012

bruno.braizinha@bofa.com

# Meghan Swiber, CFA

Rates Strategist

BofAS

+1 646 743 7020

meghan.swiber@bofa.com

# Europe

# Ralf Preusser, CFA

Rates Strategist

MLI (UK)

+44 20 7995 7331

ralf.preusser@bofa.com

# Ruben Segura-Cayuela

Europe Economist

BofA Europe (Madrid)

+34 91 514 3053

ruben.segura-cayuela@bofa.com

# Mark Capleton

Rates Strategist

MLI (UK)

+44 20 7995 6118

mark.capleton@bofa.com

# Sphia Salim

Rates Strategist

MLI (UK)

+44 20 7996 2227

sphia.salim@bofa.com

# Kamal Sharma

FX Strategist

MLI (UK)

+44 20 7996 4855

ksharma32@bofa.com

# Ronald Man

Rates Strategist

MLI (UK)

+44 20 7995 1143

ronald.man@bofa.com

# Michalis Rousakis

FX Strategist

MLI (UK)

+44 20 7995 0336

michalis.rousakis@bofa.com

# Pac Rim

# Adarsh Sinha

FX and Rates Strategist

MLI (UK)

+44 20 7995 9745

adarsh.sinha@bofa.com

# Janice Xue

Emerging Asia FI/FX Strategist

BofA (Hong Kong)

+852 3508 8587

janice.xue@bofa.com

# Shusuke Yamada, CFA

FX/Rates Strategist

BofAS Japan

+81 3 6225 8515

shusuke.yamada@bofa.com

Trading ideas and investment strategies discussed herein may give rise to significant risk and are not suitable for all investors. Investors should have experience in relevant markets and the financial resources to absorb any losses arising from applying these ideas or strategies.
"""
