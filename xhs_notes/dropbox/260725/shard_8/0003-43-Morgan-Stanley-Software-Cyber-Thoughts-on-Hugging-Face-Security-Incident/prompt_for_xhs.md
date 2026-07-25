你是资深小红书内容策划 + 投研翻译官，擅长把英文/中文研报改写成高互动、可收藏、可转发的中文小红书笔记。

【目标】
- 把下面的研报解析内容，改写成一篇中文小红书笔记。
- 风格：投研博主风：信息密度高，但像给朋友讲逻辑
- 长度：不超过 1000 字，信息密度高但不要写长文。
- emoji 密度：中

【必须输出的结构】
1. 第一行：标题，20 字以内，不要像论文标题，也不要用夸张极限词。
2. 第二行：封面短标题，10 字以内，适合放在图中间。
3. 第三行：封面副标题，10-18 字，短句。
4. 正文分段清晰，每段不超过 3 行，可以用编号、小标题或加粗。
5. 正文要自然呈现观点，但不要暴露写作框架或思考过程。
6. 末尾可以保留 2-4 个相关标签，只允许从这些标签里选择：`#学习笔记`、`#研究笔记`、`#学习研究`、`#研报解读`。

【严禁输出】
- 不要出现这些栏目名或类似栏目名：`一句话结论`、`我最想提醒的一点`、`配图建议`、`免责声明`、`非投资建议`、`仅做学习交流`、`仅作学习交流`。
- 不要在正文最后追加配图建议，不要告诉我第 2/3/4 张图怎么配文。
- 不要输出任何包含“投资”的免责声明，也不要输出“非投资建议”这种表述。
- 不要输出财经敏感标签：`#投资学习`、`#财经`、`#金融`、`#股票`、`#基金`、`#理财`。
- 不要输出无关标签：`#小红书笔记`、`#笔记分享`、`#干货分享`。
- 不要写“关注”“点赞”“求关注”“评论区见”“评论区留言”等直接互动诱导；可以写“欢迎一起讨论”“可以继续交流”。

【平台发布合规要求】
- 不要写“爆款”“震惊”“必看”“必读”“最强”“最全”“唯一”“全网首发”等极限词或夸张词。
- 不要写“投资建议”“买入”“卖出”“强烈推荐”“稳赚”“保本”“必涨”“抄底”“上车”“内幕”“翻倍”等金融操作或收益承诺表达。
- “投资”相关词尽量改成“投研”“研究”“观察”“学习参考”；如果必须保留，也要放在中性语境里。
- 不要承诺收益，不要引导交易，不要暗示确定性结果。

【内容要求】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 可以把专业表达翻成人话，但不能扭曲意思。
- 遇到不确定或缺失信息：用“研报未给出”或“这里是推测”明确标注。
- 默认避免出现具体投行品牌名，比如“GS”“GS”，统一写作“投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

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

Within the last 12 months, MS has provided or is providing investment banking services to, or has an investment banking client relationship with, the following company: Adobe Inc., Akamai Technologies, Inc., Amplitude Inc., Appian Corp, Asana Inc, Atlassian Corporation PLC, Autodesk, BILL Holdings Inc, Blackline Inc, Box Inc, C3.ai, CCC Intelligent Solutions Holdings Inc, Check Point Software Technologies Ltd., Cloudflare Inc, Commerce.com Inc., CoreWeave, Coursera, Inc., CrowdStrike Holdings Inc, Datadog, Inc., Descartes Systems Group Inc, DigitalOcean Holdings Inc, Docebo Inc., DocuSign Inc, Elastic NV, Figma Inc, Five9 Inc, Fortinet Inc., Freshworks Inc, Gen Digital Inc., GitLab Inc, GoDaddy Inc, HubSpot, Inc., Intuit, JFrog Ltd., Klaviyo, Inc, LegalZoom.com Inc, Lightspeed Commerce Inc., Liveramp Holdings Inc, Microsoft, monday.com Ltd, MongoDB Inc, Navan Inc, Nebius Group NV, Netskope, Inc., NICE Ltd., Okta, Inc., Oracle Corporation, PagerDuty, Inc., Palantir Technologies Inc., Palo Alto Networks Inc, Qualys Inc, Rapid7 Inc, RingCentral Inc, Sabre Corp, SailPoint Inc, Salesforce, Inc., Samsara Inc, SentinelOne, Inc., ServiceNow Inc, ServiceTitan Inc, Shopify Inc, Snowflake Inc., Sprinklr Inc, Sprout Social Inc, SPS Commerce Inc, Tenable Holdings Inc, Toast, Inc., Twilio Inc, UiPath Inc, Varonis Systems, Inc., Vertex Inc., Via Transportation Inc, Wix.Com Ltd, Workday Inc, Zeta Global Holdings Corp, Zoom Communications, Zscaler Inc.

