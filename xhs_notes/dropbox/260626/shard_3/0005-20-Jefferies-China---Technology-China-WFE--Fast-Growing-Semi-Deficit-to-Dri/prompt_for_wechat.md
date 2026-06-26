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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`JEF`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JEF研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## China WFE: Fast-Growing Semi Deficit to Drive Strong WFE Capex

China's May SPE/WFE imports fell 9%/12%, but testing/packaging grew 25%/19%. Positively, WFE's fall is entirely driven by a 32% decline in etching, as deposition/ion implanting grew 12%/21%. Fall in etching is associated with a 28%/58% fall in WFE imports from Japan/Malaysia. YTD, WFE imports fell 12%, driven by 24%/18% fall in litho/etching, while imports from Japan/Netherlands dropped the most, by 28%/24%. We still expect 2026 WFE capex to fall LSD to MSD.

China's WFE imports fell 12% in May, worse than previous two months, but it is narrow-based. China's May SPE imports fell 9%, driven mainly by 12% decline in WFE. Packaging imports grew 8% YTD, the only category with positive growth. We highlighted before Huawei's "Tau" scaling law is based on advanced packaging, and China does not face any restrictions on packaging tools. Therefore, we expect this to be a strong growth area in the next 12-24 months. For WFE, even though the 12% fall in May is a deterioration from 6%/3% decline in Apr/Mar, we are encouraged that May's fall is narrow-based. It is almost entirely driven by a 24% fall in etching. Deposition and ion implanting grew 12% and 21%, respectively, while litho imports were flattish. YTD, WFE imports fell 12%, driven mainly by 24%/18% decline in litho/etching. Deposition and thermal YTD both grew 3%. We believe the YTD weakness is due to 1) CXMT slowing after big pull-in last year and likely waiting for any sign of relaxation of US restrictions and 2) decline in advanced logic due to pull in last year and very long delivery lead time of critical tools in the grey market. We remain confident of some demand recovery in 2H26, leading to low-single-digit (LSD) to mid-single digit (MSD) growth in WFE capex for the full year. We believe memory capex will be the key driver in 2H26.

Singapore has become the largest source of WFE imports for China. It is worth noting the 32% decline in May etching imports coincided with a 58%/28% fall, in WFE imports from Malaysia/Japan. We saw the same trend for the Apr data. It suggests etching tools that China buys are mainly coming from these two countries. YTD, imports of Japan and the Netherlands fell the most (24%/28%) while imports from Singapore and Taiwan rose 45% and 22%, respectively. In fact, Singapore and Taiwan are the only countries that show positive growth YTD for WFE imports into China. Singapore has overtaken Japan as the largest source of WFE imports into China (5M26), with a 25% import share. Japan ranked No. 2 with 23% share, while the Netherlands' share has fallen to No. 3 at 18%.

Rapidly rising semi trade deficit will drive strong long-term WFE capex growth. China's semiconductor imports grew 71% in May, a new high. Semiconductor imports have been accelerating sharply for five consecutive months, driven by, in our view, skyrocketing memory prices and rising demand for AI-related chips such as CPU, optics, and high-end capacitors. Note semi imports from Korea rose 154% in May and 103% YTD. In May, Korea for the first time overtook Taiwan as the largest source of China's semi imports, with a 37% import share or \~US\$18bn. Our analysis shows China's 5M26 semi trade deficit grew 19% YoY to US\$99bn vs being flattish in the past three years. We see rapidly widening semi trade deficit as one of the biggest drivers of China's WFE capex growth. Moreover, China needs much more foundry capacity in mature nodes (for SRAM/PMIC/optics/power), advanced nodes (< 14nm, CPU/GPU/ADAS), and memory to support its efforts in AI, robotics, and electrification. Together with its WFE localization efforts due to US restrictions, Chinese WFE players are among our top picks in China tech.

![](images/76f8a45386a6252308a582c4674f83583c0898f634ed0298c76d7067c2ff3984.jpg)  
Source: China Customs, JEF

Chart 2 - China WFE Imports YoY  
![](images/b0b08351232ea615c2c65372f1005f6a38436c6d56d3f3f963b469507cb8fc35.jpg)  
Source: China Customs, JEF

