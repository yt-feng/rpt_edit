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
# China Internet & New Media

29 July 2026

EQUITY: INTERNET & NEW MEDIA

## Monthly App Tracker – June 2026

## Cross border ecommerce grapples with raised policy barriers in Europe

MAS rose $1.2\%$ y-y and total monthly time spent increased $10.1\%$ y-y in June  
Monthly active smartphone (MAS) users in China rose $1.2\%$ y-y to 1.28bn in June 2026. China's MAS has remained stable in recent months. Total monthly time spent (MTS) grew $8.6\%$ y-y in June, decelerating from $10.1\%$ y-y growth in May 2026.

## Shifting focus from consumer AI chatbots to business agents

According to Questmobile, Doubao [owned by Bytedance (unlisted)] appeared to have further widened its lead in the crowded field of AI native chatbots with DAU growth of 6% m-m and 3.3x y-y to 167mn. DeepSeek (unlisted) ranked second with DAU standing at 32.4mn, up 6% m-m and 1% y-y, followed by Alibaba's (BABA US, Buy) Qwen app (up 84x y-y and up 5% m-m to 29.3mn). According to Questmobile, 55% of Qwen users appeared to be casual users (daily time spent < 1 minute), for which the number increased 168x y-y in June. Qwen app's hardcore users (daily time spent > 1 minutes) accounted for 45% in June, down from 72% one year ago, for which the number increased 52x y-y. In comparison, the share of hardcore users of Doubao and DeepSeek stood at 85% and 81%, respectively, in June, largely stable compared with the levels a year ago. As a result, the average daily time spent per DAU (DTSD) of Qwen was much lower than that of Doubao and DeepSeek's. Among Chinese AI native chatbots, DeepSeek delivered the highest DTSD at 16.67mn in June 2026, up 65% y-y.

As major Chinese AI platforms are shifting focus from consumer AI towards business-oriented AI solutions, we project the competition in AI chatbots to further cool down which will be accompanied by slowing user engagement and declining marketing spent from major AI chatbot publishers down the road.

## Tencent's WorkBuddy maintains top spot among office AI agents

According to Analysys, a third-party research firm, Tencent's (700 HK, Buy) WorkBuddy remained the most popular desktop AI agent platform in China as of June 2026, with monthly visits surging to 21mn (up from 8.85mn in March). ByteDance's TRAE IDE (domestic version) ranked second, recording 12.79mn monthly visits (vs. 3.34mn in March), while Alibaba's QoderWork followed with 7.88mn visits (vs. 2.15mn in March).

This highlighted that internet giants are leveraging their ecosystem advantages to dominate the AI agent platform market at this stage. For instance, their super-apps—including office and business applications—serve as instant messaging platforms to seamlessly call the aforementioned AI agents, enhancing user accessibility.

Within traditional office applications, Feishu (owned by ByteDance) exhibited the strongest DAU growth at 51% in June 2026, according to Questmobile, likely partially driven by its smaller user base – its DAU is equivalent of 12–13% of DingTalk (owned by Alibaba) and WeCom's (owned by Tencent). Besides, WeCom sustained solid DAU growth of 10% in June, further narrowing its gap with DingTalk, which reported flat y-y DAU growth.

## DAU gap between Dou Sheng Sheng and Dianpian is narrowing

In February, Douyin LS launched an independent local service app, "Dou Sheng Sheng" (DSS). The DAU gap between DSS and Dianpian app [owned by Meituan (3690 HK, Buy)] is narrowing, thanks to the Douyin traffic support. According to QuestMobile data, Dianping app's DAU declined $2\%$ m-m to 32mn in June, while DSS's DAU grew $32\%$ m-m to 21mn, implying $65\%$ of Dianpian's level in June, up from $15\%$ in March. But, in terms of DTSD, Dianping app was at 8.3 minutes (down $3\%$ m-m), which is much higher than DSS's 4.5 minutes (down $3\%$ m-m), suggesting that Dianping may still

