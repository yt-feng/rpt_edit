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
<table><tr><td colspan="2">MS ASIA (SINGAPORE) PTE.+</td></tr><tr><td colspan="2">Mayank Maheshwari</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Mayank.Maheshwari@morganstanley.com</td><td>+65 6834-6719</td></tr><tr><td colspan="2">Ryan M Heng</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Ryan.Heng@morganstanley.com</td><td>+65 6834-6465</td></tr><tr><td colspan="2">Vivek Rajamani</td></tr><tr><td colspan="2">Equity Analyst</td></tr><tr><td>Vivek.Rajamani@morganstanley.com</td><td>+65 6834-6740</td></tr><tr><td colspan="2">MS INDIA COMPANY PRIVATE LIMITED+</td></tr><tr><td colspan="2">Pranitha Shetty</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Pranitha.Shetty@morganstanley.com</td><td>+91 22 6118-3022</td></tr><tr><td colspan="2">Hinal Choudhary</td></tr><tr><td colspan="2">Research Associate</td></tr><tr><td>Hinal.Choudhary@morganstanley.com</td><td>+91 22 6118-2044</td></tr></table>

July 6, 2026 01:00 PM GMT

Investor Presentation | Asia Pacific

## Asia Summer School: Power: Changing Face

In the age of electricity, Asia's power markets are becoming increasingly more dynamic, prompting policymakers to focus on securing energy supply chains. As these markets evolve, shifts in power economics, emerging fuel sources, and advances in energy storage technologies are reshaping the region's electricity landscape.

## See our notes:

• Asia Energy Security and AI: Energy Meets Compute: Supercycle Recharges

• Power: Changing Face with AI

Exhibit 1: Economics of power  
Round the Clock Power Generation Economics (UScents/kwh)  
![](images/3fc64b394ba16a2569500443f8f9704553b85341cfbefc549eb36780afe77bb4.jpg)  
Source: MS estimates.

![](images/f0468126a431a15a193f5c513ad95c4721678ec87349b882c584054663b39ef2.jpg)

MS does and seeks to do business with companies covered in MS. As a result, investors should be aware that the firm may have a conflict of interest that could affect the objectivity of MS. Investors should consider MS as only a single factor in making their investment decision.

For analyst certification and other important disclosures, refer to the Disclosure Section, located at the end of this report.

+= Analysts employed by non-U.S. affiliates are not registered with FINRA, may not be associated persons of the member and may not be subject to FINRA restrictions on communications with a subject company, public appearances and trading securities held by a research analyst account.

## Asia Summer School 2026

The Diffusion in Energy Markets  
![](images/baf938d94f2b934b50b8818e72a61712fc07695b00128741853b2d928f462cad.jpg)

![](images/820473c637827f1685c31004eafc76da90bf2ec5b18ada2d28feec05d06d47d3.jpg)

Structural themes and challenges will drive a paradigm shift and require a co-existence of oil, gas, renewables, and coal energy markets

Source: MS.

Asia's Age of Electricity in Perspective

## Global Power Demand is Inflecting

![](images/b4228e0fe4a0e0b216ee126d0159995db15716c9fa946c4fd76e32cc7be4a005.jpg)  
Source: IEA Energy Outlook 2025.

Need for Electricity as Energy Shocks Become More Frequent  
![](images/dc9cf1df9bd4cb6b4cb79eb00c67191fa0b8e682a27d8918358025f28d18b5eb.jpg)  
Since the 1970s, global events and energy crises have triggered a rise in emergency response and energy security policies worldwide  
Note: The analysis focuses on 85 countries, covering $93\%$ of global primary energy demand, $87\%$ of global oil demand and $95\%$ of global natural gas demand.  
Source: IEA Energy Outlook 2025.

## Asia's Energy Security Implementation vs Urgency Matrix

![](images/c09ffeef00c6352f011a2aae29a5e4475d7a2adc4ca6040dd50c07c990e32a49.jpg)  
Source: Statistical Review of World Energy, MS estimates.

## What's Driving the US\$5+trn Supercycle? Power Play

![](images/e4636efd97dd2c8287fd2cd0472392f8dbf6d3d2f9b7946f9959cf12024bda67.jpg)  
We estimate power to make up \~65% of Asia's energy security investment needs

