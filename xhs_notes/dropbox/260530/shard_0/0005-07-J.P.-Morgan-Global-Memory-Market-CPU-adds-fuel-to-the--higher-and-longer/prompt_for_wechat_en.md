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
# Global Memory Market

CPU adds fuel to the ‘higher and longer’ upcycle thesis and 28E TAM at \$1.7trn; valuation framework transition in progress

- Memory demands broaden out from GPU to CPU. CPU compute workload for AI is accelerating for orchestration (task coordination and logic), state management, and API execution. We have witnessed strong traction in Vera CPU adoption and expect major CSP customers to launch their own in-house CPU (e.g. Graviton/Axion) from 2H27 onwards. The CPU-to-GPU ratio has consistently trended up over the past three years (from 5.4:1 in '23 to 3.2:1 in '25) and we estimate it moving up to 2.4:1 by 28E (major reason behind 20-22% FY27E-28E server-grade DDR/LPDDR5 bit demand upward revision). We forecast AI CPU DRAM (headnode and standalone) demand at 11mn/17mn GB for FY27E-28E (19%/24% of total market demand). In the long term, Physical and World AI are the next areas of growth and a series of new applications (e.g. wearable and humanoid) are under development.   
- Higher Memory TAM, S-D shortage likely to worsen next year, LTA remains to ASP stabilization. Reflecting CoWoS model upward revisions (note), CPU memory upside, and CE demand degrade, we revise up our FY26E-28E memory TAM by 37-53% (vs Mar-26 model) and expect S-D shortage to worsen. This could theoretically add further upside risk to pricing for DRAM/NAND next year after a 220-250% y-y increase this year; however, we see a rather stable pricing trend supported by an increase in LTA contract sales mix. We estimate the Memory TAM will further expand to US\$1.3trn in 27E with \~50% market cap upside throughout next year using a 3.6x P/S multiple. Upside could be greater if we use the Market Cap to OP approach as memory stocks trade at a discount to their earnings (Figures 2-4 for details).   
- HBM ASP upside risk from tighter S-D, higher wafer allocation trend continues. We have introduced a new HBM S-D view with higher TAM (17-21% upward revision through 26E-28E) and the key changes are: i) ASIC demand acceleration (ASIC bit mix up from 33% in 26E to 39% in 27E), ii) NVDA Rubin GPU forecast cut in 26E offset by stronger GB build, iii) conservative HBM4E content assumption reflecting a longer 12Hi product life-cycle. Given the \$/bit crossover between HBM and non-HBM, we expect memory makers to turn vocal on raising HBM ASP next year (JPMe: +10% y-y on a like-for-like and +30% on a blended basis). As the HBM bit installation demand CAGR (+85% in the next three years) continues to outpace the rest of the market, we believe DRAM wafer capacity allocation to HBM will continue to rise (from 24% in 26E to 31% in 28E) adding greater pressure on conventional DRAM S-D.   
- Memory gains substantial value within CSP capex, higher hardware spending to add confidence to memory earnings. Memory is turning into a strategic asset (MU CEO interview) and we believe stable procurement is imperative for AI service operations for faster and high quality service quality. Memory as a % of total CSP hardware capex ranged between mid-teens % at the beginning of AI and is now anticipated to reach over half this year. Considering the importance of memory's role in AI compute systems, a higher value share is understandable, but many investors we have spoken to have

# Technology - Semiconductors

# Jay Kwon AC

(82-2) 758-5725

jay.h.kwon@JPM.com

JPM Securities (Far East) Limited, Seoul Branch

# Sangsik Lee

(82-2) 758 5146

sangsik.lee@JPM.com

JPM Securities (Far East) Limited, Seoul Branch

# Neelay Y Kamath

(91-22) 6157 3764

neelay.kamath@jpmchase.com

JPM India Private Limited

# Harlan Sur

(1-415) 315-6700

harlan.sur@JPM.com

JPM Securities LLC

# Mio Shikanai

(81-3) 6736 1313

mio.shikanai@JPM.com

JPM Securities Japan Co., Ltd.

expressed concerns surrounding memory's further value share hike next year. This is one of the major reasons why memory stocks continue to trade at a discount to EPS. Higher CSP hardware capex (JPM hardware research for details) and greater longevity (more evidence on NVDA's 2030E US\$3-4trn spending outlook commentary) should help alleviate concerns on memory earnings, in our view. Delayed utility infrastructure readiness or a slower new AI business model pickup could negatively impact hardware capex spending and eventually related memory demand.

