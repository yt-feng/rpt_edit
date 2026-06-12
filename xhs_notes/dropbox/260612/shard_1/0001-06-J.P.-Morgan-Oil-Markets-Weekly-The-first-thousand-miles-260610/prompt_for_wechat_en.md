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
## Oil Markets Weekly

The first thousand miles

The largest supply disruption on record has produced a surprisingly unremarkable price chart. Since the start of the conflict, Brent has averaged just \$101, closely tracking the price path implied by our framework in early March.

At the time, we concluded that only two forces could plausibly explain such a restrained outcome. Either demand losses, alongside inventory drawdowns, could prove large enough to rebalance the market outright. Or the adjustment could move down the barrel, away from crude and into refined products (Down the barrel, 8 May 2026). Under that scenario, crude prices could hover near \$100/bbl while scarcity shows up instead in gasoline, diesel, and jet fuel prices. The shock would be expressed not through materially higher flat crude prices, but through widening product cracks and sharply higher refined product prices. In March, we viewed the latter as the more likely adjustment mechanism.

The first part of that framework proved correct. The second did not. Crude prices followed the expected path. Product markets did not. After an initial spike, gasoline, diesel, and jet fuel prices have reset lower, while refining margins have narrowed rather than widened (Figure 1).

Figure 1: US petroleum product price change from February 27 to June 8  
![](images/08659c5410c21080396740868b70630d4441b27aac0f7702665f666fee82ab89.jpg)

<details>
<summary>line chart</summary>

| Date     | Jet  | Gasoline | Diesel | Naphtha |
|----------|------|----------|--------|---------|
| 27-Feb   | 0%   | 0%       | 0%     | 0%      |
| 6-Mar    | 65%  | 30%      | 40%    | 45%     |
| 13-Mar   | 68%  | 45%      | 50%    | 60%     |
| 20-Mar   | 95%  | 55%      | 70%    | 75%     |
| 27-Mar   | 75%  | 60%      | 70%    | 80%     |
| 3-Apr    | 85%  | 65%      | 75%    | 78%     |
| 10-Apr   | 60%  | 50%      | 55%    | 65%     |
| 17-Apr   | 85%  | 45%      | 40%    | 70%     |
| 24-Apr   | 90%  | 60%      | 55%    | 85%     |
| 1-May    | 100% | 70%      | 60%    | 110%    |
| 8-May    | 80%  | 65%      | 55%    | 90%     |
| 15-May   | 80%  | 75%      | 60%    | 105%    |
| 22-May   | 50%  | 60%      | 50%    | 85%     |
| 29-May   | 40%  | 50%      | 45%    | 70%     |
| 5-Jun    | 45%  | 45%      | 40%    | 60%     |
</details>

Source: Bloomberg Finance L.P., JPM Commodities Research

## Global Commodities Research

## Natasha Kaneva

(1-212) 834-3175

natasha.kaneva@JPM.com

## Lyuba Savinova

(1-212) 270-3781

lyuba.savinova@jpmchase.com

## Artem Fakhretdinov

(1-212) 272-1839

artem.fakhretdinov@JPM.com

JPM Chase Bank NA

The most plausible explanation is that the market has absorbed much of the disruption through a combination of demand losses and large-scale inventory releases. Demand has weakened in the conflict zone itself. In parts of Asia, reduced physical oil availability has curtailed consumption directly. In China, consumers have substituted away from oil more readily than many expected. In Africa, higher prices have triggered more traditional forms of demand destruction. At the same time, governments and commercial operators have drawn heavily on both crude and refined product inventories. Together, these adjustments have reduced the burden on prices to do the balancing.

For US consumers, however, this does not mean that fuel markets have fully normalized. Our forecast still calls for Brent to average around \$100 through most of the remainder of 2026. On that view, we estimate that the US retail gasoline prices will remain near \$4 per gallon for much of the year (Figure 2). While far below the levels implied by a full-blown product shortage in more extreme scenarios, they remain elevated enough to keep energy firmly in focus for households and policymakers alike.