Source: MS estimates.

## Energy Security & AI: The US\$9trn Value Creation Opportunity in Asia

![](images/7c41df733670bbefbe981ec357744bff553a41240e828163fa278dbce1063410.jpg)

We see a nearly 1.6x torque to the value creation, as US\$5trn+ in investments across the region ensure security of tech, AI, food, and energy supply chains, unlocking US\$9trn in value.

Source: MS estimates.

Learnings From Power Supply Chain Re-rating: Getting Broader Across Energy  
![](images/fd5d1ed7020a3577d60bae38c669c5796eef71b9d5578b4c7f0e1f56eaffa6db.jpg)  
Source: Refinitiv, MS.

Power supply chain has re-rated 20-50% in the past two years, as the consumption growth outlook has changed. The story widens to all dependable energy.

![](images/d0ae2fee11978f13841427d63698670b572cb9e59d18772d715760a88419947d.jpg)

![](images/6f981e6a5c9b6e372510d70efe8478c0ddc479b0a539b13c74a03f9ddc2eb556.jpg)

![](images/851fc32e372de9b775ee0c42ede46c6af08bcb3c5df7c8660992776407fa388e.jpg)  
nuclear and power grid deployment

![](images/74df88c933539d6fabc18dc99b55da77b139ea263013f3346703843c674b7d56.jpg)

## Energy Security Exposure Guide: Stacking up Power Supply Chain Exposure

![](images/2f830de4e5f43755908b7b13ca66c166c0e75eba3e27d77a42a334c248707244.jpg)

![](images/d50500ea2dea9041ed269eb18e98b59aba6430f3cb2af44ee697bacefc931c0b.jpg)

![](images/f94dc573db948709253ca3f3d51ac96fd34a00df3868c79bc9328881678763d7.jpg)

![](images/f9e4ad0c0d0519390a234c9ed1e667d7e4a224d28b362e4d68b17d77c5d18071.jpg)

![](images/bac9e54dbc9e5541efed027fa2ebd638dcb0ea9b3243877ff855a48027629413.jpg)

![](images/6bb8a29e3772636c6b982ce7f0995cb1edb04b6146f0ad415c23fe288e27d037.jpg)  
energy capex will double by 2030.

![](images/0a6ef59ae310692eceff93b927f11af7d85a85a5ccaae50f9c3882f46f0d6785.jpg)

![](images/da941b06a5181b11f3c541994a3b7f91bf898a7fc3bfaf823e33b770f9fdf802.jpg)

![](images/b0069bf79bd1d8cd570df203e367d123eb1ebedb75d4d7d0b9a24ea46d2c27bd.jpg)

![](images/8afe228ea18b41da0ebbcb2bf2de77603d9a1a637e8172432187fe55fb9da9d7.jpg)

![](images/9c7576b07a8637ad50a3addc90d60a467433ffd3a4d7122eef946119bc7db0d3.jpg)

![](images/f03f39321be840401a1a68391094043d7d3d79c06ab3f72372166a26ed807deb.jpg)

![](images/95b9030f203aa9fa65c2874f016d0a29add4457fb401f3e753a1a3ca9e574206.jpg)

![](images/c2d94d1100ed1ad01636ced7bd8c7eb126d7056b069767d30aba980f3b82df30.jpg)

![](images/ce943a2b3e4c5ea0aa9fe12fb14461cf73cbeede635394aa6afde2eaa3293e6d.jpg)

![](images/a850553a2ec5983eb8ee4a158bf5c094e61d07d6da4ebe5661c7b28b44e97a85.jpg)

![](images/df67fc25282b6f84e4c76df7beb6f1df9c209b53c3b8679e970fc0855de895ca.jpg)

![](images/895cb546c60668f245000b9d47dcf2c10cd8fb73183220cbf6db9c6b8a677b6a.jpg)

![](images/5b63f3d02b6d737f03695f4300c5048a47802d7284714a567d576c01a2c2bb36.jpg)

![](images/f4a554e9ecf146fa27468fc965ee33aa39bdd2ddc69cdd794b298893aa12b5ec.jpg)

![](images/734641117c2544fa6ba064a0fcfa341d1fb1fe4f7685dca0782d5dbcee4dc526.jpg)