## Research Analysts

China Internet & New Media
Jialong Shi - NIHK
Jialong.shi@NOM.com
+852 2252 1409

Rachel Guo - NIHK

rachel.guo@NOM.com +852 2252 1400

Production Complete: 2026-07-29 10:34 UTC

## enjoy higher user engagement.

Chinese cross-border ecommerce platforms decelerating in major overseas markets

According to Sensor Tower, Temu's [owned by PDD (PDD US, Neutral)] global monthly active users (MAU) reverted to a 2% y-y decline in June 2026 (vs. 2% growth in May 2026), primarily driven by weakened MAU performance in Latin America and Europe, which offset its robust growth in the US (due to low base a year ago caused by the US's tariff hike and import policy change). QuestMobile data corroborates this trend, showing that Temu's sellers' DAU down 11% y-y in June 2026.

Similarly, Shein's global MAU decelerated to $5\%$ y-y in June 2026 (vs. $14\%$ y-y in May 2026), with strong user growth in Brazil and India offsetting declines in Europe.

Overall, it seems that Temu and Shein's global user base is stabilizing, while both are witnessing a drop of users lately in their European markets, where tightening regulations against imported merchandise—including the removal of de minimis exemptions for low-value cross-border products and the introduction of additional tariffs—officially took effect on 1 July 2026. We will monitor closely whether and how these Chinese cross-border ecommerce platforms will navigate these tough market conditions smoothly.

## Overview of leading Chinese apps

Much of the traffic flow in June 2026 was dominated by apps owned by Bytedance, Tencent, Baidu (BIDU US, Buy), and Alibaba. In particular, Bytedance's apps took five spots among the Top-20 in terms of both monthly active users (MAU) and time spent share in June, according to QuestMobile. Tencent's WeChat alone recorded a $19.3\%$ share in terms of time spent by Chinese mobile users, leading the next two apps – Douyin and Douyin Lite (both unlisted, owned by Bytedance) – with $19\%$ and $6.3\%$ time-spent share, respectively.

Fig. 1: Top-20 apps in China, by MAU and time spent – June

<table><tr><td colspan="5">Top 20 Apps in MAU: MAUs change and penetration</td></tr><tr><td>App Name</td><td>Rank M-M chg</td><td>Penetration</td><td>Penetration Y-Y</td><td>Penetration M-M</td></tr><tr><td>WeChat</td><td>-</td><td>90.0%</td><td>2.9ppt</td><td>0.0ppt</td></tr><tr><td>Douyin</td><td>-</td><td>80.3%</td><td>8.1ppt</td><td>-0.1ppt</td></tr><tr><td>Taobao</td><td>-</td><td>76.7%</td><td>-0.6ppt</td><td>-0.4ppt</td></tr><tr><td>Alipay</td><td>-</td><td>74.3%</td><td>0.6ppt</td><td>0.7ppt</td></tr><tr><td>Amap</td><td>-</td><td>71.2%</td><td>0.3ppt</td><td>-1.2ppt</td></tr><tr><td>Pinduoduo</td><td>-</td><td>54.9%</td><td>-2.8ppt</td><td>-0.9ppt</td></tr><tr><td>Sogou Keyboard</td><td>-</td><td>54.5%</td><td>4.1ppt</td><td>0.1ppt</td></tr><tr><td>JD</td><td>-</td><td>52.7%</td><td>2.4ppt</td><td>2.0ppt</td></tr><tr><td>Baidu</td><td>-</td><td>50.0%</td><td>-5.3ppt</td><td>-0.7ppt</td></tr><tr><td>QQ</td><td>-</td><td>48.9%</td><td>-1.6ppt</td><td>-0.4ppt</td></tr><tr><td>Baidu Maps</td><td>-</td><td>44.1%</td><td>-1.9ppt</td><td>-0.7ppt</td></tr><tr><td>Meituan</td><td>-</td><td>40.7%</td><td>0.3ppt</td><td>-0.3ppt</td></tr><tr><td>Baidu Keyboard</td><td></td><td>38.7%</td><td>-0.5ppt</td><td>0.0ppt</td></tr><tr><td>Weibo</td><td></td><td>38.6%</td><td>-0.3ppt</td><td>0.0ppt</td></tr><tr><td>Kuaishou</td><td>-</td><td>34.4%</td><td>-1.9ppt</td><td>-0.9ppt</td></tr><tr><td>Doubao</td><td></td><td>29.8%</td><td>18.7ppt</td><td>1.0ppt</td></tr><tr><td>Toutiao</td><td></td><td>29.1%</td><td>-2.2ppt</td><td>-0.8ppt</td></tr><tr><td>Red Fruit Free Short Drama</td><td>-</td><td>28.7%</td><td>12.0ppt</td><td>0.8ppt</td></tr><tr><td>QQ Browser</td><td>-</td><td>26.1%</td><td>-7.4ppt</td><td>-0.7ppt</td></tr><tr><td>Douyin Lite</td><td>-</td><td>25.7%</td><td>3.0ppt</td><td>-0.3ppt</td></tr></table>

