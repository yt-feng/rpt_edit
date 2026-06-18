你是麦肯锡/投研风格的微信公众号财经文章主笔，擅长用金字塔原理把研报内容转化为“有主张、有层次、有洞察、但仍保留完整报告阅读欲望”的长文。

【目标】
- 基于下面的研报解析内容，写一篇微信公众号文章 Markdown。
- 风格：稳重、专业、克制、有洞察，像咨询公司合伙人写给高净值读者/产业决策者的研报导读。
- 长度：约 3000 字，允许上下浮动 15%。
- 不要使用 emoji。
- 可以基于报告内容做适度发散，但必须是从原文逻辑推出的判断，不要编造数据、公司动作或引用。
- 不要把研报所有正文内容讲完，要留下明确但自然的伏笔，让读者愿意加入社群阅读完整报告。

【金字塔原理写作原则】
1. 结论先行：文章开头先回答“这份报告最值得看的判断是什么”，而不是介绍背景。
2. 统领思想：全文只能服务一个主判断，避免变成摘要合集。
3. 纵向回答：每一层都要回答上一层提出的“为什么”或“所以呢”。
4. 横向 MECE：每个一级小节必须彼此独立、共同支撑主判断，避免重叠。
5. Synthesis over summary：不要复述报告段落，要提炼“这些事实合在一起意味着什么”。
6. So what：每个小节末尾必须落到对行业、公司、竞争格局、资产定价或读者观察框架的含义。
7. Action title：所有 `##` 小标题必须是“直接讲述洞察的完整句子”，不能是目录标签。

【标题与小标题硬性要求】
- `# 标题` 必须直接表达一个判断，例如“市场真正低估的不是需求，而是供给侧的再定价”。
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`JPM`。标题格式建议：`# JPM：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 机构名只要求出现在 `# 标题` 中，正文可以克制提及，不要为了重复机构名牺牲可读性。
- 禁止使用以下机械标题：
  - 一、核心判断
  - 二、真正重要的是结构性变量
  - 三、报告没有说透
  - 四、对读者的启发
  - 关键变化
  - 投资启示
  - 总结
- 所有 `##` 标题都要像麦肯锡报告里的 action title：读完标题就知道这一节结论。
- 小标题可以带序号，但序号后必须是一句洞察，例如：`## 1. 这轮变化真正考验的是企业能否把规模转化为议价权`。

【建议结构，但不要机械照抄标题】
1. `# 标题`：机构中文名 + 一句主判断，不超过 40 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
5. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
6. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：欢迎来星球微信群里继续讨论。
7. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
8. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。可以类似“欢迎来星球微信群里继续讨论”。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份JPM研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
## Hong Kong Property

Takeaways from legal expert call on cross-border home purchase

The State Council's Regulations on Outbound Direct Investment (“Document 837”) (report) have triggered investors' concerns about the eligibility of Mainland Chinese to purchase property in Hong Kong. To address the legal implications, we hosted an expert call with a Beijing-based lawyer. Our 6 key takeaways:

1. For Mainland Chinese, money remittance to Hong Kong for the purpose of buying property has never been—and is unlikely to be—allowed.  
2. However, there is no ban on Mainland Chinese buying property in Hong Kong if the funding source is offshore.  
3. Document 837 does not appear to be targeted at curbing Mainland Chinese purchases of property in Hong Kong.  
4. Including real estate in CRS is complex and may not be realistic in the near term.  
5. For Mainland Chinese classified as “Mainland tax residents”, they are theoretically subject to 20% tax on rental income/capital gains from HK property, but this is not a new rule.  
6. Even if some Mainland Chinese are found to have violated laws to fund purchases of HK property, penalties are likely but forced disposals are unlikely.

While we believe the overhang may persist for some time, we came out of the call marginally less concerned, as it appears Document 837 is not (at least for now) targeted at Mainland Chinese purhcases of property in HK, and the regulations are, more or less, the status quo. However, the expert call still highlighted the risk of the Chinese government potentially requiring HK-based Mainland Chinese (if defined as “Mainland tax residents”) to report their offshore asset holdings (including real estate), which might be subject to additional taxes. This would then make holding HK property financially less attractive. In the HK housing market, we estimate 5-10% of all transactions (10-15% by value) are from non-HK-based Mainland Chinese buyers, who may potentially be impacted by the tighter enforcement (although if they can prove the funding source is offshore, they theoretically should not be impacted). This alone, in our view, should not derail the property upcycle (more discussion in our previous report). However, the sector is currently confronted by two other headwinds: (1) rising expectations of a rate hike (report); (2) a lackluster Hang Seng Index, which has historically shown a strong correlation to HK home prices. In the near term, we expect the sector to trade range-bound until: (1) proof of minimal impact on primary sell-through rates, secondary sales volumes and home prices; (2) easing expectations for a rate hike. In the near term, we expect CKA/Sino to outperform and Henderson/NWD to underperform. On dips, we would accumulate SHKP.

