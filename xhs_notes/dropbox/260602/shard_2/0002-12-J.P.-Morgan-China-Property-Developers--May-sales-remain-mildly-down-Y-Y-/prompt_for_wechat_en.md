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
- End with: `*This article is for learning and discussion only and does not constitute investment advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
# China Property

Developers' May sales remain mildly down Y/Y; focus on alphas (COLI, CRL, Jinmao)

According to CREIS, the top 100 developers' contracted sales dropped $4\%$ Y/Y in May, broadly in line with April $(-5\%$ Y/Y) (Figure 1). Compared to the static base (4-year average of 2018-21), sales remained $71\%$ below (April: $-71\%$ ). On 29 May, the sector rallied $4\%$ (vs. HSI $+1\%$ ) despite no clear catalyst. Some investors wonder if this is related to the five-year urban renewal plan released by the State Council, but we did not find the plan particularly exciting as the direction is just similar to previous ones. Over the next few months, we expect primary sales to stay at a similar momentum $(+/- 5\%$ Y/Y) (reminder: the recent green shoots in volume & prices are more evident in the secondary market). We recommend focusing on developers with positive sales growth, and our top picks are COLI $(+14\%$ Y/Y year-to-date; $+14\%$ Y/Y in May), CR Land $(+8\% / +28\%)$ & Jinmao $(+11\% / -16\%)$ .

- The $15^{\text{th}}$ five-year urban renewal plan is hardly a game changer: On 28 May, State Council released the $15^{\text{th}}$ five-year plan for urban renewal. The plan includes doubling the number of dilapidated urban housing renovations from 250K units under the $14^{\text{th}}$ five-year plan to 500K units, and targeting to renovate 4,000 urban villages (the $14^{\text{th}}$ five-year plan: 4,100). The plan also allows local governments to issue special bonds to fund urban renewal projects. That said, we are not particularly excited about the plan because (1) cash compensation for the urban village renovation (i.e. compensating relocated residents with cash to buy private residential units) was not mentioned, and we see limited impact on residential sales for now; (2) the overall direction is similar to previous narratives; and (3) the policy goal is more to improve people's living standards, rather than to stimulate the housing market.   
- Contracted sales not yet showing meaningful improvement, but also not getting worse: On an M/M basis, contracted sales rose 11%. However, the improvement is largely due to seasonality, as May is typically a relatively stronger month than April (Table 3). On a 4-year average basis, sales stayed at -71% in May (same as April). Looking ahead, as June is usually the strongest month for sales (as developers are pushing to meet half-year targets), we expect M/M growth to stay positive, but on a Y/Y basis, we forecast sales to remain on a broadly flattish trend (+/- 5% Y/Y).   
- SOEs' sales stayed positive Y/Y for the $2^{\text{nd}}$ consecutive month: On a Y/Y basis, SOE developers' sales rose 6% Y/Y in May (April: +19%), while POE/distressed developers' sales fell 50%/30% Y/Y, respectively (April: -23%/-39% Y/Y) (Figure 3). Compared to the 4-year average, SOE developers' sales improved from -10% in April to -3% in May, but POE/distressed developers' were still down \~90% (Figure 4).   
- COLI and CR Land continue to see solid sales momentum: In May alone (on a total basis), 5 SOE developers achieved double-digit Y/Y sales growth (Figure 6) - CR Land (+28%), CMSK (+20%), Yuexiu (+18%), COLI (+14%) and C&D (+13%). As for Jinmao (the outperformer over the past 12 months), contracted sales fell 16% Y/Y in May, but this is mostly due to fewer new launches (1 new launch in 2026 vs. 6 new launches in 2025); on a year-to-date (5M26) basis, Jinmao's sales have maintained a +11% Y/Y growth,

# Mainland China/Hong Kong Property & Conglomerates

Karl Chan AC

(852) 2800-8513

karl.chan@JPM.com

Venus Choi

(852) 2800-8599

venus.choi@JPM.com

Jocelyn Gao

(852) 2800-8529

jocelyn.gao@JPM.com

JPM Securities (Asia Pacific) Limited/ JPM Broking (Hong Kong) Limited

making it one of the four key developers with positive Y/Y growth in 5M26, with the others being COLI (+14%), CMSK (+13%) and CR Land (+8%) (Figure 5).

# Developers' Contracted Sales

Table 1: Contracted sales leaderboard – 5M26 top 30 developers by attributable sales 

<table><tr><td rowspan="2">5M26 Rank</td><td rowspan="2">5M25 Rank</td><td rowspan="2"></td><td rowspan="2">Developer</td><td rowspan="2"></td><td rowspan="2">SOE?</td><td colspan="2">5M26</td><td colspan="2">May-26</td></tr><tr><td>Attri. Sales (Rmb bn)</td><td>Y/Y</td><td>Attri. Sales (Rmb bn)</td><td>Y/Y</td></tr><tr><td>1</td><td>2</td><td> $\uparrow 1$ </td><td>COLI</td><td>中海地产</td><td>Y</td><td>95</td><td>14%</td><td>25</td><td>13%</td></tr><tr><td>2</td><td>1</td><td> $\downarrow -1$ </td><td>Poly Developments</td><td>保利发展</td><td>Y</td><td>83</td><td>-9%</td><td>22</td><td>-3%</td></tr><tr><td>3</td><td>3</td><td> $\rightarrow 0$ </td><td>CR Land</td><td>华润置地</td><td>Y</td><td>66</td><td>14%</td><td>17</td><td>60%</td></tr><tr><td>4</td><td>4</td><td> $\rightarrow 0$ </td><td>China Merchants Shekou</td><td>招商蛇口</td><td>Y</td><td>47</td><td>2%</td><td>12</td><td>3%</td></tr><tr><td>5</td><td>7</td><td> $\uparrow 2$ </td><td>C&amp;D</td><td>建发房产</td><td>Y</td><td>40</td><td>-5%</td><td>11</td><td>13%</td></tr><tr><td>6</td><td>5</td><td> $\downarrow -1$ </td><td>Greentown</td><td>绿城中国</td><td>Y</td><td>33</td><td>-27%</td><td>9</td><td>-40%</td></tr><tr><td>7</td><td>10</td><td> $\uparrow 3$ </td><td>China Jinmao</td><td>中国金茂</td><td>Y</td><td>29</td><td>11%</td><td>7</td><td>-16%</td></tr><tr><td>8</td><td>8</td><td> $\rightarrow 0$ </td><td>Yuexiu Property</td><td>越秀地产</td><td>Y</td><td>24</td><td>-27%</td><td>7</td><td>19%</td></tr><tr><td>9</td><td>12</td><td> $\uparrow 3$ </td><td>Greenland Holdings</td><td>绿地控股</td><td>N</td><td>21</td><td>-7%</td><td>8</td><td>36%</td></tr><tr><td>10</td><td>6</td><td> $\downarrow -4$ </td><td>Vanke</td><td>万科</td><td>N</td><td>21</td><td>-52%</td><td>5</td><td>-44%</td></tr><tr><td>11</td><td>11</td><td> $\rightarrow 0$ </td><td>China Railway Construction</td><td>中国铁建</td><td>Y</td><td>17</td><td>-26%</td><td>4</td><td>26%</td></tr><tr><td>12</td><td>13</td><td> $\uparrow 1$ </td><td>Binjiang</td><td>滨江集团</td><td>N</td><td>16</td><td>-24%</td><td>4</td><td>-5%</td></tr><tr><td>13</td><td>15</td><td> $\uparrow 2$ </td><td>China Construction Yipin</td><td>中建壹品</td><td>Y</td><td>14</td><td>-14%</td><td>3</td><td>-16%</td></tr><tr><td>14</td><td>16</td><td> $\uparrow 2$ </td><td>CSCEC Dongfu</td><td>中建东孚</td><td>Y</td><td>13</td><td>-6%</td><td>1</td><td>-68%</td></tr><tr><td>15</td><td>17</td><td> $\uparrow 2$ </td><td>Poly Property</td><td>保利置业</td><td>Y</td><td>13</td><td>-6%</td><td>3</td><td>-2%</td></tr><tr><td>16</td><td>21</td><td> $\uparrow 5$ </td><td>China Railway Group</td><td>中国中铁</td><td>Y</td><td>12</td><td>22%</td><td>3</td><td>38%</td></tr><tr><td>17</td><td>18</td><td> $\uparrow 1$ </td><td>Country Garden</td><td>碧桂园</td><td>N</td><td>12</td><td>-16%</td><td>3</td><td>-15%</td></tr><tr><td>18</td><td>9</td><td> $\downarrow -9$ </td><td>Huafa Industrial</td><td>华发股份</td><td>Y</td><td>10</td><td>-62%</td><td>2</td><td>-50%</td></tr><tr><td>19</td><td>19</td><td> $\rightarrow 0$ </td><td>HOROY Real Estate</td><td>鸿荣源集团</td><td>N</td><td>10</td><td>-26%</td><td>6</td><td>188%</td></tr><tr><td>20</td><td>22</td><td> $\uparrow 2$ </td><td>Dahua</td><td>大华集团</td><td>N</td><td>10</td><td>4%</td><td>3</td><td>39%</td></tr><tr><td>21</td><td>41</td><td> $\uparrow 20$ </td><td>Lianfa</td><td>联发集团</td><td>Y</td><td>9</td><td>60%</td><td>3</td><td>143%</td></tr><tr><td>22</td><td>23</td><td> $\uparrow 1$ </td><td>CCCG Real Estate</td><td>中交房地产</td><td>Y</td><td>9</td><td>0%</td><td>2</td><td>-13%</td></tr><tr><td>23</td><td>14</td><td> $\downarrow -9$ </td><td>Longfor</td><td>龙湖集团</td><td>N</td><td>9</td><td>-53%</td><td>2</td><td>-53%</td></tr><tr><td>24</td><td>38</td><td> $\uparrow 14$ </td><td>Beijing Urban Construction</td><td>北京城建</td><td>Y</td><td>8</td><td>20%</td><td>3</td><td>214%</td></tr><tr><td>25</td><td>25</td><td> $\rightarrow 0$ </td><td>Xiamen ITG Holding</td><td>国贸地产</td><td>Y</td><td>7</td><td>-16%</td><td>2</td><td>7%</td></tr><tr><td>26</td><td>31</td><td> $\uparrow 5$ </td><td>Xiangyu Construction</td><td>象屿地产</td><td>Y</td><td>7</td><td>-11%</td><td>2</td><td>11%</td></tr><tr><td>27</td><td>34</td><td> $\uparrow 7$ </td><td>China Galaxy</td><td>星河控股</td><td>N</td><td>6</td><td>-5%</td><td>2</td><td>6%</td></tr><tr><td>28</td><td>60</td><td> $\uparrow 32$ </td><td>Guangzhou Metro</td><td>广州地铁地产</td><td>Y</td><td>6</td><td>59%</td><td>2</td><td>51%</td></tr><tr><td>29</td><td>33</td><td> $\uparrow 4$ </td><td>Power Construction</td><td>电建地产</td><td>Y</td><td>6</td><td>-24%</td><td>2</td><td>32%</td></tr><tr><td>30</td><td>20</td><td> $\downarrow -10$ </td><td>China Energy Engineering Urban Con.</td><td>能建城发</td><td>Y</td><td>6</td><td>-46%</td><td>2</td><td>3%</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-11%</td><td></td><td>3%</td></tr></table>

Note: The table above is based on an attributable basis, not total basis (which is shown in some tables below). Source: CREIS, Company data

Figure 1: CREIS top 100 developers' aggregate attributable contracted sales Y/Y growth and vs. 2018-21 average   
![](images/120c3dc08d6ea802d33736df0ebabd41dfc1d53d53f5048031596b122fa91916.jpg)

<details>
<summary>line</summary>

| Month    | Y/Y   | vs. 2018-21 avg |
|----------|-------|-----------------|
| Jul-23   | -31%  | -60%            |
| Aug-23   | -31%  | -55%            |
| Sep-23   | -23%  | -61%            |
| Oct-23   | -35%  | -61%            |
| Nov-23   | -34%  | -59%            |
| Dec-23   | -39%  | -63%            |
| Jan-24   | -37%  | -64%            |
| Feb-24   | -71%  | -71%            |
| Mar-24   | -42%  | -56%            |
| Apr-24   | -46%  | -65%            |
| May-24   | -34%  | -66%            |
| Jun-24   | -14%  | -66%            |
| Jul-24   | -26%  | -71%            |
| Aug-24   | -29%  | -68%            |
| Sep-24   | -40%  | -77%            |
| Oct-24   | 17%   | -64%            |
| Nov-24   | -1%   | -65%            |
| Dec-24   | -12%  | -63%            |
| Jan-25   | -12%  | -68%            |
| Feb-25   | 18%   | -66%            |
| Mar-25   | -14%  | -62%            |
| Apr-25   | -12%  | -70%            |
| May-25   | -13%  | -70%            |
| Jun-25   | -25%  | -75%            |
| Jul-25   | -22%  | -77%            |
| Aug-25   | -8%   | -71%            |
| Sep-25   | -6%   | -78%            |
| Oct-25   | -40%  | -73%            |
| Nov-25   | -35%  | -77%            |
| Dec-25   | -17%  | -70%            |
| Jan-26   | -21%  | -75%            |
| Feb-26   | -40%  | -80%            |
| Mar-26   | -18%  | -69%            |
| Apr-26   | -5%   | -71%            |
| May-26   | -4%   | -71%            |
</details>

Source: CREIS, CRIC

Figure 2: CREIS top 100 developers' aggregate contracted sales by month (2019-2025) vs. 2018-21 average   
![](images/df8e717ea8168d5ff5c8250363ad4bd0f3e6ae88a080a1407de2075c8f3d9e51.jpg)

<details>
<summary>bar_line</summary>

| Month | 2019 (Rmb billion) | 2020 (Rmb billion) | 2021 (Rmb billion) | 2022 (Rmb billion) | 2023 (Rmb billion) | 2024 (Rmb billion) | 2025 (Rmb billion) | 2026 (Rmb billion) | vs. 2018-21 avg (%) |
|---|---|---|---|---|---|---|---|---|---|
| Jan | 500 | 350 | 720 | 450 | 300 | 150 | 150 | 150 | -75 |
| Feb | 650 | 380 | 620 | 300 | 400 | 100 | 100 | 100 | -80 |
| Mar | 680 | 580 | 930 | 400 | 550 | 200 | 220 | 220 | -69 |
| Apr | 680 | 680 | 850 | 450 | 450 | 180 | 180 | 180 | -71 |
| May | 720 | 780 | 930 | 450 | 400 | 180 | 220 | 220 | -71 |
| Jun | 1150 | 1050 | 1000 | 570 | 400 | 180 | 250 | 250 | — |
| Jul | 670 | 830 | 720 | 420 | 300 | — | 170 | — | — |
| Aug | 470 | 800 | 650 | 410 | 280 | — | 190 | — | — |
| Sep | 930 | — | 730 | 420 | 330 | — | 180 | — | — |
| Oct | 780 | — | 610 | 450 | 310 | — | 210 | — | — |
| Nov | 760 | — | 710 | 490 | 330 | — | 180 | — | — |
| Dec | 1110 | — | 810 | 610 | — | — | — | — | — |
Compared to 2018-21 average
</details>

Note: As CREIS data is only available since June 2019, data before June 2019 is from CRIC   
Source: CREIS, CRIC

Table 2: Top 100 developers' monthly contracted sales (Rmb billion) 

<table><tr><td></td><td>Jan</td><td>Feb</td><td>Mar</td><td>Apr</td><td>May</td><td>Jun</td><td>Jul</td><td>Aug</td><td>Sep</td><td>Oct</td><td>Nov</td><td>Dec</td></tr><tr><td>2017</td><td>362</td><td>334</td><td>581</td><td>455</td><td>446</td><td>645</td><td>404</td><td>430</td><td>539</td><td>514</td><td>583</td><td>879</td></tr><tr><td>2018</td><td>556</td><td>443</td><td>597</td><td>571</td><td>686</td><td>878</td><td>664</td><td>617</td><td>705</td><td>664</td><td>712</td><td>937</td></tr><tr><td>2019</td><td>509</td><td>402</td><td>669</td><td>666</td><td>723</td><td>1,161</td><td>671</td><td>466</td><td>914</td><td>780</td><td>761</td><td>1,093</td></tr><tr><td>2020</td><td>347</td><td>347</td><td>583</td><td>697</td><td>798</td><td>1,044</td><td>820</td><td>793</td><td>989</td><td>987</td><td>975</td><td>1,298</td></tr><tr><td>2021</td><td>722</td><td>629</td><td>928</td><td>842</td><td>925</td><td>991</td><td>725</td><td>652</td><td>723</td><td>614</td><td>700</td><td>808</td></tr><tr><td>2022</td><td>461</td><td>299</td><td>408</td><td>350</td><td>448</td><td>570</td><td>416</td><td>410</td><td>423</td><td>457</td><td>488</td><td>627</td></tr><tr><td>2023</td><td>305</td><td>406</td><td>527</td><td>443</td><td>402</td><td>400</td><td>288</td><td>282</td><td>323</td><td>296</td><td>323</td><td>380</td></tr><tr><td>2024</td><td>192</td><td>131</td><td>306</td><td>241</td><td>266</td><td>343</td><td>212</td><td>199</td><td>195</td><td>347</td><td>277</td><td>378</td></tr><tr><td>2025</td><td>169</td><td>155</td><td>263</td><td>211</td><td>232</td><td>256</td><td>165</td><td>184</td><td>184</td><td>208</td><td>180</td><td>312</td></tr><tr><td>2026</td><td>133</td><td>93</td><td>215</td><td>201</td><td>224</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Note: As CREIS data is only available since June 2019, data prior to June 2019 is from CRIC   
Source: CREIS, CRIC

Table 3: Top 100 developers' contracted sales monthly distribution 

<table><tr><td></td><td>Jan</td><td>Feb</td><td>Mar</td><td>Apr</td><td>May</td><td>Jun</td><td>Jul</td><td>Aug</td><td>Sep</td><td>Oct</td><td>Nov</td><td>Dec</td></tr><tr><td>2016</td><td>5.9%</td><td>4.0%</td><td>8.6%</td><td>8.3%</td><td>8.9%</td><td>10.9%</td><td>7.2%</td><td>7.7%</td><td>11.0%</td><td>10.9%</td><td>8.2%</td><td>8.3%</td></tr><tr><td>2017</td><td>6.5%</td><td>5.8%</td><td>10.1%</td><td>7.9%</td><td>7.4%</td><td>9.8%</td><td>6.7%</td><td>7.7%</td><td>9.0%</td><td>9.1%</td><td>9.3%</td><td>10.8%</td></tr><tr><td>2018</td><td>7.6%</td><td>5.4%</td><td>8.0%</td><td>7.4%</td><td>8.3%</td><td>11.5%</td><td>8.0%</td><td>7.4%</td><td>8.9%</td><td>8.8%</td><td>8.7%</td><td>9.9%</td></tr><tr><td>2019</td><td>5.8%</td><td>5.2%</td><td>8.3%</td><td>8.0%</td><td>8.5%</td><td>11.2%</td><td>7.4%</td><td>8.0%</td><td>9.6%</td><td>9.3%</td><td>9.5%</td><td>9.2%</td></tr><tr><td>2020</td><td>4.8%</td><td>2.6%</td><td>6.6%</td><td>7.1%</td><td>8.5%</td><td>11.5%</td><td>8.5%</td><td>9.3%</td><td>10.1%</td><td>9.9%</td><td>9.9%</td><td>11.3%</td></tr><tr><td>2021</td><td>7.6%</td><td>6.5%</td><td>9.3%</td><td>9.2%</td><td>10.0%</td><td>11.1%</td><td>7.7%</td><td>7.4%</td><td>7.3%</td><td>7.8%</td><td>7.3%</td><td>8.9%</td></tr><tr><td>2022</td><td>8.6%</td><td>5.6%</td><td>7.6%</td><td>6.5%</td><td>8.4%</td><td>10.6%</td><td>7.8%</td><td>7.7%</td><td>7.9%</td><td>8.5%</td><td>9.1%</td><td>11.7%</td></tr><tr><td>2023</td><td>7.0%</td><td>9.3%</td><td>12.1%</td><td>10.1%</td><td>9.2%</td><td>9.1%</td><td>6.6%</td><td>6.4%</td><td>7.4%</td><td>6.8%</td><td>7.4%</td><td>8.7%</td></tr><tr><td>2024</td><td>6.2%</td><td>4.3%</td><td>9.9%</td><td>7.8%</td><td>8.6%</td><td>11.1%</td><td>6.9%</td><td>6.5%</td><td>6.3%</td><td>11.2%</td><td>9.0%</td><td>12.2%</td></tr><tr><td>2025</td><td>6.7%</td><td>6.1%</td><td>10.4%</td><td>8.4%</td><td>9.2%</td><td>10.2%</td><td>6.6%</td><td>7.3%</td><td>7.3%</td><td>8.3%</td><td>7.1%</td><td>12.4%</td></tr><tr><td>Average (2016-25)</td><td>6.7%</td><td>5.5%</td><td>9.1%</td><td>8.1%</td><td>8.7%</td><td>10.7%</td><td>7.3%</td><td>7.5%</td><td>8.5%</td><td>9.1%</td><td>8.5%</td><td>10.3%</td></tr></table>

Source: CREIS, CRIC

Figure 3: Key developers' contracted sales Y/Y growth by type   
![](images/cea7cedc69656cac4e756565a2f69d740362b80625946a701627265a34b8087b.jpg)

<details>
<summary>line</summary>

| Month   | SOE   | Private | Distressed |
|---------|-------|---------|------------|
| Jan 24  | -27%  | -40%    | -51%       |
| Feb 24  | -63%  | -63%    | -70%       |
| Mar 24  | -32%  | -58%    | -61%       |
| Apr 24  | -37%  | -59%    | -49%       |
| May 24  | -22%  | -44%    | -51%       |
| Jun 24  | 9%    | -44%    | -44%       |
| Jul 24  | -18%  | -37%    | -41%       |
| Aug 24  | -21%  | -52%    | -29%       |
| Sep 24  | -34%  | -53%    | -49%       |
| Oct 24  | 23%   | -41%    | -22%       |
| Nov 24  | -5%   | -38%    | -27%       |
| Dec 24  | 22%   | -35%    | -30%       |
| Jan 25  | -4%   | -49%    | -29%       |
| Feb 25  | 24%   | -31%    | -26%       |
| Mar 25  | -2%   | -38%    | -35%       |
| Apr 25  | -14%  | -53%    | -49%       |
| May 25  | -2%   | -33%    | -33%       |
| Jun 25  | -22%  | -43%    | -36%       |
| Jul 25  | -11%  | -43%    | -28%       |
| Aug 25  | 0%    | -44%    | -33%       |
| Sep 25  | 10%   | -40%    | -35%       |
| Oct 25  | -40%  | -51%    | -42%       |
| Nov 25  | -27%  | -59%    | -45%       |
| Dec 25  | -8%   | -56%    | -44%       |
| Jan 26  | -6%   | -48%    | -45%       |
| Feb 26  | -31%  | -62%    | -47%       |
| Mar 26  | -7%   | -58%    | -36%       |
| Apr 26  | 19%   | -39%    | -39%       |
| May 26  | 6%    | -50%    | -30%       |
</details>

Source: CREIS, Company data

Figure 4: Key developers' contracted sales vs. 2018-21 average by type   
![](images/fe3d6109175e36a28d7d38ee3e45a75eee12549ba9bd17440b6555c6d4ccde43.jpg)

<details>
<summary>line</summary>

| Month   | SOE   | Private | Distressed |
|---------|-------|---------|------------|
| Jan 24  | -31%  | -60%    | -79%       |
| Feb 24  | -28%  | -51%    | -81%       |
| Mar 24  | 13%   | -63%    | -81%       |
| Apr 24  | -12%  | -69%    | -80%       |
| May 24  | -14%  | -70%    | -84%       |
| Jun 24  | -15%  | -75%    | -85%       |
| Jul 24  | -33%  | -71%    | -87%       |
| Aug 24  | -33%  | -75%    | -85%       |
| Sep 24  | -36%  | -79%    | -89%       |
| Oct 24  | 18%   | -73%    | -84%       |
| Nov 24  | -5%   | -76%    | -87%       |
| Dec 24  | -13%  | -80%    | -85%       |
| Jan 25  | -

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 01 Jun 2026 07:13 AM HKT

Disseminated 01 Jun 2026 07:14 AM HKT
"""
