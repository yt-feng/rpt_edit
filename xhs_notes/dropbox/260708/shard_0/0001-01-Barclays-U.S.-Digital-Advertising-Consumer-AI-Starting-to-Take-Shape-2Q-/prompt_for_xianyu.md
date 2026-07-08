你是闲鱼资料类商品文案编辑，擅长把一份投研/行业/公司研报改写成适合闲鱼发布的商品说明。

【目标】
- 基于下面研报解析内容，生成一份可以复制到闲鱼商品详情里的中文文案。
- 风格参考用户提供的闲鱼对标笔记：标题直给、信息密度高、用途明确、适合人群明确、交付方式清楚。
- 语言要自然，像真实卖家发布，不要像公众号文章、小红书笔记或 AI 摘要。
- 不要使用太夸张的营销词，不要承诺收益，不要说“稳赚”“内幕”“必涨”。
- 可以适度口语化，但不要低俗。
- 硬性要求：全文不要使用任何 emoji 或符号表情。
- 硬性要求：全文必须低于 1500 字，宁可少写，也不要超长。

【必须输出结构】
1. `闲鱼标题：` 一行，控制在 30 字以内，适合商品标题。
2. `商品描述：` 正文，适合直接粘贴到闲鱼详情页。
3. `Hashtag：` 一行，给 6-10 个平台可用标签，用 `#` 开头，空格分隔。

【长度硬性要求】
- 输出总字数必须低于 1500 字，包括标题、商品描述、Hashtag。
- 商品描述控制在 900-1200 字以内，避免写成长文。
- 亮点 bullet 每条控制在 30 字以内。

【严禁输出】
- 不要输出 `建议价格：`。
- 不要输出 `搜索关键词：`。
- 不要输出“搜索词”“关键词”“搜索关键词”等栏目。
- 不要给具体价格区间、成交承诺或价格建议。
- 不要使用任何 emoji，例如 ✅、🔥、📌、👉、💰、⭐ 等。

【商品描述写法】
- 第一段：直接说明这是什么报告，页数/语言/主题/公司或行业。如果页数、日期、语言不确定，就不要编。
- 第二段：说明适合谁，比如投研、券商面试、PE/VC、行业研究、学习参考、写报告等。
- 第三段：用 3-5 个亮点 bullet，风格参考：
  - 三大情景框架：DCF、P/ARR、EV/Sales
  - 关键变量分析
  - 估值逻辑、假设、终值占比等核心内容覆盖
  - 适合准备 AI 相关面试、研究 AI 估值的同学
- 第四段：交付说明，参考：`资料为电子版 PDF，拍下后 24 小时内发网盘链接或邮箱。`
- 第五段：虚拟商品说明，参考：`电子类资料一经发货不退不换，有问题可以提前咨询。`
- 可以补一句：`需要其他报告也可以私聊，支持一站式咨询。`

【Hashtag 写法】
- 只输出平台相对安全、偏学习和资料属性的标签。
- 推荐从这些里选择：`#学习资料` `#研究笔记` `#学习笔记` `#行业研究` `#研报资料` `#资料整理` `#报告学习` `#案例研究`。
- 不要输出 `#财经` `#投资` `#股票` `#基金` `#理财` `#暴富` `#内幕` 等敏感标签。

【平台发布合规要求】
- 不要出现“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要保持中性。
- 不要出现“独家”“原版”“内部”“无水印”“全网最低”“最全”“最强”“必看”等高风险或极限词。
- 不要写“关注”“点赞”“求关注”“评论区留言”等直接互动诱导。
- 不要承诺资料一定可用于获利、就业、通过面试或获得收益。

【合规与避坑】
- 默认避免出现具体投行品牌名，比如“GS”“GS”“MS”，统一写作“投行研报”或“投行研报”。
- 不要承诺研究或交易结果。
- 不要伪造页数、日期、作者、公司覆盖范围。研报未给出时就不写。
- 不要输出解释说明，只输出闲鱼文案本身。

