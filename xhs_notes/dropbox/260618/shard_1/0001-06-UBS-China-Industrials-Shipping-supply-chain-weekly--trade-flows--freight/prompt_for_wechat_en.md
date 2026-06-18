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
## First Read

# China Industrials

Shipping supply chain weekly: trade flows, freight and Hormuz updates (week 24)

## Key highlights from high-frequency data

We compile weekly data from UBS Evidence Lab, the Ministry of Transport, UBS Evidence Lab and other third-party data providers to track the latest trade flows across shipping, shipbuilding and ports.

## Hormuz reopen may result in recovery of VLCC average earnings

Oil and tanker stocks moved reacted positively to the US-Iran peace agreement, with sentiment supported by the announced reopening of the Strait of Hormuz. While daily vessel transits through the Strait of Hormuz remained constrained in early June. VLCC average earnings from Middle East/West Africa to China remained flattish while earnings from US Gulf to China remained stable last week, with average earnings below US\$100k/day.

## Container shipping volume keep rising

Container throughput at key ports in China declined 1% WoW while increasing 5% YoY last week. Amid a pick-up in shipping demand, main lane freight rates saw further gains: overall SCFI freight rates increased by 9% WoW last week (+43% YoY), with Shanghai-Europe +18% WoW and Transpacific +10-12% WoW; Port of LA imports were up 7% YoY in week 24 and estimated to grow \~7% YoY in week 25. Intra-Asia containership chartering index recovered by 0.5% WoW last week. Based on our Maritime Destination Monitor (> Access Dataset), the container shipping volume in Asia-US route showed strong YoY growth since May.

## BDI & earnings of bulker and new build price remained elevated

The bulker market softened last week, with BDI down 10% WoW and average earnings of capesize bulker down 18% WoW, but BDI has still recorded a 61% rally YTD. The shipbuilding newbuild price index remained flattish WoW last week.

## Equities

China

Industrial

Robin Xu

Analyst

bin.xu@ubs.com

+86-21-3866 8872

Zed Sheng

Analyst

S1460525030003

zed.sheng@ubs.com

+86-21-3866 8730

Cristian Nedelcu, CFA

Analyst

cristian.nedelcu@ubs.com

+44-20-7568 4375

William Deng

Economist

william-w.deng@ubs.com

+852-2971 6765

Xin Chen

Analyst

S1460511050002

xin.chen@ubs.com

+86-21-3866 8864

Figure 1: Middle East/US Gulf/West Africa-China VLCC TCE +99%/-17%/-49% vs. pre-conflict level  
![](images/381378f85bf11eff8ee95be434d6cf5915a0aa70ebd32ede6bf13d2c11444ed2.jpg)

<details>
<summary>line chart</summary>

| Date       | West Africa - China | USG - China | ME - China | Average VLCC Earnings |
|------------|---------------------|-------------|----------|------------------------|
| 02-Jan     | ~30                 | ~40         | ~50      | ~60                    |
| 09-Jan     | ~50                 | ~60         | ~80      | ~100                   |
| 16-Jan     | ~70                 | ~80         | ~100     | ~120                   |
| 23-Jan     | ~90                 | ~100        | ~120     | ~130                   |
| 30-Jan     | ~110                | ~120        | ~140     | ~140                   |
| 06-Feb     | ~130                | ~140        | ~160     | ~150                   |
| 13-Feb     | ~150                | ~160        | ~180     | ~170                   |
| 20-Feb     | ~170                | ~180        | ~200     | ~190                   |
| 27-Feb     | ~200                | ~220        | ~250     | ~240                   |
| 06-Mar     | ~250                | ~280        | ~450     | ~380                   |
| 13-Mar     | ~150                | ~180        | ~400     | ~250                   |
| 20-Mar     | ~120                | ~140        | ~350     | ~220                   |
| 27-Mar     | ~130                | ~150        | ~330     | ~210                   |
| 03-Apr     | ~140                | ~160        | ~350     | ~220                   |
| 10-Apr     | ~130                | ~150        | ~450     | ~230                   |
| 17-Apr     | ~120                | ~140        | ~480     | ~220                   |
| 24-Apr     | ~110                | ~130        | ~470     | ~210                   |
| 01-May     | ~100                | ~120        | ~450     | ~200                   |
| 08-May     | ~110                | ~130        | ~460     | ~210                   |
| 15-May     | ~120                | ~140        | ~450     | ~220                   |
| 22-May     | ~130                | ~150        | ~440     | ~230                   |
| 29-May     | ~140                | ~160        | ~430     | ~240                   |
| 05-Jun     | ~150                | ~170        | ~420     | ~250                   |
| 12-Jun     | ~160                | ~180        | ~410     | ~260                   |
</details>