![](images/a12a3aca65e30cd104764323d6a2830cb029730f61b786434300b095ecf8c395.jpg)

![](images/b15c4fafafe9ec67d73f973dd3dfc266d2a6b451206390ee87aba729f59bcbf6.jpg)

![](images/26b5af6fc626f8b21f4e0ea7de79920a3c22fb3645c012df879d8af7a9eba92c.jpg)

![](images/e2d0e5698c1f84aef37896e103d3c1fd65e3fd8aad772641ad6097e4d35c1ac4.jpg)

![](images/bb3aecb3471350e966a23fb2baf2a270df8bf16ae8267cbae502998ad2f07805.jpg)

![](images/8d24edf1e28eb8d74dc6aac621e34a918e9de404e530ec43df80d8f78172f451.jpg)

![](images/207f05307d23d3083e134f579e5509e18cd89f25bf8034c50fbba344e761350a.jpg)

![](images/4b5c43620baa33bcf0818cdf034d71613e0e116592070f4b3cc207c9d11b46df.jpg)

![](images/2fff0c6b8b92c475ba931a596118cfa89bf47f791c92115a5db993b7af1675f9.jpg)

![](images/7b7ddd9c48ea00b017467bd4fa6ffa93b937871e67b0ca220e81a64dee533310.jpg)

![](images/f1c851f7fb069be16dedc53661ad31a9be4523a4cc8c43afed07de62d586ae26.jpg)

![](images/9b327e6acc6817d110e2d68156fb577329835188c87b6f68db64585ba20e7bc8.jpg)

![](images/39ef93b0e1e5f123a7b8cbf4cc594f9cf676ded29f76b966cdfc202b8e61d402.jpg)  
Energy storage expands rapidly

![](images/95a816e1655fd2ef7b84745e4b5ad400f4111fc859b15a3a8a3275f32ac2b0c3.jpg)  
GanfengLithium EVEEnergy TIANQI LITHIUM

![](images/1a04128ca06583576a5e74423cad9de9400551acced71e2594476a17850a195d.jpg)

![](images/c6d1a1ef2374a54e55d65186576d0f0eee90e2982a71e2537520ed1f7e3ae250.jpg)

![](images/556be6ff8e06d420de7fdc5fffa4a06c935aaf815e666dfe234cc24413dfc798.jpg)

![](images/1d446d803357c112568f71cbdc05c1ce9e1dc0e38a8a2def7d9191b5fbf8951e.jpg)

![](images/b34a43bdda5c00cb7c9a0fb11f971ee082b04e1f92dc854548e6a49e36538a70.jpg)

![](images/af658193bccf65d47c40d1c67540cf919ed2b408a01ba7560356b36bfa097343.jpg)  
Sieyuan 中广核CGN

![](images/2071ac774bb134716829d11c67557775a14eb8569f6ac1fc6de45f622549e8cd.jpg)

![](images/5095cab65b39b39a76198a8ed4bedef78687809811aaba9e614756568780ed85.jpg)

![](images/d8c6afe89669458c6f28b3f6bf1a414f96ba5f6d9df9a969a1585dea45e3a690.jpg)

![](images/78203a2318a87ef9f700fbb20dd4b6146072e03927ad283945bd438133cd2c43.jpg)  
DOOSAN Enerbility

![](images/ed47dd1d8719f0966a298dd1f1608ab993a365df2dca3a3b31738cc588d23a55.jpg)

![](images/f760755783d538bec5643955fc3f18213ba7b83fb156594c68548ef7c9993dd0.jpg)

![](images/7af9a4de746f56ca01a1d6eff41522eabc39896f2d35b0269f25a4c763bdea84.jpg)

![](images/be5edddebef364cc84f84445264ed5edcded1fe9b80d60c73cc0526fdfc25181.jpg)  
Source: MS.

![](images/58a7d4238be93dcc9006c529eb2ed5d92bdc8e34cf254128ad66f3eb1f310542.jpg)

![](images/723b2e87b64e0871853854d24e76b12779b8fa5f587c72c1d2ce9d669d329777.jpg)

![](images/a8cc21b8d7a0fafa12af00e31e3af3a80115b7d2fd315470a1345dc18cd5fdc6.jpg)