- Enterprise SSD leads NAND TAM expansion, capex upward revision not yet meaningful. We see a clear trend in customers' preference for high-density and high-speed SSD with meaningful content growth (JPMe: over 40% GB per server increase y-y). We estimate the eSSD market to be over 500EB in 26E (43% of total NAND bit demand) and we forecast it to rise to over 1,100EB in the next two years at a +52% CAGR. Considering the ASP premium, eSSD value TAM could be over US\$300bn (larger than HBM TAM) in the next two years. On technology upfront, SLC based high speed SSD is gaining stronger traction on top of mainstream TLC SSD and we expect to see various solutions hitting the market from 2H26E (high I/OPs, HBF, and others). A growing SLC mix could be in favor of NAND S-D (higher bit per wafer trade-off vs TLC/QLC) as capex spending continues to remain below historical peak levels.   
- Capex acceleration to debottleneck the supply shortage. Sharp memory economics improvement and a multi-year shortage outlook incentivize suppliers to accelerate capex spending (JPMe: US\$450bn in the next three years vs US\$300bn from Dec-25 model). DRAM: CY28-end WSPM at 2.8mn (880k increase from CY25-end) with three years accumulated capex of US\$364bn. 60% of incremental WSPM allocation to HBM and capex-to-sales average at 13% in the next three years. EUV procurement and infrastructure build out capacity is a key bottleneck. NAND: CY28-end WSPM at 1.44mn (165k increase from CY25-end) with US\$86bn spending (three year combined basis). Majority of spend is on tech migration and greenfield capacity impact materializing from 2H28. Relatively lower priority vs DRAM among top 3 producers, but we are beginning to see evidence of 2029 greenfield projects.   
- China Competition Assessment. Volume share gains continue (DRAM share from 6% in '25 to 8-11% in 26E-28E and NAND share from 12% in '25 to 12-16% in 26E-28E) with above-industry capacity build out trends (DRAM/NAND capacity shares each at 18%/19% by CY28-end) and improving supply-chain localization. While all suppliers benefit from favorable S-D dynamics, inferior product mix likely limits the value share gain potential (DRAM/NAND value share at 10%/12% by CY28E). Key monitoring points are: 1) DRAM WSPM allocation amount to HBM (greater HBM wafer mix would result in tighter conventional DRAM S-D) and 2) Equipment export restriction policy update (i.e. MATCH Act - link).   
- Investment recommendations. The global memory sector continues to outperform the respective index and ecosystem peers 2026-YTD and we maintain our multi-year bullish view on the sector. Fundamental key drivers remain: a) AI demand broadening out to CPU, b) rising HBM wafer allocation with greater trade loss ratio, and c) supply discipline in NAND (i.e. under-investment continuing) with potential supply constraints via SLC demand pickup. We acknowledge that the path to a new valuation framework will likely be a patchy one; however, we argue that AI has introduced a new spectrum of demand profiles and view a new valuation approach as necessary (GMM: “LTA paves the path for a new valuation framework” for details). Our top buy ideas include Korea Memory (SKH > SEC in the near-term), Kioxia in Japan, Micron in the U.S. We also like Winbond from Taiwan (covered by Jimmy Huang). For the broader supply chain in Asia, we like TEL (SPE) in Japan and SIMO (covered by Gokul Hariharan) in the controller solution space. Lastly, we view the risk-reward balance as unfavorable in selective stocks (Hanmi).

# Key charts

Figure 1: Aggregate market cap vs leading memory market revenue trend (1Q ahead)   
![](images/09f922416ad0dd5b27d03ca14a84a10651bfbfeecd0d8ae967781ca1700663c9.jpg)

<details>
<summary>line</summary>

| Date    | Aggregate market cap rebased to 2014 (LHS) | Memory market revenue 1-Q ahead (RHS) |
|---------|---------------------------------------------|----------------------------------------|
| Dec-14  | ~100                                        | ~10                                    |
| Dec-15  | ~150                                        | ~15                                    |
| Dec-16  | ~200                                        | ~20                                    |
| Dec-17  | ~250                                        | ~25                                    |
| Dec-18  | ~300                                        | ~30                                    |
| Dec-19  | ~350                                        | ~35                                    |
| Dec-20  | ~400                                        | ~40                                    |
| Dec-21  | ~350                                        | ~35                                    |
| Dec-22  | ~300                                        | ~30                                    |
| Dec-23  | ~350                                        | ~35                                    |
| Dec-24  | ~400                                        | ~40                                    |
| Dec-25  | ~1,500                                      | ~1,50                                  |
| Dec-26  | ~2,000                                      | ~2,00                                  |
| Dec-27  | ~2,500                                      | ~2,50                                  |
</details>

