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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Commodity Market Positioning & Flows

Agri and precious metals drive global commodity open interest decline

- The estimated value of open interest across tracked commodity markets decreased by 1% WoW (\$14 billion) to \$1.8 trillion, falling for three consecutive weeks (as of 5 Jun) (Table 2, Figure 2). The decline was led by agri and precious metals markets as prices across grains & oilseeds and gold & silver fell sharply over the week, driving the overall open interest decline even as total net contract-based flows were supported by inflows into metals. On the macro front, our economists see the strong US employment report as reinforcing their view that a cyclical lift in global business spending is now broadening to hiring in a manner that will cushion the energy price drag on household purchasing power. Meanwhile, the combination of a cyclical lift alongside sticky and elevated inflation furthers the case for a Fed hike ahead (Global Data Watch: Yes, and it counts, Kasman et al, 5 June 2026).  
- The estimated value of net investor positioning aggregated across global commodity futures markets remained broadly flat WoW at \$223 billion as of the latest data available (Table 1, Figure 3, Figure 4). Net length in energy markets decreased by \$7.7 billion WoW, as investors cut length across Brent and Dubai crude oil benchmarks and across TTF Natgas. Net length in precious metals increased by \$10 billion WoW and net length in base metals increased by \$2 billion WoW, led by gold and copper respectively. Net length in agri markets decreased by \$6 billion WoW led by a decline in grains & oilseeds. JPM QDS's latest projections, as of June 8, indicate that positioning across commodity markets is expected to decline further by nearly \$15 billion, primarily from a decline in agri (-\$10 billion) and precious metals markets (-\$3 billion).  
- The Global Commodities Inventory Monitor (GCIM) remained broadly stable in May at 69.4 days-of-use. On an ex-China basis—which is a proxy for globally tradeable inventories—the monitor also remained stable in May at 58.6 days-of-use. Across the GCIM, rising US natural gas availability was offset by declines across oil and aluminum availability. Agri availability was largely stable across both monitors over the month. Stripping out the seasonal impact of US natural gas storage, GCIM through May remained broadly stable at 73.2 days-of-use. Ex-China commodity availability (ex US natural gas) also stabilized at 64.7 days-of-use in May. Across the GCIM (ex-US natural gas), inventory availability only rose for lead, zinc and nickel.  
- The estimated value of open interest in energy markets remained broadly flat WoW at \$819 billion (5 Jun, Figure 6) as the decline in the open interest across the crude oil markets was more than offset by an increase across the petroleum products and natural gas markets. The estimated value of open interest across the crude oil and petroleum products markets declined by \$3 billion, driven by net contract-based outflows of \$10 billion from crude oil markets, partially offset by an increase in prices across crude oil (NYM WTI up 4% WoW) and petroleum products markets (ICE Gas Oil up 5% WoW). Our base case assumes the Strait of Hormuz reopens in June,

## Global Commodities Research

## Otar Dgebuadze, CFA

(44-20) 3493-8246

otar.dgebuadze@JPM.com

JPM Securities plc

## Natasha Kaneva

(1-212) 834-3175

natasha.kaneva@JPM.com

JPM Chase Bank NA

## Gregory C. Shearer

(44-20) 7134-8161

gregory.c.shearer@JPM.com

JPM Securities plc

## Tracey Allen

(44-20) 7134-6732

tracey.l.allen@JPM.com

JPM Securities plc

## Ali A. Ibrahim

(44-20) 3493-6438

ali.ibrahim@JPM.com

JPM Securities plc

## Aradhaya Makkar

aradhaya.makkar@jpmchase.com

JPM India Private Limited

## Ananyashree Gupta

(91-22) 6157 3627

ananyashree.gupta@jpmchase.com

JPM India Private Limited

keeping Brent near \$100 for the rest of the year, with sub-\$100 monthly averages only late in 2026. However, we note that if the Strait stays closed, each extra month would materially lift prices (roughly +\$5 for 2026 and +\$15 in 4Q26), as inventories deplete further. The estimated value of open interest in natural gas markets increased by 3% over the week to \$6 billion (5 Jun, Figure 13). This was driven by an increase in prices across European and Asian benchmarks (TTF up 4% WoW), further supported by net contract-based inflows of \$2.3 billion across all trader types. We note that ADNOC's Mubaraz—the first laden LNG tanker to exit the Strait of Hormuz on April 26—re-entered the Strait on June 3. Despite these sporadic movements, only nine LNG vessels are currently inside the Strait, so exports remain capped until a full reopening. Beyond these cargoes, volumes will need to come from renewed upstream and liquefaction operations (as well as normalizing port logistics).

