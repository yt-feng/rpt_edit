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
## 7 Takeaways Post K3 Release: Connect The Dots on Models, Cloud & Applications

Highlights (1) Moonshot AI: K3 is far from reaching upper limit in intelligence. ARR has fastest growth the next day; (2) More T-parameters China models (e.g. Qwen3.8, 2.4T) to come; (3) Updates from Zhipu and Stepfun; (4) Compute is focus on recent financing /KC Preview (link); (5)Token Expenditure Index remains soft; (6) Video models landscape do not see notable change;(7) Tencent's WorkBuddy gains traction; (8) Reaffirm Buy on BABA's full stack capabilities

In this report, we provide investors with data points on model pricing by companies, pricing comparison between China and US, model intelligence from Artificial Analysis, token consumption in OpenRouter, Token Expenditure Index trends and other industry data for analysis.

Closing the gap amid competition. Investors are surprised to see K3 (link) achieved new intelligence milestone and ranked at top positions in different metrics. According to Arena (Exhibit 5). This is the first time China takes the lead over US models in Frontend Code Arena vs early 2025 (DeepSeek-R1 is the last Chinese models came close with US models). Investors feedback is more about the closing of intelligence gap and anticipate more Chinese models (Exhibit 2) having T-parameter in coming months. Balance between intelligence and good to use amid supply constraints For Chinese models is expected.

Moonshot AI: Still far from the upper limit in model intelligence. ARR reached the fastest growth rate the next day. According to STAR Market Daily, President Mr.Zhang highlights (1) Scaling Law is valid. K3 is not the most intelligent model despite a big advancement is made vs K2.6; (2) It is still early to talk about the upper bound of model intelligence; (3) ARR experienced the fastest growth rate the next day post K3 release.

Latest strategies from Zhipu and Stepfun on industry trends. (1) Zhipu: (a) Scaling Law continues to accelerate across data, environment, RL and infra. (b) GLM-5.2 has less parameters vs K3. It can exceed K3 capabilities when scale to latter's level. Please refer to page 2 for details; (2) Stepfun: During WAIC (a) agents become the atomic unit of productivity; (b) integration between AI and terminals is the next focus; (c) AI coding exceeds human; (d) Agent-to-Agent is the next internet