Source: QuestMobile, NOM

<table><tr><td colspan="5">Time spent share for top 20 Chinese mobile apps in June</td></tr><tr><td>App Name</td><td>Rank M-M chg</td><td>Time spent share</td><td>Time spent share Y-Y</td><td>Time spent share M-M</td></tr><tr><td>WeChat</td><td>-</td><td>19.3%</td><td>-1.3ppt</td><td>0.3ppt</td></tr><tr><td>Douyin</td><td>-</td><td>19.0%</td><td>2.7ppt</td><td>0.3ppt</td></tr><tr><td>Douyin Lite</td><td>-</td><td>6.3%</td><td>1.0ppt</td><td>0.0ppt</td></tr><tr><td>Red Fruit Free Short Drama</td><td>-</td><td>4.5%</td><td>2.5ppt</td><td>0.5ppt</td></tr><tr><td>Kuaishou</td><td>-</td><td>3.8%</td><td>-1.0ppt</td><td>-0.1ppt</td></tr><tr><td>Sogou Keyboard</td><td>-</td><td>3.1%</td><td>-0.1ppt</td><td>0.0ppt</td></tr><tr><td>Toutiao</td><td>-</td><td>2.7%</td><td>-0.5ppt</td><td>-0.1ppt</td></tr><tr><td>Rednote</td><td></td><td>2.3%</td><td>-0.1ppt</td><td>0.1ppt</td></tr><tr><td>Kuaishou Express</td><td></td><td>2.3%</td><td>-0.4ppt</td><td>0.0ppt</td></tr><tr><td>Pinduoduo</td><td></td><td>2.2%</td><td>-0.1ppt</td><td>-0.1ppt</td></tr><tr><td>Fanqie Free Novels</td><td></td><td>1.9%</td><td>0.0ppt</td><td>0.0ppt</td></tr><tr><td>Baidu Keyboard</td><td></td><td>1.9%</td><td>-0.4ppt</td><td>-0.2ppt</td></tr><tr><td>Weibo</td><td></td><td>1.8%</td><td>-0.2ppt</td><td>-0.1ppt</td></tr><tr><td>Taobao</td><td>-</td><td>1.7%</td><td>-0.1ppt</td><td>-0.1ppt</td></tr><tr><td>Bilibili</td><td>-</td><td>1.7%</td><td>0.0ppt</td><td>0.0ppt</td></tr><tr><td>Baidu</td><td></td><td>1.5%</td><td>-0.6ppt</td><td>-0.1ppt</td></tr><tr><td>Sina News</td><td></td><td>1.4%</td><td>-0.1ppt</td><td>-0.2ppt</td></tr><tr><td>Alipay</td><td></td><td>1.2%</td><td>0.1ppt</td><td>0.1ppt</td></tr><tr><td>Honour of Kings</td><td></td><td>1.2%</td><td>0.1ppt</td><td>-0.1ppt</td></tr><tr><td>Tencent News</td><td>-</td><td>1.0%</td><td>-0.2ppt</td><td>-0.1ppt</td></tr></table>