Chart 3 - China Semiconductor Imports YoY  
![](images/87d500ddcbeadd741d6f8ee9d1c0abd1fbe4e2e54c8145ce7a437288ea2479b5.jpg)  
Source: China Customs, JEF

Chart 4 - China Semi Trade Deficit  
![](images/622ac8abc343030d3518d195e2d9c7cb94a5a89c178f9b56182159324bd3f1e7.jpg)  
Source: China Customs, JEF

Edison Lee, CFA \* | Equity Analyst
852 3743 8009 | edison.lee@JEF.com

Nick Cheng \* | Equity Analyst
+852 3743 8750 | nick.cheng@JEF.com

Matt Ma \* | Equity Analyst
852 3767 1109 | matt.ma@JEF.com

Annie Ping, CFA, FRM \* | Equity Associate +852 3767 1273 | annie.ping@JEF.com

Chart 5 - China Semiconductor Imports YoY  
![](images/b20f50810725703bee8c515dbffa06d9729a24ea0f85586fb85f1d1d3925f582.jpg)  
Source: China Customs, JEF

Chart 6 - China SPE Imports YoY  
![](images/4cc4c4b05243ecd8bf5da88d774c41677286a01ec8b88423590665ae04ec6960.jpg)  
Source: China Customs, JEF

Chart 7 - China Lithography Equipment Imports YoY  
![](images/8eb4bf48e71185fdf26a5292a41a6c0bfbc84d7980422430b1c8707f5880ecf1.jpg)  
Source: China Customs, JEF

Chart 8 - China Deposition Equipment Imports YoY  
![](images/08e686569c4d7ec138af775e794062308693b118709d2f1d31fe881c78c2166c.jpg)  
Source: China Customs, JEF

Chart 9 - China Ion Implanting Equipment Imports YoY  
![](images/27916f3bd6c452e01a6ed0f8ca324abad9de4b9f1fc0806c52ba57708a1151f9.jpg)  
Source: China Customs, JEF

Chart 10 - China Etching Equipment Imports YoY  
![](images/8449ee691e5e7a686e437f25f47a22a3a901a75c4d8bd91afe71cc0fd8aeab78.jpg)  
Source: China Customs, JEF

Table 1 - Quarterly SPE Imports by Key Countries (US\$m)

