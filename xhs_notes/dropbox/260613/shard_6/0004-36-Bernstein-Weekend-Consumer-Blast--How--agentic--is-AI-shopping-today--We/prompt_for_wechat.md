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
- `# 标题` 必须包含报告机构的中文名称。已识别机构名：`Bernstein`。标题格式建议：`# Bernstein：一句主判断`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如GS、摩根斯坦利、HSBC、JPM、UBS、Citi、美国银行、BARC、DB、NOM。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份Bernstein研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# Weekend Consumer Blast: How "agentic" is AI shopping today? We tested 5 models...

Zhihan Ma, CFA +1 917 344 8303 zhihan.ma@bernsteinsg.com

Alexia Howard +1 917 344 8453 alexia.howard@bernsteinsg.com

Aneesha Sherman +1 917 344 8457 aneesha.sherman@bernsteinsg.com

Callum Elliott, CFA, ACA +44 20 7676 7183 callum.elliott@bernsteinsg.com

Danilo Gargiulo +1 917 344 8475 danilo.gargiulo@bernsteinsg.com

Euan McLeish +81 3 5962 9611 euan.mcleish@bernsteinsg.com

Ian Moore +1 917 344 8434 ian.moore@bernsteinsg.com

Jignanshu Gor +91 226 842 1494 jignanshu.gor@bernsteinsg.com

Luca Solca +41 582 723 126 luca.solca@bernsteinsg.com

Melinda Hu +852 2123 2643 melinda.hu@bernsteinsg.com

Nadine Sarwat, CFA +44 20 7676 6849 nadine.sarwat@bernsteinsg.com

Richard J. Clarke, FCA +44 20 7676 6850 richard.clarke@bernsteinsg.com

Trevor Stirling +44 20 7676 7521 trevor.stirling@bernsteinsg.com

William Woods +44 20 7676 6806 william.woods@bernsteinsg.com

Agentic shopping burst onto the US Retail scene last October after Walmart announced its partnership with ChatGPT. $^{1}$ More than six months later, how agentic is shopping today?

We tested five different tools. Three are foundational AI models - ChatGPT, Gemini, and Claude - with broad capabilities. The other two, Amazon's Alexa and Walmart's Sparky, are retail-native AI tools built directly on top of retail ecosystems. The goal was to see how each approaches the shopping funnel: from identifying the right product, to validating pricing, and actually enabling a purchase. More importantly, we assess where each tool breaks down and how far we are from a true end-to-end agentic e-commerce experience. While human interaction is still needed at every stage, payment is where the whole experience unravels. Even in the simplest case - buying a single, generic item - the hand off from “AI found it” to “I bought it” still requires the user to engage. Until payment is embedded directly into the experience, AI remains one step removed from making shopping decisions on behalf of users.

Underpinning that is a tension between general and retailer-integrated systems. The foundational AI models feel powerful because they can roam freely, comparing products, surfacing deals, and stitching together options across a fragmented retail landscape. However, they are doing so without direct access to the structured catalog data, real-time pricing, inventory, or delivery options. Meanwhile, those retail ecosystems have the opposite problem: they are highly precise and almost-transaction-ready, but confined to their own assortment (1P and/or 3P). Bridging this gap, from either end, will be key as the technology evolves.

## BUYING ONE ITEM - REQUIRES INTEGRATION!

We evaluated how effective each AI assistant is through each step of the basic e-commerce process for one item, from product discovery to final transaction execution: I want to make scrambled eggs, but I've run out of milk. Could you please find me a 64 fl oz carton of organic whole milk? How soon can it be delivered to me in ZIP 22201 (Arlington, VA)? Exhibit 1 shows each AI tool's performance at each stage.

EXHIBIT 1: Amazon Alexa and Walmart Sparky currently maintain an advantage in real-time pricing accuracy, total cost estimation, and transaction execution.

<table><tr><td></td><td>Identifies Category</td><td>Identifies SKU</td><td>Identifies Pricing</td><td>Estimates Full Cost</td><td>Add to Cart</td><td>Payment</td></tr><tr><td>ChatGPT</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>Claude</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>Gemini</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>Amazon Alexa</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>Walmart Sparky</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td><td>●</td></tr></table>

Definitions - Identifies Category: Ability to correctly determine the relevant product category; Identifies SKU: Ability to accurately identify the specific item, including its brand, size, and variant; Identifies Pricing: Ability to correctly determine the exact price of the selected item; Estimate Full Cost: Ability to accurately calculate the total order cost, including fulfillment, taxes, and any additional fees; Add to Cart: Ability to successfully add selected items to the shopping cart; Payment: Ability to complete the checkout process and successfully execute the order.

