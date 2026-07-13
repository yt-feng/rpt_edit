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
# BMW (BMWG.DE): 2Q26 preview: China drags but resilient US/Europe holds the Auto margin in the 1-3% guide; share buyback accelerates

Following BMW's release of 2Q26 retail volume and public pre-close call on July 10, in which the company confirmed the revised guidance from June 16 (link) and expects 2Q EBIT margins to be in line with the full-year range (1-3%), we slightly revise our estimates to reflect stronger US/Europe (+8%/+10% vs. previous GSe +2%/+2%), softer China volume (-30% vs. previous GSe -24%) and the split of Auto profitability. We now expect the company to report 2Q Group EPS of €1.72 (vs. Visible Alpha consensus €2.24) and Auto EBIT at €782mn or 2.9% margin (vs. VA cons €780mn or 2.8%). For FY26, we forecast an Auto margin at 2.6%, comprising a lower China JV margin (1.3%, cut from 2.3%) and a higher ex-JV margin (2.8%, raised from 2.7%). BMW is scheduled to report 2Q results on July 30.

Retail confirms the China-led weakness, with resilient offsets. 2Q retail volume came in at 591k units (-4.9% yoy), reflecting 2Q weakness in China and parts of Asia-Pacific, partly offset by growth in Europe and the US. Mini and the BMW iX3 posted solid 2Q deliveries, with the latter tracking toward 100k orders. Encouragingly, management continues to expect to meet 2026 CO2 targets without pooling, and is accelerating iX3 production capacity (a second shift pulled forward in Debrecen, with a third under consideration), further supported by the 7-Series and all-new X5 (Neue Klasse tech, five powertrains link).

2Q auto margin still free from restructuring burden, to hold within reset 1-3% corridor. On revenues, management pointed to a familiar set of pressures. Retail volume fell around 4.9%, with wholesale volumes down at a broadly similar rate, and pricing remained under pressure across many markets. On top of the volume and pricing weakness, the stronger Euro added a further drag on the reported top line. Walking down to EBIT, management confirmed that the 2Q margin will sit within the new 1-3% full-year corridor and anticipates headwinds from negative volume/mix/pricing, negative raw materials and currency effects, and a heavier D&A burden. Importantly, the restructuring costs will not impact the 2Q but land entirely in the 2H26, with the associated cash flow impact only coming through from 2027. Working the other way, cost reduction and tariff relief provide some support, but management was clear that these only partly offset the headwinds.

2Q Auto FCF positive but lower sequentially on working capital drag, share buyback acceleration provides balance sheet confidence. On cash, the picture follows naturally from the EBIT weakness. Auto free cash flow is squeezed by the

Christian Frenes  
+44(20)7051-8641 |  
christian.frenes@gs.com  
GS International

Monika Mengting Liu, CFA +44(20)7051-7601 | monika.liu@gs.com GS International

Shivam Kotecha +1(332)245-7822 | shivam.kotecha@gs.com GS India SPL

Robert Triulzi  
+44(20)7552-2281 | robert.triulzi@gs.com GS International

lower earnings and by a working-capital drag from inventory build-up amid iX3 and i3 launches, though depreciation and investment provide some cushion. The net result should still be positive free cash flow, but likely below the 1Q level. For FY26, we expect BMW to generate €3.1bn Auto FCF, well above the guidance floor of €2.5bn (VA cons €3.0bn). On capital return, the headline is that the share buyback has been accelerated by around five months versus the original plan (3rd tranch of the 3rd program in the amount of 625mn started on July 1 to be completed by Nov 30 instead of April 2027), which is a reassuring signal of balance-sheet confidence despite the earnings reset in our view.

2H26 carries risk from potential further China dealer support and the absence of Mexico/US tariff relief, though not impacting FY guide. Finally, on the various puts and takes: in China, a dealer support payment (in the low-triple-digit millions of Euros) is expected at the end of the 2Q, and while no further support is planned for the 2H, management is willing to consider it if needed without affecting full-year guidance. The IEEPA benefit, also in the low-triple-digit millions, will be booked in 2Q and roughly washes against the China dealer support. On trade, the anticipated reduction in the Mexico-to-US tariff from $27.5\%$ did not materialise, but this does not materially change guidance, according to management.

Exhibit 1: BMW estimate changes, new vs. old