【研报解析内容】
"""
U.S. Digital Advertising

# Consumer AI Starting to Take Shape - 2Q Preview

We like GOOGL, META and PINS into the print. We expect a solid quarter from the digital advertising group in 2Q, with key revenue growth rates broadly in line to above the Street. Trends should slow through '26 but already factored into consensus expectations.

The Key Takeaway: Stock prices across the digital advertising sector have been reacting more to AI trends and winner/loser baskets of late, rather than core financial results. GOOGL is benefiting mostly from GCP growth (and in 2Q likely the TPUaaS business) rather than Search revenue growth rates. META remains in the sentiment doghouse, and we think the company could surprise on AI in 2H (both models and products) while ad revenue growth should remain steady. PINS is likely to get things back on track in 2Q (see below) and arguably has the best setup in the group heading into late '26 as core ads start to outperform. SNAP has been volatile around the Specs launch, but its ad business seems to be improving a bit in 2Q. This is all playing out as consumer AI seems on the verge of its next major push since ChatGPT's original debut. Native AI advertising remains nascent and isn't likely to have an impact on the group in 2Q. In summary, the backdrop remains broadly constructive for digital advertising: 1) fears around AI disruption risk seem a bit overblown, and 2) most names are currently trading at a discount to the S&P 500.

Most Ad Categories Tracking Solidly in 2Q: Retail represents upwards of 20-25% of ad spend for larger walled gardens, and up to 85%+ for companies like Pinterest. With the combination of late-quarter promotions falling in 2Q this year (Prime Day, etc.) and some tariff refunds coming through to various brands and retailers being redeployed into customer acquisition, we think trends were broadly stable. Travel seemed to have picked up a bit as Middle East tensions eased and one-off events like World Cup helped demand. AI-native apps are being created and launched at a rapid pace, and often come with heavy direct response ad buys to increase awareness. Lastly, prediction market apps have hit product market fit in 2026 and seem to be leaning into digital marketing, which could result in billions of ad dollars for the largest ecosystems.

# Consumer AI on the Verge of Its Agentic Moment - Siri AI Could Restart the Consumer Race

The Siri AI debut at WWDC looked impressive from the standpoint of being the first "safe and normie" consumer AI app that defaults connectors across Apple's suite of O+O applications into

BARC Capital Inc. and/or one of its affiliates does and seeks to do business with companies covered in its research reports. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of this report. Investors should consider this report as only a single factor in making their investment decision.

Please see analyst certifications and important disclosures beginning on page 5.
Completed: 06-Jul-26, 21:17 GMT Released: 07-Jul-26, 04:10 GMT Restricted - External

U.S. Internet
POSITIVE

U.S. Internet
Ross Sandler
+1 415 263 4470
ross.sandler@BARC.com
BCI, US

Alex Hughes
+1 212 526 3069
alexander.hughes@BARC.com
BCI, US

Michael DiSanto
+1 212 526 1054
michael.disanto@BARC.com
BCI, US

Owen Clendenin
+1 212 526 7518
owen.clendenin@BARC.com
BCI, US

Alexander Kessinger
+1 212 526 1324
alexander.kessinger@BARC.com
BCI, US

the service for personalization. Gemini and ChatGPT have developer SDKs and plug-ins, but on a consumer opt-in basis they aren't in the same trusted position as Apple, nor do they sit at the OS/device levels. This kind of personalized service with connectors is likely to be what will push the consumer AI space into its next stage, much like how ChatGPT's original debut triggered chatbot adoption. Often a precursor to the West, we are seeing this trend already happening in China – WeChat is integrating its 4m mini-programs into its AI service, allowing consumers to take action, not just chat.

Apple went further out of its way to show off how the orchestration and routing layers of their new AI stack are largely built in-house (in some cases distilled from Gemini) and are not sending queries to other AI models, outside of a few complex tasks. This release was impressive in our view from the standpoint of abstracting away some of the complicated set-up steps for personalized consumer AI, allowing the user to take action, not just chat, and giving Apple much more control of the user interaction layer on the iPhone.

FIGURE 1. Apple Looks to Control Much More of the AI Experience (and the User Interaction Layer) with Siri AI  
![](images/313003a810849068d5591fe6de58e006e174d1fd6b42fa7beb72a09ea119c2e6.jpg)  
Source: BARC, Company Disclosures

Like WeChat, Apple is attempting to control most of the transactions between the user and third-party applications like DoorDash and Instacart via the App Intent API. In 2Q, ByteDance introduced paid tiers to its popular consumer AI service Doubao ranging from \$10-\$70 per month, comparable to ChatGPT (\~5% payers), so we are likely to see other examples of consumer agent business models take form. All of this is to say that if Siri AI gains traction after being rolled out this fall, we believe it could direct some transactions away from existing channels and into Apple-controlled services.

Noted above, other consumer AI services are building the same capabilities, including Google's Gemini, Meta AI and ChatGPT via various third-party app integrations. To the degree that this kind of interaction between consumer agentic AI services and third-party apps takes off, it could shift ad dollars out of Search and Social, or could potentially be deflationary to overall digital advertising (but still TBD, depending on adoption).

## ChatGPT Ads Still Tiny, But Growing Fast

Somewhat related to consumer agentic AI adoption, we are monitoring how native AI advertising within these new surfaces is progressing. We aren't yet concerned around chatbot ads taking share from the legacy digital channels. There appears to be some anecdotal examples of companies/agencies cutting back on digital to fund chatbot ads, but in our view this is unlikely to be an issue in 2Q. We estimate AI ads could hit a \$1B quarterly run rate by 4Q26, at which point the industry may have to start taking notice. Until then, trends and market share in core digital should remain largely as is.

FIGURE 2. ChatGPT Ads Could Reach \$1B Per Quarter By 4Q26  
![](images/f14626eb1841865058c5351ecdf979ad2a696955cd726ed342e6b7f69437435b.jpg)  
Source: BARC, The Information, Company Disclosures

## Company-Specific 2Q Previews

GOOGL: Checks remain solid in 2Q, and we are expecting similar growth in 2Q (ex-fx) for Google's ad businesses. We estimate Search revenue growth of 16% Y/Y (15% ex-fx) in 2Q, which seems appropriate based on the set-up. Query growth has picked up from AI Overviews and AI Mode adoption, including the higher "refresh" rate on some of these queries. The reduction in organic traffic referrals continues to force brands to allocate more to paid search in order to grow. At the same time the company is starting to experiment with native AI ads in some of these new surfaces. We expect queries to remain elevated and paid click-through rates (CTR) to pick up potentially over the next year, but not likely by enough to drive above-industry growth in Search revenue. We expect YouTube +10% Y/Y in 2Q with some small help from the World Cup campaigns on the brand side, but ad growth continues to lag on the mix shift towards ad-free subscriptions. GCP should once again be the standout based on a combination of factors: Anthropic (private) and the overall inference side of GCP inflecting higher. We expect Google Cloud to grow well north of last quarter's 63% Y/Y as agentic enterprise AI appears to have really hit its stride in 2Q. EPS likely benefits once again from below-the-line gains in non-marketable securities from recent IPOs.

META: Advances in META's ad stack continue to drive subtle but important improvements in revenue trajectory. Engagement per user is up across IG and Blue based on content recommendations. Ad load is also going up dynamically, while ad targeting continues to

improve. The company introduced its Adaptive Ranking Model in 4Q25 and has rolled it out more broadly since, and we think 2Q trends may have benefited to some degree. Some of the historical model tweaks have been subtle in terms of revenue impact, but this one seems more significant and could be more meaningful over time. We are modeling \$59B in ad revenue (+25% ex-fx) which could prove conservative by a point or two. We aren't expecting any major surprises on the Capex or Opex outlooks in 2Q. We doubt the debate around equity financing needs or cloud tokens-as-a-service will be fully put to bed until the next Muse models are released, but we would use the recent volatility to add to positions.

PINS: As noted above, our checks suggest retail had a solid 2Q with late-quarter promotions helping a bit. We hosted an NDR for PINS management in early June and the tone was broadly upbeat. Direct response may see some improvement from tariff relief, and the company expressed excitement about what they expect TVScientific will bring to the table. Search ads for 3P-CTV is a nascent opportunity that only Amazon, and now PINS, are really pursuing at this point. Small advertiser spend should continue to outpace the larger accounts on PINS, on the back of Performance+. We expect some headwinds to Europe from the sales reorg, but that's well documented and we believe is already reflected in consensus. 2Q and the outlook for 2H could see slight upside for PINS vs our estimates; we are modeling revenue of \$1.15b (+15% Y/Y).

SNAP: We are hopeful that SNAP could get things back on track in 2Q. The company is lapping some company-specific snafus in direct response, in addition to the tariff-related cuts last year, both of which should see solid improvement. We expect core ad growth to pick up from 3% in 1Q to somewhere in the mid-single-digits in 2Q. Sponsored Snaps remains the new product most in favor for Snapchat, with increased focus on brands leveraging smaller groups and private conversations vs. the traditional social media ad buys. SNAP's brand advertising has been declining for a few quarters, so we would view any new signs of life as a positive. The Specs launch was met with new investor skepticism, but we note that the company packed a lot of technology into the form factor (comparable to a META Orion prototype) and can always slim things down in consumer v2 (which could already be in development). The company does have a nice lead in AR technology and the ecosystem around lens studio which it can leverage. The activist campaign seems to have come and gone without much impact, which may explain some of the weakness in shares since the Specs launch. Specs de-consolidation remains an option for Snap.

LFTO: We just initiated coverage of Liftoff, so for more detail on our thesis refer to Performance Rules Everything Around Me, 6/29/26. 2Q should have upside to the 28% Y/Y growth forecasted by consensus as the company continues to benefit from internal model updates that drive share gains within gaming and rapid growth in new categories like retail and prediction markets. 1Q had a successful model update, hence the company stated it doesn't expect the same level of growth in 2Q (FX was also a smaller tailwind).

## Analyst(s) Certification(s):

I, Ross Sandler, hereby certify (1) that the views expressed in this research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this research report and (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this research report.

## Important Disclosures:

BARC is produced by the Investment Bank of BARC Bank PLC and its affiliates (collectively and each individually, "BARC"). All authors contributing to this research report are Research Analysts unless otherwise indicated. The publication date at the top of the report reflects the local time where the report was produced and may differ from the release date provided in GMT.

## Availability of Disclosures:

Where any companies are the subject of this research report, for current important disclosures regarding those companies please refer to https://publicresearch.BARC.com or alternatively send a written request to: BARC Compliance, 745 Seventh Avenue, 13th Floor, New York, NY 10019 or call +1-212-526-1072.

The analysts responsible for preparing this research report have received compensation based upon various factors including the firm's total revenues, a portion of which is generated by investment banking activities, the profitability and revenues of the Markets business and the potential interest of the firm's investing clients in research with respect to the asset class covered by the analyst.

Research analysts employed outside the US by affiliates of BARC Capital Inc. are not registered/qualified as research analysts with FINRA. Such non-US research analysts may not be associated persons of BARC Capital Inc., which is a FINRA member, and therefore may not be subject to FINRA Rule 2241 restrictions on communications with a subject company, public appearances and trading securities held by a research analyst's account.

Analysts regularly conduct site visits to view the material operations of covered companies, but BARC policy prohibits them from accepting payment or reimbursement by any covered company of their travel expenses for such visits.

BARC Department produces various types of research including, but not limited to, fundamental analysis, equity-linked analysis,

quantitative analysis, and trade ideas. Recommendations contained in one type of BARC may differ from those contained in other types of BARC, whether as a result of differing time horizons, methodologies, or otherwise.

In order to access BARC Statement regarding Research Dissemination Policies and Procedures, please refer to https:// publicresearch.BARC.com/S/RD.htm. In order to access BARC Conflict Management Policy Statement, please refer to: https://publicresearch.BARC.com/S/CM.htm.

Materially Mentioned Stocks (Ticker, Date, Price)

Alphabet Inc. (GOOGL, 02-Jul-2026, USD 359.91), Overweight/Positive, A/CD/CE/D/E/J/K/L/M/N

Liftoff Mobile, Inc. (LFTO, 02-Jul-2026, USD 24.46), Overweight/Positive, A/CE/D/E/J/L

Meta Platforms, Inc. (META, 02-Jul-2026, USD 582.90), Overweight/Positive, CD/CE/J/K/M/N

Pinterest, Inc. (PINS, 02-Jul-2026, USD 22.07), Equal Weight/Positive, CE/D/J/L

Snap, Inc (SNAP, 02-Jul-2026, USD 4.84), Overweight/Positive, CD/CE/J/K/N

Unless otherwise indicated, prices are sourced from Bloomberg and reflect the closing price in the relevant trading market, which may not be the last available closing price at the time of publication.

## Disclosure Legend:

A: BARC Bank PLC and/or an affiliate has been lead manager or co-lead manager of a publicly disclosed offer of securities of the issuer in the previous 12 months.

B: An employee or non-executive director of BARC PLC is a director of this issuer.

CD: BARC Bank PLC and/or an affiliate is a market-maker in debt securities issued by this issuer.

CE: BARC Bank PLC and/or an affiliate is a market-maker in equity securities issued by this issuer.

CH: BARC Bank PLC and/or its group companies makes, or will make, a market in the securities (as defined under paragraph 16.2 (k) of the HK SFC Code of Conduct) in respect of this issuer.

D: BARC Bank PLC and/or an affil

[中间内容因长度限制已省略]

 and accordingly should not be construed as such. Furthermore, this information is being made available on the basis that the recipient acknowledges and understands that the entities and securities to which it may relate have not been approved, licensed by or registered with the UAE Central Bank, the Dubai Financial Services Authority or any other relevant licensing authority or governmental agency in the UAE. The content of this report has not been approved by or filed with the UAE Central Bank or Dubai Financial Services Authority. BARC Bank PLC in the Qatar Financial Centre (Registered No. 00018) is authorised by the Qatar Financial Centre Regulatory Authority (QFCRA). BARC Bank PLC-QFC Branch may only undertake the regulated activities that fall within the scope of its existing QFCRA licence. Principal place of business in Qatar: Qatar Financial Centre, Office 1002, 10th Floor, QFC Tower, Diplomatic Area, West Bay, PO Box 15891, Doha, Qatar. Related financial products or services are only available to Business Customers as defined by the Qatar Financial Centre Regulatory Authority.

Russia: This material is not intended for investors who are not Qualified Investors according to the laws of the Russian Federation as it might contain information about or description of the features of financial instruments not admitted for public offering and/or circulation in the Russian Federation and thus not eligible for non-Qualified Investors. If you are not a Qualified Investor according to the laws of the Russian Federation, please dispose of any copy of this material in your possession.

Sustainable Investing Related Research: There is currently no globally accepted framework or definition (legal, regulatory or otherwise) of, nor market consensus as to what constitutes a ‘sustainable’, ‘ESG’, ‘green’, ‘climate-friendly’ or an equivalent company, investment, strategy or consideration or what precise attributes are required to be eligible to be categorised by such terms. This means there are different ways to evaluate a company or an investment and so different values may be placed on certain sustainability credentials as well as adverse ESG-related impacts of companies and ESG controversies. The evolving nature of sustainable investing considerations, models and methodologies means it can be challenging to definitively and universally classify a company or investment under a sustainable investing label and there may be areas where such companies and investments could improve or where adverse ESG-related impacts or ESG controversies exist. The evolving nature of sustainable finance related regulations and the development of jurisdiction-specific regulatory criteria also means that there is likely to be a degree of divergence as to the interpretation of such terms in the market. We expect industry guidance, market practice, and regulations in this field to continue to evolve.

Any information, data, image, or other content including from a third party source contained, referred to herein or used for whatsoever purpose by BARC or a third party (“Information”), in relation to any actual or potential ‘ESG’, ‘sustainable’ or equivalent objective, issue, factor or consideration is not intended to be relied upon for ESG or sustainability classification, regulatory regime or industry initiative purposes (“ESG Regimes”), unless otherwise stated. Nothing in these materials, including any images included therein, is intended to convey, suggest or indicate that BARC considers or represents any product, service, person or body mentioned in these materials as meeting or qualifying for any ESG or sustainability classification, label or similar standards that may exist under ESG Regimes. BARC has not conducted any assessment of compliance with ESG Regimes. Parties are reminded to make their own assessments for these purposes.

IRS Circular 230 Prepared Materials Disclaimer: BARC does not provide tax advice and nothing contained herein should be construed to be tax advice. Please be advised that any discussion of U.S. tax matters contained herein (including any attachments) (i) is not intended or written to be used, and cannot be used, by you for the purpose of avoiding U.S. tax-related penalties; and (ii) was written to support the promotion or marketing of the transactions or other matters addressed herein. Accordingly, you should seek advice based on your particular circumstances from an independent tax advisor.

© Copyright BARC Bank PLC (2026). All rights reserved. No part of this publication may be reproduced or redistributed in any manner without the prior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request.
"""