<table><tr><td></td><td>1Q20</td><td>2Q20</td><td>3Q20</td><td>4Q20</td><td>1Q21</td><td>2Q21</td><td>3Q21</td><td>4Q21</td><td>1Q22</td><td>2Q22</td><td>3Q22</td><td>4Q22</td><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>5M26</td></tr><tr><td>Germany</td><td>183</td><td>193</td><td>186</td><td>249</td><td>272</td><td>272</td><td>272</td><td>232</td><td>232</td><td>265</td><td>264</td><td>284</td><td>247</td><td>244</td><td>259</td><td>336</td><td>341</td><td>305</td><td>291</td><td>367</td><td>319</td><td>364</td><td>300</td><td>380</td><td>395</td><td>325</td></tr><tr><td>Israel</td><td>93</td><td>117</td><td>120</td><td>120</td><td>202</td><td>104</td><td>179</td><td>215</td><td>187</td><td>188</td><td>205</td><td>275</td><td>238</td><td>236</td><td>318</td><td>237</td><td>310</td><td>181</td><td>154</td><td>290</td><td>268</td><td>241</td><td>233</td><td>427</td><td>158</td><td>318</td></tr><tr><td>Japan</td><td>1,544</td><td>1,788</td><td>1,988</td><td>2,912</td><td>2,292</td><td>3,071</td><td>2,762</td><td>2,923</td><td>2,748</td><td>2,255</td><td>2,673</td><td>2,045</td><td>2,421</td><td>2,343</td><td>3,160</td><td>3,342</td><td>3,066</td><td>6,156</td><td>3,108</td><td>4,242</td><td>2,901</td><td>3,146</td><td>3,737</td><td>3,168</td><td>3,137</td><td>3,970</td></tr><tr><td>Korea</td><td>852</td><td>717</td><td>1,027</td><td>911</td><td>1,089</td><td>1,304</td><td>993</td><td>955</td><td>958</td><td>888</td><td>1,038</td><td>658</td><td>556</td><td>536</td><td>877</td><td>817</td><td>870</td><td>887</td><td>875</td><td>1,150</td><td>922</td><td>1,044</td><td>1,180</td><td>913</td><td>756</td><td>1,370</td></tr><tr><td>Latvia</td><td>124</td><td>186</td><td>146</td><td>156</td><td>210</td><td>233</td><td>458</td><td>458</td><td>377</td><td>353</td><td>305</td><td>324</td><td>246</td><td>218</td><td>337</td><td>955</td><td>907</td><td>407</td><td>388</td><td>268</td><td>783</td><td>981</td><td>1,482</td><td>1,499</td><td>1,518</td><td>1,334</td></tr><tr><td>Netherlands</td><td>445</td><td>919</td><td>903</td><td>531</td><td>928</td><td>875</td><td>539</td><td>1,100</td><td>866</td><td>728</td><td>519</td><td>661</td><td>614</td><td>1,501</td><td>2,733</td><td>2,691</td><td>2,221</td><td>1,879</td><td>3,142</td><td>2,525</td><td>2,094</td><td>1,338</td><td>2,780</td><td>2,899</td><td>1,649</td><td>2,068</td></tr><tr><td>Sweden</td><td>669</td><td>837</td><td>995</td><td>766</td><td>1,107</td><td>1,469</td><td>1,569</td><td>1,579</td><td>1,512</td><td>1,642</td><td>1,371</td><td>951</td><td>1,335</td><td>1,991</td><td>1,041</td><td>2,371</td><td>1,965</td><td>1,886</td><td>2,080</td><td>6,070</td><td>4,771</td><td>2,147</td><td>2,627</td><td>1,919</td><td>1,974</td><td>5,587</td></tr><tr><td>Taiwan</td><td>344</td><td>374</td><td>405</td><td>444</td><td>461</td><td>613</td><td>672</td><td>626</td><td>635</td><td>648</td><td>625</td><td>631</td><td>512</td><td>549</td><td>590</td><td>548</td><td>446</td><td>699</td><td>837</td><td>633</td><td>690</td><td>578</td><td>776</td><td>733</td><td>743</td><td>1,288</td></tr><tr><td>US</td><td>1,344</td><td>1,443</td><td>1,696</td><td>1,330</td><td>1,834</td><td>1,978</td><td>1,902</td><td>1,876</td><td>1,797</td><td>1,879</td><td>1,740</td><td>1,121</td><td>975</td><td>1,197</td><td>1,831</td><td>1,970</td><td>1,436</td><td>1,607</td><td>1,530</td><td>1,657</td><td>3,134</td><td>1,204</td><td>1,376</td><td>709</td><td>682</td><td>1,382</td></tr><tr><td>Others</td><td>208</td><td>287</td><td>317</td><td>340</td><td>346</td><td>422</td><td>417</td><td>407</td><td>403</td><td>403</td><td>403</td><td>434</td><td>338</td><td>338</td><td>338</td><td>623</td><td>623</td><td>653</td><td>653</td><td>653</td><td>582</td><td>582</td><td>616</td><td>616</td><td>616</td><td>824</td></tr><tr><td>Total RMHS</td><td>5,778</td><td>6,784</td><td>7,750</td><td>6,758</td><td>8,736</td><td>10,355</td><td>9,483</td><td>10,453</td><td>9,693</td><td>9,143</td><td>9,300</td><td>7,256</td><td>7,159</td><td>8,788</td><td>13,076</td><td>13,968</td><td>11,558</td><td>11,485</td><td>13,029</td><td>13,938</td><td>11,472</td><td>11,635</td><td>15,296</td><td>13,337</td><td>9,775</td><td>16,454</td></tr></table>

Source: China Customs, JEF

Table 2 - Quarterly SPE Imports YoY by Key Countries