<table><tr><td rowspan="2">€ mn</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td><td colspan="3">2029E</td><td colspan="3">2026-29E</td></tr><tr><td>New</td><td>Old</td><td>New vs. Old</td><td>New</td><td>Old</td><td>New vs. Old</td><td>New</td><td>Old</td><td>New vs. Old</td><td>New</td><td>Old</td><td>New vs. Old</td><td>New</td><td>Old</td><td>New vs. Old</td></tr><tr><td colspan="16">Revenues</td></tr><tr><td>Auto</td><td>110,419</td><td>111,878</td><td>-1.3%</td><td>110,603</td><td>112,041</td><td>-1.3%</td><td>113,420</td><td>114,898</td><td>-1.3%</td><td>115,795</td><td>117,311</td><td>-1.3%</td><td>450,237</td><td>456,128</td><td>-1.3%</td></tr><tr><td>Motorcycles</td><td>3,128</td><td>3,128</td><td>0.0%</td><td>3,175</td><td>3,175</td><td>0.0%</td><td>3,222</td><td>3,222</td><td>0.0%</td><td>3,271</td><td>3,271</td><td>0.0%</td><td>12,795</td><td>12,795</td><td>0.0%</td></tr><tr><td>Financial Services</td><td>39,814</td><td>39,814</td><td>0.0%</td><td>40,411</td><td>40,411</td><td>0.0%</td><td>41,017</td><td>41,017</td><td>0.0%</td><td>41,632</td><td>41,632</td><td>0.0%</td><td>162,874</td><td>162,874</td><td>0.0%</td></tr><tr><td>Reconciliation</td><td>-27,477</td><td>-27,738</td><td>0.9%</td><td>-27,625</td><td>-27,883</td><td>0.9%</td><td>-28,247</td><td>-28,512</td><td>0.9%</td><td>-28,792</td><td>-29,063</td><td>0.9%</td><td>-112,141</td><td>-113,197</td><td>0.9%</td></tr><tr><td>Total Revenue</td><td>125,883</td><td>127,081</td><td>-0.9%</td><td>126,563</td><td>127,744</td><td>-0.9%</td><td>129,412</td><td>130,626</td><td>-0.9%</td><td>131,906</td><td>133,150</td><td>-0.9%</td><td>513,765</td><td>518,601</td><td>-0.9%</td></tr><tr><td colspan="16">EBIT</td></tr><tr><td>Auto</td><td>2,870</td><td>2,936</td><td>-2.2%</td><td>4,493</td><td>4,547</td><td>-1.2%</td><td>5,425</td><td>5,492</td><td>-1.2%</td><td>5,921</td><td>5,994</td><td>-1.2%</td><td>18,709</td><td>18,969</td><td>-1.4%</td></tr><tr><td>Motorcycles</td><td>183</td><td>183</td><td>0.0%</td><td>175</td><td>175</td><td>0.0%</td><td>187</td><td>187</td><td>0.0%</td><td>196</td><td>196</td><td>0.0%</td><td>741</td><td>741</td><td>0.0%</td></tr><tr><td>Financial Services</td><td>2,006</td><td>2,006</td><td>0.0%</td><td>2,425</td><td>2,425</td><td>0.0%</td><td>2,461</td><td>2,461</td><td>0.0%</td><td>2,498</td><td>2,498</td><td>0.0%</td><td>9,390</td><td>9,390</td><td>0.0%</td></tr><tr><td>Reconciliation</td><td>381</td><td>384</td><td>-0.9%</td><td>567</td><td>572</td><td>-0.8%</td><td>646</td><td>651</td><td>-0.8%</td><td>689</td><td>695</td><td>-0.8%</td><td>2,283</td><td>2,302</td><td>-0.8%</td></tr><tr><td>Total EBIT</td><td>5,440</td><td>5,509</td><td>-1.3%</td><td>7,659</td><td>7,718</td><td>-0.8%</td><td>8,719</td><td>8,791</td><td>-0.8%</td><td>9,304</td><td>9,384</td><td>-0.8%</td><td>31,123</td><td>31,402</td><td>-0.9%</td></tr><tr><td colspan="16">EBIT Margin, %</td></tr><tr><td>Auto</td><td>2.6%</td><td>2.6%</td><td>0.0pp</td><td>4.1%</td><td>4.1%</td><td>0.0pp</td><td>4.8%</td><td>4.8%</td><td>0.0pp</td><td>5.1%</td><td>5.1%</td><td>0.0pp</td><td>4.2%</td><td>4.2%</td><td>0.0pp</td></tr><tr><td>Motorcycles</td><td>5.8%</td><td>5.8%</td><td>0.0pp</td><td>5.5%</td><td>5.5%</td><td>0.0pp</td><td>5.8%</td><td>5.8%</td><td>0.0pp</td><td>6.0%</td><td>6.0%</td><td>0.0pp</td><td>5.8%</td><td>5.8%</td><td>0.0pp</td></tr><tr><td>Financial Services</td><td>5.0%</td><td>5.0%</td><td>0.0pp</td><td>6.0%</td><td>6.0%</td><td>0.0pp</td><td>6.0%</td><td>6.0%</td><td>0.0pp</td><td>6.0%</td><td>6.0%</td><td>0.0pp</td><td>5.8%</td><td>5.8%</td><td>0.0pp</td></tr><tr><td>Group EBIT Margin</td><td>4.3%</td><td>4.3%</td><td>0.0pp</td><td>6.1%</td><td>6.0%</td><td>0.0pp</td><td>6.7%</td><td>6.7%</td><td>0.0pp</td><td>7.1%</td><td>7.0%</td><td>0.0pp</td><td>6.1%</td><td>6.1%</td><td>0.0pp</td></tr><tr><td colspan="16">Investments and Cash Flow</td></tr><tr><td>R&amp;D expenditure</td><td>6,973</td><td>7,039</td><td>-0.9%</td><td>5,316</td><td>5,365</td><td>-0.9%</td><td>5,824</td><td>5,878</td><td>-0.9%</td><td>6,595</td><td>6,658</td><td>-0.9%</td><td>24,708</td><td>24,940</td><td>-0.9%</td></tr><tr><td>Capital expenditure (PPE)</td><td>5,887</td><td>5,947</td><td>-1.0%</td><td>6,075</td><td>6,132</td><td>-0.9%</td><td>6,018</td><td>6,074</td><td>-0.9%</td><td>6,134</td><td>6,191</td><td>-0.9%</td><td>24,113</td><td>24,344</td><td>-0.9%</td></tr><tr><td>R&amp;D Capitalization</td><td>2,273</td><td>2,295</td><td>-0.9%</td><td>1,860</td><td>1,878</td><td>-0.9%</td><td>2,038</td><td>2,057</td><td>-0.9%</td><td>2,374</td><td>2,397</td><td>-0.9%</td><td>8,546</td><td>8,627</td><td>-0.9%</td></tr><tr><td>Capitalization Ratio</td><td>32.6%</td><td>32.6%</td><td>0.0%</td><td>35.0%</td><td>35.0%</td><td>0.0%</td><td>35.0%</td><td>35.0%</td><td>0.0%</td><td>36.0%</td><td>36.0%</td><td>0.0%</td><td>34.6%</td><td>34.6%</td><td>0.0%</td></tr><tr><td>Free Cash Flow Auto</td><td>3,102</td><td>3,139</td><td>-1.2%</td><td>4,418</td><td>5,041</td><td>-12.4%</td><td>5,529</td><td>5,542</td><td>-0.2%</td><td>5,336</td><td>5,627</td><td>-5.2%</td><td>18,385</td><td>19,350</td><td>-5.0%</td></tr><tr><td colspan="16">P&amp;L</td></tr><tr><td>Reported PBT</td><td>5,897</td><td>5,969</td><td>-1.2%</td><td>7,769</td><td>7,827</td><td>-0.7%</td><td>8,895</td><td>8,971</td><td>-0.8%</td><td>9,553</td><td>9,636</td><td>-0.9%</td><td>32,114</td><td>32,403</td><td>-0.9%</td></tr><tr><td>Tax</td><td>1,634</td><td>1,654</td><td>-1.2%</td><td>2,047</td><td>2,062</td><td>-0.7%</td><td>2,446</td><td>2,467</td><td>-0.8%</td><td>2,723</td><td>2,746</td><td>-0.9%</td><td>8,850</td><td>8,929</td><td>-0.9%</td></tr><tr><td>Reported net income</td><td>4,175</td><td>4,226</td><td>-1.2%</td><td>5,714</td><td>5,715</td><td>0.0%</td><td>6,608</td><td>6,617</td><td>-0.1%</td><td>7,168</td><td>7,178</td><td>-0.1%</td><td>23,665</td><td>23,737</td><td>-0.3%</td></tr><tr><td>EPS</td><td>7.01</td><td>7.13</td><td>-1.7%</td><td>10.10</td><td>10.17</td><td>-0.7%</td><td>12.22</td><td>12.32</td><td>-0.8%</td><td>13.99</td><td>14.20</td><td>-1.5%</td><td>43.32</td><td>43.81</td><td>-1.1%</td></tr><tr><td>Dividend</td><td>2.90</td><td>2.90</td><td>0.0%</td><td>3.60</td><td>3.60</td><td>0.0%</td><td>4.30</td><td>4.40</td><td>-2.3%</td><td>4.90</td><td>5.00</td><td>-2.0%</td><td>15.70</td><td>15.90</td><td>-1.3%</td></tr><tr><td>Group deliveries, wholesale</td><td>2,371,812</td><td>2,354,690</td><td>0.7%</td><td>2,363,320</td><td>2,345,421</td><td>0.8%</td><td>2,409,876</td><td>2,391,661</td><td>0.8%</td><td>2,446,944</td><td>2,428,600</td><td>0.8%</td><td>9,591,952</td><td>9,520,373</td><td>0.8%</td></tr></table>