Figure 2: JPM US retail gasoline price forecast under alternative Strait of Hormuz reopening scenarios \$ per gallon  
![](images/fac48c7b539a9091f1c5c612eee2aa353da24d32939f737a34688062c608470d.jpg)

<details>
<summary>line chart</summary>

| Month    | Actual | Baseline | July | August |
| -------- | ------ | -------- | ---- | ------ |
| Jan-26   | 2.8    | -        | -    | -      |
| Feb-26   | 2.9    | -        | -    | -      |
| Mar-26   | 3.7    | -        | -    | -      |
| Apr-26   | 4.1    | -        | -    | -      |
| May-26   | 4.5    | 4.5      | 4.5  | 4.5    |
| Jun-26   | -      | 4.3      | 4.4  | 4.4    |
| Jul-26   | -      | 4.4      | 4.6  | 4.7    |
| Aug-26   | -      | 4.4      | 4.7  | 5.0    |
| Sep-26   | -      | 4.4      | 4.8  | 5.2    |
| Oct-26   | -      | 4.2      | 4.6  | 5.1    |
| Nov-26   | -      | 4.0      | 4.5  | 5.1    |
| Dec-26   | -      | 3.8      | 4.4  | 5.0    |
</details>

Source: JPM Commodities Research

Importantly, national averages can obscure significant regional differences. Nowhere is this more evident than on the US West Coast, where fuel markets remain the tightest in the country. California is particularly exposed. A combination of unique state regulations—including high taxes and environmental mandates—and the closure of Valero’s Benicia refinery and Phillips 66’s Los Angeles refinery, which together account for 17% of California’s refining capacity, is expected to tighten fuel balances further in a market that already operates with limited flexibility.

Unlike most of the country, California cannot easily draw on supplies from neighboring states. Instead, the state relies heavily on CARB (California Air Resources Board)-compliant gasoline from Asian refiners, which account for nearly two-thirds of gasoline imports into California and roughly $20\%$ to $30\%$ of the state's total gasoline supply. Since March 1, however, many Asian refiners have been forced to reduce refined product exports as disruptions to crude flows from Hormuz have constrained feedstock availability.

The challenge is compounded by California's unique fuel specifications and the lack of major product pipelines linking the state to the rest of the country. More broadly, California's vulnerability reflects a longer-term shift. Once a major producer and exporter of oil and refined products, the state has become increasingly import-dependent as local production has steadily declined.

This structural tightness is evident at the pump. Even as crude oil prices have dipped below \$100 per barrel, pump prices have steadily declined. Today, the national average for a gallon of regular gasoline sits at roughly \$4.16, down more than 10% from a late-May peak near \$4.56. Prices nevertheless exceed \$5.0 in six states, with drivers in California paying an average of \$5.89 a gallon (Figure 3).

Diesel shows the same pattern. Nationwide, average diesel prices have eased to about \$5.32 per gallon. Yet, truckers filling up in California are still paying an average of \$7.16 at the pump.

This matters far beyond the region itself. Roughly one in five of all goods entering the United States arrives through West Coast gateways such as the Ports of Los Angeles and Long Beach. And before those imports ever reach warehouses, distribution centers, and consumers across the country, they often travel their first several hundred—or even thousand—miles powered by West Coast diesel and gasoline. In practice, this means that a meaningful share of America’s supply chain pays West Coast fuel prices. These prices influence freight costs, transportation margins, and ultimately the delivered cost of goods nationwide.

Figure 3: Average retail gasoline price by state  
\$/gallon  
![](images/d2ebdc857bc5d7809721842922bb81e0ef7824c9bd84af677da77cfaec9c9d1d.jpg)

<details>
<summary>choropleth map</summary>

