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
  1. 机构 big name：高盛、摩根士丹利、摩根大通、瑞银、花旗、美联储等。
  2. 中国读者熟悉的人名 big name：洪灏、邢自强、辜朝明；国际公众人物：特朗普、马斯克、鲍威尔等。
  3. 反常识或意外差：例如市场普遍悲观时，报告给出“触底”“修复”“再加速”等相反信号。
- 已识别机构名：`布鲁金斯学会`。如果识别机构名为空，请从研报标题/正文中识别机构并使用中文名，例如高盛、摩根士丹利、汇丰、摩根大通、瑞银、花旗、美国银行、巴克莱、德意志银行、野村。
- 标题里不要同时写中文机构名和英文缩写，禁止“摩根大通：JPM：……”“高盛：GS：……”这类重复；写“摩根大通：……”或“高盛：……”即可。
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
7. 文末自然承接未解问题，引导读者加入社群/微信群继续讨论。不要照抄固定话术，请基于本文未解问题每次重新写一段自然 CTA；语义可以参考：加入社群，领取完整研报解读与原始图表。。
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
- 不要隐藏报告机构名；标题必须出现机构中文名。正文如需概括来源，可写“这份布鲁金斯学会研报”或“该机构报告”，但不要编造机构观点以外的信息。
- 不要解释你的思考过程，不要输出多余说明。