Source: Bernstein analysis

There is currently no agentic shopping tool capable of buying a product in an unsupervised fashion. Human engagement is needed at many steps.

ChatGPT, Claude, and Gemini are primarily research and recommendation tools. Because they lack direct access to retailers' assortment (unless shared by retailers directly), they seem to rely on workarounds such as web scraping or third-party articles (Exhibit 2). Therefore, they sometimes struggle with SKU identification and pricing accuracy. In addition, they are incapable of handling fulfillment and payment (in so far as they lack a connection). As a result, these are product discovery tools. However, they are partnering with retailers to bridge the gap. ChatGPT, for example, has introduced its Agentic Commerce Protocol (ACP), and Claude integrates with Uber Eats to enable grocery and food delivery (Exhibit 6). Still, users need to follow links to retailers' websites to complete transactions.

In contrast, Amazon and Walmart operate fundamentally differently. Their AI assistants have access to the real time inventory data. This allows them to manage the entire purchase funnel within their ecosystems, from product discovery through payment. Amazon's implementation illustrates both the potential and the limitations of this approach. Alexa can add non-perishable items to a cart (Exhibit 7) but currently excludes Amazon Fresh and Whole Foods products (Exhibit 8). There are still limitations at the final step. The payment process is not fully integrated within either Sparky or Alexa, so users cannot complete the transaction directly within the assistant.

## EXHIBIT 2: ChatGPT can identify the SKU and estimate an approximate price range, but appears to rely on web scraping at times.

Whole Foods link, in exhibit, directs to an article on Whole Foods delivery policy.

I want to make scrambled eggs, but I've run out of milk. Could you please find me a 64 fl oz carton of organic whole milk? How soon can it be delivered to me in zip 22201 (Arlington, VA)?

![](images/9e6d1ce5896043c9af4b82e0d02993711cb39cafbc4afdd6fc34ac9b91075bf5.jpg)

Here are the best quick options I found for a 64 fl oz organic whole milk delivery to Arlington, VA 22201:

## Fastest + Cheapest Likely Option

• Great Value Organic Whole Vitamin D Milk, Half Gallon, 64 fl oz  
Price: about \$3.98 at Walmart ↗  
Delivery: typically same-day within 1–3 hours through Walmart delivery in Arlington if slots are  
available.  
Whole Foods

## Best Premium Organic Brand

• Organic Valley Organic Whole Milk Half Gallon Carton 64 oz

Price: about \$4.96-\$6.26 at Walmart ↗

Delivery: generally same-day in your ZIP if ordered soon. Whole Foods ...

## Whole Foods Option

• Organic Valley Organic Whole Milk 64 Oz

Price: usually around \$6–7 at Whole Foods Market ↗

Delivery: often under 2 hours via Amazon/Whole Foods delivery depending on availability.

Whole Foods.

Source: ChatGPT (OpenAI), Bernstein analysis

## EXHIBIT 3: With the initial prompt, Gemini suggests relevant product and delivery options but does not identify items at the SKU level.

It also appears to rely on online scraping to generate its responses.

For your immediate cooking needs in zip code 22201 (Arlington, VA), you have a few highly efficient options to secure a 64 fl oz carton of organic whole milk (commonly available from trusted organic brands like Horizon Organic, Organic Valley, or Stonyfield):

## On-Demand & Instant Delivery (Fastest)

If you are mid-recipe and need it immediately, delivery apps are your best option:

Instacart, DoorDash, or Uber Eats: You can order a 64 oz carton directly from local stores right in your neighborhood (such as the Safeway on Wilson Blvd or the Whole Foods Market in Clarendon).  
Delivery Speed: These services typically offer on-demand rush delivery that can arrive at your door in 30 to 60 minutes.

## Same-Day Store Services

If you have a bit more flexibility later in the day:

Safeway Flash / DriveUp & Go: The Safeway location at 1525 Wilson Blvd handles rapid fulfillment online, often preparing "Flash" delivery orders or window pickups in 30 minutes or less. Safeway  
Amazon Fresh / Whole Foods Market: Standard same-day delivery slots for the Arlington area are usually available within a 2-hour window depending on current courier availability. Dragonfly

To get it fastest, checking DoorDash or Instacart mapped to your exact street address will show you the precise real-time courier ETA, which should easily be under an hour.

Source: Google Gemini, Bernstein analysis

## EXHIBIT 4: This is not due to a lack of capability. When prompted further, such as asking for the price of the milk, Gemini is able to retrieve SKU-level product information.