Within the last 12 months, MS has either provided or is providing non-investment banking, securities-related services to and/or in the past has entered into an agreement to provide services or has a client relationship with the following company: Adobe Inc., Akamai Technologies, Inc., Amplitude Inc., Asana Inc, Atlassian Corporation PLC, Autodesk, Blackline Inc, Box Inc, CCC Intelligent Solutions Holdings Inc, Check Point Software Technologies Ltd., Cloudflare Inc, Commerce.com Inc., CoreWeave, CrowdStrike Holdings Inc, Datadog, Inc., DigitalOcean Holdings

Inc, Docebo Inc., DocuSign Inc, Dynatrace Inc, Figma Inc, Five9 Inc, Fortinet Inc, Freshworks Inc, Gen Digital Inc, GitLab Inc, GoDaddy Inc, HubSpot, Inc, Intuit, JFrog Ltd., Klaviyo, Inc, LegalZoom.com Inc, Microsoft, monday.com Lt

[中间内容因长度限制已省略]

74</td></tr><tr><td>Autodesk (ADSK.O)</td><td>O (08/23/2024)</td><td>$203.50</td></tr><tr><td>Figma Inc (FIG.N)</td><td>E (08/25/2025)</td><td>$21.47</td></tr><tr><td>Five9 Inc (FIVN.O)</td><td>E (10/10/2022)</td><td>$22.95</td></tr><tr><td>Freshworks Inc (FRSH.O)</td><td>E (10/18/2021)</td><td>$10.06</td></tr><tr><td>GoDaddy Inc (GDDY.N)</td><td>E (07/19/2021)</td><td>$89.40</td></tr><tr><td>HubSpot, Inc. (HUBS.N)</td><td>O (03/21/2023)</td><td>$204.90</td></tr><tr><td>Klaviyo, Inc (KVYO.N)</td><td>O (04/29/2026)</td><td>$16.20</td></tr><tr><td>LegalZoom.com Inc (LZ.O)</td><td>U (07/28/2022)</td><td>$7.08</td></tr><tr><td>Liveramp Holdings Inc (RAMP.N)</td><td>E (01/13/2025)</td><td>$37.66</td></tr><tr><td>NICE Ltd. (NICE.O)</td><td>E (07/21/2026)</td><td>$88.52</td></tr><tr><td>RingCentral Inc (RNG.N)</td><td>E (08/08/2023)</td><td>$37.66</td></tr><tr><td>Sprinklr Inc (CXM.N)</td><td>E (07/19/2021)</td><td>$5.56</td></tr><tr><td>Sprout Social Inc (SPT.O)</td><td>E (11/17/2020)</td><td>$7.61</td></tr><tr><td>Twilio Inc (TWLO.N)</td><td>O (02/24/2025)</td><td>$183.38</td></tr><tr><td>Wix.Com Ltd (WIX.O)</td><td>E (07/21/2026)</td><td>$48.66</td></tr><tr><td>Zeta Global Holdings Corp (ZETA.N)</td><td>E (08/01/2024)</td><td>$20.18</td></tr><tr><td>ZoomInfo Technologies Inc (GTM.O)</td><td>E (02/01/2024)</td><td>$2.92</td></tr><tr><td colspan="3">Josh Baer, CFA</td></tr><tr><td>Asana Inc (ASAN.N)</td><td>U (05/20/2025)</td><td>$6.88</td></tr><tr><td>Box Inc (BOX.N)</td><td>E (05/21/2024)</td><td>$28.45</td></tr><tr><td>CCC Intelligent Solutions Holdings Inc (CCC.O)</td><td>O (11/13/2024)</td><td>$5.73</td></tr><tr><td>Commerce.com Inc. (CMRC.O)</td><td>++</td><td>$2.72</td></tr><tr><td>CoreWeave (CRWV.O)</td><td>E (04/22/2025)</td><td>$82.64</td></tr><tr><td>Coursera, Inc. (COUR.N)</td><td>E (04/22/2026)</td><td>$5.34</td></tr><tr><td>DigitalOcean Holdings Inc (DOCN.N)</td><td>O (01/16/2025)</td><td>$142.68</td></tr><tr><td>Docebo Inc. (DCBO.O)</td><td>E (05/12/2025)</td><td>$19.54</td></tr><tr><td>DocuSign Inc (DOCU.O)</td><td>E (01/16/2024)</td><td>$47.89</td></tr><tr><td>Lightspeed Commerce Inc. (LSPD.N)</td><td>E (02/18/2021)</td><td>$9.76</td></tr><tr><td>monday.com Ltd (MNDY.O)</td><td>O (08/12/2025)</td><td>$73.91</td></tr><tr><td>Nebius Group NV (NBIS.O)</td><td>E (01/15/2026)</td><td>$218.16</td></tr><tr><td>Sabre Corp (SABR.O)</td><td>E (03/16/2021)</td><td>$1.66</td></tr><tr><td>ServiceTitan Inc (TTAN.O)</td><td>O (01/20/2026)</td><td>$69.90</td></tr><tr><td>Toast, Inc. (TOST.N)</td><td>O (12/16/2021)</td><td>$29.21</td></tr><tr><td>Via Transportation Inc (VIA.N)</td><td>O (01/20/2026)</td><td>$17.50</td></tr><tr><td>Zoom Communications (ZM.O)</td><td>E (10/11/2022)</td><td>$85.81</td></tr><tr><td>Check Point Software Technologies Ltd. (CHKP.O)</td><td>E (10/16/2023)</td><td>$127.91</td></tr><tr><td>CrowdStrike Holdings Inc (CRWD.O)</td><td>O (03/10/2026)</td><td>$188.42</td></tr><tr><td>Fortinet Inc. (FTNT.O)</td><td>E (07/21/2026)</td><td>$155.05</td></tr><tr><td>Gen Digital Inc. (GEN.O)</td><td>E (06/07/2024)</td><td>$25.58</td></tr><tr><td>Netskope, Inc. (NTSK.O)</td><td>O (10/13/2025)</td><td>$11.96</td></tr><tr><td>Okta, Inc. (OKTA.O)</td><td>O (12/02/2024)</td><td>$136.69</td></tr><tr><td>Palo Alto Networks Inc (PANW.O)</td><td>O (10/10/2017)</td><td>$335.28</td></tr><tr><td>Qualys Inc (QLYS.O)</td><td>U (02/09/2021)</td><td>$140.23</td></tr><tr><td>Rapid7 Inc (RPD.O)</td><td>U (07/21/2026)</td><td>$9.91</td></tr><tr><td>SailPoint Inc (SAIL.O)</td><td>O (09/02/2025)</td><td>$14.78</td></tr><tr><td>SentinelOne, Inc. (S.N)</td><td>E (12/02/2024)</td><td>$18.22</td></tr><tr><td>Tenable Holdings Inc (TENB.O)</td><td>E (12/02/2024)</td><td>$32.83</td></tr><tr><td>Varonis Systems, Inc. (VRNS.O)</td><td>E (01/26/2026)</td><td>$45.33</td></tr><tr><td>Zscaler Inc (ZS.O)</td><td>E (04/22/2026)</td><td>$142.26</td></tr><tr><td colspan="3">Sanjit K Singh</td></tr><tr><td>Akamai Technologies, Inc. (AKAM.O)</td><td>O (01/12/2026)</td><td>$124.30</td></tr><tr><td>Appian Corp (APPN.O)</td><td>E (04/30/2026)</td><td>$22.64</td></tr><tr><td>C3.ai (AI.N)</td><td>U (01/04/2021)</td><td>$8.19</td></tr><tr><td>Cloudflare Inc (NET.N)</td><td>O (12/02/2024)</td><td>$268.98</td></tr><tr><td>Datadog, Inc. (DDOG.O)</td><td>O (01/12/2026)</td><td>$245.77</td></tr><tr><td>Dynatrace Inc (DT.N)</td><td>E (02/13/2024)</td><td>$41.36</td></tr><tr><td>Elastic NV (ESTC.N)</td><td>E (07/21/2026)</td><td>$58.68</td></tr><tr><td>GitLab Inc (GTLB.O)</td><td>E (01/12/2026)</td><td>$31.35</td></tr><tr><td>JFrog Ltd. (FROG.O)</td><td>E (07/21/2026)</td><td>$79.68</td></tr><tr><td>MongoDB Inc (MDB.O)</td><td>O (04/12/2023)</td><td>$304.97</td></tr><tr><td>Oracle Corporation (ORCL.N)</td><td>E (01/15/2019)</td><td>$125.84</td></tr><tr><td>PagerDuty, Inc. (PD.N)</td><td>U (07/21/2026)</td><td>$8.82</td></tr><tr><td>Palantir Technologies Inc. (PLTR.O)</td><td>E (02/04/2025)</td><td>$124.57</td></tr><tr><td>Snowflake Inc. (SNOW.N)</td><td>O (06/24/2025)</td><td>$267.80</td></tr><tr><td>UiPath Inc (PATH.N)</td><td>E (09/07/2022)</td><td>$10.70</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