【研报解析内容】
"""
# The Brookings Institution The Current podcast

# "Will the Strait of Hormuz reopen after the US-Iran deal?"

June 25, 2026

## Participants:

Aslı Aydıntaşbaş
Fellow, Foreign Policy, Center on the United States and Europe
Director, The Turkey Project
The Brookings Institution

Kari Heerman
Director, Trade and Economic Statecraft
Senior Fellow, Economic Studies
The Brookings Institution

## Bruce Jones

Senior Fellow, Foreign Policy, Center for Asia Policy Studies, Strobe Talbott
Center for Security, Strategy, and Technology
The Brookings Institution

## Episode Summary:

After the United States and Iran signed a memorandum of understanding to end the war, Aslı Aydıntaşbaş spoke to Kari Heerman and Bruce Jones about its geopolitical implications, building on their recent articles in the series “Blowback: How the Iran war may change the world.”

JONES: I think this episode has shown Iran that it can flex the major muscle that it has, which is to constrict shipping through Hormuz

HEERMAN: Iran did not only assert control over the strait, it also experimented a little bit with politically conditioned access, offering discounts to its friends and higher rates to its enemies. And that's a major departure from not only the status quo ante, it also presents major challenges for international maritime law.

JONES: Ninety percent of world trade flows by sea. Seventy percent of world energy, and 99 percent percent of the world's data that flows on the seabed cables, all of that is vulnerable.

[music]

AYDINTASBAS: Hi, welcome to The Current. My name is Aslı Aydıntaşbaş. I'm a fellow at Brookings Foreign Policy program, and with me are two senior scholars, both senior fellows from different parts of Brookings. Kari Heerman. Kari is a senior fellow with the Economic Studies program. And Bruce Jones, also a senior fellow at Strobe Talbott Center for Security, Strategy, and Technology.

Kari and Bruce are with me to talk about what happens in and around Iran, specifically Hormuz, now that we have a deal with Iran. But before we get to the discussion, I want to set the table briefly, because we’ve had a lot happening on Iran over the past couple of days, I will say.

First of all, last week there was the signature of an MOU, memorandum of understanding. President Trump actually signed it a number of times, lately in Versailles, France. And then JD Vance was in Bürgenstock, Switzerland, over the weekend in what seemed to be extensive talks with Iran. Now, there's a lot written about it, also a lot of contradiction in what the parties to the conflict are saying.

[2:01]

I want to start with Bruce. What is your understanding of what's happening, specifically on Hormuz, but anything else you want to mention here?

[2:12]

JONES: Well, I'll I'll just start by saying that I don't think many people missed the symbolism of signing this at Versailles. I'm not quite sure what the president's advance team was thinking for that one. You know, in general terms, I think only the president's most fervent admirers see this war and its outcomes as anything other than a major, a major error and a failure.

I I want to take a moment first before we get into anything else to acknowledge the human cost of this as well. I mean, there are people who died I won't lose any sleep over, but there were also a lot of Iranian civilians, and there were American service men and women who died. And I think most people see this as a pretty flawed outcome, a pretty flawed overall foreign policy moment for the president.

I will say this. If some weeks from now, 60 days or however long it takes, we end up with a deal in which Iran permanently, verifiably, genuinely verifiably, gives up its

nuclear weapons program, we will reevaluate where we are. Right now, this looks like a very bad outcome that has strengthened Iran, but we'll reevaluate that if in fact it is possible to get a deal on the nuclear weapons program—

AYDINTASBAS: —that's an important point—

JONES: —and to see the straits remain open in a way that doesn't cede a great deal of leverage to Iran, which is what has happened now.

[3:31]

AYDINTASBAS: So we're not exactly returning to the previous status quo even with a deal, right?

[3:38]

JONES: I think this episode has shown Iran that it can flex the major muscle that it has, which is to constrict shipping through Hormuz, and it can withstand the price that the West would impose on it as a consequence, and the United States in particular would impose on it as a consequence. It’s been able to withstand this American military barrage and come out with its capacity to threaten the straits essentially undiminished. And that I think puts Iran in a stronger position than we went in.

Now, to be clear, Iran is weakened militarily, internally. There's no question about that. But it's not a very complicated thing to threaten the straits, and their capacity to do that and withstand punishment is strengthened.

[4:17]

AYDINTASBAS: So Kari, as Bruce has actually just highlighted, it turns out Iran's strongest weapon was not really its nuclear program, but it was the strait, its ability to close down straits. And over the course of this war, we saw an Iranian blockade and an American blockade on the Iranian blockade, et cetera. Now, it does seem like the strait is opening, but I think there's a good deal of confusion in terms of what is happening at this very moment and what the deal, the agreement, to end the war entails. Do you have a sense of what's happening?

[4:54]

HEERMAN: What I do understand is that the immediate priority is to open the Strait of Hormuz to get energy and other goods flowing, and also to allow Iran to sell oil on global markets in U.S. dollars, which it hasn't been able to do for some time.

So for the next 60 days, what's been agreed in the MOU is that Iran would open the strait and allow commercial vessels to traffic through it. And it looks like traffic is indeed moving. And likewise, that the United States would provide waivers and licenses and targeted sanctions relief to allow Iran to make sales of petroleum, crude oil, and petroleum products and petrochemicals on global markets in U.S. dollars. And that also appears to be moving forward in some to some degree.

What's unknown is what happens after that 60 days. Within the MOU, the Iranians did not agree to never assert control over the strait again, to never impose costs. One of the interesting things is that when Iran took asserted control over the strait, they established a Persian Gulf Strait Authority, which they were setting up in order to collect fees or tolls on vessels that would transit the strait and to monitor the traffic.

They have not taken that authority down and in fact, they have, my understanding is had the national insurance company open a policy that countries transiting the strait are gonna be required to apply for in order to to use the strait. They will, at least for 60 days, be able to do so with no charge at all. But in the MOU it explicitly states that Iran will consult with Oman, who has the other side of the strait to discuss going forward how the strait should be administered. And that's a major departure from not only the status quo ante, it also a presents major challenges for international maritime law.

Our colleague at Brookings, Scott Anderson, is a great expert in this, and I I won't go into it in a, but he is a great resource.

[6:56]

JONES: I just want to add on Kari's good points.

## AYDINTASBAS: Yeah.

JONES: It's one thing to have agreed all this on paper. In practice, the strait is still mined. And getting rid of the mines is a major operation. There're two ways that happens. Either Iran removes them, which is the easier way. If they are fully implementing the deal and with full cooperation, they remove the mines. That's the easier way.

Or the Europeans have agreed to send demining ships and do the work of removing the mines. That will take months and months and months. Right now we're seeing some ships transit the southern route along the Omani coast, but a lot of ships are still not willing to make the main run through the main strait because there are still mines on the seabed. And how quickly Iran actually removes those mines remains to be seen.

Plus, mining is easy. It's like the difference between starting a fire and fighting a fire. Starting a fire is real easy. Fighting it is hard work. At any moment, Iran could re-mine the straits and it's realized that huge leverage that it has.

[7:54]

AYDINTASBAS: But since President Trump talks about having obliterated, entirely eliminating Iran's navy, would they even have the capability to do the demining that's necessary for traffic?

JONES: I actually don't know the specific answer to that. What I do know is that if they know where they put all their mines. Usually when a country mines—

AYDINTASBAS: —they know—

JONES: —a body of water, they know where they put them.

Now, my guess is in the white hot heat of war that they don't have perfect records of where they mined, and that this is not gonna be as straightforward as just sharing the mining information and the Europeans go take it out.

If if Iran knows where all the mines are and if they're fully cooperating with Britain and France and whoever sends demining ships, it would, you know, it could be done in a matter of, let's say, two, three months. But it's not happening overnight, and that's with full cooperation and full knowledge of what they've done.

I suspect neither condition will be true, and this will be a months-long process at best to de-mine the straits. And then the deal doesn't say a single word about the Iranian threat to impose a levy or a toll, whatever word you want, on the data that flows on the seabed cables—

AYDINTASBAS: —explain—

JONES: —along the Strait of Hormuz. These are crucial data cables. Overall, cables carry 99 percent of the world's data. The cables that run along the Strait of Hormuz are vital for the Arab world and for parts of Africa. Iran, during the conflict, threatened to impose a levy on the data flowing through them. Not really sure how they would do that technically, but they could also disrupt those cables. They could sever them. They could do damage to them.

And unlike with oil, you know, if they, if they block the flow of oil out of Hormuz, they're hurting their own economy as well as the global economy. Data cables, it would have a minimal effect on their economy and have significant disruptive implications for the region.

So there's a whole set of threats there that this doesn't even touch on and remain a risk going forward.

[9:45]

AYDINTASBAS: Now I want to turn to the articles that you both have written. Kari, your piece was with David Wessel from Economic Studies arguing that Iran's weaponization of the Strait of Hormuz actually sets a very dangerous precedent for all types of choke points. I want you to briefly explain, I think this is exactly what Bruce was alluding to, but I want you to take it from Iran to what we're talking about globally.

[10:15]

HEERMAN: Yeah. So Iran did not only assert control over the strait, it also experimented a little bit with politically conditioned access to the strait.

AYDINTASBAS: Politically conditioned access.

HEERMAN: Yeah. Yeah.

AYDINTASBAS: An expression you're using as opposed to the regular disruption.

HEERMAN: Yes, exactly. So not just blocking everybody, not just imposing a uniform fee on everybody who wants to access the strait, but offering discounts to its friends and higher rates to its enemies.

Not only does that is that different from the status quo ante where there are no fees or no costs, and not only does it implicate, you know, maritime law, but it also changes the nature of the political leverage associated with access to the strait.

So what David and I observed, and we think is important in sort of looking beyond what could be outcomes, longer term outcomes of of this incident, is that risk that politically conditioned access to one of these narrow waterways where there are very few alternatives to use them could be something that could be used as a tool instead of a global public good that allowed open access to everyone in the world.

It's turned into a tool to pressure rivals, to favor partners and allies, and thus becomes a source of geopolitical leverage.

[11:28]

AYDINTASBAS: Let's talk about a bunch of these places. Can we, can you name a few places that...

[11:33]

HEERMAN: There're a number, and I think, you know, I don't—

AYDINTASBAS: —Malacca Straits—

HEERMAN: —the Straits of Malacca is one of them. There’s the Strait of Denmark is one of them. There’re a number of them, and it—

AYDINTASBAS: —Bosphorus, of course—

HEERMAN: —yes, of course—

AYDINTASBAS: —is important, or that's been open for nearly 100 years.

HEERMAN: Exactly. Well, most of these have been. There, there's a long custom of providing global access to international waterways like this even preexisting the international maritime law that that institutionalized it.

But just as Bruce was saying earlier it isn't free to do that. It would be very costly for most of these countries to give up that freedom of navigation. It benefits most countries much more than it is a source of leverage. So it is not something that we expect to start unfolding tomorrow.

But just as these things slowly become normalized, and it slowly becomes, while of course Iran wants to use the leverage that it has in this much more contested geopolitical environment when tariffs are being used strategically, when export controls are being used strategically, our concern is that it just starts to be one more thing that looks a little bit normal, and we end up in a situation where—

AYDINTASBAS: —normalizing—

HEERMAN: —yes—

AYDINTASBAS: —use of geography as a leverage particularly for economic punishment.

[12:47]

Bruce, I want to turn to your piece. I learned a lot. Its title is "A Sinking Feeling: The Strait of Hormuz and the strains on U.S. naval power." Now, freedom of navigation is as American as apple pie. Right? It's long been a U.S. policy, stated U.S. goal. But tell me a little bit about what you wanted to say and what the sinking feeling is.

[13:12]

JONES: Yeah. So there are two or three points here. So first, as Kari said, there's been a long custom here, predates American hegemony. It's ... But it was a a cornerstone of American post-war global role. The notion that the American Navy guarantees the freedom of navigation has been, I would argue—

AYDINTASBAS: —everywhere—

JONES: —the cornerstone of American power globally.

AYDINTASBAS: And everywhere, right—

JONES: —everywhere—

AYDINTASBAS: —pretty much.

JONES: —everywhere.

But I'm a, I I put the the elements of why this is collapsing slightly differently. So it's absolutely true what Kari said, but even before we got to that, we saw fighting in the Black Sea between Russia and Ukraine threatening the disruption of some of the largest flows of food and fertilizer in the world, threatening famine for tens of millions of people literally.

We saw Iran helping the Houthis use weaponry in the Red Sea that disrupted trade there, trade flows there. And we're, we're starting to see around the world non-state armed groups as well as relatively small states getting a hold of robotics, weaponry, drones, AI-enabled drones, and other kinds of tools that I think we're, we're gonna see a spread of threats to to shipping.

In the case of states doing that, there are costs and risks, whether it's you're disrupting your own oil sales or or, you know, your own benefits from free flow of trade. In the state of non-state actors, that might look very different. And I think that we're gonna see more contest from both states and non-states on the flow of shipping.

Put this in context. Ninety percent of world trade flows by sea. Seventy percent of world energy, 70 percent of world food supplies, 90-plus percent of metal and and rare earths elements, all the stuff we need to manufacture, and 99 percent percent of the world's data. Every time you use your cellphone or do online banking or do anything remotely—

AYDINTASBAS: —WOW—

JONES: —let alone U.S. military communications, let alone AI, all moves on undersea cables. All of that is vulnerable.

[15:03]

Third point. What we have done since the end of the Cold War, we, the United States, and we, the West, is to continue to shrink the size of naval assets that we have. When we ended the Cold War, the United States had a 600-ship Navy. Right now, we're fighting with a 280-ship Navy. So we've dramatically increased the economic stakes of what's flowing at sea and decreased our capacity to secure those flows.

At the same time, China has become by far and away the world's most comprehensive maritime power. So the balance of power and who can secure crucially important flows at sea is moving away from the United States. This episode, I think, hastens that. It didn't trigger it, but it is hastening it.

But I think the United States faces a a really difficult moment ahead where the viability of that guarantee of the free, the freedom of navigation is gonna become extremely hard to implement. I will also say lots and lots and lots of other countries benefit hugely from the flow of goods at sea.

AYDINTASBAS: But this is something I wanted to ask you..

JONES: So it is perfectly reasonable for the United States to ask for others to be doing more.

[16:15]

AYDINTASBAS: Sure, but you also make the point further in your piece that actually Russia and China massively benefit from U.S. naval guarantee of freedom of goods and oil specifically. So should United States start thinking of these issues in more selective terms, or is the whole global economy so intertwined that you really cannot be selective?

[16:44]

JONES: So this is the point that I concluded my last book on, I wrote this book called To Rule the Waves, which is about these issues, and it ends with this point, that there's just a fundamental contradiction at the heart of modern globalization and modern American power. We are expending enormous amounts of treasure and manpower and and lives to secure flows whose primary beneficiary is our principal adversary. That is illogical in its most fundamental level.

Now, we also profit from the growth of the Chinese economy, and it's all integrated and yada, yada, yada, but there is a fundamental contradiction here.

So my own view for the last several years is we need to be moving towards two globalizations, one that the United States secures and one that it does not. That is not what we're watching. We're watching something much more chaotic than that.

AYDINTASBAS: That's very interesting and definitely should be the topic of a different podcast because this differentiated globalization is rather unique.

[17:35]

Kari, I wanted to ask you about the deal in broader terms because JD Vance talks about turning over a new leaf with Iran, you know, in repeated interviews over the weekend. And last week, he talked about this as a grand bargain. And I thought of you in the sense that I knew I was going to come for this discussion today, and you have worked in U.S. government, in bureaucracy, where you dealt with sanctions, economic statecraft and, and, and definitely export controls and so on.

It must be a new page for everyone who works on U.S. government. In other words, sanctions do not get lifted the moment you say, Okay, I'm lifting the sanctions, right? It's a very complicated system. Have you thought of what could happen? Can this happen, a major reconstruction fund for Iran or unfreezing of the frozen Iranian assets and sanctions relief?

[18:35]

HEERMAN: Well, I'll reiterate that there is quite a bit that is unknown about what is actually happening. But yes you can. What is happening right away is a general license from the U.S. Treasury that allows waivers and licenses for things to resume flowing for Iran to to sell oil on international markets. That is something that's time-limited for the next 60 days again.

Longer term, actually removing the sanctions, you're right that there are legal complexities involved in it. There are some things that the executive branch can do fairly straightforward. There are some things that will require Congress. Some of the sanctions are not U.S. unilateral sanctions. Yes, there are legal complexities. I think that their removal is probably tied to the broader set of negotiations, so I don't expect, although I could be—

AYDINTASBAS: —who knows—

HEERMAN: —terribly wrong, but I don’t expect that the U.S. as down payment is removing all sanctions permanently. This is something that will take some time and will probably be quite complicated in the negotiations. You’re right about that.

AYDINTASBAS: So it's not going to be, Okay, I decided to wire you \$300 billion expected by Thursday. Give me your bank account. It it it's just basically impossible at this point.

HEERMAN: Well, that would be surprising. So I think what you're talking about now is different from sanctions relief.

AYDINTASBAS: Yes, as the reconstruct—

HEERMAN: There's sanctions relief, there's making frozen assets available, and then the third element is a reconstruction fund, for which there are very few details. In the MOU, it says there will be a reconstruction fund of some kind. There's a lot of uncertainty surrounding what that is. To what degree is it private investment commitments? To what degree is it money from from various governments? JD Vance has said not one U.S. dollar of taxpayer money is going to be used for reconstruction in Iran. It's unclear exactly what what this reconstruction fund looks like. Having read a few things over the past few days, there are many different ideas going around.

I think what, what's interesting is that this is quite a different approach to reconstruction or economic development, or the provision of economic security post-conflict. There's long been a recognition that securing peace post-conflict requires an element of economic security. That's a lesson learned from about 100 years ago pretty firmly.

And so it's not surprising to me that regional allies and and other countries would want to commit to providing support for Iran to reintegrate into the global economy. There are many examples of where that has provided some economic stability both domestically and globally.

I think what will be interesting to watch is who benefits from that. There's money to be made. What kind of a regional economic infrastructure that sets up and whether that really secures the Iranian economy and integrates it with the region post-conflict.

[21:32]

JONES: I would say, by the way, that we may see countries willing to participate in this for a couple of reasons. One is, and we should just acknowledge this point, like, the end of the war is intrinsically a good thing.

AYDINTASBAS: Sure.

JONES: No matter what else is true—

AYDINTASBAS: —sure—

JONES: —the war stopping is a good thing. You know, the estimates are different here, but some estimate around \$2 trillion cost to the global economy so far. The president himself said that if this had gone on, it would’ve triggered a great depression. Like the, you know, if we, if we really saw oil flows constrict past the point where reserves and reduced demand were able to cope with it, the consequences would be extremely large.

So, a lot of countries will have a stake in helping make sure that this does actually work. And I think we'll see a lot of people winking and nodding and turning a blind eye and, you know, fees or tolls and various other things. Diplomacy can smooth a lot of cracks. We know that from all of modern history and recent history.

So it would not surprise me if we see countries putting money into this. It will surprise me if this is all stable and if we don't see breakdown, collapse, return to conflict, lack of implementation of the deal, and all of the above. That will surprise me.

AYDINTASBAS: Well, that seems like—

JONES: —a bad note on which to end—

AYDINTASBAS: —a bad note to end. But nonetheless—

JONES: —a sinking feeling—

AYDINTASBAS: —our time is up. Thank you for this very, very interesting conversation. Thanks to both of you, and I’m going to also thank our listeners for listening and watching.

[music]

You can learn about all of this, as well as read Bruce and Kari's pieces on our website at Brookings dot edu.

This is Aslı Aydıntaşbaş from The Current.
"""