Among the Top-50 apps, which accounted for \~93% of the total mobile time spent in China during June, we note that the Bytedance camp gained time-spent share on a y-y basis, which rose from 33.3% in June 2025 to 40.1% in June 2026, surpassing Tencent camp's 29.7%. Sequentially, Bytedance's time-spent share was up 0.9pp m-m.

Fig. 2: Time-spent share of various internet camps among the Top-50 apps in China  
![](images/2e98ff9232b15ec77c8023787e450ee3eff493624b9927875f033298cdb0d650.jpg)  
Source: QuestMobile, NOM

## Long-form vs short-form dramas

Long-form video apps remained weak in June. The MTS of Tencent Video (owned by Tencent) recorded a 34% y-y decline in June, dragged by a 25% decline in DAU and a 12% decline in DTSD. Youku (owned by BABA)/Mango TV (300413 CH, Not rated)/iQIYI (IQ US, Neutral) recorded 47%/3%/11% y-y declines in total time spent, mainly dragged by 34%/9%/16% declines in DAU.

The dominant short-form drama app – Red Fruit Free Short Drama (owned by Bytedance)—kept its strong growth trend with an MTS increase of 145%, backed by 106% growth in DAU and 19% growth in DTSD.

Fig. 3: DAUs of long-form vs short-form dramas apps  
![](images/527568829c36915ab8e61c4d4e7290b334727e95dffe0f8411d2d3f938b124fe.jpg)  
Source: QuestMobile, NOM

Fig. 4: Average daily time spent per user  
![](images/ae51d162463a8953785b5bf4043c2cf22f11e92776475e49472e1971d49f7cc1.jpg)  
Source: QuestMobile, NOM

## Short video

In June, Douyin maintained its solid growth momentum in terms of MTS, at 27% y-y, mainly driven by 20% growth in DAU. Total time spent for Bilibili (BILI US, Neutral) recorded 7% y-y growth in June, driven by 5% y-y growth in DAU and 3% growth in DTSD. However, Kuaishou (1024 HK, Neutral) continued its relatively soft performance, with a decline of 14% y-y in MTS, mainly dragged by a 13% y-y decline in DTSD.

Fig. 5: DAUs of short video apps  
![](images/617744cd65c40b214d46af2cbfb9a4b4630095e9fb180be95dae0424d7d4d89b.jpg)  
Source: QuestMobile, NOM

Fig. 6: Average daily time spent per user  
![](images/8bf8f087c15e3b9f76188ecca528fb3f0fe867302f4812cb288c16e3597d915a.jpg)  
Source: QuestMobile, NOM

## Online reading

The MTS of the free reading app leader Tomato Free Novels (unlisted; owned by ByteDance) showed decelerating growth trend at 8% y-y in June (from 12% in May 2026), mainly backed by an increase of 8% y-y in DAU. Another free reading app, Qimao Free Novels (unlisted) continued its downward trend with a 44% y-y decline in total time spent, dragged by 31% and 20% y-y declines in DAU and DTSD, respectively.

Paid reading apps owned by China Literature (772 HK, Buy), i.e., Qidian reading and QQ reading also appeared soft user engagements, recording respective declines of $8\%$ and $7\%$ on a y-y basis in DAU during the month, and their DTSDs each down by $10\%$ y-y.

Fig. 7: DAU of online reading platforms  
![](images/9768d7ad672fa2e604ab9836874773eac3371f4241a6be3d4473a85a023bfca5.jpg)  
Source: QuestMobile, NOM

Fig. 8: Average daily time spent per DAU of online reading platforms  
![](images/4d18e017f7bcb0b342a9cda5617f02872ee508d35d35baa6a55d6845b44f0fab.jpg)  
Source: QuestMobile, NOM

