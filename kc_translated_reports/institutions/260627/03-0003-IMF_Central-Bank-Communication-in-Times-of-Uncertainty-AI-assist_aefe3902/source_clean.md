# Central Bank Communication in Times of Uncertainty: AI- assisted Decoding of Recent Trends in Europe

Francesca Caselli, Luisa Charry, Larry Cui, Pragyan Deb, Allan Gloe Dizioli, Alexandra Fotiou, Ben Park and Sebastian Weber

WP/26/133

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.

2026
JUN


[[KC_IMAGE_001]]


# IMF Working Paper European Department

# Central Bank Communication in Times of Uncertainty: AI-assisted Decoding of Recent Trends in Europe\*

Authorized for distribution by Helge Berger
June 2026

IMF Working Papers describe research in progress by the author(s) and are published to elicit comments and to encourage debate. The views expressed in IMF Working Papers are those of the author(s) and do not necessarily represent the views of the IMF, its Executive Board, or IMF management.


RECOMMENDED CITATION: Caselli, Francesca, Luisa Charry, Larry Cui, Pragyan Deb, Allan Gloe Dizioli, Alexandra Fotiou, Ben Park, and Sebastian Weber, “Central Bank Communication in Times of Uncertainty: AI-assisted Decoding of Recent Trends in Europe,” IMF Working Paper WP/26/133.


# Central Bank Communication in Times of Uncertainty: AI-assisted Decoding of Recent Trends in Europe

Prepared by Francesca Caselli, Luisa Charry, Larry Cui, Pragyan Deb, Allan Gloe Dizioli, Alexandra Fotiou, Ben Park and Sebastian Weber

## ContentsPage

I. Introduction 4
II. A survey of central bank communication practices in Europe 7
III. Indices of central bank communication 9
IV. Stylized facts on central bank communication 10
A. Stylized fact I: AE central banks make greater use of forward-looking language 10
B. Stylized fact II: Central banks commonly use forward-looking and backward-looking communication at the same time 12
C. Stylized fact III: Inertia in central banks communication 13
V. How do central banks react to uncertainty 13
A. Net forward-looking language as an anchoring device 19
VI. How do central banks communicate uncertainty 20
VII. Conclusion 27
References 28
Appendices
A. Appendix 31
A.1. Data 31
A.2. Robustness with static equation 31
A.3. Robustness with equation in 12-months difference 32
A.4. Robustness controlling for the zero lower bound 35
A.5. Robustness to different dictionary: the ECB index 36
List of Tables
1. Dynamic model - lag net forward-looking index 15
2. Dynamic model - lag net forward-looking index with more uncertainty measures 18
3. Correlates of forward-/backward-looking communication - decomposing the net forward-looking index 19
4. Anchoring of market interest rate expectations 21
5. Description of variables used among different specifications 31
6. Static model - Net forward-looking index with more uncertainty measures 32
7. Explaining the change in net forward-looking index all sample 33
8. Explaining the change in net forward-looking index advanced 34
9. Explaining the change in net forward-looking index developing 34
10. Dynamic model - lag net forward-looking index with more uncertainty measures 36

## List of Figures

1. Financial market and economic policy uncertainty 4
2. Central banks' use of key communication tools 8
3. Content of central banks' monetary policy communication 8
4. Distribution of the net forward-looking index across country groups 11
5. Net forward-looking index evolution over time for selected countries 11
6. Correlations between backward- and forward-looking communication indices 12
7. Inertia in the forward-looking communication index 13
8. AE central banks' communication responses to inflation uncertainty over time 16
9. Monetary policy uncertainty and net forward-looking communication 20
10. Central bank uncertainty aligns with large shock events 22
11. Cross-country correlation of the CBUI and policy rates 22
12. Rolling correlation of CBUI 23
13. What drives central banks to talk about uncertainty 24
14. CBUI Highly Correlated with Policy Rate Pricing Uncertainty During Certain Periods 25
15. ECB's backward-looking communication index: Robustness to dictionary 37

## I. INTRODUCTION

Successive large shocks—including pandemics, armed conflicts, geopolitical fragmentation, and trade tensions—have pushed uncertainty to historically high levels (Figure 1). Many policy makers expect the environment of elevated uncertainty to become the new normal (e.g., Bailey 2025, Georgieva 2025, and Lagarde 2025), posing new challenges to central banks. They point out that elevated uncertainty complicates forecasting, weakens signals of traditional policy tools, and risks reducing the effectiveness of conventional monetary policy. In this context, central bank communication has assumed greater importance as a policy instrument in its own right to help anchor and guide expectations. Gauging the effectiveness of central bank communication and improving its design are therefore central to maintaining effective monetary policy in times of enduring uncertainty.

Figure 1. Financial market and economic policy uncertainty

[[KC_IMAGE_002]]

Note: The figure shows the European VSTOXX index (left axis), capturing financial market uncertainty, and the Global Economic Policy Uncertainty (EPU) index (right axis).

European central banks have increasingly relied on communication tools to support monetary policy since the 1990s, particularly after the Global Financial Crisis (GFC). The move toward central bank independence, the establishment of the European Central Bank (ECB), and the expansion of monetary policy tools to include quantitative measures reinforced the need for transparent, systematic, and clear communication to help establish credibility and anchor expectations (Blinder, Ehrmann, Fratzscher, De Haan, and Jansen 2008; Blinder, Ehrmann, de Haan, and Jansen 2024; Armelius, Bertsch, Hull, and Zhang 2018). The GFC accelerated this process, as unconventional policies—such as large-scale asset purchases, and negative interest rates—required more frequent and clearer explanations to signal central banks' intentions and maintain policy credibility. This shift extended across many European central banks, which gradually increased the frequency, transparency, and scope of their communications to shape market and public expectations. Today, they face additional challenges, including persistent inflation pressures and heightened uncertainty from the Russian war in Ukraine, the war in the Middle East, and evolving geopolitical and trade tensions, making effective communication even more critical.

Given persistently elevated uncertainty, this paper examines how central banks in Europe communicate and adjust messaging in response to different sources of uncertainty. We address four key questions: First, how have these central banks communicated when responding to heightened uncertainty: more cautious and “data-dependent” by using backward-looking language for flexibility, or more assertive and forward-looking to anchor agents’ expectations? Second, do central banks react differently depending on the source of uncertainty—whether it is directly influenced by monetary policy (e.g., inflation uncertainty) or largely outside of their control (e.g., financial or stock market-implied uncertainty)? Third, do emerging market (EM) central banks react differently from their advanced economy (AE) counterparts? Fourth, how do central banks’ own assessment of uncertainty and monetary policy outlook compare with market participants’ perceptions?

To address these questions, we survey the landscape of communication practices of major European central banks and develop AI-based numerical indicators that track how central banks adjust communication styles over time. Focusing on monetary policy statements—comparable documents released by central banks following policy decisions and available over sufficiently long time series—we measure the shifts in the balance between forward- and backward-looking language as the magnitude and sources of uncertainty evolve. A key distinction in this paper concerns different forms of forward-looking communication. While the literature often associated forward-looking communication with commitment-based forward guidance (i.e., explicit signals about the future path of policy instruments), our focus is broader. We capture forward-looking language as information-based communication about the economic outlook, risks, and likely policy reactions, which may or may not involve explicit commitments.

This paper contributes to three strands of the literature on monetary policy and central bank communication. First, it examines how central bank communication mitigates information frictions and anchors inflation expectations, particularly under heightened uncertainty. Theory provides rich guidance on how monetary policy should react to different uncertainty: gradual adjustments under uncertain monetary policy transmission (Brainard, 1967) but aggressive if faced with inflation uncertainty (Dupraz, Guilloux-Nefussi, and Penalver, 2023; Soederstroem, 2002; Gust, Herbst, and López-Salido, 2025). But theory offers limited insight on optimal central bank communication under heightened uncertainty. Markets and households often lack knowledge of the central bank reaction function, weakening transmission (Blinder and others 2008, Blinder and others 2024, Bernanke 2025). Empirical evidence shows that greater transparency increases the extent to which private agents rely on public central bank information, thereby improving expectations formation, especially during volatile periods (Crowe and Meade (2008); Altavilla, Gürkaynak, Kind, and Laeven 2025). Clear but state-contingent communication of credible monetary policy rules can reduce uncertainty about policy intentions and limits discretionary errors (Orphanides 2019, Orphanides 2025), though micro evidence highlights that transmission effects also depend on agents' ability to internalize signals (Albrizio, Dizioli, Simon, and Zhang (2025)). Historical surveys document that formal monetary policy statements became routine as central banks shifted from secrecy toward transparency, later expanding to more elaborate monetary policy reports and meeting minutes (Blinder and others 2008; Jeanneau (2009)).