Compute is the focus on recent financing by AI Lab and Kingsoft Cloud Preview. Recent financing of AI Lab (link) (1) DeepSeek (USD7bn, Jun-26); (2) Zhipu (USD4bn, Jul-26 and (3) MiniMax (USD2bn, Jul-26). We view new funding can strengthen respective computing needs amid surging demand. For Kingsoft Cloud, we adjust our revenue slightly in 2Q, factoring in the supply constraints issues with capex spending happened more in Jun vs Apr/May (link)

Token expenditure trends reflect highly cost efficient model is important. According to Silicon Data LLM Token Expenditure Index (Exhibit 4), the index continues to remain soft and ranged between 1.56 to 1.61 the week of 12 Jul (vs 1.63 to 1.65 the week of 5 Jul), vs 2.04 on 31 May. Based on Artificial Analysis, China models are highly cost-efficient vs US models and API cost is a fraction vs US models (Exhibit 3). We look into (1) Blended price vs Intelligence by models (Exhibit 1). The recent industry trends from US /China tech companies show the debate on Tokenmaxxing vs token spending means cost efficient models become increasing important in Coding and Agentic AI.

Video generation model landscape does not see to have notable change. According to Kimi's co-founder Mr. Zhou Xinyu, the current focus is model intelligence and video generation model

Exhibit 1 - Artificial Analysis Intelligence Index vs Blended Price  
![](images/e3443364a7f8785b18ebc7f70894df72f58864e7ae2dd635bb8a19564b4f0e49.jpg)  
Source: Artificial Analysis, JEF

Exhibit 2 - Total parameters for different flagship models

<table><tr><td>Models</td><td>Total parameters</td></tr><tr><td>Kimi-3</td><td>2.8T</td></tr><tr><td>DeepSeek-V4-Pro</td><td>1.6T</td></tr><tr><td>Qwen3.7 Max</td><td>1.2T</td></tr><tr><td>GLM-5.2</td><td>744B</td></tr><tr><td>MiniMax M3</td><td>428B</td></tr><tr><td>Hy3</td><td>295B</td></tr></table>

Source: JEF

Exhibit 3 - Blended prices for China models vs US models (2Q26)  
![](images/7769f3d513defce8f4445ba9e5bf50579552378a74b139d5e44ec0ae815727c2.jpg)  
Source: Artificial Analysis, JEF

Exhibit 4 - Silicon Data LLM Token Expenditure Index  
![](images/96d2e8a289f2d2febe341cfe0b106cd829d22c1b82107f276a2760219c3aa4a6.jpg)  
Source: Bloomberg, JEF

Exhibit 5 - Weekly token consumption over the past 12 months as of 13 Jul (tn)  
![](images/a51f81540523176957807ce7667028460d79eb8b6812905b9ff041f832a6a857.jpg)  
Source: OpenRouter, JEF

Thomas Chong \* | Equity Analyst 852 3743 8016 | thomas.chong@JEF.com

Zoey Zong \* | Equity Analyst 852 3743 8163 | zoey.zong@JEF.com

is not top priority at the moment. According to Volcano Engine Conference (link) in Jun, it released Seedance 2.5 and considers video

Continued overleaf ...

generation represents over half of MaaS revenue (link). On the other hand, Kling raised new financing be used for business expansion, daily operations, working capital, team development and others (link)

Tencent's WorkBuddy is gaining traction. On application side, we expect Tencent's WorkBuddy continues to gain traction. According to Analysys (link), it highlights operating metrics for WorkBuddy in the segment (Mar-26). These include (1) number of desktop monthly visits reached 8.85m; (2) WorkBuddy is ahead of Trae (ByteDance), QClaw (Tencent) and Qoder Work (BABA). On the other hand, BABA releases Meoo (diverse AI enterprise apps) during WAIC. For Baidu, it highlights a number of AI showcases such as Baidu Drive, Baidu Wenku and Xiaodu during WAIC (link). On the other hand, Kingsoft Office held AI Productivity Conference last week and released AI products Lingxi Professional and WPS AI Hub (link)

What's next to be anticipated? These include (1) With model iterations happen in less than 3 months, we expect upcoming models for Qwen (Qwen 3.8, 2.4T), MiniMax (M3 Pro), Zhipu (GLM) and Tencent (Hy4) are to be anticipated. For BABA, it highlights Qwen3.8 is open weight model (total parameters 2.4T) which will be released in near term. Its Qwen3.8-Max-Preview model is available in Token Plan, Qoder and Qoder Work. It is also available in PC and mobile of Qianwen; (2) a number of companies are expected to achieve over USD1bn ARR in 2026 or early 2027: (a) BABA; (b) Zhipu; (c) MiniMax; (d) Kling; (e) Volcano Engine. We expect Kimi ARR is to be watched out post release of K3. We view BABA to stand out on its full stack of capabilities with models, cloud, chips and applications.

## Zhipu: Key Takeaways from Conference Call

\- Scaling Law continues to accelerate. This can be seen in breakthrough made by OpenAI and Anthropic heading towards AGI.

\- Thoughts on K3. (1) K3 is successful in scaling and close to global frontier models; (2) GLM-5.2 has less parameters vs K3 (Exhibit 6). It expects to exceed K3 capabilities when it scales to K3 level

\- GLM series. (1) Feb-26: GLM-5 vs GLM-4 series. It doubles no of parameters with pre-training of 30T tokens and adopts DSA architecture; (2) Apr-26/Jun-26: released GLM5.1/5.2 version. (a) GLM5.1 emphasizes on long horizon tasks; (b) GLM-5.2 extends to 1M context length and handles complicated coding work; (c) next version GLM-5.3 will have minor iterations and better coding experience; (d) next model series will have new architecture with bigger scale while maintain cost efficiencies

\- Multiple areas in scaling. These include (1) data; (2) environment; (3) RL (Reinforcement Learning); (4) Infra. On data, it covers pre-training/mid-training and SWE scaling can automatically create coding agent environment. On RL, the use of SAO technology drives better accuracy vs GRPO optimization in particular long horizon tasks. On Infra, (a) ZCube vs Clos: it lowers cost by 33% and throughout by 15%; (b) LayerSplit: reduce KV Cache and increase throughput by 132%; (c) prefill-decode separation; (d) DSA+IndexShare enhances efficiency

\- Touch High. On top of new models, other areas include (1) LLM-driven autonomous agent system (AAS) and (2) Recursive self-improvement (RSI)

Exhibit 6 - Comparison between GLM-5.2 vs K3

<table><tr><td></td><td>GLM-5.2</td><td>Kimi K3</td></tr><tr><td>Total no of parameters</td><td>744B</td><td>2.8T</td></tr><tr><td>Activated parameters</td><td>40B, 8/256 experts</td><td>16/896 experts</td></tr><tr><td>Training Tokens</td><td>30T+ tokens</td><td>na</td></tr><tr><td>Contexts</td><td>1M: texts</td><td>1M: multimodal</td></tr><tr><td>Core architecture</td><td>DSA + Index Share</td><td>KDA + AttnRes + Stable LatentMoE</td></tr><tr><td>API price (cache/input/output)</td><td>RMB2/8/28 USD0.26/1.4/4.4</td><td>RMB2/20/100 USD0.3/3.0/15.0</td></tr><tr><td>Open source</td><td>Release weights under MIT</td><td>Release open weights on 27 Jul</td></tr><tr><td>Deployment</td><td>8 cards</td><td>64+ supernode</td></tr><tr><td>Speed</td><td>Average 60 TPS High Speed 450 TPS</td><td>Average 20 TPS</td></tr></table>

Source: Company, JEF

Exhibit 7 - Frontend Code Arena: US vs China  
![](images/62f364b5545b1b207a946ef4bf4fa03263438ca271107901f957340263b96096.jpg)  
SOURCE: ARENA WEBDEV AND CODE ARENA PUBLIC HISTORIES  
Source: Arena, JEF

Based on Artificial Analysis, China models DeepSeek, Qwen, Kimi, MiniMax and Zhipu are closing the gap with US models in terms of intelligence. China models are highly cost-efficient on Mixture of Experts (MoE) architecture, linear attention, and MFU (Model Flog Utilization). According to 2026 Stanford AI Index Report (Apr-26), the top US model leads Chinese models by 2.7%. Separately, Anthropic (1503), xAI (1495), Google (1494), OpenAI (1481), Alibaba (1449) and DeepSeek (1424) occupy the top tier of Arena Elo ratings as of Mar-26.

China models are narrowing the gap with US models in terms of intelligence. On Input/Output API, China large models are highly efficient vs US models.

Exhibit 8 - Artificial Analysis Intelligence Index

Artificial Analysis Intelligence Index

Artificial Analysis Intelligence Index v4.1 incorporates 9 evaluations: GDPval-AA v2, $\tau^3$ -Banking, Terminal-Bench v2.1, SciCode, Humanity's Last Exam, GPQA Diamond, CritPt, AA-Omniscience, AA-LCR

Artificial Analysis

![](images/d994646e196b3bd02dd20ea805a0f501f3c78892eced31577233b04268c73369.jpg)  
Reasoning models are indicated by a lightbulb icon  
Source: Artificial Analysis, JEF

Exhibit 9 - Coding Cost Per Task Assessment: K3 vs Global Peers  
Kimi Code Bench V2 · Score vs Cost per Task  
![](images/f96c52ab2011595f59b15defd84c91bce6b076f4eb1237bff33961cd7c1ca302.jpg)  
Source: Moonshot AI, JEF

Exhibit 10 - Browsing Cost Per Task Assessment: K3 vs Global Peers  
![](images/9b72e738335d0cfd9648100c6cc9db54e24a2f2063807bcffbac3768ce7c9269.jpg)  
Source: Moonshot AI, JEF

## Model Input/Output Price By Companies

Exhibit 11 - DeepSeek: Input price  
![](images/c515d6096d8f8e93a0285ea7a755ee5a5a1f9875b30303ad708566d106c954d6.jpg)  
Source: Artificial Analysis, JEF

Exhibit 12 - DeepSeek: Output price  
![](images/cd65b7c097b0713d7a8a3edb969ea2192676e6177f669fa4de44daa38df45676.jpg)  
Exhibit 13 - Kimi: Input price  
Source: Artificial Analysis, JEF

![](images/a68e333ac3bc237a123bd7f47e0f0f404dc3eafc4af90e42eb9a5c18f8642324.jpg)  
Source: Artificial Analysis, JEF

Exhibit 14 - Kimi: Output price  
![](images/69540c9dea9a7e16e40d2e1452197a627d9b459883702c2c3eb87c447c698b8e.jpg)  
Source: Artificial Analysis, JEF

Exhibit 15 - Zhipu: Input price  
![](images/58bde6f29002d0ec32f3bf951f0638f5a87a8ad2e31dfbd8223733523681ecd2.jpg)  
Source: Artificial Analysis, JEF

Note: API price is the same across all context lengths in GLM-5.2 vs tiered pricing in GLM-5.1  
Exhibit 16 - Zhipu: Output price  
![](images/d8f7ca8a36a461719f6aea46033563be098063228a73725a51ca809539e9c6b0.jpg)  
Source: Artificial Analysis, JEF  
Note: API price is the same across all context lengths in GLM-5.2 vs tiered pricing in GLM-5.1

Exhibit 17 - Qwen: Input price  
![](images/12736c3fb1f984b39935ee8cca1d5d726333f2a9312886fa53e779fe1b917aaf.jpg)

![](images/a9edc2babd3be8ca4c343eaf539ab17b8642237aec2b6f788b352715fafdbd87.jpg)  
Source: Artificial Analysis, JEF

Exhibit 18 - Qwen: Output price  
![](images/d2fcbf9869d7dd373e4c7bc58e83dab6cde7fe3703d7dec7395d63f3b2995203.jpg)  
Source: Artificial Analysis, JEF

Exhibit 19 - MiniMax: Input price  
![](images/7b40bae89a8d748d4ea636546f9abd67675cb818447bd0474c71215d615004fc.jpg)  
Source: Artificial Analysis, JEF
Note: > 512k input tokens for MiniMax-M3

Exhibit 20 - MiniMax: Output price  
![](images/dab370f29e8237b2b07522de8f9986128fd0fbf500758b802ace04f0db329db6.jpg)  
Source: Artificial Analysis, JEF  
Note: >512k input tokens for MiniMax-M3

Source: Artificial Analysis, JEF
Note: 32k < Input tokens <= 128k

Exhibit 21 - Doubao Seed: Input price  
![](images/0f04491d7e012464102e4578c6f9ebc98edef3df94b17207aa727cbf4354dd2e.jpg)  
Source: Company, JEF  
Note: 128k < input tokens <= 256k for doubao-seed-2.0-pro, doubao-seed-1.8

Exhibit 22 - Doubao Seed: Output price  
![](images/9cf578740547e561ffb372ef11899a14f668aea82159ca1f46a4bc76eef2a984.jpg)  
Source: Company, JEF  
Note: 128k < input tokens <= 256k for doubao-seed-2.0-pro, doubao-seed-1.8

Exhibit 23 - Xiaomi: Input price  
![](images/785432bae0f6b5581177bd124331187c63b14faf8c80c184bbdeb80c9a62d0cb.jpg)  
Source: Artificial Analysis, JEF

Exhibit 24 - Xiaomi: Output price  
![](images/f6f169ef8a4a305b760988d95225869dbbf6e2d91a733472b983fa09ed032583.jpg)  
Exhibit 25 - Tencent: Input price  
Source: Artificial Analysis, JEF

![](images/ed3d52a1a618c26146d5e68e69f9246160ba98f1f71e6a4b41a90f8e6be7c2ca.jpg)  
Source: Company, JEF

Exhibit 26 - Tencent: Output price  
![](images/dab5eb83834d016f7b70d684460270dbc31b18347f37346c6a93f9849a0ad3f7.jpg)

Exhibit 27 - Baidu: Input price  
![](images/e0160ccfb1d0405f89cab6078cfb45d3e0cec8db0842208088739324d3b36da2.jpg)  
Source: Company, JEF

Exhibit 28 - Baidu: Output price  
![](images/3dd54ac2e14b4f4b1a918d7b08ec1cf96b1c42757e44560a43dcda6fee100a5b.jpg)  
Source: Artificial Analysis, JEF
Note: 32k < Input tokens <= 128k

Exhibit 29 - StepFun: Input price  
![](images/844f574dd212866eae420e1f25d913d27980138fca8f6f6c350b92d2a880676b.jpg)  
Source: Artificial Analysis, JEF

Exhibit 30 - StepFun: Output price  
![](images/24907380e5e8f2477b810046d37922928e756532de82f9a6598bec7879987839.jpg)  
Source: Artificial Analysis, JEF

Exhibit 31 - OpenAI: Input price  
![](images/534b6e7a7a2c857c381d354af44f8fc05ebf457ccd69a18fd7a08d3eedfe97fd.jpg)  
Source: Artificial Analysis, JEF

Exhibit 32 - OpenAI: Output price  
![](images/cf0a05daccf6897d4b60ac3e9d4d65835818aee64e3f28be0468e43720deb887.jpg)  
Source: Artificial Analysis, JEF

Exhibit 33 - Anthropic Claude Opus: Input price  
![](images/6034e230aad14dd99da1a267cf72774c464627db73fdcbc8e3686c3a2bae990d.jpg)  
Source: Artificial Analysis, JEF

Exhibit 34 - Anthropic Claude Opus: Output price  
![](images/2a2c4d0ea541ce278e25fe016f5c1d55741d98144e59e0404ef50468ff85ff04.jpg)  
Source: Artificial Analysis, JEF

Exhibit 35 - Anthropic Claude Sonnet: Input price  
![](images/3c39faf25b26bffe413a2bde095137eea7e51c928a24c4f6ad09e564059472b6.jpg)  
Source: Artificial Analysis, JEF

Exhibit 36 - Anthropic Claude Sonnet: Output price  
![](images/2dfc454dc03c462a9c61450e1b2f94ce68f6fdb46c57cf68cf234df4a4638b6a.jpg)  
Source: Artificial Analysis, JEF

We would like to thank Fiona Fan, employee of Evalueserve Inc., for providing research support services to our preparation of this report. We would like to thank Han Wang, employee of Evalueserve Inc., for providing research support services to our preparation of this report. We would like to thank Erica Qiu, employee of Evalueserve Inc., for providing research support services to our preparation of this report.

## Company Valuation/Risks

For Important Disclosure information on companies recommended in this report, please visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action or call 212.284.2300.

## Analyst Certification:

I, Thomas Chong, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

I, Zoey Zong, certify that all of the views expressed in this research report accurately reflect my personal views about the subject security(ies) and subject company(ies). I also certify that no part of my compensation was, is, or will be, directly or indirectly, related to the specific recommendations or views expressed in this research report.

Registration of non-US analysts: Thomas Chong is employed by JEF Hong Kong Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst.

Registration of non-US analysts: Zoey Zong is employed by JEF Hong Kong Limited, a non-US affiliate of JEF LLC and is not registered/qualified as a research analyst with FINRA. This analyst(s) may not be an associated person of JEF LLC, a FINRA member firm, and therefore may not be subject to the FINRA Rule 2241 and restrictions on communications with a subject company, public appearances and trading securities held by a research analyst. As is the case with all JEF employees, the analyst(s) responsible for the coverage of the financial instruments discussed in this report receives compensation based in part on the overall performance of the firm, including investment banking income. We seek to update our research as appropriate, but various regulations may prevent us from doing so. Aside from certain industry reports published on a periodic basis, the large majority of reports are published at irregular intervals as appropriate in the analyst's judgement.

## Investment Recommendation Record

## (Article 3(1)e and

[中间内容因长度限制已省略]

ular investment objectives, portfolio holdings, strategy, financial situation, or needs of any recipient. As such, any advice or recommendation in this report may not be suitable for a particular recipient. JEF assumes recipients of this report are capable of evaluating the information contained herein and of exercising independent judgment. A recipient of this report should not make any investment decision without first considering whether any advice or recommendation in this report is suitable for the recipient based on the recipient's particular circumstances and, if appropriate or otherwise needed, seeking professional advice, including tax advice. JEF does not perform any suitability or other analysis to check whether an investment decision made by the recipient based on this report is consistent with a recipient's investment objectives, portfolio holdings, strategy, financial situation, or needs.

By providing this report, neither JRS nor any other JEF entity accepts any authority, discretion, or control over the management of the recipient's assets. Any action taken by the recipient of this report, based on the information in the report, is at the recipient's sole judgment and risk. The recipient must perform his or her own independent review of any prospective investment. If the recipient uses the services of JEF LLC (or other affiliated broker-dealers), in connection with a purchase or sale of a security that is a subject of these materials, such broker-dealer may act as principal for its own accounts or as agent for another person. Only JRS is registered with the SEC as an investment adviser; and therefore neither JEF LLC nor any other JEF affiliate has any fiduciary duty in connection with distribution of these reports.

The price and value of the investments referred to herein and the income from them may fluctuate. Past performance is not a guide to future performance, future returns are not guaranteed, and a loss of original capital may occur. Fluctuations in exchange rates could have adverse effects on the value or price of, or income derived from, certain investments.

This report may contain forward looking statements that may be affected by inaccurate assumptions or by known or unknown risks, uncertainties, and other important factors. As a result, the actual results, events, performance or achievements of the financial product may be materially different from those expressed or implied in such statements.

This report has been prepared independently of any issuer of securities mentioned herein and not as agent of any issuer of securities. No Equity Research personnel have authority whatsoever to make any representations or warranty on behalf of the issuer(s). Any comments or statements made herein are those of the JEF entity producing this report and may differ from the views of other JEF entities.

This report may contain information obtained from third parties, including ratings from credit ratings agencies such as Standard & Poor's, and information derived from third-party or proprietary generative artificial intelligence (Gen AI) models. JEF does not guarantee the accuracy, completeness, timeliness or availability of this information, and is not responsible for any errors or omissions (negligent or otherwise), regardless of the cause, or for the results obtained from the use of such content. Neither JEF nor any third-party content providers, including providers of Gen AI models, give any express or implied warranties, including, but not limited to, any warranties of merchantability or fitness for a particular purpose or use. Neither JEF nor any third-party content provider shall be liable for any direct, indirect, incidental, exemplary, compensatory, punitive, special or consequential damages, costs, expenses, legal fees, or losses (including lost income or profits and opportunity costs) in connection with any use of their content, including ratings. Credit ratings are statements of opinions and are not statements of fact or recommendations to purchase, hold or sell securities. They do not address the suitability of securities or the suitability of securities for investment purposes, and should not be relied on as investment advice. Reproduction and distribution of third party content in any form is prohibited except with the prior written permission of the related third party.

JEF reports are disseminated and available electronically, and, in some cases, also in printed form. Electronic research is simultaneously made available to all clients. This report or any portion hereof may not be copied, reprinted, sold, or redistributed or disclosed by the recipient or any third party, by content scraping or extraction, automated processing, or any other form or means, without the prior written consent of JEF. Any unauthorized use is prohibited. Neither JEF nor any of its respective directors, officers or employees, is responsible for guaranteeing the financial success of any investment, or accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this report or its contents. Nothing herein shall be construed to waive any liability JEF has under applicable U.S. federal or state securities laws.

For Important Disclosure information relating to JRS, please see https://adviserinfo.sec.gov/IAPD/Content/Common/crd\_iapd\_Brochure.aspx?BRCHR\_VRSN\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://avatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.

© 2026 JEF
"""
