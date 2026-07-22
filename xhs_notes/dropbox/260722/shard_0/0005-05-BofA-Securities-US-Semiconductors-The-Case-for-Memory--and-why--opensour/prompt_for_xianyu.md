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
US Semiconductors

# The Case for Memory, and why “open-source” expands TAM

Industry Overview

## Chinese Open LLMs are no threat to memory demand

Latest releases in open-source models, including China's Kimi K3 launched July 16, reinforce our bullish thesis on memory/MU. From a high level, we view the aggressive Chinese open-model API pricing (up to 5-350x cheaper than Western models) as reflective of business-model choices, not necessarily reflective of hardware costs. Importantly, these models, using various efficiency techniques (more below), are able to reduce compute/GPU intensity, but require the same or more memory as their model weights and active parameters increase. We also flag that every open-weight download also creates a new customer-side memory socket that wouldn't exist in a closed-model setting.

## Chinese models charge less, but still require same memory

Chinese open-model API pricing is aggressive, with Tencent Hunyuan at \$0.06/mn input vs. Claude Opus 4.8 at \$15/mn, and even Moonshot AI's latest Kimi K3 charging only \$3/mn despite 'similar' performance. However, we flag API price is a business-model choice, not necessarily a hardware-cost read-through. For instance, Kimi K3 still requires \~1.4 TB of HBM per serving instance to run. This is similar to OpenAI's 'oss-120b' open model with the same MXFP4 native precision (for like-for-like compression) with 120B total parameters (23x smaller than Kimi K3) requiring \~63GB of weight memory to run (22x smaller). In other words, often times API pricing actually scales with total memory weight and active parameters, even for open Chinese LLMs. "Open" refers to weight distribution, not deployment cost, and customers still need to purchase HBM, DRAM, NAND to run the model on their own hardware.

## Efficiency techniques, subsidies likely help lower pricing