In addition, recent research highlights that effective central bank communication hinges on balancing forward-looking and backward-looking messaging under specific circumstances. Under heightened uncertainty, structured risk disclosure, scenario-based analysis, and timely narrative framing help markets interpret policy intentions and reduce misaligned inflation expectations (Fadda, Hanifi, Istrefi, and Penalver 2025; Garga, Herbst, McKay, Nicolo, and Paustian 2025, BIS (2025)). Theory provides ambiguous guidance on the relative effectiveness of forward- and backward-looking communication, as optimal strategies depend on economic conditions, the heterogeneity of agents and shocks, and the severity of information frictions (Angeletos and Lian

2018 and Hagedorn, Luo, Manovskii, and Mitman 2019). Empirical evidence shows substantial cross-country differences driven by AE and EM contexts and varying uncertainty sources (Blinder and others (2024); BIS (2025)). An emerging theme concerns the complementary roles in communication: forward-looking communication conveys conditional policy paths and helps anchor expectations, while backward-looking communication explains past decisions, reinforces accountability, and supports institutional credibility (Blinder and others 2008, Blinder and others 2024, Bernanke 2025, and Christiano Silva, Moriya, and Veyrune (2025)). Consistent with this, Evdokimova, Mohácsi, Ponomarenko, and Ribakova (2023) find that EM central banks adapt more dynamically to real-time conditions, and Brandão-Marques and Nguyen 2024 show that forward-looking communication conditioned on scenarios strengthens credibility under uncertain inflation persistence.

Furthermore, this paper relates to a growing literature using artificial intelligence (AI) and natural language processing (NLP) to systematically quantify central bank communication and its impact. Text-as-data methods now enable large-scale analysis of speeches, statements, minutes, and reports across countries and over time, capturing features such as tone, thematic emphasis, and policy signals (Bholat, Hansen, Santos, and Schonhardt-Bailey 2015; Evdokimova and others 2023; Christiano Silva, Moriya, and Veyrune 2025). For example, Bholat and others 2015 provide an early framework for converting unstructured text into quantitative indicators relevant for policy analysis. Building on this, Evdokimova and others 2023 use NLP to compare the clarity and timeliness of communication across AE and EM central banks, showing that communications by several EM central banks have matched or exceeded those by the Fed and ECB in readability and inflation focus. Christiano Silva, Moriya, and Veyrune (2025) apply large language models to a broad cross-country dataset, showing that communication evolves with institutional frameworks such as inflation targeting, and that NLP can generate consistent measures to study communication effects across countries. They also construct forward- and backward-looking indexes using a broad set of communication documents including speeches. These studies demonstrate that AI-assisted text analysis provides a systematic, comparable, and policy-relevant tool for benchmarking central bank communication.

We show that, across a sample of twenty European central banks, formal communication toolkits are similar, particularly regarding publications such as monetary policy statements and online presence. Yet the degree of transparency and the intensity with which these tools are used differ significantly. AE central banks are more likely to publish meeting minutes, hold press conferences, and employ forward-looking tools such as scenarios, fan charts, and projected interest rate paths. These differences are also reflected in how central banks adjust their communication in response to uncertainty. Using a net indicator of forward- versus backward-looking communication across different sources of uncertainty, we find that, in a reduced sample of eleven central banks, both AE and EM central banks react mostly to inflation uncertainty, a source of uncertainty central banks can influence. However, while AE central banks shift toward a more forward-looking messaging as expected, EM central banks tend to shift in the opposite direction. Beyond constraints of available tools, this pattern may reflect credibility as a precondition for effective forward-looking communication (Cole, Martinez-Garcia, and Sims 2023). Rolling-window regressions point to an evolution in communication practices. In earlier periods, European AE central banks placed less emphasis on forward-looking communication in response to inflation uncertainty. During the low inflation (and low inflation uncertainty) environment following the euro area debt crisis, these central banks' forward-looking communication appears mostly driven by the low interest rate and the constraints of the effective lower bound. Only in recent years have they responded to rising inflation uncertainty by adopting more forward-looking messaging, accompanied by increased emphasis on the conditionality in messaging. More broadly, while the distinction between advanced and emerging economies provides a useful organizing framework, it may likely capture a range of underlying structural characteristics. Differences in institutional credibility, monetary policy frameworks, and exchange rate regimes may more directly account for cross-country variation in communication strategies. The AE/EM split should therefore be interpreted as a reduced-form proxy for these deeper characteristics.

The rest of paper is organized as follows: Section II provides an overview of central bank communication practices across a sample of twenty European central banks. Section III presents our methodology to build text-mining numerical indicators that summarize central bank communication, and Section IV provides some stylized facts of these indices for eleven European central banks. Section V and VI provide the empirical analyses using these indexes. Section VII concludes and provides some policy recommendations.

## II. A SURVEY OF CENTRAL BANK COMMUNICATION PRACTICES IN EUROPE

As a first step, we survey the existing European central bank communication toolkits and their use in practice. Having been disproportionately affected by a sequence of recent shocks, European central banks have increasingly converged on a similar set of communication tools, albeit with different usage intensity (Figure 2). Drawing on the taxonomy in International Monetary Fund (2020) and Casiraghi and Perez (2022), these tools include monetary policy statements (MPS), monetary policy reports (MPRs), minutes or transcripts of monetary policy meetings, press conferences, and other forms of media and public outreach. In AEs, $^{1}$ central banks make extensive use of this full communication toolkit, with nearly all employing each instrument. In EMs, $^{2}$ by contrast, communication practices are more selective. Most EM central banks publish MPRs and MPSs and maintain official websites and social media channels for monetary policy communication, but the publication of meeting minutes or transcripts is far less common. Moreover, around one-third of EM central banks do not regularly hold press conferences.

More pronounced differences arise in the content of central bank communications, particularly between AEs and EMs (Figure 3). On the one hand, there are important similarities: all AE central banks and more than 80 percent of EM central banks publish quantitative forecasts or projections for inflation or interest rates; over 60 percent in either groups provide explicit forward communication regarding the likely future path of monetary policy. On the other hand, AE central banks are substantially more likely to publish forward-looking scenarios accompanied by explicit policy assumptions, narratives, and simulated economic paths in their outlooks—practices adopted by fewer than 10 percent of EM central banks. These differences underscore why European central banks provide a particularly relevant setting for examining the role of communication in managing uncertainty.

Figure 2. Central banks' use of key communication tools

[[KC_IMAGE_003]]

Source: IMF staff calculations based on country desk survey

Figure 3. Content of central banks' monetary policy communication

[[KC_IMAGE_004]]

Source: IMF staff calculations based on country desk survey

Among the differences, scenario analysis has evolved into a core communication tool for many AE central banks, serving to provide conditional forward communication in periods of heightened uncertainty (Box 1). Bernanke (2025), European Central Bank (2025a), and Seim (2025) underscored that scenario analysis is crucial for central banks to communicate uncertainty and risks around economic forecasts in providing conditional forward communication. They argued that relying solely on a single central forecast can give a misleading sense of certainty about the future. Instead, scenario analysis allows policymakers and the public to see a range of plausible economic outcomes, including less likely but high impact scenarios, helping them un-

derstand how different shocks affect the economy and central banks' likely reactions. In addition, scenario analysis should strike a balance between comprehensiveness—covering sufficient alternative scenarios to illustrate potential economic paths and policy responses—and simplicity to ensure clear signals to markets and the public. While implementation varies across institutions, the trend is toward greater transparency, simplicity, flexibility, and realism in conveying uncertainty, risks, and the central bank reaction functions.

## III. INDICES OF CENTRAL BANK COMMUNICATION

As described in the previous section, central banks with similar monetary policy objectives communicate with different tools and styles. In this section we develop standardized and comparable numerical indicators of central bank communication by relying on a text-mining frequency approach. We construct three novel indices that capture the degree to which central bank MPSs are backward-looking, forward-looking, and the implied net forward-looking communication conveyed in communication. We focus on the MPS as the main document to enhance cross-country comparability. $^{3}$ MPSs are issued by central banks shortly after monetary policy decisions and explain those decisions to the public and market in a standardized format typically at a quarterly frequency. They assess current economic conditions and risks, discuss the outlook, and provide communication on the expected future policy stance, and are available for most major central banks over long time horizons. $^{4}$ The indices are developed for 11 central banks that have sufficient MPSs for comparison: the ECB and national central banks of the United Kingdom, Iceland, Israel, Sweden, the Czech Republic, Hungary, Poland, Serbia, Romania, and Türkiye.