![](images/7a2e706442a5e41d1364c23d5ab1961a747ac411a2dc9367aaede6c269d5444e.jpg)

![](images/eee1e83f63430de869d4e0c7134ce9a849ae72e30830712ec100e63e776be0c8.jpg)

Asia's Power Demand Keeps Growing

Power Demand Growth Expectations to 2030 CAGR  
Power Consumption Growth Expectations Have Consistently Been Revised Upwards  
![](images/3a91c2d261903453d68053646fbe7fabf5db1e824b2167998297ccf737cf8c00.jpg)  
Source: Statistical Review of World Energy, MS estimates.

Asia's Power Supply Mix: Fueling the Demand  
2025 Global Power Generation Mix  
![](images/7c031a68c67e06bf3b54e993e29912ca89e707f4ea51b63ad8de783d93ac6e83.jpg)

Weekly Token Demand is Rising Globally  
![](images/8722e6fccffcf3972835e4b521718181c21206793475da80f8530116451dc2a1.jpg)  
■ Top 6 - US models ■ Top 6 - Chinese model □ Out of top 6  
Source: OpenRouter, MS.

AI Requires a Lot More Energy  
![](images/987d9d788f0077ccc1b9b98b4fe35e8345ed952d7758fd9b38e5bb119bdc8846.jpg)

![](images/3024d6e569fb7434bc96c1e54819819e92bfe7e69bb63649af6fac1fbbb4dbd9.jpg)

A Lot More Power Investments Needed  
![](images/4a2557b632021d8afcbd218d50df07b753e58b8f4d729195510303cf563360c4.jpg)

Global AI data center capex is set to surpass investment in both power and oil & gas

Source: International Energy Agency; Organization of the Petroleum Exporting Countries, IMF Estimates, Epoch, OurWorldInData, MS.

Powering AI: Asia vs US vs Europe Data Center Power Demand  
![](images/5e77edddfdf9c5051793dfecf81ef0d643c9532a84a3bf092463cd4841b5a9ff.jpg)

Who's Adding DC Capacity in Asia: A Non-linear Growth in Need of DCs  
![](images/6a9bd2aa72ccbcb4fdcfe2dc7513a4fc601044a83311f0ac5c9a5816ec735126.jpg)  
China will drive a significant portion of data center growth in Asia, as inference demand and chip self sufficiency drive commoditization and faster commercialization  
Source: MS estimates.

US Power Supply Chain Constraints Also Help More AI Capacity in Asia  
![](images/8370202f032e85e1a2f2f593a7ae0576df2e2b231399e0900b63884949c713bf.jpg)  
We estimate \~9GW of potential power shortfall for US DCs factoring in suitable nuclear and fuel cell power with a possible 6GW spillover to Asia  
Source: MS estimates.

More Energy Storage & Grid Investments Needed

## Energy Storage Expands Rapidly, Even in Markets Outside of China

![](images/1a5f310481b681fbcfe371237ed936d60b6439b8fb22dfe2210877e5aee0651c.jpg)

## Power Grid Deployment Boom

![](images/8893dc3f385b2332a7f07e8116f8b5a9f2c71e281b38424b003656e7ca314d79.jpg)

The Return of Coal in Asia's Energy Mix

## Asia Imports More Than a Third of its Power Needs