## Mainland China/Hong Kong Property & Conglomerates

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

## 20 Q&As from expert call

Q1) What is the background of Document 837? Why was this rolled out at this juncture?

- The introduction of Document 837 was primarily triggered by a representative cross-border case involving a US company's proposed acquisition of a Chinese AI company. This case raised two key regulatory concerns: (1) individual outbound investment: The controlling shareholder held equity offshore in a personal capacity; and (2) technology export: The company transferred its core operations and personnel offshore, which Chinese regulators deemed an unapproved technology export. Document 837 represents a top-down regulatory response prompted by real-world cases.  
- Another key driver is tax supervision. Chinese individuals have accumulated significant offshore assets (e.g. equities), but the lack of a unified State Council-level framework previously made it difficult to coordinate supervision and tax enforcement. The new regulations aim to address this gap. Document 837 is a framework-level policy that consolidates existing rules across ministries, without materially changing the current regime.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Q2) Will more explicit measures be introduced to regulate Mainland Chinese residents purchasing property in Hong Kong?

Under the current legal framework, Mainland residents' use of onshore funds to purchase overseas properties (including HK) has not been formally liberalized, and no fully compliant channel exists.

- SAFE has explicitly stated that outbound transfers for overseas property purchases (including the annual US\$50,000 FX quota) under the capital account are not permitted.  
- Overseas property falls under the capital account, which remains tightly controlled (with only limited openings for equity investments).

China's FX regime distinguishes between:

- Current account (largely open): trade in goods and services.  
- Capital account (restricted): including overseas investments, lending, guarantees, and real estate.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Q3) Under the current framework, are Mainland residents prohibited from purchasing overseas property?

The key distinction lies in the source of funds:

\- Onshore funds: RMB cannot be legally converted or remitted offshore for property purchases.

\- Offshore funds: If an individual already has legitimate offshore income (e.g., salary or investment income), and no onshore funds are involved, overseas purchases are allowed.

The regulatory focus is on whether the funds originate from the Chinese Mainland:

\- If no cross-border transfer of onshore funds is involved, restrictions generally do not apply.

\- If RMB is converted and remitted offshore for property purchases, it falls under restricted capital-account activity.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Q4) For Mainland individuals working in Hong Kong, are there any restrictions on property purchases? What are the tax implications?

This needs to be analyzed from two dimensions: FX regulation and taxation.

From an FX perspective, restrictions apply only if both conditions are met:

1. The individual is still a Mainland resident (e.g., holds a Mainland ID); and

2. the funds originate from the Mainland.

If either condition is not met (e.g., use of income generated in Hong Kong), then FX restrictions typically do not apply.

From a tax perspective, the key is whether the individual is a Mainland Chinese tax resident. If so, global income (including offshore rental income and capital gains) is subject to a 20% individual income tax (with foreign tax credits to avoid double taxation). Typically, if a person still holds a Mainland Chinese hukou (household registration), he or she would be classified as a Mainland Chinese tax resident (long-term working/living in HK alone does not necessarily change that status).

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Q5) Will real estate be included under the common reporting standard (“CRS”) in the future?

\- CRS is designed for information exchange between tax authorities and financial institutions, covering financial accounts (balances, interest, dividends, etc.).

• Real estate is currently not categorized as a financial asset under CRS.

\- Including real estate would require coordination among global property registries or a major expansion of the CRS framework, which is operationally complex.

However, indirect monitoring is possible:

• Account-level data may reveal large outflows or asset growth;

• tax authorities may request explanations; and

\- public property registries (e.g., Hong Kong Land Registry) may enable cross-checking.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Q6) If funds were previously transferred offshore in violation of FX rules to purchase HK property, what are the risks?

Enforcement focuses on illegal cross-border fund transfers, not the property purchase itself.

Common violations include:

• Underground banking channels  
- Matching transactions (“对敲”)  
- Aggregation of multiple USD50k quotas.

Penalties generally involve fines of approximately 5–10% (or higher for illegal funds).

Forced disposal of offshore assets is unlikely, in practice.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Q7) How does the Chinese government view Mainland residents holding assets in Hong Kong?

The key concern remains compliance with capital outflows, rather than asset location.

In practice:

- Existing offshore assets are generally treated as a fait accompli.  
• Authorities typically do not require repatriation.  
- Hong Kong is viewed as relatively more acceptable compared to other offshore jurisdictions (as it is part of China).

For corporates, however, policy tends to favor investment in strategic outbound regions (e.g., Southeast Asia, Middle East, Latin America).

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Q8) Can offshore income (e.g., IPO proceeds, stock compensation) be used to purchase property in HK?