Source: Clarksons, data as of 12 June

Figure 2: VLCC 1 year charter rate remained stable  
![](images/a04a38caebd4a3c82af7de9c56460dbba484e0678da07001cf1655f1113a4a96.jpg)

<details>
<summary>line chart</summary>

| Date   | 1-year timecharter rate | 2-year timecharter rate | 3-year timecharter rate | 5-year timecharter rate |
|--------|--------------------------|--------------------------|--------------------------|--------------------------|
| May-26 | 129                      | 80                       | 70                       | 60                       |
</details>

Source: Clarksons, data as of 12 June

Figure 3: Average earnings of Capesize dropped by 18% WoW last week  
![](images/84993e74b459608340e323f909363acabd4a4fb6bd244b5edb3fcf4d9965cd51.jpg)

<details>
<summary>line chart</summary>

| Date   | Average Capesize Earnings | Panamax Average Earnings | Baltic Exchange Dry Index (RHS) |
|--------|---------------------------|---------------------------|--------------------------------|
| Jan-23 | 10                        | 5                         | 1000                           |
| Mar-23 | 15                        | 10                        | 1500                           |
| May-23 | 20                        | 15                        | 2000                           |
| Jul-23 | 15                        | 10                        | 1500                           |
| Sep-23 | 25                        | 15                        | 2500                           |
| Nov-23 | 45                        | 20                        | 4000                           |
| Jan-24 | 30                        | 15                        | 3000                           |
| Mar-24 | 40                        | 20                        | 3500                           |
| May-24 | 30                        | 15                        | 3000                           |
| Jul-24 | 35                        | 15                        | 3500                           |
| Sep-24 | 30                        | 10                        | 3000                           |
| Nov-24 | 35                        | 10                        | 3500                           |
| Jan-25 | 10                        | 5                         | 1000                           |
| Mar-25 | 25                        | 10                        | 2000                           |
| May-25 | 30                        | 15                        | 2500                           |
| Jul-25 | 35                        | 15                        | 3000                           |
| Sep-25 | 30                        | 15                        | 3500                           |
| Nov-25 | 35                        | 15                        | 4000                           |
| Jan-26 | 25                        | 10                        | 3500                           |
| Mar-26 | 30                        | 15                        | 4000                           |
| May-26 | 45                        | 20                        | 4500                           |
</details>

Source: Clarksons, data as of 12 June

Figure 4: Crude tanker passage at Hormuz remained 95% below pre-conflict level  
![](images/9103ca128f99099f06f220559178c472638b9a9e1177204660f24c43100dab49.jpg)

<details>
<summary>line chart</summary>