- The estimated value of open interest in precious metals markets decreased by 3% WoW (\$7.2 billion WoW) to \$257 billion, continuing on a multi-week decline (5 Jun, Figure 8). Across all trader types, the sector saw net contract-based inflows totalling \$5.4 billion WoW, mostly into gold (\$2.4 billion WoW) and silver (\$2.7 billion WoW). While, Managed Money positioning in COMEX Gold futures (as of 2 Jun) rose by 14.7k contracts to \~112k contracts net long. Gold prices have faced selling pressure amid a rates repricing across forward rates markets, and since the start of the Middle East conflict, gold prices have declined by 18%, with further downside risks if the Fed turns more hawkish on strong employment data and potentially higher inflation.  
- The estimated value of open interest in base metals markets remained broadly flat WoW at \$239 billion (5 Jun, Figure 9). The sector saw net contract-based inflows across all trader types reaching \$2 billion over the week, which were concentrated in nickel (\$1.2 billion WoW) and copper (\$0.9 billion WoW). With the US tariff review forthcoming, interest has turned back to the COMEX/LME arb dynamics. Later this month, by June 30, 2026, the US Commerce Secretary is to provide the President with an update on whether additional Section 232 copper tariff modifications are necessary. Our view remains that it is more likely than not that the Trump administration will enact an escalating tariff as was laid out in last July's original executive order (i.e. starting at 15% in 2027, increasing to 30% a year later) to 1) ensure that all the copper that has already been imported into the US stays onshore and 2) keep this excess US inventory as a critical reserve, rather than enact policy which incentivizes it to quickly destock in the coming years. A continued strong import pull into the US in the coming quarters would continue to strain ex-US cathode supply, particularly over periods where China's import arb is also open.  
- The estimated value of open interest across environmental markets decreased by 4% WoW to \$73 billion (5 Jun, Figure 7). This was driven by a 6% decline in the EUA prices over the week, while net contract-based flows were positive at \$1.4 billion, primarily into EUAs. Investment Funds increased their net long position across EUAs as of 29 May to 51.2k lots, up by 12.2k lots WoW.  
- The estimated value of open interest in agricultural markets decreased by 3% WoW to \$382 billion (5 Jun, Figure 10, Figure 14). This decline in OI was largely driven by sharp declines in prices across grains & oilseeds markets. Across all trader types, net contract-based inflows were \$1.2 billion WoW, as outflows from grains & oilseeds (-\$1.6 billion WoW) and livestock (-\$2 billion WoW) were more than offset by inflows into soft markets (\$4.8 billion WoW).  
- Price momentum largely decreased across most of the complex over the week (5 Jun, Figure 17, Figure 18). The long-term momentum trading signal on Kansas Wheat, CBOT Soybeans and ICE Cotton switched negative to a ‘sell’ signal during the week. The short-term momentum trading signal on TTF switched to ‘buy’, while the signal on LME Nickel switched to ‘sell’ during the week. Meanwhile, the short-term price momentum trading signals on CMX Gold, CMX Silver, NYM Platinum, NYM

Palladium and ICE NY Cocoa exceeded their respective extreme-negative thresholds, indicating a potential trend exhaustion.

See Agricultural Commodities CFTC COT Report for relevant supplemental data across agricultural markets.

Table 1: Net investor positioning across tracked commodity markets  
USD million