what's the price of the milk

In the Arlington, VA area (zip 22201), a 64 fl oz carton of organic whole milk generally ranges between \$4.69 and \$7.49 depending on the store brand and specific label:

Store Brands (Most Affordable):  
Whole Foods (365 Brand): \$4.69 per 64 oz carton. Whole Foods Market  
- Premium National Brands:  
Organic Valley: \$6.29 per 64 oz carton. Whole Foods Market  
- Horizon Organic: \$6.99 (Standard Whole Milk) to \$7.49 (DHA Omega-3 formula) per 64 oz carton.

Note: If you order through a third-party application like Instacart or DoorDash, the base price may be slightly marked up by \$0.50 to \$1.00, and standard delivery fees/service tips will apply.

Source: Google Gemini, Bernstein analysis

## EXHIBIT 5: Similar to Gemini, Claude initially presents delivery options along with item recommendations and approximate delivery times.

I want to make scrambled eggs, but I've run out of milk. Could you please find me a 64 fl oz carton of organic whole milk? How soon can it be delivered to me in zip 22201 (Arlington, VA)?

Shopping and grocery delivery isn't something I can search directly, but here are some great options for getting organic whole milk delivered quickly to Arlington, VA (22201):

## Same-day or fast delivery options:

- Instacart (instacart.com) — connects to local stores like Whole Foods, Safeway, Giant, and more. Often delivers in 1-2 hours.  
- Amazon Fresh — if you're a Prime member, same-day or next-day delivery is common in Arlington.  
• Whole Foods (via Amazon) — Prime members often get free 2-hour delivery.  
- DoorDash / Uber Eats — both partner with grocery stores and can deliver in under an hour from nearby locations.

For a 64 fl oz carton of organic whole milk, brands like Organic Valley, Horizon Organic, or 365 by Whole Foods are widely available through all of the above.

Arlington is very well-served by these services, so same-day delivery within 1-2 hours is very likely. In the meantime, for your scrambled eggs — a small splash of water or a bit of cream cheese actually works wonderfully as a milk substitute!

Source: Claude (Anthropic), Bernstein analysis

## EXHIBIT 6: Through its partnership with Uber Eats, Claude enables users to complete purchases via Uber Eats directly within the interface.

I don't have a grocery delivery connector available to place orders directly. Let me see if there's one I can suggest for you!

Searching connectors >

Unfortunately there's no grocery delivery connector (like Instacart or Amazon Fresh) available to connect right now. The closest option I found is Uber Eats, which does partner with some grocery stores:

![](images/6d715968eb15391e73ae7bb5a3dd4e3b6014bd117de843dc5f49b411d0784acd.jpg)

Your connectors

Beta

![](images/58134d539b00182380713f083e15d2db8899271aa566a059e6ff1ba7a2ebce1e.jpg)

Uber Eats Connected

![](images/0ef279f7323eac9ef75af159f111d0a6d1afb022083620e957e78dd0dba47894.jpg)

Looking for something else? Browse all connectors

None of these

Uber Eats is one option — would you like to connect it to search for grocery stores near you? Otherwise, your quickest bet would be heading directly to instacart.com or Amazon Fresh to search for that 64 fl oz organic whole milk — both should have it to you in Arlington within an hour or two.

Source: Claude (Anthropic), Bernstein analysis

## EXHIBIT 7: Amazon provides product recommendations at the SKU level, presenting users with a range of options to choose from.

I want to make scrambled eggs, but I've run out of milk. Could you please find me a 64 fl oz carton of organic whole milk? How soon can it be delivered to me in zip 22201 (Arlington, VA)?

Great news! I found some 64 fl oz organic whole milk options that can be delivered today between 1 PM – 3 PM in Arlington, VA (22201):

## 64 fl oz Organic Whole Milk - Delivered Today See more

![](images/4918b16a15ac73e9e8e1eccd3ecd19766a04b4375ecdd6c41a6b64758c895c08.jpg)

365 by Whole Foods Market, Organic Whole Milk, 64 oz

4.7 ★★★★★☆ (12,677)

10K+ bought in past month

\$479 (\$0.07/fluid ounce)

FREE delivery Today 1 PM - 3 PM on orders over \$25.00

365 by Whole Foods Market – USDA Organic, pasture-raised, GMO-free, fortified with Vitamin D3. \$4.79

## More details

![](images/3efc036a0cab3caeca3e4f517f03b3572cc0358aebf5c1a818a772e2f1bfc449.jpg)

Organic Valley, Organic Whole Milk, 64 Oz (Half Gallon)