| Date    | Bab el-Mandeb | Hormuz |
|---------|---------------|--------|
| Jan-04  | 5             | 33     |
| Jan-11  | 4             | 34     |
| Jan-18  | 6             | 35     |
| Jan-25  | 4             | 37     |
| Feb-01  | 6             | 37     |
| Feb-08  | 5             | 34     |
| Feb-15  | 6             | 37     |
| Feb-22  | 8             | 40     |
| Mar-01  | 5             | 34     |
| Mar-08  | 6             | 0      |
| Mar-15  | 15            | 0      |
| Mar-22  | 14            | 0      |
| Mar-29  | 13            | 0      |
| Apr-05  | 12            | 0      |
| Apr-12  | 11            | 2      |
| Apr-19  | 10            | 0      |
| Apr-26  | 11            | 0      |
| May-03  | 12            | 0      |
| May-10  | 11            | 0      |
| May-17  | 8             | 0      |
| May-24  | 10            | 2      |
| May-31  | 12            | 0      |
| Jun-07  | 12            | 2      |
</details>

Source: UBS Evidence Lab (> Access Dataset)

Figure 5: Container throughput at China's key ports -4% WoW, 5% YoY last week  
![](images/19fa98bf236f033768997c2ae86a559b59fd5f00603d0291327864f4ea9ea4cd.jpg)

<details>
<summary>line chart</summary>

| Month   | 2022 | 2023 | 2024 | 2025 | 2026 |
|---------|------|------|------|------|------|
| 3-Jan   |      |      |      |      |      |
| 3-Feb   |      |      |      |      |      |
| 3-Mar   |      |      |      |      |      |
| 3-Apr   |      |      |      |      |      |
| 3-May   |      |      |      |      |      |
| 3-Jun   |      |      |      |      |      |
| 3-Jul   |      |      |      |      |      |
| 3-Aug   |      |      |      |      |      |
| 3-Sep   |      |      |      |      |      |
| 3-Oct   |      |      |      |      |      |
| 3-Nov   |      |      |      |      |      |
| 3-Dec   |      |      |      |      |      |
Week 23: -4% WoW, +5%YoY
Week 24: -1% WoW, +5%YoY
</details>

Source: Ministry of Transport

Figure 6: Container volume new in transit from Asia to US has been showing a front loading pattern  
![](images/58f5668ae1da232feacddcc8d295ef7e49252cf9de53b2e260405f8233f070da.jpg)

<details>
<summary>line chart</summary>