<table><tr><td></td><td>1Q20</td><td>2Q20</td><td>3Q20</td><td>4Q20</td><td>1Q21</td><td>2Q21</td><td>3Q21</td><td>4Q21</td><td>1Q22</td><td>2Q22</td><td>3Q22</td><td>4Q22</td><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>5M26</td></tr><tr><td>Germany</td><td>-21%</td><td>-23%</td><td>-40%</td><td>50%</td><td>67%</td><td>41%</td><td>47%</td><td>25%</td><td>-14%</td><td>-3%</td><td>-3%</td><td>-38%</td><td>6%</td><td>-19%</td><td>36%</td><td>74%</td><td>38%</td><td>43%</td><td>-19%</td><td>5%</td><td>-6%</td><td>19%</td><td>3%</td><td>4%</td><td>-39%</td><td>-42%</td></tr><tr><td>Israel</td><td>166%</td><td>-27%</td><td>35%</td><td>0%</td><td>116%</td><td>-31%</td><td>39%</td><td>110%</td><td>-10%</td><td>-43%</td><td>54%</td><td>10%</td><td>-10%</td><td>-55%</td><td>-14%</td><td>31%</td><td>23%</td><td>-52%</td><td>-23%</td><td>-13%</td><td>33%</td><td>-12%</td><td>47%</td><td>-7%</td><td>-34%</td><td>-19%</td></tr><tr><td>Japan</td><td>30%</td><td>40%</td><td>27%</td><td>11%</td><td>48%</td><td>72%</td><td>39%</td><td>53%</td><td>20%</td><td>-27%</td><td>-3%</td><td>-30%</td><td>-12%</td><td>4%</td><td>18%</td><td>63%</td><td>27%</td><td>35%</td><td>-2%</td><td>25%</td><td>-5%</td><td>0%</td><td>20%</td><td>-25%</td><td>-20%</td><td>-20%</td></tr><tr><td>Korea</td><td>24%</td><td>-6%</td><td>32%</td><td>4%</td><td>28%</td><td>82%</td><td>-3%</td><td>5%</td><td>-14%</td><td>-32%</td><td>5%</td><td>-31%</td><td>-43%</td><td>-33%</td><td>-15%</td><td>24%</td><td>63%</td><td>50%</td><td>0%</td><td>38%</td><td>6%</td><td>-18%</td><td>35%</td><td>-29%</td><td>-18%</td><td>-15%</td></tr><tr><td>Russia</td><td>246%</td><td>-10%</td><td>32%</td><td>52%</td><td>70%</td><td>-15%</td><td>65%</td><td>194%</td><td>-7%</td><td>-86%</td><td>64%</td><td>-29%</td><td>-61%</td><td>-55%</td><td>49%</td><td>190%</td><td>188%</td><td>61%</td><td>-41%</td><td>-11%</td><td>87%</td><td>143%</td><td>274%</td><td>-7%</td><td>27%</td><td>-10%</td></tr><tr><td>Netherlands</td><td>75%</td><td>135%</td><td>167%</td><td>-24%</td><td>108%</td><td>-5%</td><td>-40%</td><td>107%</td><td>-7%</td><td>-17%</td><td>-4%</td><td>-40%</td><td>-29%</td><td>106%</td><td>426%</td><td>307%</td><td>262%</td><td>25%</td><td>-15%</td><td>-6%</td><td>-29%</td><td>-29%</td><td>-124%</td><td>54%</td><td>-21%</td><td>-21%</td></tr><tr><td>Other</td><td>200%</td><td>-20%</td><td>54%</td><td>6%</td><td>65%</td><td>-1%</td><td>48%</td><td>106%</td><td>37%</td><td>-10%</td><td>-7%</td><td>-40%</td><td>-25%</td><td>-5%</td><td>49%</td><td>149%</td><td>91%</td><td>36%</td><td>-25%</td><td>-32%</td><td>-18%</td><td>-14%</td><td>26%</td><td>-15%</td><td>-1%</td><td>20%</td></tr><tr><td>Taiwan</td><td>-40%</td><td>-17%</td><td>7%</td><td>26%</td><td>34%</td><td>64%</td><td>66%</td><td>42%</td><td>38%</td><td>6%</td><td>-7%</td><td>0%</td><td>-19%</td><td>-15%</td><td>-6%</td><td>-13%</td><td>-13%</td><td>27%</td><td>42%</td><td>15%</td><td>55%</td><td>-17%</td><td>-7%</td><td>-10%</td><td>8%</td><td>18%</td></tr><tr><td>US</td><td>90%</td><td>15%</td><td>27%</td><td>7%</td><td>36%</td><td>37%</td><td>12%</td><td>41%</td><td>-2%</td><td>-5%</td><td>-9%</td><td>-40%</td><td>-46%</td><td>-36%</td><td>5%</td><td>76%</td><td>47%</td><td>34%</td><td>-16%</td><td>-18%</td><td>-8%</td><td>-25%</td><td>-10%</td><td>-57%</td><td>-48%</td><td>-33%</td></tr><tr><td>Others</td><td>15%</td><td>15%</td><td>23%</td><td>33%</td><td>73%</td><td>25%</td><td>36%</td><td>13%</td><td>-2%</td><td>-9%</td><td>4%</td><td>7%</td><td>-17%</td><td>-14%</td><td>32%</td><td>44%</td><td>22%</td><td>15%</td><td>-27%</td><td>7%</td><td>-18%</td><td>27%</td><td>-27%</td><td>-17%</td><td>-18%</td><td></td></tr><tr><td>Total</td><td>42%</td><td>23%</td><td>33%</td><td>7%</td><td>51%</td><td>53%</td><td>22%</td><td>55%</td><td>11%</td><td>-32%</td><td>-1%</td><td>-31%</td><td>-26%</td><td>-4%</td><td>39%</td><td>92%</td><td>61%</td><td>31%</td><td>0%</td><td>0%</td><td>-1%</td><td>-1%</td><td>17%</td><td>-4%</td><td>-16%</td><td>-13%</td></tr></table>