Based on frequency counts, these indices are constructed through text-mining of MPSs and AI-assisted dictionaries with expert checking. We use a novel approach to choose the words that make up our dictionary and extract our indices. In particular, the choice of words is guided by the interaction of the Generative Pre-trained Transformers (GPT) model and expert judgments. $^{5}$ This approach involved two main steps: 1) we selected a sample of monetary policy statements and used the prompt “what are the key words in this statements that indicate forward (backward)-looking statements; 2) Using this set of keywords after expert judgment, we filtered and retained those deemed most relevant.

For the backward-looking index, the dictionary includes: “Assessment”, “Data-dependent”, “Historical”, “Indicator”, “Data dependent”, “Previous”, “Past”, “Current framework”, “experience”, “Cyclical drivers”, “Current data”, and “Current Inflation”. For the forward-looking index, the dictionary includes: “Outlook”, “Projected”, “Expectation”, “Guidance”, “Future path”, “Expect”, “Future”, “Projection”, “Guiding us forward”, “New frontier”, “Proactive”, “Emerging threat”, “Future”, “Anticipate”, “Prepared for change”, “Flexibility”, “Evolving framework”, “Stabilizing inflation”, “Timely return”, “Commitment to target”, “Expectation”, “Path”, “Commitment”, “Inflation expectation”, and “Forecast”.

The forward- and backward-looking indices are calculated as the number of sentences containing any of the words in our dictionaries divided by the total number of sentences in the MPSs:

$$
\text { Forward - / backward - looking   index } = 1 0 0 \times \frac {\text { N.   of   sentences   containing   dictionary   words }}{\text { Total   N.   of   sentences   in   the   monetary   policy   statement }}\tag{1}
$$

And the net forward-looking index is given by the difference between the forward- and the backward-looking index:

$$
\text { Net   forward - looking   index } = \text { Forward - looking   index } - \text { Backward - looking   index }\tag{2}
$$

Importantly, the forward-looking index captures predominantly information-based forward-looking communication (i.e., references to the outlook, projections, expectations, and possible policy paths), rather than explicit commitment-based forward guidance. As such, it should be interpreted as a measure of how central banks communicate about the future, not necessarily the extent to which they commit to a specific policy path. While the net forward-looking index provides a convenient summary measure of communication, it is important to note that forward- and backward-looking language are not mutually exclusive. In practice, central banks often rely on both types of communication simultaneously—particularly around policy decisions—when they explain past developments while also conveying expectations about the future. As a result, the net forward-looking index should be interpreted as capturing the relative emphasis between forward- and backward-looking communication, rather than their absolute levels. To ensure that important information is not obscured, we also examine the two indices separately in Section 5.

## IV. STYLIZED FACTS ON CENTRAL BANK COMMUNICATION

## A. Stylized fact I: AE central banks make greater use of forward-looking language

We start the analysis by investigating whether there are systematic differences in the net forward-looking index between advanced economies and emerging markets. Figure 4 plots the distribution of the index across the two country groups. AE central banks appear to make greater use of forward-looking language relative to backward-looking language than EM counterparts. This is also consistent with evidence that advanced economies presenting, on average, more anchored long-term inflation expectations, despite gains in inflation anchoring in EMs since the mid-2000s (Bems, Caselli, Grigoli, and Gruss 2021). To unpack country heterogeneity we plot the net forward-looking index series over time for four selected central banks, namely the ECB, the Bank of England (BoE), the Czech National Bank, and the Central Bank of the Republic of Türkiye. In the case of the ECB, the net forward-looking index rises during the COVID-19 crisis and subsequently declines during the ECB's hiking cycle, coinciding with the shift toward a more data-dependent policy framework. This shift aimed to place greater weight on incoming information in the reaction function at a time of heightened forecast uncertainty, thereby increasing the backward-looking component of central bank communication. A similar pattern is observed for the Czech National Bank, with the net forward-looking index exhibiting a clear downward trend in the period following COVID-19. Although the authorities did not formally adopt a data-dependent communication framework, they shifted toward a more backward-looking communication strategy emphasizing past economic developments and policy inertia during their policy hiking cycle. The Central Bank of the Republic of Türkiye also exhibits a similar decline in the net forward-looking index following the pandemic. The trends are similar in the case of the BoE, but with an notable increase in

the forward-looking focus since the 2024 Bernanke review as the BoE increasingly incorporated scenario analysis in its communications.

Figure 4. Distribution of the net forward-looking index across country groups

[[KC_IMAGE_005]]

Note: The figure plots the density of the net forward-looking communication indicator for the two separate country groups. AEs include the Czech Republic, the euro area, the United Kingdom, Iceland, Israel, and Sweden. EMs include Hungary, Poland, Romania, Serbia, and Türkiye.

Figure 5. Net forward-looking index evolution over time for selected countries

[[KC_IMAGE_006]]


[[KC_IMAGE_007]]


[[KC_IMAGE_008]]


[[KC_IMAGE_009]]

Note: The figure plots the net forward-looking index for the ECB, the Bank of England, the Czech National Bank, and the Central Bank of the Republic of Türkiye.

## B. Stylized fact II: Central banks commonly use forward-looking and backward-looking communication at the same time

Figure 6 shows that central banks tend to use both styles of communication together. This pattern is particularly pronounced among advanced economies in our sample, where the ECB and the Riksbank simultaneously employ more backward-looking and forward-looking communication, while reinforcing the use of the net forward-looking language. By contrast, emerging market central banks exhibit a clearer separation in communication styles, with the corresponding indices either uncorrelated (as in Hungary and Turkey) or negatively correlated (as in Serbia).

This co-movement suggests that forward- and backward-looking communication are not mutually exclusive, but often deployed jointly as part of a broader communication effort. In particular, around monetary policy decisions—especially turning points in the policy cycle—central banks appear to intensify communication along multiple dimensions by explaining past developments and policy actions while simultaneously providing guidance about the future. In this sense, periods of heightened communication intensity may mechanically raise both indices. This interpretation reinforces the importance of focusing on the relative balance between forward-and backward-looking language, rather than their levels in isolation. At the same time, it highlights that periods of heightened communication intensity may raise both indices simultaneously, implying that the net measure abstracts from these common movements. We therefore complement the analysis using the separate forward- and backward-looking indices in Section 5.

Figure 6. Correlations between backward- and forward-looking communication indices
Relationship between indicators

[[KC_IMAGE_010]]

Note: The figure plots the correlation between the forward- and backward-looking indices for each country.

## C. Stylized fact III: Inertia in central banks communication

Persistence is another key feature of central bank communication. Changes tend to occur gradually over time (see Figure 7). For example, the Bank of England and the ECB exhibit high inertia, with a one-year serial correlation of about 0.5. Emerging markets central banks also present a high correlation in the forward-looking index. While not presented here, the backward-looking index displays a high correlation too. This inertia and gradualism in communication mirrors the way central banks typically adjust policy itself, namely by implementing changes gradually to reduce the risk of abrupt reversals and the attendant risk to credibility. Consistent with this approach, standard reaction-function models characterize the policy rate as a weighted average of its past values and the notional desired policy rate (see Clarida, Galí, and Gertler 2000). For a broader overview of the literature on interest rate smoothing, see, among others, Coibion and Gorodnichenko (2012).

Figure 7. Inertia in the forward-looking communication index

[[KC_IMAGE_011]]

Note: The figure plots the autocorrelation in the forward looking index.

## V. HOW DO CENTRAL BANKS REACT TO UNCERTAINTY

In this section we analyze empirically how central banks shift their communication around monetary policy decision announcements when uncertainty increases. Commitment-based forward guidance (i.e., explicit communication about the future path of policy instruments) is one prominent tool used by central banks to anchor expectations under uncertainty. However, central banks also rely on information-based forward-looking communication, which conveys the likely direction of policy conditional on incoming data without making firm commitments. This allows the central bank to use its established credibility to obtain inflation outcomes with a smaller sacrifice ratio (see Morris and Shin 2018). For example, tightening (easing) monetary policy becomes more effective if agents lower (raise) their inflation expectations. On the other hand, when uncertainty also impairs central bank's ability to assess the outlook, limiting forward-looking communication may be optimal. In these situations, central banks may differ in weights placed on recent outturns, incoming information, their forecasts, and policy reaction functions. They might however continue to rely on information-based forward-looking communications to explain its decisions and reaction function. For instance, in 2022, the ECB announced that, given large forecast errors, its monetary policy decisions would be data-dependent, implying that incoming real time data would inform the policy decision more than in normal times. Around 2024, the Czech central bank also signaled a shift toward a more data-dependent, meeting-by-meeting approach. In comparison, the Riksbank re-introduced alternative scenarios in 2023 to more systematically complement baseline projections and better clarify its reaction function to different developments.