| Month | 2025 | 2026 |
| --- | --- | --- |
| Jan-04 | 380 | 300 |
| Feb-01 | 440 | 350 |
| Mar-01 | 230 | 240 |
| Apr-01 | 340 | 360 |
| May-01 | 320 | 300 |
| Jun-01 | 350 | 320 |
| Jul-01 | 310 | 340 |
| Aug-01 | 330 | 350 |
| Sep-01 | 360 | 380 |
| Oct-01 | 210 | 290 |
| Nov-01 | 350 | 360 |
| Dec-01 | 290 | 310 |
| Jan-02 | 310 | 320 |
| Feb-02 | 330 | 340 |
| Mar-02 | 350 | 360 |
| Apr-02 | 370 | 380 |
| May-02 | 390 | 400 |
| Jun-02 | 410 | 420 |
| Jul-02 | 430 | 440 |
| Aug-02 | 450 | 460 |
| Sep-02 | 470 | 480 |
| Oct-02 | 490 | 500 |
| Nov-02 | 510 | 520 |
| Dec-02 | 530 | 540 |
| Jan-03 | 550 | 560 |
| Feb-03 | 570 | 580 |
| Mar-03 | 590 | 600 |
| Apr-03 | 610 | 620 |
| May-03 | 630 | 640 |
| Jun-03 | 650 | 660 |
| Jul-03 | 670 | 680 |
| Aug-03 | 690 | 700 |
| Sep-03 | 710 | 720 |
| Oct-03 | 730 | 740 |
| Nov-03 | 750 | 760 |
| Dec-03 | 770 | 780 |
| Jan-04 | 790 | 800 |
| Feb-04 | 810 | 820 |
| Mar-04 | 830 | 840 |
| Apr-04 | 850 | 860 |
| May-04 | 870 | 880 |
| Jun-04 | 890 | 900 |
| Jul-04 | 910 | 920 |
| Aug-04 | 930 | 940 |
| Sep-04 | 950 | 960 |
| Oct-04 | 970 | 980 |
| Nov-04 | 990 | 1000 |
| Dec-04 | 1010 |  |
| Jan-05 |  |  |
| Feb-05 |  |  |
| Mar-05 |  |  |
| Apr-05 |  |  |
| May-05 |  |  |
| Jun-05 |  |  |
| Jul-05 |  |  |
| Aug-05 |  |  |
| Sep-05 |  |  |
| Oct-05 |  |  |
| Nov-05 |  |  |
| Dec-05 |  |  |
| Jan-06 |  |  |
| Feb-06 |  |  |
| Mar-06 |  |  |
| Apr-06 |  |  |
| May-06 |  |  |
| Jun-06 |  |  |
| Jul-06 |  |  |
| Aug-06 |  |  |
| Sep-06 |  |  |
| Oct-06 |  |  |
| Nov-06 |  |  |
| Dec-06 |  |  |
| Jan-07 |  |  |
| Feb-07 |  |  |
| Mar-07 |  |  |
| Apr-07 |  |  |
| May-07 |  |  |
| Jun-07 |  |  |
| Jul-07 |  |  |
| Aug-07 |  |  |
| Sep-07 |  |  |
| Oct-07 |  |  |
| Nov-07 |  |  |
| Dec-07 |  |  |
| Jan-08 |  |  |
| Feb-08 |  |  |
| Mar-08 |  |  |
| Apr-08 |  |  |
| May-08 |  |  |
| Jun-08 |  |  |
| Jul-08 |  |  |
| Aug-08 |  |  |
| Sep-08 |  |  |
| Oct-08 |  |  |
| Nov-08 |  |  |
| Dec-08 |  |  |
| Jan-09 |  |  |
| Feb-09 |  |  |
| Mar-09 |  |  |
| Apr-09 |  |  |
| May-09 |  |  |
| Jun-09 |  |  |
| Jul-09 |  |  |
| Aug-09 |  |  |
| Sep-09 |  |  |
| Oct-09 |  |  |
| Nov-09 |  |  |
| Dec-09 |  |  |
| Jan-10 |  |  |
| Feb-10 |  |  |
| Mar-10 |  |  |
| Apr-10 |  |  |
| May-10 |  |  |
| Jun-10 |  |  |
| Jul-10 |  |  |
| Aug-10 |  |  |
| Sep-10 |  |  |
| Oct-10 |  |  |
| Nov-10 |  |  |
| Dec-10 |  |  |
| Jan-11 |  |  |
| Feb-11 |  |  |
| Mar-11 |  |  |
| Apr-11 |  |  |
| May-11 |  |  |
| Jun-11 |  |  |
| Jul-11 |  |  |
| Aug-11 |  |  |
| Sep-11 |  |  |
| Oct-11 |  |  |
| Nov-11 |  |  |
| Dec-11 |  |  |
| Jan-12 |  |  |
| Feb-12 |  |  |
| Mar-12 |  |  |
| Apr-12 |  |  |
| May-12 |  |  |
| Jun-12 |  |  |
| Jul-12 |  |  |
| Aug-12 |  |  |
| Sep-12 |  |  |
| Oct-12 |  |  |
| Nov-12 |  |  |
| Dec-12 |  |  |
</details>

Source: UBS Evidence Lab (> Access Dataset)

Figure 7: SCFI +9% WoW and +43% YoY