Source: China customs, JEF

Table 3 - Quarterly SPE Imports by Key Product Categories (US\$m)

<table><tr><td></td><td>1Q20</td><td>2Q20</td><td>3Q20</td><td>4Q20</td><td>1Q21</td><td>2Q21</td><td>3Q21</td><td>4Q21</td><td>1Q22</td><td>2Q22</td><td>3Q22</td><td>4Q22</td><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>5M26</td></tr><tr><td>Wafer Fabrication</td><td>2,906</td><td>3,488</td><td>3,839</td><td>3,302</td><td>4,928</td><td>6,027</td><td>4,723</td><td>5,458</td><td>5,173</td><td>4,702</td><td>4,876</td><td>3,915</td><td>4,060</td><td>5,152</td><td>8,801</td><td>9,353</td><td>7,764</td><td>7,527</td><td>8,826</td><td>9,378</td><td>7,377</td><td>7,629</td><td>10,175</td><td>9,240</td><td>6,504</td><td>10,719</td></tr><tr><td>Inspecting &amp; Testing</td><td>548</td><td>615</td><td>597</td><td>451</td><td>725</td><td>803</td><td>881</td><td>1,022</td><td>883</td><td>1,037</td><td>1,079</td><td>942</td><td>805</td><td>1,141</td><td>1,531</td><td>1,418</td><td>1,078</td><td>1,059</td><td>1,291</td><td>1,607</td><td>1,207</td><td>1,051</td><td>1,661</td><td>1,062</td><td>778</td><td>1,567</td></tr><tr><td>Other</td><td>274</td><td>343</td><td>518</td><td>493</td><td>577</td><td>724</td><td>845</td><td>795</td><td>634</td><td>651</td><td>501</td><td>328</td><td>312</td><td>334</td><td>355</td><td>377</td><td>294</td><td>350</td><td>360</td><td>340</td><td>315</td><td>320</td><td>398</td><td>481</td><td>296</td><td>463</td></tr><tr><td>Cristival Gruwine</td><td>189</td><td>226</td><td>212</td><td>231</td><td>249</td><td>389</td><td>444</td><td>402</td><td>588</td><td>530</td><td>181</td><td>459</td><td>397</td><td>449</td><td>426</td><td>445</td><td>443</td><td>472</td><td>265</td><td>426</td><td>321</td><td>420</td><td>325</td><td>439</td><td>276</td><td>463</td></tr><tr><td>Parts</td><td>1,406</td><td>1,648</td><td>2,106</td><td>1,748</td><td>1,788</td><td>1,897</td><td>2,079</td><td>2,137</td><td>1,907</td><td>1,682</td><td>1,798</td><td>1,291</td><td>1,105</td><td>1,265</td><td>1,360</td><td>1,557</td><td>1,267</td><td>1,572</td><td>1,371</td><td>1,461</td><td>1,477</td><td>1,527</td><td>1,992</td><td>1,493</td><td>1,416</td><td>2,326</td></tr><tr><td>Others</td><td>452</td><td>487</td><td>579</td><td>459</td><td>547</td><td>611</td><td>651</td><td>501</td><td>507</td><td>504</td><td>772</td><td>383</td><td>429</td><td>479</td><td>820</td><td>684</td><td>715</td><td>815</td><td>830</td><td>830</td><td>782</td><td>631</td><td>735</td><td>511</td><td>831</td><td>831</td></tr><tr><td>Total (RHS)</td><td>5,778</td><td>6,784</td><td>7,750</td><td>6,758</td><td>8,736</td><td>10,355</td><td>9,483</td><td>10,453</td><td>9,693</td><td>9,143</td><td>9,390</td><td>7,256</td><td>7,159</td><td>7,898</td><td>13,076</td><td>13,968</td><td>11,558</td><td>11,485</td><td>13,029</td><td>13,938</td><td>11,477</td><td>11,635</td><td>15,296</td><td>13,337</td><td>9,775</td><td>16,452</td></tr></table>