Source: GS Global Investment Research

Exhibit 2: GSe vs. Visible Alpha Consensus Data

<table><tr><td rowspan="2">€ mn</td><td colspan="3">2Q26E</td><td colspan="3">2026E</td><td colspan="3">2027E</td><td colspan="3">2028E</td><td colspan="3">2029E</td><td colspan="3">2020-203E</td></tr><tr><td>GSe</td><td>Cons</td><td>GSe vs. Cons</td><td>GSe</td><td>Cons</td><td>GSe vs. Cons</td><td>GSe</td><td>Cons</td><td>GSe vs. Cons</td><td>GSe</td><td>Cons</td><td>GSe vs. Cons</td><td>GSe</td><td>Cons</td><td>GSe vs. Cons</td><td>GSe</td><td>Cons</td><td>GSe vs. Cons</td></tr><tr><td colspan="19">Revenues</td></tr><tr><td>Auto</td><td>27,128</td><td>28,185</td><td>-3.7%</td><td>110,419</td><td>113,601</td><td>-2.8%</td><td>110,603</td><td>116,784</td><td>-5.3%</td><td>113,420</td><td>119,288</td><td>-4.9%</td><td>115,795</td><td>121,114</td><td>-4.4%</td><td>450,237</td><td>470,787</td><td>-4.4%</td></tr><tr><td>Motorcycles</td><td>966</td><td>954</td><td>1.3%</td><td>3,128</td><td>3,152</td><td>-0.8%</td><td>3,175</td><td>3,216</td><td>-1.3%</td><td>3,222</td><td>3,281</td><td>-1.8%</td><td>3,271</td><td>3,365</td><td>-2.8%</td><td>12,795</td><td>13,014</td><td>-1.7%</td></tr><tr><td>Financial Services</td><td>10,078</td><td>9,941</td><td>1.4%</td><td>39,814</td><td>39,697</td><td>0.3%</td><td>40,411</td><td>40,757</td><td>-0.8%</td><td>41,017</td><td>41,694</td><td>-1.6%</td><td>41,632</td><td>42,547</td><td>-2.2%</td><td>162,874</td><td>164,696</td><td>-1.1%</td></tr><tr><td>Reconciliation</td><td>-6,839</td><td>-6,428</td><td>-6.4%</td><td>-27,477</td><td>-26,296</td><td>-4.5%</td><td>-27,625</td><td>-26,697</td><td>-3.5%</td><td>-28,247</td><td>-27,239</td><td>-3.7%</td><td>-28,792</td><td>-27,459</td><td>-4.9%</td><td>-112,141</td><td>-107,691</td><td>-4.1%</td></tr><tr><td>Total Revenue</td><td>31,333</td><td>32,562</td><td>-3.8%</td><td>125,883</td><td>130,077</td><td>-3.2%</td><td>126,563</td><td>134,385</td><td>-5.8%</td><td>129,412</td><td>137,672</td><td>-6.0%</td><td>131,906</td><td>139,680</td><td>-5.6%</td><td>513,765</td><td>541,814</td><td>-5.2%</td></tr><tr><td colspan="19">EBIT</td></tr><tr><td>Auto</td><td>782</td><td>780</td><td>0.3%</td><td>2,870</td><td>3,122</td><td>-8.1%</td><td>4,493</td><td>5,043</td><td>-10.9%</td><td>5,425</td><td>6,207</td><td>-12.6%</td><td>5,921</td><td>6,920</td><td>-14.4%</td><td>18,709</td><td>21,292</td><td>-12.1%</td></tr><tr><td>Motorcycles</td><td>39</td><td>113</td><td>-65.7%</td><td>183</td><td>174</td><td>5.3%</td><td>175</td><td>182</td><td>-4.3%</td><td>187</td><td>199</td><td>-6.3%</td><td>196</td><td>219</td><td>-10.3%</td><td>741</td><td>774</td><td>-4.4%</td></tr><tr><td>Financial Services</td><td>561</td><td>608</td><td>-7.7%</td><td>2,006</td><td>2,187</td><td>-8.3%</td><td>2,425</td><td>2,370</td><td>2.3%</td><td>2,461</td><td>2,561</td><td>-3.9%</td><td>2,498</td><td>2,806</td><td>-11.0%</td><td>9,390</td><td>9,925</td><td>-5.4%</td></tr><tr><td>Reconciliation</td><td>69</td><td>265</td><td>-73.9%</td><td>381</td><td>886</td><td>-57.1%</td><td>567</td><td>714</td><td>-20.5%</td><td>646</td><td>565</td><td>14.2%</td><td>689</td><td>669</td><td>2.9%</td><td>2,283</td><td>2,835</td><td>-19.5%</td></tr><tr><td>Total EBIT</td><td>1,451</td><td>1,733</td><td>-16.3%</td><td>5,440</td><td>6,276</td><td>-13.3%</td><td>7,659</td><td>8,323</td><td>-8.0%</td><td>8,719</td><td>9,906</td><td>-12.0%</td><td>9,304</td><td>10,739</td><td>-13.4%</td><td>31,123</td><td>35,244</td><td>-11.7%</td></tr><tr><td colspan="19">EBIT Margin, %</td></tr><tr><td>Auto</td><td>2.9%</td><td>2.8%</td><td>0.1%</td><td>2.6%</td><td>2.7%</td><td>-0.1pp</td><td>4.1%</td><td>4.3%</td><td>-0.3pp</td><td>4.8%</td><td>5.2%</td><td>-0.4pp</td><td>5.1%</td><td>5.7%</td><td>-0.6pp</td><td>4.2%</td><td>4.5%</td><td>-0.4pp</td></tr><tr><td>Motorcycles</td><td>4.0%</td><td>11.8%</td><td>-7.8%</td><td>5.8%</td><td>5.5%</td><td>0.3pp</td><td>5.5%</td><td>5.7%</td><td>-0.2pp</td><td>5.8%</td><td>6.1%</td><td>-0.3pp</td><td>6.0%</td><td>6.5%</td><td>-0.5pp</td><td>5.8%</td><td>6.0%</td><td>-0.2pp</td></tr><tr><td>Financial Services</td><td>5.6%</td><td>6.1%</td><td>-0.6%</td><td>5.0%</td><td>5.5%</td><td>-0.5pp</td><td>6.0%</td><td>5.8%</td><td>0.2pp</td><td>6.0%</td><td>6.1%</td><td>-0.1pp</td><td>6.0%</td><td>6.6%</td><td>-0.6pp</td><td>5.8%</td><td>6.0%</td><td>-0.3pp</td></tr><tr><td>Group EBIT Margin</td><td>4.6%</td><td>5.3%</td><td>-0.7%</td><td>4.3%</td><td>4.8%</td><td>-0.5pp</td><td>6.1%</td><td>6.2%</td><td>-0.1pp</td><td>6.7%</td><td>7.2%</td><td>-0.5pp</td><td>7.1%</td><td>7.7%</td><td>-0.6pp</td><td>6.1%</td><td>6.5%</td><td>-0.4pp</td></tr><tr><t

[中间内容因长度限制已省略]

es, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

© 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