Thus, our focus is to test whether and how central banks change their communication in response to increased uncertainty. Given the substantial inertia in central bank communication observed in Figure 7, i.e. given the high serial-correlation in our measured communication indices, the empirical analysis focuses on a dynamic specification. Specifically, we use a 3-month lag index variable as a control in the main specifications. $^{6}$ The stylized facts in Section 5 show that central bank communication is both persistent and multidimensional. In particular, forward- and backward-looking language often move together (see Figure 6), reflecting periods of heightened communication intensity—such as around monetary policy decisions—when central banks simultaneously explain past actions and provide guidance about the future. To abstract from these common movements and focus on changes in the directional emphasis of communication, the empirical analysis in this section relies primarily on the net forward-looking index, defined as the difference between forward- and backward-looking language reflected in monetary policy statements, as defined in Equation 2. $^{7}$ This approach allows us to isolate shifts in the balance of communication, although it may mask episodes in which both forward- and backward-looking language increase simultaneously during periods of heightened communication intensity. To address this limitation, we complement the analysis by examining the forward- and backward-looking indices separately. Incorporating these stylized facts about the central bank communication indices, we estimate the following simple dynamic panel regressions at the monthly frequency how standard measures of uncertainty and policy rate affect the net forward-looking index.

$$
N e t I n d e x _ {i, t} = \alpha_ {i} + \beta_ {1} N e t I n d e x _ {i, t - 3} + \beta_ {2} V S T O X X _ {t - 1} + \beta_ {3} \Pi_ {U, t - 1} + \beta_ {4} P o l i c y r a t e _ {t - 1} + \varepsilon_ {i, t},\tag{3}
$$

where $NetIndex_{i,t}$ denotes the net forward-looking index obtained from monetary policy statements for country i and time t. $\alpha_{i}$ captures country fixed effects, and $\varepsilon_{i,t}$ is the idiosyncratic error term. The specification includes the lag of the dependent variable to capture persistence in central bank communication, reflecting the gradual adjustment of messaging over time. The model further incorporates a set of macro-financial determinants that may influence communication strategies: financial market volatility (VSTOXX), inflation expectations uncertainty ( $\Pi_{U,t-1}$ proxied by the disagreement in inflation expectations among forecasters), and the monetary policy stance, captured by the policy rate (Table 5 in the Appendix describes the variables used in more detail). All the explanatory variables enter the regression with a one-month lag, while the dependent variable is lagged by three months consistent with the typical interval between monetary policy press conferences. Standard errors are corrected for serial correlation applying the Newey-West procedure. We estimate Equation 3 for the full sample of countries and then repeat the analysis separately for advanced and emerging economies.

Table 1 reports the baseline results. As expected, central bank communication appears to be persistent, with the three-month lag entering positively and significantly in the regression. Inflation uncertainty appears to be an important determinant of central bank communication, but the signs suggest opposite moves for AEs versus EMs. While AE central banks react as expected to increasing inflation uncertainty by adopting a more forward-looking communication stance, EM central banks do the opposite by relying more on backward-looking language. In particular, AE may adopt a more forward-looking communication strategy to anchor expectations in line with their inflation-targeting mandates with a focus on information-based forward looking communications. This interpretation is consistent with the practice of AE central banks publishing future interest rate paths and scenarios, and relying more heavily on projections and forward guidance when inflation dynamics become less stable. The policy rate enters negatively and significantly for advanced economies, suggesting that they tend to become more backward-looking with a need to explain past policy decisions when rates are increased. In terms of economic importance, a 1 standard deviation increase in inflation uncertainty increases the use of net forward-looking language by 3.41. This compares with an effect of -4.5 for the policy rate, and -0.86 for financial volatility. In other words, inflation uncertainty is almost as important as the policy rate for the communication of AE central banks. As discussed in Blinder and others (2024), forward-looking policy communication is harder for the general public to interpret than backward-looking information, despite being readily absorbed by experts. Namely, Kryvtsov and Petersen (2021) show that forward-looking announcements have smaller effects on individual expectations than backward-looking announcements of interest rate changes. Finally, financial volatility does not correlate significantly with the net forward-looking communication in EM central banks, but leads to less forward-looking communication in AEs. One reason could be because central banks might need to do more explanation of past data during periods of noisy financial volatility

Table 1. Dynamic model - lag net forward-looking index


Note: Newey-West standard errors in parentheses. Significance levels: \* p<0.10, \*\* p<0.05, \*\*\* p<0.01.

We showed that inflation uncertainty, as proxied by forecasters' disagreements, is the main determinant of the shift in central bank communication towards a more forward-looking stance. We extend the framework in Equation 3 to a rolling panel regression to test the stability of the coefficient on inflation uncertainty over time to check if central banks in advanced economies always chose to be more forward looking when faced with increased inflation uncertainty or if there was any change in communication strategy. Thus, we estimate the Equation in 3 limiting the sample to a four years rolling-window. Figure 8 plots the coefficient over time. $^{8}$

Figure 8. AE central banks' communication responses to inflation uncertainty over time

[[KC_IMAGE_012]]

Note: The figure shows the coefficient on inflation uncertainty in a rolling window regression with the net forward-looking index on the left hand side. Standard errors are corrected for serial correlation.


on the financial volatility term suggests. $^{10}$ Overall, the recent change in communication style by AE central banks can be very informative about their main goal of better anchoring agents' expectations first in response to low inflation and the ELB and latter in an uncertain environment. Finally, the stock of central bank credibility might play a big role in how central banks respond to inflation uncertainty and might limit the scope of possible responses that central banks in emerging economies could choose.

To test if our findings are robust and other sources of uncertainty also matter for communication, we enrich our empirical model by incorporating a broader set of uncertainty proxies used in the literature (Table 2). Specifically, we include a standard measure of economic policy uncertainty (EPU) (Baker, Bloom, and Davis 2016), as well as forecaster disagreements on one-year ahead growth projections to proxy for growth uncertainty. Specifically, we expand equation 3 with the set of controls summarized in $X_{t-1}$ that includes both economic policy uncertainty and growth uncertainty.

$$
N e t I n d e x _ {i, t} = \alpha_ {i} + \beta_ {1} N e t I n d e x _ {i, t - 3} + \beta_ {2} V S T O X X _ {t - 1} + \beta_ {3} \Pi_ {U, t - 1} + \beta_ {4} P o l i c y r a t e _ {t - 1} + \beta_ {5} X _ {t - 1} + \varepsilon_ {i, t},\tag{4}
$$

The first result to highlight is that the inclusion of these additional uncertainty variables does not alter the results reported in Table 1: inflation uncertainty becomes even more important to explain the net forward-looking index of central bank communication. Second economic growth uncertainty is insignificant but economic policy uncertainty statistically significant in explaining the net forward-looking index in AE central banks communication. While financial volatility makes central banks adopt a more backward-looking communication, presumably because financial volatility could make central bank forecasts less reliable, economic policy uncertainty increases forward communication, possibly reflecting the need for more conditional guidance in the face of policy uncertainty, buttressed by the recent evolution of policy tools used by AE central banks (see Box 1). In summary, the results suggest that AE central banks tend to respond to inflation expectations uncertainty by preserving or even strengthening forward-looking guidance, while EM central banks respond to uncertainty by shifting more decisively toward backward-looking, data-dependent communication. Since these uncertainty measures tend to be highly correlated, we run robustness tests in the appendix where we add one variable at a time to our baseline model. We showed that our results are robust to the addition of different measures of uncertainty sequentially and are not driven by multicollinearity of the these variables.

Finally, while the net forward-looking index serves as the main focus to characterize central bank communication, it is also informative to decompose the effects into separate forward- and backward-looking components. The first three columns of Table 3 report estimates from the dynamic panel specifications for the forward-looking communication index, allowing explicitly for strong persistence in communication behavior across different income groups. Across the entire sample, the lagged dependent variable enters with a large and highly significant coefficient, confirming that forward-looking communication is highly persistent over time. In the full sample, this persistence absorbs a substantial share of the variation. Market-based uncertainty (financial volatility) seems to lower the amount of forward looking communication. Once again, there is great differentiation across country groups. In AEs (second column in Table 3), inflation expectations uncertainty emerges as the dominant driver of forward-looking communication, with coefficients that are economically and statistically significant. In EMs (third column in Table 3), inflation expectations uncertainty lower the amount of forward-looking language. Finally, market-based uncertainty also seems to drive lower use of