- Yes. Such income is generally considered legitimate offshore funds under FX rules and can be used for offshore investment.  
- However, if the individual is a Chinese tax resident, the income may still be subject to taxation in China.  
- There is currently no requirement for individuals to repatriate offshore investment income.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Q9) Will more detailed rules follow the Document 837?

Document 837 is a framework/coordination regulation, and further detailed rules are likely.

Its three core elements are:

- Unified oversight of corporate ODI: consolidating and standardizing regulation of corporate outbound investment.  
• Stronger technology export controls: tighter rules for key areas (e.g., AI).  
- Bringing individual outbound investment into the regulatory system: for the first time at the national level, explicitly proposing standardized management of individuals' overseas investment.

Following typical legislative practice, after the State Council issues a framework regulation, implementing agencies (NDRC, MOFCOM, SAFE, etc.) would issue supporting rules and operational guidance. Thus, regulatory standards and operational pathways—especially for individual outbound investment—are expected to become clearer. Exact timeline is, however, uncertain.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Q10) After paying penalties for FX violations, are the funds considered “legal”?

\- In practice, penalties apply to the FX violation itself. Once fines are paid, the funds typically remain offshore and are not required to be repatriated.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Q11) Will Document 837 make it even harder for funds to go to Hong Kong for home purchases in the future?

- Common methods used in practice include: using the annual USD50k quota, netting/ offset arrangements (or underground channels), shifting funds via service fees between related Mainland–Hong Kong companies, and using ODI structures to remit funds and then divert them to property purchases or personal use (the last one has the highest compliance risk). Many of these are grey areas and may not be legitimate.  
- Supervision over outbound remittances is tightening, and these channels are expected to face stricter scrutiny and higher execution difficulty. Bank compliance reviews for cross-border transfers have become more demanding.  
- In practice, “netting” risks concentrate around centralized fund flows.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Q12) Can gifted offshore funds be used for home purchases in HK?

\- Yes, if the gift (e.g. from a HK-based relative) is genuinely offshore and does not involve disguised cross-border transfers.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Q13) Can company/trust structures avoid CRS or tax obligations?

\- For a company structure, CRS typically focuses on the account holder and its controlling persons (e.g., shareholders). The exact disclosure depends on structuring and reporting positions, and there are relatively few public practical cases, so the effect is uncertain.

- For trusts, CRS requires reporting key parties including the settlor, trustee, and beneficiaries. There is practice showing such information can be exchanged to Mainland tax authorities and trigger inquiries.  
- From a tax perspective, authorities generally apply “substance over form.” If the main purpose of the structure is tax avoidance, tax authorities may look through it and impose tax obligations.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Q14) Will “Property Connect” (购房通) progress?

- “Property Connect” (i.e. establishing a legal way for HK-based Mainland Chinese to remit funds from the Chinese Mainland for home purchases in HK) is a proposal from Hong Kong, but whether it can truly land depends on whether the Mainland side addresses the core issue: outbound fund remittance. Since FX conversion and capital-account flows are regulated on the Mainland, without Mainland policy support, Hong Kong alone cannot roll this out.  
- A pilot is not impossible under specific conditions (e.g., limited cities, targeted groups such as high taxpayers, quota-based opening), but it would more likely be a cautious, limited pilot rather than a full opening. However, so far there is no sign of the Chinese government pushing for “Property Connect”.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Q15) Is RMB settlement in the Mainland for Hong Kong property purchases considered compliant?

\- Not compliant. Regulators would view this as a cross-border transaction that is paid in FX, which is explicitly restricted under FX administration.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Q16) Are fines limited to transferred funds? Would assets be confiscated?

- Fines are typically calculated only on the amount of funds remitted out in violation of rules. For example, if USD1 million was remitted out in violation, the fine is generally around 5%–10% of that amount, and does not extend to other funds that never left the Chinese Mainland.  
- As for asset disposal, public cases have not shown confiscation, forced sale, or mandatory repatriation. Although rules (especially State Council regulations) in theory mention disposal of offshore assets/rights for illegal outbound investment, market understanding is that this mainly targets corporate ODI.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## Q17) Would there be a grace period for past violations?

\- A “grace period” or “transition period” is unlikely. FX violations are generally handled under existing rules, and there has been no clear policy offering penalty waivers for voluntary disclosure.

\- From a tax compliance perspective, enforcement is generally subject to a practical limitations period and typically focuses on matters arising within the most recent 3 years; issues from earlier periods are less likely to be pursued on a retroactive basis.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Q18) When Document 837's implementing rules come out, could they explicitly open up overseas real estate investment, or at least mention related arrangements?

