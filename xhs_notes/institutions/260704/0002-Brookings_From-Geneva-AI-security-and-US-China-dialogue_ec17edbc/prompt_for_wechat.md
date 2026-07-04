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
- CTA 必须每篇重新写，不能固定套话。它需要自然包含这些信息：更多国际信源汇编&评论，扫码交流，每日更新，汇总国际主流叙事&数据&图表，观测边际变化；汇聚了头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等朋友，期待交流。

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
# The Beijing Brief podcast The Brookings Institution

# "From Geneva: AI, security, and US-China dialogue"

Wednesday, July 1, 2026

## Participants:

R. David Edelman

Director, Project on Technology, the Economy, & National Security Massachusetts Institute of Technology

Nonresident Senior Fellow, John L. Thornton China Center, The Brookings Institution

Ryan Hass

Director, John L. Thornton China Center

Senior Fellow, Foreign Policy, Center for Asia Policy Studies, John L. Thornton China Center; Chen-Fu and Cecilia Yen Koo Chair in Taiwan Studies

The Brookings Institution

## Episode Summary:

In this special episode of The Beijing Brief, Ryan Hass speaks with R. David Edelman on the sidelines of the United Nations Global Conference on AI, Security, and Ethics in Geneva, Switzerland. Drawing on seven years of experience participating in a track II dialogue on AI and national security, they discuss the importance of sustained dialogue despite broader strategic competition, prospects for renewed government-to-government AI talks, shared concerns over AI-enabled cyber and biological risks, and the growing debate over global AI governance.

EDELMAN: If there is one set of issues that seems to unite U.S. and China, it is mutual anxiety about the impact that AI can have on our collective national security, and even for the relationship and sleepwalking into, God forbid, a conflict. And so that's really what we're focused on today, is talking about what are the mechanisms that exist bilaterally, at the perhaps multilateral or international level, to bring down the risk of an otherwise unintended conflict.

[music]

HASS: Hi, this is Ryan Hass, co-host of the Beijing Brief podcast. I'm here with my friend and colleague, David Edelman.

EDELMAN: Hey, Ryan. Good to see you.

HASS: Good to see you. We are in Geneva, sunny, summery Geneva today. David, why are we here?

[0:40]

EDELMAN: We are here at the UN Global Conference on AI, Security, and Ethics, hosted by the United Nations here in Geneva, and the UN Disarmament Agency, UNIDIR, which is pulling together folks from around the world to talk about the intersection of national security and artificial intelligence.

And specifically, we're here on behalf of Brookings, to talk about some of the experience that we've had over the course of the last seven years on AI, and specifically U.S.-China AI national security, an issue that I know you've been leading on from well before then.

[1:07]

HASS: David, you were just on the stage at this UNIDIR conference. What were some of the key messages that you wanted to get across?

[1:12]

EDELMAN: Well, you know, the first message was that this is one of those issues that is evolving faster than governments can keep up, and that we have heard consistently from governments that there is a real need to have this conversation happening both bilaterally, U.S.-China, and more broadly.

We keep hearing over and over from those, you know, here at this conference, that this is gonna be a global dialogue, and it needs to be situated within that. But at the same time, I think there's a lot of anxiety in this room about where this very consequential security relationship, one that is not always on positive tenor, is headed.

And if there is one set of issues that seems to unite U.S. and China, it is mutual anxiety about the impact that AI can have on our collective national security, and even for the relationship and sleepwalking into, God forbid, a conflict.

And so that's really what we're focused on today, is talking about what are the mechanisms that exist bilaterally, at the perhaps multilateral or international level, to bring down the risk of an otherwise unintended conflict.

[2:08]

HASS: It was a powerful visual having you on the stage with your Chinese counterpart, Xiao Qian, talking about the work of this Track II dialogue on the role of AI in national security that Brookings and Tsinghua have led for the past seven years. What were some of the headwinds that you described in that conversation to the progress of this dialogue?