Source: China Customs, JEF

Table 4 - Quarterly SPE Imports YoY by Key Product Categories

<table><tr><td></td><td>1Q20</td><td>2Q20</td><td>3Q20</td><td>4Q20</td><td>1Q21</td><td>2Q21</td><td>3Q21</td><td>4Q21</td><td>1Q22</td><td>2Q22</td><td>3Q22</td><td>4Q22</td><td>1Q23</td><td>2Q23</td><td>3Q23</td><td>4Q23</td><td>1Q24</td><td>2Q24</td><td>3Q24</td><td>4Q24</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>1Q26</td><td>5M26</td></tr><tr><td>Wafer Fabrication</td><td>59%</td><td>37%</td><td>31%</td><td>7%</td><td>70%</td><td>73%</td><td>23%</td><td>65%</td><td>5%</td><td>-22%</td><td>3%</td><td>-28%</td><td>-22%</td><td>10%</td><td>81%</td><td>139%</td><td>91%</td><td>46%</td><td>0%</td><td>0%</td><td>-5%</td><td>1%</td><td>15%</td><td>-1%</td><td>-14%</td><td>-12%</td></tr><tr><td>Inspection &amp; Tacture</td><td>76%</td><td>10%</td><td>14%</td><td>-6%</td><td>32%</td><td>30%</td><td>48%</td><td>137%</td><td>22%</td><td>29%</td><td>22%</td><td>-8%</td><td>-9%</td><td>10%</td><td>42%</td><td>50%</td><td>34%</td><td>-7%</td><td>-16%</td><td>13%</td><td>12%</td><td>-1%</td><td>29%</td><td>-34%</td><td>-36%</td><td>-15%</td></tr><tr><td>Packaging</td><td>53%</td><td>-16%</td><td>0%</td><td>56%</td><td>109%</td><td>124%</td><td>56%</td><td>61%</td><td>14%</td><td>-24%</td><td>-41%</td><td>-59%</td><td>-51%</td><td>-39%</td><td>-29%</td><td>1

[中间内容因长度限制已省略]

lar investment objectives, portfolio holdings, strategy, financial situation, or needs of any recipient. As such, any advice or recommendation in this report may not be suitable for a particular recipient. JEF assumes recipients of this report are capable of evaluating the information contained herein and of exercising independent judgment. A recipient of this report should not make any investment decision without first considering whether any advice or recommendation in this report is suitable for the recipient based on the recipient's particular circumstances and, if appropriate or otherwise needed, seeking professional advice, including tax advice. JEF does not perform any suitability or other analysis to check whether an investment decision made by the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