Source: WSTS, OMDIA, Bloomberg Finance L.P., JPM estimates. Note: Market cap includes SEC, SK Hynix, Micron, Nanya Technology, Western Digital. Kioxia / SNDK added from 1Q25 and excluded WDC.

Figure 2: Memory TAM vs peak mkt cap/TAM analysis US\$bn, peak mkt cap/TAM (x)   
![](images/73c4d967ac7e10a20d5bb947653dd15891f9f165355acf635c8f6ca76fdf0170.jpg)

<details>
<summary>bar_line</summary>

| Year | Peak market cap. (US$bn) - LHS | Mkt cap / memory TAM - RHS |
| :--- | :--- | :--- |
| 2018 | 450 | 2.9 |
| 2021 | 663 | 4.3 |
| 2025 | 1,075 | 5.0 |
| 2026E YTD | 3,271 | 3.7 |
| 2027E (forecast) | 4,814 | 3.6 |
| 2028E (forecast) | 6,052 | 3.6 |
The chart also notes that 47% upside on 27E TAM (3.6x P/S multiple) and 85% upside on 28E TAM? The data points are annotated with percentages (47% and 85%) indicating relative multiples or changes between the two metrics.
</details>

Source: Bloomberg Finance L.P., WSTS, Company data, JPM estimates. Note: only considered SEC, SKH, and MU market cap.

Figure 3: Memory TAM vs peak mkt cap/memory OP analysis   
![](images/bda90e58679df28679e74095a7480e7a2cb496a55bd2e1d62ac5cc161183ab52.jpg)

<details>
<summary>bar_line</summary>

| Year | Peak market cap. (US$bn) - LHS | Mkt cap / memory OP - RHS |
| :--- | :--- | :--- |
| 2018 | 450 | 6.0 |
| 2021 | 663 | 15.8 |
| 2025 | 1,075 | 16.6 |
| 2026E YTD | 3,271 | 4.9 |
| 2027E (forecast) | 6,180 | 6.0 |
| 2028E (forecast) | 7,675 | 6.0 |
Higher upside potential on profit base vs. P/S 89% upside on 27E OP
</details>

Source: Bloomberg Finance L.P., WSTS, Company data, JPM estimates. Note: only considered SEC, SKH, and MU market cap.

Figure 4: Memory TAM vs Memory OPM   
![](images/da6c05953c2f1fbc5f3f7488ab22a965158b06f7b4baee79f986e40c4ff9ee52.jpg)

<details>
<summary>bar_line</summary>

| Year | Memory TAM (US$bn) | Memory OPM (%) |
| :--- | :--- | :--- |
| 2018 | 155 | 48 |
| 2021 | 153 | 27 |
| 2025 | 214 | 30 |
| 2026E (forecast) | 896 | 75 |
| 2027E (forecast) | 1,337 | 77 |
| 2028E (forecast) | 1,681 | 76 |
New norm OPM at high-70%
</details>

Source: Bloomberg Finance L.P., WSTS, Company data, JPM estimates. Note: only considered SEC, SKH, and MU market cap.

Figure 5: CSP capex and AI memory % share   
![](images/d3f9314746fc84e6f41cb8414996e832cd20742e27f7300831ff3951481e8bcd.jpg)

<details>
<summary>bar_line</summary>

| Year | JPMe CSP capex (US$bn) | NVDAe CSP capex (US$bn) | Memory as % of CSP capex (RHS) (%) |
| :--- | :--- | :--- | :--- |
| 2022 | 150 | - | 20 |
| 2023 | 160 | - | 9 |
| 2024 | 250 | - | 15 |
| 2025 | 400 | - | 16 |
| 2026E | 669 | - | 52 |
| 2027E | 991 | 1000 | 73 |
| 2030E | - | - | - |
CSP hardware capex move up critical for memory to keep value share above 50?
</details>

Source: Company data, Bloomberg Finance L.P., JPM estimates.

Table 1: Market cap changes across AI ecosystem partners   
US\$bn, % 