<table><tr><td rowspan="2"></td><td rowspan="2"># of markets /Last reported date</td><td rowspan="2">Lastreportedvalue</td><td rowspan="2">Latestprojection08-Jun-26</td><td rowspan="2">Projectionvs lastreported</td><td colspan="4">Change in Positioning (reported)</td></tr><tr><td>1 Week</td><td>1 Month</td><td>3 Months</td><td>2026 YTD</td></tr><tr><td>Total Commodities</td><td>33</td><td>222,799</td><td>208,067</td><td>-14,732</td><td>201</td><td>-17,081</td><td>9,726</td><td>29,310</td></tr><tr><td>Energy</td><td>8</td><td>35,437</td><td>34,451</td><td>-985</td><td>-7,771</td><td>-12,914</td><td>1,044</td><td>36,725</td></tr><tr><td>Crude Oil</td><td>3</td><td>44,128</td><td>43,261</td><td>-866</td><td>-7,064</td><td>-15,607</td><td>2,397</td><td>30,247</td></tr><tr><td>ICE Brent</td><td>2-Jun-26</td><td>17,585</td><td>17,250</td><td>-334</td><td>-4,259</td><td>-13,165</td><td>13,921</td><td>22,658</td></tr><tr><td>NYMEX WTI</td><td>2-Jun-26</td><td>14,615</td><td>14,083</td><td>-532</td><td>-501</td><td>-3,670</td><td>-4,413</td><td>10,819</td></tr><tr><td>ICE Dubai</td><td>2-Jun-26</td><td>11,929</td><td>na</td><td>na</td><td>-2,304</td><td>1,228</td><td>-7,111</td><td>-3,230</td></tr><tr><td>Petroleum Products</td><td>3</td><td>-16,924</td><td>-17,060</td><td>-136</td><td>1,066</td><td>5,358</td><td>-3,070</td><td>-11,077</td></tr><tr><td>NYMEX Gasoline</td><td>2-Jun-26</td><td>7,345</td><td>7,278</td><td>-67</td><td>-43</td><td>-1,610</td><td>-744</td><td>1,994</td></tr><tr><td>ICE Gasoil</td><td>2-Jun-26</td><td>-24,905</td><td>na</td><td>na</td><td>880</td><td>7,295</td><td>-1,124</td><td>-12,090</td></tr><tr><td>NYMEX Heat Oil</td><td>2-Jun-26</td><td>636</td><td>567</td><td>-68</td><td>229</td><td>-327</td><td>-1,202</td><td>-981</td></tr><tr><td>Natural Gas</td><td>2</td><td>8,233</td><td>8,250</td><td>17</td><td>-1,772</td><td>-2,665</td><td>1,717</td><td>17,555</td></tr><tr><td>NYMEX Natgas</td><td>2-Jun-26</td><td>-5,894</td><td>-5,877</td><td>17</td><td>-14</td><td>-1,248</td><td>-251</td><td>345</td></tr><tr><td>TTF Natgas</td><td>29-May-26</td><td>14,127</td><td>na</td><td>na</td><td>-1,758</td><td>-1,417</td><td>1,968</td><td>17,210</td></tr><tr><td>Environmental</td><td>2</td><td>6,743</td><td>6,743</td><td>0</td><td>1,488</td><td>2,158</td><td>1,292</td><td>-7,204</td></tr><tr><td>EUA</td><td>29-May-26</td><td>4,992</td><td>na</td><td>na</td><td>1,342</td><td>1,791</td><td>586</td><td>-7,271</td></tr><tr><td>UKA</td><td>29-May-26</td><td>1,751</td><td>na</td><td>na</td><td>146</td><td>368</td><td>706</td><td>67</td></tr><tr><td>Metals</td><td>10</td><td>145,164</td><td>141,390</td><td>-3,774</td><td>12,229</td><td>11,820</td><td>6,492</td><td>-21,669</td></tr><tr><td>Precious</td><td>4</td><td>89,453</td><td>86,575</td><td>-2,878</td><td>10,200</td><td>4,581</td><td>-8,625</td><td>-27,199</td></tr><tr><td>CMX Gold</td><td>2-Jun-26</td><td>79,017</td><td>77,093</td><td>-1,924</td><td>9,565</td><td>4,412</td><td>-6,498</td><td>-23,815</td></tr><tr><td>CMX Silver</td><td>2-Jun-26</td><td>9,039</td><td>8,509</td><td>-529</td><td>560</td><td>305</td><td>-1,909</td><td>-2,839</td></tr><tr><td>NYMX Platinum</td><td>2-Jun-26</td><td>1,672</td><td>1,271</td><td>-401</td><td>-51</td><td>-84</td><td>31</td><td>-370</td></tr><tr><td>NYMX Palladium</td><td>2-Jun-26</td><td>-275</td><td>-299</td><td>-24</td><td>126</td><td>-52</td><td>-249</td><td>-175</td></tr><tr><td>Base</td><td>6</td><td>55,711</td><td>54,814</td><td>-896</td><td>2,030</td><td>7,239</td><td>15,117</td><td>5,530</td></tr><tr><td>CMX Copper</td><td>2-Jun-26</td><td>13,158</td><td>12,262</td><td>-896</td><td>1,543</td><td>3,820</td><td>5,532</td><td>4,387</td></tr><tr><td>LME Copper</td><td>5-Jun-26</td><td>15,629</td><td>na</td><td>na</td><td>1,359</td><td>586</td><td>5,704</td><td>-6,725</td></tr><tr><td>LME Aluminum</td><td>5-Jun-26</td><td>18,715</td><td>na</td><td>na</td><td>-872</td><td>1,428</td><td>1,506</td><td>4,623</td></tr><tr><td>LME Zinc</td><td>5-Jun-26</td><td>4,143</td><td>na</td><td>na</td><td>0</td><td>820</td><td>646</td><td>1,478</td></tr><tr><td>LME Nickel</td><td>5-Jun-26</td><td>4,188</td><td>na</td><td>na</td><td>0</td><td>-174</td><td>749</td><td>1,290</td></tr><tr><td>LME Lead</td><td>5-Jun-26</td><td>-123</td><td>na</td><td>na</td><td>0</td><td>758</td><td>980</td><td>477</td></tr><tr><td>Agriculture</td><td>13</td><td>35,455</td><td>25,483</td><td>-9,972</td><td>-5,746</td><td>-18,146</td><td>898</td><td>21,458</td></tr><tr><td>Grains</td><td>6</td><td>25,908</td><td>17,824</td><td>-8,084</td><td>-4,175</td><td>-10,325</td><td>207</td><td>22,015</td></tr><tr><td>CBT Corn</td><td>2-Jun-26</td><td>4,404</td><td>2,349</td><td>-2,055</td><td>-2,505</td><td>-5,683</td><td>-1,219</td><td>3,216</td></tr><tr><td>CBT Wheat</td><td>2-Jun-26</td><td>-1,229</td><td>-1,226</td><td>3</td><td>-928</td><td>-715</td><td>-376</td><td>610</td></tr><tr><td>KBT Wheat</td><td>2-Jun-26</td><td>-286</td><td>-322</td><td>-37</td><td>-227</td><td>-772</td><td>-466</td><td>-238</td></tr><tr><td>CBT Soy beans</td><td>2-Jun-26</td><td>10,941</td><td>7,286</td><td>-3,655</td><td>-1,196</td><td>-2,942</td><td>-2,729</td><td>4,479</td></tr><tr><td>CBT Soy Meal</td><td>2-Jun-26</td><td>5,095</td><td>3,774</td><td>-1,321</td><td>15</td><td>749</td><td>2,002</td><td>5,166</td></tr><tr><td>CBT Soy Oil</td><td>2-Jun-26</td><td>6,983</td><td>5,964</td><td>-1,020</td><td>667</td><td>-961</td><td>2,995</td><td>8,783</td></tr><tr><td>Softs</td><td>4</td><td>2,146</td><td>1,040</td><td>-1,106</td><td>-978</td><td>-2,719</td><td>5,206</td><td>2,016</td></tr><tr><td>ICE Cotton</td><td>2-Jun-26</td><td>3,282</td><td>2,761</td><td>-521</td><td>-110</td><td>-869</td><td>3,969</td><td>4,292</td></tr><tr><td>ICE Sugar</td><td>2-Jun-26</td><td>-1,726</td><td>-1,959</td><td>-233</td><td>-427</td><td>-82</td><td>1,636</td><td>597</td></tr><tr><td>ICE Coffee</td><td>2-Jun-26</td><td>1,301</td><td>987</td><td>-315</td><td>-408</td><td>-1,867</td><td>-388</td><td>-1,967</td></tr><tr><td>ICE Cocoa</td><td>2-Jun-26</td><td>-711</td><td>-748</td><td>-37</td><td>-34</td><td>99</td><td>-11</td><td>-905</td></tr><tr><td>Livestock</td><td>3</td><td>7,401</td><td>6,619</td><td>-782</td><td>-592</td><td>-5,103</td><td>-4,515</td><td>-2,573</td></tr><tr><td>CME Live Cattle</td><td>2-Jun-26</td><td>8,473</td><td>8,241</td><td>-231</td><td>-149</td><td>-2,033</td><td>906</td><td>1,141</td></tr><tr><td>CME Lean Hogs</td><td>2-Jun-26</td><td>-1,418</td><td>-1,849</td><td>-431</td><td>-511</td><td>-1,658</td><td>-4,320</td><td>-2,851</td></tr><tr><td>CME Feeder Cattle</td><td>2-Jun-26</td><td>347</td><td>226</td><td>-120</td><td>67</td><td>-1,412</td><td>-1,101</td><td>-863</td></tr></table>

