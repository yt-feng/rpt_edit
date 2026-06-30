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
- `# 标题` 必须短、锐利、可转发，优先 18-30 个中文字符，最长不超过 36 个中文字符。
- `# 标题` 必须直接表达一个判断或悬念，例如“黄金缺的不是央行，是ETF”。
- `# 标题` 必须包含一个传播钩子，但只能用报告中真实出现或可由报告标题明确推出的信息：
  1. 机构 big name：GS、MS、JPM、UBS、Citi、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`HSBC`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、MS、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
- 标题里不要同时写中文机构名和英文缩写，禁止“JPM：JPM：……”“GS：GS：……”这类重复；写“JPM：……”或“GS：……”即可。
- 标题可以用问句或对比句，但不要标题党到超出原报告证据。避免“震惊”“爆了”“彻底反转”“一夜变天”等廉价词。
- 标题不要晦涩抽象。少用“结构性分化”“二阶影响”“再定价框架”这类泛化词；如果必须使用，要落到一个具体对象。
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
1. `# 标题`：机构中文名或报告中的 big name + 一句主判断，不超过 36 字。
2. 开头 4-6 段：直接给出主判断、为什么现在重要、报告提供了什么新信号。
3. 4-6 个 `##` 小节：每个小节标题都是洞察句，不是栏目名。
4. 在正文中穿插 2-4 个 `> **KC评论：** ...` 引用块，每个 1-3 句，用更平白的话解释“这张图/这个判断对读者意味着什么”，并自然引出读完整报告的必要性。
5. 至少一个小节讨论“报告尚未完全回答的关键问题”，但标题也要是洞察句。
6. 至少一个小节给出读者的观察框架，但不要命名为“对读者的启发”。
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：每天由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新约 10-40 页，并整理当天最新数据图表合集，方便喂给 AI，也方便人工快速把握 market dynamics。欢迎来星球微信群里继续讨论。。
8. 在免责声明前，单独插入这张图片链接：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`
9. 结尾只输出英文灰色免责声明：`<p style="color:#999999;font-size:12px;">Personal reading notes and learning share only. Not investment advice.</p>`

【hook 要求】
- 不要硬插“加入社群”。
- hook 应该来自正文自然出现的未解问题，比如：关键假设尚未验证、竞争优势仍需拆解、图表背后的二阶影响没有展开。
- 文末 CTA 要像“顺着这些未解问题继续读完整报告/继续讨论”，不是广告口吻。
- CTA 必须每篇重新写，不能固定输出“加入社群，领取完整研报解读与原始图表”。它需要自然提到：每天会由 AI agent + 人工 review 生成国际投行中文摘要与 KC评论，daily 更新，约 10-40 页，也包含当天最新数据图表合集，既方便喂给 AI，也方便人工快速把握 market dynamics。

【KC评论要求】
- `KC评论` 不是复述原文，而是读者友好的解释、提醒或追问。
- 每条 `KC评论` 先说白话结论，再点出完整报告里值得继续看的图表、假设或细分拆解。
- 语气可以有判断力，但不要编造报告没有的数据或结论。

【图片要求】
- 不要主动生成 MinerU 图片 markdown；系统会在文章生成后自动插入 MinerU 原始图片。
- 但文末免责声明前必须保留知识星球图片：`![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)`。

【内容边界】
- 只能基于研报原文和解析结果推导，不要编造数据、公司动作、引用。
- 遇到不确定内容，要用“这里仍需验证”“报告没有完全展开”等表达。
- 避免“震惊”“爆款”“一文看懂”等浮夸表达。
- 不要出现小红书话题标签。
- 不要出现 emoji。
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份HSBC研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
By: Janet Henry, James Pomeroy and Bethan Ellis

Q3 2026 www.research.hsbc.com

# Global Economics

Crosscurrents

Policymakers will welcome the lower oil prices, which have curbed some of the risks to growth and inflation...

...but there are other powerful forces at play, the effects of which will be uneven around the world...

...with AI playing a key role, as well as El Niño effects on food, and risks around securing a final US-Iran deal

![](images/9ee7b720aca570fef93a1978025fbb10e859591f15744fd9ad5846d0c5600b48.jpg)

Play video with Janet Henry

Disclosures & Disclaimer: This report must be read with the disclosures and the analyst certifications in the Disclosure appendix, and with the Disclaimer, which forms part of it.

# Executive summary

## Ceasefire extended, lower oil, but what about a final deal?

The signing by the US and Iran of a Memorandum of Understanding (MoU) to extend the ceasefire and lay a framework for future nuclear negotiations leaves many important questions unanswered. Material risks persist. Even assuming the US-Iran talks on the nuclear programme and other sticking points proceed as planned, it is far from clear what the new normal in the Strait of Hormuz will look like. Already Iran has indicated there will be no return to the pre-war status quo.

## Energy prices have fallen

Nonetheless, the rapid drop in the Brent oil price to around USD80/b in response to the 60-day ceasefire extension and the commitment to re-open the Strait – assuming it is sustainable – would limit the downside risks to growth and limit some of the upside risks to inflation and be in line with our central case scenario for the global economy. We have been assuming that Hormuz traffic and Gulf output would gradually restart in June, and a return to near-normal system-level production and flows would occur by end-Q3 2026.

## Crosscurrents

The pace at which the Strait re-opens will not be the sole influence on the global economy in 2026-27, even if it is the single biggest one. There are also other powerful forces moving in different directions at the very same time, which could have very uneven effects: in particular the AI-related export and investment boom which we discuss on pages 24-32 and the risks to agricultural output and prices from severe El Niño weather conditions which we examine on pages 33-39. Fiscal policy will also have varying impacts on the growth trajectory in 2026-27.

## Consumer spending to soften...

In terms of the economic implications of the supply shock from the Middle East so far, the clearest impact has been an auto-fuel-driven rise in headline inflation and higher input costs, whether from crude, diesel, jet fuel and various gas derivatives for which prices, while off their highs, are still 30% or so higher than pre-conflict levels.

This has all hit confidence and squeezed margins and disposable incomes, though the impact on the limited available consumer data for Q2 suggests no sharp downturn. In the major economies we are so far seeing a familiar pattern of sluggish spending by households in China, weighed down by the ongoing property sector headwinds and limited employment prospects, and ongoing resilience in the US, where the income squeeze has been offset by higher tax rebates and ongoing wealth effects from the surge in tech prices.

Globally, consumer spending appears set to soften further over the next couple of quarters given the squeeze on real wages and, for those reliant on credit, tighter financial conditions even as some areas of investment – particularly AI, but also increasingly energy infrastructure spending – hold up well.

## ...and, El Niño means food prices are still a big risk

Falling pump prices have mostly stabilised consumer and business confidence at a low level, but the risks surrounding food price inflation persist. Diesel costs have already hindered agricultural output in parts of Asia and future harvests in some economies will be affected by lower yields as the planting season was hit by the sharp rise in fertiliser and diesel prices in March and April.

There will still be some lagged effects, but now the potential food inflation story stems from the severe El Niño weather phenomenon, which has the potential to push up inflation materially in H2 2026 and into 2027 in many emerging economies, including the likes of India and Brazil. Even less-exposed advanced economies could be affected by the higher imported food prices as well as higher packaging costs given plastic prices.

## AI surge is potentially huge but uneven...

More positively from a growth perspective, if the energy price shock now fades, as the markets seem to be assuming, the AI boom is set to continue. The relative impacts of the capex, industrial production, export, profits and wealth effects between economies will vary enormously, though there might be scope for usage growth to become more widespread in the coming years.

GDP in Taiwan and the US is set to continue to be lifted the most from the AI boom, but other exporters will too. The enormous investment in the whole AI ecosystem that has continued to drive world trade growth even against a backdrop of tariffs, bilateral trade frictions, and an enormous supply shock. Our forecasts show slower, but still positive, growth in exports for most countries and a clear electronics-driven divide between Asia and the rest of the world. The impact of AI on consumer spending is set to be uneven, though, with big variations across age and income cohorts too.

## ...and poses other cost shocks in the coming year

Currently, the inflation risks of AI stem more from the enormous investment in the whole AI ecosystem that has continued to drive world trade growth even against a backdrop of tariffs, bilateral trade frictions, and an enormous supply shock.

Some of the inflation risks stemming from the AI boom could be more widespread. The sheer scale of AI construction and capex underway means many policymakers perceive that the demand-side effects on inflation might be more immediate than the supply-side effects on productivity and labour markets. The cost of construction from copper wiring to memory chip prices barely paused for breath at even the height of the disruption in April. Apple CEO Tim Cook stated in mid-June that soaring component costs have made price increases “unavoidable $^{1}$ ”.

Even assuming a full re-opening of the Strait by the end of Q3, not all inflation risks will fade as swiftly as the oil price fell in mid-June.

## Pressure on central banks, and maybe governments, could ease

Under our central scenario, the gradual re-opening of the Strait and the fall in crude oil prices should ease some of the demands on fiscal policy in the coming months.

In some economies, domestic demand should still be supported by the pre-war fiscal stimulus that had already been announced or delivered, notably in the US. But in many places, there has been a clear effort to contain gasoline price increases through either price controls or a temporary downside adjustment to fuel taxes, both to reduce the income squeeze from higher energy prices on consumers, and to limit the scope for inflation and interest rates to rise.

Assuming the drop in oil prices is sustained or extends further, the cost of such subsidies should ease somewhat. As every region of the world starts from a position where budget deficits and debts are larger and structural spending demands on defence, age-related spending and the energy transition are set to rise more sharply, any relief governments may get from lower inflation-linked spending and borrowing costs would certainly be welcome.

The different forces discussed in this report will also have an impact on FX. Since global oil and gas supplies started to be disrupted at end-February, the US energy surplus and safe-haven status have supported USD vis-à-vis all energy importers, excluding China. Our FX team forecasts that US growth exceptionalism, and a greater likelihood of a Fed rate rise than a cut this year, means USD should firm further vs most currencies (A new sheriff in town 18 June 2026).

So, whereas the implications of the fall in oil prices for inflation means we now think the ECB will not raise rates again and the BoE will not hike at all. Unlike the market, we think they could both cut in 2027, but we still believe several Asian economies will likely be under pressure to raise rates further in the second half of this year. In Latin America, we forecast an extended pause in Mexico and Brazil.

## Forecasts: the good and the ugly

Pulling all of these forces together, this year's global growth forecast of $2.5\%$ – the weakest pace since the pandemic – is unchanged, as is our 2027 forecast of $2.7\%$ , although that masks sizeable revisions to some economies.

As explained in Running out of gas?, March 2026, there is no winner from the big supply shock that was inflicted on the world by the conflict, but there are always relative winners and relative losers. As with 2026, the most notable upgrade to our 2027 forecast is to the US while the biggest downgrades are to the likes of India and Brazil, reflecting a weaker carryover from H2 2026 when both lagged effects of the energy shock and an anticipated impact from El Niño are set to weigh on the growth outlook.

Even with the drop in the oil price and our assumption that it will average USD75/b by H2 2027, the revisions to our inflation forecasts are upwards for both 2026 and 2027, driven almost entirely by the emerging world, notably across Asia.

In our ‘uglier’ scenario, based on a partial re-opening, whereby less than half of the pre-conflict crude oil passes through the Strait, the oil market would remain in deficit, reserves would continue to run down and prices edge higher over the next six months, potentially to USD140-150/b. Inevitably, the growth numbers would be much lower, particularly in the energy importers, although we would expect investment in alternative energy sources and bypass pipelines to be stepped up and the global AI investment story would not be derailed.

Inflation forecasts would be higher given the enormous array of products that would be affected, and we would expect monetary policy to be tightened more aggressively, pushing some economies into outright recession.

## Key forecasts

<table><tr><td rowspan="2">% Year</td><td colspan="6">GDP</td><td colspan="6">Inflation</td></tr><tr><td colspan="2">2025</td><td colspan="2">2026f</td><td colspan="2">2027f</td><td colspan="2">2025</td><td colspan="2">2026f</td><td colspan="2">2027f</td></tr><tr><td>World</td><td>2.8</td><td>(2.8)</td><td>2.5</td><td>(2.5)</td><td>2.7</td><td>(2.7)</td><td>3.1</td><td>(3.1)</td><td>3.8</td><td>(3.5)</td><td>3.1</td><td>(2.8)</td></tr><tr><td>Advanced</td><td>1.9</td><td>(1.9)</td><td>1.6</td><td>(1.6)</td><td>1.7</td><td>(1.6)</td><td>2.5</td><td>(2.5)</td><td>2.9</td><td>(2.9)</td><td>2.5</td><td>(2.3)</td></tr><tr><td>Emerging</td><td>4.5</td><td>(4.4)</td><td>4.0</td><td>(4.1)</td><td>4.3</td><td>(4.3)</td><td>3.6</td><td>(3.7)</td><td>4.4</td><td>(4.0)</td><td>3.5</td><td>(3.1)</td></tr><tr><td>US</td><td>2.1</td><td>(2.1)</td><td>2.3</td><td>(2.1)</td><td>2.3</td><td>(2.0)</td><td>2.7</td><td>(2.7)</td><td>3.3</td><td>(3.2)</td><td>2.7</td><td>(2.6)</td></tr><tr><td>US (Q4/Q4)</td><td>2.0</td><td>(2.0)</td><td>2.3</td><td>(1.9)</td><td>2.4</td><td>(2.0)</td><td>2.7</td><td>(2.7)</td><td>3.3</td><td>(3.1)</td><td>2.7</td><td>(2.7)</td></tr><tr><td>Mainland China</td><td>5.0</td><td>(5.0)</td><td>4.6</td><td>(4.6)</td><td>4.7</td><td>(4.7)</td><td>0.0</td><td>(0.0)</td><td>0.9</td><td>(0.9)</td><td>1.0</td><td>(0.8)</td></tr><tr><td>Japan</td><td>1.1</td><td>(1.2)</td><td>0.7</td><td>(0.7)</td><td>1.0</td><td>(1.0)</td><td>3.2</td><td>(3.2)</td><td>2.5</td><td>(2.2)</td><td>2.3</td><td>(1.7)</td></tr><tr><td>India*</td><td>7.5</td><td>(7.5)</td><td>6.8</td><td>(6.3)</td><td>6.4</td><td>(6.8)</td><td>2.0</td><td>(2.0)</td><td>5.1</td><td>(4.5)</td><td>4.6</td><td>(4.3)</td></tr><tr><td>ASEAN-6</td><td>5.0</td><td>(5.0)</td><td>4.2</td><td>(4.2)</td><td>4.3</td><td>(4.5)</td><td>1.6</td><td>(1.6)</td><td>3.7</td><td>(3.0)</td><td>3.0</td><td>(2.7)</td></tr><tr><td>Eurozone</td><td>1.5</td><td>(1.5)</td><td>0.3</td><td>(0.7)</td><td>0.9</td><td>(1.1)</td><td>2.1</td><td>(2.1)</td><td>2.9</td><td>(2.9)</td><td>2.2</td><td>(2.1)</td></tr><tr><td>UK</td><td>1.4</td><td>(1.3)</td><td>1.1</td><td>(0.8)</td><td>1.0</td><td>(1.2)</td><td>3.4</td><td>(3.4)</td><td>3.1</td><td>(2.9)</td><td>2.9</td><td>(2.6)</td></tr><tr><td>Brazil</td><td>2.3</td><td>(2.3)</td><td>2.0</td><td>(2.0)</td><td>1.7</td><td>(2.2)</td><td>5.1</td><td>(5.1)</td><td>4.8</td><td>(4.0)</td><td>4.7</td><td>(4.1)</td></tr><tr><td>Mexico</td><td>0.6</td><td>(0.6)</td><td>1.0</td><td>(1.5)</td><td>2.0</td><td>(2.0)</td><td>3.8</td><td>(3.8)</td><td>4.2</td><td>(4.3)</td><td>4.2</td><td>(4.4)</td></tr></table>

Source: HSBC Economics, Bloomberg. Note: \*India data is calendar year forecast here for comparability. GDP aggregates use chain nominal GDP (USD) weights and inflation aggregates calculated using GDP PPP (USD) weights. Parenthesis show forecasts from the Global Economics Quarterly Q2 2026. We have adjusted the mix of economies in our advanced and emerging economy aggregates in alignment with IMF definitions

## Contents

Executive summary 2
Key forecasts 6
Crosscurrents 7
Global economic forecasts 40
GDP 41
Consumer prices 43
Policy rates 45
Exchange rates vs USD 46
Exchange rate vs EUR & GBP 47
Consumer spending 48
Investment spending 49
Exports 50
Industrial production 51
Wage growth 52
Budget balance 53
Current account 54
North America 56
US 56
Canada 58
Asia Pacific 60
Mainland China 60
Japan 62
India 64
Australia 66
South Korea 68
Indonesia 70
Taiwan 72
Thailand 74
Malaysia 76
Singapore 78
Hong Kong 80
Philippines 82

Vietnam 84  
New Zealand 86  
Eurozone 88  
Eurozone 88  
Germany 90  
France 92  
Italy 94  
Spain 96  
Other Western Europe 98  
UK 98  
Switzerland 100  
Sweden 102  
Norway 104  
CEEMEA 106  
Poland 106  
Russia 108  
Türkiye 110  
Saudi Arabia 112  
South Africa 114  
Latin America 116  
Brazil 116  
Mexico 118  
Argentina 120  
Colombia 122  
Chile 124  
Disclosure appendix 126  
Disclaimer 128

## Key forecasts

Key forecasts under base and 'ugly' scenarios

<table><tr><td rowspan="3">% Year</td><td colspan="6">Central forecast (best case scenario)</td><td colspan="6">&#x27;Ugly&#x27; scenario</td></tr><tr><td colspan="2">GDP</td><td colspan="2">Inflation</td><td colspan="2">Policy rate*</td><td colspan="2">GDP</td><td colspan="2">Inflation</td><td colspan="2">Policy rate*</td></tr><tr><td>2026</td><td>2027</td><td>2026</td><td>2027</td><td>2026</td><td>2027</td><td>2026</td><td>2027</td><td>2026</td><td>2027</td><td>2026</td><td>2027</td></tr><tr><td>World (nominal weights)</td><td>2.5</td><td>2.7</td><td>3.8</td><td>3.1</td><td>-</td><td>-</td><td>2.1</td><td>2.1</td><td>4.5</td><td>4.4</td><td>-</td><td>-</td></tr><tr><td>Advanced</td><td>1.6</td><td>1.7</td><td>2.9</td><td>2.5</td><td>-</td><td>-</td><td>1.4</td><td>1.1</td><td>3.4</td><td>3.5</td><td>-</td><td>-</td></tr><tr><td>Emerging</td><td>4.0</td><td>4.3</td><td>4.4</td><td>3.5</td><td>-</td><td>-</td><td>3.4</td><td>3.7</td><td>5.3</td><td>5.1</td><td>-</td><td>-</td></tr><tr><td>North America</td><td>2.2</td><td>2.2</td><td>3.2</td><td>2.7</td><td>-</td><td>-</td><td>2.1</td><td>2.0</td><td>3.6</td><td>3.5</td><td>-</td><td>-</td></tr><tr><td>US</td><td>2.3</td><td>2.3</td><td>3.3</td><td>2.7</td><td>3.625</td><td>3.625</td><td>2.2</td><td>2.1</td><td>3.6</td><td>3.5</td><td>3.875</td><td>3.875</td></tr><tr><td>Canada</td><td>0.9</td><td>1.4</td><td>2.5</td><td>2.4</td><td>2.25</td><td>2.25</td><td>0.5</td><td>0.9</td><td>3.5</td><td>2.9</td><td>2.50</td><td>2.75</td></tr><tr><td>Asia-Pacific</td><td>4.2</td><td>4.1</td><td>2.5</td><td>2.2</td><td>-</td><td>-</td><td>3.5</td><td>3.4</td><td>3.4</td><td>3.7</td><td>-</td><td>-</td></tr><tr><td>Asia ex-Japan</td><td>4.7</td><td>4.5</td><td>2.5</td><td>2.2</td><td>-</td><td>-</td><td>3.9</td><td>3.8</td><td>3.4</td><td>3.8</td><td>-</td><td>-</td></tr><tr><td>Asia Big Three</td><td>4.4</td><td>4.4</td><td>2.2</td><td>2.1</td><td>-</td><td>-</td><td>3.6</td><td>3.8</td><td>3.1</td><td>3.8</td><td>-</td><td>-</td></tr><tr><td>Mainland China</td><td>4.6</td><td>4.7</td><td>0.9</td><td>1.0</td><td>1.40</td><td>1.40</td><td>4.0</td><td>4.2</td><td>1.6</td><td>2.6</td><td>1.40</td><td>1.40</td></tr><tr><td>Japan</td><td>0.7</td><td>1.0</td><td>2.5</td><td>2.3</td><td>1.25</td><td>1.25</td><td>0.2</td><td>0.4</td><td>3.0</td><td>2.9</td><td>1.25</td><td>1.50</td></tr><tr><td>India**</td><td>6.3</td><td>6.6</td><td>5.1</td><td>4.6</td><td>5.75</td><td>5.75</td><td>5.4</td><td>5.4</td><td>6.6</td><td>6.7</td><td>5.75</td><td>6.25</td></tr><tr><td>Asia ex Big Three</td><td>3.9</td><td>3.2</td><td>3.4</td><td>2.7</td><td>-</td><td>-</td><td>3.0</td><td>2.3</td><td>4.3</td><td>3.6</td><td>-</td><td>-</td></tr><tr><td>Australia</td><td>1.5</td><td>1.0</td><td>4.3</td><td>2.5</td><td>4.35</td><td>3.85</td><td>1.1</td><td>0.6</td><td>5.2</td><td>2.7</td><td>4.60</td><td>3.35</td></tr><tr><td>South Korea</td><td>2.8</td><td>2.0</td><td>2.8</td><td>2.3</td><td>3.00</td><td>3.00</td><td>2.2</td><td>1.1</td><td>3.3</td><td>2.5</td><td>3.25</td><td>3.00</td></tr><tr><td>Indonesia</td><td>4.7</td><td>4.9</td><td>3.5</td><td>3.0</td><td>6.00</td><td>5.50</td><td>4.1</td><td>4.1</td><td>4.6</td><td>4.6</td><td>6.25</td><td>6.00</td></tr><tr><td>Taiwan</td><td>10.2</td><td>5.3</td><td>2.0</td><td>2.0</td><td>2.125</td><td>2.125</td><td>7.8</td><td>3.5</td><td>2.1</td><td>2.0</td><td>2.250</td><td>2.250</td></tr><tr><td>Thailand</td><td>2.2</td><td>1.7</td><td>2.7</td><td>2.1</td><td>1.00</td><td>1.00</td><td>1.0</td><td>-0.1</td><td>4.9</td><td>4.3</td><td>1.00</td><td>1.50</td></tr><tr><td>Malaysia</td><td>4.5</td><td>4.7</td><td>2.5</td><td>2.7</td><td>2.75</td><td>2.75</td><td>4.0</td><td>4.2</td><td>2.8</td><td>2.7</td><td>3.00</td><td>3.00</td></tr><tr><td>Singapore</td><td>3.3</td><td>2.5</td><td>2.2</td><td>2.2</td><td>1.50</td><td>1.50</td><td>1.9</td><td>1.4</td><td>3.0</td><td>3.2</td><td>2.00</td><td>2.00</td></tr><tr><td>Hong Kong</td><td>3.8</td><td>3.0</td><td>2.0</td><td>1.9</td><td>4.00</td><td>4.00</td><td>3.4</td><td>2.8</td><td>2.3</td><td>2.4</td><td>4.25</td><td>4.25</td></tr><tr><td>Philippines</td><td>3.4</td><td>4.8</td><td>6.2</td><td>4.3</td><td>5.50</td><td>5.00</td><td>2.5</td><td>3.4</td><td>7.2</td><td>5.2</td><td>6.00</td><td>6.00</td></tr><tr><td>Vietnam</td><td>6.5</td><td>6.5</td

[中间内容因长度限制已省略]

) the analyst(s) responsible for authoring this report are stated on the chart above labelled "HSBC & Analyst Disclosures".

The document is intended to be distributed in its entirety. Unless governing law permits otherwise, you must contact a HSBC Group member in your home jurisdiction if you wish to use HSBC Group services in effecting a transaction in any investment mentioned in this document. HSBC Bank plc is registered in England No 14259, is authorised by the Prudential Regulation Authority and regulated by the Financial Conduct Authority and the Prudential Regulation Authority and is a member of the London Stock Exchange.

If you are a customer of HSBC International Wealth & Premier Banking ("IWPB"), including HSBC Private Bank, you are eligible to receive this publication only if: (i) you have been approved to receive relevant research publications by an applicable HSBC legal entity; (ii) you have agreed to the applicable HSBC entity's terms and conditions and/or customer declaration for accessing research; and (iii) you have agreed to the terms and conditions of any other internet banking, online banking, mobile banking and/or investment services offered by that HSBC entity, through which you will access research publications (collectively with (ii), the "Terms"). If you do not meet the above eligibility requirements, please disregard this publication and, if you are a IWPB customer, please notify your Relationship Manager or call the relevant customer hotline. Distribution of this publication is the sole responsibility of the HSBC entity with whom you have agreed the Terms. Receipt of research publications is strictly subject to the Terms and any other conditions or disclaimers applicable to the provision of the publications that may be advised by IWPB. © Copyright 2026, HSBC Bank plc, ALL RIGHTS RESERVED. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Bank plc.

## Main contributors

![](images/2a68af9f2bb1c4218c3b12586ce6b10ff0d05ad6eec73a726b219b4fa49b112f.jpg)

## Janet Henry

Global Chief Economist

HSBC Bank plc

janet.henry@hsbcib.com

+44 20 7991 6711

![](images/5e07ad1edc01d38a77646bd1c5fb37c76fed8e98deabff1501c384f73fdd662f.jpg)

## James Pomeroy

Global Economist
HSBC Bank plc
james.pomeroy@hsbc.com
+44 20 7991 6714

![](images/9697713411dd33a77fa7de32b77d58661bdda5700efa595159a4cb4ca89c39c7.jpg)

## Bethan Ellis

Global Economist
HSBC Bank plc
bethan.ellis@hsbc.com
+44 20 7991 6714

Janet Henry was appointed as HSBC's Global Chief Economist in August 2015 and is responsible for all of HSBC's economic forecasts and thematic economic research output globally. She was previously HSBC's Chief European Economist. Since the COVID-19 pandemic, her work has focused on the labour market implications, evolving inflation dynamics and policy challenges in a world facing geopolitical tensions, protectionism, new innovations and enormous demographic and climate challenges. Janet is a Governor of the UK's National Institute of Economic and Social Research, a member of the World Economic Forum's Chief Economists Community and a Non-Executive Director of HSBC Bank UK plc. She has given evidence to the financial committees of the EU Parliament on China and UK House of Lords on Europe. Janet joined HSBC in 1996 in Hong Kong where she worked as an Asian economist in the run-up to, and aftermath of, the Asian crisis.

James is a global economist at HSBC. He joined the Economics team in 2013 having previously worked within the Asset Allocation research team. His global work focuses on longer-term trends and themes, and the impact that they have on the economy and policy decisions today. Demographic data is at the heart of much of his work, but he has also written about urbanisation, the role of technology in the economy and how the world is moving away from cash. Alongside this, he provides economics coverage of Scandinavia. James holds a BSc in Economics from the University of Bath.

Bethan Ellis is a global economist based in London. She joined HSBC in July 2025, having previously worked with the UK and global economics teams for a year as part of her degree. She holds a BSc (first-class honours) in Politics with Economics from the University of Bath.

## How to access HSBC Global Investment Research

![](images/85faf8e605af68073d625cdc61da2801615b869c1b4e397dcc6e6634e7827ddd.jpg)

## Log on to the Global Investment Research website

To access all reports and videos log on to research.hsbc.com

![](images/2aad6293ba4831e3b193b48f99baf2c873563861eb47784dd5379274e8da8c58.jpg)

## Download the HSBC Global Investment

Research app From Apple's App Store or Google Play. The app features topical and timely curated reports, multimedia, and upcoming events

![](images/4daa444845a5ba8a7bd2013157ddfb4498a67ca3d81382a6c13fb322ecaae8cc.jpg)

Connect with Global Investment Research on LinkedIn Search #HSBCResearch for free to view insights that can easily be shared with clients and prospects

![](images/7363b51cfe93f56f4f7be44fd29e6b1138e65cdd953a398fc72b4acde03f64c9.jpg)

## Subscribe and listen to our podcasts

Under the Banyan Tree by HSBC Global Investment Research on Apple, Spotify or YouTube

The Macro Brief by HSBC Global Investment Research on Apple, Spotify or YouTube

![](images/230d5e8c057a780ee04419a18d5872f4866aad55f9e3e72a4d1aaadf6b0217a6.jpg)

Newsletters Subscribe to our monthly collection of free to view reports and interviews in Open Pass or read our bite-sized round up of research covering our nine key themes, Talking Points
"""