Source: Amazon Alexa, Bernstein analysis

## EXHIBIT 8: Alexa is unable to do so for Amazon Fresh and Whole Foods products; it directs the user to an external link.

All four options qualify for free delivery today (1 PM – 3 PM) on qualifying orders. The 365 by Whole Foods Market option is the most budget-friendly at \$4.79. Would you like me to add one to your cart?

Add the 365 Whole Foods milk to my cart

I wasn't able to add this item directly to your cart — Fresh/Whole Foods products need to be added from the product page. You can do so here:

365 by Whole Foods Market Organic Whole Milk, 64 fl oz — \$4.79

Just tap the link to go to the product page and add it to your cart from there!

Source: Amazon Alexa, Bernstein analysis

## EXHIBIT 9: Sparky is capable of handling the full flow from product discovery through to building a basket (or cart).

Great news — two of these options show delivery as soon as 18 minutes to 22201 (Arlington, VA). Here are your 64 fl oz organic whole milk options:

## Sparky's Picks

## Best seller, most affordable at \$3.97

![](images/50303b68be22d8c5cc275829f5ab99d11e7c2eacd1d7e27a9a49e1326e806521.jpg)

![](images/126025d78e5339b5221ca5c40a55829b8cb5849b6c6d0d23aaa63e8ce19bbfe9.jpg)

Great Value Organic
Whole Vitamin D Milk, Hal...

★★★★★ (3329)

Best seller

\+ Add

## ♦ Added DHA Omega-3, also a best seller

![](images/14927fc750928177f051c0c6082a99e3f1e3faa81f56ade53055b28bf4d9f532.jpg)

![](images/20a92e921beae19980fa9b4734faf5f12a94d6ba590b35ada795eed32fc15746.jpg)

Horizon Organic DHA Omega-3 Whole Milk, DH...

★★★★★ (2524)

Best seller

\+ Add

## Organic Valley, currently on rollback

Source: Walmart Sparky, Bernstein analysis

## BUILDING A GROCERY BASKET - DESIGN CHOICES GUIDE LLM'S

Beyond finding and buying a single item, we tested AI agents' ability to build a grocery basket. It requires translating a multi-day meal plan into a complete grocery basket, estimating appropriate quantities for a family of four, and accounting for constraints such as a nut allergy. In addition, it assesses the ability to demonstrate contextual awareness, organize items and avoid duplication. The prompt is:

Household description: family of four (two adults and two children, ages 6 and 10) living in New York City, with a total household income of \$100,000. This family has nut allergies. [Inserted Exhibit 10 as list]. Please build me a grocery basket for this week. Thank you!

## EXHIBIT 10: We fed this meal plan as text into the prompt.

We kept meal choices rudimentary, this isn't a culinary exercise.

<table><tr><td>Meal / Day</td><td>Monday</td><td>Tuesday</td><td>Wednesday</td><td>Thursday</td><td>Friday</td></tr><tr><td>Breakfast</td><td>Yogurt</td><td>Scrambled eggs</td><td>Oatmeal</td><td>Waffles</td><td>Bagels with cream cheese</td></tr><tr><td>Lunch</td><td>Turkey sandwich</td><td>Chicken and rice</td><td>Ham wrap and snacks</td><td>PB&amp;J</td><td>Salad and fruit</td></tr><tr><td>Dinner</td><td>Tacos</td><td>Spaghetti</td><td>Meat loaf and mash potatoes</td><td>Fried rice with eggs and vegetables</td><td>Pizza and Fries</td></tr></table>

Source: Bernstein analysis

## EXHIBIT 11: Foundational LLMs are better at understanding context while retail-integrated models provide SKU-level detail.

<table><tr><td></td><td>Is it a list?</td><td>Is it a basket?</td><td>Pricing</td><td>Add to cart</td></tr><tr><td>ChatGPT</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>Gemini</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>Claude</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>Amazon Alexa</td><td>●</td><td>●</td><td>●</td><td>●</td></tr><tr><td>Walmart Sparky</td><td>●</td><td>●</td><td>●</td><td>●</td></tr></table>

Definitions - List: A set of relevant product suggestions based on the user's request; Basket: A structured collection of specific SKUs selected for purchase; Pricing: The accuracy and reasonableness of the price information provided for each item; Add to Cart: The capability of a shopping tool to add selected items directly into a virtual cart for purchase.

Source: Bernstein analysis