| State       | Value  |
| ----------- | ------ |
| California  | $5.5   |
| Texas       | $5.0   |
| Florida     | $4.5   |
| New York    | $4.0   |
| Pennsylvania| $4.5   |
| Illinois    | $4.5   |
| Ohio        | $4.5   |
| Michigan    | $4.5   |
| Georgia     | $4.5   |
| North Carolina | $4.5  |
| Virginia    | $4.5   |
| Washington  | $4.5   |
| Arizona     | $4.5   |
| Massachusetts | $4.5  |
| Tennessee   | $4.5   |
| Indiana     | $4.5   |
| Maryland    | $4.5   |
| Missouri    | $4.5   |
| Colorado    | $4.5   |
| Minnesota   | $4.5   |
| Wisconsin   | $4.5   |
| Michigan    | $4.5   |
| Indiana     | $4.5   |
| Iowa        | $4.5   |
| Kansas      | $4.5   |
| Nebraska    | $4.5   |
| South Dakota | $4.5  |
| North Dakota| $4.5   |
| Montana     | $4.5   |
| Wyoming     | $4.5   |
| Utah        | $4.5   |
| Idaho       | $4.5   |
| Nevada      | $4.5   |
| New Hampshire | $4.5  |
| Rhode Island | $4.5  |
| Maine       | $4.5   |
| Vermont     | $4.5   |
| New Hampshire | $4.5  |
| Delaware    | $4.5   |
| Maryland    | $4.5   |
| Alaska      | $4.5   |
| Hawaii      | $4.5   |
| Maine       | $4.5   |
| Vermont     | $4.5   |
| New Hampshire | $4.5  |
| Rhode Island | $4.5  |
| Delaware    | $4.5   |
| Maine       | $4.5   |
| Vermont     | $4.5   |
| New Hampshire | $4.5  |
| Rhode Island | $4.5  |
| Delaware    | $4.5   |
| Maine       | $4.5   |
| Vermont     | $4.5   |
| New Hampshire | $4.5  |
| Rhode Island | $4.5  |
| Delaware     | $4.5   |
| Maine       | $4.5   |
| Vermont     | $4.5   |
| New Hampshire | $4.5  |
| Rhode Island | $4.5  |
| Delaware    | $4.5   |
| Maine       | $4.5   |
| Vermont     | $4.5   |
| New Hampshire | $4.5  |
| Rhode Island | $4.5  |
| Delaware```  | $4.0   |
</details>

Note: as of June 8 $^{th}$  
Source: AAA, JPM Commodity Research

Understanding where fuel prices go from here requires looking beyond crude oil to the underlying product markets.

US gasoline prices surged in May as the domestic balance tightened on both the supply and demand fronts. Inventories fell while refiners increasingly prioritized jet fuel, constraining gasoline output. At the same time, demand rebounded from the February-April lull, supported by strong Memorial Day travel and resilient consumer activity.

Higher gasoline prices have since begun to elicit a partial response: some refinery production has shifted back from jet fuel toward gasoline, and incremental imports from Canada and Northwest Europe have started to arrive, offering relief to the East Coast market. That said, this rebalancing may be short-lived. European gasoline markets remain tight, and as summer demand builds, incentives to keep barrels in-region are likely to strengthen. If so, US gasoline imports could slow later this summer, leaving domestic inventories at relatively low seasonal levels, though still comfortable overall in terms of days of demand (Figures 4 & 5).

Figure 4: US commercial inventories of gasoline and diesel  
![](images/93c2527f39ecb352d142bf1e3cb08de6e714c5ffee8fc114c9a15ceb203f789a.jpg)

<details>
<summary>line chart</summary>

| Year | Gasoline (Thousand barrels) | Diesel (Thousand barrels) |
|------|-----------------------------|---------------------------|
| 2000 | ~215,000                    | ~95,000                   |
| 2001 | ~218,000                    | ~115,000                  |
| 2002 | ~220,000                    | ~135,000                  |
| 2003 | ~215,000                    | ~95,000                   |
| 2004 | ~218,000                    | ~135,000                  |
| 2005 | ~220,000                    | ~115,000                  |
| 2006 | ~225,000                    | ~135,000                  |
| 2007 | ~230,000                    | ~145,000                  |
| 2008 | ~235,000                    | ~115,000                  |
| 2009 | ~185,000                    | ~135,000                  |
| 2010 | ~235,000                    | ~175,000                  |
| 2011 | ~245,000                    | ~175,000                  |
| 2012 | ~235,000                    | ~155,000                  |
| 2013 | ~235,000                    | ~135,000                  |
| 2014 | ~235,000                    | ~135,000                  |
| 2015 | ~245,000                    | ~145,000                  |
| 2016 | ~255,000                    | ~165,000                  |
| 2017 | ~265,000                    | ~175,000                  |
| 2018 | ~255,000                    | ~145,000                  |
| 2019 | ~265,000                    | ~135,000                  |
| 2020 | ~275,000                    | ~175,000                  |
| 2021 | ~265,000                    | ~145,000                  |
| 2022 | ~255,000                    | ~135,000                  |
| 2023 | ~245,000                    | ~135,000                  |
| 2024 | ~255,000                    | ~135,000                  |
| 2025 | ~245,000                    | ~135,000                  |
| 2026 | ~265,000                    | ~135,000                  |
</details>

Source: EIA, JPM Commodities Research

Figure 5: US commercial inventories of gasoline and diesel in days of demand coverage  
![](images/5bf6377cf8baa422561f2cd4500128d4ff84fe93496eadcb15bf39354885f4d2.jpg)

<details>
<summary>line chart</summary>

| Year | Gasoline Days | Diesel Days |
|------|---------------|-------------|
| 2003 | 24            | 38          |
| 2009 | 20            | 40          |
| 2020 | 32            | 47          |
| 2026 | 28            | 34          |
</details>

Source: EIA, JPM Commodities Research

Diesel, by contrast, is being pulled by both domestic needs and a widening global shortfall, with the US Gulf Coast increasingly acting as the marginal supplier. Diesel exports averaged 1.2 mbd in January and February, nearly 150 kbd higher than the same period last year, despite the closure of three US refineries since the start of 2025. Much of the increase appears tied to stronger demand from Brazil, where Russian diesel shipments have declined, and from Europe, where restrictions on products refined from Russian crude came into effect in January.

The closure of Hormuz has only amplified these dynamics. Since the start of the conflict, US diesel exports have risen further to 1.5 mbd, accelerating inventory draws and pushing stocks to a 23 year low, even as refinery utilization remains strong (Figures 4 & 5).

If gasoline illustrates regional tightness and diesel highlights global scarcity, jet fuel sits somewhere in between. US jet fuel inventories have remained relatively resilient despite strong domestic consumption and rising export demand as record refinery yields keep pace with demand, leaving inventories well supplied. Seasonal demand has continued to strengthen with the onset of summer travel and the approach of the World Cup, even as several airlines have already reduced flight schedules through the third quarter (Figure 6).

Figure 6: US commercial inventories of jet in days of demand coverage  
Days (LHS); Commercial inventory (RHS) in thousands of barrels  
![](images/ede68de3f9a19d98de2ef22f6a441ad6e2d23537ef67d4000617f8d2419c8d4b.jpg)

<details>
<summary>line chart</summary>

| Year | Days (LHS) | Inventory (RHS) |
|------|------------|-----------------|
| 2023 | 21 days    | 15,000          |
</details>

Source: EIA, JPM Commodities Research

Table 1: JPM crude oil price forecasts (US\$/bbl)

<table><tr><td colspan="2"></td><td>2023</td><td>2024</td><td>1Q25</td><td>2Q25</td><td>3Q25</td><td>4Q25</td><td>2025</td><td>1Q26</td><td>2Q26</td><td>3Q26</td><td>4Q26</td><td>2026</td><td>1Q27</td><td>2Q27</td><td>3Q27</td><td>4Q27</td><td>2027</td></tr><tr><td rowspan="2">Brent</td><td>Avg</td><td>81</td><td>80</td><td>75</td><td>67</td><td>68</td><td>63</td><td>68</td><td>78</td><td>103</td><td>104</td><td>98</td><td>96</td><td>85</td><td>79</td><td>69</td><td>65</td><td>75</td></tr><tr><td>EoP</td><td>86</td><td>76</td><td>75</td><td>68</td><td>67</td><td>61</td><td>61</td><td>118</td><td>101</td><td>107</td><td>95</td><td>95</td><td>82</td><td>73</td><td>69</td><td>64</td><td>64</td></tr><tr><td rowspan="2">WTI</td><td>Avg</td><td>76</td><td>76</td><td>71</td><td>64</td><td>65</td><td>59</td><td>65</td><td>73</td><td>96</td><td>97</td><td>93</td><td>89</td><td>80</td><td>75</td><td>65</td><td>61</td><td>70</td></tr><tr><td>EoP</td><td>81</td><td>72</td><td>71</td><td>65</td><td>62</td><td>57</td><td>57</td><td>101</td><td>94</td><td>100</td><td>89</td><td>89</td><td>77</td><td>69</td><td>65</td><td>60</td><td>60</td></tr><tr><td>WTI - Brent Spread</td><td>Avg</td><td>-5</td><td>-4</td><td>4</td><td>3</td><td>3</td><td>4</td><td>4</td><td>6</td><td>8</td><td>7</td><td>6</td><td>6</td><td>5</td><td>4</td><td>4</td><td>4</td><td>4</td></tr><tr><td rowspan="2">Brent Forward Curve</td><td>Avg</td><td>82</td><td>80</td><td>75</td><td>67</td><td>68</td><td>63</td><td>68</td><td>78</td><td>104</td><td>94</td><td>87</td><td>91</td><td>83</td><td>80</td><td>79</td><td>78</td><td>80</td></tr><tr><td>EoP</td><td>77</td><td>73</td><td>75</td><td>68</td><td>67</td><td>61</td><td>61</td><td>118</td><td>102</td><td>91</td><td>85</td><td>85</td><td>82</td><td>80</td><td>79</td><td>78</td><td>78</td></tr><tr><td rowspan="2">WTI Forward Curve</td><td>Avg</td><td>78</td><td>76</td><td>71</td><td>64</td><td>65</td><td>59</td><td>65</td><td>73</td><td>96</td><td>87</td><td>80</td><td>84</td><td>77</td><td>75</td><td>74</td><td>73</td><td>74</td></tr><tr><td>EoP</td><td>72</td><td>71</td><td>71</td><td>65</td><td>62</td><td>57</td><td>57</td><td>101</td><td>94</td><td>84</td><td>79</td><td>79</td><td>76</td><td>74</td><td>73</td><td>72</td><td>72</td></tr></table>

Source: JPM Commodities Research, ICE, NYMEX, Bloomberg Finance L.P. Actuals till 2Q25. Forward curve for Brent from 3Q25 and WTI from 3Q25 onwards. Price forecasts last updated on April 14, 2025

Table 2: Global oil supply and demand balance, 2025

<table><tr><td rowspan="2">mbd</td><td colspan="12">2025F</td><td colspan="4">2025F</td><td>2025F</td></tr><tr><td>Jan</td><td>Feb</td><td>Mar</td><td>Apr</td><td>May</td><td>Jun</td><td>Jul</td><td>Aug</td><td>Sep</td><td>Oct</td><td>Nov</td><td>Dec</td><td>1Q</td><td>2Q</td><td>3Q</td><td>4Q</td><td></td></tr><tr><td>Total Oil Demand</td><td>103.4</td><td>104.6</td><td>103.4</td><td>104.5</td><td>104.2</td><td>106.5</td><td>107.6</td><td>106.6</td><td>107.0</td><td>106.2</td><td>105.6</td><td>106.5</td><td>103.8</td><td>105.0</td><td>107.0</td><td>106.1</td><td>105.5</td></tr><tr><td>Total Oil Supply</td><td>103.6</td><td>104.7</td><td>105.8</td><td>105.5</td><td>105.6</td><td>107.1</td><td>108.0</td><td>108.0</td><td>109.7</td><td>109.0</td><td>109.1</td><td>108.1</td><td>104.7</td><td>106.1</td><td>108.6</td><td>108.7</td><td>107.0</td></tr><tr><td>OPEC Crude</td><td>29.1</td><td>29.7</td><td>30.0</td><td>29.7</td><td>29.7</td><td>30.2</td><td>30.5</td><td>29.9

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 09 Jun 2026 11:28 PM EDT

Disseminated 10 Jun 2026 07:00 AM EDT
"""