EDELMAN: Well, look, this dialogue, as you well know, happens in a context not of mutual trust, but of mutual interest. Right? The U.S. and China at the governmental level do not trust one another on these issues as a long list of others. And so, you know, I think one of the core headwinds that we’ve always been facing, and frankly anywhere we want to make constructive progress, even on issues that are challenging in U.S.-China, is the fact that there is consistent political relationship separate from any academic dialogue, separate from any Track II, even separate from the issues we might want to talk government to government with, with China, in the broader tenor of the relationship. There are lots of things that make that a dynamic relationship.

And so obviously this dialogue, like any other, has run into the challenges of ensuring that we are making sure we are fully representing the realities of the relationship. No one wants to have a conversation for its own sake. The idea is to actually make meaningful progress to help where appropriate, inform or educate or provide new ideas to the governmental level. And also frankly to help one another more deeply understand where the trajectories are headed, where this technology is headed, and where there might be areas for constructive if not agreement, at least constructive overlap in the policies that we want to see.

You know, U.S.-China, it is clear that both countries are concerned about the idea of these capabilities falling into the hands of non-state actors for malicious use, whether that's in the context of biological weapons or other bio concerns, whether it's in the cybersecurity context we're reading so much about right now, AI plus cyber hacking.

These are issues that are not U.S. or China. These are global issues. And yet they're the two most consequential parties, the U.S. and China, that are leading the AI revolution, and therefore, it's one of the most important conversations that can be had right now is between them.

So, certainly it continues to be the case that this is a challenging relationship. These are challenging conversations to be had. But just as was true throughout the Cold War, when the U.S. and the Soviet Union, then Russia were able at times to sit together to talk about consequential national security interests, in the interest of broader global stability, this is going to have to be one of those issues, as hard and halting as it can often be.

[4:26]

HASS: One of the things that I have heard both in government but also since being out of government is a sense of skepticism about the role of Track II dialogues, which are dialogues between former officials and experts that don't have a government affiliation. What do you say to people who are cynical about the prospect that people who are not in government could play a role in advancing some of these discussions?

[4:46]

EDELMAN: Well, look, I, I’ve been there. I’ve been in government. You’ve been in government. I mean, the reality is, we, as those who are not presently in government, we are not the government. There is a absolutely important and critical distinction that is made there, for better and for worse. The reality is that one of the values of Track II dialogues is that it can be a venue in which not policies, but ideas of ways in which there can be overlap in policy can be explored. And it can be explored in a safe way where governments have total deniability in the outcomes of those processes.

There are other governmental processes that exist in exactly the same way. Right here at the UN, I was involved for years in a group of governmental experts on cybersecurity. It's a UN-based mechanism that exists, again, for experts to come together, try their best to anticipate where policy is going, and then devise, if not solutions, common understandings about that. And then the governments can choose to walk away. They can choose to pick up some of it or not.

But, having been inside government, as you have as well, truth is we don't have a lot of time to be sitting, developing 100-hour dialogues, 50-page studies of every element. We really hope and rely on deep expertise of those that can help inform that and to scope out directions that frankly may be more creative than those that we would necessarily have.

I don't think a Track II, it can ever claim it has more access than a Track I. Hopefully it has contributing better ideas than would otherwise be available in the absence.

[6:07]

HASS: Well, on that note, President Trump and President Xi have announced that the United States and China at a government-to-government level will will resume an official dialogue on artificial intelligence.

[6:16]

EDELMAN: Now you, Ryan Hass, have been in that seat. Right? I was there. You have run functionally the last state visit by Xi Jinping to the United States. Okay, so you've been through it. We've got this high-level statement. Our people, right, shall go talk about AI. What's the expectation there? When two leaders say that, on the Chinese side and on the U.S. side, what are they actually directing?

[6:40]

HASS: Well, I was going to ask you the question, but since you posed it to me, I'll just say a few things. First of all, the fact that the two leaders said this when they met in Beijing, knowing that they would see each other again in September in Washington, D.C., means that they are setting expectations that there will be some semblance of progress on AI issues between their last meeting and their next meeting. Otherwise, they wouldn't have gone to the effort of building the fanfare and the expectation around this issue.

