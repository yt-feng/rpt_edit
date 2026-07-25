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
July 23, 2026 04:01 AM GMT

Software | North America

# Cyber Thoughts on Hugging Face Security Incident

Detection and mitigation of Hugging Face's security breach this week took place largely by utilizing other LLMs / internal tools. The sophistication of the attack, and seeming lack of traditional cyber tools being used, has caused investors to question impact to traditional cyber vendors.

## Key Takeaways

Hugging Face reported a highly sophisticated attack last week, carried out by an autonomous agent of an advanced LLM.

Their anomaly-detection pipeline utilized LLM-based triage over security telemetry vs noting usage of a SIEM/XDR, which would normally be used by enterprises.

SIEM/XDRs designed to detect the very type of attacks we saw, however, need to be well tuned and modernized to detect advanced behaviors in a timely fashion.

Leaves us positive on vendors with most modern solutions, namely CRWD / PANW / ESTC.

Does the SIEM adapt to next-generation attacks? As we highlighted in our deep dive into the SIEM market last month, the security information and event management (SIEM) and extended detection and response (XDR) market today is the traditional line of defense in helping security operations centers (SOCs) detect and remediate attacks. In a breach such as the one that Hugging Face (private) reported last week, a SIEM, receiving logs from identity, cloud, endpoints, network devices, and application infrastructure, could have generated alerts on: use of stolen credentials, privilege escalation, access to sensitive repositories, lateral movement, data exfiltration, large number of API calls, frequency of actions from ephemeral compute. It would need to be a more mature and well-tuned SIEM that would have needed a solid behavioral baseline, particularly to detect the actions from the ephemeral compute so quickly. The speed of detection, particularly to as sophisticated an attack, necessitates more advanced alerting and certainly the collection of a fuller set of logs (SIEM+XDR+SOAR can improve mean time to remediation by 96%). While we see some customers deploying advanced analytics such as we saw from Hugging Face, we would expect most to still rely on the logs / alerts / baselining of their SIEM, though they would increasingly turn to the most next-gen vendors. Given the advanced data signal collection from security vendors, we still see them as best positioned (CRWD/PANW/ESTC highlighted in our note as having screened best in customer / VAR conversations).

What happened? The breach, as reported by Hugging Face on July 16th, originated in their data processing pipeline, which ingests raw data from multiple data sources,

MS & CO. LLC

Meta A Marshall

Equity Analyst
Meta.Marshall@morganstanley.com +1 212 761-0430

Jonathan.Eisenson@morganstanley.com +1 212 761-2808

Lucas.Cerisola@morganstanley.com +1 212 761-9194

## SOFTWARE

Industry View Attractive transforms it and then loads it into a data store such as a data lake or data warehouse for analysis and operational use. The autonomous agent introduced a malicious dataset that exploited two separate vulnerabilities: a first, which let the attacker run arbitrary code simply by having it loaded as a dataset, and a second, that let them inject commands through a template system that was never meant to execute external instructions. From there, the autonomous agent escalated its own privileges, harvested stored credentials, and moved laterally across internal clusters. It did all of this through a self-migrating mechanism running inside ephemeral sandboxes, a compute environment that is created on-demand, used for a specific task (such as running untested AI code or previewing a pull request), and completely destroyed immediately afterward. The breach was detected through Hugging Face's anomaly detection pipeline, utilizing LLM-based triage over security telemetry (essentially what a SIEM does). "To understand what a swarm of tens of thousands of automated actions did, we ran LLM-driven analysis agents over the full attacker action log, comprised of more than 17,000 recorded events. This allowed us to reconstruct the timeline, extract indicators of compromise, map the credentials touched, and separate genuine impact from decoy activity," Hugging Face said in a statement. The LLM-based triage was based on an open-weight model vs. a frontier model or traditional security vendor SIEM.

## What type of other cyber tools could have helped detect the breach? A

