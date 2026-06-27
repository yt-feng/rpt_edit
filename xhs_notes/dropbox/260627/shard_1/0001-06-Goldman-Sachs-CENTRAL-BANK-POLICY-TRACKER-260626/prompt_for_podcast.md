你是财经类 AI Podcast 制作人，擅长把研报内容改写成中文、英文两条独立的访谈式播客脚本。

【目标】
- 基于下面研报解析内容，写两份 podcast 脚本：一份中文，一份英文。
- 每份目标时长约 5 分钟。
- 两份都要是“访谈聊天式”，不是单人念稿。
- 听感：像一位主持人和一位研究员围绕报告做深度但自然的讨论。
- 不要使用 emoji。
- 不要把全文讲完，要留下 1-2 个“完整报告里会继续展开”的悬念。

【输出格式必须严格遵守】
- 中文部分只能使用 `ZH_A:` 和 `ZH_B:` 开头。
- 英文部分只能使用 `EN_A:` 和 `EN_B:` 开头。
- 每一句独立成行。
- 不要输出 Markdown 标题。
- 不要输出舞台说明、音效说明或括号注释。
- 先输出完整中文脚本，再输出完整英文脚本。

【角色设定】
- A 是主持人：负责提问、转场、替听众追问“所以这意味着什么”。
- B 是研究员：负责解释报告逻辑、给出结构化判断和保留悬念。
- 两个角色必须频繁轮换，避免一个人连续说超过 3 句。
- 每句要适合 TTS 朗读：短句、自然、不要太书面。

【中文脚本结构】
1. 开场：A 用一个问题引出报告价值，B 给出主判断。
2. 第一部分：这份报告真正要回答的问题是什么。
3. 第二部分：2-3 个关键洞察，每个洞察都要有“这意味着什么”。
4. 第三部分：哪些问题仍然没有完全展开，为什么值得继续读完整报告。
5. 结尾：自然引导听众加入社群/阅读完整报告，不要硬广。

【英文脚本结构】
- 英文不是中文逐句翻译，而是面向英文听众重新组织。
- 保留同样的主线和洞察，但表达更口语、更 podcast。
- Use natural conversational English.
- Avoid long sentences and avoid reading like a research memo.

【内容边界】
- 可以基于研报内容做适度发散，但必须是从原文逻辑推出的判断。
- 不要编造具体数据、公司动作或引用。
- 对不确定内容要用“这里仍需要继续验证”或 “the report does not fully answer this yet” 表达。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”或 “a global investment bank report”。