<table><tr><td>US$bn</td><td>Top 4 CSP</td><td>AI semi</td><td>Foundry</td><td>Memory</td><td>AI ecosystem mkt cap.</td><td>SOX</td><td>NASDAQ index</td><td>DOW Jones index</td></tr><tr><td>1Q24</td><td>8,122</td><td>3,226</td><td>632</td><td>595</td><td>12,575</td><td>5,795</td><td>39,807</td><td>5,254</td></tr><tr><td>2Q24</td><td>8,871</td><td>4,109</td><td>772</td><td>623</td><td>14,376</td><td>6,991</td><td>39,119</td><td>5,460</td></tr><tr><td>3Q24</td><td>8,652</td><td>4,113</td><td>784</td><td>491</td><td>14,039</td><td>6,900</td><td>42,330</td><td>5,762</td></tr><tr><td>4Q24</td><td>9,243</td><td>4,667</td><td>850</td><td>395</td><td>15,156</td><td>7,306</td><td>42,544</td><td>5,882</td></tr><tr><td>1Q25</td><td>8,162</td><td>3,651</td><td>711</td><td>423</td><td>12,947</td><td>6,040</td><td>42,002</td><td>5,612</td></tr><tr><td>2Q25</td><td>10,027</td><td>5,448</td><td>940</td><td>557</td><td>16,972</td><td>8,481</td><td>44,095</td><td>6,205</td></tr><tr><td>3Q25</td><td>10,979</td><td>6,427</td><td>1,111</td><td>721</td><td>19,238</td><td>10,022</td><td>46,398</td><td>6,688</td></tr><tr><td>4Q25</td><td>11,508</td><td>6,594</td><td>1,280</td><td>1,145</td><td>20,526</td><td>10,608</td><td>48,063</td><td>6,846</td></tr><tr><td>1Q26</td><td>9,907</td><td>6,122</td><td>1,424</td><td>1,411</td><td>18,863</td><td>10,738</td><td>46,342</td><td>6,529</td></tr><tr><td>2Q26YTD</td><td>12,435</td><td>8,233</td><td>1,948</td><td>3,369</td><td>25,986</td><td>15,469</td><td>50,669</td><td>7,564</td></tr></table>

% chaqnes 

<table><tr><td>2Q24</td><td>9%</td><td>27%</td><td>22%</td><td>5%</td><td>14%</td><td>21%</td><td>-2%</td><td>4%</td></tr><tr><td>3Q24</td><td>-2%</td><td>0%</td><td>1%</td><td>-21%</td><td>-2%</td><td>-1%</td><td>8%</td><td>6%</td></tr><tr><td>4Q24</td><td>7%</td><td>13%</td><td>8%</td><td>-19%</td><td>8%</td><td>6%</td><td>1%</td><td>2%</td></tr><tr><td>1Q25</td><td>-12%</td><td>-22%</td><td>-16%</td><td>7%</td><td>-15%</td><td>-17%</td><td>-1%</td><td>-5%</td></tr><tr><td>2Q25</td><td>23%</td><td>49%</td><td>32%</td><td>31%</td><td>31%</td><td>40%</td><td>5%</td><td>11%</td></tr><tr><td>3Q25</td><td>9%</td><td>18%</td><td>18%</td><td>30%</td><td>13%</td><td>18%</td><td>5%</td><td>8%</td></tr><tr><td>4Q25</td><td>5%</td><td>3%</td><td>15%</td><td>59%</td><td>7%</td><td>6%</td><td>4%</td><td>2%</td></tr><tr><td>1Q26</td><td>-14%</td><td>-7%</td><td>11%</td><td>23%</td><td>-8%</td><td>1%</td><td>-4%</td><td>-5%</td></tr><tr><td>2Q26YTD</td><td>26%</td><td>34%</td><td>37%</td><td>139%</td><td>38%</td><td>44%</td><td>9%</td><td>16%</td></tr></table>

mkt cap. mix within the AI ecosystem 