traditional SIEM that is used primarily for log detection could see static rules bypassed, have novel attacks not match previous signatures and without behavioral analytics, wouldn't necessarily pick up on the low-level events the ephermeral compute carried out. As we highlighted in our piece, the addition of XDR and SOAR would help with bringing detection more into real time, with UEBA (User & Entity Behavior Analytics), Cloud Detection & Response (CDR) and Identity Threat Detection and Response (ITDR) helping as well.

Elastic NV is covered by Sanjit Singh

Exhibit 1: Traditional SIEM Alone Not Enough For Newer Sophisticated Attacks, but Combination of Tools Leads To Significantly Higher MTTR  
![](images/05848f05ff12bb79bbfcae6feabc8b1cffdabf68c2c8fdc87199b825a3f9d481.jpg)  
Source: Medium.

Exhibit 2: Modern SOC Architecture Combines Detection Engine with Response  
![](images/c2a3af6ea76a08261d07a55f47827ba2aa1b6643c8cf62f41b597aab1ec25449.jpg)  
Source: Medium.

Exhibit 3: Customers Need to Evolve Their SIEM Architectures Towards XDR +SOAR  
![](images/d05169c54c6cc2d86875bc289a6f86791b3d2934c9eb01f408f46a6675a54ca3.jpg)  
Source: MS.

## Valuation Methodology and Risks

## CrowdStrike Holdings Inc (CRWD.O)

Our \$227 PT is based on 60X CY30e FCF of \$5.21B, discounted back at 12%. This multiple implies \~33X EV/CY27 Sales, a premium to Large Cap SaaS/Security peers.

## Risks to Upside

■ Stronger than expected endpoint security demand remains elevated due to rising cyber threats

■ TAM expansion opportunities (XDR, Identity, Cloud Workload Protection) materialize faster than expected

## Risks to Downside

■ Competition makes new customer acquisition tougher

■ Lower cost alternatives commoditize CRWD's premium pricing

■ Softer hiring environment pressures upsell activity

## Elastic NV (ESTC.N)

We arrive at our \$66 price target by applying a \~13x multiple (0.51x growth-adjusted) to our CY28 FCF/shr estimate of \$5.09. This implies 3.0x EV/CY27 Sales or 0.20x growth-adjusted, which reflects a discount to the DevOps peer median of 4.8x/0.44x.

## Risks to Upside

■ Elastic drives faster than expected use case expansion in Security and Observability

■ The \~5% GenAI tailwind materializes, accelerating sales-led subscription growth

■ Adoption of Elastic Cloud grows at a faster rate

## Risks to Downside

■ Competition intensifies across observability, SIEM and hyperscalers

■ Internal disruption from sales changes or management departures

■ New search paradigms arrive through GenAI

## Palo Alto Networks Inc (PANW.O)

Based on 52x Base Case 2028e FCF per share of \$7.05; this multiple is a premium to similarly growing large cap software peers.

## Risks to Upside

■ Stronger firewall refresh cycle and higher subscription attach rates

■ Faster uptake of new Cloud-based Next-Gen Security solutions such as Cortex (AI-Powered Security Analytics) and Prisma SASE

## Risks to Downside

■ Slowing firewall refreshes could drive a greater than expected impact to PANW's top line growth

■ An increasingly competitive environment could necessitate additional S&M spending,

limiting margin leverage.

## Disclosure Section

The information and opinions in MS were prepared by MS & Co. LLC, and/or MS C.T.V.M. S.A., and/or MS Mexico, Casa de Bolsa, S.A. de C.V., and/or MS Canada Limited. As used in this disclosure section, "MS" includes MS & Co. LLC, MS C.T.V.M. S.A., MS Mexico, Casa de Bolsa, S.A. de C.V., MS Canada Limited and their affiliates as necessary.

For important disclosures, stock price charts and equity rating histories regarding companies that are the subject of this report, please see the MS Disclosure Website at www.morganstanley.com/eqr/disclosures/webapp/generalresearch, or contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY, 10036 USA.

For valuation methodology and risks associated with any recommendation, rating or price target referenced in this research report, please contact the Client Support Team as follows: US/Canada +1 800 303-2495; Hong Kong +852 2848-5999; Latin America +1 718 754-5444 (U.S.); London +44 (0)20-7425-8169; Singapore +65 6834-6860; Sydney +61 (0)2-9770-1505; Tokyo +81 (0)3-6836-9000. Alternatively you may contact your investment representative or MS at 1585 Broadway, (Attention: Research Management), New York, NY 10036 USA.