<table><tr><td rowspan="2">Power Generation Resiliency (% of Total Generation)</td><td colspan="4">Imported</td><td colspan="5">Self Reliance</td></tr><tr><td>Coal</td><td>Natural Gas</td><td>Nuclear</td><td>Total Imports</td><td>Coal</td><td>Natural Gas</td><td>Nuclear</td><td>Renewables &amp; Others</td><td>Total Self Reliance</td></tr><tr><td>US</td><td>1%</td><td>2%</td><td>17%</td><td>20%</td><td>14%</td><td>38%</td><td>1%</td><td>27%</td><td>80%</td></tr><tr><td>Europe</td><td>7%</td><td>14%</td><td>19%</td><td>40%</td><td>2%</td><td>2%</td><td>2%</td><td>55%</td><td>60%</td></tr><tr><td>LATAM</td><td>1%</td><td>10%</td><td>NA</td><td>11%</td><td>1%</td><td>15%</td><td>2%</td><td>NA</td><td>18%</td></tr><tr><td>Middle East</td><td>0%</td><td>0%</td><td>NA</td><td>0%</td><td>0%</td><td>85%</td><td>5%</td><td>NA</td><td>90%</td></tr><tr><td>China</td><td>6%</td><td>1%</td><td>4%</td><td>11%</td><td>49%</td><td>2%</td><td>0%</td><td>38%</td><td>89%</td></tr><tr><td>India</td><td>3%</td><td>1%</td><td>3%</td><td>7%</td><td>66%</td><td>1%</td><td>0%</td><td>26%</td><td>93%</td></tr><tr><td>Japan</td><td>30%</td><td>34%</td><td>10%</td><td>74%</td><td>0%</td><td>0%</td><td>0%</td><td>26%</td><td>26%</td></tr><tr><td>Australia</td><td>0%</td><td>0%</td><td>NA</td><td>0%</td><td>44%</td><td>18%</td><td>0%</td><td>NA</td><td>61%</td></tr><tr><td>Singapore</td><td>NA</td><td>94%</td><td>NA</td><td>94%</td><td>NA</td><td>0%</td><td>0%</td><td>NA</td><td>0%</td></tr><tr><td>Malaysia</td><td>51%</td><td>12%</td><td>NA</td><td>63%</td><td>6%</td><td>28%</td><td>0%</td><td>NA</td><td>33%</td></tr><tr><td>Thailand</td><td>8%</td><td>21%</td><td>NA</td><td>29%</td><td>2%</td><td>38%</td><td>0%</td><td>NA</td><td>41%</td></tr><tr><td>Philippines</td><td>47%</td><td>8%</td><td>NA</td><td>54%</td><td>16%</td><td>9%</td><td>0%</td><td>NA</td><td>24%</td></tr><tr><td>South Korea</td><td>30%</td><td>29%</td><td>30%</td><td>88%</td><td>3%</td><td>2%</td><td>0%</td><td>7%</td><td>12%</td></tr><tr><td>Taiwan</td><td>29%</td><td>51%</td><td>1%</td><td>82%</td><td>0%</td><td>0%</td><td>0%</td><td>18%</td><td>18%</td></tr><tr><td>Vietnam</td><td>26%</td><td>7%</td><td>NA</td><td>33%</td><td>25%</td><td>3%</td><td>0%</td><td>NA</td><td>28%</td></tr></table>

Asia's needs for natural gas for the power sector should see a shift toward coal, energy storage, and dependable fuels

Source: MS estimates.

South-East Asia

## The Return of Coal to Secure AI's Need for Energy

## COAL and COAL GASIFICATION

Rising power demand, energy security concerns, and coal-to-gas substitution are driving a new coal investment cycle across Asia.

![](images/6fc6204fac88b56d6a5c4a7371695193a9f35a82da0b5481c3a3fbbf4f476a54.jpg)

We expect Asian markets to spend US\$318bn in coal investments, driven by higher power demand and coal-to-gas switching

Source: MS estimates.

## Comparing Power Generation Economics

Round the Clock Power Generation Economics (UScents/kwh)  
![](images/6f8e4b8650c96606e35afdbf350f62cd1f96ae0af5ed42a857ebce8b1ed9dfd3.jpg)

US shale revolution will be exported to Asia for the first time at scale in 2027, with repercussions across the powering AI and energy security thematics

Source: MS estimates.

## Diversification of Asia's Power Mix

Diversification of Energy Sourcing to the US & LatAm  
![](images/d9d53dbd8246bcabd72c54ddf67df5bd54d11101a2793972dae7876e8bac2bae.jpg)  
Source: MS estimates.

## The Supply Chain Shift: More US Energy for Power and Plastics

Asia's LNG Demand vs Global LNG Surplus/(shortage) (MTPA)  
![](images/5174e3aadc31cbd3eb6b31c833fd28ac1bc91487baba92f2b47e2a7dd5fb3e08.jpg)

US shale revolution will be exported to Asia for the fi

[中间内容因长度限制已省略]