<table><tr><td>WoW/YoY</td><td>SCFI</td><td>CCFI</td><td>SCFI Europe</td><td>SCFI W/C US</td><td>SCFI E/C US</td><td>NCFI Thailand&amp;Vietnam</td></tr><tr><td>2026-05-08</td><td>2%/45%</td><td>1%/16%</td><td>5%/37%</td><td>4%/20%</td><td>3%/14%</td><td>2%/18%</td></tr><tr><td>2026-05-15</td><td>10%/45%</td><td>0%/16%</td><td>14%/57%</td><td>10%/1%</td><td>11%/4%</td><td>6%/29%</td></tr><tr><td>2026-05-22</td><td>4%/40%</td><td>3%/19%</td><td>5%/45%</td><td>1%/-4%</td><td>2%/1%</td><td>1%/15%</td></tr><tr><td>2026-05-29</td><td>16%/24%</td><td>4%/22%</td><td>30%/56%</td><td>31%/-20%</td><td>24%/-15%</td><td>-1%/10%</td></tr><tr><td>2026-06-05</td><td>6%/22%</td><td>3%/22%</td><td>5%/56%</td><td>10%/-19%</td><td>8%/-17%</td><td>-5%/10%</td></tr><tr><td>2026-06-12</td><td>9%/43%</td><td>5%/19%</td><td>18%/66%</td><td>12%/25%</td><td>10%/-6%</td><td>-5%/11%</td></tr></table>

Source: Shanghai Shipping Exchange, Clarksons, data as of 12 June 2026

Figure 9: Container ships re-routing away from Red Sea still at high levels (+4-5% YoY)  
![](images/c5969ab77eaf0a613d76cb0e75194fff37e109a3c43d0df72e83eee6776e4ca9.jpg)

<details>
<summary>line chart</summary>

| Date   | m TEU | YoY (RHS) |
|--------|-------|-----------|
| Feb-25 | 11.0  | 30%       |
| Mar-25 | 9.5   | 10%       |
| Apr-25 | 9.8   | 12%       |
| May-25 | 10.0  | 14%       |
| Jun-25 | 10.2  | 16%       |
| Jul-25 | 10.1  | 15%       |
| Aug-25 | 10.3  | 17%       |
| Sep-25 | 10.4  | 18%       |
| Oct-25 | 10.2  | 16%       |
| Nov-25 | 10.5  | 19%       |
| Dec-25 | 10.3  | 20%       |
| Jan-26 | 10.4  | 21%       |
| Feb-26 | 10.6  | 22%       |
| Mar-26 | 10.8  | 23%       |
| Apr-26 | 10.9  | 24%       |
| May-26 | 10.7  | 23%       |
| Jun-26 | 9.8   | 5%        |
</details>

Source: Clarksons; Note: data as of 12 June 2026

Figure 11: Strong VLCC demand drives up YTD strong global shipbuilding demand  
![](images/60cc8fb32d391eca0a48b7c9a2dacaa0b6e2bc6a165c6c2cf7ca7d526d1e7052.jpg)

<details>
<summary>bar chart</summary>

| Month    | Value (m dwt) |
| -------- | ------------- |
| Jan-21   | 8             |
| Feb-21   | 18            |
| Mar-21   | 24            |
| Apr-21   | 13            |
| May-21   | 15            |
| Jun-21   | 10            |
| Jul-21   | 9             |
| Aug-21   | 12            |
| Sep-21   | 7             |
| Oct-21   | 5             |
| Nov-21   | 13            |
| Dec-21   | 6             |
| Jan-22   | 11            |
| Feb-22   | 10            |
| Mar-22   | 11            |
| Apr-22   | 7             |
| May-22   | 9             |
| Jun-22   | 8             |
| Jul-22   | 9             |
| Aug-22   | 8             |
| Sep-22   | 9             |
| Oct-22   | 8             |
| Nov-22   | 9             |
| Dec-22   | 8             |
| Jan-23   | 10            |
| Feb-23   | 11            |
| Mar-23   | 10            |
| Apr-23   | 13            |
| May-23   | 14            |
| Jun-23   | 13            |
| Jul-23   | 9             |
| Aug-23   | 10            |
| Sep-23   | 10            |
| Oct-23   | 8             |
| Nov-23   | 9             |
| Dec-23   | 10            |
| Jan-24   | 15            |
| Feb-24   | 16            |
| Mar-24   | 14            |
| Apr-24   | 18            |
| May-24   | 9             |
| Jun-24   | 38            |
| Jul-24   | 10            |
| Aug-24   | 19            |
| Sep-24   | 15            |
| Oct-24   | 13            |
| Nov-24   | 14            |
| Dec-24   | 10            |
| Jan-25   | 9             |
| Feb-25   | 8             |
| Mar-25   | 10            |
| Apr-25   | 5             |
| May-25   | 13            |
| Jun-25   | 16            |
| Jul-25   | 10            |
| Aug-25   | 10            |
| Sep-25   | 16            |
| Oct-25   | 13            |
| Nov-25   | 24            |
| Dec-25   | 33            |
| Jan-26   | 20            |
| Feb-26   | 28            |
| Mar-26   | 20            |
| Apr-26   | 11            |
</details>