## Analyst Certification

The following analysts hereby certify that their views about the companies and their securities discussed in this report are accurately expressed and that they have not received and will not receive direct or indirect compensation in exchange for expressing specific recommendations or views in this report: Meta A Marshall.

## Global Research Conflict Management Policy

MS has been published in accordance with our conflict management policy, which is available at www.morganstanley.com/institutional/research/conflictpolicies. A Portuguese version of the policy can be found at www.morganstanley.com.br

## Important Regulatory Disclosures on Subject Companies

The analyst or strategist (or a household member) identified below owns the following securities (or related derivatives): Lucas Cerisola - Palo Alto Networks Inc(common or preferred stock); Jonathan Eisenson - Adobe Inc.(common or preferred stock), Sprout Social Inc(common or preferred stock); Meta A Marshall - Adobe Inc.(common or preferred stock), Intuit(common or preferred stock), Microsoft(common or preferred stock), Oracle Corporation(common or preferred stock), Palo Alto Networks Inc(common or preferred stock), Salesforce, Inc.(common or preferred stock).

As of June 30, 2026, MS beneficially owned 1% or more of a class of common equity securities of the following companies covered in MS: Adobe Inc., Akamai Technologies, Inc., Amplitude Inc., Appian Corp, Asana Inc, Atlassian Corporation PLC, Autodesk, BILL Holdings Inc, Blackline Inc, Box Inc, C3.ai, CCC Intelligent Solutions Holdings Inc, Check Point Software Technologies Ltd., Cloudflare Inc, CoreWeave, CrowdStrike Holdings Inc, Datadog, Inc., Descartes Systems Group Inc, DocuSign Inc, Elastic NV, Figma Inc, Five9 Inc, Fortinet Inc., Freshworks Inc, Gen Digital Inc., GitLab Inc, GoDaddy Inc, HubSpot, Inc., Intuit, Klaviyo, Inc, LegalZoom.com Inc, Lightspeed Commerce Inc., Liveramp Holdings Inc, Manhattan Associates Inc., Microsoft, monday.com Ltd, MongoDB Inc, Nebius Group NV, NICE Ltd., Okta, Inc., Oracle Corporation, PagerDuty, Inc., Palantir Technologies Inc., Palo Alto Networks Inc, Qualys Inc, Rapid7 Inc, RingCentral Inc, Sabre Corp, Salesforce, Inc., Samsara Inc, SentinelOne, Inc., ServiceNow Inc, ServiceTitan Inc, Shopify Inc, Snowflake Inc., Sprinklr Inc, Sprout Social Inc, SPS Commerce Inc, Tenable Holdings Inc, Toast, Inc., Twilio Inc, UiPath Inc, Vertex Inc., Wix.Com Ltd, Workday Inc, Zeta Global Holdings Corp, ZoomInfo Technologies Inc.

Within the last 12 months, MS managed or co-managed a public offering (or 144A offering) of securities of Akamai Technologies, Inc., Check Point Software Technologies Ltd., CoreWeave, DigitalOcean Holdings Inc, Figma Inc, Intuit, Navan Inc, Nebius Group NV, Netskope, Inc., Salesforce, Inc., ServiceNow Inc, Via Transportation Inc, Wix.Com Ltd.

Within the last 12 months, MS has received compensation for investment banking services from Akamai Technologies, Inc., Autodesk, Blackline Inc, CCC Intelligent Solutions Holdings Inc, Check Point Software Technologies Ltd., CoreWeave, DigitalOcean Holdings Inc, Figma Inc, HubSpot, Inc., Intuit, Microsoft, Navan Inc, Nebius Group NV, Netskope, Inc., NICE Ltd., RingCentral Inc, Salesforce, Inc., ServiceNow Inc, Via Transportation Inc, Wix.Com Ltd, Workday Inc, Zeta Global Holdings Corp.