【研报解析内容】
"""
CENTRAL BANK POLICY TRACKER

June 2026

■ Recent policy changes: Central bank actions have shifted more hawkish due to the war in Iran. In DMs, no central banks lowered and 39% raised rates over the last three months. In EMs, 16% cut rates and 7% raised rates over the same period. But our Global Financial Conditions Index (GS FCI) has eased by 24bp over the last three months, reflecting 34bp of easing in DMs and 10bp of easing in EMs (largely reflecting higher rates). At the country level, financial conditions have eased the most in Türkiye (-117bps), South Korea (-93bps), and Romania (-83bps) and tightened the most in Russia (158bps), Israel (57bps), and Brazil (57bps).

Forecast updates: We have made several policy rate forecast revisions over the last 30 days. In the US, we pushed back the final two rate cuts in our Fed forecast back to June and December of 2027 (vs. December 2026 and March 2027 previously). In Brazil, we raised our end-2026 policy rate forecasts by +75bp to 14.0%, in Hungary we lowered our end-2026 policy rate forecasts by -50bp to 5.25%, and in Taiwan we removed further rate cuts and now forecast a hold at 2% (vs 2.25% previously) through end-2026. In South Korea we raised our end-2027 policy rate forecasts by +25bp to 3.25%.

■ Current forecasts: We forecast that global central banks will lower rates by 0.1pp to $3.1\%$ (on a GDP-weighted basis) over the next four quarters. We expect that DM central banks will increase policy rates by 8bp on average over the next four quarters, reflecting rate hikes in New Zealand (+50bps), Euro Area (+25bps), Sweden (+25bps), Norway (+25bps) and Japan (+25bps) that are partially offset by holds or decreases elsewhere, particularly the US (-25bps through June 2027; -50bp through end-2027) and the UK (-50bps through June 2027; -75bp through end-2027). We expect that EM central banks will cut rates by -33bp on average, reflecting -208bp of cuts in CEEMEA and -35bp in Latin America, with 4bp of hikes in Asia.

■ Forecasts relative to consensus and current pricing: Our end-2026 policy rate forecasts are dovish relative to market pricing (our forecasts are below pricing in 73% of DMs and 57% of EMs; above in 18% of DMs and 43% of EMs). Our forecasts are balanced relative to consensus in both DMs (at least 0.1pp below in 27% vs. at least 0.1pp above in 27%) and EMs (at least 0.1pp below in 32% vs. at least 0.1pp above in 36%).

■ Balance sheet policy: Balance sheets as a share of GDP remain particularly

Jan Hatzius
+1(212)902-0394 | jan.hatzius@gs.com
GS & Co. LLC

Joseph Briggs +1(212)902-2163 | joseph.briggs@gs.com GS & Co. LLC

Sarah Dong
+1(212)357-9741 | sarah.dong@gs.com
GS & Co. LLC

Megan Peters  
+44(20)7051-2058 |  
megan.l.peters@gs.com  
GS International

elevated relative to their 2019 levels in New Zealand (8pp higher) and Australia (4pp). In the US, we see scope for a modest reduction in the Fed's balance sheet size if a reduction in reserve demand warrants an adjustment, but think the bar to a meaningful decline is high.

Exhibit 1: Global Central Banks Have Mostly Either Held or Hiked Over the Last Three Months  
![](images/373cddf35a3da51bcd18ebadbffc66d49ca85718a74e975a586de5cf03a7b165.jpg)  
Source: GS Global Investment Research

![](images/89fa2e88d938d72fde0b9ebe98b7be9e904e5276acacbd6510a38f8527edba56.jpg)

Exhibit 2: We Forecast Further Policy Rate Declines in the UK, US, and Some EMs, but Rate Hikes or Holds in Most DMs Over the Next Four Quarters  
![](images/f4ab4560bbe4cd72ca87a8092fc31a24ac7e8de368158e3759850e8d32d50446.jpg)  
Source: GS Global Investment Research

![](images/4738990b1d685f005f3e677e47e39a1f055c9965bb302ccd98585094f66683ab.jpg)

Exhibit 3: Our End-2026 Policy Rate Forecasts Are Dovish Relative to Market Pricing but Skewed Hawkish Relative to Consensus

<table><tr><td rowspan="4"></td><td colspan="6">End-2026 Policy Rate</td></tr><tr><td colspan="4">Policy Rate Forecasts</td><td colspan="2">vs. GS Forecast</td></tr><tr><td>Latest</td><td>GS</td><td>Consensus</td><td>Market Pricing</td><td>GS - Consensus</td><td>GS - Market Pricing</td></tr><tr><td colspan="4">(%)</td><td colspan="2">(pp)</td></tr><tr><td>Global*</td><td>4.6</td><td>4.7</td><td>4.6</td><td>4.5</td><td>0.0</td><td>0.2</td></tr><tr><td colspan="7">Developed Economies</td></tr><tr><td>US</td><td>3.6</td><td>3.6</td><td>3.1</td><td>4.0</td><td>0.5</td><td>-0.3</td></tr><tr><td>Euro Area</td><td>2.3</td><td>2.5</td><td>2.5</td><td>2.5</td><td>0.0</td><td>0.0</td></tr><tr><td>Japan</td><td>1.0</td><td>1.0</td><td>1.3</td><td>1.2</td><td>-0.3</td><td>-0.2</td></tr><tr><td>UK</td><td>3.8</td><td>3.8</td><td>3.9</td><td>4.0</td><td>-0.1</td><td>-0.2</td></tr><tr><td>Canada</td><td>2.3</td><td>2.3</td><td>2.3</td><td>2.4</td><td>0.0</td><td>-0.2</td></tr><tr><td>Australia</td><td>4.4</td><td>4.6</td><td>4.4</td><td>4.5</td><td>0.2</td><td>0.1</td></tr><tr><td>Switzerland</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td></tr><tr><td>Sweden</td><td>1.8</td><td>2.0</td><td>1.9</td><td>1.9</td><td>0.1</td><td>0.1</td></tr><tr><td>Hong Kong</td><td>2.8</td><td>2.1</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>New Zealand</td><td>2.3</td><td>2.8</td><td>2.6</td><td>2.8</td><td>0.2</td><td>-0.1</td></tr><tr><td colspan="7">Latam</td></tr><tr><td>Brazil</td><td>14.3</td><td>14.0</td><td>13.4</td><td>13.8</td><td>0.6</td><td>0.2</td></tr><tr><td>Mexico</td><td>6.5</td><td>6.5</td><td>6.5</td><td>6.9</td><td>0.0</td><td>-0.4</td></tr><tr><td>Colombia</td><td>11.3</td><td>12.3</td><td>11.9</td><td>11.7</td><td>0.3</td><td>0.6</td></tr><tr><td>Chile</td><td>4.5</td><td>4.5</td><td>4.7</td><td>4.4</td><td>-0.2</td><td>0.1</td></tr><tr><td>Peru</td><td>4.3</td><td>4.3</td><td>4.3</td><td>NA</td><td>-0.1</td><td>NA</td></tr><tr><td colspan="7">CEEMEA</td></tr><tr><td>Russia</td><td>14.3</td><td>12.0</td><td>13.0</td><td>NA</td><td>-0.9</td><td>NA</td></tr><tr><td>Turkiye</td><td>37.0</td><td>37.0</td><td>35.2</td><td>39.4</td><td>1.8</td><td>-2.4</td></tr><tr><td>Poland</td><td>3.8</td><td>3.8</td><td>3.8</td><td>3.8</td><td>0.0</td><td>-0.1</td></tr><tr><td>Israel</td><td>3.8</td><td>3.3</td><td>3.6</td><td>3.9</td><td>-0.3</td><td>-0.6</td></tr><tr><td>Egypt</td><td>19.0</td><td>21.0</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>South Africa</td><td>7.0</td><td>7.3</td><td>7.0</td><td>7.3</td><td>0.3</td><td>0.0</td></tr><tr><td>Romania</td><td>6.5</td><td>6.5</td><td>6.3</td><td>NA</td><td>0.2</td><td>NA</td></tr><tr><td>Czech Republic</td><td>3.5</td><td>3.8</td><td>3.6</td><td>4.0</td><td>0.1</td><td>-0.3</td></tr><tr><td>Hungary</td><td>6.0</td><td>5.3</td><td>5.9</td><td>5.0</td><td>-0.7</td><td>0.2</td></tr><tr><td>Ukraine</td><td>15.0</td><td>13.5</td><td>14.2</td><td>NA</td><td>-0.7</td><td>NA</td></tr><tr><td>Ghana</td><td>14.0</td><td>14.0</td><td>13.2</td><td>NA</td><td>0.8</td><td>NA</td></tr><tr><td>Kazakhstan</td><td>17.0</td><td>15.5</td><td>16.2</td><td>NA</td><td>-0.7</td><td>NA</td></tr><tr><td colspan="7">Asia</td></tr><tr><td>Mainland China</td><td>1.4</td><td>1.4</td><td>NA</td><td>NA</td><td>NA</td><td>NA</td></tr><tr><td>India</td><td>5.3</td><td>5.8</td><td>5.5</td><td>5.6</td><td>0.2</td><td>0.1</td></tr><tr><td>South Korea</td><td>2.5</td><td>3.0</td><td>3.0</td><td>3.7</td><td>0.0</td><td>-0.7</td></tr><tr><td>Indonesia</td><td>5.8</td><td>5.8</td><td>5.6</td><td>NA</td><td>0.1</td><td>NA</td></tr><tr><td>Taiwan</td><td>2.0</td><td>2.0</td><td>2.1</td><td>1.9</td><td>-0.1</td><td>0.1</td></tr><tr><td>Thailand</td><td>1.0</td><td>1.0</td><td>1.1</td><td>1.0</td><td>-0.1</td><td>0.0</td></tr><tr><td>Philippines</td><td>4.8</td><td>5.5</td><td>5.1</td><td>NA</td><td>0.4</td><td>NA</td></tr><tr><td>Vietnam</td><td>4.5</td><td>4.5</td><td>4.9</td><td>NA</td><td>-0.4</td><td>NA</td></tr><tr><td>Malaysia</td><td>2.8</td><td>2.8</td><td>2.8</td><td>2.8</td><td>-0.1</td><td>0.0</td></tr></table>

Note: Red shading indicates GS forecast above consensus forecast or market pricing, and blue shading indicates GS forecast below consensus forecast or market pricing.  
\* Global policy rate forecasts represent a GDP-weighted average of the economies with both consensus forecasts and market pricing available.

## Changes in Policy Rates and Financial Conditions

Exhibit 4: Recent Policy Rate Changes  
![](images/676f76fed9545a23c4680abb6a10ee2b639a14bfbbeb165c2716d909211c9d95.jpg)  
Source: Haver Analytics, GS Global Investment Research

Exhibit 5: Change in Average Global Policy Rate Over Time  
![](images/6e5d200c7a5bf2025e24a98062e21c06dcbf4bcee39ad717dace078a6aeb8b50.jpg)  
Source: GS Global Investment Research

Exhibit 6: Changes in Financial Conditions Over the Last 3 Months  
![](images/d758405e1cb91ebc80c8b43e6b3d2b681246a1663f25eebe90c8ac89026ceb4a.jpg)  
Source: GS Global Investment Research

Exhibit 7: Changes in Financial Conditions Over the Last 12 Months  
![](images/bafb55e9c723a03f99f34f12ba076d4e618ba50c17f8b0abcaa6a1a4744a8473.jpg)  
Source: GS Global Investment Research

## Policy Rate Forecasts

Exhibit 8: Policy Rate Forecast Revisions in Last 30 Days  
![](images/1ca27c56e1201d4d9fe0111ef88f2a34489691046c0b043d2361b79586b3bbec.jpg)  
Source: GS Global Investment Research

Exhibit 9: GS Forecast Policy Rate Changes  
![](images/a9ad4cef4391e5e57f142b2ea673ea55aa875cdb796d2bf3a9acdc8e99b87b76.jpg)  
Source: GS Global Investment Research

## Exhibit 11: GS Policy Rate Forecasts vs. Bloomberg Consensus Forecasts and Market Pricing

![](images/d98816de227dcfa99271195d38a824584831f557c48bb81adb13e0fec9977882.jpg)

![](images/aaa6a715b2b89418eb633b1dfc23d48e667dd48174de28d62ed66c0f636b2e7f.jpg)

![](images/0f7d1b742e1d632be8b95471c80df710b133930cbb675d5c4dfd2cc5c0876181.jpg)

![](images/f4b93b2521f143e2fa7b75becc4598b12a942908a7e0871a7e99aa2dd936def9.jpg)

![](images/949b76bc20780fc8306698217a9254f65d14bf0b952c65f255833d8764894121.jpg)

![](images/cad9580bd436ff322fa70ca7ec4374769c5e8d97a0d0ef1e69fe7efb0d4f4565.jpg)

![](images/2a2b7e9916c4c601011bf0b31dc40ed5d7fc7f76ee19051500e580d83df9ae51.jpg)  
We exclude economies where GS forecasts differ from market pricing and consensus by more than 3pp due to data quality concerns, as well as economies where policy rate forecasts exceed $10\%$ for easier exposition.  
Source: GS Global Investment Research, Bloomberg

Exhibit 12: GS Policy Rate Forecasts vs. Bloomberg Consensus Forecasts and Market Pricing

<table><tr><td rowspan="4"></td><td colspan="7">Year-End Policy Rate, Percent</td></tr><tr><td rowspan="3">Latest</td><td colspan="3">End-2026</td><td colspan="3">End-2027</td></tr><tr><td colspan="3">Policy Rate Forecasts</td><td colspan="3">Policy Rate Forecasts</td></tr><tr><td>GS</td><td>Consensus</td><td>Market Pricing</td><td>GS</td><td>Consensus</td><td>Market Pricing</td></tr><tr><td>Global*</td><td>4.6</td><td>4.7</td><td>4.6</td><td>4.5</td><td>4.0</td><td>4.1</td><td>4.5</td></tr><tr><td colspan="8">Developed Economies</td></tr><tr><td>US</td><td>3.6</td><td>3.6</td><td>3.7</td><td>4.0</td><td>3.1</td><td>3.4</td><td>3.8</td></tr><tr><td>Euro Area</td><td>2.3</td><td>2.5</td><td>2.5</td><td>2.5</td><td>2.0</td><td>2.3</td><td>2.5</td></tr><tr><td>Japan</td><td>1.0</td><td>1.0</td><td>1.3</td><td>1.2</td><td>1.5</td><td>1.5</td><td>1.7</td></tr><tr><td>UK</td><td>3.8</td><td>3.8</td><td>3.9</td><td>4.0</td><td>3.0</td><td>3.3</td><td>3.9</td></tr><tr><td>Canada</td><td>2.3</td><td>2.3</td><td>2.3</td><td>2.4</td><td>2.8</td><td>2.8</td><td>2.9</td></tr><tr><td>Australia</td><td>4.4</td><td>4.6</td><td>4.4</td><td>4.5</td><td>3.6</td><td>4.2</td><td>4.2</td></tr><tr><td>Switzerland</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.0</td><td>0.1</td></tr><tr><td>Sweden</td><td>1.8</td><td>2.0</td><td>1.9</td><td>1.9</td><td>2.3</td><td>2.0</td><td>2.1</td></tr><tr><td>Hong Kong</td><td>2.8</td><td>2.1</td><td>NA</td><td>NA</td><td>1.9</td><td>NA</td><td>NA</td></tr><tr><td>New Zealand</td><td>2.3</td><td>2.8</td><td>2.6</td><td>2.8</td><td>2.8</td><td>3.1</td><td>3.3</td></tr><tr><td colspan="8">Latam</td></tr><tr><td>Brazil</td><td>14.3</td><td>14.0</td><td>13.4</td><td>-0.1</td><td>12.0</td><td>11.5</td><td>0.9</td></tr><tr><td>Mexico</td><td>6.5</td><td>6.5</td><td>6.5</td><td>6.9</td><td>6.5</td><td>6.5</td><td>7.6</td></tr><tr><td>Colombia</td><td>11.3</td><td>12.3</td><td>11.9</td><td>11.7</td><td>11.3</td><td>10.6</td><td>10.1</td></tr><tr><td>Chile</td><td>4.5</td><td>4.5</td><td>4.7</td><td>4.4</td><td>4.3</td><td>4.6</td><td>4.5</td></tr><tr><td>Peru</td><td>4.3</td><td>4.3</td><td>4.3</td><td>NA</td><td>4.3</td><td>4.5</td><td>NA</td></tr><tr><td colspan="8">CEEMEA</td></tr><tr><td>Russia</td><td>14.3</td><td>12.0</td><td>13.0</td><td>NA</td><td>8.0</td><td>9.5</td><td>NA</td></tr><tr><td>Turkiye</td><td>37.0</td><td>37.0</td><td>35.2</td><td>39.4</td><td>29.0</td><td>26.4</td><td>NA</td></tr><tr><td>Poland</td><td>3.8</td><td>3.8</td><td>3.8</td><td>3.8</td><td>3.5</td><td>3.6</td><td>3.8</td></tr><tr><td>Israel</td><td>3.8</td><td>3.3</td><td>3.6</td><td>3.9</td><td>3.3</td><td>3.2</td><td>3.5</td></tr><tr><td>Egypt</td><td>19.0</td><td>21.0</td><td>NA</td><td>NA</td><td>14.0</td><td>NA</td><td>NA</td></tr><tr><td>South Africa</td><td>7.0</td><td>7.3</td><td>7.0</td><td>7.3</td><td>6.5</td><td>6.4</td><td>7.2</td></tr><tr><td>Romania</td><td>6.5</td><td>6.5</td><td>6.3</td><td>NA</td><td>4.5</td><td>5.2</td><td>NA</td></tr><tr><td>Czech Republic</td><td>3.5</td><td>3.8</td><td>3.6</td><td>4.0</td><td>3.0</td><td>3.5</td><td>4.0</td></tr><tr><td>Hungary</td><td>6.0</td><td>5.3</td><td>5.9</td><td>5.0</td><td>4.0</td><td>5.0</td><td>4.7</td></tr><tr><td>Ukraine</td><td>15.0</td><td>13.5</td><td>14.2</td><td>NA</td><td>11.5</td><td>12.3</td><td>NA</td></tr><tr><td>Ghana</td><td>14.0</td><td>14.0</td><td>13.2</td><td>NA</td><td>16.0</td><td>13.3</td><td>NA</td></tr><tr><td>Kazakhstan</td><td>17.0</td><td>15.5</td><td>16.2</td><td>NA</td><td>11.0</td><td>NA</td><td>NA</td></tr><tr><td colspan="8">Asia</td></tr><tr><td>Mainland China</td><td>1.4</td><td>1.4</td><td>NA</td><td>NA</td><td>1.3</td><td>NA</td><td>NA</td></tr><tr><td>India</td><td>5.3</td><td>5.8</td><td>5.5</td><td>5.6</td><td>5.8</td><td>5.6</td><td>6.1</td></tr><tr><td>South Korea</td><td>2.5</td><td>3.0</td><td>3.0</td><td>3.7</td><td>3.3</td><td>3.1</td><td>4.0</td></tr><tr><td>Indonesia</td><td>5.8</td><td>5.8</td><td>5.6</td><td>NA</td><td>5.8</td><td>5.2</td><td>NA</td></tr><tr><td>Taiwan</td><td>2.0</td><td>2.0</td><td>2.1</td><td>1.9</td><td>2.0</td><td>2.1</td><td>1.9</td></tr><tr><td>Thailand</td><td>1.0</td><td>1.0</td><td>1.1</td><td>1.0</td><td>1.0</td><td>1.1</td><td>1.2</td></tr><tr><td>Philippines</td><td>4.8</td><td>5.5</td><td>5.1</td><td>NA</td><td>5.5</td><td>4.9</td><td>NA</td></tr><tr><td>Vietnam</td><td>4.5</td><td>4.5</td><td>4.9</td><td>NA</td><td>4.5</td><td>4.8</td><td>NA</td></tr><tr><td>Malaysia</td><td>2.8</td><td>2.8</td><td>2.8</td><td>2.8</td><td>2.8</td><td>2.9</td><td>NA</td></tr></table>

Note: Red shading indicates consensus forecast or market pricing above GS forecast, and blue shading indicates consensus forecast or market pricing below GS forecast.  
\* Global policy rate forecasts represent a GDP-weighted average of the economies with both consensus forecasts and market pricing available.

## Policy Rate Forecast Drivers

Exhibit 13: GS Growth and Policy Rate Forecasts vs. Bloomberg Consensus Forecasts  
![](images/e064bc28aec7076a713383a178bb494cc90649f057c8a98e0905b777304cb602.jpg)  
Source: GS Global Investment Research, Bloomberg

Exhibit 14: GS GDP Growth Forecasts vs. Central Bank and Bloomberg Consensus Forecasts

<table><tr><td rowspan="3"></td><td rowspan="2">End-2025</td><td colspan="6">Real GDP Growth (Annual Average), Percent Change</td></tr><tr><td colspan="3">End-2026</td><td colspan="3">End-2027</td></tr><tr><td>Actual****</td><td>GS</td><td>GS - Central Bank</td><td>GS - Consensus</td><td>GS</td><td>GS - Central Bank</td><td>GS - Consensus</td></tr><tr><td>Global*</td><td>1.8</td><td>1.7</td><td>NA</td><td>0.0</td><td>1.9</td><td>NA</td><td>0.3</td></tr><tr><td colspan="8">Developed Economies</td></tr><tr><td>US**</td><td>2.0</td><td>2.0</td><td>-0.2</td><td>-0.1</td><td>2.2</td><td>-0.1</td><td>0.1</td></tr><tr><td>Euro Area</td><td>1.5</td><td>0.5</td><td>-0.3</td><td>-0.1</td><td>1.2</td><td>0.0</td><td>0.6</td></tr><tr><td>Japan***</td><td>0.8</td><td>0.5</td><td>-0.2</td><td>NA</td><td>1.2</td><td>0.4</td><td>NA</td></tr><tr><td>UK**</td><td>1.0</td><td>1.2</td><td>-0.1</td><td>0.2</td><td>1.6</td><td>0.0</td><td>0.6</td></tr><tr><td>Canada**</td><td>0.7</td><td>1.6</td><td>-0.2</td><td>0.6</td><td>2.0</td><td>0.6</td><td>0.9</td></tr><tr><td>Australia</td><td>2.0</td><td>1.7</td><td>0.4</td><td>-0.3</td><td>2.2</td><td>0.8</td><td>0.2</td></tr><tr><td>Switzerland</td><td>1.5</td><td>0.9</td><td>-0.1</td><td>-0.2</td><td>1.5</td><td>0.0</td><td>0.4</td></tr><tr><td>Sweden</td><td>1.7</td><td>1.7</td><td>1.9</td><td>-0.3</td><td>2.0</td><td>0.7</td><td>0.0</td></tr><tr><td>Hong Kong</td><td>3.6</td><td>4.6</td><td>NA</td><td>1.2</td><td>2.5</td><td>NA</td><td>-1.0</td></tr><tr><td>New Zealand</td><td>0.2</td><td>2.1</td><td>0.4</td><td>0.5</td><td>2.5</td><td>-1.1</td><td>0.9</td></tr><tr><td colspan="8">Latam</td></tr><tr><td>Brazil</td><td>2.3</td><td>2.2</td><td>0.2</td><td>0.3</td><td>1.6</td><td>NA</td><td>-0.3</td></tr><tr><td>Mexico</td><td>0.5</td><td>1.2</td><td>-0.4</td><td>0.1</td><td>1.7</td><td>-0.3</td><td>0.6</td></tr><tr><td>Colombia</td><td>2.6</td><td>2.4</td><td>0.0</td><td>0.0</td><td>2.4</td><td>0.3</td><td>0.0</td></tr><tr><td>Chile</td><td>2.5</td><td>1.6</td><td>NA</td><td>-0.1</td><td>2.6</td><td>NA</td><td>0.9</td></tr><tr><td>Peru</td><td>3.4</td><td>3.4</td><td>0.5</td><td>0.5</td><td>2.5</td><td>NA</td><td>-0.4</td></tr><tr><td colspan="8">CEEMEA</td></tr><tr><td>Russia**</td><td>1.0</td><td>0.9</td><td>NA</td><td>0.0</td><td>1.8</td><td>NA</td><td>1.0</td></tr><tr><td>Turkiye</td><td>3.6</td><td>2.7</td><td>NA</td><td>NA</td><td>3.6</td><td>NA</td><td>NA</td></tr><tr><td>Poland**</td><td>3.8</td><td>3.3</td><td>-0.8</td><td>-0.1</td><td>3.6</td><td>1.5</td><td>0.1</td></tr><tr><td>Israel</td><td>3.2</td><td>2.2</td><td>-2.4</td><td>-0.9</td><td>4.8</td><td>NA</td><td>1.7</td></tr><tr><td>Egypt</td><td>4.4</td><td>4.7</td><td>NA</td><td>0.2</td><td>4.7</td><td>NA</td><td>0.2</td></tr><tr><td>South Africa</td><td>1.1</td><td>1.6</td><td>-0.3</td><td>0.4</td><

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g.,

marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints. As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