The question then becomes, where is progress practical? And on that, I think that we need to learn a lesson from the last administration. The Biden administration tried once to have a AI dialogue with the Chinese.

EDELMAN: It didn't go great, as I understand.

HASS: It was shambolic.

EDELMAN: Okay.

HASS: Diplomatically unprepared. And as a consequence, both sides came into that meeting with different sets of expectations about the agenda and what would be achieved.

That mistake cannot repeat itself again. Instead, both sides need to do the diplomatic groundwork of making sure that they have aligned agendas, aligned expectations before they enter the room to have this next set of dialogues. And the issues that seem to be most animating right now, are around the ability of AI to amplify cyber threats and potential threats to critical infrastructure.

[7:54]

EDELMAN: I think we’ve also heard from a range of interlocutors, but the Chinese included, that this intersection of AI and bio is an area of real concern. That the idea that you might have rogue actors, particularly non-state actors, that would be in a position to actually engage what we think of as bio-terrorism, that’s an area that we’ve certainly heard about.

Now, will Xi and and Trump be able to talk about something that sensitive? Who knows. That's a pretty tall order.

[8:18]

HASS: You know, David, one other thing that I've learned over the seven years of us doing this dialogue with the Chinese is that progress doesn't travel on a linear path. It's very jagged. There are iterations of meetings where it feels like no progress is being made.

And then there are sort of step increases in the productivity of the dialogue. And I think that we should probably factor that into our assessment of what's happening at the government-to-government level as well, because this is a complicated set of

issues that are evolving in real time. And I think it'll be animated by where both sides identify mutual vulnerability and mutual risk, as well as mutual interest.

[8:50]

EDELMAN: Yeah, I think that's kind of the key of this idea of coming together, not for its own sake, not because of trust, but because of mutual interest, because there is this need that both sides have as the two most consequential superpowers, yes, but AI superpowers in this context.

And that sense of vulnerability and that the technology is moving more quickly than government can, that's something we say in the U.S. all the time. It's become kind of a cliché, and people have been saying this, I've been... you know, in government and technology for 15, 20 years, they're always saying that.

To hear it out of Beijing, the idea that technology is moving faster than they would say even their own government can keep up, that's actually a really important statement. I think it shows that even at this time of, you know, tension as we had under the Biden administration, obviously tensions persist now under the Trump administration, the idea that this is going to be an area where these two leaders think there either can or more importantly has to be some area of mutual agreement or mutual pursuit, that strikes me as pretty significant.

And I'll just say as someone involved in in technology and foreign policy for a long time, if you told me that, you know, the president of the United States and the president of China sitting down and one of the top five issues on their agenda would be AI or any tech issue at all, that's remarkable.

HASS: Yeah.

EDELMAN: And it's remarkable over a long sweep that we've seen from the shirt sleeves summit at Sunnylands talking to President Obama, and Obama brought up hacking as a major area of his concerns, specifically theft of intellectual property. You know, the relationship continued to be tense on those issues then.

And now, an issue that is also technological, that you could see being just as frankly poisonous to the relationship, where there's a sense that there's an arms race on, we talked about it earlier, an unhelpful frame, but people have framed it that way. The idea that these leaders are saying, Hey, you know what? We might be racing, we might have competition here. We might not trust one another approaching it, but we absolutely have to talk because this could be fundamentally destabilizing to our relationship, and as a result of that, to the global security picture.

That to me is a pretty important tell and an interesting point of real nonpartisan continuity across administrations in the U.S. as well.

[10:54]

HASS: I think that's a great point. But your, your other point is also really valid, which is that even though the United States and China are the two dominant actors in the space, they are not the only actors. We've just spent the last two days at the United

Nations listening to counterparts from around the world talking about governance issues. What are some of the things that you've heard?

[11:08]

EDELMAN: You know, what I’ve been surprised by most is the creativity or the range of ideas that people have about how to get their hands around this global AI governance question, which is not just one question, to be clear. AI governance is happening at at every level. It’s an economic issue, it’s a national security issue, and beyond.