In the next 3 months, MS expects to receive or intends to seek compensation for investment banking services from Adobe Inc., Akamai Technologies, Inc., Amplitude Inc., Appian Corp, Asana Inc, Atlassian Corporation PLC, Autodesk, BILL Holdings Inc, Blackline Inc, Box Inc, C3.ai, CCC Intelligent Solutions Holdings Inc, Check Point Software Technologies Ltd., Cloudflare Inc, Commerce.com Inc., CoreWeave, Coursera, Inc., CrowdStrike Holdings Inc, Datadog, Inc., Descartes Systems Group Inc, DigitalOcean Holdings Inc, Docebo Inc., DocuSign Inc, Elastic NV, Figma Inc, Five9 Inc, Fortinet Inc., Freshworks Inc, Gen Digital Inc., GitLab Inc, GoDaddy Inc, HubSpot, Inc., Intuit, JFrog Ltd., Klaviyo, Inc, LegalZoom.com Inc, Lightspeed Commerce Inc., Liveramp Holdings Inc, Microsoft, monday.com Ltd, MongoDB Inc, Navan Inc, Nebius Group NV, Netskope, Inc., NICE Ltd., Okta, Inc., Oracle Corporation, PagerDuty, Inc., Palantir Technologies Inc., Palo Alto Networks Inc, Qualys Inc, Rapid7 Inc, RingCentral Inc, Sabre Corp, SailPoint Inc, Salesforce, Inc., Samsara Inc, SentinelOne, Inc., ServiceNow Inc, ServiceTitan Inc, Shopify Inc, Snowflake Inc., Sprinklr Inc, Sprout Social Inc, SPS Commerce Inc, Tenable Holdings Inc, Toast, Inc., Twilio Inc, UiPath Inc, Varonis Systems, Inc., Vertex Inc., Via Transportation Inc, Wix.Com Ltd, Workday Inc, Zeta Global Holdings Corp, Zoom Communications, Zscaler Inc.

Within the last 12 months, MS has received compensation for products and services other than investment banking services from Adobe Inc., Akamai Technologies, Inc., Amplitude Inc., Asana Inc, Atlassian Corporation PLC, Autodesk, Blackline Inc, Box Inc, CCC Intelligent Solutions Holdings Inc, Check Point Software Technologies Ltd., Cloudflare Inc, CoreWeave, CrowdStrike Holdings Inc, DigitalOcean Holdings Inc, Docebo Inc., DocuSign Inc, Dynatrace Inc, Figma Inc, Five9 Inc, Freshworks Inc, Gen Digital Inc., GitLab Inc, HubSpot, Inc., Intuit, JFrog Ltd., Klaviyo, Inc, LegalZoom.com Inc, Microsoft, monday.com Ltd, MongoDB Inc, NICE Ltd., Oracle Corporation, Palantir Technologies Inc., Palo Alto Networks Inc, RingCentral Inc, Sabre Corp, SailPoint Inc, Salesforce, Inc., SentinelOne, Inc., ServiceNow Inc, ServiceTitan Inc, Snowflake Inc., Tenable Holdings Inc, Toast, Inc., UiPath Inc, Varonis Systems, Inc., Workday Inc, Zeta Global Holdings Corp, Zoom Communications, Zscaler Inc.

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Adobe Inc., Akamai Technologies, Inc., Amplitude Inc., Appian Corp, Asana Inc, Atlassian Corporation PLC, Autodesk, BILL Holdings Inc, Blackline Inc, Box Inc, C3.ai, CCC Intelligent Solutions Holdings Inc, Check Point Software Technologies Ltd., Cloudflare Inc, Commerce.com Inc., CoreWeave, Coursera, Inc., CrowdStrike Holdings Inc, Datadog, Inc., Descartes Systems Group Inc, DigitalOcean Holdings Inc, Docebo Inc., DocuSign Inc, Elastic NV, Figma Inc, Five9 Inc, Fortinet Inc., Freshworks Inc, Gen Digital Inc., GitLab Inc, GoDaddy Inc, HubSpot, Inc., Intuit, JFrog Ltd., Klaviyo, Inc, LegalZoom.com Inc, Lightspeed Commerce Inc., Liveramp Holdings Inc, Microsoft, monday.com Ltd, MongoDB Inc, Navan Inc, Nebius Group NV, Netskope, Inc., NICE Ltd., Okta, Inc., Oracle Corporation, PagerDuty, Inc., Palantir Technologies Inc., Palo Alto Networks Inc, Qualys Inc, Rapid7 Inc, RingCentral Inc, Sabre Corp, SailPoint Inc, Salesforce, Inc., Samsara Inc, SentinelOne, Inc., ServiceNow Inc, ServiceTitan