## Live broadcasting

Live broadcasting show apps maintained their y-y downward trend in MTS in June. However, Momo's (MOMO US, Not rated) overall user engagement appeared more resilient compared to YY (owned by Baidu). The MTS of Momo dropped 12% y-y in June 2026, mainly owing to 11% decline of DAU. Comparably, YY's MTS reduced 17% y-y, mainly dragged by 14% decline in DTSD.

Fig. 9: DAUs of live broadcasting show apps  
![](images/f76970a1bc38bf3f3ea0cd88bc895ecdf4d63af6798751046c14aca50869363c.jpg)

Fig. 10: Average daily time spent per user  
![](images/359ecbf5320254ab96011e1b52ccee6d018f737934fb4dbd25a67d7bc83e0b0c.jpg)  
Source: QuestMobile, NOM  
Source: QuestMobile, NOM

For game live broadcasting apps, the MTS for Huya (HUYA US, Not rated) recorded a $14\%$ decline in June, mainly dragged by a $16\%$ y-y decline in DAU. The MTS for Douyu (DOYU US, Not rated) recorded $2\%$ y-y decline in June, dragged by a $12\%$ y-y decline in DAU, offsetting $11\%$ y-y growth in DTSD.

Fig. 11: DAUs of game live broadcasting apps  
![](images/3f18bde4151de6292204872c0e16c5869218aa0d5d9497c43e4ae02521bae952.jpg)  
Source: QuestMobile, NOM

Fig. 12: Average daily time spent per user  
![](images/65128d97bf7a8b20c12cd4a1cee9a046f518c0f38c62611efe29f0fd4f468539.jpg)  
Source: QuestMobile, NOM

## Music

The y-y decline in DAU continued for most part of the music universe, except for Soda Music and Tomato Music (both owned by ByteDance), which recorded 77% and 43% y-y growth, respectively, in June. Against the competition from the emerging Soda Music and Tomato Music, NetEase Cloud Music (9899 HK, Not rated) remained relatively stable user scale, with 1% y-y growth of DAU in June. However, the music apps [owned by TME (TME US, Buy)], i.e. QQ Music/Kugou Music/Kuwo Music were experiencing user churn, down 5%/13%/14% y-y in terms of DAU in June (as shown in Fig. 13).

Tencent Karaoke maintained its y-y downward trend in MTS, with a 22% y-y decline, mainly dragged by a 28% y-y drop in DAU, offsetting 9% y-y growth in DTSD in June (as shown in Fig. 14).

Fig. 13: DAUs of music streaming apps  
![](images/e4501a192b4f23b15a520606c3a0c5d756a2861462cda0411ce0763793df7acf.jpg)  
Source: QuestMobile, NOM

Fig. 14: DAUs of online karaoke app  
![](images/f0a07402fd19f21d5aa1c4422f07824de922e111d6c2cab4d9ce40a2e02eadf8.jpg)  
Source: QuestMobile, NOM

## Social

The MTS of Xiaohongshu (unlisted) recovered to $3\%$ y-y growth in June, mainly driven by $4\%$ y-y growth in DAU, driven by the exclusive online streaming right secured for the FIFA World Cup 2026 in China, in our view. The MTS of Weibo (WB US, Neutral) declined $3\%$ y-y in June, dragged by a $3\%$ decline in DTSD. Within Tencent's social ecosystem, QQ maintained its downward trend in MTS, with a $4\%$ y-y decline, while WeChat recorded $2\%$ y-y growth in terms of total time spent in June.

Fig. 15: DAUs of social apps  
![](images/064eaa0c5cbc085dc7a016478ae07c4fd0cbaa9779afe7bfc9d0ea04cd99a4e4.jpg) 

[中间内容因长度限制已省略]