etary Limited is a member of the JSE Limited and A2X (Pty) Ltd. RMB MS Proprietary Limited is a joint venture owned equally by MS International Holdings Inc. and RMB Investment Advisory (Proprietary) Limited, which is wholly owned by FirstRand Limited. The information in MS is being disseminated by MS Saudi Arabia, regulated by the Capital Market Authority in the Kingdom of Saudi Arabia, and is directed at Sophisticated investors only.

The information in MS is being communicated by MS & Co. International plc (DIFC Branch), regulated by the Dubai Financial Services Authority (the DFSA) or by MS & Co. International plc (ADGM Branch), regulated by the Financial Services Regulatory Authority Abu Dhabi (the FSRA), and is directed at Professional Clients only, as defined by the DFSA or the FSRA, respectively. The financial products or financial services to which this research relates will only be made available to a customer who we are satisfied meets the regulatory criteria of a Professional Client. A distribution of the different MS Research ratings or recommendations, in percentage terms for Investments in each sector covered, is available upon request from your sales representative.

The information in MS is being communicated by MS & Co. International plc (QFC Branch), regulated by the Qatar Financial Centre Regulatory Authority (the QFCRA), and is directed at business customers and market counterparties only and is not intended for Retail Customers as defined by the QFCRA.

As required by the Capital Markets Board of Turkey, investment information, comments and recommendations stated here, are not within the scope of investment advisory activity. Investment advisory service is provided exclusively to persons based on their risk and income preferences by the authorized firms. Comments and recommendations stated here are general in nature. These opinions may not fit to your financial status, risk and return preferences. For this reason, to make an investment decision by relying solely to this information stated here may not bring about outcomes that fit your expectations.

The trademarks and service marks contained in MS are the property of their respective owners. Third-party data providers make no warranties or representations relating to the accuracy, completeness, or timeliness of the data they provide and shall not have liability for any damages relating to such data. The Global Industry Classification Standard (GICS) was developed by and is the exclusive property of MSCI and S&P.

MS, or any portion thereof may not be reprinted, sold or redistributed without the written consent of MS.

Indicators and trackers referenced in MS may not be used as, or treated as, a benchmark under Regulation EU 2016/1011, or any other similar framework.

The issuers and/or fixed income products recommended or discussed in certain fixed income research reports may not be continuously followed. Accordingly, investors should regard those fixed income research reports as providing stand-alone analysis and should not expect continuing analysis or additional reports relating to such issuers and/or individual fixed income products.

MS may hold, from time to time, material financial and commercial interests regarding the company subject to the Research report.

Registration granted by SEBI and certification from the National Institute of Securities Markets (NISM) in no way guarantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.

## INDUSTRY COVERAGE: ASEAN Utilities and Infrastructure

<table><tr><td>COMPANY (TICKER)</td><td>RATING (AS OF)</td><td>PRICE* (07/06/2026)</td></tr><tr><td>Mayank Maheshwari</td><td></td><td></td></tr><tr><td>Global Power Synergy PCL (GPSC.BK)</td><td>U (09/12/2025)</td><td>Bt46.75</td></tr><tr><td>Gulf Development PCL (GULF.BK)</td><td>O (03/26/2025)</td><td>Bt63.50</td></tr><tr><td>Manila Electric Company (MER.PS)</td><td>O (06/20/2022)</td><td>PP579.50</td></tr><tr><td>Perusahaan Gas Negara (PGAS.JK)</td><td>E (06/18/2026)</td><td>Rp1,390</td></tr><tr><td>SembCorp Industries Ltd (SCIL.SI)</td><td>O (03/23/2026)</td><td>S$5.98</td></tr><tr><td>Tenaga Nasional (TENA.KL)</td><td>O (09/12/2023)</td><td>RM14.28</td></tr><tr><td colspan="3">Ryan M Heng</td></tr><tr><td>Airports of Thailand (AOT.BK)</td><td>O (08/25/2021)</td><td>Bt64.25</td></tr><tr><td>International Container Terminal Service (ICT.PS)</td><td>O (03/04/2024)</td><td>PP894.50</td></tr><tr><td>Maynilad Water Services, Inc. (MYNLD.PS)</td><td>E (06/30/2026)</td><td>PP20.50</td></tr></table>

Stock Ratings are subject to change. Please see latest research for each company.  
\* Historical prices are not split adjusted.

## © 2026 MS
"""