[中间内容因长度限制已省略]

 (03/21/2023)</td><td>$204.90</td></tr><tr><td>Klaviyo, Inc (KVYO.N)</td><td>O (04/29/2026)</td><td>$16.20</td></tr><tr><td>LegalZoom.com Inc (LZ.O)</td><td>U (07/28/2022)</td><td>$7.08</td></tr><tr><td>Liveramp Holdings Inc (RAMP.N)</td><td>E (01/13/2025)</td><td>$37.66</td></tr><tr><td>NICE Ltd. (NICE.O)</td><td>E (07/21/2026)</td><td>$88.52</td></tr><tr><td>RingCentral Inc (RNG.N)</td><td>E (08/08/2023)</td><td>$37.66</td></tr><tr><td>Sprinklr Inc (CXM.N)</td><td>E (07/19/2021)</td><td>$5.56</td></tr><tr><td>Sprout Social Inc (SPT.O)</td><td>E (11/17/2020)</td><td>$7.61</td></tr><tr><td>Twilio Inc (TWLO.N)</td><td>O (02/24/2025)</td><td>$183.38</td></tr><tr><td>Wix.Com Ltd (WIX.O)</td><td>E (07/21/2026)</td><td>$48.66</td></tr><tr><td>Zeta Global Holdings Corp (ZETA.N)</td><td>E (08/01/2024)</td><td>$20.18</td></tr><tr><td>ZoomInfo Technologies Inc (GTM.O)</td><td>E (02/01/2024)</td><td>$2.92</td></tr><tr><td colspan="3">Josh Baer, CFA</td></tr><tr><td>Asana Inc (ASAN.N)</td><td>U (05/20/2025)</td><td>$6.88</td></tr><tr><td>Box Inc (BOX.N)</td><td>E (05/21/2024)</td><td>$28.45</td></tr><tr><td>CCC Intelligent Solutions Holdings Inc (CCC.O)</td><td>O (11/13/2024)</td><td>$5.73</td></tr><tr><td>Commerce.com Inc. (CMRC.O)</td><td>++</td><td>$2.72</td></tr><tr><td>CoreWeave (CRWV.O)</td><td>E (04/22/2025)</td><td>$82.64</td></tr><tr><td>Coursera, Inc. (COUR.N)</td><td>E (04/22/2026)</td><td>$5.34</td></tr><tr><td>DigitalOcean Holdings Inc (DOCN.N)</td><td>O (01/16/2025)</td><td>$142.68</td></tr><tr><td>Docebo Inc. (DCBO.O)</td><td>E (05/12/2025)</td><td>$19.54</td></tr><tr><td>DocuSign Inc (DOCU.O)</td><td>E (01/16/2024)</td><td>$47.89</td></tr><tr><td>Lightspeed Commerce Inc. (LSPD.N)</td><td>E (02/18/2021)</td><td>$9.76</td></tr><tr><td>monday.com Ltd (MNDY.O)</td><td>O (08/12/2025)</td><td>$73.91</td></tr><tr><td>Nebius Group NV (NBIS.O)</td><td>E (01/15/2026)</td><td>$218.16</td></tr><tr><td>Sabre Corp (SABR.O)</td><td>E (03/16/2021)</td><td>$1.66</td></tr><tr><td>ServiceTitan Inc (TTAN.O)</td><td>O (01/20/2026)</td><td>$69.90</td></tr><tr><td>Toast, Inc. (TOST.N)</td><td>O (12/16/2021)</td><td>$29.21</td></tr><tr><td>Via Transportation Inc (VIA.N)</td><td>O (01/20/2026)</td><td>$17.50</td></tr><tr><td>Zoom Communications (ZM.O)</td><td>E (10/11/2022)</td><td>$85.81</td></tr><tr><td>Check Point Software Technologies Ltd. (CHKP.O)</td><td>E (10/16/2023)</td><td>$127.91</td></tr><tr><td>CrowdStrike Holdings Inc (CRWD.O)</td><td>O (03/10/2026)</td><td>$188.42</td></tr><tr><td>Fortinet Inc. (FTNT.O)</td><td>E (07/21/2026)</td><td>$155.05</td></tr><tr><td>Gen Digital Inc. (GEN.O)</td><td>E (06/07/2024)</td><td>$25.58</td></tr><tr><td>Netskope, Inc. (NTSK.O)</td><td>O (10/13/2025)</td><td>$11.96</td></tr><tr><td>Okta, Inc. (OKTA.O)</td><td>O (12/02/2024)</td><td>$136.69</td></tr><tr><td>Palo Alto Networks Inc (PANW.O)</td><td>O (10/10/2017)</td><td>$335.28</td></tr><tr><td>Qualys Inc (QLYS.O)</td><td>U (02/09/2021)</td><td>$140.23</td></tr><tr><td>Rapid7 Inc (RPD.O)</td><td>U (07/21/2026)</td><td>$9.91</td></tr><tr><td>SailPoint Inc (SAIL.O)</td><td>O (09/02/2025)</td><td>$14.78</td></tr><tr><td>SentinelOne, Inc. (S.N)</td><td>E (12/02/2024)</td><td>$18.22</td></tr><tr><td>Tenable Holdings Inc (TENB.O)</td><td>E (12/02/2024)</td><td>$32.83</td></tr><tr><td>Varonis Systems, Inc. (VRNS.O)</td><td>E (01/26/2026)</td><td>$45.33</td></tr><tr><td>Zscaler Inc (ZS.O)</td><td>E (04/22/2026)</td><td>$142.26</td></tr><tr><td colspan="3">Sanjit K Singh</td></tr><tr><td>Akamai Technologies, Inc. (AKAM.O)</td><td>O (01/12/2026)</td><td>$124.30</td></tr><tr><td>Appian Corp (APPN.O)</td><td>E (04/30/2026)</td><td>$22.64</td></tr><tr><td>C3.ai (AI.N)</td><td>U (01/04/2021)</td><td>$8.19</td></tr><tr><td>Cloudflare Inc (NET.N)</td><td>O (12/02/2024)</td><td>$268.98</td></tr><tr><td>Datadog, Inc. (DDOG.O)</td><td>O (01/12/2026)</td><td>$245.77</td></tr><tr><td>Dynatrace Inc (DT.N)</td><td>E (02/13/2024)</td><td>$41.36</td></tr><tr><td>Elastic NV (ESTC.N)</td><td>E (07/21/2026)</td><td>$58.68</td></tr><tr><td>GitLab Inc (GTLB.O)</td><td>E (01/12/2026)</td><td>$31.35</td></tr><tr><td>JFrog Ltd. (FROG.O)</td><td>E (07/21/2026)</td><td>$79.68</td></tr><tr><td>MongoDB Inc (MDB.O)</td><td>O (04/12/2023)</td><td>$304.97</td></tr><tr><td>Oracle Corporation (ORCL.N)</td><td>E (01/15/2019)</td><td>$125.84</td></tr><tr><td>PagerDuty, Inc. (PD.N)</td><td>U (07/21/2026)</td><td>$8.82</td></tr><tr><td>Palantir Technologies Inc. (PLTR.O)</td><td>E (02/04/2025)</td><td>$124.57</td></tr><tr><td>Snowflake Inc. (SNOW.N)</td><td>O (06/24/2025)</td><td>$267.80</td></tr><tr><td>UiPath Inc (PATH.N)</td><td>E (09/07/2022)</td><td>$10.70</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