- The detailed rules are unlikely to substantively open up overseas real estate investment.  
- Two possible approaches in wording: (1) not mentioning real estate, maintaining the current “not opened” status; or (2) explicitly reiterating that overseas real estate investment is not allowed through fund remittance. Either way, a substantive shift is not expected.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Q19) If someone previously remitted funds out in violation of FX rules and bought a home in Hong Kong, then later canceled their Mainland identity/hukou, is there still retroactive risk?

\- Tax liability depends on when the gain is realized. If the person is no longer a Mainland Chinese tax resident at the time of the sale, the gain may not be taxable in China.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Q20) What are the penalties for a Mainland Chinese failing to declare rental income or capital gains from HK properties?

- Late payment charges are typically calculated at $0.05\%$

[中间内容因长度限制已省略]

pdates may be provided on companies/industries based on company-specific developments or announcements, market conditions or any other publicly available information. There can be no assurance that future results or events will be consistent with any such opinions, forecasts or projections, which represent only one possible outcome. Furthermore, such opinions, forecasts or projections are subject to certain risks, uncertainties and assumptions that have not been verified, and future actual results or events could differ materially. The value of, or income from, any investments referred to in this material may fluctuate and/or be affected by changes in exchange rates. All pricing is indicative as of the close of market for the securities discussed, unless otherwise stated. Past performance is not indicative of future results. Accordingly, investors may receive back less than originally invested. This material is not intended as an offer or solicitation for the purchase or sale of any financial instrument. The opinions and recommendations herein do not take into account individual client circumstances, objectives, or needs and are not intended as recommendations of particular securities, financial instruments or strategies to particular clients. This material may include views on structured securities, options, futures and other derivatives. These are complex instruments, may involve a high degree of risk and may be appropriate investments only for sophisticated investors who are capable of understanding and assuming the risks involved. The recipients of this material must make their own independent decisions regarding any securities or financial instruments mentioned herein and should seek advice from such independent financial, legal, tax or other adviser as they deem necessary. JPM may trade as a principal on the basis of the Research Analysts' views and research, and it may also engage in transactions for its own account or for its clients' accounts in a manner inconsistent with the views taken in this material, and JPM is under no obligation to ensure that such other communication is brought to the attention of any recipient of this material. Others within JPM, including Strategists, Sales staff and other Research Analysts, may take views that are inconsistent with those taken in this material. Employees of JPM not involved in the preparation of this material may have investments in the securities (or derivatives of such securities) mentioned in this material and may trade them in ways different from those discussed in this material. This material is not an advertisement for or marketing of any issuer, its products or services, or its securities in any jurisdiction.

Confidentiality and Security Notice: This transmission may contain information that is privileged, confidential, legally privileged, and/or exempt from disclosure under applicable law. If you are not the intended recipient, you are hereby notified that any disclosure, copying, distribution, or use of the information contained herein (including any reliance thereon) is STRICTLY PROHIBITED. Although this transmission and any attachments are believed to be free of any virus or other defect that might affect any computer system into which it is received and opened, it is the responsibility of the recipient to ensure that it is virus free and no responsibility is accepted by JPM Chase & Co., its subsidiaries and affiliates, as applicable, for any loss or damage arising in any way from its use. If you received this transmission in error, please immediately contact the sender and destroy the material in its entirety, whether in electronic or hard copy format. This message is subject to electronic monitoring: https://www.JPM.com/disclosures/email

MSCI: Certain information herein (“Information”) is reproduced by permission of MSCI Inc., its affiliates and information providers (“MSCI”) ©2026. No reproduction or dissemination of the Information is permitted without an appropriate license. MSCI MAKES NO EXPRESS OR IMPLIED WARRANTIES (INCLUDING MERCHANTABILITY OR FITNESS) AS TO THE INFORMATION AND DISCLAIMS ALL LIABILITY TO THE EXTENT PERMITTED BY LAW. No Information constitutes investment advice, except for any applicable Information from MSCI ESG Research. Subject also to msci.com/disclaimer

Sustainalytics: Certain information, data, analyses and opinions contained herein are reproduced by permission of Sustainalytics and: (1) includes the proprietary information of Sustainalytics; (2) may not be copied or redistributed except as specifically authorized; (3) do not constitute investment advice nor an endorsement of any product or project; (4) are provided solely for informational purposes; and (5) are not warranted to be complete, accurate or timely. Sustainalytics is not responsible for any trading decisions, damages or other losses related to it or its use. The use of the data is subject to conditions available at https://www.sustainalytics.com/legal-disclaimers. ©2026 Sustainalytics. All Rights Reserved.

"Other Disclosures" last revised May 16, 2026.

Copyright 2026 JPM Chase & Co. All rights reserved. This material or any portion hereof may not be reprinted, sold or redistributed without the written consent of JPM. It is strictly prohibited to use or share without prior written consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.

Completed 16 Jun 2026 12:23 PM HKT

Disseminated 16 Jun 2026 12:23 PM HKT
"""