Design choices guide performance in this task. The foundational LLM's understand the complexity in full, and are able to provide detailed answers. However, there is no clear link down the funnel, so the output is (for now) more akin to a shopping list. Alexa operates best within Amazon's shelf-stable assortment, while Fresh items are not yet available. This could be by choice, or for a lack of wiring in the back end. Sparky takes a completely different approach and provides product recommendations in the context of recipes. Is this computationally more efficient? It generates recipes that loosely align with the requested meals. Each recipe can be opened in detail, and from there, users can add all required ingredients to their cart with accurate pricing, creating a smooth path from idea to purchase. Once again, human engagement is required.

ChatGPT, Gemini, and Claude generate comprehensive shopping lists that ope

[中间内容因长度限制已省略]

ence system.

Bernstein may use artificial intelligence tools in the preparation of its materials. Any such materials are reviewed by Bernstein's research analysts prior to publication.

This report has been prepared for information purposes only and is based on current public information that we consider reliable, but the entities noted herein do not warrant or represent (express or implied) as to the sources of information or data contained herein are accurate, complete, not misleading or as to its fitness for the purpose intended even though the entities noted herein rely on reputable or trustworthy data providers, it should not be relied upon as such. Opinions expressed are the author(s)' current opinions as of the date appearing on the material only and we do not undertake to advise you of any change in the reported information or in the opinions herein.

Any references to SG herein are purely factual, based upon publicly available information, and included for comparative purposes only. They do not constitute an opinion or recommendation with respect to the securities of SG.

This publication was prepared and issued by the entity referred to herein for distribution to eligible counterparties or professional clients. The information in this report is intended for general circulation and does not constitute an offer to buy or sell any security, investment, legal or tax advice nor a personal recommendation, as defined by any of the aforementioned regulators. It does not take into account the particular investment objectives, financial situations, or needs of individual investors. The report has not been reviewed by any of the aforementioned regulators and does not represent any official recommendation from the aforementioned regulators. The investments referred to herein may not be suitable for you. Investors must make their own investment decisions in consultation with advice sought from a financial adviser regarding the suitability of the investment product, taking into account the specific investment objectives, financial situation or particular needs of any recipient of the recommendation, before the recipient makes a commitment to purchase the investment product.

The analysis contained herein is based on numerous assumptions. Different assumptions could result in materially different results. The information in this report does not constitute, or form part of, any offer to sell or issue, or any offer to purchase or subscribe for shares, or to induce engagement in any other investment activity. The value of any securities or financial instruments mentioned in this report may fluctuate subject to market conditions. Information about past performance of an investment is not necessarily a guide to, indicative of, or assurance of future performance. Estimates of future performance mentioned by the research analyst in this report are based on assumptions that may not be realized due to unforeseen factors like market volatility/fluctuation. In relation to securities or financial instruments denominated in a foreign currency other than the clients' home currency, movements in exchange rates will have an effect on the value, either favorable or unfavorable. Before acting on any recommendations in this report, recipients should consider the appropriateness of investing in the subject securities or financial instruments mentioned in this report and, if necessary, seek independent professional advice.

The securities described herein may not be eligible for sale in all jurisdictions or to certain categories of investors where that permission profile is not consistent with the licenses held by the entities noted herein. This document is for distribution only as may be permitted by law. It is not directed to, or intended for distribution to or use by, any person or entity who is a citizen or resident of or located in any locality, state, country or other jurisdiction where such distribution, publication, availability or use would be contrary to law or regulation or would subject the entities noted herein to any regulation or licensing requirement within such jurisdiction.

Source: Bloomberg Index Services Limited. BLOOMBERG® is a trademark and service mark of Bloomberg Finance L.P. and its affiliates (collectively “Bloomberg”). Bloomberg or Bloomberg’s licensors own all proprietary rights in the Bloomberg Indices. Neither Bloomberg nor Bloomberg’s licensors approves or endorses this material, or guarantees the accuracy or completeness of any information herein, or makes any warranty, express or implied, as to the results to be obtained therefrom and, to the maximum extent allowed by law, neither shall have any liability or responsibility for injury or damages arising in connection therewith.

No part of this material may be reproduced, distributed or transmitted or otherwise made available without prior consent of the entities noted herein. Copyright Bernstein Institutional Services LLC Bernstein Autonomous LLP, BSG France S.A., Bernstein (Hong Kong) Limited 盛博香港有限公司, Bernstein (Canada) Limited, Bernstein (India) Private Limited (SEBI registration no. INH000006378), Bernstein (Singapore) Private Limited and Bernstein Japan KK (サンフォード・C・バーンスタイン株式会社). All rights reserved. The trademarks and service marks contained herein are the property of their respective owners. Any unauthorized use or disclosure is strictly prohibited. The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands.
"""