Source: Clarksons

Figure 8: Container freight futures on Far East-Northern Europe fall back after US-Iran peace deal  
![](images/d9a207f1f5c0a242327ca8e80b2bae059f94f8aec86223418e4cf2c4bab8ffa3.jpg)

<details>
<summary>line chart</summary>

| Date   | ec2604 | ec2606 | ec2608 | ec2610 | ec2612 | ec2703 |
|--------|--------|--------|--------|--------|--------|--------|
| May-25 | 1000   | 1000   | 1000   | 1000   | 1000   | 1000   |
| Jun-25 | 1050   | 1100   | 1150   | 1050   | 1100   | 1150   |
| Jul-25 | 1100   | 1200   | 1300   | 1150   | 1250   | 1350   |
| Aug-25 | 1150   | 1300   | 1400   | 1250   | 1350   | 1450   |
| Sep-25 | 1200   | 1400   | 1500   | 1350   | 1450   | 1550   |
| Oct-25 | 1250   | 1500   | 1600   | 1450   | 1550   | 1650   |
| Nov-25 | 1300   | 1600   | 1700   | 1550   | 1650   | 1750   |
| Dec-25 | 1350   | 1700   | 1800   | 1650   | 1750   | 1850   |
| Jan-26 | 1400   | 1800   | 1900   | 1750   | 1850   | 1950   |
| Feb-26 | 1450   | 1900   | 2000   | 1850   | 1950   | 2050   |
| Mar-26 | 1500   | 2000   | 2100   | 1950   | 2050   | 2150   |
| Apr-26 | 1550   | 2100   | 2200   | 2050   | 2150   | 2250   |
| May-26 | 1600   | 2200   | 2300   | 2150   | 2250   | 2350   |
| Jun-26 | 1650   | 2300   | 2400   | 2250   | 2350   | 2450   |
</details>

Source: Shanghai Futures Exchange

Figure 10: Intra-Asia chartering index recovered WoW last week  
![](images/fcc1608c460daf66dc4443a88e69023c1b24f533d0d51807782b21c013529f1a.jpg)

<details>
<summary>line chart</summary>

| Week | 2025  | 2026  |
|------|-------|-------|
| 2    | 2100  | 2350  |
| 4    | 2150  | 2370  |
| 6    | 2200  | 2380  |
| 8    | 2180  | 2360  |
| 10   | 2250  | 2250  |
|

[中间内容因长度限制已省略]