Where Chinese models do have pricing/cost advantage is often not hardware-related. We estimate Chinese cost advantage in architectural efficiency (MoE sparsity, MLA/hybrid attention, native FP8/MXFP4 quantization, as well as up to 1.5-2x advantage in physical infra efficiency (lower Chinese electricity, labor, and land costs). Rest of the pricing differential could come from state-linked capital subsidies and cloud revenue/FCF at Chinese CSPs (Alibaba, Tencent, Baidu). Interestingly, Moonshot's Kimi K3 paused new subscriptions within just 48 hours of K3's launch, likely as GPU capacity ran out (or to cut costs/losses), and Xiaomi in May 2026 cut its MiMo model pricing by $99\%$ (likely unprofitable), likely as an effort to grab market share.

## CXMT not a threat, reit. MU Buy ahead of buyback resume

We reiterate Buy on MU with \$1,550 PO. While China-based CXMT is aggressively expanding capacity (now low-10% of global wafer capacity), we view limited competition in AI memory. CXMT primarily addresses the underserved consumer/commodity DRAM segment, not HBM3E/HBM4. It also remains unclear whether US OEMs will receive gov't approval to source from CXMT any time soon. Critically, MU's CHIPS Act buyback restrictions expire around Dec-26 (two years after the first funding tranche received Dec-24), opening the door to large-scale repurchases – given its \$120-130bn/yr+ FCF outlook over the next few years. A 40% payout policy would result in \~\$50-60bn/yr of buybacks, or \~5-6% of its \~\$1Tn market cap per year.

## 20 July 2026

Equity
United States
Semiconductors

Vivek Arya
Research Analyst
BofAS
vivek.arya@bofa.com

Duksan Jang
Research Analyst
BofAS
duksan.jang@bofa.com

Michael Mani
Research Analyst
BofAS
michael.mani@bofa.com

Liam Pharr
Research Analyst
BofAS
liam.pharr@bofa.com

CXMT: ChangXin Memory Technologies

## Contents

Memory is still critical in open models 3
Chinese models charge less, but may not cost much less 3
Open models continue to grow in weight size 4
Open models expand memory endpoints vs. closed 5
Scaling gains much faster than efficiency gains 6
China models create disruption but also expand market, beneficial for semis 8
Glossary: 9

## Memory is still critical in open models

## Chinese models charge less, but may not cost much less

Chinese open-model API pricing is very competitive. Latest Kimi K3 charges \$3/M input and \$15/M output vs. Claude Opus 4.8 and GPT-5.6 at roughly 5x that.

However, we flag API price is a business-model choice, not necessarily a hardware-cost readout. Kimi K3 still requires a 64+ accelerator super-node with \~1.4 TB of HBM per serving instance to run – that memory content is required whether Moonshot charges \$3 or \$30 per million tokens.

OpenAI's similar open model with MXFP4 native precision (for like-for-like compression) with 120B total parameters (23x smaller than Kimi K3) requires \~63GB of weight memory to run (22x smaller), in-line with the memory requirements of K3 if model sizes were the same.

Exhibit 1: Global token usage increased on average by +6% per week since 2025, or +9% per week since 2026, with China models accounting for \~70% of the tokens in July 2026
Weekly Token Usage by Major Models (API) via OpenRouter

![](images/56a1cd91cdde436cf45d5795d3beaa3e3d459c9343d93413888896e2da89fcf9.jpg)  
Source: BofA Global Research, OpenRouter  
BofA GLOBAL RESEARCH

## Cost advantage often comes from non-hardware efficiency

We suspect much of Chinese LLM cost advantages (up to 5-50x vs. western) actually come from non-hardware efficiencies.

## Architectural efficiency (2-3x)

\- Extreme MoE sparsity: Qwen3-Coder-Next activates just 3B of 80B total parameters (\~3.75%); Kimi K3 activates \~1.8%. Compute per decoded token in Chinese LLMs is a fraction of what a comparable dense model would need.

\- MLA/hybrid attention: DeepSeek's MLA and Kimi's KDA compress KV cache 10-90x vs. standard attention, so batch density is also much higher — more concurrent users per GPU.

\- Native low-bit quantization: Kimi K2 Thinking ships W4A16, K3 ships MXFP4, DeepSeek trains natively in FP8. That's another 2x throughput vs. FP16 of Meta Llama 4 or Google Gemma 4 open models.

Combined, net architectural efficiency could reach 2-3x per token vs. an equivalently sized Western model that ships in BF16/FP8 native, without these efficiency gains.

Input-side infrastructure cost (\~1.5-2x)

\- Chinese electricity: \~\$0.05-0.08/kWh vs. \~\$0.10-0.15/kWh in US hyperscaler zones

\- Chinese labor: Engineering salaries 40-60% lower than US equivalents

\- Land/real estate: Data center capex and related land/shell/power spend meaningfully lower in interior China (Ningxia, Guizhou)

Combined, net input-cost advantage could also reach 1.5-2x per token, depending on the underlying compute bill.

Competition, subsidies for market share

Lastly, we flag Moonshot AI paused new subscriptions within just 48 hours of K3's launch, because GPU capacity ran out or potentially just to cut costs/losses.

If K3's low price genuinely reflected proportional hardware savings, we expect Moonshot to have provisioned enough capacity. As such, actual hardware cost per query at Kimi K3 could be higher than the much cheaper API price implies, and Moonshot may be subsidizing to grab market share.

There are similar cases, such as Xiaomi cutting its MiMo model pricing by 99% in May 2026, likely as an effort to grab market share.

Exhibit 2: Open models continue to grow in weight size (i.e. memory), with their API input/output cost generally also increasing with the weight Key Open Models Pricing and Weight Memory

<table><tr><td>Model</td><td>Input $/M tokens</td><td>Output $/M tokens</td><td>Weight Memory (GB)</td><td>Input $/B tokens / Weight Memory (GB)</td><td>Access</td></tr><tr><td>Kimi K3</td><td>3</td><td>15</td><td>1400</td><td>$2.14</td><td>Open Weight</td></tr><tr><td>DeepSeek-V3.2</td><td>0.28</td><td>0.42</td><td>336</td><td>$0.83</td><td>Open Weight</td></tr><tr><td>DeepSeek-V4-Flash</td><td>0.14</td><td>0.28</td><td>142</td><td>$0.99</td><td>Open Weight</td></tr><tr><td>Qwen3-235B (Alibaba API)</td><td>0.5</td><td>1.5</td><td>118</td><td>$4.24</td><td>Open Weight</td></tr><tr><td>GLM-4.5 (Z.ai API)</td><td>0.6</td><td>2.2</td><td>178</td><td>$3.37</td><td>Open Weight</td></tr><tr><td>gpt-oss-120b (via provider)</td><td>0.15</td><td>0.6</td><td>63</td><td>$2.38</td><td>Open Weight</td></tr><tr><td>GPT-5.6 Sol</td><td>1.25</td><td>10</td><td>N/A - closed</td><td></td><td>Closed</td></tr><tr><td>Claude Opus 4.8</td><td>15</td><td>75</td><td>N/A - closed</td><td></td><td>Closed</td></tr><tr><td>Claude Sonnet 5</td><td>3</td><td>15</td><td>N/A - closed</td><td></td><td>Closed</td></tr><tr><td>Gemini 3 Pro</td><td>1.25</td><td>10</td><td>N/A - closed</td><td></td><td>Closed</td></tr><tr><td>Grok 4</td><td>3</td><td>15</td><td>N/A - closed</td><td></td><td>Closed</td></tr></table>

Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

## Open models continue to grow in weight size

Frontier open-weight model size continues to increase sharply (closed models often do not publish model weight data):

\- DeepSeek-V3 at 671B (Dec 2024)

\- Kimi K2 at 1T (mid-2025)

\- DeepSeek-V4-Pro at 1.6T (Apr 2026)

\- Kimi K3 at 2.8T parameters (Jul 16, 2026) — the largest open-weight model ever released

## Larger weights flow directly to memory demand.

In fact, the MIT Data Provenance audit documents a 17x increase in average open model size from 2019-2025. Even in native MXFP4 (4-bit), Kimi K3's weights now occupy \~1.4 TB and Moonshot's own guidance requires 64+ accelerators per serving instance.

Weight memory scales with total parameters (such as K3's 2.8T parameters), not active parameters.

Even with industry compression/quantization from FP8 to MXFP4 delivering a 2x saving, model sizes have grown \~4x more in parameter growth, more than offsetting the

efficiency gains from compression. For instance, Kimi K3 (July 2026) in native MXFP4 requires 2x the memory of DeepSeek-V3 in FP8 (December 2024).

## Active parameters reduce compute, not memory

With the use of MoE (i.e. using just active parameters), Kimi K3 activates only 16 of 896 experts at a time, i.e. it only activates 50B of its total 2.8T parameters per token. This greatly reduces the total compute requirement during the inference process.

However, the model still needs to keep nearly the entire expert pool (i.e. the entire model weight) resident in nearby memory. In fact, HBM capacity scales much more closely with total parameters, than with active parameters.

This is because MoE routers select experts dynamically per token, so every expert (i.e. total weight) must remain resident in fast memory regardless of activation sparsity. As a result, doubling total parameters requires double HBM per instance, which is why K3 needs 64+ accelerators while V3 needed just 8.

## Larger model weight drives multi-tier memory

Lastly, larger weights force multi-tier memory hierarchies: hot experts in HBM, inactive experts spilled to CPU LPDDR5X/DDR5, cold KV cache to enterprise NAND. Every tier gets more content per deployment.

Exhibit 3: Open MoE model total parameters and active parameters per token continue to scale upward, resulting in larger weight for memory storage
Open MoE models total parameters (bn) vs. active parameters per token (bn)  
![](images/4f3f13a508dbc5dd01a14cfde83c159c5c1485cb66474fa62500bd10424fc73a.jpg)  
Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

## Open models expand memory endpoints vs. closed

The mechanism is simple: a closed model has one deployment footprint; an open model has as many footprints as it has downloads.

For instance when OpenAI serves GPT-5.6 (closed model), the model weights live in a small number of Microsoft Azure data centers. Every user in the world — millions of them — hits that same shared HBM pool. Total memory content is set by peak concurrent demand across all users combined, and can be amortized because usage patterns diversify across time zones and workloads.

But when Moonshot releases Kimi K3 weights (open model), or DeepSeek releases V3, or OpenAI releases gpt-oss-120b, the weights get downloaded and loaded into memory on every buyer's own hardware. An enterprise running gpt-oss-120b needs its own 80 GB of HBM3E. A sovereign cloud running DeepSeek-V3 provisions its own 8× H200 cluster (\~1.1 TB of HBM). Moonshot's own guidance for K3 calls for 64+

accelerators per serving instance — and that footprint gets replicated by every enterprise, government, and cloud that downloads the weights. None of that memory would have been purchased if the same intelligence were only available through a closed API, because the customer would have rented compute cycles rather than owned the hardware.

As a result for open models, both model weights and KV cache must be resident in fast memory to serve inference — they cannot be shared across separately owned clusters. Unlike a shared API where 10,000 users effectively share one copy of the weights in HBM, 10,000 enterprises self-hosting the same open model means 10,000 copies of the weights loaded into 10,000 separate HBM pools. Each deployment also needs its own KV cache capacity scaled to its own user base — and at the 128K–1M context windows common in 2026, KV cache per active user session can exceed 40 GB, so this scales with concurrency on every endpoint independently.

## Memory endpoints benefit from cheaper API pricing

Open models having separate memory endpoints also benefit end memory deployment, as Chinese LLM labs charge cheaper API pricing and thus drive overall demand up. In other words:

\- Cheaper Chinese API pricing = more inference workload volume + more open-weight enterprise self-hosting + more memory sockets deployed globally.

While frontier model labs are spending capital to grab share, the market is likely expanding its aggregate compute and memory capacity in the process; and every enterprise that downloads Qwen, GLM, Hunyuan, or MiMo instead of paying for Claude Opus creates a new customer-side memory footprint that wouldn't exist in a pure closed-API world.

Overall, closed models consolidate memory demand; open models multiply it — and the compression from efficiency innovations doesn't offset multiplication by endpoint count.

## Scaling gains much faster than efficiency gains

Lastly, we highlight workload intensity and overall demand gained by Jevons Paradox are far greater than the efficiency gains from MoE, quantization, KV cache compression techniques.

Exhibit 4: Latest multi-agent workloads generate up to 200,000x more output tokens per query than traditional non-reasoning chat workloads (GPT-4o)
Tokens per query by different model workloads

![](images/12332ea2cdb096ef7d4ccb34c203cf6b0c52aa7a1b74e9bbd4921db378a220f0.jpg)  
Source: BofA Global Research estimates  
BofA GLOBAL RESEARCH

Exhibit 5: Newer releases of open models generally feature much larger total parameters, context windows, and weight memory gen-over-gen
List of key LLMs and their model weights

<table><tr><td>Model</td><td>Developer</td><td>Origin</td><td>Release</td><td>Openness Category</td><td>Architecture</td><td>Total Params</td><td>Context Window</td><td>Native Precision</td><td>Weight Memory (FP8, GB)</td><td>Weight Memory (4-bit, GB)</td></tr><tr><td>DeepSeek-V3.2</td><td>DeepSeek AI</td><td>China</td><td>Late 2025</td><td>Open Weight (permissive)</td><td>MoE</td><td>671B</td><td>128K</td><td>FP8</td><td>671</td><td>336</td></tr><tr><td>DeepSeek-V4-Pro</td><td>DeepSeek AI</td><td>China</td><td>Apr-26</td><td>Open Weight (permissive)</td><td>MoE</td><td>1.6T</td><td>1M</td><td>FP8</td><td>1600</td><td>800</td></tr><tr><td>Qwen3.6-35B-A3B</td><td>Alibaba</td><td>China</td><td>Apr-26</td><td>Open Weight (permissive)</td><td>MoE</td><td>35B</td><td>128K</td><td>BF16</td><td>35</td><td>16</td></tr><tr><td>Kimi K2</td>

[中间内容因长度限制已省略]

he extent this material discusses any legal proceeding or issues, it has not been prepared as nor is it intended to express any legal conclusion, opinion or advice. Investors should consult their own legal advisers as to issues of law relating to the subject matter of this material. BofA Global Research personnel's knowledge of legal proceedings in which any BofA entity and/or its directors, officers and

employees may be plaintiffs, defendants, co-defendants or co-plaintiffs with or involving issuers mentioned in this material is based on public information. Facts and views presented in this material that relate to any such proceedings have not been reviewed by, discussed with, and may not reflect information known to, professionals in other business areas of BofA in connection with the legal proceedings or matters relevant to such proceedings.

This information has been prepared independently of any issuer of securities mentioned herein and not in connection with any proposed offering of securities or as agent of any issuer of any securities. None of BofAS any of its affiliates or their research analysts has any authority whatsoever to make any representation or warranty on behalf of the issuer(s). BofA Global Research policy prohibits research personnel from disclosing a recommendation, investment rating, or investment thesis for review by an issuer prior to the publication of a research report containing such rating, recommendation or investment thesis.

Any information relating to sustainability in this material is limited as discussed herein and is not intended to provide a comprehensive view on any sustainability claim with respect to any issuer or security.

Any information relating to the tax status of financial instruments discussed herein is not intended to provide tax advice or to be used by anyone to provide tax advice. Investors are urged to seek tax advice based on their particular circumstances from an independent tax professional.

The information herein (other than disclosure information relating to BofA and its affiliates) was obtained from various sources and we do not guarantee its accuracy. This information may contain links to third-party websites. BofA is not responsible for the content of any third-party website or any linked content contained in a third-party website. Content

contained on such third-party websites is not part of this information and is not incorporated by reference. The inclusion of a link does not imply any endorsement by or any affiliation with BofA. Access to any third-party website is at your own risk, and you should always review the terms and privacy policies at third-party websites before submitting any personal information to them. BofA is not responsible for such terms and privacy policies and expressly disclaims any liability for them.

All opinions, projections and estimates constitute the judgment of the author as of the date of publication and are subject to change without notice. Prices also are subject to change without notice. BofA is under no obligation to update this information and BofA ability to publish information on the subject issuer(s) in the future is subject to applicable quiet periods. You should therefore assume that BofA will not update any fact, circumstance or opinion contained herein.

Subject to the quiet period applicable under laws of the various jurisdictions in which we distribute research reports and other legal and BofA policy-related restrictions on the publication of research reports, fundamental equity reports are produced on a regular basis as necessary to keep the investment recommendation current.

Certain outstanding reports or investment opinions relating to securities, financial instruments and/or issuers may no longer be current. Always refer to the most recent research report relating to an issuer prior to making an investment decision.

In some cases, an issuer may be classified as Restricted or may be Under Review or Extended Review. In each case, investors should consider any investment opinion relating to such issuer (or its security and/or financial instruments) to be suspended or withdrawn and should not rely on the analyses and investment opinion(s) pertaining to such issuer (or its securities and/or financial instruments) nor should the analyses or opinion(s) be considered a solicitation of any kind. Sales persons and financial advisors affiliated with BofAS or any of its affiliates may not solicit purchases of securities or financial instruments that are Restricted or Under Review and may only solicit securities under Extended Review in accordance with firm policies.

Neither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information.
"""