<table><tr><td>Total Regions</td><td>33</td><td>222,799</td><td>208,067</td><td>-14,732</td><td>201</td><td>-17,081</td><td>9,726</td><td>29,310</td></tr><tr><td>US</td><td>22</td><td>154,768</td><td>140,371</td><td>-14,397</td><td>5,667</td><td>-16,600</td><td>-8,805</td><td>10,822</td></tr><tr><td>UK</td><td>9</td><td>48,912</td><td>48,577</td><td>-334</td><td>-5,050</td><td>-855</td><td>15,977</td><td>8,549</td></tr><tr><td>EU</td><td>2</td><td>19,119</td><td>19,119</td><td>0</td><td>-416</td><td>374</td><td>2,555</td><td>9,939</td></tr></table>

Where projections are not available, latest reported values are used for totals  
Projections by JPM QDS Research; US exchanges data is an aggregate of Managed Money and Other Reportables, European exchanges data is an aggregate of Investment Funds and Other Financial Firms.  
Source: Exchange data, Bloomberg Finance L.P., JPM QDS and Commodities Research

Table 2: The estimated value of commodity market open interest across major global exchanges reached \$1.8 trillion in the week ending 5 June USD million

<table><tr><td rowspan="2">Sector</td><td>Number of futures markets</td><td>Total estimated Open Interest</td><td colspan="4">Change in Open Interest</td><td colspan="4">Cumulative flows</td><td colspan="5">Tracked Open Interest by location of exchange (% of global total)</td></tr><tr><td>Count</td><td>05-Jun-26</td><td>1 Week</td><td>1 Month</td><td>3 Months</td><td>2026 YTD</td><td>1 Week</td><td>1 Month</td><td>3 Months</td><td>2026 YTD</td><td>US</td><td>UK</td><td>EU</td><td>China</td><td>RoW</td></tr><tr><td>Total commodities</td><td>91</td><td>1,808,828</td><td>-13,730</td><td>-80,048</td><td>-180,735</td><td>102,617</td><td>7,343</td><td>-19,518</td><td>-142,413</td><td>-204,717</td><td>45%</td><td>32%</td><td>9%</td><td>13%</td><td>1%</td></tr><tr><td>Energy</td><td>18</td><td>819,069</td><td>2,591</td><td>-36,045</td><td>-109,644</td><td>158,432</td><td>-7,103</td><td>-16,557</td><td>-97,374</td><td>-120,378</td><td>36%</td><td>50%</td><td>9%</td><td>1%</td><td>0%</td></tr><tr><td>Crude Oil</td><td>7</td><td>484,142</td><td>-7,208</td><td>-31,492</td><td>-83,536</td><td>105,517</td><td>-10,584</td><td>-14,486</td><td>-66,504</td><td>-64,185</td><td>33%</td><td>65%</td><td>0%</td><td>1%</td><td>0%</td></tr><tr><td>Petroleum Products</td><td>7</td><td>154,021</td><td>4,100</td><td>-12,913</td><td>-20,151</td><td>27,987</td><td>1,159</td><td>-4,912</td><td>-28,852</td><td>-46,640</td><td>48%</td><td>51%</td><td>0%</td><td>1%</td><td>0%</td></tr><tr><td>Natural Gas</td><td>4</td><td>180,906</td><td>5,699</td><td>8,360</td><td>-5,957</td><td>24,928</td><td>2,322</td><td>2,842</td><td>-2,018</td><td>-9,552</td><td>32%</td><td>9%</td><td>42%</td><td>0%</td><td>0%</td></tr><tr><td>Environmental</td><td>3</td><td>72,722</td><td>-2,951</td><td>4,307</td><td>8,819</td><td>1,096</td><td>1,430</td><td>4,001</td><td>540</td><td>12,623</td><td>0%</td><td>0%</td><td>100%</td><td>0%</td><td>0%</td></tr><tr><td>EU Allowances</td><td>2</td><td>68,262</td><td>-2,695</td><td>3,736</td><td>7,670</td><td>1,275</td><td>1,395</td><td>3,779</td><td>660</td><td>11,700</td><td>0%</td><td>0%</td><td>100%</td><td>0%</td><td>0%</td></tr><tr><td>UK ETS</td><td>1</td><td>4,459</td><td>-256</td><td>571</td><td>1,148</td><td>-179</td><td>34</td><td>222<

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 09 Jun 2026 06:09 PM BST

Disseminated 09 Jun 2026 06:09 PM BST
"""