Table 2. Dynamic model - lag net forward-looking index with more uncertainty measures


Note: Newey-West standard errors in parentheses. Significance levels: \* p<0.10, \*\* p<0.05, \*\*\* p<0.01.

forward-looking communication across AEs and EMs. These results suggest that EMs respond in a broadly similar manner to different sources of uncertainty, but they generally rely less on forward-looking communication when inflation uncertainty increases. The last three columns in Table 3 confirm that backward-looking communication is also highly persistent across all samples, with lag coefficients of similar magnitude. In the full sample (column four in Table 3), financial market volatility is the only significant variable to explain backward-looking communication, indicating that higher financial volatility leads central banks to place relatively less emphasis on retrospective assessments.

In AEs (column five in Table 3), backward-looking communication only responds to financial volatility, with higher financial volatility associated with a reduced emphasis on backward-looking language. This is consistent with AE central banks shifting away from historical narratives when uncertainty increases, instead favoring forward-looking language. In EMs (column six in Table 3), market based uncertainty is the only variable that matters statistically and with a negative coefficient. Similar to advanced economies, under increased market volatility, EM central banks actively de-emphasize backward-looking language, maybe because of increased noise in past data. The fact that both backward- and forward-looking communication decline in response to financial market uncertainty implies that central bank communication tends to avoid sentences that either look back and explain what happened or provide an assessment of, or guidance on, future developments. It is also important to acknowledge that the dictionary we used to build our indices is more geared toward backward communication on inflation as opposed to financial variables. Hence, backward-looking communication should be interpreted as referring to monetary policy and inflation aspects, and not backward-looking in general. Moreover, while this effect is present in both country groups, it is economically and statistically stronger in EMs, where financial uncertainty significantly decreases backward-looking communication. In AEs, these relationships are weaker and less stable across specifications, suggesting greater flexibility in communication strategies.

Table 3. Correlates of forward-/backward-looking communication - decomposing the net forward-looking index


Note: Newey-West standard errors in parentheses. Significance levels: \* p<0.10, \*\* p<0.05, \*\*\* p<0.01.

## A. Net forward-looking language as an anchoring device

The results in this section suggest that central banks in advanced economies have responded to inflation uncertainty with more forward-looking messaging in their policy decision statements. One reason for this type of communication might be the objective to anchor agents' expectations during uncertain times. In this subsection, we test this hypothesis. We first build a measure to capture market pricing of monetary policy uncertainty as the monthly standard deviation of the daily market pricing for the policy rate two months ahead of a policy rate decision announcement. Since this metric is not easily available for every country, we constrain our analysis to the European Central Bank (ECB). To test if adopting more net forward-looking communication helps to anchor agents' expectations about policy rate decisions we run the following regression:

$$
\text { MonetaryPolicyUncertainty } _ {i, t} = \alpha_ {i} + \beta_ {1} \text { NetIndex } _ {i, t - 1} + \beta_ {2} \text { VSTOXX } _ {t} + \beta_ {3} \pi_ {t} + \beta_ {4} \text { Policyrate } _ {t} + \beta_ {5} F F R _ {t} + \varepsilon_ {i, t},\tag{5}
$$

where Monetary policy uncertainty is the standard deviation of the daily market pricing for the policy rate two months ahead of a policy rate decision announcement. Controls include financial volatility, headline inflation, the deposit facility rate, and the US federal funds rate as factors driving markets' interest rates expectations. The regression is subject to an obvious endogeneity problem. The ECB might decide to increase its forward-looking communication because market interest rate pricing volatility is high. In other words, we might have a problem of reverse causality. Indeed, Figure 9 shows during the ECB's hiking cycle, the increase in monetary policy uncertainty, as proxied by markets uncertainty about future rates, seems to be driving a reaction in communication by the ECB.

Figure 9. Monetary policy uncertainty and net forward-looking communication

[[KC_IMAGE_013]]

Note: The figure shows the rolling daily standard deviation of market pricing of monetary policy two meetings ahead and our measure of net forward-looking index communication.

In fact, the results of the OLS estimation in the first column of Table 4 show that the net forward-looking communication is positively associated with monetary policy uncertainty, meaning that forward-looking communication is associated with an increase of market uncertainty on future policy. The reverse causality can be driving this result if the central banks become much more forward-looking in communications following an increase in market measured monetary policy uncertainty. $^{[11]}$ In order to account for these outlier periods, when the reverse causality might be of a particular concern, we use the MM-estimator by Yohai (1987). The MM-estimation mitigates the influence of extreme observations that disproportionately affect OLS estimates, which seems to be the case in our monetary policy uncertainty series. After controlling for the extreme observations, we see that coefficient on net forward-looking index is now negative and significant suggesting that an increase in the degree of forward looking communication is negatively associated with lower market interest rate expectation volatility. Note that the MM estimator might still be biased upward (making it to be less negative) because of the reverse causality, so the true effect of forward-looking communication might be even larger on market interest rate expectation volatility. While more formal tests can be derived to better make this point, this evidence suggests that more forward-looking language could be a tool for central banks to use to anchor expectations in an uncertain environment.

## VI. HOW DO CENTRAL BANKS COMMUNICATE UNCERTAINTY

The previous section documented how central banks changed guidance communication based on increased uncertainty among market participants, professional forecasters, or the broader public. A related question is the

Table 4. Anchoring of market interest rate expectations


reverse: what is the central banks' own account of uncertainty, and how does the audience of CB communication react to it? To do a cross-country comparison of how central banks communicate uncertainty, we build another numerical index on uncertainty. We apply the same technique as described in Section III to construct a central bank uncertainty index (CBUI). More specifically, the CBUI is based on a dictionary and frequency counts. The dictionary used is to built the CBUI is given by the following list of words: “uncertainty”, “uncertain”, “unclear”, “lack of clarity”, “ambiguity”, “unknown”, “unpredictability”, “volatile” and “volatility”. We once again use monetary policy statements as the main text through which central banks are communicating. The index then is the frequency of phrases using any of the words in our dictionary overall the total number of phrases in the monetary policy statement. The CBUI is available for 11 countries, five AEs and six EMs. Figure 10 summarizes the overall evolution of this indicator over time by AE and EM economies. As it can be seen, the indicator is highly correlated with periods of heightened uncertainty, reflecting that central banks tend to communicate uncertainty in their policy decision statements around uncertainty events.

Figure 10. Central bank uncertainty aligns with large shock events

[[KC_IMAGE_014]]


The trends in the CBUI across all countries and in the subindices for AEs and EMs are broadly similar. Spikes generally coincide with large shocks such as the Global Financial Crisis, Brexit, COVID-19, and tariff announcements. There has also been an increasing trend over the last decade, with central banks placing greater emphasis on uncertainty in their communications.

Yet, while all central banks increasingly discuss uncertainty, they do not seem to do so simultaneously all the time. Looking at the correlation between individual economy's CBUI, we find that the average correlation of the uncertainty index is limited (see Figure 11), especially when compared to the correlation of central bank policy rates (see Figure 11). This idiosyncratic behavior with temporary strong co-movements (see Figure 12) likely reflects different messages central banks want to convey at a particular conjuncture (of global calm), while none can escape large global shocks.

Figure 11. Cross-country correlation of the CBUI and policy rates

CBUI


[[KC_IMAGE_015]]


[[KC_IMAGE_016]]


Figure 12. Rolling correlation of CBUI

[[KC_IMAGE_017]]


Notwithstanding country idiosyncrasies, the common spikes and upward trend, suggests that central banks' own account of uncertainty is broadly aligned with other major metrics of uncertainty. A formal regression analysis confirms this. The CBUI aligns closely with economic policy uncertainty $^{12}$ which is the largest driver of an increase in CBUI, followed distantly by the level of inflation and its standard deviation (Figure 13). While central bank communication appears to react mostly to inflation (and to a lesser extent financial) uncertainty, central banks' own account of uncertainty is mostly related to global economic uncertainty. That is, central banks appear more willing to communicate about uncertainty when general economic uncertainty is high, as opposed to when uncertainty concerns central banks' own objectives. This may be unsurprising, as it could reflect a tendency to avoid confirming destabilizing beliefs and thus prevent "bad" equilibria.

Figure 13. What drives central banks to talk about uncertainty

[[KC_IMAGE_018]]