bai Financial Services Authority) in the United Arab Emirates ('UAE') or a 'Market Counterparty' or a 'Business Customer' (as defined by the Qatar Financial Centre Regulatory Authority) in the State of Qatar ('Qatar') by NOM Saudi Arabia, NIplc or any other member of the NOM Group, as the case may be. Neither this document nor any copy thereof may be taken or transmitted or distributed, directly or indirectly, by any person other than those authorised to do so into Saudi Arabia or in the UAE or in Qatar or to any person other than 'Authorised Persons', 'Exempt Persons' or 'Institutions' located in Saudi Arabia or a 'Market Counterparty' or a 'Professional Client' in the UAE or a 'Market Counterparty' or a 'Business Customer' in Qatar. Any failure to comply with these restrictions may constitute a violation of the laws of the UAE or Saudi Arabia or Qatar.

For report with reference of TAIWAN public companies or authored by Taiwan based research analyst:

THIS DOCUMENT IS SOLELY FOR REFERENCE ONLY. You should independently evaluate the investment risks and are solely responsible for your investment decisions. NO PORTION OF THE REPORT MAY BE REPRODUCED OR QUOTED BY THE PRESS OR ANY OTHER PERSON WITHOUT WRITTEN AUTHORIZATION FROM NOM GROUP. Pursuant to Operational Regulations Governing Securities Firms Recommending Trades in Securities to Customers and/or other applicable laws or regulations in Taiwan, you are prohibited to provide the reports to others (including but not limited to related parties, affiliated companies and any other third parties) or engage in any activities in connection with the reports which may involve conflicts of interests. INFORMATION ON SECURITIES / INSTRUMENTS NOT EXECUTABLE BY NOM INTERNATIONAL (HONG KONG) LTD., TAIPEI BRANCH IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT BE CONSTRUED AS A RECOMMENDATION OR A SOLICITATION TO TRADE IN SUCH SECURITIES / INSTRUMENTS.

This material may not be distributed in Indonesia or passed on within the territory of the Republic of Indonesia or to persons who are Indonesian citizens (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia. The securities mentioned in this document may not be offered or sold in Indonesia or to persons who are citizens of Indonesia (wherever they are domiciled or located) or entities of or residents in Indonesia in a manner which constitutes a public offering under the laws of the Republic of Indonesia.

An individual name printed next to NOI on the front page of a research report indicates that this document is a translation of a research report issued by NOI in the PRC. In all other cases, this document is prepared by NOM Group or its subsidiary or affiliate (collectively, "Offshore Issuers") that is not licensed in the PRC to provide securities research. This research report is not approved or intended to be circulated in the PRC. The A-share related analysis (if any) is not produced for any persons located or incorporated in the PRC. The recipients should not rely on any information contained in this research report in making investment decisions and Offshore Issuers take no responsibility in this regard. NO PART OF THIS MATERIAL MAY BE (I) COPIED, PHOTOCOPIED, REPRODUCED OR DUPLICATED IN ANY FORM, BY ANY MEANS; OR (II) REDISSEMINATED, REPUBLISHED OR REDISTRIBUTED WITHOUT THE PRIOR WRITTEN CONSENT OF A MEMBER OF THE NOM GROUP. If this document has been distributed by electronic transmission, such as e-mail, then such transmission cannot be guaranteed to be secure or error-free as information could be intercepted, corrupted, lost, destroyed, arrive late or incomplete, or contain viruses. The sender therefore does not accept liability (in negligence or otherwise, and in whole or in part) for any errors or omissions in the contents of this document, which may arise as a result of electronic transmission. If verification is required, please request a hard-copy version.

The NOM Group manages conflicts with respect to the production of research through its compliance policies and procedures (including, but

not limited to, Conflicts of Interest, Chinese Wall and Confidentiality policies) as well as through the maintenance of Chinese Walls and employee training.

Additional information regarding the methodologies or models used in the production of any investment recommendations contained within this document is available upon request by contacting the Research Analysts of NOM listed on the front page. Disclosures information is available upon request and disclosure information is available at the NOM Disclosure web page: http://go.NOMnow.com/research/m/Disclosures

Copyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved.
"""