<table><tr><td>1Q24</td><td>65%</td><td>26%</td><td>5%</td><td>5%</td><td>100%</td><td rowspan="4"></td></tr><tr><td>2Q24</td><td>62%</td><td>29%</td><td>5%</td><td>4%</td><td>100%</td></tr><tr><td>3Q24</td><td>62%</td><td>29%</td><td>6%</td><td>3%</td><td>100%</td></tr><tr><td>4Q24</td><td>61%</td><td>31%</td><td>6%</td><td>3%</td><td>100%</td></tr><tr><td>1Q25</td><td>63%</td><td>28%</td><td>5%</td><td>3%</td><td>100%</td><td rowspan="4"></td></tr><tr><td>2Q25</td><td>59%</td><td>32%</td><td>6%</td><td>3%</td><td>100%</td></tr><tr><td>3Q25</td><td>57%</td><td>33%</td><td>6%</td><td>4%</td><td>100%</td></tr><tr><td>4Q25</td><td>56%</td><td>32%</td><td>6%</td><td>6%</td><td>100%</td></tr><tr><td>1Q26</td><td>53%</td><td>32%</td><td>8%</td><td>7%</td><td>100%</td><td rowspan="2"></td></tr><tr><td>2Q26YTD</td><td>48%</td><td>32%</td><td>7%</td><td>13%</td><td>100%</td></tr></table>

Source: Bloomberg Finance L.P., Note: 1) Top 4 CSP includes GOOG/MSFT/AMZN/META;; 2) AI semi includes NVDA/AMD/AVGO/MRVL; 3) Foundry includes TSMC; 4) Memory includes SKH/MU/SEC; 5) NASDAQ and DJIS in index vs others in absolute market cap; 6) Market cap. based on qtr-end; 7) colors indicate % performance rank within the qtr.

Table 2: OPM comparison across AI ecosystem partners   
% 

<table><tr><td>OPM comparison</td><td>2022</td><td>2023</td><td>2024</td><td>2025</td><td>2026E</td><td>2027E</td><td>2028E</td></tr><tr><td>CSP Cloud</td><td>29%</td><td>29%</td><td>35%</td><td>36%</td><td>37%</td><td>38%</td><td>39%</td></tr><tr><td>AI Semi</td><td>39%</td><td>49%</td><td>57%</td><td>57%</td><td>63%</td><td>64%</td><td>63%</td></tr><tr><td>Memory</td><td>23%</td><td>-30%</td><td>26%</td><td>36%</td><td>76%</td><td>75%</td><td>72%</td></tr><tr><td>Foundry</td><td>46%</td><td>40%</td><td>42%</td><td>49%</td><td>56%</td><td>55%</td><td>56%</td></tr></table>

Source: Company data, JPM estimates, Bloomberg Finance L.P. \*note: Memory OPM includes both DRAM and NAND.

Figure 6: DRAM bit demand vs bit supply   
![](images/e2c33169fbabb6038e212a039713dd23c79d72cb8e15c378194315b4f07a0ba3.jpg)

<details>
<summary>bar</summary>

| Year | DRAM bit demand (%) | DRAM bit shipment (%) |
| :--- | :--- | :--- |
| 2025A | 20.9 | 19.4 |
| 2026E | 32.5 | 22.9 |
| 2027E | 34.4 | 21.7 |
| 2028E | 21.1 | 23.8 |
</details>

Source: JPM estimates.

Figure 7: NAND bit demand vs bit supply   
![](images/dec3830f8afaaa7bf1a30a75304c23d525dfc54720b059473666bf4039e9f18f.jpg)

<details>
<summary>bar</summary>

| Year | NAND bit demand (%) | NAND bit shipment (%) |
| :--- | :--- | :--- |
| 2025A | 19.3 | 14.5 |
| 2026E | 23.0 | 19.8 |
| 2027E | 29.4 | 21.2 |
| 2028E | 22.3 | 20.9 |
</details>

Source: JPM estimates.

Figure 8: DRAM bit demand vs bit consumption vs bit supply in absolute terms   
![](images/2b8c0b8ff9a8528a536f35459d042e58bf21a3433929ba22ad72860f1d3a6713.jpg)

<details>
<summary>bar</summary>

| Year | Bit demand (M) | Bit consumption (M) | Bit supply (M) |
| :--- | :--- | :--- | :--- |
| 2025A | 37,000 | 38,000 | 38,000 |
| 2026E | 50,000 | 49,000 | 46,000 |
| 2027E | 67,000 | 61,000 | 57,000 |
| 2028E | 81,000 | 73,000 | 71,000 |
</details>

Source: JPM estimates.

Figure 10: DRAM capex and Y/Y trend   
![](images/1aad15e98352665b871f769d704ecd85a0ef2b1e3f8c66e6c27d67669694d28d.jpg)

<details>
<summary>bar_line</summary>

| Year | DRAM capex (US$

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 29 May 2026 09:53 PM HKT

Disseminated 29 May 2026 09:54 PM HKT
"""