This figure reports the relative importance of each explanatory variable in accounting for variation in the uncertainty index. The measure is based on changes in the regression $R^{2}$ for each variable, we compute the reduction in the model's $R^{2}$ when that variable is excluded from an otherwise identical specification with country fixed effects. The resulting difference in $R^{2}$ captures the unique explanatory contribution of each variable, conditional on the inclusion of all other controls. Larger bars indicate variables whose exclusion leads to a larger loss of explanatory power.

Communicating about uncertainty could reflect central banks attempt to discuss factors which affect model uncertainty and signal possible uncertainty about the future monetary policy path. To analyze this possibility, we explore to which degree our CBUI is correlated with the market pricing of monetary policy uncertainty. We measure the latter as the monthly standard deviation of the daily market pricing for the policy rate two months ahead of a policy rate decision announcement for two cases where data is easily available to derive such metrics. Figure 14 and 14 contrast the respective country's CBUI with the uncertainty about monetary policy decisions derived from market pricing for the Riksbank and the ECB (blue dotted line in the charts). Although the correlation between the two measures is generally low over the full sample, it rose noticeably in the post-pandemic period—particularly during the 2022 hiking cycle and most prominently in Sweden. This pattern suggests that common factors were driving both measures during this period. One plausible interpretation is that market participants began to treat the uncertainty embedded in monetary policy statements as informative about the distribution of future policy decisions themselves. More recently, a widening gap has emerged between both measures, especially after November 2024. This divergence suggests that markets currently perceive little uncertainty about near-term central bank actions, even as monetary policy statements convey elevated levels of economic uncertainty.

Figure 14. CBUI Highly Correlated with Policy Rate Pricing Uncertainty During Certain Periods
Sweden: CBUI vs market based monetary policy uncertainty

[[KC_IMAGE_019]]


ECB: CBUI vs market based monetary policy uncertainty

[[KC_IMAGE_020]]

Note: The blue series measures the monthly standard deviation of the daily market pricing for the two months ahead ECB/Riksbank meeting. The yellow line is our uncertainty index, which measures the words related to uncertainty over the total number of words in each ECB's/Riksbanks's monetary policy statement.

One communication tool that may have helped anchor expectations about monetary policy even amid heightened uncertainty is scenario analysis. Several AE central banks have started to employ scenario analysis more formally in their communication toolkit. Box 1 provides an overview of its application in three European AE central banks. While we highlight the merits of scenario analysis based on emerging evidence, its relatively short history makes an empirical assessment of its effects premature.

## Box 1: Scenario analysis in central bank communication

To better communicate heightened uncertainty, many AE central banks have incorporated scenario analysis in their communication, increasing the conditionality of forward guidance. In particular, following the 2024 Bernanke Review (see Bernanke 2025), the Bank of England has progressively integrated scenario analysis into its policymaking and communication. The scenarios are more than mere shocks; they explore different economic trajectories – something that the BoE has repeatedly emphasized. The scenarios approach has brought benefits for both policymaking and communications. For policymaking, it has enriched MPC discussions by illustrating alternative economic states, mechanisms and structural changes, fostered robust internal debates by providing a common framework and discipline, and ensured more robust policy decisions by forcing “what if” discussions. For communications, scenarios transparently acknowledge uncertainty and disclose the reaction function, allowing MPC members to associate themselves with different scenarios to justify their views. Hence it provides richer economic storytelling, which is seen as superior to traditional fan charts where the focus tended to be on the middle path.

At the ECB, scenario analysis has been integrated into its monetary policy assessments and stress-testing frameworks. Scenarios are derived from macroeconomic models reflecting different economic conditions, such as varying inflation rates or geopolitical tensions. European Central Bank (2025a) underlined that scenarios bring transparency and guard against false certainty. In response to the post-pandemic inflation surge and structural shifts (e.g., digitalization, geopolitical tensions), the ECB emphasized the need for flexibility and robustness in its communication. The ECB communicates these scenarios in its Economic Bulletin, press conferences and blogs, aiming to provide clarity to the market and general public on potential risks to the euro area economy. Since the pandemic, the ECB has published scenario analysis including modeling shocks such as energy, trade, or geopolitical events. Also, European Central Bank (2025b) strategy assessment emphasized scenarios in showing how wars or pandemics shape inflation, e.g., Ukraine scenario predicted above 7 percent inflation vs baseline of about 5 percent, aligning with realized 8 percent. Key strengths of ECB's scenario analysis include the comprehensive nature of the scenarios, which cover a wide range of economic shocks and tail risks. However, the complexity of the models used underscores the continued need to use a wide range of communication tools to provide clarify to the market and the public. Continued efforts are also needed to contextualize the scenarios and better communicate on the probability of the scenarios (see Dizioli 2025).

The Riksbank had a long-standing tradition of developing and publishing alternative scenarios, both as part of its internal analysis and its external communications. Since 2007—and more systematically since 2023—the Riksbank has incorporated alternative scenarios into its monetary policy communication to complement its baseline projections (see Seim 2025). It explicitly notes that “it is difficult to say in advance how monetary policy will react,” thereby signaling a wider policy reaction function and greater conditional uncertainty. In such circumstances, scenarios simulate macroeconomic developments using specific assumptions and shocks, offering detailed narratives that clarify potential risks and the bank’s Executive Board’s likely responses. Typically, two alternative scenarios are presented. These are constructed by applying shocks to the central projection and, when necessary, by adjusting structural parameters or assumptions about the Riksbank’s reaction function. The scenarios are generally symmetrical, illustrating the effects of both upside and downside risks to the policy rate forecast. Each scenario is accompanied by a detailed narrative, with outcomes for inflation, GDP, and the policy rate path presented in charts. The scenarios reflect the Executive Board’s views on the main risks to the outlook, and the Board assumes responsibility for them. Unlike probabilistic fan charts, they provide structured insights into how policy might adapt under different conditions. Crucially, they also serve to test the robustness of the baseline policy by comparing outcomes across multiple plausible states, thereby enhancing transparency and credibility in an uncertain environment.

## VII. CONCLUSION

Shocks to economies have intensified in recent years, and heightened uncertainty is expected to persist in the near-term. In such periods, effective central bank communication becomes more challenging yet more critical because it plays a key role in managing expectations and maintaining central bank credibility. With conventional monetary policy signals becoming increasingly noisy and forecasting more difficult, central bank communication has evolved from a supporting tool into a core policy instrument for shaping expectations and strengthening policy credibility.

This study examines how European central banks have responded to heightened uncertainty by adapting their communication toolkits and styles. We survey recent central bank communication practices across advanced and emerging economies in Europe and leverage novel text-mining-based indicators constructed from monetary policy statements to decode the trend. In particular, we develop indicators to quantify the degree to which central banks rely on forward-looking versus backward-looking language over time. These indicators are then linked to multiple sources of uncertainty—including inflation uncertainty, financial market volatility, and economic policy uncertainty—to assess how communication styles adjust across advanced and emerging market economies.

We find that communication frameworks of twenty European central banks exhibit notable similarities in formal toolkits but substantial differences in transparency, frequency, and sophistication. This is reflected in a clear distinction in communication styles between advanced and emerging economies. In advanced economies, an increase in inflation expectations uncertainty leads central banks to use more forward-looking language relative to backward-looking language, which highlights the importance of expectations management and the use of forecasts when inflation dynamics become less predictable. Survey evidence also suggests more emphasis on conditional forward guidance using scenario analysis. In contrast, emerging economies do not systematically shift communication styles when faced with increased uncertainty in inflation expectations. AE central banks become less forward-looking under high financial market volatility, which could suggest that those central banks assess past data to be noisy information about the future.

Overall, these findings underscore that communication strategies differ between central banks and are also state-dependent, reflecting differences in policy frameworks, credibility, and macroeconomic environments. Specifically, the findings are consistent with the view that credibility may support the effectiveness of forward-looking communication. In other words, central banks with well-anchored expectations can afford to provide guidance even under uncertainty, while those with weaker credibility may rationally limit forward commitments. That said, use of information-based forward-looking communications can help central banks build credibility over time. Moreover, communication strategies are state-contingent, adjusting not only to the level but also to the source of uncertainty. Finally, transparency tools—such as scenarios and fan charts—may help reconcile the trade-off between guidance and flexibility under uncertainty by conveying uncertainty explicitly rather than suppressing forward-looking information. Even highly credible central banks have improved the conditionality of their forward guidance in practice, such as by clarifying reaction functions in scenario analysis.

Future research could extend this work by exploring contextual language models and other advanced approaches to capture richer semantic and linguistic features of central bank communication and by linking communication styles more directly to market and household expectation measures to shed more light on their effectiveness.