But, you know, here at the UN, we're at the UN in Geneva, right? And which agencies and organizations live here? The ITU, the International Telecommunications Union. The United Nations Disarmament Agency is here. The International Atomic Energy Agency is also in Europe. You look at these agencies, and I think a lot of people around the world are looking for what can be the single location. It's almost a clearing house for a lot of these concerns.

Now, personally, I think that's kind of a tall order. One, international organizations, if national governments were having trouble keeping up with the speed of it, IOs might have even more trouble. So that's just a reality.

But, you know, we're hearing real clarity. I was there in the hallways and someone said, you know what we really need is an International Atomic Energy Agency, an IAEA for AI just like we have for nuclear weapons and nuclear power. That's a powerful idea. It has great clarity to it. It is also not lost on me that the head of the IAEA was addressing this very conference.

So I think you're gonna see this institutional pressure, not just from, you know, sort of the grassroots or the global majority as they're calling themselves, to, you know, talk about where can we deal with this issue, particularly for lower resource countries that might not have the capacity to do a lot of governance and that feel like they are receivers, not givers of the rules of AI, but want to be very involved in it. That desire for more unified governance at the intergovernmental level, it it's definitely gonna be there.

I think the question that we all have to ask ourselves now is what are the mechanisms that have worked in dealing with hard national security relevant technologies that, frankly, could benefit in certain areas from interlocking, I won't say overwhelming, but interlocking levels of governance at the international intergovernmental level.

## [13:07]

And that last word is really critical. It's kind of a line of UN speak. You know, we say things out here like the multi-stakeholder model and intergovernmental. What intergovernmental means, generally speaking, is that companies are not invited, that civil society is not invited. When you think about the history of internet policy and technology policy in the last 20-plus years, that multi-stakeholderism has been really important. It's been critical to preserving the long-term freedom and openness of the internet. It's been critical to preserving, you know, what we think of as its innovative potential. Oh, and by the way, turns out unlike nuclear weapons, AI is a private sector invention with a lot of help from academia fundamentally.

And so there is no state monopoly on AI that exists. And so when we think about these sort of governance paradigms to lay on top, yes, IAEA, or the CERN is another thing people have said is an international collaboration, there’s probably going to be a role for international organizations to find their space here and to figure out what they can uniquely work on and uniquely galvanize a particularly largely legitimate bloc.

But at the same time, we have to weigh this against the speed at which we need governance, and that is true at the domestic economic level, and it's just as true in the national security level as well. And that's why I suspect you're going to see conversations like U.S.-China remain not only vital, but somewhat counterintuitively at the forefront of this global dialogue precisely because they're the countries that have the most to gain and the most to lose from this going awry.

HASS: Well, David, thank you so much for adding so much insight into this conversation. We started out talking about a Track II dialogue between Brookings and Tsinghua. We expanded it to talk about the U.S.-China government-to-government dialogue and how it fits into the relationship between the two countries as well as the two leaders. And now we’ve closed by talking about the role of the United Nations’ international system in looking at governance issues related to these questions.

We've covered a ton of ground. This has been a really rich supplement to the June 23rd podcast on U.S. and China AI strategies. We will be back in Washington soon, so to our listeners, please stay tuned.

For more in-depth analysis from our team, visit the China Center on the Brookings website at Brookings dot edu slash ChinaCenter.

EDELMAN: Thanks, Ryan.

[music]

JON CZIN: On behalf of the team at the John L. Thornton China Center, thank you for listening to The Beijing Brief. This podcast is produced by the Brookings Podcast Network.

Our thanks to the production team, including supervising producer Ike Blake; senior producer Fred Dews; producer Allie Matthias; audio engineer Gastón Reboredo; and video producers Daniel Morales and Teddy Wansink. Rachel Slattery designed the show's artwork. Also, thank you to our colleagues in the John L. Thornton China Center, Foreign Policy, and Office of Communications at Brookings for their support.

To learn more about our research, visit us at Brookings dot edu slash China Center, and to learn more about this podcast, go to Brookings dot edu slash The Beijing Brief or wherever you like to get podcasts.
"""