d Kingdom, UBS AG is authorised by the Prudential Regulation Authority and is subject to regulation by the Financial Conduct Authority and limited regulation by the Prudential Regulation Authority. Details about the extent of regulation by the Prudential Regulation Authority are available from us on request. A member of the London Stock Exchange. This publication is distributed to retail clients of UBS Wealth Management. Ukraine: UBS is a premier global financial services firm offering wealth management services to individual, corporate and institutional investors. UBS is established in Switzerland and operates under Swiss law and in over 50 countries and from all major financial centers. UBS is not registered and licensed as a bank/financial institution under Ukrainian legislation and does not provide banking and other financial services in Ukraine. UBS has not made, and will not make, any offer of the mentioned products to the public in Ukraine. No action has been taken to authorize an offer of the mentioned products to the public in Ukraine and the distribution of this document shall not constitute financial services for the purposes of the Law of Ukraine "On Financial Services and Financial Companies" dated 14 December 2021. Any offer of the mentioned products shall not constitute an investment advice, public offer, circulation, transfer, safekeeping, holding or custody of securities in the territory of Ukraine. Accordingly, nothing in this document or any other document, information or communication related to the mentioned products shall be interpreted as containing an offer, a public offer or invitation to offer or to a public offer, or solicitation of securities in the territory of Ukraine or investment advice under Ukrainian law. Electronic communication must not be considered as an offer to enter into an electronic agreement or other electronic instrument within the meaning of the Law of Ukraine "On Electronic Commerce" dated 3 September 2015. This document is strictly for private use by its holder and may not be passed on to third parties or otherwise publicly distributed. USA: Distributed to US persons only by UBS Financial Services Inc. or UBS LLC, subsidiaries of UBS AG. UBS Switzerland AG, UBS Europe SE, UBS Bank, S.A., UBS BB Corretora de Câmbio, Títulos e Valores Mobiliários S.A., UBS Asesores México, S.A. de C.V., UBS SuMi TRUST Wealth Management Co., Ltd., UBS Wealth Management Israel Ltd. and UBS Menkul Degerler AS are affiliates of UBS AG. UBS Financial Services Inc. accepts responsibility for the content of a report prepared by a non-US affiliate when it distributes reports to US persons. All transactions by a US person in the securities mentioned in this report should be effected through a US-registered broker dealer affiliated with UBS, and not through a non-US affiliate. The contents of this report have not been and will not be approved by any securities or investment authority in the United States or elsewhere. UBS Financial Services Inc. is not acting as a municipal advisor to any municipal entity or obligated person within the meaning of Section 15B of the Securities Exchange Act (the "Municipal Advisor Rule") and the opinions or views contained herein are not intended to be, and do not constitute, advice within the meaning of the Municipal Advisor Rule. For information on the ways in which UBS LLC manages conflicts and maintains independence of its UBS Global Research product; historical performance information; certain additional disclosures concerning UBS Global Research recommendations; and terms and conditions for certain third party data used in research report, please visit https://www.ubs.com/disclosures

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

## CS Wealth Management Disclaimer

This disclaimer must be read in conjunction with "Risk information" and "Important Information About Sustainable Investing Strategies" sections of the Global Wealth Management Disclaimer above. You receive this document in your capacity as a client of CS Wealth Management. Your personal data will be processed in accordance with the CS privacy statement accessible at your domicile through the official CS website https://www.credit-suisse.com. In order to provide you with marketing materials concerning our products and services, UBS Group AG and its subsidiaries may process your basic personal data (i.e. contact details such as name, e-mail address) until you notify us that you no longer wish to receive them. You can optout from receiving these materials at any time by informing your Relationship Manager.

Except as otherwise specified herein and/or depending on the local CS entity from which you are receiving this report, this report is distributed by UBS Switzerland AG, authorised and regulated by the Swiss Financial Market Supervisory Authority (FINMA). Saudi Arabia: This document is being distributed by CS Saudi Arabia I Part of UBS Group (CR Number 1010228645, NUN Number 7001515373), duly licensed and regulated by the Saudi Arabian Capital Market Authority pursuant to License Number 08104-37 dated 23/03/1429H corresponding to 21/03/2008AD. CS Saudi Arabia's principal place of business is at King Khaled Road, Laysen Valley, Building number 6, 12329-2376, Riyadh, Saudi Arabia. Website: https://www.credit-suisse.com/sa/en/cssa.html.

© UBS 2026. The key symbol and UBS are among the registered and unregistered trademarks of UBS. All rights reserved.

![](images/df5252019e4cbd9f8094849ecd702c520a6ecefd13ad0c2993bf33cc18ec8a6e.jpg)
"""