Albrizio, Silvia, Allan Dizioli, Pedro Simon, and Yifan Zhang, 2025, “Attention, Please! Listening to the Central Bank in Uncertain Times,” in AEA Papers and Proceedings, Vol. 115, pp. 254–260 (American Economic Association 2014 Broadway, Suite 305, Nashville, TN 37203).

Altavilla, Carlo, Refet Gürkaynak, Thilo Kind, and Luc Laeven, 2025, “Monetary Transmission with Frequent Policy Events,” CEPR Discussion Paper 20196, Centre for Economic Policy Research, cEPR Discussion Paper No. 20196.

Angeletos, George-Marios, and Chen Lian, 2018, “Forward Guidance without Common Knowledge,” American Economic Review, Vol. 108, No. 9, pp. 2477–2512.

Armelius, Hanna, Christoph Bertsch, Isaiah Hull, and Xin Zhang, 2018, “Spread the Word: International Spillovers from Central Bank Communication,” Working Paper Series 357, Sveriges Riksbank (Central Bank of Sweden).

Bailey, Andrew, 2025, “Monetary policy in uncertain times,” Speech at the Reykjavík Economic Conference, delivered in May, accessed: 30 December 2025.

Baker, Scott R., Nicholas Bloom, and Steven J. Davis, 2016, “Measuring Economic Policy Uncertainty\*,” The Quarterly Journal of Economics, Vol. 131, No. 4, pp. 1593–1636.

Bems, Rudolfs, Francesca Caselli, Francesco Grigoli, and Bertrand Gruss, 2021, “Expectations’ anchoring and inflation persistence,” Journal of International Economics, Vol. 132, p. 103516.


Bholat, David, Stephen Hansen, Pedro Santos, and Cheryl Schonhardt-Bailey, 2015, “Text mining for central banks: handbook,” Centre for Central Banking Studies Handbook, , No. 33, pp. 1–19.

BIS, 2025, Monetary policy decision-making and communication under high uncertainty, BIS Papers, Vol. None (Bank for International Settlements), none ed.

Blinder, Alan S., Michael Ehrmann, Jakob de Haan, and David-Jan Jansen, 2024, “Central Bank Communication with the General Public: Promise or False Hope?” Journal of Economic Literature, Vol. 62, No. 2, p. 425–57.

Blinder, Alan S., Michael Ehrmann, Marcel Fratzscher, Jakob De Haan, and David-Jan Jansen, 2008, “Central Bank Communication and Monetary Policy: A Survey of Theory and Evidence,” Journal of Economic Literature, Vol. 46, No. 4, p. 910–45.

Brainard, William C., 1967, “Uncertainty and the Effectiveness of Policy,” The American Economic Review, Vol. 57, No. 2, pp. 411–425.

Brandão-Marques, Roland Meeks, Luis, and Vina Nguyen, 2024, “Monetary Policy with Uncertain Inflation Persistence,” IMF Working Papers, Vol. 2024, No. 047, p. 1.

Casiraghi, Marco, and Leonardo Pio Perez, 2022, “Central bank communications,” IMF Technical Assistance Handbook.

Christiano Silva, Thiago, Kei Moriya, and Romain Veyrune, 2025, “From Text to Quantified Insights: A Large-Scale LLM Analysis of Central Bank Communication,” Techn. rep., International Monetary Fund Working Paper.

Clarida, Richard, Jordi Galí, and Mark Gertler, 2000, “Monetary Policy Rules and Macroeconomic Stability: Evidence and Some Theory\*,” The Quarterly Journal of Economics, Vol. 115, No. 1, pp. 147–180.

Coibion, Olivier, and Yuriy Gorodnichenko, 2012, “Why Are Target Interest Rate Changes So Persistent?” American Economic Journal: Macroeconomics, Vol. 4, No. 4, p. 126–62.

Cole, Stephen, Enrique Martinez-Garcia, and Eric R Sims, 2023, “Living Up to Expectations: Central Bank Credibility, the Effectiveness of Forward Guidance, and Inflation Dynamics Post-Global Financial Crisis,” Working Paper 31777, National Bureau of Economic Research.

Crowe, Christopher, and Ellen E Meade, 2008, “Central bank independence and transparency: Evolution and effectiveness,” European Journal of Political Economy, Vol. 24, No. 4, pp. 763–777.

Dizioli, Allan, 2025, “Interest Rate Sensitivity Scenarios to Guide Monetary Policy,” IMF Working Papers, Vol. 2025, No. 107, p. 1.

Dupraz, Stephane, Sophie Guilloux-Nefussi, and Adrian Penalver, 2023, “A Pitfall of Cautiousness in Monetary Policy $^{a}$ —,” International Journal of Central Banking, Vol. 19, No. 3, pp. 269–323.


Evdokimova, T, PN Mohácsi, O Ponomarenko, and E Ribakova, 2023, “Central banks and policy communication: How emerging markets have outperformed the Fed and ECB| PIIE,” Techn. rep., Section: Working Papers 23-10.

Fadda, Pietro, Rayane Hanifi, Klodiana Istrefi, and Adrian Penalver, 2025, “Central bank communication of uncertainty,” Journal of International Money and Finance, Vol. 157, p. 103385.

Garga, Vaishali, Edward P. Herbst, Alisdair McKay, Giovanni Nicolo, and Matthias Paustian, 2025, “Monetary Policy, Uncertainty, and Communications,” Finance and Economics Discussion Series, , No. 2025-074, pp. 1–1.

Georgieva, Kristalina, 2025, “Resilience in a World of Uncertainty.” Speech at the 2025 Annual Meetings Plenary, delivered in October, accessed: 30 December 2025.

Gust, Christopher, Edward Herbst, and David López-Salido, 2025, “Optimal monetary policy with uncertain private sector foresight,” Journal of Monetary Economics, Vol. 155, p. 103826.

Hagedorn, Marcus, Jinfeng Luo, Iourii Manovskii, and Kurt Mitman, 2019, “Forward guidance,” Journal of Monetary Economics, Vol. 102, pp. 1–23.

International Monetary Fund, 2020, “The Central Bank Transparency Code,” Imf policy paper, International Monetary Fund, approved by the Executive Board on June 4, 2020.

Jeanneau, Serge, 2009, “Communication of monetary policy decisions by central banks: what is revealed and why,” BIS papers.

Kryvtsov, Oleksiy, and Luba Petersen, 2021, “Central bank communication that works: Lessons from lab experiments,” Journal of Monetary Economics, Vol. 117, No. C, pp. 760–780.

Lagarde, Christine, 2025, “From resilience to strength: unleashing Europe’s domestic market..” Speech at the 35th Frankfurt European Banking Congress, delivered in November, accessed: 30 December 2025.

Morris, Stephen, and Hyun Song Shin, 2018, “Central bank forward guidance and the signal value of market prices,” Vol. 108, pp. 572–577.

Orphanides, Athanasios, 2019, “Monetary policy strategy and its communication,” in Federal Reserve Bank of Kansas City 2019 Jackson Hole Economic Policy Symposium, Challenges for Monetary Policy, Jackson Hole, August, pp. 211–260.

——, 2025, Enhancing Resilience with Monetary Policy Rules (Hoover Institution Press).


Soederstroem, Ulf, 2002, “Monetary Policy with Uncertain Parameters,” Scandinavian Journal of Economics, Vol. 104, No. 1, pp. 125–145.

Yohai, Victor J, 1987, “High breakdown-point and high efficiency robust estimates for regression,” The Annals of statistics, pp. 642–656.

## APPENDIX A. APPENDIX

## A.1. Data

Table 5. Description of variables used among different specifications


## A.2. Robustness with static equation

While the dynamic model is more appropriate to the current analysis, as we showed that central bank communications are very correlated over time, as central banks usually try to keep consistent communications and do modifications at the margin, as a robustness exercise in this section we will re-estimate the model in Equation 3 using a static framework. In particular, we will be estimating the following equation:

$$
N e t I n d e x _ {i, t} = \alpha_ {i} + \beta_ {1} V S T O X X _ {t - 1} + \beta_ {2} \Pi_ {U, t - 1} + \beta_ {3} P o l i c y r a t e _ {t - 1} + \beta_ {4} X _ {t - 1} + \varepsilon_ {i, t}.\tag{6}
$$

The variables are the same as in the extended version of Equation 3 – it includes the set of additional controls X (i.e., EPU and growth uncertainty) but it does not control for the lagged net forward-looking index. Standard errors are clustered at the country level to account for serial correlation and heteroskedasticity. We again estimate Equation 6 for the full sample of countries and then repeat the analysis separately for advanced and emerging economies.

