You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Keep the article concise and end after the last substantive point.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Source specificity: ground every interpretation in a concrete number, named mechanism, comparison, or causal relationship from the report.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should translate the report into a decision framework for readers.
- Never create a section about unresolved questions, what the report failed to answer, research gaps, limitations, further reading, or community access. If the source explicitly states a limitation, mention it once inside the relevant analytical paragraph.
- End with the final substantive paragraph. Do not add a CTA, promotional invitation, website, community reference, summary, or rhetorical question.
- End with: `*For informational purposes only. Portions may be generated, translated, summarized, or edited with AI assistance based on source materials and may contain omissions or errors. Please verify independently. This is not investment, legal, tax, accounting, or other professional advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Open with the most specific fact, contrast, or tension in the source. Avoid generic openings such as "Against this backdrop", "In recent years", or "As the market evolves".
- Vary sentence and paragraph length naturally. Do not repeat stock transitions such as "This means", "In other words", or "What matters most".
- Do not invent a personal voice, interview, or first-hand experience. Editorial character must come from evidence selection and precise phrasing.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
GLOBAL ECONOMICS ANALYST

# Geopolitics and GDP: Structural Alignment Matters More than Near-Term Risk

■ Geopolitical risks from the war in Iran have faded since March. But broader risks around geopolitical and economic fragmentation remain, with some measures signaling the lowest level of global alignment since the 1980s. In this Global Economics Analyst, we explore the impact of geopolitics on the global economy, with a particular focus on the longer-run implications for global growth.

The effects of geopolitics on commodity prices and economic outcomes are well-studied, although only a subset of geopolitical crises—typically those directly involving major oil-producing regions—have a material impact on oil prices. Outside of the commodity channel, we find that the direct impacts of geopolitical risk events have created only modest drags on growth due to increased caution from consumers and businesses. For example, a sustained increase in geopolitical risk indices as large as the spike due to the war in Iran would only subtract 0.3pp from global GDP growth in 2026-H1 (incremental to commodity headwinds) according to our estimates.

The long-run impacts from shifting geopolitical alliances are not small, however. A one standard deviation shift in country-specific geopolitical alignment toward improved relations with the rest of the world (defined by the GDP-weighted alignment to all other countries)—a shift roughly as large as during the defrosting of Chinese-western relations following Nixon's visit in 1972—adds $3\%$ to long-run GDP on the back of increased trade and investment, particularly if driven by increased alignment with western nations. We also find larger benefits in EMs than DMs, with stratified estimates suggesting that increased trade, lower resource dependence, and positive spillovers to domestic governance and institutions help EMs catch up.

One reason why shifts in geopolitical alignment lead to long-run GDP effects that build for almost a decade is that they prompt increases in trade that lead to longer-run efficiencies. We find that overall trade volumes increase following an increase in bilateral alignment, a pattern that suggests more efficient allocations of production. We also find increases in FDI and FX reserve allocations following a positive shift in alignment, suggesting that increased capital flow enhances efficiency.

\- Our results suggest that a hypothetical return to mid-2010s levels of geopolitical alignment could add up to 1% to global GDP over the remainder of the decade, with outsized benefits in EMs. In contrast, an incremental increase in

Johan Allen
+44(20)7774-7122 |
johan.allen@gs.com
GS International

Joseph Briggs
+1(212)902-2163 |
joseph.briggs@gs.com
GS & Co. LLC

fragmentation equivalent to that seen since 2016 would lower global GDP by 1% over the long run.

## Geopolitics and GDP: Structural Alignment Matters More than Near-Term Risk

Near-term geopolitical risks appear to be receding. Despite some signs of fragility, the US-Iran memorandum of understanding lays the groundwork for a gradual normalization of global economic conditions as oil flows through the Strait of Hormuz recover. But risks around broader geopolitical and economic fragmentation remain, with some measures signaling the lowest level of global alignment since the 1980s.

In this Global Economics Analyst, we explore the impact of geopolitics on the global economy, with a particular focus on the longer-run implications for global growth.

## Measuring Geopolitical Risk and Alignment

Recent academic research has focused on quantifying two distinct types of geopolitical exposures.

1. Geopolitical risk event measures capture the quantity and intensity of events such as military confrontations, political crises and diplomatic incidents. We use a recently-introduced Geopolitical Risk Index from Iacoviello and Tong (2026) $^{1}$ which analyses historical geopolitical events on a country level by applying an LLM to historical newspaper articles.

2. Geopolitical alignment measures instead quantify the relationships between nations—how aligned a country is to other states. We measure alignment using a Geopolitical Alignment Index constructed from the Global Geopolitical Events Database (GGED) developed by Fan (2025) $^{2}$ . GGED uses a web-search enabled LLM model to identify historical events between country pairs and assign scores reflecting relative alignment or misalignment. Following Fan (2025), we construct country-level alignment scores by taking GDP-weighted averages of the bilateral alignment measures.

Methodologically, the geopolitical risk event index and geopolitical alignment index are somewhat similar. Both combine media and other text to extract a signal of shifting geopolitical stances. Exhibit 1 shows the evolution of the global geopolitical risk index (intensity-weighted share of newspaper coverage devoted to global geopolitical risk) and geopolitical alignment index (GDP-weighted average of country-specific indices) since 1960. There are common trends—for example, geopolitical risks declined in the mid-1970s, around the same time that geopolitical alignment increased against the backdrop of US-Soviet détente. Most relevant for the current outlook, both measures have risen sharply since the 2010s—consistent with more geopolitical risk events and higher fragmentation—and stand close to all-time highs. Although fragmentation eased slightly since 2021, the latest alignment datapoint is 2024—before the 2025 ‘Liberation Day’ tariffs and the Iran war—and therefore fails to capture a likely incremental deterioration in alignment over the last two years.

Exhibit 1: Global Geopolitical Fragmentation Has Increased Over the Last 5-10 Years  
![](images/7d237a66cfb837b765d2b23fc7e9ed887c3c92824b58269bf4d49a2d5c2e544c.jpg)  
Source: GS Global Investment Research, Iacoviello and Tong (2026), Fan (2025)

While geopolitical risk and alignment are correlated, it is worth emphasizing that geopolitical risk is a distinct phenomenon from geopolitical alignment. This is most apparent on a national level: to illustrate, Exhibit 2 shows the two country-level indices for the UK and Vietnam (the geopolitical risk index corresponds to the intensity-weighted share of newspaper coverage devoted to UK/Vietnamese geopolitical risk; the geopolitical alignment index is defined as the GDP-weighted average of bilateral alignment between the UK/Vietnam and all other countries). In the case of the UK, Brexit led to a deterioration in overall alignment without a corresponding rise in event risk. And in the case of Vietnam, the end of the Vietnam war led event risk to decline 20 years before alignment improved.

Exhibit 2: Geopolitical Risk and Geopolitical Alignment Are Distinct Phenomena  
![](images/1635da3516349298cbab248b549bb947bc0023f6fcf15bb5068b6501c54e197c.jpg)  
Source: GS Global Investment Research, Iacoviello and Tong (2026), Fan (2025)

![](images/8ac7e127b1330c1a84b0f379f0af504298f50da174e58096ed9c87de03b5baf0.jpg)

A key differentiating factor between geopolitical risk events and changes in geopolitical alignment is their relative persistence: Individual geopolitical risk events tend to be highly salient when they occur but are most often shorter-lived. Geopolitical alignment, by contrast, is a slower yet persistent process.

To quantify this distinction, we run a local projection of the country-level geopolitical risk and alignment indices on themselves. Exhibit 3 shows that a one-unit ‘shock’ in the risk index exhibits some persistence but falls sharply within two years and subsides after five. A one-unit geopolitical alignment shock endures far longer, fully receding only after roughly 14 years. Wars, acts of terror and threats of interstate violence are deeply disruptive—but are fortunately usually measured in days, months or at most years—whereas the strengthening and deterioration of relations between nations is a gradual process that unfolds over decades.

Exhibit 3: Geopolitical Risk Shocks Fade Quickly, but Changes in Geopolitical Alignment Are Much More Persistent  
![](images/fe5c91b0d9ed9f80a5f3d3c20926b5725ad000e7a1c3d73b281b173b025d6372.jpg)  
Source: GS Global Investment Research, Iacoviello and Tong (2026), Fan (2025)

## The Short and Sharp Impact of Geopolitical Risk Events

Many well-known geopolitical crises—the 1979 Iranian revolution, Russia’s 2022 invasion of Ukraine and the ongoing Iran war—hit the global economy primarily through one channel: commodity market disruptions that pushed up commodity prices. We have previously highlighted our rule-of-thumb that a 10% rise in oil prices lowers global GDP by approximately 0.1%, implying that the Hormuz closure has erased roughly 0.3% from global GDP this year. Yet most geopolitical risk events—for instance, the Falklands war, the 1999 NATO bombing of Yugoslavia and the 2025 announcement of US tariffs—have nothing to do with oil. A simple scatter plot of the Geopolitical Risk Index against the one-month change in global oil prices shows no relationship (Exhibit 4) $^{3}$ .

Exhibit 4: We Often Focus on Commodity Price Impacts of Geopolitical Shocks, but the Response of Oil Prices to Geopolitical Events is Surprisingly Weak

![](images/1491fa53b1816336a39af551d64f5c37fa007394c9e5a83acc81c6b1a117dfbf.jpg)

To estimate the direct short-run effects of geopolitical events on global GDP—due to precautionary saving, delayed investment and risk-off capital outflows, but excluding oil—we run a panel local projection of country-level geopolitical risk indices on quarterly GDP growth, controlling for oil prices. A one standard deviation rise in the index—an increase roughly as large as the one that occurred in China following the announcement of tariffs in early 2025—tends to lower country-level GDP growth by 0.2pp in the affected quarter and by a further 0.1pp the following quarter, before the effect subsides (Exhibit 5).

The drag is materially larger in Emerging Markets than in Developed Markets, likely because EMs are more vulnerable to risk-off capital outflows. The key takeaway from these patterns is that growth drags are generally small and only temporary. The global geopolitical risk index was 30% higher in 2025-H1 compared to 2024-H2, implying that global growth in Q1-Q2 was approximately 0.3pp lower than in a counterfactual without the Iran war, with some recovery likely in H2 on the back of the recent normalization in risks.

Exhibit 5: Geopolitical Risk Events Have a Short-Run Impact on Real GDP Growth (Incremental to Commodity Price Effects)...  
![](images/e28c38aa3aee58722898d288a109efd964f55ed1b461dfa1a3a213efe48aeb4a.jpg)  
Source: GS Global Investment Research, Iacoviello and Tong (2026)

## The Larger Long-Term Consequences of Geopolitical Alignment

Geopolitical alignment shapes economic activity over a far longer horizon. To demonstrate, we run a set of local projections that exploit country-level changes in the GDP-weighted average of bilateral geopolitical alignment indices on annual GDP, while also controlling for country and time fixed effects (we include separate time fixed effects for DMs and split EMs by the seven World Bank regions). The resulting estimates therefore capture the effect of a one standard deviation shift in a specific country's alignment with the rest of the world, holding alignment for all other countries fixed. Causal identification is admittedly difficult—economic progress could lead to an improvement in alignment, while not all alignment shifts will necessarily generate significant economic benefits—but idiosyncratic time variation in alignment likely provides useful insight into the impact on GDP.

We find that a one standard-deviation $^{4}$ increase in country-level geopolitical alignment raises the level of GDP by approximately 3% over seven years for the average country in our panel. This effect is large but generally follows from material shifts in alignment—an alignment shock of this magnitude would roughly correspond to the shock that occurred to China after Nixon visited in 1972 or the shift in Iran's alignment after it signed the JCPOA in 2015 $^{5}$ .

While the estimated impact on GDP is large, it aligns with a growing body of economic literature that finds large effects of alignment on economic activity. As examples, 1) Fan (2025) finds that a one-standard deviation permanent shift in alignment raises GDP per capita by 10% over 25 years, 2) Fan Wo and Xiang (2026) find that a similar shift in

alignment boosts bilateral trade by 20% over 10 years, 3) Shan and Tilton (2024) find that the US does not trade much with or invest in countries that are geopolitically distant, though China has close trade and investment relationships with both geopolitically close countries and many countries that are geopolitically more distant. 4) Gopinath Gourinchas Presbitero and Topalova (2024) find that trade and FDI flows across misaligned blocs have declined by 12% and 20% more than flows within the same bloc since the start of the war in Ukraine, 5) Javorick Kitzmuller Schweiger and Yildirim (2024) find that reversing recent alignment trends and economic integration could subtract 4.7% from GDP. Additional research highlights the importance of geoeconomic power and pressure in explaining long-run economic dynamics, suggesting that such forces are increasingly recognized as an important driver of long-run activity.

Exhibit 6: ...Whereas Geopolitical Alignment Effects Have a Long-Run Impact on GDP  
![](images/c98df0040de5b32cd458c283fe1b4fd8e77c852a8ea8d1de209019f92f5d885d.jpg)  
Source: GS Global Investment Research, Fan (2025)

What drives this increase in GDP? Rerunning our model to estimate the impact of country-level changes in the GDP-weighted average of bilateral geopolitical alignment indices (i.e., alignment with the rest of the world) on the subcomponents of GDP reveals three channels. First, fixed investment rises the most, as improved relations widen access to global capital markets and lower the risk of domestic investment for local and international investors alike (Exhibit 7). Although investment may also rise in response to a deterioration of bilateral relations—through channels such as higher domestic defense expenditure, the nearshoring of supply chains and higher domestic energy infrastructure construction—our results suggest that larger longer-run investment gains accrue from an improvement, rather than a decline, in geopolitical alignment. Second, exports rise as improved alignment lowers trade barriers and deepens bilateral commerce. This effect is more pronounced for smaller economies—re-estimating our model only on the largest economies shows a smaller (though still significant) contribution from exports. Third, household and government consumption also rise, though by less than overall GDP, likely as a second-order effect of stronger investment and trade.

Exhibit 7: The Positive GDP Impacts from Increased Geopolitical Alignment Comes Mostly From Increases in Investment and Trade  
![](images/2ee05719519f3adf613c5857fa607c8d2e2da5eedf4593a83346119d6737a294.jpg)  
Source: GS Global Investment Research, Fan (2025)

Given the importance of the investment and trade channels, it is unsurprising that emerging markets see materially larger gains from improved geopolitical alignment compared to developed markets (Exhibit 8). Stratifying our results suggests two further reasons. First, closer alignment helps EMs move away from a resource-extraction model and its associated volatility. Second, effects are larger for countries with weaker domestic institutions and governance, suggesting closer alignment with other countries generates positive spillovers beyond direct economic channels.

Exhibit 8: Less-Developed Countries With Weaker Institutions Have Tended to See A Larger Impact from Improving Geopolitical Alignment  
![](images/628b4407dc9cdb4123fba03f42ab306894447e9e40a84d12bb2b45fd17d4b830.jpg)  
Source: GS Global Investment Research, Fan (2025), World Bank

Which bilateral relationships have historically delivered the largest economic benefits? We regress each country's bilateral alignment score with a given partner on that country's GDP—the US-Argentina score on Argentine GDP, the US-Brazil score on Brazilian GDP, and so on—while again controlling for country and region-time fixed effects. The takeaway from this exercise is that better relations with Western countries imply higher GDP gains than improving relations with China or Russia (Exhibit 9).

Somewhat surprisingly, our estimates suggest that the UK—rather than the US—screens as the most valuable partner to improve bilateral relations with. We see two likely drivers of this result. First, given the close historical alignment between the UK and US, increased bilateral alignment with the UK also leads to an endogenous increase in bilateral alignment with the US, such that the UK index serves as a US alignment proxy as well. Second, the UK also maintains close economic and political ties to mainland Europe, and therefore likely similarly captures simultaneous improvement in European alignment as well. Put simply, the UK’s close economic and political ties to both the US and mainland Europe likely lead it to serve as the most effective proxy for other country’s overall alignment with the Western bloc.

Exhibit 9: Historically, Better Relations With Western Countries Have Led to Larger GDP Gains  
![](images/ece8a67a3898287ad9ab003461d107f10065ac02c7ed47b30110786f6d3c34f3.jpg)  
\*Prior to 1991: Soviet Union  
Source: GS Global Investment Research, Fan (2025)

## Increased Alignment Improves Efficiency

The large and persistent impact of country-level alignment with the rest of the world on GDP likely reflects more than its direct effects on GDP components. By influencing trade and capital flows, alignment may also foster efficiency gains that accrue over time, amplifying its long-run effects on economic activity. We highlight three patterns supporting this view.

First, just as an improvement in a nation's aggregate geopolitical alignment improves its aggregate exports, an improvement in the bilateral relationship between two nations persistently increases bilateral trade (Exhibit 10).

Effect of 1sd Geopolitical Alignment Shock on FDI Assets and Liabilities

Exhibit 10: A 1sd Improvement in Bilateral Geopolitical Alignment Persistently Raises Bilateral Trade Volumes by 6%  
![](images/f53940bbe952641a0945d60535e2723ecac80bd1d810860edc1bb81fb5ef7d4f.jpg)  
Source: G

[中间内容因长度限制已省略]

 have long or short positions in, act as principal in, and buy or sell, the securities or derivatives, if any, referred to in this research, unless otherwise prohibited by regulation or GS policy.

The views attributed to third party presenters at GS arranged conferences, including individuals from other parts of GS, do not necessarily reflect those of Global Investment Research and are not an official view of GS.

Any third party referenced herein, including any salespeople, traders and other professionals or members of their household, may have positions in the products mentioned that are inconsistent with the views expressed by analysts named in this report.

This research is focused on investment themes across markets, industries and sectors. It does not attempt to distinguish between the prospects or performance of, or provide analysis of, individual companies within any industry or sector we describe.

Any trading recommendation in this research relating to an equity or credit security or securities within an industry or sector is reflective of the investment theme being discussed and is not a recommendation of any such security in isolation.

This research is not an offer to sell or the solicitation of an offer to buy any security in any jurisdiction where such an offer or solicitation would be illegal. It does not constitute a personal recommendation or take into account the particular investment objectives, financial situations, or needs of individual clients. Clients should consider whether any advice or recommendation in this research is suitable for their particular circumstances and, if appropriate, seek professional advice, including tax advice. The price and value of investments referred to in this research and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

Certain transactions, including those involving futures, options, and other derivatives, give rise to substantial risk and are not suitable for all investors. Investors should review current options and futures disclosure documents which are available from GS sales representatives or at https://www.theocc.com/about/publications/character-risks.jsp and https://www.goldmansachs.com/disclosures/cftc\_fcm\_disclosures. Transaction costs may be significant in option strategies calling for multiple purchase and sales of options such as spreads. Supporting documentation will be supplied upon request.

Differing Levels of Service provided by Global Investment Research: The level and types of services provided to you by GS Global Investment Research may vary as compared to that provided to internal and other external clients of GS, depending on various factors including your individual preferences as to the frequency and manner of receiving communication, your risk profile and investment focus and perspective (e.g., marketwide, sector specific, long term, short term), the size and scope of your overall client relationship with GS, and legal and regulatory constraints.

As an example, certain clients may request to receive notifications when research on specific securities is published, and certain clients may request that specific data underlying analysts' fundamental analysis available on our internal client websites be delivered to them electronically through data feeds or otherwise. No change to an analyst's fundamental research views (e.g., ratings, price targets, or material changes to earnings estimates for equity securities), will be communicated to any client prior to inclusion of such information in a research report broadly disseminated through electronic publication to our internal client websites or through other means, as necessary, to all clients who are entitled to receive such reports.

All research reports are disseminated and available to all clients simultaneously through electronic publication to our internal client websites. Not all research content is redistributed to our clients or available to third-party aggregators, nor is GS responsible for the redistribution of our research by third party aggregators. For research, models or other data related to one or more securities, markets or asset classes (including related services) that may be available to you, please contact your GS representative or go to https://research.gs.com.

Disclosure information is also available at https://www.gs.com/research/hedge.html or from Research Compliance, 200 West Street, New York, NY 10282.

## © 2026 GS.

You are permitted to store, display, analyze, modify, reformat, and print the information made available to you via this service only for your own use. You may not resell or reverse engineer this information to calculate or develop any index for disclosure and/or marketing or create any other derivative works or commercial product(s), data or offering(s) without the express written consent of GS. You are not permitted to publish, transmit, or otherwise reproduce this information, in whole or in part, in any format to any third party without the express written consent of GS. This foregoing restriction includes, without limitation, using, extracting, downloading or retrieving this information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system.
"""