Table 6 summarizes the determinants of net forward-looking index in central bank communication for the static model. In the full sample (first column in Table 6), the signs are similar to the ones of the dynamic model, but no variable is statistically significant. The lack of significance again probably reflects the slow moving communication styles in central banks' communication.

However, the results with the overall sample mask large heterogeneity across advanced and emerging economies. In advanced economies (column 2 in Table 6), the net forward-looking index is once again strongly and positively associated with inflation expectations uncertainty, with even larger and more significant than in the dynamic model. Once again the policy rate enters negatively in this regression, indicating that central banks in advanced economies tend to use more backward-looking language to explain the movements in the policy rate. For example, central banks in advanced economies would tend to justify why they raised rates using backward-looking language. In contrast, emerging economies (column 3 in Table 6) display a markedly different pattern. While no variable is statistically significant, the signs remain the same as in the dynamic model. In particular, inflation uncertainty does not increase net forward-looking communication. This result once again suggests that emerging economies respond to inflation uncertainty by shifting more decisively toward backward-looking, data-dependent communication.

Table 6. Static model - Net forward-looking index with more uncertainty measures


Standard errors in parentheses. Country fixed effects included. Standard errors clustered at the country level. $^{*}$ p < 0.10, $^{**}$ p < 0.05, $^{***}$ p < 0.01

## A.3. Robustness with equation in 12-months difference

Given the substantial inertia in some central bank communication, i.e. given the high serial-correlation in our measured communication indices, we re-estimate the panel fixed-effect Equation 3 in a 12-months difference, that is, we estimate the following equation:

$$
\begin{array}{l} Y _ {i, t} - Y _ {i, t - 1 2} = \alpha_ {i} + \beta_ {1} \big (\mathrm{VSTOXX} _ {t - 1} - \mathrm{VSTOXX} _ {t - 1 3} \big) \\ \qquad + \beta_ {2} \big (\mathrm{EPU} _ {t - 1} - \mathrm{EPU} _ {t - 1 3} \big) \\ \qquad + \beta_ {3} \big (\text { UncertaintyIndex } _ {t - 1} - \text { UncertaintyIndex } _ {t - 1 3} \big) \\ \qquad + \gamma^ {\prime} \big (\mathbf {X} _ {i, t - 1} - \mathbf {X} _ {i, t - 1 3} \big) + \varepsilon_ {i, t}. \end{array}\tag{7}
$$

where again $Y_{i,t} \in \left\{ Backward Index_{i,t}, Forward Index_{i,t} \right\}$ , and in successive specifications, the vector $X_{i,t-1} - X_{i,t-13}$ includes the 12 months difference of lagged inflation expectations uncertainty, the policy rate, and GDP growth expectations uncertainty. All regressions are estimated using within-country variation, and stan-

dard errors are clustered at the country level. We again estimate Equation 7 for the full sample of countries and then repeat the analysis separately for advanced and emerging economies.

The regressions in Tables 7-9 show that changes in net forward-looking index are most robustly explained by changes in the uncertainty index. Across all specifications, the coefficient on the change in uncertainty is positive and statistically significant, indicating that when central banks explicitly acknowledge greater uncertainty in their statements, they tend to shift toward more forward-looking communication relative to backward-looking language. Other variables, such as changes in financial market volatility, economic policy uncertainty, uncertainty in inflation forecasts, policy rate, and uncertainty in GDP growth forecasts, are generally insignificant.

Table 7. Explaining the change in net forward-looking index all sample


Standard errors in parentheses
Country fixed effects included. Standard errors clustered at the country level. Significance levels: \* p<0.10, \*\* p<0.05, \*\*\* p<0.01.

However, once again pooling the results of advanced economies with emerging economies masks large differences across these groups. In advanced economies, Table 8, the positive association between the change in uncertainty and the change in net forward-looking index remains, but the coefficient is less precisely estimated and loses statistical significance. Instead, the most notable finding is the strong and significant positive effect of uncertainty in inflation forecasts on net forward-looking index. This suggests that central banks in advanced economies respond to increased uncertainty in inflation expectations by reinforcing forward-looking communication, consistent with their greater reliance on projections, forecasts, and explicit guidance frameworks. Additionally, changes in the policy rate and GDP growth uncertainty have negative and sometimes significant effects, indicating that tightening monetary policy or greater growth uncertainty makes central banks in advanced economies to be more backward-looking and data-dependent.

Meanwhile, for emerging economies, Table 9, the results show a positive and sometimes significant effect of the change in uncertainty index on the change in net forward-looking index, similar to the full sample. However, the effect is generally smaller and less robust than in advanced economies. Uncertainty in inflation forecasts also enters positively and is significant in some specifications, but the magnitude is lower than in ad-

Table 8. Explaining the change in net forward-looking index advanced


Standard errors in parentheses
Country fixed effects included. Standard errors clustered at the country level.
Significance levels: \* p<0.10, \*\* p<0.05, \*\*\* p<0.01.

Table 9. Explaining the change in net forward-looking index developing


Standard errors in parentheses
Country fixed effects included. Standard errors clustered at the country level.
Significance levels: \* p<0.10, \*\* p<0.05, \*\*\* p<0.01.

vanced economies. Other macroeconomic variables, including changes in financial market volatility, policy rate, and GDP growth uncertainty, do not have significant effects. This pattern suggests that emerging economy central banks do respond to explicit uncertainty by shifting toward more forward-looking communication, but the response is less pronounced and less consistently tied to uncertainty in inflation forecasts than in advanced economies.

A clear distinction emerges between advanced and emerging economies. In advanced economies, the change in net forward-looking index over the course of a year is strongly and positively associated with professional forecasters uncertainty in inflation forecasts, highlighting the importance of expectations management and the use of forward-looking language when inflation dynamics become less predictable. In contrast, emerging economies show a more modest and less consistent response to uncertainty in inflation forecasts. Overall, these results suggest that while central banks in both advanced and emerging economies adjust their communication in response to rising uncertainty, advanced economies tend to reinforce forward-looking guidance in the face of uncertainty in inflation forecasts, whereas emerging economies show a less pronounced shift toward forward-looking communication.

## A.4. Robustness controlling for the zero lower bound

This section includes a dummy variable for the zero lower bound period. In our sample Czech Republic, ECB, the United Kingdom, Poland and Sweden all experienced some periods of the zero lower bound. Results do not change much when controlling for the zero lower bound.

Table 10. Dynamic model - lag net forward-looking index with more uncertainty measures


Standard errors in parentheses
Country fixed effects included. Standard errors clustered at the country level.
\* $p < {0.10},{}^{* * }p < {0.05},{}^{* *  * }p < {0.01}$

## A.5. Robustness to different dictionary: the ECB index

A central bank should always be data dependent, but the term has been used in different ways and in different contexts across central banks. As a result, interpreting "data dependence" as inherently backward-looking may be misleading. In the case of the ECB, one could argue that the term is often used in a forward-looking sense, namely to communicate that future policy decisions will depend on incoming information—including updated projections—while avoiding pre-commitment to a particular policy path. From this perspective, references to data dependence may be better interpreted as an absence of forward guidance rather than as evidence of backward-looking communication. Given these alternative interpretations, this appendix evaluates the extent to which data-dependence-related terms affect the backward-looking index constructed in the main text.

Figure 15 plots the original index identified in the main text (orange line) alongside an alternative index constructed using the same dictionary but excluding terms related to data dependence (blue line). By construction, the blue line is lower than the orange line because the latter is based on a broader set of terms. More importantly, the two indices exhibit a high degree of co-movement, with a correlation coefficient of 0.85. In recent years, the ECB has made more frequent use of data-dependence-related language, which is reflected in the larger increase in the original index relative to the alternative measure. Nevertheless, the upward trend remains evident even after excluding these terms, indicating that ECB communication has become more backward-looking over time irrespective of how data dependence is classified.

Finally, it is important to emphasize that a shift toward more backward-looking communication does not necessarily imply a less sophisticated communication strategy. Indeed, in July 2022 the ECB deliberately discontinued commitment-based forward guidance and adopted a meeting-by-meeting, data-dependent approach. This reflected a strategic decision to preserve policy flexibility in an environment characterized by exceptionally high forecast uncertainty.


[[KC_IMAGE_021]]

Figure 15. ECB's backward-looking communication index: Robustness to dictionary
This figure reports the backward-looking index excluding the terms related to data dependence.


[[KC_IMAGE_022]]
