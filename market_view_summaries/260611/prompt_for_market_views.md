请基于下面每天新报告的摘要，写一份“市场最新观点汇总”的结构化 JSON，用于生成 PDF。

要求：
1. 观点要分门别类，例如：宏观与利率、AI/算力、能源与大宗、地产与消费、区域市场、风险偏好等。类别由内容决定，不要机械套模板。
2. sections 建议 8-12 个，尽量覆盖所有报告 ID；references 合并后应覆盖大多数甚至全部报告。
3. 每个板块要综合多篇报告，不要逐篇复述，但不能只写高度抽象的空话。
4. 每个板块必须有 5-10 个要点，每个要点是可读的完整句子，保留关键数据、方向和分歧。
5. 每个板块末尾必须给 references，引用报告 ID，不要在正文每句后塞引用。
6. 可以使用所有 figure_ids，没有总数限制，但只选择真正支撑该板块观点且图表说明干净的图。
7. 投行名字必须脱敏：常见投行写 GS、JPM、MS、BofA、Citi、UBS、DB 等缩写，不确定就写“投行”。
8. 不要给投资建议，不要写买卖评级。
9. 输出必须是 JSON 对象，不要 Markdown 代码块。

JSON 格式：
{"title":"市场最新观点汇总","subtitle":"一句话说明今天的市场主线","executive_summary":["要点1"],"sections":[{"heading":"板块标题","thesis":"核心判断","bullets":["要点1"],"figure_ids":["F001"],"references":["R001"]}],"closing":"简短收束"}

报告摘要：
[
  {
    "id": "R001",
    "title": "NOM：中国通胀的结构性真相——市场低估了供给驱动的持续性，高估了需求复苏的弹性",
    "digest": "[wechat_article.md]\n# NOM：中国通胀的结构性真相——市场低估了供给驱动的持续性，高估了需求复苏的弹性\n\n中国5月通胀数据公布后，市场的主流叙事是“通胀温和，政策空间犹存”。CPI同比持平于1.2%，PPI同比升至3.9%，似乎验证了经济温和复苏、通胀压力可控的判断。但NOM这份最新研报揭示了一个更复杂的图景：当前通胀并非需求回暖的信号，而是一场由外部供给冲击主导的“成本推入式”再定价。市场真正需要关注的，不是通胀本身的高低，而是这种通胀的结构——它正在挤压企业利润、侵蚀居民购买力，并可能迫使政策在“稳增长”与“防输入性通胀”之间做出更艰难的选择。\n\n这份报告的核心判断是：中国通胀已经走出了通缩，但走向的并非温和复苏，而是一种“类滞胀”的初期形态。PPI的高企主要由能源和AI相关材料驱动，剔除这两项后，PPI可能仍是负值。而CPI的稳定，则更多依赖能源价格的基数效应，而非消费需求的真正回暖。这意味着一件事：如果外部供给约束持续，中国将面临“成本上升但需求不足”的尴尬局面，这比单纯的通缩或通胀都更难应对。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 当前通胀的“双轨制”：上游热、下游冷，中间环节的利润正在被系统性压缩\n\nNOM报告中最具穿透力的观察，在于对通胀结构性的拆解。5月PPI同比3.9%的读数，看似强劲，但它的驱动力高度集中。NOM估算，能源和AI相关材料两项合计贡献了PPI通胀的3.96个百分点。换句话说，剔除这两个板块，PPI通胀将是负值。\n\n具体来看，石油相关行业（占PPI篮子约14%）贡献了1.90个百分点，有色矿采和加工业贡献了1.80个百分点，科技制造业贡献了0.26个百分点。而下游消费品部门的PPI通胀仍为负值（-0.8%），尽管较4月的-1.0%有所改善，但依然处于收缩区间。\n\n这意味着什么？当前的通胀不是\n\n[... middle omitted ...]\n\n类滞胀场景下的推演”等议题，展开更深入的讨论。期待你的加入。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月物价数据：一张图看懂通胀逻辑\n\nCPI持平，PPI继续涨\n\n**5月通胀数据出炉：CPI持平1.2%，PPI跳升至3.9%**\n\n刚看了某外资投行最新的通胀研报，信息量很大，帮你拆解一下5月物价数据的核心逻辑👇\n\n**1/ CPI为什么没动？**\n- 汽油涨价贡献了CPI一半涨幅（同比+23.5%），但猪肉价格跌了16.1%，拖累明显\n- 核心CPI（剔除食品和能源）反而微降，服务价格走弱\n- 鸡蛋涨价6.6%，手机平板小幅上涨（AI需求带动），但整体消费端还是偏弱\n\n**2/ PPI跳升背后：能源+AI双主线**\n- 5月PPI同比3.9%，创近三年新高\n- 能源相关行业贡献约1.96个百分点（石油开采同比+35.7%）\n- 有色金属（铜等）贡献1.8个百分点，AI相关电子设备贡献0.26个百分点\n- 但涨价集中在最上游，下游消费品PPI还是负的（-0.8%），说明涨价还没传导到消费者\n\n**3/ 研报上调了全年预测**\n- 全年CPI预测从0.6%上调至0.9%\n- 全年PPI预测从1.0%上调至2.5%\n- 主要原因是油价高位+AI需求持续推升芯片价格\n\n**4/ 一个值得注意的视角**\n研报提到，\n\n[... middle omitted ...]\n\nsome emerging support from consumer electronic products due to rising chip prices. Meanwhile, food prices remained a serious drag, as pork prices failed to rebound after hitting a 16-year low.\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R002",
    "title": "DB：中国贸易数据揭示的不是短期反弹，而是供给优势的再定价",
    "digest": "[wechat_article.md]\n# DB：中国贸易数据揭示的不是短期反弹，而是供给优势的再定价\n\n这份由DB在2026年6月9日发布的宏观报告，核心判断不是“出口又变好了”这样的短期叙事。报告真正值得关注的信号是：中国贸易的结构性驱动力正在从单纯的规模扩张，转向以AI相关产品、能源密集型产品为代表的定价权优势。5月出口同比增长19.4%，进口增长27.4%，但这组数字背后的含义远比表面增速更深刻。\n\n市场习惯将中国贸易数据解读为全球需求的晴雨表，或者简单归结为基数效应。DB的报告提供了一个不同的框架：它把增长拆解为“AHEAD”因素——AI相关产品、汽车、其他机械——并发现这些因素贡献了16个百分点的出口增长。这意味着，即便剔除全球周期的影响，中国自身的供给能力正在成为贸易增长的主引擎。\n\n为什么现在这个判断重要？因为全球投资者正在重新评估中国资产的定价逻辑。如果贸易增长主要依赖的是中国在AI硬件、能源密集型产业的成本与技术优势，而不是单纯的外部需求拉动，那么这种增长的可持续性和质量都会不同。这对于汇率预期、产业投资方向、甚至全球供应链的重新布局都有直接的含义。\n\n报告提出的一个关键观察是：AI相关出口在5月同比增速翻倍至81%，其对整体出口的贡献从1-4月的5个百分点跃升至10个百分点。这不是一个边际变化，而是量级上的跃迁。与此同时，能源和石化产品的出口也显著走强——精炼油出口从-1%反弹至27%，塑料制品从7%加速至12%。这两条线索叠加在一起，指向一个更根本的叙事：中国正在将其在制造业和能源领域的规模优势，转化为全球贸易中的定价权。\n\n以下是我们从这份报告中提炼出的五个层次判断，它们共同支撑一个核心主张：市场低估的不是中国贸易的短期韧性，而是供给侧优势正在被重新定价。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮贸易加速中，AI相关\n\n[... middle omitted ...]\n\n他机构的交叉验证，深入探讨这些未解问题背后的投资与产业含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月出口数据，有点意思\n\n出口新高，AI贡献翻倍\n\n5月出口增速继续冲高，从1-4月的14%拉到19.4%，季调后的出口量创历史新高。\n\n核心驱动力还是“AHEAD”因素（AI、汽车、其他机械等），贡献了16个百分点的增长。其中AI相关出口环比翻倍，从42%飙到81%，贡献从5ppt升到10ppt。\n\n另一个亮点是能源和石化出口明显走强。精炼油从-1%反弹到+27%，塑料从7%加速到12%，说明中国在能源密集型产业的定价优势正在释放。\n\n1/ 发达市场意外回暖\n- 新兴市场保持18%左右的增速，贡献6ppt\n- 发达市场（美日韩台）合计增速从2%跳升到30%\n- 美国反弹主要因为去年5月基数低+关税缓和\n- 核心还是AI需求拉动\n\n2/ 进口也跟上了\n- 进口增速从23%升到27.4%\n- 能源进口滞后反映：3-4月主要供应商的出口增加，5月才在国内数据体现\n- 原油、煤炭、天然气进口都显著提速\n\n3/ 全年展望\n研报维持12%出口、15%进口的预测，认为如果能源石化继续走强，存在上行风险。同时看好人民币，预计2026年底到6.55，2027年进一步到6.30。\n\n值得留意的是，AI相关出口的爆发力还在持续增\n\n[... middle omitted ...]\n\nm 5ppts. In addition, energy and petrochemical exports strengthened notably, with refined oil exports rebounding from -1% to +27% YoY, and plastics accelerating from 7% to 12% YoY. This unders\n\n[... middle omitted ...]\n\n8000</td><td>DB Securities Inc.The DB Center1 Columbus CircleNew York, NY 10019Tel: (1) 212 250 2500</td><td>DB AGFiliale SingapurOne Raffles Quay, SouthTowerSingapore 048583Tel: (65) 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R003",
    "title": "摩根斯坦利：印度真正需要解决的，不是短期资本流入，而是制造业竞争力的结构性缺口",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：印度真正需要解决的，不是短期资本流入，而是制造业竞争力的结构性缺口\n\n市场对印度近期的政策反应普遍积极——取消资本利得税、扩大政府债券投资范围、提高海外个人投资限额，一系列措施密集出台。但摩根斯坦利最新发布的亚洲宏观报告提出了一个冷静的判断：这些措施能缓解短期压力，但无法解决根本问题。\n\n这份由首席亚洲经济学家Chetan Ahya领衔的报告，核心论点是：印度面临的不是流动性问题，而是国际收支的结构性承压。而解决这一压力的唯一路径，是制造业竞争力的系统性提升。资本账户管理只是治标，制造业出口能力的建设才是治本。\n\n报告的数据框架清晰地展示了问题的严重性：2024年12月至2026年3月，印度国际收支累计录得520亿美元的赤字。这个数字是2011-2013年期间250亿美元赤字的两倍以上。更值得关注的是，卢比的实际有效汇率已经跌至低于10年均值3.7个标准差的位置——这不是短期波动，而是系统性的失衡信号。\n\n本文将从五个层次拆解这份报告的核心洞察，并在最后提出一个报告尚未完全回答的关键问题，供读者进一步思考。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 资本外流的根源不是市场情绪，而是相对盈利增速的结构性分化\n\n许多市场观察者将印度的资本外流归因于地缘政治风险或全球利率环境。但摩根斯坦利的分析揭示了更深层的原因：印度企业的相对盈利增速正在失去吸引力。\n\n报告提供了一组关键对比数据：2026年第一季度，印度BSE500指数成分股盈利同比增长13%。这个数字本身并不差，但放在区域比较中就显得苍白——韩国KOSPI指数盈利增长171%，台湾加权指数增长49%，日本TOPIX增长33%，美国标普500增长29%。印度是主要经济体中盈利增速最低的几个之一。\n\n这意味着什么？全球资本正在重新定价“增长溢价”。\n\n[... middle omitted ...]\n\n报告的解读、原始图表，以及更多关于亚洲制造业格局的深度分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n印度制造，这次真的不能再拖了\n\n印度制造，为何是关键\n\n最近某外资行研报点出一个核心问题：印度短期资金压力有解，但中期必须靠制造业突围。\n\n1/ 短期压力已缓解\n印度央行近期推了一波措施：取消国债资本利得税、放宽外资买债限制、提高海外个人投资额度、给国企外币借款提供汇率对冲。这些能暂时稳一稳资本流动。\n\n2/ 但中期缺口还在\n2024年底到2026年3月，印度国际收支赤字已达520亿美元，是2011-2013年期间的两倍多。更关键的是，经常账户赤字预计从F26的0.6%扩大到F27的1.8%，光靠短期措施不够。\n\n3/ 制造业是双重解药\n提升制造业竞争力→扩大商品出口→缩小经常账户赤字。\n同时制造业能吸引外资流入→双管齐下改善国际收支。\n研报特别指出：印度需要提升全价值链制造能力，瞄准高增长行业，整合供应链，加大研发投入，培养技能人才。\n\n4/ 为什么资金在流出？\n过去两年外资持续流出，原因是：印度企业盈利增速放缓（到去年9月才触底反弹），而AI主题让韩国、台湾等市场盈利增长更抢眼（韩国一季度盈利增长171%，印度只有13%）。加上能源价格冲击，印度的相对吸引力在减弱。\n\n油价如果继续跌，经常账户压力会缓解，\n\n[... middle omitted ...]\n\nstainably to meet the rising need for investment.  \n- India should focus on lifting goods exports competitiveness and boosting manufacturing capabilities across the value chain.  \nManufacturin\n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R004",
    "title": "Bernstein：AI不是音乐的威胁，而是超级粉丝变现的桥梁",
    "digest": "[wechat_article.md]\n# Bernstein：AI不是音乐的威胁，而是超级粉丝变现的桥梁\n\n音乐产业正在经历一场被市场低估的结构性转变。当大多数讨论聚焦于AI是否将取代人类创作时，一份来自Bernstein的最新研报提出了相反的判断：AI恰恰是唱片公司实现“超级粉丝”变现的关键工具，而非生存威胁。\n\n这份报告的触发点来自Spotify最近的投资者日活动。当天最重磅的公告不是用户增长或定价策略，而是一份史无前例的授权协议——Spotify与环球音乐集团达成合作，允许Premium用户基于授权曲库付费创作AI翻唱和混音版本。这是全球主流流媒体平台与主要唱片公司之间首次建立基于“同意、署名和补偿”原则的AI音乐框架。\n\nBernstein团队长期认为，AI是唱片公司实现超级粉丝变现的桥梁，而非行业颠覆者。这份协议就是最清晰的证据。从Suno和Udio最初闯入AI音乐领域至今不过短短数年，整个品类已经可以通过全球最大音乐平台的框架，演变为唱片公司明确的增长引擎。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 超级粉丝附加服务正在创造一块完全增量的版税池\n\n理解这一变化的关键在于：这不是对现有流媒体收入的重新分配，而是在其之上叠加的全新收入层。\n\nSpotify管理层在投资者日上明确了一个核心洞察——用户的付费意愿遵循幂律分布。头部一小部分高度活跃的用户愿意支付远超标准订阅费用的金额。公司不再试图仅通过提价和增加订阅人数来扩大音乐收入池，而是通过付费附加服务来捕获这部分“超级粉丝”的价值。\n\n与环球音乐达成的翻唱和混音协议，正是这一策略在版权方层面的首次落地。它的结构是付费Premium附加服务，录音版权所有者和词曲作者共同分享粉丝创作带来的收益。对行业而言，最关键的信号是：这笔收入是增量。它叠加在流媒体收入之上，而非重新分配现有池子。而且，由\n\n[... middle omitted ...]\n\nstein的原始图表，也会定期组织对这些关键假设的跟踪讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n音乐行业正在经历一个关键转折：超级粉丝经济要来了\n\n超级粉丝经济来了\n\nAI让平台开始为“创作”付费\n\n最近Spotify投资人日释放了一个重要信号。它和环球音乐签了一个全新授权协议——Premium用户可以为喜欢的歌做AI翻唱和混音，平台会为此单独付费。\n\n这不是普通的版权续约，而是一个全新的收入池。\n\n1/ 超级粉丝的付费意愿远超想象\nSpotify管理层提到一个核心洞察：用户的付费意愿呈“幂律分布”——少数重度用户愿意支付远高于标准订阅费的价格。与其提高所有人的月费，不如给这群人提供增值服务。\n\n参考Audiobooks+的数据：上线不到一年，100万用户付费，年化收入约1亿美元。相当于每人每月多付8美元，渗透率仅0.3%。\n\n2/ AI翻唱/混音正在创造增量\n核心逻辑是：这个新收入是“加在”现有流媒体收入之上的，而不是重新分配。因为用的是已有版权库，不需要增加播放时长就能产生新收入。\n\n保守估算：2%的用户愿意每月多付5美元，Spotify每年多赚3.5亿美元，版权方分到约2.1亿美元，相当于现有流媒体收入的1.9%。\n\n基准情景：5%渗透率×8美元/月，版权方年增收8.4亿美元，提升7.7%。\n\n3\n\n[... middle omitted ...]\n\n850e537bf120c1925ef24d7d6ffd12d.jpg)\n\nMin-Joo Kang\n\n+852 2123 2644\n\nminjoo.kang@bernsteinsg.com\n\n![](images/3e14e9fead89bc65916dd6a4ae2f73c4a6e1ac157fd0277f9b3951c5932d4acb.jpg)\n\nNosher Ali Kh\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R005",
    "title": "GS：欧洲半导体公司的估值重估才刚刚开始，市场低估了AI对功率半导体的需求弹性",
    "digest": "[wechat_article.md]\n# GS：欧洲半导体公司的估值重估才刚刚开始，市场低估了AI对功率半导体的需求弹性\n\n这份GS最新发布的欧洲半导体研报，表面上只是上调了英飞凌和意法半导体的盈利预测与目标价，但真正值得关注的信号并非数字本身，而是其背后一套完整的估值逻辑重置。\n\n报告传递了一个清晰判断：市场此前对AI半导体需求的认知过于集中在GPU和高端计算芯片上，而忽略了AI基础设施大规模部署对功率半导体、光通信等“使能器件”的结构性拉动。GS将英飞凌12个月目标价从75欧元上调至88欧元，意法半导体目标价从42欧元上调至58欧元，估值倍数分别从16倍和10倍的EV/EBITDA提升至18倍和13倍。但比目标价更重要的，是支撑这一倍数扩张的逻辑——这两家公司正在经历从周期性半导体公司向AI结构性增长公司的身份转换。\n\n以下是我们从这份报告中提炼出的五个核心洞察，以及一个报告尚未完全回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 英飞凌的估值扩张并非凭空而来，其背后是收入增速翻倍的支撑\n\nGS对英飞凌的估值调整，最值得关注的是其推导逻辑。报告明确指出，英飞凌的历史中位两年远期收入复合增长率约为9%，而当前预测值约为17%，几乎翻倍。这一增速提升，与GS给予的估值倍数扩张幅度高度吻合——从历史中位约10倍的12个月远期EV/EBITDA，提升至目标价隐含的约21倍。\n\n这不是简单的“给AI概念股溢价”，而是基于收入增速变化与估值倍数之间的历史对应关系。GS用同样的逻辑检验了盈利增速：英飞凌历史两年远期EPS复合增长率为19%，当前预测为43%，扩张幅度约2.3倍；而目标价隐含的12个月远期PE从历史约20倍提升至约39倍，扩张幅度同样约为2倍。\n\n这意味着，GS并非在给英飞凌一个“AI故事溢价”，而是在系统性地论证：当一家公司的增长\n\n[... middle omitted ...]\n\n起讨论这些未解问题，分享完整报告中的原始图表和估值模型细节。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲AI芯片双雄，投行怎么看\n\n📈 AI需求拉动成长\n\n最近某外资投行更新了对欧洲两家半导体公司——英飞凌（IFX）和意法半导体（STM）的模型预测，核心逻辑是AI相关芯片需求正在变强。\n\n1️⃣ **英飞凌：电源芯片受益AI**\n- 投行维持FY26营收预测，但上调FY27-30营收约1-2%，理由是AI芯片（GPU/CPU）对电源半导体的需求增长，加上公司正扩产（如德累斯顿新模块，中期可支持50亿欧元年营收）。\n- 毛利率因产能利用率改善上调0-1pp，FY27-30调整后EBIT上调3-4%。\n- 目标价从€75上调至€88，估值倍数从16x提高到18x（基于CY27 EV/EBITDA），因为当前2年营收CAGR（17%）几乎是历史中位数（9%）的两倍。\n\n2️⃣ **意法半导体：AI基础设施拉动更大**\n- FY26-30营收预期上调4-9%（美元计），主要来自AI基础设施（尤其是光网络）的客户需求和订单。\n- 毛利率上调约1-2pp，FY26-30调整后EBIT上调13-23%。\n- 目标价从€42上调至€58（ADR从$49上调至$67.5），估值倍数从10x提高到13x。当前2年营收CAGR（\n\n[... middle omitted ...]\n\n26 revenue estimate unchanged but raise our FY27-30 revenue estimates by c.1-2% to reflect a more constructive view on AI-related demand (from both GPU/CPUs) for IFX's power semis due to recen\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R006",
    "title": "Bernstein：亚洲动量交易已进入估值泡沫区，减仓窗口正在关闭",
    "digest": "[wechat_article.md]\n# Bernstein：亚洲动量交易已进入估值泡沫区，减仓窗口正在关闭\n\n这份报告的核心判断并不复杂，但它的警示信号值得认真对待：亚洲市场（除日本和中国外）的动量交易已经进入历史级别的估值与预期双泡沫区间，而韩国和台湾市场正是风险最集中的区域。Bernstein量化策略团队在6月初发布的这份报告中，明确建议削减这两个市场的动量敞口。\n\n为什么现在重要？因为过去几个月，动量策略在亚洲取得了极为罕见的超额收益——在除日本外的亚洲市场，价格动量因子年内跑赢基准36%至38%；如果剔除中国，这一数字更是飙升至53%至60%。韩国和台湾的动量因子年内绝对超额收益甚至超过50%。但极端收益往往伴随着极端风险。Bernstein团队指出，这些市场的动量交易不仅估值创下历史新高，盈利预期同样处于前所未有的高位，而这两者叠加在一起，构成了一个脆弱性极高的组合。\n\n报告给出的建议很清晰：削减台湾和韩国的动量敞口，转向反动量篮子，即高股息或低波动资产。但真正值得深思的，不是这个建议本身，而是它背后反映的市场结构变化——动量因子与成长因子的相关性已升至历史高位，而动量在低波动和价值股中却在持续下降。这种极端的市场内部分化，往往预示着风格切换的临界点正在逼近。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 动量交易的估值泡沫并非均匀分布，台湾和韩国是真正的风险中心\n\nBernstein的量化分析显示，亚洲（除日本、除中国）的动量组合正处于历史最高估值水平，无论是12个月远期市盈率还是市净率，都已突破此前所有周期的高点。具体来看，台湾和韩国动量篮子的估值均达到历史峰值，而且从6月初开始已经出现估值收缩的迹象。相比之下，中国和印度的动量股距离泡沫估值区间还相去甚远，日本动量股的估值甚至仍低于长期平均水平。\n\n这里需要特别关注一个细节：报告区分\n\n[... middle omitted ...]\n\n新报告的精读和实战应用，帮助你在市场转折点做出更清醒的判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚洲动量正在“过热”？\n\n警惕台湾韩国回调风险\n\n最近亚洲市场动量风格涨得有多猛？投行研报直接用了“极端的”这个词。今天来拆一下逻辑。\n\n1️⃣ **动量涨到哪了？**\n- 亚洲（除日本）动量策略年内跑赢市场36%-38%\n- 台湾、韩国更夸张，动量超额收益超50%\n- 但研报提示：这两个市场已出现“过热”和集中度风险\n\n2️⃣ **估值泡沫在哪里？**\n- 亚洲（除日本、中国）动量组合估值创历史新高\n- 台湾和韩国动量股估值在6月初已开始回落\n- 中国和印度动量股估值离泡沫还远\n- 日本动量股估值仍在历史均值下方\n\n3️⃣ **比估值更危险的是盈利预期**\n- AI技术推动亚洲科技股盈利预期创纪录\n- 台湾、韩国动量股盈利预期处于历史高位\n- 韩国略低于2009年水平——但结合高估值，这个“乐观”很脆弱\n\n4️⃣ **市场内部已出现极端分化**\n- 动量与成长因子的相关性创历史新高\n- 低波动风格动量跌至25年最低\n- 台湾和韩国高波动股票疯涨，低波动股票被抛弃\n- 这种极端分化通常预示着风格切换\n\n研报认为：降低动量敞口，分散到高股息或低波动风格，可能是更稳妥的选择。\n\n你觉得动量风格还会继续吗？欢迎一起\n\n[... middle omitted ...]\n\n Since April, we have been positive on momentum stocks across Asia and Japan, as a risk-on proxy to play the de-escalation of the war (see here, here, here). However, over the last few weeks, \n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R007",
    "title": "Citi：美元兑日元的真正支撑不是利差，而是日本股市催生的对冲需求",
    "digest": "[wechat_article.md]\n# Citi：美元兑日元的真正支撑不是利差，而是日本股市催生的对冲需求\n\n市场对日元走强的共识正在变厚。美日长期利差已经收窄到足以清晰支持日元升值的方向，短期利差的信号同样不容忽视。但美元兑日元汇率却依然顽固地维持在160附近。这种背离让许多宏观交易员困惑——是模型错了，还是市场定价里藏了一个被低估的结构性因素？\n\nCiti这份题为《Japan FX: An analysis of the USD/JPY price formation mechanism》的报告，给出一个值得认真对待的判断：当前美元兑日元的强势，很大程度上来自日本股市处于历史高位所催生的日元卖出对冲需求。这不是一个短期噪音，而是一种与股市市值深度绑定的结构性买盘。Citi维持对美元兑日元的中长期看空观点，认为160日元附近就是顶部区间，年底前将回落至155以下。但要控制日元在短期内的阶段性走弱，仍需要日本央行货币政策正常化以及日本当局的卖出美元干预。\n\n这份报告的核心贡献，不在于给出了一个具体的点位预测，而在于提供了一个分析框架——如何区分趋势、周期和噪音，以及为什么传统利差模型在当前环境下可能严重低估了股市对冲需求的力量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 利差收窄已经明确指向日元升值，但汇率没有跟随，说明市场存在“第五因素”\n\nCiti在报告中开宗明义地指出，美元兑日元的定价受到四个基本面因素的共同影响：美日货币政策差距、整体市场风险偏好、日本的国际收支状况，以及美元整体方向（尤其是对欧元的走势）。这四个因素构成了一个基本估值框架。\n\n然而，报告明确承认，即便这四个因素全部纳入模型，依然存在一个“残差”——实际价格与模型估值的每日偏差。这个残差通常被归因于短期投机活动造成的错误定价。但问题在于，预测这个残差恰恰是市场参与者最困难\n\n[... middle omitted ...]\n\n格和更细致的拆解笔记，也欢迎大家带着自己的持仓和观点来交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日元被低估了吗？拆解一个投行模型\n\n**日元模型拆解**\n\n**两层结构看透USD/JPY定价逻辑**\n\n最近某外资投行发布了一份关于USD/JPY定价机制的研究，用了一个“双层模型”来分析汇率走势。我把它拆解成能看懂的语言，分享几个关键点。\n\n1/ 模型分为上下两层：\n- 上层：观察USD/JPY偏离200日均线的幅度，解释短期波动\n- 下层：观察200日均线本身的走势，解释长期趋势\n\n2/ 上层模型用了4个变量：美日10年期利差、日本股市（TOPIX）、商品贸易条件指数、美元指数（DXY）。结果发现，日本股市和美元指数的解释力最强。\n\n3/ 下层模型用了4个变量：美日实际利率差、日本股市、大宗商品指数、美元指数。同样，日本股市和美元指数是最主要的驱动因素。\n\n4/ 当前模型估算USD/JPY合理价位在161左右，实际汇率略低于这个水平。研报认为，这可能是因为日本当局进行了买入日元的干预操作。\n\n5/ 为什么利差收窄但日元没有升值？一个重要原因是日本股市处于历史高位，产生了大量的日元卖出对冲需求。\n\n6/ 研报的核心判断：160是USD/JPY的顶部区间，年底前会回落到155以下。但短期日元走弱的风险仍存，\n\n[... middle omitted ...]\n\n also justifies the current level of the USDJPY. We see no need to change our bearish medium- to long-term view on the USDJPY. In our view, around ¥160/\\$ will be the ceiling for the pair and \n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R008",
    "title": "DB：亚洲通胀反弹正在重塑央行的利率路径，市场尚未完全定价这一轮紧缩的力度与广度",
    "digest": "[wechat_article.md]\n# DB：亚洲通胀反弹正在重塑央行的利率路径，市场尚未完全定价这一轮紧缩的力度与广度\n\n2026年二季度，亚洲经济正在经历一个看似矛盾但逻辑清晰的阶段：增长放缓但高于趋势，通胀加速但政策干预有效。DB在其最新发布的《Asia Macro Insight》报告中提出一个核心判断——亚洲央行将进一步加息，且加息的力度和广度可能超出当前市场定价。这不是一次常规的周期调整，而是一次由供给侧结构变化、地缘政治冲击和国内政策权衡共同推动的利率重置。\n\n报告指出，2026年亚洲CPI通胀预计将达到2.7%，是去年的三倍。这一数字本身并不惊人，但真正值得关注的是通胀的来源结构：芯片价格飙升带来的贸易条件改善、伊朗战争推高的能源成本、以及中国再通胀进程的超预期推进。三个因素叠加，使得亚洲央行的政策天平从“保增长”明确转向“稳价格与稳汇率”。\n\n对于投资者而言，这意味着需要重新审视亚洲资产的定价逻辑。利率上行不再是尾部风险，而是基准情景。而哪些经济体、哪些行业能够在这一轮紧缩中保持韧性，将决定未来12个月的相对表现。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 通胀的三重驱动：芯片溢价、能源冲击与中国再通胀\n\nDB的报告清晰勾勒出当前亚洲通胀的三个来源，它们彼此独立但相互强化。\n\n首先是半导体价格的飙升。报告指出，韩国和台湾正受益于强劲的半导体定价，这不仅仅是周期性的需求回暖，更是AI投资驱动的结构性变化。芯片价格的上涨幅度足以抵消进口价格上涨对贸易条件的侵蚀，使得韩国和台湾的名义增长可能分别达到1996年和1987年以来的最高水平。这是一种“好通胀”——由高附加值出口拉动，伴随企业盈利改善和名义GDP扩张。\n\n其次是伊朗战争引发的能源成本冲击。报告数据显示，部分经济体在2026年5月的交通/燃料通胀环比大幅跳升，菲律宾达到50%\n\n[... middle omitted ...]\n\n完整的报告原文和图表分析，欢迎来我们的星球微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚洲经济正在经历一场“冷热交替”\n\n**封面短标题：** 亚洲经济冷热图\n\n**封面副标题：** 出口热、内需冷，加息潮要来了\n\n---\n\n最近看了一份某外资投行的亚洲宏观研报，信息量很大，给大家拆几个核心逻辑。\n\n**1. 出口很热，但内需在降温**\n\n4月数据显示，亚洲经济增长在放缓，但依然高于趋势线。最亮眼的是出口，尤其是半导体和电子产品，带动了韩国、台湾等地的贸易条件改善。中国的出口增长也被上调到12%，主要靠AI投资和绿色转型拉动。\n\n但另一边，国内消费和投资却有点“冷”。中国4月零售增速掉到0.2%，餐饮和旅游受油价上涨影响明显。固定投资也意外下滑，基建和制造业投资都出现了同比负增长。\n\n**2. 通胀压力在积聚，加息成为主旋律**\n\n油价和芯片价格上涨，让亚洲的通胀压力明显回升。研报预计，2026年亚洲CPI通胀率将是去年的三倍，达到2.7%。\n\n为了应对通胀和汇率压力，亚洲各国央行大概率会继续加息。印尼和菲律宾可能再加75个基点，韩国和印度可能加100个基点。连马来西亚的加息也可能提前到今年。\n\n**3. 中国的“再通胀”与地产“筑底”**\n\n中国虽然内需偏弱，但“再通胀”进度比预期快，这得益\n\n[... middle omitted ...]\n\nrket. With the growth soft patch largely anticipated in Q2, most central banks are likely to prioritize price and market stability, reinforcing the case for further and/or more aggressive tigh\n\n[... middle omitted ...]\n\nk, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R009",
    "title": "NOM：韩元走弱的真正推手不是经济基本面，而是资本市场成功的“悖论”",
    "digest": "[wechat_article.md]\n# NOM：韩元走弱的真正推手不是经济基本面，而是资本市场成功的“悖论”\n\n韩国正在经历一个让许多宏观交易员感到困惑的时刻。经济账上，出口强劲推动经常账户盈余在2026年3月飙升至373亿美元，年化占GDP比例高达23%；KOSPI指数年内涨幅达87%，领跑全球主要股指。按照教科书逻辑，韩元应当成为亚洲表现最强的货币之一。然而现实是，韩元兑美元和名义有效汇率年内反而贬值约5.5%，沦为亚洲表现最差的货币之一。\n\n这份NOM研报的核心判断是：韩元当前面临的不是基本面问题，而是一个由资本市场繁荣自身催生的、结构性的资本外流悖论。理解这一悖论的运行机制，比猜测韩国央行何时干预或美元何时走弱，更能帮助投资者把握韩元的中期走向。\n\n报告的价值在于，它系统性地拆解了韩国国际收支中几个相互作用的资本流动引擎，并给出了三种情景下的量化压力测试。这不仅仅是一份汇率分析，更是一份关于“当国内资产价格暴涨时，资本账户会如何反向吞噬经常账户盈余”的机制说明书。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 经常账户盈余与货币贬值并存的悖论，根源在于资本账户的结构性失血\n\n韩国经济目前呈现出一个典型的“K型”图景：科技出口部门极度繁荣，但这一繁荣并未有效转化为韩元的买入力量。NOM的分析揭示了背后三个关键的资金漏损渠道。\n\n第一个渠道是企业层面的美元囤积。尽管出口强劲，韩国企业并未将大量美元收入结汇为韩元。报告引用韩国当局的表态和当地媒体报道，指出企业正在主动持有美元资产，这直接压低了实际贸易结算的净流入规模。企业这种行为背后是对全球贸易环境的不确定性和对韩元潜在贬值空间的防御性布局。\n\n第二个渠道是零售投资者的海外资产配置。韩国散户对海外股票，尤其是美国科技股的配置热情在过去一年极为高涨。在2026年4月和5月，韩国零售投资者出现了自2\n\n[... middle omitted ...]\n\n演进路径，以及如何将NOM的分析框架转化为可执行的交易思路。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n韩国股市越涨，韩元反而越弱？\n\n**涨得越好，压力越大**\n\n韩国股市今年涨了87%，但韩元却贬值了5.5%。这种“反常”现象，背后是复杂的资金流动逻辑。\n\n**1️⃣ NPS的新目标：看似利好，实则暗流**\n\n韩国国民年金（NPS）上调了国内股票配置目标（从14.9%→20.8%），按理说会减少资金外流。但问题在于，如果KOSPI继续大涨（比如再涨60%），NPS的国内股票仓位会被动超标，反而需要卖出国内股票、买入海外资产，形成新的抛压。\n\n**2️⃣ 芯片双雄的“10%魔咒”**\n\n三星电子和SK海力士是韩国股市的发动机。如果这两只股票再涨60%，很多全球基金因为“单只股票持仓不得超过10%”的规则，必须强制卖出。据测算，这可能带来高达480亿美元的外资流出。\n\n**3️⃣ 散户：从买美股到“观望”**\n\n韩国散户过去疯狂买美股，但最近两个月开始净卖出。不过，一旦SpaceX、Anthropic等AI明星公司IPO，可能又会吸引大量资金出海。这种“暂停”是暂时还是趋势，是决定韩元强弱的关键。\n\n**4️⃣ 企业的“美元囤积症”**\n\n韩国企业赚了很多出口美元，却没有换回韩元，而是选择持有。加上政府承诺每年\n\n[... middle omitted ...]\n\nbut without risk negativity) on the global AI cycle – Korea's BoP dynamics will remain unfavorable.  \n- We conducted a scenario analysis on Korea's BOP dynamics, taking into account three scen\n\n[... middle omitted ...]\n\nrmation is available upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM Singapore Ltd., Singapore. All rights reserved."
  },
  {
    "id": "R010",
    "title": "摩根斯坦利：中国大宗商品出口的“结构性分化”正在重塑全球定价权",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：中国大宗商品出口的“结构性分化”正在重塑全球定价权\n\n这份报告的价值不在于它记录了5月的贸易数据，而在于它揭示了一个正在发生的根本性变化：中国大宗商品的出口结构正在从“数量驱动”转向“套利驱动”，而这种转变对不同品种的定价逻辑和竞争格局有着截然不同的含义。\n\n摩根斯坦利刚刚发布的5月贸易数据追踪报告，表面上是一组月度数字的更新。但如果我们把这些数字放在一起看，一个清晰的信号浮现出来：铝和铝制品出口创下7个月新高，钢铁出口在低位企稳，而铜的进口则呈现出一种“价格高企但需求不弱”的韧性。这些看似零散的现象，背后有一条共同的逻辑线——全球供应链的再调整正在改变中国作为“世界工厂”的出口角色。\n\n这不是一个关于“需求复苏”的故事，而是一个关于“供给再定价”的故事。理解这一点，比记住任何一个单月数据都重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 铝出口的跳升不是需求信号，而是套利窗口被打开的必然结果\n\n5月中国铝及铝制品出口达到63.2万吨，环比增长6%，同比增长16%，创下自2024年11月以来的最高水平。这个数字本身并不令人意外，真正值得关注的是它背后的驱动机制。\n\n报告明确指出，中东地区的供给中断收紧了除中国以外的市场，推高了LME铝价，从而扩大了出口套利空间。换句话说，这轮出口增长的核心驱动力不是海外终端需求的突然爆发，而是中国生产商抓住了价格差扩大的窗口。\n\n这带来了一个重要推论：这种出口增长的可持续性取决于套利窗口能开多久，而不是海外需求有多强。一旦LME价格回落或国内成本上升压缩了价差，出口量可能会迅速回调。对于投资者而言，这意味着需要跟踪的不是简单的出口量趋势，而是内外价差的动态变化。\n\n更深一层的含义是，中国铝行业正在从“被动接受全球价格”转向“主动利用全球价差”。那些拥有低成本产\n\n[... middle omitted ...]\n\n定期组织专题讨论，帮助大家把研报中的信号转化为可执行的判断。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国大宗商品5月进出口：铝出口跳升，钢、煤分化\n\n铝出口创半年新高\n\n5月中国铝及制品出口63.2万吨，同比+16%，环比+6%，创2024年11月以来最高。中东供应中断推高LME价格，出口套利窗口扩大，铝材出口是主要拉动力。\n\n钢材出口量增但同比转负\n\n5月钢材出口1034万吨，环比+9%但同比-2%（去年基数高）。1-5月累计出口4455万吨，同比-8%。中钢协会员企业5月日均产量同比-4.4%（4月-5.7%），推算表观消费同比-10.4%。\n\n铜进口小幅增长，现货需求依然坚挺\n\n5月铜及制品进口44.6万吨，同比+4%，环比-1%。洋山铜溢价维持在60-75美元/吨，实物需求不弱。铜精矿进口235万吨，同比持平，加工费继续下行但硫酸价格支撑冶炼利润。\n\n铁矿石库存高位缓降\n\n5月进口铁矿石9800万吨，环比-6%，同比持平。港口库存开始缓慢去化但仍处高位。钢厂生铁产量YTD-2%，粗钢YTD-4%。\n\n煤进口季节性走弱，6月或反弹\n\n5月进口煤3300万吨，同比-8%，环比+1%。需求淡季+进口煤价高是主因。国内煤价上涨后进口套利窗口重新打开，预计6月环比回升。\n\n#学习笔记\n\n[source_min\n\n[... middle omitted ...]\n\ncopper products (refined + alloys) totaled 446kt in May, down 1% MoM but up 4% YoY. The import arbitrage opened intermittently during April and May despite rising copper prices, with net refin\n\n[... middle omitted ...]\n\nGroup Limited (0639.HK)</td><td>O (09/15/2022)</td><td>HK$2.73</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.\n\n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R011",
    "title": "GS：日本央行6月加息的可能性被市场低估，真正关键的是加息后的沟通路径",
    "digest": "[wechat_article.md]\n# GS：日本央行6月加息的可能性被市场低估，真正关键的是加息后的沟通路径\n\n市场对日本央行加息的讨论，大多停留在“6月还是7月”的择时博弈上。但GS最新一期日本经济研报提出了一个更具结构性的判断：**加息时点本身不是最重要的，真正决定资产定价走向的，是央行在加息后如何修改前瞻指引，以及如何管理市场对“接近中性利率”的预期。**\n\n这份报告由GS首席日本经济学家Akira Otani领衔，在植田和男6月3日讲话后，将加息预期从7月提前至6月。这个调整本身并不令人意外——市场已经部分定价。但报告真正有穿透力的部分，在于它对加息之后路径的推演，以及对央行沟通策略的精细化拆解。这些内容，恰恰是很多短期交易视角容易忽略的。\n\n以下是我们从报告中提炼出的五个核心层次，它们共同指向一个结论：**日本正在进入一个“加息但不紧缩”的微妙阶段，市场对央行沟通的敏感度将前所未有地上升。**\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 经济数据“软硬分化”为加息提供了窗口，但真正的推力来自政治沟通的铺垫\n\nGS的分析起点，是一个看似矛盾但已被多次验证的现象：日本经济正在经历软数据与硬数据的背离。消费者信心和景气观察调查等软指标在走弱，但机械订单、消费活动指数等硬数据依然稳健。这种“软硬分化”本身并不构成加息的充分条件——事实上，过去几年类似的分化曾多次出现，央行都选择了按兵不动。\n\n真正改变局面的，是GS捕捉到的两个关键信号。\n\n第一个信号是5月22日植田和男与首相高市早苗的会面。GS明确指出，这次会面为加息做了政治层面的铺垫。在日本的货币政策决策框架中，政府与央行的沟通一直是一个“房间里的大象”——市场知道它重要，但很难量化。GS这次提供了一个可操作的观察框架：植田在会面后两周的6月3日讲话中，非但没有像市场预期的那样“降温”，反\n\n[... middle omitted ...]\n\n起拆解这些图表背后的二阶影响，以及它们对不同资产类别的含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日本央行6月加息概率上升\n\n6月加息，节奏偏稳\n\n某外资投行最新研报解读：\n日本经济韧性超预期，B2B价格加速上涨，预计很快传导至消费端。\n\n1/ 关键判断：6月加息概率大\n- 之前市场预期7月加息，但行长植田和男6月3日讲话偏鹰\n- 结合5月22日与首相会面，认为已经为加息铺好路\n- 如果6月不加息，行长应该会释放信号冷却预期，但实际讲话更鹰\n\n2/ 后续节奏：半年一次\n- 6月加息后，预计下次在2027年1月\n- 最终利率目标1.5%，预计2027年7月达到\n- 节奏可能会受市场波动和政府沟通进度影响\n\n3/ 关于购债计划\n- 6月会议将讨论缩减JGB购买\n- 预计维持现有计划到2027年3月\n- 之后每月购买规模保持在约2万亿日元\n\n研报认为，日本央行会采取渐进但坚定的加息路径，不会激进。\n\n#学习笔记\n\n[source_mineru.md]\n# Japan Economic Flash: BOJ June MPM Review: We Expect a Rate Hike in June, Followed by Roughly Semi-annual Hikes\n\nThe Japanese econ\n\n[... middle omitted ...]\n\nin conjunction with the June rate hike to maintain a hawkish stance while hinting that it is approaching the neutral rate.  \n■ After the June hike, we expect the next rate hike in January 2027\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R012",
    "title": "GS：CMS释放的信号比药价谈判本身更重要",
    "digest": "[wechat_article.md]\n# GS：CMS释放的信号比药价谈判本身更重要\n\n市场对药品定价改革的关注点，大多集中在“砍价幅度有多大”这个数字游戏上。但GS在其第47届全球医疗保健年会上与CMS高层官员的对话，揭示了一个更深层的结构性变化：美国医保体系正在经历一场系统性的财政责任再分配。这场再分配的最终影响，可能比任何一轮药价谈判都要深远。\n\nGS的研报显示，CMS领导层将其近期议程锚定在四个核心优先事项上：以患者为先的支付方、预防导向的战略、打击欺诈浪费和滥用、以及可负担性。这听上去是一份标准的政策清单。但真正值得关注的，是这些优先事项背后隐含的财政逻辑——联邦政府正在系统性收紧其在医疗支出中的敞口，并将更多成本压力向下传导至州政府、制药企业和医疗服务提供方。\n\n这不是一个孤立的事件。这是一轮医疗体系供给侧的结构性再定价。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 药价谈判只是表象，真正重要的是MFN机制正在重塑全球定价体系\n\nCMS在会议上披露的数据值得反复推敲：第一轮IRA谈判带来了约20%的平均净节省，而当前政府主导的第二轮谈判，折扣幅度已接近40%。这个数字本身并不意外——市场对此已有预期。但GS分析师敏锐地捕捉到了一个更关键的信号：CMS将最惠国（MFN）机制视为一个“更广泛的工具包”，其目标不仅仅是美国市场，而是通过贸易动态在全球范围内施加定价压力。\n\n这意味着什么？MFN的逻辑是，如果制药企业在美国市场给出了一个折扣价格，那么其他联邦医保项目也应该享受同样的价格。但CMS的表述暗示，他们正在将这个逻辑延伸至全球——如果一家制药公司在某个国家接受了较低的价格，那么这个价格应该成为美国市场的参照基准。\n\n这实际上是在构建一个全球性的药品定价锚定体系。对于跨国制药企业而言，这不再是“美国市场单独承压”的问题，而是全球定价体系正\n\n[... middle omitted ...]\n\n影响路径，并分享GS研报中未被本文覆盖的原始数据和图表分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCMS 最新政策风向：药价谈判与医保改革\n\n药价谈判新逻辑\n\n某外资投行在近期全球医疗会议上，与CMS高层深度交流后，梳理出几个关键政策方向。\n\n1️⃣ 核心优先级重塑\nCMS将工作重心锁定在四个方向：以患者为中心的支付体系、预防策略（MAHA）、打击欺诈滥用、以及最受关注的药价可及性。整体思路是“系统现代化”。\n\n2️⃣ 药价谈判：第一轮 vs 第二轮\nIRA谈判首轮实现约20%的净节省，但第二轮在现政府推动下，折扣幅度拉大到约40%。更值得关注的是“最惠国”（MFN）条款——通过贸易机制在全球范围施加定价压力。目前仅涉及17家生物制药公司，是否会扩大，研报未给出明确信号。\n\n3️⃣  Medicaid 资金大洗牌\n联邦资金占比从最初的60%升至约70%，CMS认为部分州项目（如提供商税机制、Medicaid扩展人群）正在推高联邦支出。政策方向是：引入按Medicare基准的支付上限，要求州政府承担更多财务责任。\n\n4️⃣ ACA交易所：严查欺诈\n重点是清理不合规参保者，并加强计划间的竞争。新支付规则已嵌入多项诚信措施。\n\n💡 我的观察：MFN+IRA的组合拳，本质是系统性地压低药品成本。Medicaid改\n\n[... middle omitted ...]\n\nlton, CMS Deputy Administrator and Rebekah Armstrong, CMS Chief of Staff and Director, Office of Legislation.\n\nThe panel framed their perspectives on key healthcare issues, with a focus on mos\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R013",
    "title": "GS：医疗健康板块的结构性拐点，比市场感知的更近",
    "digest": "[wechat_article.md]\n# GS：医疗健康板块的结构性拐点，比市场感知的更近\n\n过去三年，全球医疗健康投资界一直在等待一个明确的信号：基本面改善何时能转化为估值修复。GS在第47届全球医疗健康年会上组织的一场投行家圆桌讨论，给出了一个值得认真对待的答案——这个拐点可能比多数人预期的更近，但它不会以整齐划一的方式到来。\n\n这份讨论纪要的核心信息不是“医疗健康板块要涨了”，而是一个更微妙的判断：板块内部正在发生深刻的分化，决定胜负的关键不再是赛道选择，而是企业在资本配置、资产组合和运营效率上的执行力。那些能够将规模转化为议价权、将数据积累转化为竞争壁垒的企业，将在下一轮周期中占据显著优势。\n\n这场讨论的价值不在于提供了多少新数据，而在于它揭示了市场定价与基本面之间正在形成的裂口——以及这个裂口如何为有准备的投资者创造机会。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 并购市场的结构性升温，本质是产业逻辑而非周期驱动\n\n2026年至今，全球医疗健康并购交易额已接近1000亿美元，而2025年全年仅为500亿美元。这个数字本身已经足够引人注目，但真正值得关注的是背后的驱动力。\n\n投行家们观察到，本轮并购活跃度并非简单来自低利率或充裕资本，而是源于产业内部的结构性压力。大型生物科技公司正在主动追逐中型标的，且交易模式发生了显著变化：买方更早介入谈判、更频繁使用或有价值权（CVR）来管理风险、更专注于大型药企通常忽略的细分治疗领域。\n\n这意味着什么？传统上，大型药企的并购逻辑是“补品种”——用现金换收入。而当前这轮并购的底层逻辑是“补能力”——用交易换效率。大型药企意识到，内部研发的回报率正在下降，而通过并购获取经过验证的、执行风险较低的商业化阶段资产，是提升资本回报率的最可靠路径。\n\n对投资者而言，这意味着需要重新评估哪些公司最可能成为并购目标\n\n[... middle omitted ...]\n\n的讨论通常会比文章更早触及那些尚未被市场充分定价的边际变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n全球医疗投研的“中场战事”\n\n市场在等一个信号\n\n投行把脉2026医疗赛道：并购回暖、AI落地、中国创新成焦点\n\n最近参加了一场外资投行举办的全球医疗健康大会，几个资深投行家的圆桌讨论信息量很大。整理几个核心观察：\n\n1️⃣ 并购市场明显回暖\n上半年医疗并购交易额已达1000亿美元，是去年的两倍。大药企开始追着中小型biotech谈收购，尤其关注细分治疗领域。交易结构也更灵活，CVR（或有价值权）成为常见工具。\n\n2️⃣ 中国创新：威胁还是机会？\n这是个高度分裂的话题。一方认为中国biotech是“存在性威胁”，另一方则看到高质量创新、低成本资本和高效临床试验的优势。一个有趣的现象是：中国企业想进美国市场，美国企业想买中国资产。这种双向需求正在倒逼美国本土创新者提升运营效率。\n\n3️⃣ AI落地：行政先行，实验室在后\n目前AI在医疗领域的应用还集中在法律文书、监管申报等行政环节。真正体现在营收增长、减少实验室人员或加速临床试验上，还需要时间。部署成本高、责任归属不明确是主要卡点。\n\n4️⃣ 器械与诊断：冰火两重天\n器械板块整体被市场冷落，但基本面扎实。诊断领域的高增长细分（如肿瘤诊断）正在成功转向盈利。AI在\n\n[... middle omitted ...]\n\nkers who cover Biopharma, Life Sciences Tools & Diagnostics, Medtech, M&A, and Europe Healthcare titled A Conversation with GS Investment Bankers: The State & Outlook for the Healthcare Sector\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R014",
    "title": "Citi：中国2万亿AI投资计划的核心不在于规模，而在于国产化率的硬约束",
    "digest": "[wechat_article.md]\n# Citi：中国2万亿AI投资计划的核心不在于规模，而在于国产化率的硬约束\n\n当市场还在讨论中国AI算力缺口有多大时，一份来自Citi研报的最新信号值得决策者认真对待：中国计划在未来五年投入2万亿元人民币建设数据中心和网络基础设施，以支撑国内AI产业发展。这个数字本身并不令人意外——市场早已预期中国会在AI基础设施上持续加码。真正被低估的，是这份计划中一个看似技术性的硬性约束：电信运营商运营的数据中心，必须使用至少80%的国产AI加速器。\n\n这个80%的国产化率目标，才是理解未来五年中国半导体产业链投资逻辑的关键。它不仅仅是一个采购指引，更是一个产业格局的再分配机制。Citi的研报正是在这个判断基础上，给出了对代工厂、封测、设备以及AI芯片供应商的正面看法。\n\n这份报告发布的时间点也值得玩味。当前，中国AI芯片市场已经发生了结构性变化：英伟达H200的进口基本停滞，国产AI芯片实际上已经占据了市场的绝大多数份额。这意味着，80%的国产化目标并非遥不可及的远景，而是对已经发生的市场现实的确认和制度化。但问题在于，这种确认对不同环节、不同体量的企业意味着完全不同的东西。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 国产化率硬约束的落地，将系统性重塑AI芯片的竞争格局\n\nCiti研报中最具洞察力的判断之一，在于它对国产化率目标实现路径的评估。报告明确指出，80%以上的AI芯片国产化目标是“可实现的”，因为国产AI芯片厂商今年实际上已经有效占据了市场的绝大多数份额。但这并不意味着所有国产厂商都能均分这块蛋糕。\n\n关键在于，国有资本投资的数据中心在采购时，天然倾向于更广泛的供应商选择。这与过去市场集中采购少数头部芯片的逻辑有本质区别。Citi认为，这种变化对中小型AI芯片厂商更为有利——国有数据中心更愿意从更广泛的供应\n\n[... middle omitted ...]\n\n2万亿投资计划遇上HBM供应瓶颈时，市场可能会如何重新定价？\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国AI投资2万亿，半导体链怎么看\n\n2万亿，5年，80%国产化\n\n最近有消息说，中国计划未来5年投入2万亿人民币（约2950亿美元）建设数据中心和网络，专门支持国内AI产业。运营商运营的数据中心，要求至少80%使用国产AI加速器。\n\n这个规划，给国内半导体供应链画了条很清晰的路线图。\n\n**1. 谁最受益？**\n\n投行研报认为，这条消息对以下环节偏正面：\n- **晶圆代工**：中芯国际、华虹半导体\n- **封测**：长电科技、通富微电\n- **设备**：ASMPT、上海微电子（推测）\n- **AI芯片厂商**：尤其是国产AI加速器供应商\n\n**2. 80%国产化，能实现吗？**\n\n研报认为，这个目标可行。原因很直接：\n- 今年英伟达H200进口基本停滞，国产AI芯片已经拿下了国内绝大部分市场。\n- 相比之前，国字号数据中心更愿意向更多供应商采购，这对中小AI芯片厂商反而是好事。\n\n**3. 国产芯片到底什么水平？**\n\n研报附了一份对比表，我提炼几个关键点：\n- **华为**：910B/910C/920/950系列，制程从7nm到6nm，性能逐步追赶。950 PR和DT的FP16算力达到1.0 PFLOPS\n\n[... middle omitted ...]\n\nnd 4) AI accelerator vendors; given a clearer roadmap ahead for China's AI localization. The 80%+ AI chip localization target should be achievable as domestic AI chip vendors have effectively \n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R015",
    "title": "Bernstein：量子计算的真正变量不是技术路线，而是速度与保真度的取舍",
    "digest": "[wechat_article.md]\n# Bernstein：量子计算的真正变量不是技术路线，而是速度与保真度的取舍\n\n量子计算行业正站在一个关键的十字路口。市场上充斥着“量子霸权”的叙事和各类技术路线的争论，但真正决定产业走向的核心问题，并非哪种量子比特最终胜出，而是一个更根本的取舍：你是愿意在毫秒级完成计算但容忍一定误差，还是愿意等待一秒以上但确保结果的精确性？\n\nBernstein最新发布的量子计算行业专家研讨会纪要，揭示了这一被多数投资者忽视的核心矛盾。该机构邀请了一位拥有15年行业经验、横跨硬件、系统和软件应用全栈的量子技术管理者，系统拆解了当前量子计算的技术格局与竞争态势。这份纪要的价值不在于罗列技术参数，而在于给出了一个可操作的判断框架：不同应用场景对计算速度和保真度的要求截然不同，这意味着未来的量子计算不会是“赢家通吃”，而是一个多模态共存的生态系统。\n\n对于产业决策者和投资者而言，理解这一框架，远比押注某一技术路线更为重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 量子计算的核心张力不在于技术路线，而在于“制造”与“天然”的物理本质差异\n\n大多数市场讨论将量子计算技术路线简单归类为“谁更快”或“谁更准”，但这种比较忽略了最根本的物理学差异。Bernstein专家提出的分析框架极具洞察力：所有量子比特应被分为“制造型”和“天然型”两大类。\n\n制造型量子比特，包括超导、硅自旋和拓扑等路线，本质上是人类工程设计的产物。它们的优势在于速度快——操作频率可达千赫兹甚至兆赫兹级别，计算重复速率远超其他方案。但代价是“一致性”缺失：即使是精心制造的两个超导量子比特，其特性参数仍存在约10%的差异。这导致控制系统的复杂度大幅上升，同时噪声更高、相干时间更短。\n\n天然型量子比特，包括离子阱和中性原子，则利用了自然界中本就存在的完美一致性。每一个\n\n[... middle omitted ...]\n\n讨论。我们会在群内分享更详细的行业解读和定期更新的技术跟踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n量子计算谁在领跑？一文看懂\n\n量子竞赛，三强并立\n\n谁最可能先实现实用量子计算？\n\n最近看了某外资投行组织的量子行业专家分享，信息量很大，整理几个关键点👇\n\n1️⃣ 量子比特分两类：人造 vs 天然\n- 人造：超导、硅自旋、拓扑，速度快但噪声高、相干时间短\n- 天然：离子阱、中性原子，天生一致性好、抗噪强，但操作慢\n- 光子算中间态：天然载体+人造波导\n\n2️⃣ 目前三大主流技术路线\n- 超导：规模大、速度快、工业成熟，IBM/谷歌等重金投入，但长程交互是难题\n- 离子阱：天然支持长程交互，保真度高，速度慢但正在突破\n- 中性原子：近3年突飞猛进，哈佛/MIT团队成果亮眼，但仅少数团队能稳定实现\n- 其他路线：自旋/光子还在早期，拓扑风险高回报大但离实用很远\n\n3️⃣ 速度vs精度决定应用场景\n- 化学模拟、材料科学：需要大量重复采样→选超导（快）\n- 密码学、组合优化：需要精确答案→选天然量子比特（保真度高）\n- IBM预测今年实现“量子优势”，但大规模容错量子计算仍需多年\n\n4️⃣ 商业前景：云为主，巨头主导\n- 量子计算资本密集，未来大概率是云服务模式\n- 早期需求来自学术/政府/研究，金融/物流/优化\n\n[... middle omitted ...]\n\nert with 15 years experience in leading Quantum companies and large tech, as a follow-up to our recently published Quantum Deep dive note. This note is an edited transcript with key takeaways.\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R016",
    "title": "DB：中国车企在欧洲的渗透已从“试探”进入“阵地战”阶段",
    "digest": "[wechat_article.md]\n# DB：中国车企在欧洲的渗透已从“试探”进入“阵地战”阶段\n\n2026年4月，中国车企在欧洲市场的单月销量突破16.3万辆，同比增长41.7%，市场份额首次稳定在12%的关口。这个数字本身已经足够引起关注，但DB这份最新月度监测报告真正值得深读的信号，不是总量增长，而是增长结构的质变——中国车企正在从过去依赖俄罗斯市场的单一支点，转向对西欧核心市场的全面渗透。\n\n这份报告以月度追踪数据为基础，覆盖了欧洲主要国家的中国品牌销量。数据本身是冰冷的，但当我们将这些数字放在一起看时，一个清晰的判断浮现出来：中国车企的欧洲战略已经完成了“市场测试”阶段，进入了需要重资产投入、本地化运营和品牌建设的“阵地战”阶段。对于产业决策者和投资者而言，这意味着评估框架需要从“能不能卖出去”切换到“能不能留下来”。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 俄罗斯市场的收缩正在被西欧市场的爆发所对冲，中国车企的欧洲版图正在重新绘制\n\n这是这份报告最核心的结构性变化。2025年之前，中国车企在欧洲的销量高度依赖俄罗斯市场。但2026年前四个月的数据显示，中国车企在俄罗斯的销量同比下降13.8%，而同期在英国的销量飙升127.7%，意大利增长129.5%，德国增长139.0%。\n\n这不是简单的“东方不亮西方亮”。俄罗斯市场的收缩有地缘政治和制裁的叠加因素，而西欧市场的增长背后是中国车企产品力、渠道布局和品牌认知的综合提升。DB的数据清晰显示，4月份中国车企在西欧核心市场的销量占比已经超过了俄罗斯——英国、意大利、西班牙、德国、法国五国合计销量达到7.76万辆，而俄罗斯为5.33万辆。\n\n这意味着什么？中国车企正在完成一次市场重心的战略转移。过去几年，俄罗斯是中国品牌出海的“练兵场”和“利润池”，但这一池子正在变浅。真正决定中国车企海外\n\n[... middle omitted ...]\n\n据，以及围绕未解问题的小范围闭门讨论。扫描下方图片即可加入。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国车企，正在欧洲悄悄崛起\n\n欧洲市场 中国车企正在跑\n\n4月销量16.3万辆，同比增长41.7%\n\n1 总量在涨，份额在涨\n4月中国车企在欧洲卖了16.3万辆，同比+41.7%，市占率来到12%。虽然环比3月下降13.9%，但整体向上趋势明显。前4个月累计57.3万辆，同比+40.4%，欧洲正成为中国车企的重要增长极。\n\n2 各国表现分化，英国暴涨\n英国4月销量2.5万辆，同比+192.8%，前4个月累计11.2万辆，同比+127.7%。意大利4月2万辆，+130.4%。德国4月近1万辆，+144.3%。法国4月7744辆，+71.4%。俄罗斯反而是唯一同比下滑的主要市场，4月5.3万辆，-9.7%。\n\n3 谁是欧洲最猛的中国车企？\n4月奇瑞卖得最多，4.1万辆，市占率25%。上汽3万辆，比亚迪2.8万辆。但增速最猛的是零跑，4月8758辆，同比+415.8%，前4个月累计+590%。小鹏4月3344辆，+102.7%。蔚来还在起步阶段，4月仅46辆。\n\n4 德国市场：中国车企份额翻倍\n德国4月中国车企市占率4%，比去年同期的1.7%翻了一倍多。比亚迪在德国卖得最好，份额1.5%，上汽0.9%。中国品牌在德\n\n[... middle omitted ...]\n\n-7057\n\nFigure 1: Chinese OEMs European market volume by country\n\n<table><tr><td colspan=\"6\">Chinese OEM European Volume by Country</td></tr><tr><td>(unit)</td><td>Apr-26</td><td>YoY</td><td>Mo\n\n[... middle omitted ...]\n\nk, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R017",
    "title": "GS：中国餐饮的五月数据揭示的不是需求疲软，而是品牌分化的加速",
    "digest": "[wechat_article.md]\n# GS：中国餐饮的五月数据揭示的不是需求疲软，而是品牌分化的加速\n\n五月的数据，看起来有点“冷”。\n\nGS最新发布的餐饮月度追踪报告显示，五月同店销售增长（SSSG）较四月进一步走弱。五一假期需求温和，消费情绪未见明显提振，部分地区还受到天气扰动。如果你只看这个开头，很容易得出一个笼统的判断：消费复苏又踩了一脚刹车。\n\n但这份报告的真正价值，不在于确认“五月数据变差”这个已知事实，而在于它揭示了一个更为关键的结构性变化：品牌之间的分化正在加速，且这种分化并非简单的“大品牌抗跌、小品牌承压”，而是由商业模式、品类属性和成本结构共同决定的。那些仅仅用“消费降级”或“需求疲软”来解释一切的人，正在错过真正的投资信号。\n\n报告中最值得关注的判断是：**五月数据确认了高基数效应开始显现，但真正决定企业未来走势的，不是需求总量的波动，而是品牌能否在分化中构建起新的定价权和成本优势。** 这一点，在现制茶饮（FMD）和火锅两个赛道上表现得尤为突出。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 现制茶饮的高基数压力只是表象，真正的变量是品牌能否用新品和品类扩张对冲下滑\n\n五月，现制茶饮品牌普遍面临同店销售增长的压力，这在GS的预期之内。去年同期的强劲表现形成了一个较高的比较基数，高基数效应开始显现。但如果我们把目光从“同比”移开，观察环比和绝对量，会发现更值得关注的信号。\n\n奈雪的茶五月单店销售额同比下滑幅度从四月的-11%扩大至-24%。这个数据本身令人担忧，但更关键的是，它与其他头部品牌形成了鲜明对比。报告指出，头部品牌展现出更强的韧性，支撑力来自品类扩张和新产品。这意味着，在同样的宏观环境下，能否持续推出有吸引力的新品、能否在品类上找到新的增长点，正在成为区分品牌强弱的核心能力。\n\n这里需要警惕一个常见的误读：把高基数\n\n[... middle omitted ...]\n\n这可能是比单纯跟踪月度同店销售更有价值的思考方向。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月餐饮：消费降温，品牌分化加剧\n\n📊 5月餐饮数据出炉，整体趋势转弱\n\n五一过后消费情绪降温+天气影响，多数品牌同店增速环比4月放缓。但品牌之间分化明显，头部韧性仍在。\n\n1️⃣ 海底捞：翻台率同比微降\n- 5月翻台率同比转负（vs 4月+中个位数）\n- 对应恢复至2019年同期的80-85%水平，略高于4月但低于1Q\n- 管理团队认为端午假期移位（2025年5月只有1天）是扰动因素\n- 5月净关店4家直营+净开1家加盟\n\n2️⃣ 太二（九毛九）：同店增速仍保持高单位数\n- 5月中国大陆同店+低双位数，略低于4月但高于1Q\n- 五一期间受南方降雨拖累，节后反而加速\n- 新模式店持续贡献增量，老店也录得正增长\n- 但九毛九/松哥品牌压力仍在，同店-20%/-11%\n\n3️⃣ 新式茶饮：高基数效应开始显现\n- 奈雪5月单店销售同比-24%（4月-11%），压力显著扩大\n- 古茗/蜜雪/沪上阿姨等品牌同店增速也普遍承压\n- 积极信号：外卖占比环比/同比均下降，堂食有所回暖\n\n4️⃣ 价格战还在继续，但力度可控\n- 古茗推周周9.9元券，蜜雪对上线咖啡机的门店推买一送一\n- 瑞幸也推每日9.9元限定SKU\n- 研报\n\n[... middle omitted ...]\n\nds during Labor Day (SSSG up MSD%-HSD%), but post holiday SSSG has picked up. For freshly made drinks (FMD), high base impact has started to kick in, and brands have generally seen SSSG pressu\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R018",
    "title": "摩根斯坦利：市场对800V DC延迟的担忧被夸大了，真正的信号是供应链加速而非推迟",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场对800V DC延迟的担忧被夸大了，真正的信号是供应链加速而非推迟\n\n2026年6月9日，一则来自SemiAnalysis的报道在市场引发震动：NVIDIA原生800V DC电源架构的大规模出货被推迟至2028年，远低于市场预期。消息传出后，相关电源与散热供应链个股出现波动。但摩根斯坦利在Computex期间的供应链核查给出了截然不同的结论。\n\n这份6月10日发布的研报，虽然篇幅不长，却直接回应了市场中最大的一个争议点——AI基础设施的电源架构升级节奏是否已经放缓。我们的判断是：市场对这条消息的解读出现了方向性错误。真正的信号不是延迟，而是加速。800V DC的产业化路径不仅没有中断，反而在多个维度上比预期走得更快。\n\n以下是我们从这份摩根斯坦利研报中提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 800V DC的延迟消息与摩根斯坦利在Computex的一手供应链信息完全相悖\n\nSemiAnalysis的报道声称NVIDIA已将原生800V DC电源架构的大规模出货推迟至2028年。但摩根斯坦利分析师Sharon Shih在Computex期间的直接沟通中获取的信息截然不同：NVIDIA在GTC Taipei明确表示，800V DC电源机架（Power Rack）将在2026年第三季度准备就绪并进入量产。这一时间表与“推迟至2028年”的说法存在两年的差距。\n\n更关键的是，摩根斯坦利的供应链核查还发现了一个被市场忽视的趋势：原本计划走+-400V DC路线的多家超大规模云服务商，已经在将研发方向转向800V DC。这意味着，800V DC不仅没有延迟，反而正在成为行业共识的下一代标准。+-400V DC原本被视为过渡方案，如今其资源正在被重新分配至800V DC。\n\n这里\n\n[... middle omitted ...]\n\n交叉验证信息，持续追踪800V DC产业链的每一个关键节点。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n800V DC延期的真相来了\n\n800V DC 没延期？\n\n正文：\n最近有消息说某大厂的800V DC架构要推迟到2028年，市场有点慌。但根据某外资投行在Computex上的供应链调研，情况其实不一样。\n\n1️⃣ 进展如何？\n- 800V DC电源机架按计划在2026年Q3量产，不是2028年\n- +-400V的开发已经转向800V，多个超大规模客户都在转\n- 台达可能在2026年Q4成为首家量产800V独立电源机架的厂商\n\n2️⃣ 为什么有传言？\n- 800V的保护器件和工业安全标准还在制定中（UL认证等）\n- 初期出货量不会很大，需要时间完善生态\n- 但整体开发节奏没变，不要被单一消息带偏\n\n3️⃣ 时间线梳理\n- 2026年Q3：660kW电源机架就绪\n- 2027年Q2：1.6MW直流电源中心\n- 2028年Q1：4.8MW+电源模块\n- 接地保护、设备认证、连接器标准都在同步推进\n\n这次800V DC的节奏比很多人想的要稳，不是延期，是生态成熟需要时间。\n\n#学习笔记\n\n[source_mineru.md]\nJune 10, 2026 04:13 AM GMT\n\n# Greater China T\n\n[... middle omitted ...]\n\ned 800 VDC developments are ongoing with 800 VDC power rack being ready for mass production in 3Q26. +-400 VDC development has been redirected to 800 VDC focus across various hyperscalers. (Ex\n\n[... middle omitted ...]\n\naxy Co Ltd (2455.TW)</td><td>E (09/11/2023)</td><td>NT$395.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R019",
    "title": "美国银行：市场正在经历一场科技股信心的结构性重置，而非简单的避险",
    "digest": "[wechat_article.md]\n# 美国银行：市场正在经历一场科技股信心的结构性重置，而非简单的避险\n\n上周，标普500指数录得自2025年4月以来最大单周跌幅，跌幅达2.6%。在这样一次看似寻常的市场回调背后，美国银行（BofA）的最新客户资金流报告揭示了一个远比“避险”二字更为深刻的结构性信号：机构客户正以有数据记录以来最大的规模抛售科技股，单周个股净流出高达142亿美元。这并非一次战术性减仓，而是一场正在发生的、对科技资产定价逻辑的集体重估。\n\n这份报告的核心价值不在于告诉我们“谁在卖”，而在于揭示“卖的方式”和“卖的同时在买什么”。它指向一个正在成型的市场新叙事：资金正从过去几年主导市场的“科技+增长”单极化配置，转向一种更为分散、更注重估值保护与现金回报的多元格局。对于产业决策者和高净值投资者而言，理解这一资金流向的底层逻辑，远比预测下周指数涨跌更为重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 机构客户创纪录的科技股抛售，本质是对“规模溢价”的重新定价\n\n美国银行报告中最引人注目的数据点，是科技板块出现了自2008年有数据记录以来的最大规模资金流出。若以占板块市值百分比衡量，这一流出规模也是2014年初以来最极端的。卖盘的主导力量是机构客户，但对冲基金和私人客户同样在抛售。这不是某一类资金的孤立行为，而是整个专业投资者群体的共识性撤退。\n\n我们需要追问：为什么是科技？为什么是现在？\n\n过去两年，以Magnificent Seven为代表的科技巨头，其股价上涨的核心驱动力并非盈利增长，而是投资者愿意为“确定性”和“规模”支付的溢价。当宏观环境从通胀转向增长放缓，当AI商业化路径从“讲故事”进入“验证收入”阶段，这种溢价的基础开始松动。机构客户此刻的大规模抛售，可以理解为对“科技股是否仍应享有相对于其他板块的估值特权”这一问题的集\n\n[... middle omitted ...]\n\n合更多原始图表和后续数据，一起追踪这场资金大轮动的最终走向。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n科技股遭遇史上最大资金流出\n\n📉 历史级抛售\n\n上周标普500跌2.6%，某外资投行客户创纪录净卖出美股，单只股票流出达142亿美元。机构客户是主要卖家，对冲基金和私人客户也连续卖出。不过客户持续买入ETF，已连续11周净买入。\n\n资金完全从大盘股流出，小盘和中盘股反而获得买入。企业回购连续第二周放缓，但滚动四周均值仍升至3月底以来最高。\n\n1️⃣ 科技板块创纪录流出\n\n11个行业中有8个被净卖出，科技板块流出规模为该行2008年有数据以来最大（按市值占比算，是2014年初以来最大）。通信服务也连续第5周流出，但幅度远小于科技。\n\n仅工业、房地产和公用事业三个板块获得资金流入。房地产已连续6周获净买入。\n\n2️⃣ ETF偏好：价值>成长\n\n客户买入价值型和平衡型ETF，卖出成长型ETF。规模上，除小盘外，大中盘和宽基ETF均获买入。\n\n行业ETF中，医疗保健ETF流入为2021年10月以来最大；科技ETF流出最多，金融ETF紧随其后。\n\n3️⃣ 机构投资者在撤退\n\n机构客户此前连续5周买入后，上周成为最大净卖方（3月中旬以来最大规模）。私人客户净卖出量是2024年11月以来最高。\n\n从全年看，企业回购虽低于2\n\n[... middle omitted ...]\n\ncutive weeks, respectively. Net sales by private clients were the largest since Nov. 2024.  \n- Outflows were entirely in large caps, as clients bought small & mid cap equities.  \n- Corporate c\n\n[... middle omitted ...]\n\nw in accordance with firm policies.\n\nNeither BofA nor any officer or employee of BofA accepts any liability whatsoever for any direct, indirect or consequential damages or losses arising from any use of this information."
  },
  {
    "id": "R020",
    "title": "NOM：中国5月出口强劲，但市场真正低估的不是需求，而是价格信号的重估",
    "digest": "[wechat_article.md]\n# NOM：中国5月出口强劲，但市场真正低估的不是需求，而是价格信号的重估\n\n中国5月贸易数据再次超出预期。以美元计，出口同比增长19.4%，远高于市场一致预期的15.0%和NOM自己的13.7%预测；进口增长27.4%，也高于预期的26.0%。贸易顺差进一步扩大至1054亿美元。\n\n表面上看，这是一份“需求强劲”的报告。但NOM这份研报的核心洞察恰恰相反：**5月贸易数据的驱动力并非真实需求的扩张，而是一场由价格主导的结构性重定价。** 芯片价格飙升、能源价格冲击、以及关税政策变动带来的基数效应，共同制造了一个“名义增长强劲、实际量价严重背离”的贸易图景。\n\n理解这一点，比知道出口增长了19.4%重要得多。因为名义数据的强劲，正在掩盖一个关键事实：中国贸易的定价权正在发生转移，而这种转移将深刻影响产业链利润分配、汇率定价逻辑以及资产配置的方向。\n\n以下是我们从这份NOM研报中提炼出的五个关键判断。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. AI相关出口已连续两个月贡献中国总出口增长的近一半，但驱动力是价格而非数量\n\n这是整份报告最值得关注的结构性变化。NOM估算，5月集成电路（IC）单独贡献了出口增长的5.9个百分点，自动数据处理设备（ADP）贡献了3.4个百分点，两者合计9.3个百分点，占中国5月总出口增长的约48%。这已是连续第二个月AI相关出口贡献率接近50%。\n\n但真正的看点不在于比例高，而在于驱动方式。5月IC出口金额同比增长110.9%，但出口数量仅增长2.1%，这意味着价格贡献高达106.5个百分点。进口端同样如此：IC进口金额增长68.0%，但数量转为负增长-1.0%，价格贡献69.8个百分点。DRAM和NAND二季度合约价格上涨的传导效应，正在制造一场“名义繁荣、实际平淡”的半导体贸易。\n\n[... middle omitted ...]\n\n基于原始数据的交叉验证分析。这些内容，无法通过公开渠道获取。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月出口数据超预期，AI是主角\n\n📊 出口超预期，AI是主引擎\n\n5月出口增速19.4%，高于预期的15%，进口增速27.4%也超预期。贸易顺差扩大到1054亿美元。\n\n1️⃣ AI相关产品贡献了一半出口增长\n芯片出口贡献5.9个百分点，自动数据处理设备贡献3.4个百分点，两者合计贡献9.3个百分点。连续两个月AI相关出口占中国总出口增长的一半左右。\n\n2️⃣ 价格效应大于数量效应\n芯片出口量只增长2.1%，但出口额增长111%。价格贡献了106.5个百分点。进口端也是类似，芯片进口量下降1%，但进口额增长68%。\n\n3️⃣ 对美出口大幅反弹\n5月对美出口增长37.3%，主要因为去年同期的低基数、关税暂时下调、以及美国AI需求。\n\n4️⃣ 劳动密集型产品仍承压\n服装、鞋类、箱包、玩具出口同比分别下降4.1%、10.3%、4.9%、7%，改善幅度有限。\n\n5️⃣ 原油进口量价背离\n原油进口金额增长15.3%，但进口量下降29%，反映价格高企下的主动减少采购。\n\n有意思的是，5月芯片进口价格贡献从4月的39.2个百分点大幅上升到69.8个百分点，可能是DRAM和NAND二季度合约价格上涨的传导。\n\n#学习笔记\n\n[\n\n[... middle omitted ...]\n\nbetween value and volume growth widening further, as chip price increases continued to overwhelm quantity growth. We estimate chips contributed 5.9pp to headline export growth. Together with a\n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R021",
    "title": "Bernstein：数据中心真正的拐点不在建设量，而在供电模式的结构性重置",
    "digest": "[wechat_article.md]\n# Bernstein：数据中心真正的拐点不在建设量，而在供电模式的结构性重置\n\n市场对AI基础设施的讨论，大多集中在GPU算力需求、资本开支节奏、以及“泡沫何时破裂”的宏观叙事上。这些讨论并非没有价值，但它们往往忽略了一个正在发生的、更为根本的结构性变化：数据中心从“电网依赖型”向“自备发电型”的加速迁移。Bernstein最新发布的北美数据中心追踪报告（2026年5月）提供了一个关键信号：这一迁移的速度和规模，正在重塑整个产业链的价值分配，而市场对此的定价可能仍不充分。\n\n这份报告的核心价值，不在于它更新了324GW的总管道容量，也不在于它记录了4.4GW的新增在建工程。真正值得关注的，是“自备发电”（Behind-the-meter, BTM）管道容量在一个月内增长了14GW，同比年初至今暴增42GW，达到129GW。更关键的是，目前在建设的容量中已有25%采用BTM模式，而管道中的项目这一比例已高达40%。这意味着，未来几年内，将有近一半的新增数据中心不再完全依赖公共电网供电。\n\n为什么这很重要？因为供电模式的选择，直接决定了哪些供应商能够从中受益。当数据中心自备发电时，其对电气设备的需求结构会发生根本性变化。Bernstein估算，自备发电项目在电气分配设备上的支出比纯电网接入项目高出约30%。这才是这份报告最值得仔细拆解的核心洞察：市场真正低估的不是数据中心的需求总量，而是供电模式重置带来的供应链价值再分配。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 管道总量增长10%并非重点，真正值得追问的是“谁在推动增长”\n\nBernstein的报告显示，5月份北美数据中心项目管道总量增长了29GW，达到324GW，环比增长10%。这个数字本身并不令人意外——市场已经习惯了AI基础设施的指数级增长叙事。但报告\n\n[... middle omitted ...]\n\n和原始图表，并就BTM模式对具体公司的影响进行更深入的拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n数据中心暗流涌动：324GW项目背后的新趋势\n\n**数据中心暗战**\n\n**项目激增，但格局在变**\n\n某外资投行最新报告更新了北美数据中心追踪数据，5月项目管线增加10%至324GW，信息量很大。\n\n**1/ 新增主力变了**\n- 开发者（22GW）和加密矿商（6GW）贡献了新增的96%\n- 超大规模云厂商反而小幅缩减管线\n- 德克萨斯和犹他州是新增热点\n\n**2/ 建设加速，但方式不同**\n- 在建容量增至63GW，Meta和亚马逊贡献了超大规模厂商增量的90%\n- 一个关键变化：25%在建容量采用“表后供电”（BTM），管线中更高达40%\n- 表后供电项目比纯电网项目多花约30%的配电设备\n\n**3/ 阻力与机会并存**\n- 因社区反对而搁浅的容量升至34GW，占管线11%\n- 电气设备市场空间巨大：单是数据中心领域，估算配电设备TAM就高达数千亿美元量级\n- 发电机和现场发电设备需求持续走高\n\n投研圈都在讨论：当超大规模厂商放缓、加密矿商和开发商接棒，数据中心供应链的受益者会不会换一批？\n\n#学习笔记\n\n[source_mineru.md]\n## US Industrials & Tech\n\n# US\n\n[... middle omitted ...]\n\na5a4a3b0d1ecae553f6dffe37c34aafc845de72f13ac4f71184.jpg)\n\nVarun Govindaraj\n\n+1 917 344 8543\n\nvarun.govindaraj@bernsteinsg.com\n\n![](images/07fb8b0b86a943a0c293578cbc8c3a39305f92ac99668424dcf891\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R022",
    "title": "摩根斯坦利：中国金融体系真正的转折点不是刺激，而是“高质量”的内生循环",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：中国金融体系真正的转折点不是刺激，而是“高质量”的内生循环\n\n市场对中国金融板块的讨论，长期陷入一个二元对立框架：要么依赖大规模财政刺激拉动信贷，要么承受经济减速带来的资产质量恶化。但摩根斯坦利在近期发布的一份系列研报中，提出了一个更具穿透力的判断——中国金融体系正在进入一个“更可持续的高质量发展”正循环，而这个循环的驱动力并非来自政策强心针，而是来自产业结构自身调整带来的利润修复、信贷理性化以及居民资产配置的结构性迁移。\n\n这份报告的核心主张值得每一位关注中国资产定价的决策者认真对待：市场真正低估的，不是短期需求刺激的力度，而是供给侧出清与金融体系内生质量改善叠加后，银行板块盈利能力和估值体系可能发生的系统性重定价。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 出口与工业利润的“超预期正循环”正在取代旧有的刺激依赖\n\n报告开篇即点明一个关键背景：尽管宏观数据在近几个月出现一些分化与波动，但一个没有大规模刺激的“高质量发展”路径，正在为金融体系提供更可持续的支撑。这个判断并非空谈，而是建立在三个相互印证的数据链条之上。\n\n第一，出口增长在2026年一季度表现强劲，YTD出口增速在4月仍维持在14.5%的同比高位。更重要的是，摩根斯坦利指出，这次出口增长并非简单的价格竞争或全球补库，而是由“科技与产业升级”驱动。这意味着出口增长的可持续性和含金量，与过去几轮周期有本质区别。\n\n第二，工业利润的修复正在加速。2026年4月，制造业利润YTD同比增速进一步加快至20.4%。与此同时，PPI在4月环比上涨1.7%，同比上涨2.8%，正式回到正值区间。PPI回正与利润增长同步发生，说明企业端不仅是在“量”上恢复，更是在“价”上获得了改善，这是利润修复质量提升的关键信号。\n\n第三，最值得关注的信号来自制造业\n\n[... middle omitted ...]\n\n们将结合原始研报图表与数据，深入拆解这些尚未完全展开的议题。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n银行体系正在变健康？聊聊新逻辑\n\n中国金融体系正在“换挡”\n\n投行研报近期指出，中国金融体系正在从“量”转向“质”。简单说，就是不再追求贷款规模猛增，而是更注重可持续的良性循环。\n\n几个关键变化值得关注：\n\n1️⃣ **净息差可能提前见底**\n研报认为，银行净息差（NIM）的反弹可能比预期来得更早。这意味着银行最“难受”的利润压缩期，或许正在过去。\n\n2️⃣ **贷款增长更理性**\n过去那种“全民加杠杆”的贷款竞赛在降温。一个标志性事件是，普惠小微贷款不再设定量增长目标。贷款增速放缓，但结构更健康。\n\n3️⃣ **消费支付回暖了**\n1Q26的系统支付总额同比增长29%（4Q25仅为5%）。银联卡消费增速也转正，同比增长3.2%（2025年还是负增长）。大家更愿意花钱了。\n\n4️⃣ **家庭资产向投资迁移**\n居民新增储蓄中，有更多钱流向了投资，而不是趴在银行存款里。这对银行来说，意味着财富管理业务的机会。\n\n5️⃣ **工业利润在改善**\n尽管宏观数据有波动，但制造业利润增速在加快，2026年4月累计同比增20.4%。产能过剩风险正在降低，工业企业的“还债能力”在变强。\n\n**核心逻辑：** 这轮金融体系的\n\n[... middle omitted ...]\n\nnew household savings shifting to investments (14 May 2026)\n\nChina Financials: Another Milestone Policy Change – No More Quantitative Target for Inclusive SME loans (20 May 2026)\n\nMS ASIA LIMI\n\n[... middle omitted ...]\n\npment Bank (600000.SS)</td><td>E (08/05/2025)</td><td>Rmb9.37</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R023",
    "title": "Bernstein：亚马逊供应链的真实威胁，被市场高估了",
    "digest": "[wechat_article.md]\n# Bernstein：亚马逊供应链的真实威胁，被市场高估了\n\n过去几周，市场对亚马逊推出“Supply Chain by Amazon”的讨论持续升温。投资者最关心的问题是：当亚马逊向第三方卖家开放其强大的履约网络，UPS和FedEx的包裹业务会不会遭遇结构性冲击？\n\n直觉上，答案似乎是肯定的。亚马逊的履约能力有目共睹——Prime两日达甚至当日达已经成为行业标准，其物流基础设施的投入和效率也让传统承运商相形见绌。如果更多商家能够接入这套体系，UPS和FedEx的份额流失似乎是必然。\n\n但Bernstein这份研报给出了一个反直觉的核心判断：**亚马逊的前置库存模型在供应链结构上存在天然局限，真正适合采用该模式的零售市场上限约为20%，而考虑到数据隐私和服务容错等现实约束，实际可渗透的市场可能只有低个位数百分比。**\n\n这不是一个关于“亚马逊能不能做”的问题，而是一个关于“哪些供应链结构天然不适合前置库存”的问题。Bernstein的分析框架揭示了决定这一问题的三个核心变量：持有成本、货位成本和运输节省。当这三者的数学关系摆到台面上，亚马逊供应链的真实威胁边界就清晰了。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 供应链不是万能模板，前置库存模型只在特定品类中成立\n\n要理解Bernstein的核心论点，首先要接受一个基本前提：供应链不是“一刀切”的解决方案。不同品类的产品属性、客户需求和成本结构，决定了完全不同的网络拓扑设计。\n\nBernstein在报告中明确指出，供应链设计需要权衡三大类成本：运输成本、库存处理成本（包括仓储和地产），以及软性成本（如融资成本、过时折价和降价损失）。高周转、低价值密度的商品，适合采用密集的前置网络以最小化最后一公里成本和周期时间；而高价值、慢周转的商品，则更适合集中化库存以保\n\n[... middle omitted ...]\n\n信群里继续讨论。那里我们会分享完整的原始图表和更细致的拆解。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n亚马逊供应链，真的能吃掉快递市场吗？\n\n**供应链拆解：谁适合亚马逊模式？**\n\n最近大家都在猜，亚马逊开放供应链服务，UPS和FedEx会不会很受伤？某外资投行用一套模型算了一笔账，结论有点意思。\n\n**1/ 不是所有货都适合“前置仓”**\n亚马逊模式的核心是：把货提前放到离你近的仓库，运费省了，但库存成本和仓储费涨了。\n模型显示，只有**“便宜、好卖、体积小”**的商品才划算。比如，单价50美元、周转快的日用品。\n而那些**“贵、卖得慢、占地方”**的商品（比如家具、高价值电子产品），放前置仓就是亏钱——持有成本太高。\n\n**2/ 算一笔账：前置仓 vs 中央仓**\n模型对比了两种模式：\n- **中央仓**：集中库存，靠快递发货\n- **前置仓**：分散到20个节点，库存翻倍\n\n关键公式：**前置仓成本 = 库存持有成本增加 + 仓储成本增加 - 运输成本节省**\n结果：对于单价2240美元的商品，前置仓每年多花215万美元。运输省下的钱根本补不上库存的窟窿。\n\n**3/ 真实市场有多大？**\n研报估算，按零售额算，只有**约20%**的商品结构上适合前置仓模式。\n再考虑数据安全、服务依赖等现实因素，实际\n\n[... middle omitted ...]\n\n8ebe654efb6537522b4056d203d7f6ad7274638974b185d8bd5953f36927b09.jpg)\n\nDeeksha Pandey\n\n+1 917 344 8447\n\ndeeksha.pandey@bernsteinsg.com\n\n![](images/6a2a3bce0b41fdb5657037bc81e789085db3c43462a9d4\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R024",
    "title": "Citi：中国生物科技面临的地缘政治风险，市场可能高估了法案通过概率",
    "digest": "[wechat_article.md]\n# Citi：中国生物科技面临的地缘政治风险，市场可能高估了法案通过概率\n\n当前市场对中美生物科技脱钩的担忧，可能正在定价一个低概率事件。Citi在最新一份专家电话会纪要中释放了一个清晰但容易被忽视的信号：旨在限制美国对华生物科技投资的BINSA法案，在本届国会会期内成为法律的可能性非常低。这个判断不是基于乐观情绪，而是基于对美国立法流程、行政机构态度和产业游说力量的结构性分析。\n\n这份报告的价值不在于它给出了一个“风险解除”的结论，而在于它拆解了为什么市场习惯性高估这类法案的落地概率。对于持有中国CXO、生物科技资产的投资者，以及正在评估供应链风险的产业决策者，理解这个判断背后的逻辑，比直接相信结论更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 法案通过概率低于市场隐含预期，核心障碍在立法流程而非政治意愿\n\nCiti专家给出的BINSA法案通过概率区间为30-40%以下。这个数字本身已经低于许多市场参与者的隐含预期。但更值得关注的是概率的结构：三种可能的立法路径各有不同的障碍，而每一条路径都面临实质性的制度阻力。\n\n路径一，作为FY2027 NDAA修正案附加上市，概率30-35%。关键障碍在于众议院军事委员会主席明确反对将不相关条款附加到NDAA上。FY2027 NDAA的众议院版本已经在委员会层面清除了BINSA相关条款。路径二，由财政部采取行政行动，概率35-40%。但财政部已明确表示，现行法律下它没有监管生物科技对外投资的法定权限。路径三，作为独立法案通过，概率低于10%，因为目前没有参议院配套法案。\n\n这些障碍不是“有可能被克服”的，而是制度性的。NDAA历来有“不相关条款”的惯例约束，财政部的法定权限边界清晰，而独立法案需要完整的立法周期——专家估计至少1至1.5年。在一个国会会期内完成所有\n\n[... middle omitted ...]\n\n已经过度定价了地缘政治风险，哪些公司的基本面正在被市场忽略。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n生物科技出海，政策风险在降温\n\n政策风向下，机会在哪？\n\nBINSA法案通过概率低，1260H清单影响有限\n\n最近关于中国生物科技出海的政策担忧不少，但某外资投行的专家电话会给出了更清晰的判断。\n\n1️⃣ BINSA法案，通过概率不足40%\n- 这项针对生物科技的投资限制法案，目前国会支持度有限，仅是密歇根州议员推动，并非全国性共识\n- 即使推进，完整立法流程也要1-1.5年\n- 财政部态度冷淡，因为执行难度太大\n- 制药和生物科技行业正在积极游说，是强大的反制力量\n\n2️⃣ 三种可能的通过路径，都不太乐观\n- 纳入国防授权法修正案：概率30-35%，但众议院军事委员会主席反对\n- 财政部行政行动：概率35-40%，但财政部明确表示缺乏法律授权\n- 独立法案通过：概率低于10%，目前参议院无配套法案\n\n3️⃣ 即使通过，也会是“缩水版”\n- 行业预计会大幅豁免：缩小受监管实体定义、排除许可合作、提高交易审查门槛\n- 被动投资、国家利益豁免等条款都会加入\n\n4️⃣ 1260H清单影响有限\n- 药明康德被列入，但仅影响联邦资助项目合作\n- 公司已宣布反对，预计会启动行政复审或法律挑战\n- 市场早有预期，影响可控\n\n[... middle omitted ...]\n\nven if it advances, a full legislative cycle would likely take 1–1.5 years. The Treasury Department (the lead agency for COINS) is at most lukewarm because of the administrative difficulties t\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R025",
    "title": "GS：欧洲半导体设备市场的下一个增长动力，不是周期，是结构",
    "digest": "[wechat_article.md]\n# GS：欧洲半导体设备市场的下一个增长动力，不是周期，是结构\n\n这份GS最新发布的欧洲科技硬件研报，在标题中使用了“更新估值与目标价”这样克制的措辞。但当我们穿透数字调整的表层，会发现这远不止是一次季度性的财务模型微调。它实际上在传递一个更为根本的信号：欧洲半导体设备与AI基础设施领域，正在经历一轮由多重结构性力量共同驱动的价值重估。\n\nGS分析师Alexander Duval及其团队，同时上调了ASML、ASMI、BESI和Nebius四家公司的目标价，并同步提升了远期盈利预测。这四家公司分别覆盖光刻、沉积、封装和AI算力基础设施——几乎构成了从芯片制造到AI部署的完整价值链。而驱动这轮集体上调的，并非单一事件，而是三个彼此独立、却同时指向同一方向的信号。\n\n这份报告最值得关注的判断是：市场此前对欧洲AI使能者的定价，低估了其长期增长空间的持续扩展能力。当前的上修，只是这一过程的开始。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 三大信号同时指向一个方向：设备需求周期尚未见顶\n\nGS在报告中列举了近期三个关键数据点，分别来自存储、AI基础设施和中国市场。单独看，每个信号都有其自身的产业逻辑；放在一起，它们共同回答了一个关键问题：这轮半导体设备投资的强度，是否已经接近尾声？\n\n第一个信号来自SK海力士。据媒体报道，这家全球领先的HBM供应商计划在未来五年内将晶圆产能翻倍。GS明确指出，这一计划进一步增强了市场对“多年存储器投资周期”的信心。HBM（高带宽存储器）是AI芯片的关键配套，其产能扩张意味着对前道设备的需求将持续释放。这不是一个短期补库存行为，而是基于AI推理和训练需求的结构性扩产。\n\n第二个信号来自博通。博通重申其预期：到2027财年，AI半导体收入将超过1000亿美元，对应10GW的数据中心容量建\n\n[... middle omitted ...]\n\n公开文章中无法完全展开，但恰恰是深入理解这份报告价值的关键。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n欧洲AI硬件这波，逻辑很顺\n\n欧洲半导体设备，正被AI催热\n\n最近某外资投行更新了四家欧洲AI硬件公司的看法，核心逻辑是：AI从概念走向落地，带动了设备采购和基础设施扩张，而且数据越来越扎实。\n\n1️⃣ 存储率先表态\nSK海力士计划五年内翻倍晶圆产能，HBM需求持续高烧，存储投资周期拉长是大概率事件。\n\n2️⃣ AI基础设施没降温\n博通重申FY27 AI半导体收入将超1000亿美元，对应10GW数据中心扩容，且预计FY28在此基础上继续增长。\n\n3️⃣ 中国设备支出韧性超预期\nLAM和KLA最新指引显示，中国WFE支出在CY26大致持平或微增，比之前担心的更稳，支撑全球设备需求。\n\n4️⃣ 主权AI加速\n英伟达披露，主权AI收入在1QFY27同比增长超80%，政府主导的AI基建正在成为新引擎。\n\n5️⃣ GPU定价依然强势\nH100/A100定价年初至今分别涨20%/15%，需求持续跑赢供给。\n\n6️⃣ 欧洲AI云商跟进\nNebius宣布在英国投资约17亿英镑，部署三座英伟达设施，总容量2027年达65MW。\n\n基于这些信号，投行上调了ASML/ASMI/BESI未来几年的收入和盈利预测，也上调了Nebius\n\n[... middle omitted ...]\n\nevelopments across AI adoption/demand which continue to point towards a healthy demand backdrop across both Semiconductor Capital Equipment and AI Infrastructure. Please see more details below\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R026",
    "title": "摩根斯坦利：CPO市场真正的分歧不在技术，而在量产节奏的预期差",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：CPO市场真正的分歧不在技术，而在量产节奏的预期差\n\n市场对CPO（共封装光学）的担忧正在加剧。过去几周，投资者反馈的核心焦虑是：CPO导入是否在推迟？相关标的的抛售是否意味着长期逻辑动摇了？\n\n摩根斯坦利在最新发布的CPO专题报告中给出了一个反直觉的判断：长期故事没有改变，但市场短期预期确实需要重置。这份报告的价值不在于告诉你CPO会来，而在于精确地告诉你它将以什么样的节奏、在什么样的约束条件下到来——以及当前股价中隐含的假设与这个节奏之间有多大的裂口。\n\n报告的核心结论可以浓缩为一句话：2027年光学引擎出货量预计仅为600-700万颗，远低于市场期待的2000-3000万颗。这不是技术失败，而是量产爬坡的物理约束。而真正的爆发，将从2028年开始。\n\n以下是我们从这份报告中提炼的五个层次洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 市场对2027年的出货量预期存在3-5倍的过度乐观，这是短期情绪修正的核心驱动力\n\n摩根斯坦利对2027年光学引擎（Optical Engine, OE）出货量的基准预测是600-700万颗，涵盖scale-up和scale-out两种方案。而投资者普遍期待的出货量落在2000-3000万颗区间。\n\n这个差距不是技术路线之争，而是量产节奏的根本性误判。市场往往倾向于线性外推——一旦看到台积电宣布将PIC产能扩张至10kwpm，就默认出货量会同步放大。但摩根斯坦利的分析指出，产能扩张只是必要条件，远非充分条件。\n\n这里的关键变量是良率。报告明确指出，SolC（Silicon on Carrier）良率目前仅为50-60%，下游组装良率更是低至20-50%。这两个数字才是决定最终出货量的真正瓶颈。产能可以快速扩张，但良率的提升需要时间、经验曲线和工艺迭代。\n\n[... middle omitted ...]\n\n些未解问题的进展，并在关键信号出现时进行深度解读。\n\n---\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nCPO光引擎：预期差下的机会\n\n**CPO预期差**\n\n市场担心CPO推迟，但长期故事没变\n\n1️⃣ **2027年光引擎出货量预估**\n某外资投行最新模型显示，2027年光引擎出货约600-700万颗\n而市场普遍预期是2000-3000万颗\n这个差距意味着短期情绪可能需要重新调整\n\n2️⃣ **制造瓶颈是关键变量**\nPIC产能虽在2027Q1扩至10kwpm\n但SolC良率仅50-60%\n下游封装良率更低，只有20-50%\n这两个良率是决定最终出货量的核心变量\n\n3️⃣ **时间节奏很清晰**\n2026-2028年是共存期：光模块、CPO、铜缆并行\n主流方案仍是1.6/3.2T\nCPO真正爆发要等到2028年之后\n长期催化剂路径依然完整\n\n产业链里，FOCI的CPO收入预计3季度末开始爬坡，之前主要在做量产准备。苏州天孚在CPO组件上有机会，但估值溢价明显。\n\n你们觉得2027年CPO出货量会落在哪个区间？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\nJune 10, 2026 03:53 AM GMT\n\n# Greater China Technology Semiconductor\n\n[... middle omitted ...]\n\ner major swing factor for final CPO-related shipments.  \nPositioning the inflection, CPO starting to boom from 2028 onward should support a longer-dated catalyst path despite near-term resets \n\n[... middle omitted ...]\n\ny Co Ltd (6515.TW)</td><td>O (04/17/2026)</td><td>NT$8,610.00</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R027",
    "title": "摩根斯坦利：中国保险业真正的分化不在规模，而在产品策略与渠道控制力",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：中国保险业真正的分化不在规模，而在产品策略与渠道控制力\n\n中国保险业正在经历一场由监管驱动、龙头主导的深度结构性转型。摩根斯坦利在最新发布的2026年行业观察报告中指出，过去两年间，上市保险公司已基本完成从传统险向分红险的产品切换，但这一轮转型的真正含义并非简单的产品替代，而是行业竞争格局的重新洗牌——大型保险公司与中小型保险公司正在走向截然不同的发展路径。\n\n这份报告最值得关注的核心判断是：市场对保险板块的定价可能低估了龙头公司在负债端转型与资产端优化中积累的结构性优势，同时也高估了中小保险公司在低利率环境下维持增长的能力。行业整体风险可控，但分化正在加速，而2026年一季度开始执行的更严格的偿付能力报告披露规则，将第一次让外界清晰地看到这种分化。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 分红险占比超过80%，但产品策略的分水岭才刚刚出现\n\n摩根斯坦利的数据显示，到2026年一季度，上市保险公司的新业务中分红险占比已超过80%，部分公司甚至接近90%。这一数字在2025年上半年还不到50%。转型速度之快，远超市场预期。\n\n但报告真正有价值的洞察在于：大型保险公司与中小型保险公司对这一趋势的态度正在发生根本性分歧。大型保险公司将继续深耕分红险，依托代理人渠道的惯性维持产品延续性；而许多中小保险公司自2026年二季度起已经开始重新评估策略，部分公司甚至重新加大了传统险的销售力度。\n\n为什么会出现这种分化？摩根斯坦利给出了四个层面的解释。\n\n第一，实际成本更高。虽然分红险的保证负债成本低于传统险，但计入非保证部分后的实际负债成本更高，降低分红实现率又可能削弱产品竞争力。\n\n第二，利润分享机制侵蚀股东收益。分红险的客户利润分享特性意味着，当保险公司获得超额投资收益时，更多收益将流向客户而非股东，这\n\n[... middle omitted ...]\n\n在群内分享完整报告的解读笔记、关键图表以及更深入的行业讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n2026保险业观察：大公司领跑，中小险企分化\n\n保险业正在变安静\n\n大公司稳健，小公司摇摆\n\n某外资投行最新研报拆解了2026年中国保险业的两大关键变化：\n\n1/ **产品大迁移基本完成**\n过去两年，上市险企基本完成了从传统险向分红险的转型。到2026年1季度，分红险占新单保费比例已超过80%，相比2025上半年的不足50%大幅提升。驱动因素：利率持续走低+监管引导，分红险的收益比银行定存更有吸引力。\n\n2/ **大公司与中小公司开始分化**\n大险企会继续主攻分红险，靠代理人渠道惯性维持产品连续性；但中小险企开始重新考虑策略，可能回归传统险+分红险的均衡配置。原因：\n- 分红险实际成本不低（含非保证部分）\n- 分红机制会分走股东利润\n- 资本占用可能更高\n- 现金流管理更复杂\n\n**银保渠道：大公司优势更明显**\n银保渠道2025年新单保费增长超15%，2026年1季度继续增长17%。大险企在银保渠道的分红险占比达85%+，而中小险企约58%。同时，大险企有更均衡的渠道结构（代理人渠道贡献60%-80%保费），中小险企严重依赖银保（50%-100%）。\n\n**投资端也在优化**\n利率虽已企稳，但债券交易需求\n\n[... middle omitted ...]\n\nition towards more diversified product strategy. Over the past two years, listed insurers have largely completed the transition, with $>80\\%$ of new premiums in par products in 1Q26. Many smal\n\n[... middle omitted ...]\n\nmp; C Insurance Co Ltd (6060.HK)</td><td>O (05/30/2023)</td><td>HK$10.55</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted."
  },
  {
    "id": "R028",
    "title": "BARC：市场低估了中国出口的结构性韧性，AI与绿色技术正重塑贸易格局",
    "digest": "[wechat_article.md]\n# BARC：市场低估了中国出口的结构性韧性，AI与绿色技术正重塑贸易格局\n\n这份由BARC在5月发布的中国贸易数据研报，其核心判断并非简单的“出口超预期”。真正值得关注的信号是：中国出口的驱动力正在从传统的成本优势与全球周期顺风，转向由AI资本开支与能源转型共同支撑的结构性需求。5月出口同比增长19.4%，远超市场预期的15%，这背后不是一次性的基数效应，而是全球制造业活动持续处于四年高位（PMI 52.6）与高附加值产品需求爆发共同作用的结果。\n\n报告揭示了一个重要的产业现实：市场此前担心中东能源冲击会抑制外部需求，但事实证明，AI相关产品与绿色技术出口恰恰成为了对冲这一风险的关键力量。半导体出口同比暴增111%，自动数据处理设备增长66%，这些数字背后是持续的全球AI资本开支周期。中国作为AI制造组件的关键供应商，正在享受这一轮技术投资红利。与此同时，能源冲击反而加速了全球绿色转型，中国在电动车、锂电池、风电机组和太阳能电池等领域保持低成本高质量的供给优势，这些品类的年初至今出口均维持两位数增长。\n\n这份报告的价值不仅在于数据本身，更在于它提供了一个观察中国出口新逻辑的分析框架。传统的贸易分析聚焦于目的地市场的景气度，而BARC的分析指向了一个更深刻的判断：中国出口的结构正在发生根本性转变，高附加值产品正在成为新的增长锚点。以下是我们基于报告逻辑的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 对美出口修复并非孤立事件，区域贸易网络正在重新激活\n\n5月对美出口同比飙升35.4%，远高于4月的11.3%，这确实部分得益于去年同期“解放日”关税后的低基数。但BARC的月度环比数据提供了更有说服力的证据：5月对美出口环比增长6.2%，好于2022-2024年约5.6%的平均水平（剔除2025年关税扭\n\n[... middle omitted ...]\n\n真实驱动因素。这些讨论将帮助您建立更完整的投资决策参考框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月出口又超预期，AI和绿色科技是主力\n\n🔥 出口增速再超预期\n\n5月出口同比增长19.4%，比4月的14.1%明显提速，也超过了市场预期（Bloomberg预测15%）。全球制造业PMI保持在52.6的高位，说明外需整体不错。\n\n1️⃣ 对美出口大幅回升\n- 对美国出口增长35.4%（4月仅11.3%），主要受低基数影响\n- 对东盟出口增长24.3%，对日韩台出口增长27.5%\n- 但对欧盟和英国的出口增速放缓\n\n2️⃣ AI相关产品是最大亮点\n- 高科技产品占出口总额29.8%，同比增长51%\n- 半导体出口翻倍（+111%），自动数据处理设备增长66%\n- 全球AI资本开支周期持续支撑需求\n\n3️⃣ 绿色科技产品保持强劲\n- 电动载人汽车、锂电池、风电、太阳能电池都保持两位数增长\n- 地缘政治紧张推动全球绿色转型，中国作为低成本高质量供应商受益\n\n4️⃣ 进口方面\n- 进口增长27.4%，主要受能源和半导体价格上涨推动\n- 半导体进口值大幅增长，但原油进口量下降29%\n- 大豆进口量下降15%，但仍是5月份历史第二高\n\n5月初的高频航运数据显示出口势头依然不错，6月可能继续超预期。\n\n#学习笔记\n\n[s\n\n[... middle omitted ...]\n\nina's export growth accelerated further, rising 19.4% y/y in May following a 14.1% increase in April, exceeding both the market and our expectations (Bloomberg: 15%, BARC: 14%). Breakdown data\n\n[... middle omitted ...]\n\nrior written permission of BARC. BARC Bank PLC is registered in England No. 1026167. Registered office 1 Churchill Place, London, E14 5HP. Additional information regarding this publication will be furnished upon request."
  },
  {
    "id": "R029",
    "title": "GS：市场真正低估的不是AI需求，而是2027年资本开支的上行风险",
    "digest": "[wechat_article.md]\n# GS：市场真正低估的不是AI需求，而是2027年资本开支的上行风险\n\n当大多数投资者还在为2026年84%的资本开支增速感到兴奋时，一个更重要的信号正在被系统性低估：2027年的资本开支曲线可能远比共识预测陡峭。这不是一个简单的“多花几百亿”的问题，而是意味着AI基础设施的投资强度正在逼近甚至超越历史上铁路、汽车和电力网络建设时期的GDP占比。\n\nGS这份最新研报的核心判断是：共识预测中2027年超大规模云厂商资本开支仅为9200亿美元、增速骤降至22%，但这一数字可能被大幅低估。如果增量投资达到GDP的2%至3%，2027年资本开支将落在1.1万亿至1.25万亿美元区间；在更为激进的情景下，基于现金流和投资级债券市场容量，这一数字甚至可能达到1.43万亿美元。\n\n这不是一个关于“AI有没有泡沫”的争论，而是一个关于“资本开支曲线形状”的定价问题。市场当前对AI基础设施股票的定价，隐含的是资本开支增速从84%断崖式下滑至22%的预期。如果真实曲线更为陡峭，那么整个AI基础设施受益股的盈利和估值框架都需要重估。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 共识预测已经连续三年低估资本开支，2027年可能重演\n\n理解这份报告的关键，不在于2026年的数字，而在于2027年的假设。\n\n当前共识预测显示，超大规模云厂商2026年资本开支为7570亿美元，同比增长84%；但到了2027年，这一数字仅微增至9200亿美元，增速骤降至22%。这种急剧的增速下滑，构成了当前市场对AI基础设施股票定价的核心假设。\n\n问题在于，这个假设的历史记录并不好。GS研报指出，在过去三年中，分析师对超大规模云厂商资本开支的预测平均低估了45个百分点。2024年初，共识预测增速为19%，实际执行结果为54%；2025年初预测22%，实际为\n\n[... middle omitted ...]\n\n些；3) 当资本开支增速拐点来临时，哪些细分领域最具防御性。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nAI的资本开支，比想象中更猛\n\nAI资本开支还没见顶\n\n2027年可能比市场预期的还要高\n\n---\n\n最近看了某外资投行对AI基础设施的深度研报，有几个反直觉的发现：\n\n**1/ 市场对2027年资本开支的预测可能太保守了**\n目前分析师预计2027年超大规模云厂商的资本开支是9200亿美元，增速从84%骤降到22%。但研报指出，过去三年分析师平均低估了45个百分点。如果参照铁路和汽车工业时期的投入强度（占GDP的2-3%），2027年可能达到1.1万亿美元。\n\n**2/ 更极端的情况是1.4万亿**\n如果考虑到这些公司的现金流和投资级债券市场容量，理论上限是1.4万亿。而且谷歌云和AWS的未完成订单从3580亿暴涨到8320亿，供需平衡最早要到2027年下半年。\n\n**3/ 钱不是问题**\n这些公司的净债务/EBITDA只有0.4倍，即使再增加9500亿债务，杠杆率依然低于1倍。虽然债券市场容量有限，但还有海外发债、项目融资、私募市场等多种渠道。\n\n**4/ AI应用落地还很早期**\nQ1财报季只有11%的公司量化了AI对生产力的具体影响，2%量化了对盈利的影响。软件股的估值从39倍跌到21倍再回到25倍，\n\n[... middle omitted ...]\n\nllion in capex (89% growth).  \nUpside to AI capex implies upside to earnings and share prices of AI infrastructure beneficiaries in the near term. Most of the price gains in the AI infrastruct\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R030",
    "title": "JPM：市场低估的不是出口增速，而是贸易结构对增长含义的根本改变",
    "digest": "[wechat_article.md]\n# JPM：市场低估的不是出口增速，而是贸易结构对增长含义的根本改变\n\n五月出口数据再次超预期，年增长率达到19.4%，远超市场共识的15%和JPM自己预测的12.1%。但这份JPM研报的核心判断，并非出口有多强劲，而是出口的增长模式正在发生一次被市场低估的质变——增长越来越窄、越来越依赖价格驱动、越来越与国内生产和就业脱钩。这意味着，仅仅盯着出口增速来判断经济走向，已经不够了。\n\n过去几年，市场习惯将出口增长等同于制造业景气，将贸易顺差扩大等同于对GDP的净贡献增加。但这份报告揭示了一个不那么直观的现实：出口增长的主要驱动力，已经从“量”转向了“价”，而且集中在极少数产品类别。当增长主要来自价格效应而非产量扩张时，它对上游生产、就业和资本开支的拉动效应，会显著弱化。\n\n更值得关注的是，这种结构变化发生在全球贸易政策环境高度不确定的背景下。美国正在将关税工具从IEEPA转向301和232条款，欧盟对华贸易立场也在持续硬化。这意味着，中国出口面临的风险已经从“需求端波动”转向了“政策端冲击”。对于产业决策者和投资者而言，理解这种变化，远比预测下个月出口数字更重要。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 五月出口超预期的真正推手不是需求，而是价格和产品组合\n\n五月出口环比增长3.1%，延续了四月6.7%的强劲势头。但更值得拆解的是增长来源。这份研报明确指出，出口增长主要集中在三个领域：存储芯片与模块、AI数据中心建设设备、以及新能源产品（电动汽车、太阳能、电池）。这三类产品合计贡献了约60%的出口增量。\n\n关键变化在于，半导体出口价格已经大幅上涨。存储芯片从2025年的“量增驱动”转变为了近几个月的“价增驱动”。“新三样”的价格也在企稳，同时伴随可观的量增。而其他出口产品的平均价格，在四月已经转为小幅正增长，\n\n[... middle omitted ...]\n\n起，持续追踪这些关键变量的演变，共同拆解贸易数据的真实含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月出口超预期，AI是最大推手\n\n出口超预期，AI撑场\n\n📌 5月出口同比+19.4%，高于市场预期的15%，连续第二个月超预期。\n📌 核心拉动：高科技产品（手机+19.4%、集成电路+15.2%、自动数据处理设备+11%），记忆芯片和AI数据中心设备价格上涨是重要支撑。\n📌 “新三样”（电动车、光伏、电池）量价齐升，合计贡献约60%的出口增量。\n📌 出口价格效应转正，4月以来平均出口价格由负转正，能源成本上升可能进一步推高价格。\n\n📌 进口连续6个月扩张，5月同比+27.5%，但更多是AI供应链补库和商品囤货驱动，而非国内需求全面回暖。\n📌 贸易顺差扩大至1054亿美元，1-5月累计顺差4530亿美元，略低于去年同期的4700亿美元。\n\n📌 出口增长越来越依赖价格驱动和产品集中度，对GDP和就业的贡献变得更不直接、更波动。\n📌 外部风险：美国301/232关税调查范围扩大、欧盟对华态度趋硬，政策冲击可能大于需求变化。\n📌 支撑因素：全球需求韧性+资本开支从AI向非科技领域扩散，有助于中国出口维持高个位数乃至双位数增长。\n\n📌 一个值得关注的趋势：今年进口增速可能自2021年以来首次超过出口，反映AI供应链和\n\n[... middle omitted ...]\n\nwnside skew from renewed US tariff uncertainties (a pivot to Sections 301/232) and a tougher EU stance against China.\n\nEchoing the upside surprise in FX reserves, China's May exports beat expe\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 09 Jun 2026 02:54 PM HKT\n\nDisseminated 09 Jun 2026 02:54 PM HKT"
  },
  {
    "id": "R031",
    "title": "Bernstein：半导体设备进口数据揭示的不仅是周期性复苏，更是结构性分化",
    "digest": "[wechat_article.md]\n# Bernstein：半导体设备进口数据揭示的不仅是周期性复苏，更是结构性分化\n\n当市场还在争论半导体周期何时见顶时，一份来自台湾海关的最新数据正在传递更为精细的信号。2026年5月，台湾半导体设备进口额同比增长23%，环比下降8%。这个数字本身并不令人意外——台积电的资本开支计划早已为市场所熟知。但真正值得关注的，不是总量的增长，而是增长的结构：光刻设备、测试设备、清洗设备正在经历截然不同的需求节奏，而这种分化正在重塑全球半导体设备供应商的竞争格局。\n\nBernstein的这份研报，通过对台湾半导体设备进口数据的拆解，揭示了一个关键判断：市场对日本和欧洲半导体设备公司的估值，尚未充分反映其在先进制程扩张中的差异化受益程度。简单来说，不是所有设备商都能从这轮资本开支周期中同等受益，而那些在测试、光刻等关键环节拥有不可替代性的公司，其定价权正在被低估。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 台湾进口数据是观察全球半导体设备需求的领先指标，其信号意义远超台湾本土\n\n台湾作为全球半导体制造的核心枢纽，其设备进口数据从来不只是反映本地需求。Bernstein的研报明确指出，这些数据对于覆盖日本和欧洲的设备公司具有“强相关性”。这背后的逻辑并不复杂：台积电的产能扩张直接决定了ASML、东京电子、爱德万测试等公司的订单节奏，而台湾海关每月公布的设备进口数据，本质上是对这些公司未来收入的提前映射。\n\n从总量看，5月台湾半导体设备进口额约为44亿美元，虽然环比下降8%，但同比仍保持23%的增长。更重要的是，三个月移动平均环比增长达到13%，表明增长的持续性并未被单月波动打断。这组数字支撑了Bernstein对日本和欧洲半导体设备板块的积极看法。\n\n但真正有洞察力的分析，不在于看总量，而在于看结构。Bernstein的研\n\n[... middle omitted ...]\n\n投资者一起讨论这些关键问题，欢迎来知识星球微信群里继续交流。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月台湾半导体设备进口：增速放缓但结构分化\n\n📊 设备进口增速放缓\n\n5月台湾半导体设备进口总额44亿美元，同比增长23%，但环比下降8%。从日本进口的设备环比下降17%，显示短期动能有所减弱。不过3个月移动平均仍保持10%的全球增速和6%的日本增速，趋势依然向上。\n\n🔍 各细分领域表现分化\n\n1️⃣ **测试设备：爱德万最受益**\n台湾测试设备进口环比增长7%，同比增长34%。投行研报通过回归模型测算，爱德万在台湾的季度收入可能环比增长6%，高于市场预期的3%。测试设备需求正在加速。\n\n2️⃣ **光刻设备：ASML订单强劲**\n5月光刻设备进口5.43亿欧元，环比下降38%但同比增长21%。4-5月合计环比增长约80%，主要受4月创纪录进口驱动。模型估算ASML在台湾的季度系统销售额约23.3亿欧元，环比增长61%，同比增长19%。\n\n3️⃣ **东京电子：短期承压**\n相关设备（CVD、刻蚀、清洗等）5月环比下降19%，模型建议台湾季度收入可能环比下降24%，低于市场预期的持平。短期面临调整压力。\n\n4️⃣ **清洗设备：Screen表现稳健**\n清洗设备进口环比增长11%，同比增长14%。模型估算Sc\n\n[... middle omitted ...]\n\nf8aa90e.jpg)\n\nJack Lin\n\n+852 2123 2683\n\njack.lin@bernsteinsg.com\n\nMOF Taiwan released May 2026 semiconductor equipment import data on June 10 $^{th}$ . We have extracted and analyzed relevant \n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R032",
    "title": "Citi：中国2万亿AI基建计划真正重塑的不是需求，而是国内供应链的定价权",
    "digest": "[wechat_article.md]\n# Citi：中国2万亿AI基建计划真正重塑的不是需求，而是国内供应链的定价权\n\n市场正在讨论一个巨大的数字：2万亿元人民币，五年，国家级数据中心网络。但这份Citi研报的核心判断，并非只是“需求会爆发”这么简单。它真正揭示的信号是：中国AI基础设施的竞争逻辑正在发生一次底层切换——从谁建得最快，转向谁能把国产化率80%的硬约束转化为结构性优势。\n\n国家发改委牵头的这一计划，要求至少80%的关键技术依赖国内供应商。这意味着，过去市场对AI产业链的估值模型，很大程度上基于全球供应链的假设，如今需要重写。Citi研报在6月9日发布后迅速引发关注，因为它提供了一个量化锚点：以每兆瓦约2亿元的综合成本计算，2万亿投资相当于新增约10GW的AI数据中心容量，年均2GW。而中国目前全部IDC装机容量估计约为20GW。换句话说，仅这一计划就将使AI级数据中心容量在现有基础上扩张约50%。\n\n这个数字本身已经足够震撼，但真正值得深入推敲的，是它如何重塑产业链上每一家公司的竞争地位。以下是我们从这份研报中提炼出的四个关键层次，以及一个尚未被充分讨论的问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 运营商从“管道工”升级为AI经济的基础设施运营商，其估值逻辑需要重构\n\n报告明确指出，根据媒体报道，国有电信运营商将运营这批互联数据中心的主体。这并非简单的“接单干活”，而是一次角色跃迁。\n\n过去十年，三大运营商在资本市场上的定位长期被简化为“流量管道”，估值受制于ARPU值增长乏力、资本开支周期和竞争性降价。但Citi研报暗示，当运营商成为国家级AI算力网络的核心运营方，他们的收入结构将从“卖连接”转向“卖算力+连接”。这不仅意味着单位收入的提升，更意味着商业模式的本质变化——从流量批发商升级为平台型基础设施服务商。\n\n这一转变的\n\n[... middle omitted ...]\n\n者一起跟踪这些公司的订单动态，欢迎来我们的微信群里继续讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n两万亿的AI基建计划，国内产业链怎么看？\n\n万亿AI基建，本土链受益\n\n某外资投行最新研报指出，中国计划未来五年投入约2万亿元，建设全国数据中心网络，且要求80%以上采用国产AI芯片。\n\n这轮投入有多大？研报算了笔账：按每兆瓦2亿元成本估算，相当于新增约10GW的AI数据中心容量，每年约2GW。对比当前国内IDC总容量约20GW，这相当于五年内把AI级容量再扩50%。\n\n1️⃣ 数据中心运营端\n虽然主要由国企运营商执行，但中立IDC厂商同样受益。需求加速的信号已经出现：GDS在1Q26创下约200MW的批发订单纪录，VNET同期签署了500MW+的新订单。\n\n2️⃣ 供应链国产化\n国产芯片80%的硬性要求，直接拉动本土AI服务器需求。IEIT、联想、中兴是核心受益方。光模块环节，国内龙头Accelink将受益于数据中心内外的光互联需求爆发。中软国际作为华为的IT服务和ISV伙伴，其算力服务市场空间也被打开。\n\n3️⃣ 运营商角色升级\n国企运营商将从传统连接服务商，转型为中国AI经济的基础设施运营方，地位进一步巩固。\n\n这轮基建周期，本质是“国产化+规模化”双轮驱动。研报未给出具体时间表，但订单数据已经先行。\n\n[... middle omitted ...]\n\nomentum with record 1Q26 wholesale bookings. We believe IEIT, Lenovo, ZTE (AI server demand), Accelink (domestic optics) and Chinasoft (Huawei proxy, computing power services) will benefit fro\n\n[... middle omitted ...]\n\nsult in prosecution. The information contained in the Product is intended solely for the recipient and may not be further distributed by the recipient to any third party.\n\nADDITIONAL INFORMATION IS AVAILABLE UPON REQUEST"
  },
  {
    "id": "R033",
    "title": "GS：市场对香港银行跨境监管风险的担忧，可能被放大了十倍",
    "digest": "[wechat_article.md]\n# GS：市场对香港银行跨境监管风险的担忧，可能被放大了十倍\n\n自5月21日以来，HSBC控股和渣打银行的股价分别跑输欧洲银行板块指数5%和7%。在一个充斥着政策信号的月份里，这种下跌看起来顺理成章——中国证监会宣布对线上券商加强监管，香港金管局收紧开户流程，国务院发布了关于跨境投资的新规。投资者的直觉反应是：内地资金流入香港的通道正在收窄，依赖这些流量的银行将面临盈利压力。\n\n但GS最新发布的这份报告提出了一个反直觉的判断：**市场担忧的方向是对的，但对程度的估计可能错了。** 即便在最极端的假设下——来自中国内地的净新资金完全归零——对HSBC和渣打税前利润的影响也仅为约1%和2%。这个数字与股价5%至7%的跌幅之间，存在一个明显的缺口。\n\n这个缺口意味着什么？是市场过度反应，还是报告遗漏了某些更隐蔽的风险？GS的分析框架值得仔细拆解。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 政策组合拳的真正落点不在银行，而在技术跨境流动\n\n5月22日，中国证监会宣布了对线上券商的监管措施及相关罚款。同日，香港金管局发布通函，旨在加强开户程序和合规要求。6月1日，中国国务院发布了一项关于规范跨境投资的条例。\n\n这组政策在时间上的密集出台，很容易被解读为对跨境资本流动的系统性收紧。但GS的经济学家提供了一个不同的视角：**这些政策的核心关切是技术跨境转移的管理，而非限制资本外流。**\n\n具体而言，国务院的条例重点在于建立规范跨境技术转让的框架，支持中国企业走出去，并管理与海外业务和资产相关的地缘政治风险。条例中唯一与银行直接相关的条款是第33条，该条款规定“境外金融市场投资应遵守本条例，具体规则另行制定”。\n\n关键短语是“另行制定”。这意味着，截至目前，针对银行跨境业务的实质性新规则尚未出台。GS坦承，他们尚无法预判这些\n\n[... middle omitted ...]\n\n群里继续展开，欢迎来一起拆解这份报告的完整逻辑链和隐含假设。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n香港存款新规，对银行影响有多大？\n\n香港存款监管收紧，实际影响有限\n\n最近香港存款和跨境投资的新规引发不少讨论。投行研报拆解了实际影响，发现市场可能有点过度反应了。\n\n**1/ 新规到底说了什么？**\n5月22日，证监会宣布加强对线上券商的监管，金管局也发文要求强化开户流程和合规要求，包括清理零余额账户、核实资金来源。渣打CFO在会议上表示，这些方向与现有政策一致，只是多了几个动作项。系统升级已经完成，开户服务正常进行。\n\n6月1日，国务院发布跨境投资管理新规，核心是监管跨境技术转让，支持企业出海，管理地缘风险。其中第33条提到境外金融市场投资需遵循规定，具体细则待定。\n\n**2/ 对存款的影响有多大？**\n关键数据来了：对于在香港开户的内地居民，约90%的存款来自境外（如新加坡、香港本地），仅约10%来自内地账户。2025年，HSBC净新增资金约860亿美元，渣打约520亿美元。\n\n假设未来内地来源的10%净新增资金完全停止，对HSBC/渣打的影响：\n- 每100bp息差，影响税前利润0.3%/0.7%\n- 即使按300bp息差（目前HIBOR 2.7%），也仅影响税前利润约1%/2%\n\n**3/ 保险和投\n\n[... middle omitted ...]\n\nwe take no view on the final outcome of recently announced regulations and await further details — as a sensitivity, even in a scenario where Group net new money were to slow down by 10% (as a\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R034",
    "title": "DB：中国车市正在经历的，不是周期波动，而是竞争结构的根本性重构",
    "digest": "[wechat_article.md]\n# DB：中国车市正在经历的，不是周期波动，而是竞争结构的根本性重构\n\n五月的数据看起来有些矛盾。乘用车批发总量同比下降4.9%，但新能源车（NEV）批发量却逆势增长12%，渗透率首次突破60%大关。市场似乎同时在经历“总量收缩”和“结构加速”两个方向。\n\nDB最新发布的这份月度批发量图册，提供了理解这一矛盾最直接的切口。它没有长篇大论地分析宏观政策或消费者信心，而是用一组清晰的数据，揭示了一个正在发生的底层变化：中国乘用车市场的竞争，已经从“谁能造出电动车”进入了“谁能把规模优势转化为定价权和成本护城河”的阶段。\n\n这份报告最值得关注的判断，不是五月销量好坏，而是渗透率突破60%这个数字背后所代表的竞争格局质变。当新能源车成为绝对主流，市场的游戏规则正在被重新定义——赢家通吃的逻辑更加明显，而落后者的生存空间正在被快速压缩。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 新能源渗透率突破60%不是终点，而是竞争烈度升级的起点\n\n五月新能源渗透率达到60.9%，环比提升3个百分点，同比提升超过9个百分点。这个数字的意义，远不止于市场份额的里程碑。它意味着，在当前的月度销售中，传统燃油车已经退居次位，新能源车正式成为市场的主流选择。\n\n从更长的时间线来看，这一趋势的斜率值得重视。2025年初，渗透率还在42%左右，到年中攀升至50%以上，并在2025年下半年稳定在52%-56%的区间。进入2026年，渗透率在经历了一季度季节性回落后，在四月和五月快速拉升，从48%跳升至61%。这种加速态势，通常不是由单一产品周期驱动的，而是反映了消费者认知、基础设施、以及产品性价比三者之间的正向循环已经形成。\n\n对于产业决策者而言，这个数字的含义是清晰的：市场不再需要讨论“是否要电动化”，而是必须回答“在电动化已成定局的竞争环境下\n\n[... middle omitted ...]\n\n显性化，以及投资者应该如何构建自己的观察框架。期待你的加入。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月车市：新能源渗透率突破60%\n\n封面：5月车市关键指标\n\n副标题：新能源渗透率创历史新高\n\n---\n\n5月中国乘用车批发数据出炉，有几个值得关注的信号。\n\n**1/ 整体市场：总量微降，结构变化明显**\n- 5月乘用车批发221.2万辆，同比-4.9%，但环比+4.9%\n- 前5月累计1019万辆，同比-6%，说明需求仍在恢复中\n\n**2/ 新能源：渗透率突破60%大关！**\n- 5月新能源车批发134.7万辆，同比+12%，环比+10.3%\n- 渗透率高达60.9%，比4月再提升3个百分点\n- 前5月累计渗透率51.9%，今年过半时间都在50%以上\n\n**3/ 几家车企的亮点**\n- **比亚迪**：5月38.3万辆，环比+19.4%，市占率回到17%\n- **蔚来**：同比+62.3%，环比+28.4%，增速非常亮眼\n- **零跑**：同比+81%，环比+14.3%，市占率从1.6%攀升至3.7%\n- **特斯拉中国**：同比+39.4%，市占率稳定在3.9%\n\n**4/ 几家略显疲态的车企**\n- **长安**：同比-28.4%，前5月累计-21.7%\n- **华晨宝马**：同比-31.7%，豪华品\n\n[... middle omitted ...]\n\n-4.9%</td><td>4.9%</td><td>10,189,897</td><td>-6.0%</td></tr><tr><td>Total NEV</td><td>Industry</td><td>1,347,490</td><td>12.0%</td><td>10.3%</td><td>5,290,677</td><td>2.2%</td></tr><tr><td>NE\n\n[... middle omitted ...]\n\nk, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R035",
    "title": "DB：中国新能源车市最值得关注的不是总量，而是订单结构的剧烈分化",
    "digest": "[wechat_article.md]\n# DB：中国新能源车市最值得关注的不是总量，而是订单结构的剧烈分化\n\n6月第一周的新能源车订单数据，看似平淡，实则暗流涌动。\n\nDB最新发布的周度订单追踪显示，6月首周（W23）主要新能源车企合计订单环比下滑约5%，同比更是下降了约15%。如果只看这个数字，很容易得出“需求疲软”的结论。但这份报告的价值，恰恰在于它揭示了总量数字之下，各家车企正在经历的截然不同的命运。\n\n真正重要的判断是：中国新能源车市场的竞争，已经从“谁能卖得更多”进入了“谁的订单结构更健康”的阶段。市场目前定价的核心变量，并非整体需求是否复苏，而是企业能否在订单波动中证明自己的定价能力和品牌黏性。\n\n为什么这个时间点重要？因为5月刚经历了一轮由新车型发布和促销活动驱动的订单脉冲，6月首周的回落，恰好是检验哪些品牌拥有真实需求、哪些只是靠一次性刺激撑起数据的试金石。\n\n以下，我们从这份研报的订单数据中，提炼出五个关键判断。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 比亚迪的订单滑坡，暴露了规模领先者的结构性隐患\n\n6月首周，比亚迪订单量为4.77万辆，环比下滑2%，同比骤降36%。这是所有主要车企中同比降幅最大的。更值得警惕的是，这一数字不仅远低于去年同期的7.5万辆，也低于今年5月最后一周的4.87万辆。\n\n表面上看，这是高基数效应——去年6月正值比亚迪多款冠军版车型密集上市。但问题不止于此。从更长的时间序列看，比亚迪的周度订单自3月第4周达到8.5万辆的峰值后，便进入了下行通道。尽管4月第1周仍维持在6.5万辆，但此后多数时间徘徊在4.5-5.5万辆区间。\n\n这意味着什么？比亚迪的订单中枢正在下移。市场此前对比亚迪的定价，很大程度上基于其“规模效应持续放大”的叙事。但如果订单量无法维持在高位，规模效应的边际贡献就会递减，而固定成本分摊\n\n[... middle omitted ...]\n\n续讨论。我们会基于这份研报的原始数据，做更细致的拆解和推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n6月第一周，新能源车订单有点凉\n\n订单降温，但分化加剧\n\n6月第一周的新能源车订单数据出来了，整体感觉是：不像5月那么热，但结构很有意思。\n\n1️⃣ 比亚迪周订单47.7k，同比下滑36%，环比微降2%。研报显示这是连续第二周环比偏弱，和去年6月的高基数有关。\n\n2️⃣ 蔚来集团本周28k，同比暴增419%，但环比下滑28%。5月最后一周冲量太猛（39k），6月初回调属于正常节奏。\n\n3️⃣ 理想汽车仅6.7k，同比-25%，环比-24%。这是目前新势力里比较疲软的一家，连续几周订单量都在低位徘徊。\n\n4️⃣ 小米汽车7.4k，同比+48%，环比-14%。从3月那波爆发后（单周36k），现在回归到每周7-10k的稳定区间。\n\n5️⃣ 小鹏9.5k，同比-16%，环比-14%。5月最后一周冲到29k后快速回落，说明促销效应消退很快。\n\n6️⃣ 特斯拉14.2k，同比+18%，环比+1%。稳如老狗，每周都在14k左右波动，没什么惊喜也没惊吓。\n\n🔍 一个有意思的点：HIMA（问界）本周24.2k，同比+112%，但环比骤降41%。5月最后一周冲到40.7k后回落，可能和5月底集中交付有关。\n\n整体来看，6月开局偏\n\n[... middle omitted ...]\n\n/td></tr><tr><td colspan=\"2\">Calendar days</td><td>1-7D</td><td>25-31D</td><td>2-8D</td><td></td><td></td></tr><tr><td colspan=\"7\">Weekly New Orders of key OEMs</td></tr><tr><td>1211 HK</td><t\n\n[... middle omitted ...]\n\nk, NY 10019</td><td>Tower,</td><td></td></tr><tr><td>Tel: (44) 20 7545 8000</td><td>Tel: (1) 212 250 2500</td><td>Singapore 048583</td><td></td></tr><tr><td></td><td></td><td>Tel: +65 6423 8001</td><td></td></tr></table>"
  },
  {
    "id": "R036",
    "title": "GS：中国医疗设备招标的拐点正在到来，但真正的分化才刚刚开始",
    "digest": "[wechat_article.md]\n# GS：中国医疗设备招标的拐点正在到来，但真正的分化才刚刚开始\n\n2026年5月的数据，让关注中国医疗设备行业的人稍微松了一口气。GS最新发布的招标跟踪数据显示，在经历了连续五个月的同比下滑之后，九大类医疗设备的总招标金额在5月录得了0.1%的同比正增长。这个数字不大，甚至可以说刚刚转正，但它所承载的信号意义，远比数字本身重要。\n\n这份报告的真正价值，不在于告诉你“5月数据转正了”，而在于它揭示了一个正在发生的结构性变化：中国医疗设备市场正在从“总量承压”转向“结构分化”。那些能在招标总量恢复的过程中，同时实现份额提升和海外扩张的公司，将获得远超行业平均的增长弹性。而那些仅仅依赖国内招标总量回暖的企业，可能会在接下来的竞争中感受到更大的压力。\n\n为什么这个时间点值得关注？因为2026年5月的转正，是在2025年同期已经处于相对高基数的基础上实现的。GS的报告明确指出，这一变化符合其此前“行业将从温和同比下降转向温和同比增长”的预期，并且预计更为明显的复苏将在2026年下半年出现。这意味着，市场的底部可能已经确认，但接下来的上行路径，不会是普涨。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 招标总量转正背后的三个关键信号：不是所有品类都在好转\n\n5月的数据表面上是总量层面的好消息，但拆开来看，结构性的分化才是核心。在九大类设备中，只有CT、MRI和直线加速器（LINAC）实现了同比正增长。这三类设备有一个共同特征：它们都属于大型、高单价、采购决策周期较长的设备。它们的恢复，可能意味着医院端对于大型资本开支的态度正在从“极度谨慎”转向“有条件放开”。\n\n与之形成对比的是，此前连续保持正增长的患者监护仪，在5月未能延续强势。这看似是一个负面信号，但GS在报告中给出了一个值得深思的观察：疫情期间大量采购的监护仪，现在\n\n[... middle omitted ...]\n\n整。这些讨论，往往比单篇报告本身更能帮助理解市场的真实变化。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n医院设备招标回暖，拐点信号出现\n\n🏥 设备招标数据终于转正了\n\n某外资投行最新研报跟踪了9类医疗设备招标数据，5月总招标金额同比微增+0.1%，结束了连续5个月的同比下滑。虽然幅度不大，但这是从“小幅下滑”到“小幅增长”的切换信号。\n\n**关键看点：**\n1️⃣ 5月仅CT、MRI、直线加速器实现正增长\n2️⃣ 之前一直坚挺的监护仪5月转弱（-23%），但研报认为疫情期间采购的设备已进入替换周期，后续有改善空间\n3️⃣ 整体判断：下半年有望看到更明显的行业复苏\n\n**两家龙头公司对比：**\n\n🔸 联影医疗：前5个月招标金额同比+9%，是主要竞争对手中唯一正增长的。CT/MRI市占率稳定，DSA和直线加速器还在抢份额。公司新股权激励要求2026-28年每年营收增长超20%，目前研报预测2026年增长19.3%，略低于公司指引。\n\n🔸 迈瑞医疗：1季度国内营收同比-11%，海外+16%（美元计+20%）。PMLS和医学影像还在去库存（预计2季度结束），IVD有改善迹象——凝血和免疫业务均增长约10%。核心IVD业务市占率从1H25的10%提升到1Q26的13%。\n\n**一句话总结：最差的时候可能已经过去，但全面复\n\n[... middle omitted ...]\n\ny, only CT, MRI, and LINAC recorded positive yoy growth in May. Patient monitors, which had previously sustained positive growth, failed to maintain their strong momentum. However, considering\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R037",
    "title": "HSBC：储能正在成为全球能源政策的新重心，光伏反而面临需求拐点",
    "digest": "[wechat_article.md]\n# HSBC：储能正在成为全球能源政策的新重心，光伏反而面临需求拐点\n\n2026年6月初的上海SNEC光伏展，传递出的信号并不像展馆内的热闹那样均衡。HSBC在其最新SNEC观展报告中给出了一个层次分明的判断：地面光伏正面临中国市场化定价改革带来的需求转弱，而储能——尤其是户用储能——正在成为全球能源政策切换的新重心。这一判断并非简单的“光伏不行了、储能行了”的二元叙事，而是建立在各国电网消纳瓶颈、政策补贴结构变化以及技术渗透阶段差异之上的结构性推演。\n\n对于关注中国新能源产业链的投资者而言，这份报告的核心价值不在于复述展会上的产品陈列，而在于它揭示了一个正在发生的政策优先级转移：全球范围内，从“鼓励光伏装机”到“强制配套储能”的过渡，正在从早期市场向更多国家蔓延。这意味着，储能赛道的选股逻辑，需要从“跟着光伏走”切换到“独立于光伏、甚至受益于光伏瓶颈”的新框架。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 地面光伏正在经历的需求拐点，比市场预期的更结构化\n\nHSBC在报告中明确指出了地面光伏面临的两个压力源。第一个是中国的政策切换：2025年6月，中国从固定上网电价转向市场化定价机制。这一变化的影响在一年后的SNEC上已经可以感知——参展商对地面项目需求的预期明显趋于谨慎。第二个压力来自竞争格局的恶化：非传统玩家如京东方和阳光电源都在SNEC上展示了光伏组件产品。这意味着组件环节的竞争正在从传统光伏制造商之间的“内卷”，升级为跨界巨头的“降维打击”。\n\n这两点叠加在一起，指向一个结论：地面光伏的利润率压缩可能不是周期性的，而是结构性的。市场化定价意味着电站开发商不再享有稳定的电价保证，回报率的不确定性会抑制新项目开工；而跨界玩家的进入，则意味着即便需求恢复，价格竞争也难以缓解。\n\n对于投资者而言，这意味着光伏\n\n[... middle omitted ...]\n\n进一步解读，帮助大家把这份研报的洞察转化为可操作的观察框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nSNEC 2026：储能火热，光伏遇冷\n\n📊 储能强，光伏弱\n\n刚从上海SNEC回来，跟几家头部企业的销售和管理团队聊了一圈，感受很直接：储能（特别是户用储能）的生意氛围很强，而光伏这边需求偏弱。\n\n**1/ 户用储能：出口数据很亮眼**\n- 中国锂电池出口前十大市场，今年前4个月同比增长29%\n- 澳大利亚增长最猛，1.9倍，背后是Cheaper Battery Program补贴\n- 英国Warm Home Plan（150亿英镑）预计年底生效，利好还在后头\n\n**2/ 光伏：两个压力点**\n- 中国6月刚切换到市场化定价，2026年需求预期偏弱\n- 新玩家涌入竞争：京东方、阳光电源都展出了组件产品，行业越来越卷\n\n**3/ 大储：欧盟出了个限制**\n- 4月22日欧盟禁止用中国逆变器的项目拿欧盟资金\n- 预计影响欧洲约20%的公用事业级光伏+储能市场\n- 工商业（C&I）影响相对小，约5%\n\n**4/ 太空光伏：没那么快**\n- 多家公司展示了太空级钙钛矿产品\n- 但可靠性验证需要时间，地面应用（BIPV、智能门锁、便携电子）反而更快\n- 钙钛矿比硅基轻，弱光下发电多10-18%\n\n**5/ 固态变压器\n\n[... middle omitted ...]\n\nst Applied Material (603806 CH), Eve Energy (300014 CH), S.C New Energy Technology (300724 CH), Laplace Renewable Energy Tech (688726 CH), and Shanghai Geoharbour (605598 CH), and talked to th\n\n[... middle omitted ...]\n\ntored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of HSBC Qianhai Securities Limited.\n\n[1280769]"
  },
  {
    "id": "R038",
    "title": "HSBC：SNEC 2026揭示的真正信号，不是光伏回暖，而是能源系统的权力交接",
    "digest": "[wechat_article.md]\n# HSBC：SNEC 2026揭示的真正信号，不是光伏回暖，而是能源系统的权力交接\n\n每年SNEC都是中国光伏行业的一次集体亮相，但今年的信号与往年截然不同。HSBC分析师团队在2026年6月初实地走访上海SNEC后，给出的核心判断并非关于组件价格何时触底，也不是产能出清到了哪个阶段——而是整个行业的叙事重心正在发生一次根本性转移：光伏不再只是发电源，而正在成为AI算力基础设施的底层能源架构。\n\n这份报告的价值不在于告诉读者“行业还在调整”，而在于它捕捉到了一个正在发生的结构性变化：当传统光伏供应链的展台人流稀疏、讨论沉闷时，固态变压器、AI数据中心供电一体化方案、以及住宅储能软件的智能化，正在成为新的流量中心。HSBC的观察暗示，投资者真正需要关注的不再是组件出货量或电池效率突破，而是“谁能把光伏从发电设备重新定义为算力能源接口”。\n\n这并非一个遥远的愿景。报告指出，在SNEC现场，“绿色电力驱动AIDC”已经成为大量展台的核心叙事，从渲染图到参考架构再到实物演示，生态系统的参与度远高于一年前。而固态变压器（SST）作为连接光伏直流发电与数据中心配电的关键环节，正在成为多个企业竞相布局的焦点。\n\n以下是我们基于HSBC这份实地调研报告提炼出的五个核心洞察，以及一个尚未被充分回答的关键问题。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 光伏供应链的“冷静”并非坏事，它意味着资本正在从制造端向应用端迁移\n\nHSBC团队的直观感受是，与储能和AIDC主题的火爆相比，传统光伏供应链展区“明显更安静”。这不是一个孤立的观察。当组件价格仍在RMB0.69-0.75/W的主流区间承压，分布式和海外市场能清到RMB0.85-1.00/W，而更低价的订单更多集中在年初时，整个制造环节的定价权正在被持续压缩。\n\n但“安静”不等\n\n[... middle omitted ...]\n\n完整呈现，但在持续的深度讨论中，往往能形成更清晰的判断框架。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nSNEC 2026 光伏展：储能与AI是主角\n\n**展会见闻**\n\n刚从SNEC回来，信息量很大。今年展会的热度明显分化，储能和AI数据中心电源是绝对主角，传统光伏供应链相对安静。\n\n**1. 储能：最亮的增长故事**\n- 工商业储能是增长最快的细分，项目管道稳定性在改善\n- 大型储能竞争激烈，价格战压力大，部分厂商转向海外或利基市场\n- 利润保护的关键：定价纪律 + 电池成本传导能力\n\n**2. AI数据中心电源：下一个战场**\n- \"绿色电力供AI数据中心\"是展会核心主题\n- 固态变压器（SST）成为焦点，多家厂商在开发相关方案\n- 但部署节奏偏慢，需要验证全生命周期经济性和效率\n\n**3. 户用储能：硬件同质化，竞争转向渠道与软件**\n- 展位人流量最高之一，但硬件差异化在缩小\n- AI能源管理已成标配（电价套利、智能调度、虚拟电厂参与）\n- 一体化系统（all-in-one）正在普及，简化安装和用户体验\n\n**4. 传统光伏供应链：偏冷**\n- 价格仍承压：主流大型项目约0.69-0.75元/W，分布式/海外约0.85-1.00元/W\n- 成本传导不完美：退税调整部分传导，银价上涨更难转嫁\n- 焦点是\n\n[... middle omitted ...]\n\nrelated segments. Below are our key takeaways:\n\n$\\diamond$ Space solar: Still niche at SNEC, but positioned as 'flagship' by exhibitors. Solar-cell technology is shifting beyond GaAs towards s\n\n[... middle omitted ...]\n\nystem, or transmitted, on any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of The Hongkong and Shanghai Banking Corporation Limited.\n\n[1280815]"
  },
  {
    "id": "R039",
    "title": "JPM：中国家电的估值逻辑正在从“周期股”转向“复合增长引擎”",
    "digest": "[wechat_article.md]\n# JPM：中国家电的估值逻辑正在从“周期股”转向“复合增长引擎”\n\n市场对家电板块的定价，可能还停留在旧世界里。10倍市盈率、6%的股息率、约20%的净资产收益率，这是当前市场给中国家电三巨头——美的、海尔、格力——的集体定价。这个定价隐含的假设是：这些公司本质上是国内耐用消费品周期股，补贴退坡后需求放缓，利润承压，估值没有扩张空间。\n\nJPM最新发布的家电行业深度报告提出了一个根本性的问题：如果中国家电不再应该被当作一个国内家电周期来估值，而是作为“现金牛盈利 + 全球挑战者增长 + 工业科技期权价值”的组合，那会怎样？\n\n这个问题的答案，决定了当前估值体系是否正在酝酿一次系统性重估。报告的核心判断是：市场低估的不是短期需求，而是供给侧的再定价——即龙头企业能否将中国市场的现金流，转化为全球份额扩张和B2B能力建设。而在这条逻辑线上，美的集团被选为最清晰的标的。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 国内B2C不再是增长引擎，但它是整个故事的现金基础\n\n国内家电市场正在成熟，这是共识。补贴政策退坡后，2026年国内零售需求可能出现中个位数的下滑。JPM预计，二季度将是利润率压力测试的关键窗口：需求走弱已充分预期，但石化产品驱动的成本上升将真正考验龙头企业的定价能力和成本传导能力。基准情景下，三巨头在2026年二、三季度的毛利率将温和收缩0.5至1个百分点。\n\n但这里的关键判断不是“利润会不会跌”，而是“龙头企业能否守住利润池”。报告指出，三巨头在国内市场合计控制了约60%的份额，核心利润池相对稳固。如果它们能在二、三季度再次证明毛利率的相对稳定，“成熟品类叠加利润率压缩”的熊市叙事就会失去说服力。\n\n这意味着，国内B2C业务的角色正在转变：它不再是增长的主要驱动力，而是变成了一个高现金回报的“燃料箱”\n\n[... middle omitted ...]\n\n继续讨论，我们将基于完整报告的数据和图表，进行更细致的推演。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n家电龙头，不止是卖空调\n\n**重新定义家电股的估值逻辑**\n\n家电板块还在按“补贴周期+地产周期”给估值吗？某外资投行最新研报提出了一个值得认真思考的问题——\n\n**中国白电三巨头，可能正在从“卖空调冰箱”变成“全球工业科技公司”。**\n\n1️⃣ **国内是现金牛，不是增长引擎**\n\n国内家电市场已进入成熟期，三巨头合计市占率约60%。补贴退坡后销量会承压，但研报认为关键不是增速，而是——龙头企业能否守住利润率，把国内赚到的现金，投到海外和B2B。\n\n⚠️ 2Q26是利润率压力测试：量价承压+石化成本上涨。如果三巨头能稳住毛利率，那“成熟品类+利润率压缩”的悲观逻辑就站不住脚。\n\n2️⃣ **海外才是真正的增长故事**\n\n三巨头国内市占率60%，海外只有16%。而海外可触达市场是国内的3倍。\n\n研报预计：美的/海尔/格力2026-28年海外收入CAGR分别达+11%/+9%/+7%。关键不是出口量，而是自主品牌（OBM）的渠道掌控和品牌溢价。\n\n3️⃣ **B2B是估值提升的钥匙**\n\n商用暖通空调、数据中心液冷、欧洲热泵——这些不是传统家电，但恰好是白电龙头的强项：热管理、供应链、制造规模、成本控制。\n\n全\n\n[... middle omitted ...]\n\nl priced for the old world: 10x P/E, 6% div. yield and \\~20% ROE (2027E), with heavy skepticism around the 2026–27 domestic slowdown. We agree China demand will soften, but that is unlikely to\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 09 Jun 2026 11:40 PM HKT\n\nDisseminated 09 Jun 2026 11:43 PM HKT"
  },
  {
    "id": "R040",
    "title": "JPM：零售投资者在科技股上的踩踏式抛售，暴露的不仅是情绪，更是仓位结构的脆弱性",
    "digest": "[wechat_article.md]\n# JPM：零售投资者在科技股上的踩踏式抛售，暴露的不仅是情绪，更是仓位结构的脆弱性\n\n这份发布于6月10日的JPMRetail Radar周报，捕捉到了一个关键信号：散户资金流在一周之内从极端买入科技股转向了创纪录的卖出。这并非普通的获利了结，而是一次由业绩回撤触发的、非选择性的仓位出清。\n\n对于产业决策者和高净值投资者而言，真正值得关注的不是散户的情绪波动本身，而是这种极端行为背后所反映的市场结构——当最坚定的趋势追随者开始无差别地削减仓位时，此前由AI叙事驱动的拥挤交易正在经历一次真正的压力测试。报告的数据表明，市场正在经历的，可能不是简单的风格切换，而是对过去一年半“买科技、买AI”这一核心叙事的重新定价。\n\n在这份报告中，JPM策略团队不仅记录了资金流向的剧变，还揭示了几个容易被忽视的结构性特征：散户的抛售并非为抄底其他板块筹集资金，而是纯粹的亏损止损；石油相关资产的仓位正在悄然累积；世界杯主题的交易热情尚未被点燃。这些信息为理解当前市场的底层逻辑提供了新的维度。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 散户的抛售不是“换仓”，而是“断腕”——这意味着风险偏好的系统性下降\n\n报告中最引人注目的数据点是：在截至6月10日的一周内，零售投资者的美元净流入降至一年多以来的最低水平。ETF和个股的流入百分位分别仅为2.8%和0.8%。更关键的是，上周五创下了过去一年中最大的单日散户卖出记录。\n\n这种行为模式与传统意义上的“获利了结”或“板块轮动”有本质区别。报告明确指出，散户卖出活动“主要是由业绩驱动的”——他们的投资组合遭受了回撤，尽管这些回撤尚未显著侵蚀此前积累的超额收益。换句话说，散户是在“砍仓”，而不是在“调仓”。\n\n这意味着什么？当散户投资者开始因为浮亏而被迫卖出，而不是因为看到更好的机会而主动\n\n[... middle omitted ...]\n\n更完整的研报解读、原始图表，以及围绕这些数据展开的实时讨论。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n散户这周在疯狂卖科技\n\n散户大撤退\n\n上周还在狂买，这周就创纪录卖出\n\n---\n\n这周散户资金流上演大反转：\n\n上周还在疯狂买科技，这周直接创纪录卖出。整体资金净流入仅17亿美元，远低于周均66亿，是过去一年最低水平之一。\n\n**1/ 科技ETF遭遇史上最大抛售**\n\nETF层面，科技ETF净流出创历史纪录（-3.7z）。上周还买爆了（+3.1z），这周全卖光。SOXL、IGV、SMH、EWY（韩国ETF）是重灾区。\n\n**2/ 个股：砍科技，买消费**\n\n散户砍仓集中在“科技非Mag 7”板块，MU（-3.2z）、MRVL（-6.9z）、AMD（-3.0z）、ARM（-7.0z）、DELL（-4.0z）是卖出最多的。同时买入消费必需品。没有出现广泛的“抄底”行为。\n\n**3/ Mag 7内部也分化**\n\nTSLA（+7.13亿）、NVDA（+5.83亿）、GOOGL（+2.05亿）继续被买入，但AAPL（-1.78亿）、MSFT（-1100万）、AMZN（-4300万）被卖出。\n\n**4/ 原油主题持续升温**\n\n随着美国对伊朗发动新一轮打击，散户在USO和BNO的持仓稳步增加。世界杯周四开幕，但散户目前还\n\n[... middle omitted ...]\n\nsideration.\n\n## Retail Trading Activity Overview\n\n- Over the past week, retail investor flows have swung from one extreme to another —from outsized Tech buying last week to record-selling the \n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 11 Jun 2026 02:45 AM EDT\n\nDisseminated 11 Jun 2026 02:45 AM EDT"
  },
  {
    "id": "R041",
    "title": "JEF：泡泡玛特的韧性来自股东结构变化，而非基本面改善",
    "digest": "[wechat_article.md]\n# JEF：泡泡玛特的韧性来自股东结构变化，而非基本面改善\n\n这份JEF最新发布的IP玩具月度追踪报告，表面上是一份常规的数据更新，但如果我们用金字塔原理来拆解，会发现一个被市场情绪掩盖的核心判断：泡泡玛特股价在1Q26业绩发布后的韧性，更多来自股东结构的结构性变化，而非运营基本面的加速改善。段永平在5月底购入约6%股份成为重要股东，这一事件对市场信心的支撑力度，可能超过了公司自身业绩所能提供的边际增量。\n\n报告发布时点恰逢市场对泡泡玛特海外增长动能是否可持续产生分歧。4月电商GMV同比增长70%、环比增长25%的数据，以及Labubu二手价格环比企稳的信号，确实为多头提供了弹药。但与此同时，报告也坦率指出：公司App活跃用户数在5月出现下滑，全球及区域Google搜索趋势继续走弱，Instagram粉丝增速也在放缓。这些信号组合在一起，指向一个更复杂的图景——短期催化剂（Labubu 4.0发布、世界杯相关营销）能否转化为可持续的增长，仍需验证。\n\n这份报告的价值不在于罗列数据，而在于它揭示了一个关键张力：市场正在用股东结构变化来定价，而非用运营数据的边际变化来定价。这种定价逻辑的切换，对投资者的观察框架提出了新要求。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 段永平入股是股价韧性的主要支撑，而非基本面拐点\n\n报告开篇就给出了一个清晰的判断：在5月13日1Q26业绩发布后，泡泡玛特股价保持了韧性，但JEF并未看到基本面有任何实质性变化。真正改变市场情绪的事件，是段永平在5月25日至28日期间购入8100万股，约占公司总股本的6%，使其成为重要股东。\n\n这一判断的关键在于时间序列的对照。业绩发布到段永平入股之间有两个星期的窗口期，如果市场对业绩本身有强烈正面反应，股价韧性应该在这两周内就已经建立。但报告暗示，\n\n[... middle omitted ...]\n\n享对IP玩具行业、消费品牌以及相关上市公司的最新研究和思考。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n泡泡玛特五月跟踪：热度没降，但风向在变\n\n📊潮玩五月观察\n\nLabubu二手价环比稳住，但二手交易盘面变了。Top30热门款里，非泡泡玛特产品占了3个，而泡泡玛特×aespa联名款依然是二手市场最想要的单品。\n\n电商这块，四月数据已出：泡泡玛特电商GMV同比+70%，环比+25%。Bloks同比+16%，名创优品同比+11%。五月数据要等6月15日后更新。\n\n海外社交热度有点分化：\n1️⃣ TikTok互动回暖——全球账号+49%月环比，泰国账号+67%月环比\n2️⃣ Instagram粉丝增长放缓——五月新增1.3万，四月是1.9万\n3️⃣ 但全球和美国地区的App活跃用户都下降了，Google搜索趋势也在持续走低\n\n产品端有几个看点：\n🔹 Labubu 4.0即将发布，是下一波催化剂\n🔹 世界杯营销已启动——泡泡玛特出现在FIFA 2026官方歌曲MV里，还和可口可乐联名推出Labubu罐装饮料\n🔹 Bloks五月发新13个系列，IP更分散，重点押注星球大战，还预告了《玩具总动员5》联名产品（电影6月底上映）\n\n股东层面：段永平5月底买入8100万股（约6%），成为重要股东，但这更多是信心信号，研报认为基\n\n[... middle omitted ...]\n\nthem are non-Pop Mart products, while the Pop Mart x aespa collaboration remains most wanted.  \n- Ecommerce sales: Meritco has not released May data yet; Apr data shows Pop Mart's GMV on ecomm\n\n[... middle omitted ...]\n\nd\\_iapd\\_Brochure.aspx?BRCHR\\_VRSN\\_ID=483878 and https://adviserinfo.sec.gov/Firm/292142 or visit our website at https://javatar.bluematrix.com/sellside/Disclosures.action, or www.JEF.com, or call 1.888.JEF.\n\n© 2026 JEF"
  },
  {
    "id": "R042",
    "title": "摩根斯坦利：市场真正低估的不是需求，而是供给纪律的长期重塑",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：市场真正低估的不是需求，而是供给纪律的长期重塑\n\n过去两个月，DRAM股票涨幅高达70%至134%，随后经历了一轮剧烈回调。市场主流叙事将这轮波动归结为“周期见顶的信号”——历史经验表明，当存储周期进入第六个季度，供给松动、价格增速放缓，股票往往提前四个月见顶。但摩根斯坦利在这份最新研报中提出了一个反直觉的核心判断：**这轮回调不是周期的终结，而是周期得以延续的必要重置。**\n\n真正值得关注的，不是需求是否持续——AI带来的结构性需求已经是共识——而是供给端正在发生的历史性变化。过去四十年的存储周期，每一次崩溃的根源都不是需求不足，而是供给纪律从未真正建立。这一次，长期供应协议（LTA）正在改变游戏规则。\n\n如果LTA能够覆盖未来三到五年70%以上的总供给，那么DRAM股票的理论估值中枢将从当前的5倍PE，向8至10倍PE迁移。这一判断的隐含含义是：当前市场对存储公司的定价，仍然停留在“周期股”的旧框架里，而忽视了其向“准成长股”转型的可能性。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 这轮回调不是周期的终点，而是市场从“动量驱动”转向“基本面驱动”的必经之路\n\n自2022年秋季生成式AI问世以来，存储板块已经经历了三次类似的回调。每一次都是抛物线式上涨后，杠杆ETF、对冲基金和散户的拥挤持仓与价格走势发生冲突，引发剧烈修正。摩根斯坦利在报告中明确指出，这种价格层面的重置并不意味着周期结束，恰恰相反，它是周期得以延续的必要条件。\n\n关键在于理解这轮回调的性质。它不是基本面恶化引发的恐慌，而是持仓结构过载后的技术性修正。报告引用了韩国市场历史数据：在KOSPI熔断事件后，三星电子的下一个交易日上涨概率为87.5%，三个月内平均回报率达到36.9%。虽然历史不会简单重复，但这个统计至少说明：当波动\n\n[... middle omitted ...]\n\n这些问题的深入拆解，需要回到完整的原始研报和图表中寻找线索。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nDRAM 回调是好事，不是终点\n\n健康回调，不是结束\n\n这轮内存牛市从3月低点涨得太陡，回调是必然的。但这种价格回撤不代表周期结束，反而是让行情能延续到年底的必要调整。\n\n1/ 为什么说回调是健康的？\n\nAI需求依然强劲，供应端受洁净室和EUV光刻机限制，产能增长有限。加上长期协议（LTA）锁定了大量产能，盈利和现金流增长的确定性高。历史看，自2022年生成式AI推出以来，已经有过3次类似回调，每次都是周期延续的铺垫。\n\n2/ DRAM仍是AI瓶颈\n\n每一代GPU都被内存限制，而非算力。从A100的80GB到Rubin GPU的288-768GB，单AI单元的DRAM容量增长了4-7倍。AI芯片年增速约60%，而内存是产出智能的关键输入——更多HBM带宽、更多DRAM和NAND，意味着每秒更多智能输出。\n\n3/ 价格下降≠周期结束\n\n新产能预计2027年底才上线，但AI需求的价栺弹性不同。更低的DRAM价格会降低AI推理成本，让部署更便宜，从而创造新需求，而非像过去那样只是给固定数量的消费电子降成本。\n\n4/ 估值还有空间\n\n如果LTA能覆盖未来3-5年70%以上的供应，理论上DRAM股票可从目前5倍PE重估\n\n[... middle omitted ...]\n\ngs estimates for memory companies are up just as much as the stocks are – and the LTAs justify a re-rating potential.\n\nMemory cycles – a long-term perspective. We should be near peak cycle by \n\n[... middle omitted ...]\n\narantee performance of the intermediary or provide any assurance of returns to investors. Investment in securities market are subject to market risks. Read all the related documents carefully before investing.\n\n© 2026 MS"
  },
  {
    "id": "R043",
    "title": "摩根斯坦利：中国电动车市场正进入“产品攻势间歇期”的定价博弈",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：中国电动车市场正进入“产品攻势间歇期”的定价博弈\n\n中国电动车市场的周度订单数据，在经历了密集的新品投放季后，正进入一个微妙的“中场休息”阶段。摩根斯坦利最新发布的周度订单追踪报告显示，6月第一周（6月1日至7日），主要电动车厂商的周度订单普遍出现环比下滑。这份报告表面上看是一张常规的周度数据快照，但它揭示了一个更深层的结构性信号：市场对“产品周期”的线性外推正在失效，真正决定下一阶段竞争格局的，不是谁推出了新车，而是谁能在新品间歇期维持订单势能、并在下一轮密集投放前完成渠道与产能的校准。\n\n对于产业决策者和投资者而言，这份报告的价值不在于单周订单的涨跌，而在于它提供了一个观察竞争格局演变的时间窗口。当市场注意力被比亚迪的“大唐”预售、华为与赛力斯的“尚界”系列、以及理想L8的即将推出所吸引时，摩根斯坦利的这份周报提醒我们：在电动车行业，产品攻势的节奏本身已经成为一种竞争变量。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 订单数字背后是“新品消化期”与“预期管理”的博弈\n\n6月第一周的订单数据，最显著的特征是“正常化”。蔚来汽车周订单从5月底的峰值骤降72%，小鹏汽车下滑49%，问界下滑69%。这些数字如果孤立来看，会引发对需求疲软的担忧。但摩根斯坦利在报告中明确指出，这些下滑是“新品上市冲高后的正常回落”——蔚来的ES9、小鹏的GX、问界的M9，都在此前一周或数周内经历了订单爆发，而6月首周的数据只是回到了更可持续的水平。\n\n这里的核心洞察不在于数字本身，而在于数字背后的预期管理。对于一家车企而言，新品上市当周的订单量往往带有“粉丝效应”和“早期尝鲜者”的溢价，这些订单的转化率、退单率与正常订单有本质区别。摩根斯坦利在报告中暗示，真正的考验是这些订单能否在6月交付中得到兑现。报告提到“强劲的订\n\n[... middle omitted ...]\n\n跟踪6月下半月的新品订单数据，在数据发布后第一时间进行复盘。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n6月第一周订单回落，但别慌\n\n订单降温，但6月有看头\n\n刚拿到某外资投行的周度订单跟踪，6月第一周（1-7日）各品牌订单普遍回落，但仔细看，这更像是新品发布潮后的正常调整，6月交付量反而可能走高。\n\n几个关键观察👇\n\n**1/ 比亚迪：环比涨了23%**\n周订单68.4-68.9k，虽同比降16%，但环比上月同期还涨了23%。接下来就看“大唐”的预订单转化，“汉”是下一个催化剂。\n\n**2/ 蔚来、小鹏：高位回调，但同比亮眼**\n蔚来13.2-13.7k（环比-72%，同比+144%），ES9上市冲高后回归常态。\n小鹏9.6-9.8k（环比-49%，同比-15%），GX首发热度过后也在降温。但同比数据说明，这两家今年的产品节奏确实在改善。\n\n**3/ 理想、问界：等待新车型**\n理想7.1-7.6k（环比-9%），L8即将发布。\n问界8.8-9k（环比-69%），M9热度消退后回落，但同比仍有增长。\n\n**4/ 小米、零跑、极氪：各有看点**\n小米8-8.2k（环比-20%，同比+60%），基数效应下仍保持增长。\n零跑14.6-14.8k，C系列改款SUV预计会带动后续订单。\n极氪6.6-6.8k（同比+65\n\n[... middle omitted ...]\n\nk:\n\nBYD (1211.HK/002594.SZ) 68.4-68.9k (-10% WoW, +23% MoM, -16% YoY). Order growth in the following weeks will hinge on the pre-order conversion of Great Tang, with Great Han serving as the n\n\n[... middle omitted ...]\n\nd>XPeng Inc. (XPEV.N)</td><td>O (01/29/2021)</td><td>US$15.83</td></tr></table>\n\nStock Ratings are subject to change. Please see latest research for each company.  \n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R044",
    "title": "摩根斯坦利：全球钢铁市场的真正拐点不在需求，而在欧洲供给侧的重新定价",
    "digest": "[wechat_article.md]\n# 摩根斯坦利：全球钢铁市场的真正拐点不在需求，而在欧洲供给侧的重新定价\n\n全球钢铁市场正在经历一个被多数投资者低估的结构性转变。这份摩根斯坦利刚刚发布的研报，核心判断并非关于中国出口量的短期波动，而是指向一个更深层的趋势：欧洲正在通过政策工具和地缘政治现实，系统性地重塑其钢铁定价权。对于关注全球资产配置和产业趋势的决策者而言，理解这一转变，远比跟踪月度贸易数据更为关键。\n\n报告揭示了一个看似矛盾的现象：中国5月成品钢净出口环比增长约10%，达到989万吨，年化运行率约1.19亿吨，甚至高于摩根斯坦利中国材料分析师对2026年全年约1.05亿吨的预测。然而，出口的绝对数量并非重点。真正值得关注的是，这些增量正在被全球贸易格局的区域化趋势所抵消，而欧洲正成为这一趋势的最大受益者。\n\n中国出口数据本身并不构成对欧洲市场的直接威胁。报告明确指出，中国仅占欧洲钢铁进口量的约13%。但这组数字背后的结构性含义，才是投资者需要深挖的。当全球钢铁市场从“全球化套利”转向“区域化定价”，欧洲本土钢厂正在获得过去十年未曾有过的定价权。这并非一个短期现象，而是一个由政策、地缘和成本结构共同塑造的新均衡。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 欧洲正在通过政策工具建立一道隐形的结构性壁垒，而非仅仅针对中国的贸易摩擦\n\n市场习惯将欧洲的钢铁政策视为针对中国过剩产能的临时性防御。但摩根斯坦利的分析表明，这套政策框架的设计逻辑远比“反倾销”复杂。从2026年1月1日起实施的CBAM（碳边境调节机制），以及从7月1日起收紧的保障措施（包括更高的配额外关税），正在共同构建一个多层级的保护体系。\n\n报告特别提及了“熔化与浇注条款”（melted-and-poured clause）。这一条款的设计精妙之处在于，它不仅仅限制中国直接出口，还\n\n[... middle omitted ...]\n\n拆解这份报告的图表数据，并探讨其对全球资产配置的更深层含义。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n中国5月钢材出口环比回升，但同比仍降\n\n🌍 全球钢材流向在变\n\n某外资投行最新研报显示，中国5月钢材净出口989万吨，环比增约10%，但同比仍低约8%。国内需求疲软是主因，CISA会员产量同比降7%。\n\n关键变化在区域结构👇\n\n1️⃣ 欧洲正在“筑墙”\n二季度欧洲钢材进口量环比4Q25下降，政策效果开始显现。CBAM（碳边境调节机制）2026年1月生效+保障措施7月收紧，预计让欧洲结构性短缺1000-1500万吨，支撑价格。\n\n2️⃣ 供应链安全溢价\n中东冲突以来，欧洲热卷CIF价格涨70美元/吨，而中国FOB仅涨29美元/吨。欧洲溢价扩大41美元/吨——买家在为“距离近、供应稳”付费。\n\n3️⃣ 利润池在转移\n欧盟热卷利润已升至404美元/吨，高于长期均值320美元/吨。研报认为，欧洲本土钢厂正重新获得定价权，拥有当地资产、灵活调配产能的企业更受益。\n\n📌 核心逻辑：政策红利+地缘溢价，让欧洲钢企的利润中枢可能系统性上移。\n\n大家怎么看CBAM对全球贸易流的影响？欢迎一起讨论。\n\n#学习笔记\n\n[source_mineru.md]\n## China Steel Exports | Europe\n\n# May\n\n[... middle omitted ...]\n\nwever, YtD, exports remain \\~8% lower YoY. YtD CISA member output is down \\~7% YoY, underscoring persistent demand weakness, with the latest late-May datapoint pointing to a further 4% decline\n\n[... middle omitted ...]\n\nd><td>€11.36</td></tr></table>\n\nvoestalpine AG (VOES.VI)\n\nE (06/01/2026)\n\n€45.72\n\nStock Ratings are subject to change. Please see latest research for each company.\n\n\\* Historical prices are not split adjusted.\n\n© 2026 MS"
  },
  {
    "id": "R045",
    "title": "NOM：中国汽车市场2026年可能首次出现国内需求双位数下滑",
    "digest": "[wechat_article.md]\n# NOM：中国汽车市场2026年可能首次出现国内需求双位数下滑\n\n这份NOM研报的核心判断并不令人意外，但其警示的深度值得认真对待。5月数据公布后，市场普遍关注的是环比改善，而NOM选择将目光投向一个更根本的问题：国内汽车市场正在经历一个结构性转折点，2026年全年国内零售销量可能出现有史以来首次双位数同比下滑。这个判断如果成立，将从根本上改变对中国汽车产业链的定价逻辑。\n\n报告发布时点恰逢国内车企密集推出新车型和技术升级的窗口期，但NOM的订单追踪显示，除了新车上市带来的短期脉冲，市场并未出现有意义的有机需求改善。这意味着，当前行业面临的问题不是供给端缺乏创新，而是需求端正在经历一个更深层次的收缩周期。对于投资者和产业决策者而言，理解这个收缩的性质和边界，远比关注月度环比数据更有价值。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 5月数据确认了国内需求的疲软并非短期扰动，而是趋势性下滑\n\n5月中国乘用车零售销量（剔除微型客车）为150万辆，同比下降22.0%。虽然环比增长9.2%看起来是一个积极信号，但NOM明确指出，这种环比改善更多是季节性因素所致，而非需求回暖的标志。更值得关注的是，今年前5个月累计零售销量为710万辆，同比下降19.3%，这是自2020年疫情冲击以来的最低水平。\n\n将这个数据放在更长的历史背景下看，2020年国内零售全年约为1920万辆，而2026年前5个月的运行节奏如果延续，全年零售可能落在1700-1800万辆区间。这意味着国内市场规模正在退回五年前的水平。NOM在报告中提出一个大胆但逻辑自洽的假设：如果当前趋势延续且没有增量刺激政策，2026年国内汽车销量可能出现历史上首次双位数同比下滑。\n\n这个判断的意义不在于预测的精确度，而在于它揭示了一个关键变化：过去几年市场一直习惯于将销\n\n[... middle omitted ...]\n\n研报解读和原始数据图表，并与更多关注产业趋势的读者交流观点。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n5月车市：回暖只是假象\n\n**5月车市，回暖了吗？**\n\n回暖了，但只是环比，同比还在跌。\n\n**1/ 整体销量：环比改善，同比压力未减**\n\n5月国内乘用车批发2.3mn，环比+5.8%，但同比-4.2%。零售更惨，1.5mn辆，同比-22%。前5个月累计零售7.1mn，同比-19.3%，是2020年以来最低。\n\n**2/ 新能源渗透率创新高，但增速放缓**\n\n5月EV零售95万辆，同比-7.5%，环比+12%。渗透率62.1%，同比+9.9pp，再创新高。燃油车零售56.1万辆，同比-38.4%。EV相对强势，但自身增速也在收窄。\n\n**3/ 新车+技术升级，没拉动需求**\n\n研报指出，过去两个月新车密集上市、技术升级，但没看到终端需求明显回暖。订单跟踪显示，除了新车型带来的脉冲，自然需求没有改善。如果政策刺激不追加，2026年国内零售可能首次出现两位数同比下滑。\n\n**4/ 出口是唯一亮点**\n\n5月出口80.9万辆，同比+73%；前5个月累计350万辆，同比+70%。主要玩家出口增速都很猛。但研报也提醒：出口增速太快可能引发贸易摩擦，欧盟、巴西、墨西哥等地关税风险在上升。\n\n**5/ 各品牌表现分化*\n\n[... middle omitted ...]\n\nfor the third month within 5M26, with more than 20% y-y decline. PV retail sales were at 7.1mn units in 5M26 (-19.3% y-y), the lowest level for the domestic market demand since 2020 (impacted \n\n[... middle omitted ...]\n\nable upon request and disclosure information is available at the NOM Disclosure web page:\n\nhttp://go.NOMnow.com/research/m/Disclosures\n\nCopyright © 2026 NOM International (Hong Kong) Ltd., Hong Kong. All rights reserved."
  },
  {
    "id": "R046",
    "title": "JPM：日本股市真正的博弈不在AI，而在价值与动量的交叉点",
    "digest": "[wechat_article.md]\n# JPM：日本股市真正的博弈不在AI，而在价值与动量的交叉点\n\nJPM最新发布的日本权益风格投资报告，在看似延续“AI半导体引领市场”的共识背后，藏着一个更值得推敲的判断：当前日本股市最被低估的交易机会，并非追高动量股，而是那些同时具备价值特征和适度动量的股票。这个判断的逻辑链条并不复杂，但它的含义却可能被大多数投资者忽视。\n\n这份报告发布的时间点值得注意。日经225指数在6月初逼近68000点，全球AI半导体热潮持续推高相关标的，动量因子在过去12个月录得0.44的夏普比率，Beta因子表现同样强劲。市场看起来气势如虹。但JPM的量化团队却在此时刻意提醒两个风险：市场对日本央行可能更为鹰派的加息路径定价不足，以及赢家与输家之间极端分化可能出现的部分修正。\n\n换句话说，这份报告的核心主张是：在动量过热、价值被压抑的当下，投资者不应简单地在两个阵营之间做二选一，而应该寻找那个被忽略的交集地带。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 动量交易已经拥挤到需要重新审视风险回报比\n\nJPM在报告中提供了一个关键数据点：动量因子在5月录得6.4%的月度回报，4月更是高达14.1%。但3月的数据是-12.9%。这种剧烈波动本身就说明，动量交易已经不再是低波动率的“躺赢”策略。当动量因子在三个月内从-12.9%跳到14.1%再回到6.4%，它本质上已经变成了一个高Beta、高换手率的博弈工具。\n\n更值得关注的是持仓集中度。报告明确指出，动量因子的持仓已经高度集中在AI相关标的上。这不是一个分散化的动量组合，而是一个主题化的动量赌注。当市场出现任何对AI主题不利的信号——无论是地缘政治风险、利率预期变化，还是行业自身的周期性回调——这个拥挤的动量仓位都可能面临急剧的去杠杆压力。\n\nJPM也承认，在动量出现“迷你崩盘”时，\n\n[... middle omitted ...]\n\n的具体执行细节。我们会在群内分享更多基于这份报告的深度分析。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n日股风格轮动：AI主线与价值补涨\n\n📌 价值+动量，下一个轮动方向\n\n---\n\n5月日股跟着全球AI半导体热潮继续走强，日经225逼近68000点。但市场内部已经出现明显的风格分化：\n\n**1️⃣ 动量因子依然最猛**\n半导体设备和AI基础设施相关股票持续领涨，Momentum因子5月回报+6.4%。虽然短期有过热回调，但基本面投资者逢低买入的意愿很强，下跌空间有限。\n\n**2️⃣ 价值因子正在被忽视**\n市场极度集中在AI相关股票上，价值股持续跑输。但问题来了——如果6月日本央行真的加息，那些被冷落的价值股反而可能迎来修复。研报数据显示，价值因子表现与BOJ鹰派程度高度相关，目前价值股明显没有定价这个风险。\n\n**3️⃣ 一个有意思的交叉点**\n研报筛选出“价值+动量”双重特征的股票——既有估值优势，又有一定上涨动能。这类股票在AI主题短暂回调时，可能成为资金轮动的去向。从筛选结果看，能源、保险、电力板块里这类标的比较集中。\n\n**4️⃣ 经济周期还在扩张**\n日本QMI指数5月继续处于扩张区间，AI需求拉动制造业超预期。但研报提醒：目前的改善速度部分靠存储芯片等一次性需求推动，后续加速有难度。进入夏季，需\n\n[... middle omitted ...]\n\nnd Size, particularly Large Cap, outperforming.  \n- Global optimism toward AI semiconductors continued to support Japanese equities on a smoothed basis, despite intermittent pullbacks driven b\n\n[... middle omitted ...]\n\nd third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party.\n\nCompleted 09 Jun 2026 08:35 AM JST\n\nDisseminated 09 Jun 2026 08:35 AM JST"
  },
  {
    "id": "R047",
    "title": "Bernstein：印度350cc摩托车市场真正的较量，不是产品，是分销",
    "digest": "[wechat_article.md]\n# Bernstein：印度350cc摩托车市场真正的较量，不是产品，是分销\n\n印度摩托车市场正在经历一场罕见的正面交锋。Bajaj Auto与Triumph的合资品牌，在2026年4月完成了一次关键的产品线迁移——将旗下主力车型从398cc调整至349cc，正式进入Royal Enfield统治了数十年的350cc排量区间。表面上看，这是一场关于产品力的竞争：马力、保修、服务间隔。但Bernstein这份研报通过深入的经销商调研，给出了一个更克制的判断：市场尚未真正测试Royal Enfield的护城河，因为Triumph还没有让足够多的消费者做出“二选一”的决定。\n\n这份报告的核心洞察在于：Triumph的挑战不是产品够不够好，而是它能否在Royal Enfield的“文化领地”上，建立起足以改变消费者决策路径的分销网络。这不是一个关于发动机排量的故事，而是一个关于“消费者从哪里获取信息、在哪里做决定、信任谁的服务网络”的故事。\n\n以下是我们从Bernstein研报中提炼出的五个关键层次，它们共同指向一个尚未终结的竞争格局。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 税改没有创造机会，而是制造了必须行动的“义务”\n\n2025年8月，印度政府对摩托车消费税进行了结构性调整：350cc及以下排量的税率从28%降至18%，而350cc以上排量的税率则从28-31%提升至40%。这意味着，一个22个百分点的税收悬崖，突然出现在Bajaj和Triumph的398cc产品线面前。\n\nBernstein的分析指出，这一变化被市场普遍解读为“Bajaj获得了进入350cc市场的战略机遇”，但更精确的表述是：它创造了一个无法回避的“义务”。在税改之前，Bajaj选择在398cc排量上竞争，是一个自由的商业决策；税改之后，维\n\n[... middle omitted ...]\n\n的独家图表和实地调研细节，以及我们对这些未解问题的持续追踪。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\n印度摩托车战局：350cc对决\n\n**Bajaj vs 皇家恩菲尔德**\n\n**350cc市场已不再是独角戏**\n\n某外资投行调研报告拆解了这场正在发生的竞争。\n\n---\n\n**1/ 为什么Bajaj必须下调排量**\n\n印度2025年9月调整GST税率后，350cc以下摩托车税率为18%，以上则高达40%。Bajaj旗下Triumph原本主打398cc，直接被逼降级至349cc。\n\n这不是战略野心，而是税务倒逼。\n\n---\n\n**2/ 两个品牌展厅的现状对比**\n\n皇家恩菲尔德：标准款需等3个月，定制款45-60天，工厂满负荷运转。\n\nTriumph：48小时内交付。\n\n一个在管理需求，一个在创造需求。\n\n---\n\n**3/ 谁在考虑换车？**\n\n皇家恩菲尔德350cc用户分四类：\n\n- Bullet 350（占比25%）：忠诚老用户，几乎不受影响\n- Classic 350（占比40%）：依赖品牌社区和二手保值，低度受影响\n- Hunter 350（占比20%）：年轻、城市、首购用户——高度受影响\n- Meteor 350（占比15%）：巡航用户，中度受影响\n\nTriumph目前只在Hunter买家中有真实\n\n[... middle omitted ...]\n\nort.\n\nBajaj Triumph was positioned in the 400cc segment trying to build a new sub category in the premium motorcycle segment but the GST cuts on sub-350cc motorcycles pushed Bajaj to migrate i\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R048",
    "title": "Bernstein：Visa与OpenAI的合作标志着卡片支付正式进入代理时代",
    "digest": "[wechat_article.md]\n# Bernstein：Visa与OpenAI的合作标志着卡片支付正式进入代理时代\n\n市场一直在讨论AI代理将如何颠覆支付行业，但大多数人把方向搞反了。他们担心Visa和Mastercard会被新技术边缘化，而Bernstein这份最新研报给出了一个截然不同的判断：卡片网络非但不会被替代，反而正在成为代理经济最核心的信任基础设施。\n\n这不是一个遥远的假设。就在今天，Visa宣布与OpenAI建立合作伙伴关系，共同构建代理商业的基础设施。几乎同一时间，Mastercard也推出了面向机器支付的Agent Pay for Machines服务。两件事发生在同一天，绝非巧合。\n\n如果你还停留在“AI代理需要新的支付方式”这个思维框架里，这份报告值得你重新审视整个逻辑链条。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 代理商业真正考验的不是技术，而是信任——这正是卡片网络的护城河\n\n很多人把支付理解成“把钱从A挪到B”，所以他们认为区块链、稳定币或者某种新协议就能解决代理支付问题。但Bernstein的观点更深刻：代理商业的核心矛盾不是资金转移的效率，而是信任的建立与验证。\n\n当AI代理代替人类去完成购物、订阅、订票甚至B2B采购时，谁来证明这个代理是经过授权的？谁来确保交易不会被篡改？谁来处理代理发起的欺诈行为？这些问题没有简单的技术答案。\n\nVisa和Mastercard本质上不是支付处理公司，它们是信任网络。7亿以上的凭证、超过1亿的商户覆盖、几十年来积累的风险评估和欺诈检测能力——这些不是一夜之间可以复制的。OpenAI在合作声明中说得非常清楚：“通过与Visa智能商业的整合，我们正在为安全、透明、用户可控的代理交易构建基础设施。”\n\n这不是一个技术集成，这是OpenAI在为代理经济选择信任层。\n\n![研报原图\n\n[... middle omitted ...]\n\n信群里继续讨论，我们可以一起拆解那些报告没有完全讲透的细节。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nVisa联手OpenAI，卡片支付进入代理时代\n\n封面：卡片+AI=新战场\n副标题：Visa与OpenAI合作，开启代理支付时代\n\n最近投行研报指出，Visa和OpenAI的联手，标志着卡片支付正式进入“代理时代”。\n\n**1. 核心逻辑：信任网络的价值**\n很多人担心AI代理会绕过Visa/Mastercard。但研报认为恰恰相反——代理世界信任稀缺，卡片网络拥有70亿+凭证和1亿+商户，反而会成为首选。Visa和Mastercard本质上是信任网络，而非简单的资金转移工具。\n\n**2. 具体合作看点**\nVisa与OpenAI的合作聚焦两大方向：\n- 无缝的代理商务体验\n- 探索未来代理经济用例，包括基于Codex的自主代理体验\n\nVisa同时推出了三项新服务：\n- Agent Score：评估网站对代理商务的友好度\n- Agentic Directory：验证商户和代理身份\n- Large Transaction Model：用于欺诈检测\n\n**3. Mastercard也没闲着**\n研报提到，Mastercard同日推出了Agent Pay for Machines（AP4M），这是一个多轨道的机器支\n\n[... middle omitted ...]\n\nnership with OpenAI (link) to essentially enable agentic commerce, conversational agentic workflows and developer experiences through Visa Intelligent Commerce (including Visa agent tokens) an\n\n[... middle omitted ...]\n\n The entities noted herein may pursue legal action if the unauthorized use results in any defamation and/or reputational risk to the entities noted herein and research published under the Bernstein and Autonomous brands."
  },
  {
    "id": "R049",
    "title": "GS：游戏行业真正的拐点不在2026年的游戏阵容，而在成本结构与IP运营能力的分化",
    "digest": "[wechat_article.md]\n# GS：游戏行业真正的拐点不在2026年的游戏阵容，而在成本结构与IP运营能力的分化\n\n6月初的一周内，State of Play、Summer Game Fest、Xbox Games Showcase、Nintendo Direct四场发布会密集召开，2026年及之后的游戏管线几乎全部揭晓。市场目光自然落在《GTA VI》定档11月、任天堂Switch 2的首年阵容、以及各大发行商的新作排期上。但在这些热闹背后，GS这份研报给出了一个更冷静的判断：真正决定公司未来两年股价走势的，不是管线数量，而是每家公司在“成本上升+硬件周期后半段”这一组合压力下的应对能力。\n\n这份报告覆盖了五家日本游戏公司，给出了两个Buy（索尼、Capcom）、两个Sell（Square Enix、万代南梦宫）以及一个Buy但存在短期不确定性的评级（任天堂）。评级的分化并非基于管线强弱——事实上，Square Enix的管线进展甚至超出预期——而是基于估值、成本结构、以及IP变现效率的深层差异。\n\n以下是我们从这份研报中提炼出的五个核心洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 索尼是平台商中唯一同时具备“管线强度”与“成本管控话语权”的公司\n\n在四家主要平台/发行商中，GS对索尼的评级最为坚定。理由可以拆解为两层。\n\n第一层是管线。索尼的PS5在2026年下半年拥有《GTA VI》这一行业级别的“核弹”，同时第一方与第三方的软件阵容在研报中被评价为“strong”。从Exhibit 1的排期来看，PS5独占或同步发行的重磅作品包括《Marvel‘s Wolverine》（9月）、《ONIMUSHA: Way of the Sword》（9月）以及多款第三方大作。在2026年秋季这个“神仙打架”的窗口，索尼的独占内容密度是足\n\n[... middle omitted ...]\n\n游戏行业的买方视角讨论，不一定对，但至少比市场共识多想一层。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nE3 刚过，游戏圈下半年到明年都有哪些牌？\n\n2026主机游戏大年来了\n\n索尼管线最稳，卡普空内容最多\n\n6 月初的几场游戏发布会看完了，从 State of Play 到 Summer Game Fest，再到 Xbox 和任天堂直面会，管线已经非常清晰。简单拆一下几家核心厂商的看点：\n\n**1/ 索尼：管线最充实，利润管理也有空间**\n- 除了 GTA6 定档 11 月，第一方和第三方的 2026 年阵容都很强。\n- 硬件端，PS5 已进入中后期，索尼明确表态要在成本上升环境下平衡增长和利润，通过调节销量和定价来管理硬件盈利能力，这一策略比任天堂更有主动权。\n\n**2/ 任天堂：Switch 2 需要时间验证**\n- 2026 年第一方主力只有《塞尔达传说：时之笛》重制版，略低于预期。\n- 日本已涨价，美欧 9 月跟进，参考 PS5 涨价后销量依然稳健的经验，中长期 Switch 2 仍有望随管线丰富而逐步渗透，但需要看到实际销售数据才能确认趋势。\n\n**3/ 卡普空：管线深度领先同行**\n- 《怪物猎人：荒野》大型 DLC 符合预期，但 2027 年推出《生化危机：代号维罗妮卡》是意外惊喜。\n- 加上已\n\n[... middle omitted ...]\n\nincluding content newly announced at these events, is shown in Exhibit 1. In 2026, partly because Grand Theft Auto VI, the latest installment in one of the gaming industry’s most iconic IP fra\n\n[... middle omitted ...]\n\nthis information, in whole or in part, to train or finetune a machine learning or artificial intelligence system, or to provide or reproduce this information, in whole or in part, as a prompt or input to any such system."
  },
  {
    "id": "R050",
    "title": "JPM：MLCC材料端正在经历一场被低估的定价权迁移",
    "digest": "[wechat_article.md]\n# JPM：MLCC材料端正在经历一场被低估的定价权迁移\n\n市场对MLCC（多层陶瓷电容器）的关注，长期集中在下游被动元件厂商的库存周期和产能利用率上。但一份来自JPM与国瓷材料（Sinocera）管理层的最新交流纪要揭示了一个更关键的结构性变化：本轮周期的驱动力不再仅仅是需求的回补，而是高端产品对材料端定价权的系统性重塑。\n\n这份报告的核心判断是：MLCC 粉体行业已在2026年上半年进入一个强于市场预期的上升周期，其可持续性并非来自传统消费电子的温和复苏，而是来自AI服务器和汽车电子对高端粉体需求的刚性增长，以及中国对稀土出口管控带来的长期竞争壁垒。这意味着，材料端正在从“被动跟随”转向“主动定价”，而市场对这一转变的定价可能尚不充分。\n\n国瓷材料作为占据国内MLCC粉体市场超过80%份额、全球约20%份额的绝对龙头，其产能规划、产品结构变化和客户认证进展，为理解这一产业趋势提供了清晰的微观注脚。以下是我们从这场对话中提炼出的五个关键洞察。\n\n![研报原图 1](assets/source_image_01.jpg)\n\n## 1. 高端产品线正在制造一个利润“断层”，而非简单的量价齐升\n\n传统MLCC粉体与高端产品之间的利润鸿沟，远比市场认知的更为陡峭。报告数据显示，常规MLCC粉体价格在每吨6-7万元人民币，毛利率在33%以上。而汽车级产品价格跃升至每吨8-9万元，AI服务器级粉体更是突破每吨10万元。高端产品的毛利率区间高达45%至50%。\n\n这不仅仅是数字上的差异。它意味着，当一家企业能够将产能从常规产品向高端产品转移时，其整体盈利能力的提升是倍数级的，而非线性增长。国瓷材料在2025年底投产的2000吨高端生产线，以及计划在2026年底前完成的另外3000吨扩产，正是对这一利润断层的直接回应。公司预计2026年高端产品销量将超过1000吨，这将成\n\n[... middle omitted ...]\n\n入的产业链调研、更精细的财务模型以及持续的事件跟踪才能回答。\n\n![](https://github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg)\n\n<p style=\"color:#999999;font-size:12px;\">Personal reading notes and learning share only. Not investment advice.</p>\n\n[note.md]\nMLCC 粉末，AI 和车规在撑腰\n\nMLCC 粉末的春天\n\n高端需求才是增长引擎\n\n某外资投行最新研报指出，MLCC 粉末行业在 1H26 进入强势上行周期，AI 服务器和汽车电子是主要驱动力。国内龙头厂商全年营收增长目标 20%+，在当前趋势下大概率能实现。\n\n1️⃣ **价格分层很清晰**\n- 常规 MLCC 粉末：6-7 万元/吨，毛利率 33%+\n- 车规级产品：8-9 万元/吨\n- AI 服务器级：超 10 万元/吨，高端品种毛利率可达 45%-50%\n\n2️⃣ **产能规划有序**\n- 消费级：1 万吨稳定产能，去年开工率 70%+\n- 高端产线：2000 吨已于 2025 年底投产，2026 年底再扩 3000 吨\n- 预计 2026 年高端产品销售超 1000 吨\n\n3️⃣ **技术门槛不低**\n高端 MLCC 粉末粒径要求 100-200nm，对均匀性和分散性要求极高。良率只有 80% 左右（常规产品 95%+），但一旦通过验证，后续客户认证周期会大幅缩短。\n\n4️⃣ **稀土优势是长期护城河**\n中国供应全球 80%-95% 的 MLCC 粉末用稀土资源。虽然日企有 1-2 年战略库存，\n\n[... middle omitted ...]\n\nnewly completed, high-end MLCC product lines. Capacity has ramped up for high-end MLCC powders, which boast higher selling prices and gross margins. Meanwhile, its portfolio of AI-related new \n\n[... middle omitted ...]\n\nen consent from JPM any research material received from JPM or an authorized third-party (“JPM Data”) in any third-party artificial intelligence (“AI”) systems or models when such JPM Data is accessible by a third-party."
  }
]

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
[
  {
    "figure_id": "F001",
    "report_id": "R002",
    "label": "Figure 1",
    "context": "Figure 1: China's trade momentum accelerated further"
  },
  {
    "figure_id": "F002",
    "report_id": "R002",
    "label": "Figure 2",
    "context": "Figure 2: \"AHEAD\" factors remained the dominant drivers"
  },
  {
    "figure_id": "F003",
    "report_id": "R002",
    "label": "Figure 3",
    "context": "Figure 3: Exports to major developed markets surged"
  },
  {
    "figure_id": "F004",
    "report_id": "R002",
    "label": "Figure 4",
    "context": "Figure 4: Energy imports strengthened significantly"
  },
  {
    "figure_id": "F005",
    "report_id": "R003",
    "label": "Exhibit 1",
    "context": "Exhibit 1: INR on a REER basis has now fallen to more than 3.7 standard deviations away from the 10-year mean trend"
  },
  {
    "figure_id": "F006",
    "report_id": "R003",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The key driver has been weaker BOP dynamics"
  },
  {
    "figure_id": "F007",
    "report_id": "R003",
    "label": "Exhibit 3",
    "context": "Exhibit 3: FII has recorded persistent outflows"
  },
  {
    "figure_id": "F008",
    "report_id": "R003",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Net FDI has been depressed amid outward FDI and repatriations"
  },
  {
    "figure_id": "F009",
    "report_id": "R003",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Reflecting the BoP pressures on FX, RBI has ramped up interventions"
  },
  {
    "figure_id": "F010",
    "report_id": "R003",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Import cover ratio has decreased"
  },
  {
    "figure_id": "F011",
    "report_id": "R003",
    "label": "Exhibit 7",
    "context": "Exhibit 7: India among the more exposed to the energy shock within the region Oil and gas trade balance (% of GDP, 12M trailing sum as of Mar-26)"
  },
  {
    "figure_id": "F012",
    "report_id": "R003",
    "label": "Exhibit 8",
    "context": "Exhibit 8: India's 1Q26 earnings growth lagged other major indices more levered to the AI thematic EPS growth (%Y, 1Q26)"
  },
  {
    "figure_id": "F013",
    "report_id": "R003",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Current account deficit expected to widen to 1.8% of GDP by F27 Current account balance (% of GDP, 4Q trailing sum)"
  },
  {
    "figure_id": "F014",
    "report_id": "R003",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Nascent recovery in non-tech exports so far"
  },
  {
    "figure_id": "F015",
    "report_id": "R003",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Asia headed towards a multi-year capex super-cycle"
  },
  {
    "figure_id": "F016",
    "report_id": "R003",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Asia's industrial and capex cycle is backed by multiple new structural demand drivers Asia's industrial and capex cycle is backed by multiple drivers AI and AI-related infrastructure Energy and energy transition Defens"
  },
  {
    "figure_id": "F017",
    "report_id": "R003",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Our equipment capex proxy – capital goods imports – is accelerating to beyond 2017-18 highs (excluding the pickup in 2021-22 driven by Covid base effects)"
  },
  {
    "figure_id": "F018",
    "report_id": "R003",
    "label": "Exhibit 15",
    "context": "Exhibit 15: In India, we also expect investment to GDP to rise"
  },
  {
    "figure_id": "F019",
    "report_id": "R003",
    "label": "Exhibit 16",
    "context": "Exhibit 16: We see a capex super-cycle playing out"
  },
  {
    "figure_id": "F020",
    "report_id": "R003",
    "label": "Exhibit 17",
    "context": "Exhibit 17: India's capex cycle will benefit from the four structural drivers"
  },
  {
    "figure_id": "F021",
    "report_id": "R003",
    "label": "Exhibit 18",
    "context": "Exhibit 18: India has significantly increased services exports share over the last decade"
  },
  {
    "figure_id": "F022",
    "report_id": "R003",
    "label": "Exhibit 19",
    "context": "Exhibit 19: India has not gained global goods export market share"
  },
  {
    "figure_id": "F023",
    "report_id": "R003",
    "label": "Exhibit 22",
    "context": "Exhibit 22: India's working age population addition over the next decade is large, implying the need for faster job creation"
  },
  {
    "figure_id": "F024",
    "report_id": "R003",
    "label": "Exhibit 23",
    "context": "Exhibit 23: India has not gained global goods export market share"
  },
  {
    "figure_id": "F025",
    "report_id": "R003",
    "label": "Exhibit 24",
    "context": "Exhibit 24: For India to maximise its benefit from this multi-year super-cycle, there is a need to boost its competitiveness in manufacturing... Global export share change since Dec-17"
  },
  {
    "figure_id": "F026",
    "report_id": "R003",
    "label": "Exhibit 25",
    "context": "Exhibit 25: ...and lift its market share in global exports Global export share change since Dec-17"
  },
  {
    "figure_id": "F027",
    "report_id": "R003",
    "label": "Exhibit 26",
    "context": "Exhibit 26: World Bank analysis shows global employment elasticities tend to be higher for the manufacturing exports sector... Export-employment and export-income elasticities"
  },
  {
    "figure_id": "F028",
    "report_id": "R003",
    "label": "Exhibit 27",
    "context": "Exhibit 27: ...especially in high-to-medium technology intensity exports"
  },
  {
    "figure_id": "F029",
    "report_id": "R003",
    "label": "Exhibit 28",
    "context": "Exhibit 28: China's global export market share gains have been propelled by gains in fast-growing segments"
  },
  {
    "figure_id": "F030",
    "report_id": "R003",
    "label": "Exhibit 29",
    "context": "Exhibit 29: This is helped by China's ability to anticipate shifting global demand trends in high-growth emerging sectors like EVs, batteries, and robotics and build capacity to meet demand, even if ahead of time"
  },
  {
    "figure_id": "F031",
    "report_id": "R004",
    "label": "Exhibit 6",
    "context": "EXHIBIT 6: As Spotify's gross margin climbs toward the 35% to 40% target, the content and distribution share of every revenue dollar falls from 75 cents in 2022 to about 64 cents by 2030, with the marketplace, up roughly fourfold i"
  },
  {
    "figure_id": "F032",
    "report_id": "R004",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: We see AI-driven pricing power and incremental engagement more than offsetting royalty leakage and engagement drag, adding \\~\\$2.3Bn to 2030E streaming TAM Recorded music streaming TAM, AI headwinds & tailwinds (\\$B)"
  },
  {
    "figure_id": "F033",
    "report_id": "R004",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: AI-driven upside: Streaming TAM CAGR expands to 9.3% through 2030E Streaming TAM CAGR to 2030E: AI v. Non-AI scenarios"
  },
  {
    "figure_id": "F034",
    "report_id": "R004",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: The music industry has delivered a decade of growth, highlighting the resilience of the streaming ecosystem; industry expansion suggests new technologies such as AI are more likely to grow, rather than displace the music"
  },
  {
    "figure_id": "F035",
    "report_id": "R004",
    "label": "Exhibit 11",
    "context": "EXHIBIT 11: Consumer sentiment on AI in music points to strong support for artist protections and regulatory guardrails, reinforcing the view that AI is more likely to complement than replace the core music market Consumers' views"
  },
  {
    "figure_id": "F036",
    "report_id": "R004",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Top Ten\\* Global artists - UMG is over indexed to global megastars. It remains to be seen whether these artists will also over index on covers and remixes"
  },
  {
    "figure_id": "F037",
    "report_id": "R004",
    "label": "EXHIBIT 13",
    "context": "EXHIBIT 13: Recorded Music global market shares"
  },
  {
    "figure_id": "F038",
    "report_id": "R004",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Music Publishing global market shares"
  },
  {
    "figure_id": "F039",
    "report_id": "R004",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: UMG #1 client is not disclosed but has to be Spotify implying €2.5bn revs in 2025 - #2 and #3 certainly YouTube and Apple Music"
  },
  {
    "figure_id": "F040",
    "report_id": "R004",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: Hybe's monetization model is built to fully capture the economics of superfandom, where “love” is the core driver rather than utility or passive consumption. Nature of business comparison in Entertainment space \"You can"
  },
  {
    "figure_id": "F041",
    "report_id": "R004",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: K-pop sustains high-intensity engagement across a multi-year idol lifecycle, from pre-debut discovery to peak group activity and long-tail solo phases, unlike other verticals where engagement fades quickly and monetizati"
  },
  {
    "figure_id": "F042",
    "report_id": "R005",
    "label": "Exhibit 3",
    "context": "Exhibit 3: The expansion in Infineon's valuation multiple implied by our PT is congruent with the increase in 2Y FWD revenue CAGR versus history"
  },
  {
    "figure_id": "F043",
    "report_id": "R005",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Contextualisation of valuation vs EPS growth"
  },
  {
    "figure_id": "F044",
    "report_id": "R005",
    "label": "Exhibit 5",
    "context": "Exhibit 5: The expansion in STMicro's valuation multiple in underpinned by an increase in 2Y FWD revenue CAGR versus history"
  },
  {
    "figure_id": "F045",
    "report_id": "R005",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Contextualisation of valuation vs EPS growth"
  },
  {
    "figure_id": "F046",
    "report_id": "R006",
    "label": "Exhibit 1",
    "context": "Exhibit 1-Exhibit 3) EXHIBIT 1: Asia ex Japan factor performance: YTD price momentum has led, up 36%-38% relative to market while low vol/high yield/value has underperformed the market the most Asia ex Japan 2026 YTD Factor Perfor"
  },
  {
    "figure_id": "F047",
    "report_id": "R006",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Asia ex Japan/China Factor Performance: Momentum rally has been even stronger in Asia ex China, up 60% vs. market. Growth and earnings momentum have also done well, up 40% vs. market Asia ex Japan/China 2026 YTD Factor P"
  },
  {
    "figure_id": "F048",
    "report_id": "R006",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: YTD, momentum rally has been strong in Japan too, up 18% relative to market, however, growth cohort has been the best, generating 25% alpha Japan YTD Factor Performance (rel. to Market)"
  },
  {
    "figure_id": "F049",
    "report_id": "R006",
    "label": "Exhibit 4",
    "context": "EXHIBIT 4: Asia Momentum 12m fwd. PE: Asia earnings momentum basket has been trading at record high valuations for a while. Price momentum in Asia is still not trading at record high valuations (at 1.3SD level), however in Asia ex"
  },
  {
    "figure_id": "F050",
    "report_id": "R006",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Asia Momentum PB: On PB, earnings momentum in Asia and Asia ex China reached record high in this cycle and always showing peak. Price momentum, however is at record high PB only in Asia ex China. Japan momentum trade sti"
  },
  {
    "figure_id": "F051",
    "report_id": "R006",
    "label": "Exhibit 6",
    "context": "Exhibit 6- Exhibit 7) EXHIBIT 6: Asia Momentum Earnings Revision: Momentum rally has been more driven by rising earnings expectations across Asia, Asia ex China and Japan and now earnings upgrade cycle is at record high levels. Thi"
  },
  {
    "figure_id": "F052",
    "report_id": "R006",
    "label": "Exhibit 6",
    "context": "Exhibit 6- Exhibit 7) EXHIBIT 6: Asia Momentum Earnings Revision: Momentum rally has been more driven by rising earnings expectations across Asia, Asia ex China and Japan and now earnings upgrade cycle is at record high levels. Thi"
  },
  {
    "figure_id": "F053",
    "report_id": "R006",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Asia Momentum Crowding: Interestingly the crowding risk in momentum basket in the region is not elevated Asia ex Japan 12m Price Momentum - Crowding"
  },
  {
    "figure_id": "F054",
    "report_id": "R006",
    "label": "Exhibit 8",
    "context": "EXHIBIT 8: Momentum has been extremely strong within Asia tech sector - stocks with high price momentum have generated 63%-80% alpha Asia Tech 2026 YTD Factor Performance (rel. to Market)"
  },
  {
    "figure_id": "F055",
    "report_id": "R006",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Tech Momentum is at record high valuations, all-time high upgrades and record high crowding, however relative valuations still look fine, though earnings expectations look extreme even on relative basis Asia Tech Price M"
  },
  {
    "figure_id": "F056",
    "report_id": "R006",
    "label": "Exhibit 10",
    "context": "Exhibit 10-Exhibit 12) EXHIBIT 10: Asia ex Japan momentum correlation with other factors: In Asia, momentum rally has been strongly correlated to growth stocks while low vol now sits at record low momentum. We find this extreme int"
  },
  {
    "figure_id": "F057",
    "report_id": "R006",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: In Asia ex Japan ex China, momentum has been all about high vol and growth with low vol stocks now dropping to worst momentum seen last in 1999. This further highlights a potential comeback of low vol stocks from extreme"
  },
  {
    "figure_id": "F058",
    "report_id": "R006",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: The intra-market dispersion caused by momentum rally has not been extreme in Japan"
  },
  {
    "figure_id": "F059",
    "report_id": "R006",
    "label": "Exhibit 13",
    "context": "Exhibit 13-Exhibit 16) EXHIBIT 13: YTD factor performance in Korea: Momentum has far exceeded all other styles, delivering 53%-54% alpha Korea YTD Factor Performance (rel. to Market)"
  },
  {
    "figure_id": "F060",
    "report_id": "R006",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Taiwan's momentum rally has been even more sharp, delivering $63\\%$ alpha YTD Taiwan YTD Factor Performance (rel. to Market)"
  },
  {
    "figure_id": "F061",
    "report_id": "R006",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: While China overall has lagged KR/TW markets but momentum stocks have generated 22% alpha even in China YTD China YTD Factor Performance (rel. to Market)"
  },
  {
    "figure_id": "F062",
    "report_id": "R006",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Interestingly, even in India (market that has generated negative returns), momentum has outperformed the market by 19% India YTD Factor Performance (rel. to Market)"
  },
  {
    "figure_id": "F063",
    "report_id": "R006",
    "label": "Exhibit 17",
    "context": "Exhibit 17-Exhibit 18) EXHIBIT 17: Momentum bubble is visible in both TW and KR where momentum stocks reached record high valuations in this cycle and already showing de-rating since the beginning of this month"
  },
  {
    "figure_id": "F064",
    "report_id": "R006",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: Earnings expectations for momentum stocks is at record high levels in China and TW. In KR, 2009 cycle had higher earnings revisions for momentum. In India, earnings revisions have just turned positive for momentum stocks"
  },
  {
    "figure_id": "F065",
    "report_id": "R006",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: Crowding risk is highest in Korea momentum while crowding in TW momentum is also elevated"
  },
  {
    "figure_id": "F066",
    "report_id": "R006",
    "label": "Exhibit 20",
    "context": "Exhibit 20-Exhibit 22) EXHIBIT 20: Momentum in growth stocks has reached record high in China market while momentum in value, high yield and low vol has fallen to record low"
  },
  {
    "figure_id": "F067",
    "report_id": "R006",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: In Taiwan, momentum has been strongly correlated to growth stocks and has been anti-value and anti-low vol. The dispersion is near 10yr high now Correlation: Taiwan Price Momentum 12m vs. Other factors"
  },
  {
    "figure_id": "F068",
    "report_id": "R006",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: Momentum in Korea has also created extreme dispersion for low vol stocks which are now sitting at decade low momentum Correlation: Korea Price Momentum 12m vs. Other factors Correlation: Korea Earnings Momentum 12m vs."
  },
  {
    "figure_id": "F069",
    "report_id": "R006",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: Momentum in Korea has also created extreme dispersion for low vol stocks which are now sitting at decade low momentum Correlation: Korea Price Momentum 12m vs. Other factors Correlation: Korea Earnings Momentum 12m vs."
  },
  {
    "figure_id": "F070",
    "report_id": "R006",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: Momentum in Korea has also created extreme dispersion for low vol stocks which are now sitting at decade low momentum Correlation: Korea Price Momentum 12m vs. Other factors Correlation: Korea Earnings Momentum 12m vs."
  },
  {
    "figure_id": "F071",
    "report_id": "R006",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: There is no extreme caused by momentum trends in India"
  },
  {
    "figure_id": "F072",
    "report_id": "R007",
    "label": "Figure 2",
    "context": "Our two-tiered model (double decker model) analyzes the data from 2017 through 2025, and we add dummy variables for 2022 while also adding the cross terms (interaction terms) to the analysis (we estimated both the intercept dummy and the slope dummy for 2022)."
  },
  {
    "figure_id": "F073",
    "report_id": "R007",
    "label": "Figure 2",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Note: The deviation from the 200-day MA is based on the actual 200-day MA in the single deck model and on our 200-day MA estimate in the double decker model. Figure 2. USD/JPY: Double decker"
  },
  {
    "figure_id": "F074",
    "report_id": "R007",
    "label": "Figure 3",
    "context": "One reason is that for the USDJPY and Japanese equities, the former also has a strong influence on the latter (they have strong coinstantaneity). On the other hand, regarding the rate spread, change in USD interest rates is much larger than that in JPY interes"
  },
  {
    "figure_id": "F075",
    "report_id": "R007",
    "label": "Figure 6",
    "context": "Figure 6 summarizes the lower structure of the model, and the independent variables are the 200-day moving averages of 1) the US-Japan 10-year inflation-linked bond yield differential (real long-term interest rate spread), 2) Japanese equities (log), 3) the Bl"
  },
  {
    "figure_id": "F076",
    "report_id": "R007",
    "label": "Figure 7",
    "context": "4) The DXY index is the variable via which the USDJPY is most autocorrelated, but in our view it is realistically the most important factor in defining the overall framework for movement in this currency pair (Figures 13, 14). As we note above, the two-tier mo"
  },
  {
    "figure_id": "F077",
    "report_id": "R007",
    "label": "Figure 8",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Note: Deviation from 200-day MA. Figure 8. USD/JPY and US-Japan 10y inflation-linked bond yield differential (real interest rate spread)"
  },
  {
    "figure_id": "F078",
    "report_id": "R007",
    "label": "Figure 9",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Note: 200-day moving average (MA). Figure 9. USD/JPY and Japanese stock index (TOPIX)"
  },
  {
    "figure_id": "F079",
    "report_id": "R007",
    "label": "Figure 10",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Note: Deviation from 200-day MA. Figure 10. USD/JPY and Japanese stock index (TOPIX)"
  },
  {
    "figure_id": "F080",
    "report_id": "R007",
    "label": "Figure 11",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Note: 200-day moving average (MA). Figure 11. USD/JPY and CitiFX Commodity ToT Index spread (US-Japan spread)"
  },
  {
    "figure_id": "F081",
    "report_id": "R007",
    "label": "Figure 12",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Note: Deviation from 200-day MA. Figure 12. USD/JPY and Bloomberg Commodity Index"
  },
  {
    "figure_id": "F082",
    "report_id": "R007",
    "label": "Figure 13",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Note: 200-day moving average (MA). Figure 13. USD/JPY and DXY"
  },
  {
    "figure_id": "F083",
    "report_id": "R007",
    "label": "Figure 14",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Note: Deviation from 200-day MA. Figure 14. USD/JPY and DXY"
  },
  {
    "figure_id": "F084",
    "report_id": "R007",
    "label": "Figure 15",
    "context": "In term of the USD index, we expect it to remain firm overall this year, including against the EUR, but the USDJPY tends to follow the EURUSD after a lag of two or three years (Figure 15). In addition, the nominal long-term interest rate spread has already con"
  },
  {
    "figure_id": "F085",
    "report_id": "R007",
    "label": "Figure 16",
    "context": "© 2026 Citi Inc. No redistribution without Citi's written permission. Figure 16. USD/JPY and US-Japan 10-year bond yield differential"
  },
  {
    "figure_id": "F086",
    "report_id": "R008",
    "label": "Figure 1",
    "context": "Figure 1: Slowing but above-trend growth and sharp rebound in inflation"
  },
  {
    "figure_id": "F087",
    "report_id": "R008",
    "label": "Figure 2",
    "context": "Figure 2: Weaker growth momentum in April"
  },
  {
    "figure_id": "F088",
    "report_id": "R008",
    "label": "Figure 3",
    "context": "Figure 3: Growth slows, inflation rebounds"
  },
  {
    "figure_id": "F089",
    "report_id": "R008",
    "label": "Figure 4",
    "context": "Figure 4: North Asia's strong rebound"
  },
  {
    "figure_id": "F090",
    "report_id": "R008",
    "label": "Figure 5",
    "context": "Figure 5: Surging exports, led by semis"
  },
  {
    "figure_id": "F091",
    "report_id": "R008",
    "label": "Figure 6",
    "context": "Figure 6: GDP growth"
  },
  {
    "figure_id": "F092",
    "report_id": "R008",
    "label": "Figure 7",
    "context": "Figure 7: North Asia's investment recovery"
  },
  {
    "figure_id": "F093",
    "report_id": "R008",
    "label": "Figure 8",
    "context": "Figure 8: Equipment investment mirrors exports"
  },
  {
    "figure_id": "F094",
    "report_id": "R008",
    "label": "Figure 9",
    "context": "Figure 9: Output price vs. input cost"
  },
  {
    "figure_id": "F095",
    "report_id": "R008",
    "label": "Figure 10",
    "context": "Figure 10: North Asia's consumption recovery"
  },
  {
    "figure_id": "F096",
    "report_id": "R008",
    "label": "Figure 11",
    "context": "Figure 11: Fuel price adjustment Transport/fuel inflation"
  },
  {
    "figure_id": "F097",
    "report_id": "R008",
    "label": "Figure 12",
    "context": "Figure 12: Rising Fuel & Turn in Food Inflation CPI contribution ex CH, IN %yoy"
  },
  {
    "figure_id": "F098",
    "report_id": "R008",
    "label": "Figure 13",
    "context": "Figure 13: Exports and imports are growing much faster than expected"
  },
  {
    "figure_id": "F099",
    "report_id": "R008",
    "label": "Figure 14",
    "context": "Figure 14: Investment slipped unexpectedly in April"
  },
  {
    "figure_id": "F100",
    "report_id": "R008",
    "label": "Figure 15",
    "context": "Figure 15: PPI recovery accelerated"
  },
  {
    "figure_id": "F101",
    "report_id": "R008",
    "label": "Figure 16",
    "context": "Figure 16: Industrial profits improved significantly, albeit concentrated in a few industries"
  },
  {
    "figure_id": "F102",
    "report_id": "R008",
    "label": "Figure 17",
    "context": "Figure 17: The correction has lasted about as long, and become about as deep, as typical housing downturns"
  },
  {
    "figure_id": "F103",
    "report_id": "R008",
    "label": "Figure 18",
    "context": "Figure 18: Secondary home transactions increased rapidly in large cities"
  },
  {
    "figure_id": "F104",
    "report_id": "R008",
    "label": "Figure 19",
    "context": "Figure 19: Renminbi will likely remain a strong currency"
  },
  {
    "figure_id": "F105",
    "report_id": "R008",
    "label": "Figure 20",
    "context": "Figure 20: Panda and Dim Sum bond issuance increased by 30% YoY in the first 5 months"
  },
  {
    "figure_id": "F106",
    "report_id": "R008",
    "label": "Figure 21",
    "context": "Figure 21: IPOs may accelerate further in the second half"
  },
  {
    "figure_id": "F107",
    "report_id": "R008",
    "label": "Figure 22",
    "context": "Figure 22: Housing prices reached double-digit growth, while mortgages rebounded at a slower pace"
  },
  {
    "figure_id": "F108",
    "report_id": "R008",
    "label": "Figure 23",
    "context": "Figure 23: Consumption will likely benefit from rising inbound tourism"
  },
  {
    "figure_id": "F109",
    "report_id": "R008",
    "label": "Figure 24",
    "context": "Figure 24: We expect a stronger HKD in the second half"
  },
  {
    "figure_id": "F110",
    "report_id": "R008",
    "label": "Figure 25",
    "context": "Figure 25: Urban Consumer Confidence"
  },
  {
    "figure_id": "F111",
    "report_id": "R008",
    "label": "Figure 26",
    "context": "Figure 26: Rural Consumer Confidence"
  },
  {
    "figure_id": "F112",
    "report_id": "R008",
    "label": "Figure 29",
    "context": "Figure 29: Household Inflation expectation (1-Yr ahead)"
  },
  {
    "figure_id": "F113",
    "report_id": "R008",
    "label": "Figure 30",
    "context": "Figure 30: Inflation expectation and real rates"
  },
  {
    "figure_id": "F114",
    "report_id": "R008",
    "label": "Figure 31",
    "context": "Figure 31: Household Inflation expectation (1-Yr ahead) – annual average Inflation expectations, annual average"
  },
  {
    "figure_id": "F115",
    "report_id": "R008",
    "label": "Figure 32",
    "context": "Figure 32: Household Inflation expectation (1-Yr ahead) & CPI Food–annual average"
  },
  {
    "figure_id": "F116",
    "report_id": "R008",
    "label": "Figure 34",
    "context": "Figure 33: Trade balance under pressure"
  },
  {
    "figure_id": "F117",
    "report_id": "R008",
    "label": "Figure 35",
    "context": "Figure 34: Cutback in capital goods imports since March"
  },
  {
    "figure_id": "F118",
    "report_id": "R008",
    "label": "Figure 35",
    "context": "Figure 35: Potential under-invoicing in coal exports"
  },
  {
    "figure_id": "F119",
    "report_id": "R008",
    "label": "Figure 36",
    "context": "Figure 36: Additional fuel subsidies averaging 0.1% of GDP per month Indonesia fuel subsidies"
  },
  {
    "figure_id": "F120",
    "report_id": "R008",
    "label": "Figure 39",
    "context": "Figure 38: Inflation slowed, but still meaningfully above target"
  },
  {
    "figure_id": "F121",
    "report_id": "R008",
    "label": "Figure 39",
    "context": "Figure 39: Underlying inflation still shows broad price pressures on year-ago..."
  },
  {
    "figure_id": "F122",
    "report_id": "R008",
    "label": "Figure 40",
    "context": "Figure 40: ...and sequential momentum basis."
  },
  {
    "figure_id": "F123",
    "report_id": "R008",
    "label": "Figure 41",
    "context": "Figure 41: Essential goods price inflation could accelerate if/once price caps are released"
  },
  {
    "figure_id": "F124",
    "report_id": "R008",
    "label": "Figure 44",
    "context": "Figure 42: MAS to pre-emptively tighten in July..."
  },
  {
    "figure_id": "F125",
    "report_id": "R008",
    "label": "Figure 43",
    "context": "Figure 43: ...despite the downside surprise in April inflation..."
  },
  {
    "figure_id": "F126",
    "report_id": "R008",
    "label": "Figure 44",
    "context": "Figure 44: ...as price pressures are expected to build in the months ahead..."
  },
  {
    "figure_id": "F127",
    "report_id": "R008",
    "label": "Figure 45",
    "context": "Figure 45: ...following price surges along earlier parts of the supply chain."
  },
  {
    "figure_id": "F128",
    "report_id": "R008",
    "label": "Figure 46",
    "context": "Figure 46:BoK Dot plot"
  },
  {
    "figure_id": "F129",
    "report_id": "R008",
    "label": "Figure 47",
    "context": "Figure 47: Our Taylor Rule says"
  },
  {
    "figure_id": "F130",
    "report_id": "R008",
    "label": "Figure 48",
    "context": "Figure 48: Falling Gangnam Housing"
  },
  {
    "figure_id": "F131",
    "report_id": "R008",
    "label": "Figure 49",
    "context": "Figure 49: Tourism surge"
  },
  {
    "figure_id": "F132",
    "report_id": "R008",
    "label": "Figure 50",
    "context": "Figure 50: Exports"
  },
  {
    "figure_id": "F133",
    "report_id": "R008",
    "label": "Figure 51",
    "context": "Figure 51: Taiwan's export outlook further improves"
  },
  {
    "figure_id": "F134",
    "report_id": "R008",
    "label": "Figure 52",
    "context": "Figure 52: Crude oil and natural gas inventories decreased, while they are not yet significantly lower than the lows of previous years"
  },
  {
    "figure_id": "F135",
    "report_id": "R008",
    "label": "Figure 53",
    "context": "Figure 53: Food and electricity prices are likely to be affected by the El Niño"
  },
  {
    "figure_id": "F136",
    "report_id": "R008",
    "label": "Figure 54",
    "context": "Figure 54: We expect NTD to steadily appreciate in the second half"
  },
  {
    "figure_id": "F137",
    "report_id": "R008",
    "label": "Figure 55",
    "context": "Figure 55: GDP by demand GDP contr, % yoy"
  },
  {
    "figure_id": "F138",
    "report_id": "R008",
    "label": "Figure 56",
    "context": "Figure 56: GDP fell sharply in April"
  },
  {
    "figure_id": "F139",
    "report_id": "R008",
    "label": "Figure 57",
    "context": "Figure 57: Growth drivers"
  },
  {
    "figure_id": "F140",
    "report_id": "R008",
    "label": "Figure 58",
    "context": "Figure 58: Tourism"
  },
  {
    "figure_id": "F141",
    "report_id": "R008",
    "label": "Figure 59",
    "context": "Figure 59: Fuel price hikes"
  },
  {
    "figure_id": "F142",
    "report_id": "R008",
    "label": "Figure 60",
    "context": "Figure 60: FDI remains strong"
  },
  {
    "figure_id": "F143",
    "report_id": "R008",
    "label": "Figure 61",
    "context": "Figure 61: Strong imports drag on trade balance"
  },
  {
    "figure_id": "F144",
    "report_id": "R008",
    "label": "Figure 62",
    "context": "Figure 62: Exports by goods"
  },
  {
    "figure_id": "F145",
    "report_id": "R008",
    "label": "Figure 63",
    "context": "Figure 63: Imports by goods"
  },
  {
    "figure_id": "F146",
    "report_id": "R008",
    "label": "Figure 64",
    "context": "Figure 64: Retail sales remained resilient..."
  },
  {
    "figure_id": "F147",
    "report_id": "R008",
    "label": "Figure 65",
    "context": "Figure 65: Higher inflation led by fuel"
  },
  {
    "figure_id": "F148",
    "report_id": "R008",
    "label": "Figure 66",
    "context": "Figure 66: Public investment growth"
  },
  {
    "figure_id": "F149",
    "report_id": "R008",
    "label": "Figure 67",
    "context": "Figure 67: FX, inflation and rates"
  },
  {
    "figure_id": "F150",
    "report_id": "R008",
    "label": "Figure 82",
    "context": "Figure 82: Heatmap of headline inflationary momentum"
  },
  {
    "figure_id": "F151",
    "report_id": "R008",
    "label": "Figure 83",
    "context": "Figure 83: Heatmap of Monthly Growth Indicators (MGIs)"
  },
  {
    "figure_id": "F152",
    "report_id": "R008",
    "label": "Figure 84",
    "context": "Figure 84: GDP growth – EM Asia-8 vs. CH vs. IN"
  },
  {
    "figure_id": "F153",
    "report_id": "R008",
    "label": "Figure 85",
    "context": "Figure 85: GDP growth – EM Asia vs. other EMs"
  },
  {
    "figure_id": "F154",
    "report_id": "R008",
    "label": "Figure 86",
    "context": "Figure 86: Real exports growth – EM Asia-8 vs. CH vs. IN"
  },
  {
    "figure_id": "F155",
    "report_id": "R008",
    "label": "Figure 87",
    "context": "Figure 87: Real exports growth – EM Asia vs. other EMs"
  },
  {
    "figure_id": "F156",
    "report_id": "R008",
    "label": "Figure 88",
    "context": "Figure 88: EM Asia CPI contribution"
  },
  {
    "figure_id": "F157",
    "report_id": "R008",
    "label": "Figure 89",
    "context": "Figure 89: EM Asia CPI inflation"
  },
  {
    "figure_id": "F158",
    "report_id": "R008",
    "label": "Figure 90",
    "context": "Figure 90: Export growth – EM Asia-8 vs. CH vs. IN"
  },
  {
    "figure_id": "F159",
    "report_id": "R008",
    "label": "Figure 91",
    "context": "Figure 91: Export growth – EM Asia vs. other EMs"
  },
  {
    "figure_id": "F160",
    "report_id": "R008",
    "label": "Figure 92",
    "context": "Figure 92: Composite PMI – China, India, Hong Kong"
  },
  {
    "figure_id": "F161",
    "report_id": "R008",
    "label": "Figure 93",
    "context": "Figure 93: Mfg PMI – Indonesia, Malaysia, Philippines"
  },
  {
    "figure_id": "F162",
    "report_id": "R008",
    "label": "Figure 94",
    "context": "Figure 94: Mfg PMI – China, Thailand, Vietnam"
  },
  {
    "figure_id": "F163",
    "report_id": "R008",
    "label": "Figure 95",
    "context": "Figure 95: Mfg PMI – Singapore, S Korea, Taiwan"
  },
  {
    "figure_id": "F164",
    "report_id": "R008",
    "label": "Figure 96",
    "context": "Figure 96: China – Inflation (CPI)"
  },
  {
    "figure_id": "F165",
    "report_id": "R008",
    "label": "Figure 97",
    "context": "Figure 97: China – 7d OMO Rate"
  },
  {
    "figure_id": "F166",
    "report_id": "R008",
    "label": "Figure 98",
    "context": "Figure 98: Hong Kong – Inflation (CPI)"
  },
  {
    "figure_id": "F167",
    "report_id": "R008",
    "label": "Figure 99",
    "context": "Figure 99: Hong Kong – Base Rate"
  },
  {
    "figure_id": "F168",
    "report_id": "R008",
    "label": "Figure 100",
    "context": "Figure 100: India – Inflation (CPI)"
  },
  {
    "figure_id": "F169",
    "report_id": "R008",
    "label": "Figure 101",
    "context": "Figure 101: India – Repo Rate"
  },
  {
    "figure_id": "F170",
    "report_id": "R008",
    "label": "Figure 102",
    "context": "Figure 102: Indonesia – Inflation (CPI)"
  },
  {
    "figure_id": "F171",
    "report_id": "R008",
    "label": "Figure 103",
    "context": "Figure 103: Indonesia – Reverse Repo Rate"
  },
  {
    "figure_id": "F172",
    "report_id": "R008",
    "label": "Figure 104",
    "context": "Figure 104: Malaysia – Inflation (CPI)"
  },
  {
    "figure_id": "F173",
    "report_id": "R008",
    "label": "Figure 105",
    "context": "Figure 105: Malaysia – Overnight Policy Rate"
  },
  {
    "figure_id": "F174",
    "report_id": "R008",
    "label": "Figure 106",
    "context": "Figure 106: Philippines – Inflation (CPI)"
  },
  {
    "figure_id": "F175",
    "report_id": "R008",
    "label": "Figure 107",
    "context": "Figure 107: Philippines – O/N Reverse Repo Rates"
  },
  {
    "figure_id": "F176",
    "report_id": "R008",
    "label": "Figure 108",
    "context": "Figure 108: Singapore – Inflation (CPI)"
  },
  {
    "figure_id": "F177",
    "report_id": "R008",
    "label": "Figure 109",
    "context": "Figure 109: Singapore – S\\$NEER (estimated)"
  },
  {
    "figure_id": "F178",
    "report_id": "R008",
    "label": "Figure 110",
    "context": "Figure 110: South Korea – Inflation (CPI)"
  },
  {
    "figure_id": "F179",
    "report_id": "R008",
    "label": "Figure 111",
    "context": "Figure 111: South Korea – Base Rate"
  },
  {
    "figure_id": "F180",
    "report_id": "R008",
    "label": "Figure 112",
    "context": "Figure 112: Sri Lanka – Inflation (CPI)"
  },
  {
    "figure_id": "F181",
    "report_id": "R008",
    "label": "Figure 113",
    "context": "Figure 113: Sri Lanka – Overnight Policy Rate"
  },
  {
    "figure_id": "F182",
    "report_id": "R008",
    "label": "Figure 114",
    "context": "Figure 114: Taiwan – Inflation (CPI)"
  },
  {
    "figure_id": "F183",
    "report_id": "R008",
    "label": "Figure 115",
    "context": "Figure 115: Taiwan – Discount Rate"
  },
  {
    "figure_id": "F184",
    "report_id": "R008",
    "label": "Figure 116",
    "context": "Figure 116: Thailand – Inflation (CPI)"
  },
  {
    "figure_id": "F185",
    "report_id": "R008",
    "label": "Figure 117",
    "context": "Figure 117: Thailand – 1-day Repurchase Rate"
  },
  {
    "figure_id": "F186",
    "report_id": "R008",
    "label": "Figure 118",
    "context": "Figure 118: Vietnam – Inflation (CPI)"
  },
  {
    "figure_id": "F187",
    "report_id": "R008",
    "label": "Figure 119",
    "context": "Figure 119: Vietnam – Refinancing Rate"
  },
  {
    "figure_id": "F188",
    "report_id": "R009",
    "label": "Figure 5",
    "context": "## Our key takeaways are as such: - Our estimates suggest fund allocations into Samsung Electronics and SK Hynix may have breached the 10% limit around 13 May 2026 and 6 May 2026, respectively, broadly in line with when market discussions on the topic began. -"
  },
  {
    "figure_id": "F189",
    "report_id": "R011",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Confidence is Deteriorating... Consumer Confidence and Economy Watchers Survey DI (Household Activity-Related)"
  },
  {
    "figure_id": "F190",
    "report_id": "R011",
    "label": "Exhibit 2",
    "context": "Exhibit 2: ...But Hard Data Remains Solid Machinery Orders (Private Sector Excluding Volatile Orders) and BOJ Consumption Activity Index"
  },
  {
    "figure_id": "F191",
    "report_id": "R011",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Even on a Basis Excluding the Effects of Government Measures, Growth in Many Price Indicators Has Slowed Recently, but..."
  },
  {
    "figure_id": "F192",
    "report_id": "R011",
    "label": "Exhibit 4",
    "context": "Exhibit 4: ...The Surge in B2B Prices is Expected to Increase Upward Pressure on Consumer Prices Going Forward"
  },
  {
    "figure_id": "F193",
    "report_id": "R011",
    "label": "Exhibit 6",
    "context": "Exhibit 6: BOJ is Expected to Gradually Reduce Monthly JGB Purchases Until March 2027 and Maintain Purchases Volume from April 2027 Onward BOJ's Monthly JGB Purchase Reduction Schedule"
  },
  {
    "figure_id": "F194",
    "report_id": "R016",
    "label": "Figure 2",
    "context": "Figure 2: Chinese OEMs European market volume by automaker ## By Country Figure 3: European market total volume trend"
  },
  {
    "figure_id": "F195",
    "report_id": "R016",
    "label": "Figure 4",
    "context": "Figure 4: Total European market volume breakdown by OEM"
  },
  {
    "figure_id": "F196",
    "report_id": "R016",
    "label": "Figure 5",
    "context": "Figure 5: Chinese OEMs' aggregate European market volume trend"
  },
  {
    "figure_id": "F197",
    "report_id": "R016",
    "label": "Figure 6",
    "context": "Figure 6: Aggregate market share of Chinese OEMs in European market"
  },
  {
    "figure_id": "F198",
    "report_id": "R016",
    "label": "Figure 7",
    "context": "Figure 7: Germany market wide volume trend"
  },
  {
    "figure_id": "F199",
    "report_id": "R016",
    "label": "Figure 8",
    "context": "Figure 8: Germany market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F200",
    "report_id": "R016",
    "label": "Figure 9",
    "context": "Figure 9: Chinese OEMs' aggregate volume trend in Germany"
  },
  {
    "figure_id": "F201",
    "report_id": "R016",
    "label": "Figure 10",
    "context": "Figure 10: Aggregate market share of Chinese OEMs in Germany"
  },
  {
    "figure_id": "F202",
    "report_id": "R016",
    "label": "Figure 11",
    "context": "Figure 11: France market wide volume trend"
  },
  {
    "figure_id": "F203",
    "report_id": "R016",
    "label": "Figure 12",
    "context": "Figure 12: France market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F204",
    "report_id": "R016",
    "label": "Figure 13",
    "context": "Figure 13: Chinese OEMs' aggregate volume trend in France"
  },
  {
    "figure_id": "F205",
    "report_id": "R016",
    "label": "Figure 14",
    "context": "Figure 14: Aggregate market share of Chinese OEMs in France"
  },
  {
    "figure_id": "F206",
    "report_id": "R016",
    "label": "Figure 15",
    "context": "Figure 15: UK market wide volume trend"
  },
  {
    "figure_id": "F207",
    "report_id": "R016",
    "label": "Figure 16",
    "context": "Figure 16: UK market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F208",
    "report_id": "R016",
    "label": "Figure 17",
    "context": "Figure 17: Chinese OEMs' aggregate volume trend in the UK"
  },
  {
    "figure_id": "F209",
    "report_id": "R016",
    "label": "Figure 18",
    "context": "Figure 18: Aggregate market share of Chinese OEMs in UK"
  },
  {
    "figure_id": "F210",
    "report_id": "R016",
    "label": "Figure 19",
    "context": "Figure 19: Italy market wide volume trend"
  },
  {
    "figure_id": "F211",
    "report_id": "R016",
    "label": "Figure 20",
    "context": "Figure 20: Italy market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F212",
    "report_id": "R016",
    "label": "Figure 21",
    "context": "Figure 21: Chinese OEMs' aggregate volume trend in Italy"
  },
  {
    "figure_id": "F213",
    "report_id": "R016",
    "label": "Figure 22",
    "context": "Figure 22: Aggregate market share of Chinese OEMs in Italy"
  },
  {
    "figure_id": "F214",
    "report_id": "R016",
    "label": "Figure 23",
    "context": "Figure 23: Turkiye market wide volume trend"
  },
  {
    "figure_id": "F215",
    "report_id": "R016",
    "label": "Figure 24",
    "context": "Figure 24: Turkiye market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F216",
    "report_id": "R016",
    "label": "Figure 25",
    "context": "Figure 25: Chinese OEMs' aggregate volume trend in Turkiye"
  },
  {
    "figure_id": "F217",
    "report_id": "R016",
    "label": "Figure 26",
    "context": "Figure 26: Aggregate market share of Chinese OEMs in Turkiye"
  },
  {
    "figure_id": "F218",
    "report_id": "R016",
    "label": "Figure 27",
    "context": "Figure 27: Spain market wide volume trend"
  },
  {
    "figure_id": "F219",
    "report_id": "R016",
    "label": "Figure 28",
    "context": "Figure 28: Spain market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F220",
    "report_id": "R016",
    "label": "Figure 29",
    "context": "Figure 29: Chinese OEMs' aggregate volume trend in Spain"
  },
  {
    "figure_id": "F221",
    "report_id": "R016",
    "label": "Figure 30",
    "context": "Figure 30: Aggregate market share of Chinese OEMs in Spain"
  },
  {
    "figure_id": "F222",
    "report_id": "R016",
    "label": "Figure 31",
    "context": "Figure 31: Poland market wide volume trend"
  },
  {
    "figure_id": "F223",
    "report_id": "R016",
    "label": "Figure 32",
    "context": "Figure 32: Poland market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F224",
    "report_id": "R016",
    "label": "Figure 33",
    "context": "Figure 33: Chinese OEMs' aggregate volume trend in Poland"
  },
  {
    "figure_id": "F225",
    "report_id": "R016",
    "label": "Figure 34",
    "context": "Figure 34: Aggregate market share of Chinese OEMs in Poland"
  },
  {
    "figure_id": "F226",
    "report_id": "R016",
    "label": "Figure 35",
    "context": "Figure 35: Netherlands market wide volume trend"
  },
  {
    "figure_id": "F227",
    "report_id": "R016",
    "label": "Figure 36",
    "context": "Figure 36: Netherlands market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F228",
    "report_id": "R016",
    "label": "Figure 37",
    "context": "Figure 37: Chinese OEMs' aggregate volume trend in the Netherlands"
  },
  {
    "figure_id": "F229",
    "report_id": "R016",
    "label": "Figure 38",
    "context": "Figure 38: Aggregate market share of Chinese OEMs in the Netherlands"
  },
  {
    "figure_id": "F230",
    "report_id": "R016",
    "label": "Figure 39",
    "context": "Figure 39: Sweden market wide volume trend"
  },
  {
    "figure_id": "F231",
    "report_id": "R016",
    "label": "Figure 40",
    "context": "Figure 40: Sweden market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F232",
    "report_id": "R016",
    "label": "Figure 41",
    "context": "Figure 41: Chinese OEMs' aggregate volume trend in Sweden"
  },
  {
    "figure_id": "F233",
    "report_id": "R016",
    "label": "Figure 42",
    "context": "Figure 42: Aggregate market share of Chinese OEMs in Sweden"
  },
  {
    "figure_id": "F234",
    "report_id": "R016",
    "label": "Figure 43",
    "context": "Figure 43: Norway market wide volume trend 000 Unit"
  },
  {
    "figure_id": "F235",
    "report_id": "R016",
    "label": "Figure 44",
    "context": "Figure 44: Norway market wide volume breakdown by automaker"
  },
  {
    "figure_id": "F236",
    "report_id": "R016",
    "label": "Figure 45",
    "context": "Figure 45: Chinese OEMs' aggregate volume trend in Norway"
  },
  {
    "figure_id": "F237",
    "report_id": "R016",
    "label": "Figure 46",
    "context": "Figure 46: Aggregate market share of Chinese OEMs in Norway"
  },
  {
    "figure_id": "F238",
    "report_id": "R016",
    "label": "Figure 47",
    "context": "Figure 47: SAIC European market volume by country"
  },
  {
    "figure_id": "F239",
    "report_id": "R016",
    "label": "Figure 49",
    "context": "Figure 49: SAIC European market volume trend"
  },
  {
    "figure_id": "F240",
    "report_id": "R016",
    "label": "Figure 50",
    "context": "Figure 50: SAIC European market share trend"
  },
  {
    "figure_id": "F241",
    "report_id": "R016",
    "label": "Figure 51",
    "context": "Figure 51: Chery European market volume by country"
  },
  {
    "figure_id": "F242",
    "report_id": "R016",
    "label": "Figure 53",
    "context": "Figure 53: Chery European market volume trend"
  },
  {
    "figure_id": "F243",
    "report_id": "R016",
    "label": "Figure 54",
    "context": "Figure 54: Chery European market share trend"
  },
  {
    "figure_id": "F244",
    "report_id": "R016",
    "label": "Figure 55",
    "context": "Figure 55: BYD European market volume by country"
  },
  {
    "figure_id": "F245",
    "report_id": "R016",
    "label": "Figure 57",
    "context": "Figure 57: BYD European market volume trend"
  },
  {
    "figure_id": "F246",
    "report_id": "R016",
    "label": "Figure 58",
    "context": "Figure 58: BYD European market share trend"
  },
  {
    "figure_id": "F247",
    "report_id": "R016",
    "label": "Figure 59",
    "context": "Figure 59: Leapmotor European market volume by country"
  },
  {
    "figure_id": "F248",
    "report_id": "R016",
    "label": "Figure 61",
    "context": "Figure 61: Leapmotor European market volume trend"
  },
  {
    "figure_id": "F249",
    "report_id": "R016",
    "label": "Figure 62",
    "context": "Figure 62: Leapmotor European market share trend"
  },
  {
    "figure_id": "F250",
    "report_id": "R016",
    "label": "Figure 63",
    "context": "Figure 63: XPeng European market volume by country"
  },
  {
    "figure_id": "F251",
    "report_id": "R016",
    "label": "Figure 65",
    "context": "Figure 65: XPeng European market volume trend"
  },
  {
    "figure_id": "F252",
    "report_id": "R016",
    "label": "Figure 66",
    "context": "Figure 66: XPeng European market share trend"
  },
  {
    "figure_id": "F253",
    "report_id": "R016",
    "label": "Figure 67",
    "context": "Figure 67: Geely European market volume by country"
  },
  {
    "figure_id": "F254",
    "report_id": "R016",
    "label": "Figure 69",
    "context": "Figure 69: Geely European market volume trend"
  },
  {
    "figure_id": "F255",
    "report_id": "R016",
    "label": "Figure 70",
    "context": "Figure 70: Geely European market share trend"
  },
  {
    "figure_id": "F256",
    "report_id": "R016",
    "label": "Figure 71",
    "context": "Figure 71: Great Wall European market volume by country"
  },
  {
    "figure_id": "F257",
    "report_id": "R016",
    "label": "Figure 72",
    "context": "Figure 72: Great Wall European market volume breakdown"
  },
  {
    "figure_id": "F258",
    "report_id": "R016",
    "label": "Figure 74",
    "context": "Figure 74: Great Wall European market share trend"
  },
  {
    "figure_id": "F259",
    "report_id": "R017",
    "label": "Exhibit 3",
    "context": "Exhibit 5: May growth recovery level remained relatively soft"
  },
  {
    "figure_id": "F260",
    "report_id": "R017",
    "label": "Exhibit 4",
    "context": "Exhibit 4: DAU/user session of major delivery/food service brand APP As of May 2026. Exhibit 5: May growth recovery level remained relatively soft"
  },
  {
    "figure_id": "F261",
    "report_id": "R017",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Latest domestic flight capacity exceeded the FY19 level by +0%, sequentially softened and high oil price was a headwind"
  },
  {
    "figure_id": "F262",
    "report_id": "R017",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Above sized restaurant sales growth slower vs. total catering sales in Apr China restaurant recovery trend (yoy)"
  },
  {
    "figure_id": "F263",
    "report_id": "R017",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Commodity price trends were mixed in May. Pork price stabilized and broiler slightly recovered, while beef/lamb slightly corrected."
  },
  {
    "figure_id": "F264",
    "report_id": "R017",
    "label": "Exhibit 10",
    "context": "Exhibit 10: 12-m P/Es of key restaurant players Data as of Jun 4, 2026. Helens, Chagee data based on Datastream. Exhibit 11: 12-m EV/EBITDA of key restaurant players"
  },
  {
    "figure_id": "F265",
    "report_id": "R017",
    "label": "Exhibit 10",
    "context": "Exhibit 10: 12-m P/Es of key restaurant players Data as of Jun 4, 2026. Helens, Chagee data based on Datastream. Exhibit 11: 12-m EV/EBITDA of key restaurant players"
  },
  {
    "figure_id": "F266",
    "report_id": "R018",
    "label": "Exhibit 1",
    "context": "Exhibit 1: 800 VDC equipment readiness 800 VDC Equipment Readiness Q3 2026 Option 1A – Power Rack (660 kW) Q2 2027 Option 1B – DC Power Center (1.6 MW) Q1 2028 Option 1C – Power Block"
  },
  {
    "figure_id": "F267",
    "report_id": "R019",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Tech net flows as a % of S&P 500 Tech Market cap were the most negative since Feb. '14 Weekly Tech net flows as a % of S&P 500 Tech market cap, since 2008"
  },
  {
    "figure_id": "F268",
    "report_id": "R019",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Institutional clients are the biggest net sellers post-crisis Cumulative flows (\\$ bn) by client type, February 2008-present"
  },
  {
    "figure_id": "F269",
    "report_id": "R019",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Hedge funds and institutional clients are the biggest net sellers vs private clients are net buyers over the past 12 mos L12m cumulative flows (\\$ bn) by client type, June 2025-present"
  },
  {
    "figure_id": "F270",
    "report_id": "R019",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Rolling 4wk avg. US equity flows (based on single stock+ETF flows) is at -\\$2.9bn BofA client total net buys of US equities (stocks & ETFs): four-week avg (\\$ mn) vs. S&P 500, 2008-present"
  },
  {
    "figure_id": "F271",
    "report_id": "R019",
    "label": "Exhibit 8",
    "context": "Exhibit 8: By sector, Tech stocks saw the largest outflows last week BofA client net buying (selling) by GICS sector (\\$mn) – single stocks only"
  },
  {
    "figure_id": "F272",
    "report_id": "R019",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Institutional clients were the biggest net sellers last week BofA client net buying (selling) by client group (\\$mn), stocks+equity ETFs"
  },
  {
    "figure_id": "F273",
    "report_id": "R019",
    "label": "Exhibit 14",
    "context": "Exhibit 14: Only large caps saw outflows last week BofA client net buying (selling) by size segment (\\$mn), stocks+equity ETFs"
  },
  {
    "figure_id": "F274",
    "report_id": "R019",
    "label": "Exhibit 18",
    "context": "Exhibit 18: Rolling 4-wk avg. corp. client buybacks reached record highs of nearly \\$6bn in mid-2024 but have generally decelerated since then, particularly since March 2025 Corporate client flows (buybacks), 4-week avg, \\$ mn, June"
  },
  {
    "figure_id": "F275",
    "report_id": "R019",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Corp. client buybacks trends have been correlated with aggregate S&P 500 buybacks and are +19% YoY BofA corporate clients' 4-week avg. buybacks (YoY % chg) vs. S&P 500 total quarterly buybacks (YoY % chg), since 2010"
  },
  {
    "figure_id": "F276",
    "report_id": "R019",
    "label": "Exhibit 20",
    "context": "Exhibit 20: Corporate client buybacks over the last 12 weeks have been highest in Financials (\\$7.5bn) and Discretionary (\\$4.2bn) Corporate client buybacks by sector: rolling 12-week sum (\\$mn)"
  },
  {
    "figure_id": "F277",
    "report_id": "R019",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Corp. client buybacks (normalized by S&P 500 market cap) peaked at the end of Feb. at 0.42% and have been declining ever since, currently 0.20% Rolling 52-week corporate client buybacks as a % of S&P 500 market cap"
  },
  {
    "figure_id": "F278",
    "report_id": "R019",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Fixed Income ETFs saw the largest inflows last week ETF net buys by asset class (\\$mn)"
  },
  {
    "figure_id": "F279",
    "report_id": "R019",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Blend ETFs saw the largest inflows Equity ETF net buys by style/theme (\\$mn)"
  },
  {
    "figure_id": "F280",
    "report_id": "R019",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Health Care ETFs saw the largest inflows Equity ETF net buys by GICS sector (\\$mn)"
  },
  {
    "figure_id": "F281",
    "report_id": "R019",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Large/mid/broad mkt. cap ETFs saw inflows last week Equity ETF net buys by size classification (\\$mn)"
  },
  {
    "figure_id": "F282",
    "report_id": "R019",
    "label": "Exhibit 26",
    "context": "Exhibit 26: US ETFs saw the largest inflows last week Equity ETF net buys by regional classification (\\$mn)"
  },
  {
    "figure_id": "F283",
    "report_id": "R019",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Cons Disc.: rolling 4-wk avg. outflows since early Dec. 4 week avg. flows (\\$ mn)"
  },
  {
    "figure_id": "F284",
    "report_id": "R019",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Financials: rolling 4-wk avg. inflows for the $3^{\\text{rd}}$ straight week 4 week avg. flows (\\$ mn)"
  },
  {
    "figure_id": "F285",
    "report_id": "R019",
    "label": "Exhibit 34",
    "context": "Exhibit 34: Tech: rolling 4-wk avg. outflows since mid April 4 week avg. flows (\\$ mn)"
  },
  {
    "figure_id": "F286",
    "report_id": "R019",
    "label": "Exhibit 37",
    "context": "Exhibit 37: Utilities: rolling 4-wk avg. inflows for the $5^{\\text{th}}$ straight week 4 week avg. flows (\\$ mn)"
  },
  {
    "figure_id": "F287",
    "report_id": "R019",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Staples: rolling 4-wk avg outflows for the $2^{\\text{nd}}$ straight week 4 week avg. flows (\\$ mn)"
  },
  {
    "figure_id": "F288",
    "report_id": "R019",
    "label": "Exhibit 32",
    "context": "Exhibit 32: Health Care: rolling 4-wk avg. outflows since late Mar. 4 week avg. flows (\\$ mn)"
  },
  {
    "figure_id": "F289",
    "report_id": "R019",
    "label": "Exhibit 35",
    "context": "Exhibit 35: Materials: rolling 4-wk avg. inflows for the $2^{\\text{nd}}$ straight week 4 week avg. flows (\\$ mn)"
  },
  {
    "figure_id": "F290",
    "report_id": "R019",
    "label": "Exhibit 38",
    "context": "Exhibit 38: Real Estate: rolling 4-wk avg. inflows for the $6^{\\text{th}}$ straight week 4 week avg. flows (\\$mn)"
  },
  {
    "figure_id": "F291",
    "report_id": "R019",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Energy: rolling 4-wk avg. inflows for the $1^{\\text{st}}$ time since early Nov. 4 week avg. flows (\\$ mn)"
  },
  {
    "figure_id": "F292",
    "report_id": "R019",
    "label": "Exhibit 33",
    "context": "Exhibit 33: Industrials: rolling 4-wk avg. inflows for the $3^{\\text{rd}}$ straight week 4 week avg. flows (\\$ mn)"
  },
  {
    "figure_id": "F293",
    "report_id": "R019",
    "label": "Exhibit 36",
    "context": "Exhibit 36: Comm. Svcs.: rolling 4-wk avg. outflows for the $2^{\\text{nd}}$ straight week 4 week avg. flows (\\$ mn)"
  },
  {
    "figure_id": "F294",
    "report_id": "R019",
    "label": "Exhibit 39",
    "context": "Exhibit 39: Hedge funds: rolling 4-wk. avg. single stock outflows for the $4^{\\text{th}}$ straight week Hedge fund net buys of US single stocks, 4 wk avg, (\\$mn)"
  },
  {
    "figure_id": "F295",
    "report_id": "R019",
    "label": "Exhibit 41",
    "context": "Exhibit 41: Institutional clients: rolling 4-wk avg. single stock net flows flip negative Institutional net buys of US single stocks, 4 wk avg, (\\$mn)"
  },
  {
    "figure_id": "F296",
    "report_id": "R019",
    "label": "Exhibit 43",
    "context": "Exhibit 43: Private clients: rolling 4-wk avg. single stock outflows since mid Feb. Private client net buys of US single stocks, 4 wk avg, (\\$mn)"
  },
  {
    "figure_id": "F297",
    "report_id": "R019",
    "label": "Exhibit 40",
    "context": "Exhibit 40: Hedge Funds: rolling 4-wk avg. equity (stock+ETF) outflows for the $4^{\\text{th}}$ straight week Hedge fund net buys of equities (US stocks + equity ETFs), 4 wk avg, (\\$mn)"
  },
  {
    "figure_id": "F298",
    "report_id": "R019",
    "label": "Exhibit 42",
    "context": "Exhibit 42: Institutional clients: rolling 4-wk avg. equity (stock+ETF) net flows flip negative Institutional net buys of equities (US stocks + equity ETFs), 4 wk avg, (\\$ mn)"
  },
  {
    "figure_id": "F299",
    "report_id": "R019",
    "label": "Exhibit 44",
    "context": "Exhibit 44: Private clients: rolling 4-wk avg. equity (stock+ETF) outflows for the 3 $^{rd}$ straight week Private client net buys of equities (US stocks + equity ETFs), 4 wk avg, (\\$ mn)"
  },
  {
    "figure_id": "F300",
    "report_id": "R019",
    "label": "Exhibit 45",
    "context": "Exhibit 45: Large caps: rolling 4-wk avg. single stock outflows since late Mar. Net buys of large cap US single stocks, 4 wk avg, (\\$mn)"
  },
  {
    "figure_id": "F301",
    "report_id": "R019",
    "label": "Exhibit 47",
    "context": "Exhibit 47: Mid caps: rolling 4-wk avg. single stock inflows for the 3 $^{rd}$ straight week Net buys of mid cap US single stocks, 4 wk avg, (\\$mn)"
  },
  {
    "figure_id": "F302",
    "report_id": "R019",
    "label": "Exhibit 49",
    "context": "Exhibit 49: Small caps (small+micro): rolling 4-wk avg. single stock outflows for the 5 $^{th}$ straight week Net buys of small cap US single stocks, 4 wk avg, (\\$mn)"
  },
  {
    "figure_id": "F303",
    "report_id": "R019",
    "label": "Exhibit 46",
    "context": "Exhibit 46: Large caps: rolling 4-wk avg. equity (stock+ETF) net flows flip negative Net buys of large cap equities (US stocks + equity ETFs), 4 wk avg, (\\$ mn)"
  },
  {
    "figure_id": "F304",
    "report_id": "R019",
    "label": "Exhibit 48",
    "context": "Exhibit 48: Mid caps: rolling 4-wk avg. equity (stock+ETF) inflows for the $3^{rd}$ straight week Net buys of mid cap equities (US stocks + equity ETFs), 4 wk avg, (\\$ mn)"
  },
  {
    "figure_id": "F305",
    "report_id": "R019",
    "label": "Exhibit 50",
    "context": "Exhibit 50: Small caps (small + micro): rolling 4-wk avg. equity (stock+ETF) outflows for the $5^{\\text{th}}$ straight week Small + micro cap net buys (4-week avg, \\$mn)"
  },
  {
    "figure_id": "F306",
    "report_id": "R019",
    "label": "Exhibit 52",
    "context": "Exhibit 52: Disc. ETFs: rolling 4-wk avg. inflows for the $2^{\\text{nd}}$ straight week 4 week avg, \\$ mn"
  },
  {
    "figure_id": "F307",
    "report_id": "R019",
    "label": "Exhibit 55",
    "context": "Exhibit 55: Financials ETFs: rolling 4-wk avg. outflows since late April 4 week avg, \\$ mn"
  },
  {
    "figure_id": "F308",
    "report_id": "R019",
    "label": "Exhibit 58",
    "context": "Exhibit 58: Tech ETFs: rolling 4-wk avg. net flows flip negative 4 week avg, \\$ mn"
  },
  {
    "figure_id": "F309",
    "report_id": "R019",
    "label": "Exhibit 61",
    "context": "Exhibit 61: Comm. Services ETFs: rolling 4-wk avg. inflows since late April 4-week avg, \\$ mn"
  },
  {
    "figure_id": "F310",
    "report_id": "R019",
    "label": "Exhibit 53",
    "context": "Exhibit 53: Staples ETFs: rolling 4-wk avg. outflows for the $3^{\\text{rd}}$ straight week 4 week avg, \\$ mn"
  },
  {
    "figure_id": "F311",
    "report_id": "R019",
    "label": "Exhibit 56",
    "context": "Exhibit 56: Health Care ETFs: rolling 4-wk avg. inflows for the 2 $^{nd}$ straight week 4 week avg, \\$ mn"
  },
  {
    "figure_id": "F312",
    "report_id": "R019",
    "label": "Exhibit 59",
    "context": "Exhibit 59: Materials ETFs: rolling 4-wk avg. inflows for the 5 $^{th}$ straight week 4 week avg, \\$ mn"
  },
  {
    "figure_id": "F313",
    "report_id": "R019",
    "label": "Exhibit 62",
    "context": "BofA GLOBAL RESEARCH Exhibit 62 Utilities ETFs: rolling 4-wk avg. net flows flip negative 4-week avg, \\$ mn"
  },
  {
    "figure_id": "F314",
    "report_id": "R019",
    "label": "Exhibit 54",
    "context": "Exhibit 54: Energy ETFs: rolling 4-wk avg. net flows flip positive 4 week avg, \\$ mn"
  },
  {
    "figure_id": "F315",
    "report_id": "R019",
    "label": "Exhibit 57",
    "context": "Exhibit 57: Industrials ETFs: rolling 4-wk avg. inflows since late August 4 week avg, \\$ mn"
  },
  {
    "figure_id": "F316",
    "report_id": "R019",
    "label": "Exhibit 60",
    "context": "Exhibit 60: Real Estate ETFs: rolling 4-wk avg. net flows flip negative 4 week avg, \\$ mn"
  },
  {
    "figure_id": "F317",
    "report_id": "R019",
    "label": "Exhibit 63",
    "context": "Exhibit 63: Growth ETFs: rolling 4-wk avg inflows since late Oct. 4 week avg, \\$mn"
  },
  {
    "figure_id": "F318",
    "report_id": "R019",
    "label": "Exhibit 64",
    "context": "Exhibit 64: Value ETFs: rolling 4-wk avg. inflows since early Feb. 4 week avg, \\$ mn"
  },
  {
    "figure_id": "F319",
    "report_id": "R019",
    "label": "Exhibit 65",
    "context": "Exhibit 65: Blend ETFs: rolling 4-wk avg. inflows since early April 4 week avg, \\$ mn"
  },
  {
    "figure_id": "F320",
    "report_id": "R019",
    "label": "Exhibit 66",
    "context": "Exhibit 66: Large-cap ETFs: rolling 4-wk avg. inflows since late Mar. 4 week avg, \\$ mn"
  },
  {
    "figure_id": "F321",
    "report_id": "R019",
    "label": "Exhibit 68",
    "context": "Exhibit 68: Small cap ETFs: rolling 4-wk avg. inflows for the 3 $^{rd}$ straight week 4 week avg, \\$ mn"
  },
  {
    "figure_id": "F322",
    "report_id": "R019",
    "label": "Exhibit 67",
    "context": "Exhibit 67: Mid cap ETFs: rolling 4-wk avg. inflows for the 3 $^{rd}$ straight week 4 week avg, \\$ mn"
  },
  {
    "figure_id": "F323",
    "report_id": "R019",
    "label": "Exhibit 69",
    "context": "Exhibit 69: Broad Market ETFs: rolling 4-wk avg. inflows since late August 4 week avg, \\$ mn"
  },
  {
    "figure_id": "F324",
    "report_id": "R019",
    "label": "Exhibit 70",
    "context": "Exhibit 70: Clients (hedge funds + institutional clients + private clients) have been selling single stocks and buying equity ETFs this year Overall BofA client net buys (sales) of single stocks vs. equity ETFs, \\$ mn"
  },
  {
    "figure_id": "F325",
    "report_id": "R019",
    "label": "Exhibit 7",
    "context": "Exhibit 71: Value ETF inflows have outpaced Growth ETF inflows over out data history since 2017 Growth ETF vs. Value ETF cumulative net buys, 2017-now (\\$ mn)"
  },
  {
    "figure_id": "F326",
    "report_id": "R019",
    "label": "Exhibit 72",
    "context": "Exhibit 72: Blend ETFs inflows have seen inflows most week since Mar."
  },
  {
    "figure_id": "F327",
    "report_id": "R019",
    "label": "Exhibit 73",
    "context": "Exhibit 73: Large cap ETFs have seen inflows most weeks since Feb. Large Cap ETF cumulative net buys, 2017-now (\\$ mn)"
  },
  {
    "figure_id": "F328",
    "report_id": "R019",
    "label": "Exhibit 75",
    "context": "Exhibit 75: Small cap ETF have seen inflows most week since May Small Cap ETF cumulative net buys, 2017-now (\\$ mn)"
  },
  {
    "figure_id": "F329",
    "report_id": "R019",
    "label": "Exhibit 74",
    "context": "Exhibit 74: Mid Cap ETFs: have seen outflows most week since May Mid Cap ETF cumulative net buys, 2017-now (\\$ mn)"
  },
  {
    "figure_id": "F330",
    "report_id": "R019",
    "label": "Exhibit 76",
    "context": "Exhibit 76: Broad Market ETF inflows most weeks since March Broad Market ETF cumulative net buys, 2017-now (\\$ mn)"
  },
  {
    "figure_id": "F331",
    "report_id": "R019",
    "label": "Exhibit 77",
    "context": "Exhibit 77: Outflows were led by BD clients BofA client net buys by client group (\\$ mn)"
  },
  {
    "figure_id": "F332",
    "report_id": "R021",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Current Data Center Capacity by Stage Data Center Capacity by Stage"
  },
  {
    "figure_id": "F333",
    "report_id": "R021",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: It Will Take 10 Years to Clear the Current Data Center Pipeline Based on TTM Build Rates"
  },
  {
    "figure_id": "F334",
    "report_id": "R021",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Data Center Capacity (in GW) by Stage of Development"
  },
  {
    "figure_id": "F335",
    "report_id": "R021",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Data Center Capacity by Stage of Development (% Mix)"
  },
  {
    "figure_id": "F336",
    "report_id": "R021",
    "label": "EXHIBIT 6",
    "context": "EXHIBIT 6: Data Center Capacity (in GW) by Operator Data Center Capacity by Operator"
  },
  {
    "figure_id": "F337",
    "report_id": "R021",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Data Center Capacity by Operator (% Mix) Mix of Data Center Capacity by Operator"
  },
  {
    "figure_id": "F338",
    "report_id": "R021",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Stranded Capacity Has Largely Stabilized in '26 at 10-11% of Total Pipeline"
  },
  {
    "figure_id": "F339",
    "report_id": "R021",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 9: Behind The Meter: Only $4\\%$ of the Installed Base, But $25\\%$ of What's Under Construction, and $40\\%$ of The Project Pipeline Behind-the-Meter Mix of Project by Stage"
  },
  {
    "figure_id": "F340",
    "report_id": "R021",
    "label": "EXHIBIT 10",
    "context": "EXHIBIT 10: Real Estate Developers and Crypto Companies Are Driving the Increase in Pipeline, Adding Nearly 30 GW This Month Changes to Data Center Capacity by Stage This Month"
  },
  {
    "figure_id": "F341",
    "report_id": "R021",
    "label": "EXHIBIT 11",
    "context": "EXHIBIT 11: Hyperscalers' Pipeline Remained Relatively Flat This Month, Though They Broke Ground on 1+ GW of New Capacity Changes to Hyperscaler Data Center Capacity by Stage This Month"
  },
  {
    "figure_id": "F342",
    "report_id": "R021",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Quantifying Companies' Data Center TAM Based on 1) Current Capacity in Pipeline, and 2) Given \\$M per MW Opportunity. We Estimate 70% of the Current Pipeline Are AI Builds (Based on Recent ETN Commentary That 70% of Curr"
  },
  {
    "figure_id": "F343",
    "report_id": "R021",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: Consensus is Anticipating \\~\\$640B in Capex Spend From the Top 4 Hyperscalers in '26, Up 78% Y/Y. '27 Currently Expects 27% Growth to \\$812B"
  },
  {
    "figure_id": "F344",
    "report_id": "R021",
    "label": "EXHIBIT 15",
    "context": "EXHIBIT 15: YTD, Consensus' Hyperscaler Capex Estimates Are Up 60%+ For 2026-28"
  },
  {
    "figure_id": "F345",
    "report_id": "R021",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Capacity in Pipeline is Up to 324 GW, Up 29 GW Month-Over-Month"
  },
  {
    "figure_id": "F346",
    "report_id": "R021",
    "label": "EXHIBIT 17",
    "context": "EXHIBIT 17: The Current Pipeline is Dominated by Real Estate Developers, Hyperscalers, and Colocators Mix of Current Pipeline"
  },
  {
    "figure_id": "F347",
    "report_id": "R021",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: The Pipeline Has Grown by 225 GW in the LTM, with Real Estate Developers Contributing the Most Incremental Capacity"
  },
  {
    "figure_id": "F348",
    "report_id": "R021",
    "label": "EXHIBIT 19",
    "context": "EXHIBIT 19: This Month Saw 29 GW Added to the Pipeline M/M Changes in Pipeline by Operator"
  },
  {
    "figure_id": "F349",
    "report_id": "R021",
    "label": "EXHIBIT 20",
    "context": "EXHIBIT 20: Real Estate Developers Drove the Vast Majority of the Increase with 22 GW"
  },
  {
    "figure_id": "F350",
    "report_id": "R021",
    "label": "EXHIBIT 21",
    "context": "EXHIBIT 21: Hyperscalers' Capacity in Pipeline Remained Flat Month-Over-Month at 44 GW, Though Still \\~2x vs. the Start of the Year Capacity in Pipeline by Hyperscaler"
  },
  {
    "figure_id": "F351",
    "report_id": "R021",
    "label": "EXHIBIT 22",
    "context": "EXHIBIT 22: Amazon Has Been the Most Aggressive of the Hyperscalers, Adding 12 GW to the 26 GW Added to Pipeline in the LTM Mix of Hyperscalers' Current Pipeline"
  },
  {
    "figure_id": "F352",
    "report_id": "R021",
    "label": "EXHIBIT 23",
    "context": "EXHIBIT 23: The Hyperscaler Pipeline Has Grown by 29 GW in the LTM, with Amazon Driving 40%+ of Incremental Capacity TTM Additions to Pipeline by Hyperscaler"
  },
  {
    "figure_id": "F353",
    "report_id": "R021",
    "label": "EXHIBIT 24",
    "context": "EXHIBIT 24: In Aggregate, Hyperscalers' Pipeline Remained Flat Month-Over-Month M/M Changes in Pipeline by Hyperscaler"
  },
  {
    "figure_id": "F354",
    "report_id": "R021",
    "label": "EXHIBIT 25",
    "context": "EXHIBIT 25: Google Was the Only Hyperscaler to Marginally Increase Capacity in Pipeline Additions to Pipeline This Month by Hyperscaler"
  },
  {
    "figure_id": "F355",
    "report_id": "R021",
    "label": "EXHIBIT 26",
    "context": "EXHIBIT 26: After Nearly Tripling Capacity in the Pipeline YTD Through April, the Neoclouds Saw the Pipeline Decrease in May"
  },
  {
    "figure_id": "F356",
    "report_id": "R021",
    "label": "EXHIBIT 27",
    "context": "EXHIBIT 27: Nscale and Crusoe Make Up \\~70% of the Current Neocloud Pipeline Mix of Neoclouds' Current Pipeline"
  },
  {
    "figure_id": "F357",
    "report_id": "R021",
    "label": "EXHIBIT 28",
    "context": "EXHIBIT 28: Nscale Has Added 8 GW to Neoclouds' TTM Pipeline Growth, or 50%+ of the Increase"
  },
  {
    "figure_id": "F358",
    "report_id": "R021",
    "label": "EXHIBIT 29",
    "context": "EXHIBIT 29: The Pipeline Amongst Colocators is Up 6+ GW YTD"
  },
  {
    "figure_id": "F359",
    "report_id": "R021",
    "label": "EXHIBIT 30",
    "context": "EXHIBIT 30: Digital Realty, STACK, and QTS Currently Hold the Most Capacity Share of Pipeline Mix of Colocation Current Pipeline"
  },
  {
    "figure_id": "F360",
    "report_id": "R021",
    "label": "EXHIBIT 31",
    "context": "EXHIBIT 31: The Greatest Contribution to Colocators' Pipeline Was Digital Realty with 2 GW or \\~20% of the TTM Increase"
  },
  {
    "figure_id": "F361",
    "report_id": "R021",
    "label": "EXHIBIT 32",
    "context": "EXHIBIT 32: Bitcoin Miners' Power Advantage: Access to \\~30GW planned power Bitcoin Miners - Planned Power Portfolio (MW)"
  },
  {
    "figure_id": "F362",
    "report_id": "R021",
    "label": "EXHIBIT 33",
    "context": "EXHIBIT 33: Bitcoin miners still have significant power runway available for AI/HPC deployments Bitcoin Miners - Available vs Contracted AI capacity (gross MW)"
  },
  {
    "figure_id": "F363",
    "report_id": "R021",
    "label": "EXHIBIT 34",
    "context": "EXHIBIT 34: Bitcoin miners have contracted 20% of their power pipeline to neoclouds, hyperscalers, AI chip makers, etc. Bitcoin miners - Power pipeline, contracted MW and progress (GW)"
  },
  {
    "figure_id": "F364",
    "report_id": "R021",
    "label": "EXHIBIT 35",
    "context": "EXHIBIT 35: ERCOT (Texas) is Expected to Add 24% of All Capacity in Pipeline Capacity in Pipeline by RTO"
  },
  {
    "figure_id": "F365",
    "report_id": "R021",
    "label": "EXHIBIT 36",
    "context": "EXHIBIT 36: Texas Has 2x Capacity in Pipeline as the Next Largest State Capacity in Pipeline by Top 10 States"
  },
  {
    "figure_id": "F366",
    "report_id": "R021",
    "label": "EXHIBIT 37",
    "context": "EXHIBIT 37: Utah Saw The Most Capacity Added to Pipeline This Month Behind O'Leary Ventures Capacity Added to Pipeline This Month"
  },
  {
    "figure_id": "F367",
    "report_id": "R021",
    "label": "EXHIBIT 38",
    "context": "EXHIBIT 38: Capacity in Pipeline Shows a Clear Shift - Data Centers Are Moving Inland Mix of Capacity in Pipeline by State"
  },
  {
    "figure_id": "F368",
    "report_id": "R021",
    "label": "EXHIBIT 39",
    "context": "EXHIBIT 39: Capacity Under Construction is Up to 63 GW, 32% Higher Than Current Active Capacity"
  },
  {
    "figure_id": "F369",
    "report_id": "R021",
    "label": "EXHIBIT 40",
    "context": "EXHIBIT 40: Hyperscalers and Colos Are Responsible For Nearly 70% of Current Construction Mix of Capacity Under Construction"
  },
  {
    "figure_id": "F370",
    "report_id": "R021",
    "label": "EXHIBIT 41",
    "context": "EXHIBIT 41: Capacity Under Construction Has Grown to 41 GW in the LTM. Hyperscalers and Colocators Have Contributed the Most Incremental Capacity, or Nearly 60%"
  },
  {
    "figure_id": "F371",
    "report_id": "R021",
    "label": "EXHIBIT 42",
    "context": "EXHIBIT 42: Capacity Under Construction Grew by 4.4 GW This Month"
  },
  {
    "figure_id": "F372",
    "report_id": "R021",
    "label": "EXHIBIT 43",
    "context": "EXHIBIT 43: Hyperscalers and Developers Drove \\~70% of the Increase"
  },
  {
    "figure_id": "F373",
    "report_id": "R021",
    "label": "EXHIBIT 44",
    "context": "EXHIBIT 44: Hyperscalers' Capacity Under Construction is Up to 24 GW Capacity Under Construction by Hyperscaler"
  },
  {
    "figure_id": "F374",
    "report_id": "R021",
    "label": "EXHIBIT 45",
    "context": "EXHIBIT 45: Amazon, Google, and Meta Are Responsible For 80%+ of All Hyperscale Construction Mix of Hypescalers' Capacity Under Construction"
  },
  {
    "figure_id": "F375",
    "report_id": "R021",
    "label": "EXHIBIT 46",
    "context": "EXHIBIT 46: Hyperscalers Have Started Construction of 11 GW of Capacity in the LTM. Microsoft Has Been the Least Active in Adding to Construction TTM Additions to Capacity Under Construction by Hyperscaler"
  },
  {
    "figure_id": "F376",
    "report_id": "R021",
    "label": "EXHIBIT 47",
    "context": "EXHIBIT 47: Hyperscalers Broke Ground on 1.4 GW of New Capacity Under Construction This Month M/M Change in Capacity Under Construction by Hyperscaler"
  },
  {
    "figure_id": "F377",
    "report_id": "R021",
    "label": "EXHIBIT 48",
    "context": "EXHIBIT 48: Led by Amazon and Meta with a Combined 1.1 GW New Capacity Under Construction This Month by Hyperscaler"
  },
  {
    "figure_id": "F378",
    "report_id": "R021",
    "label": "EXHIBIT 49",
    "context": "EXHIBIT 49: ERCOT and PJM Have 14 GW and 17 GW of Capacity Under Construction, or \\~50% of Total Capacity Under Construction by RTO"
  },
  {
    "figure_id": "F379",
    "report_id": "R021",
    "label": "EXHIBIT 50",
    "context": "EXHIBIT 50: About 25 GW of Capacity Under Construction Sits in Texas and Virginia Capacity Under Construction by Top 10 States"
  },
  {
    "figure_id": "F380",
    "report_id": "R021",
    "label": "EXHIBIT 51",
    "context": "EXHIBIT 51: TX, MO, IA, and VA Saw the Greatest Additions to Capacity Under Construction This Month New Capacity Under Construction This Month"
  },
  {
    "figure_id": "F381",
    "report_id": "R021",
    "label": "EXHIBIT 52",
    "context": "EXHIBIT 52: 50% of Construction is Concentrated in Texas, Virginia, Ohio, and Georgia Mix of Capacity Under Construction by State"
  },
  {
    "figure_id": "F382",
    "report_id": "R021",
    "label": "EXHIBIT 53",
    "context": "EXHIBIT 53: In the Last 12 Months, NIMBY Has Caused a Stark Rise in Stranded Capacity Which is Now Up to 34 GW"
  },
  {
    "figure_id": "F383",
    "report_id": "R021",
    "label": "EXHIBIT 54",
    "context": "EXHIBIT 54: While Most of These Projects' Developers Haven't Been Public (40%+ Not Disclosed), 40% of The Capacity Has Been Centered in Developers and Colos Mix of Stranded Capacity"
  },
  {
    "figure_id": "F384",
    "report_id": "R021",
    "label": "EXHIBIT 55",
    "context": "EXHIBIT 55: In the LTM, Hyperscalers Are Seeing Less Relative Stranded Capacity Mix of Current vs. TTM Stranded Capacity by Operator"
  },
  {
    "figure_id": "F385",
    "report_id": "R021",
    "label": "EXHIBIT 56",
    "context": "EXHIBIT 56: 55% of Americans Would Strongly Oppose New Data Center Construction Near Where They Live Americans' Attitudes Toward Data Centers"
  },
  {
    "figure_id": "F386",
    "report_id": "R021",
    "label": "EXHIBIT 57",
    "context": "EXHIBIT 57: There Are Currently 19 States Restricting or Considering Restrictions on New Data Center Construction States' Legislation Toward New Data Center Construction"
  },
  {
    "figure_id": "F387",
    "report_id": "R021",
    "label": "EXHIBIT 58",
    "context": "EXHIBIT 58: Individual States' Attitudes Toward New Data Center Construction"
  },
  {
    "figure_id": "F388",
    "report_id": "R021",
    "label": "EXHIBIT 59",
    "context": "EXHIBIT 59: Behind The Meter: Only 4% of the Installed Base, But 25% of What's Under Construction, and 40% of The Project Pipeline Behind-the-Meter Mix of Project by Stage"
  },
  {
    "figure_id": "F389",
    "report_id": "R021",
    "label": "EXHIBIT 60",
    "context": "EXHIBIT 60: YTD, BTM Trends Have Remained Largely Consistent, Though the Mix of BTM in Capacity Under Construction Has Gained Greater Share of Mix"
  },
  {
    "figure_id": "F390",
    "report_id": "R021",
    "label": "EXHIBIT 61",
    "context": "EXHIBIT 61: BTM as a % of New Projects Added to Pipeline Every Month: Avergaing 41% Since January, Up to 48% in May. Still Generating Share Gains Relative to Current Share of Active (4%) and Construction (25%) Change in BTM Pipeline"
  },
  {
    "figure_id": "F391",
    "report_id": "R021",
    "label": "EXHIBIT 62",
    "context": "EXHIBIT 62: There Are 129 GW of BTM Capacity in the Pipeline. The Vast Majority Has Yet to Be Disclosed; Developers Dominate the Known Portion"
  },
  {
    "figure_id": "F392",
    "report_id": "R021",
    "label": "EXHIBIT 63",
    "context": "EXHIBIT 63: BTM Represents 64% and 36% of Neocloud and Hyperscaler Pipelines, Respectively (Likely Higher Given Capacity Sitting in “Not Disclosed”) % of Pipeline That is BTM Power"
  },
  {
    "figure_id": "F393",
    "report_id": "R021",
    "label": "EXHIBIT 64",
    "context": "EXHIBIT 64: Stargate (SoftBank/OpenAI/Oracle) Has Led The Rise in BTM Power in Pipeline For Hyperscalers (10 GW) BTM Capacity in Pipeline by Hyperscaler"
  },
  {
    "figure_id": "F394",
    "report_id": "R021",
    "label": "EXHIBIT 65",
    "context": "EXHIBIT 65: There Are Currently 16 GW of BTM Capacity Under Construction, Up 3 GW Month-Over-Month BTM Capacity Under Construction by Operator"
  },
  {
    "figure_id": "F395",
    "report_id": "R021",
    "label": "EXHIBIT 66",
    "context": "EXHIBIT 66: Meta Owns the Vast Majority of the 4.6 GW of BTM Capacity Under Construction by Hyperscalers BTM Capacity Under Construction by Hyperscaler"
  },
  {
    "figure_id": "F396",
    "report_id": "R021",
    "label": "EXHIBIT 67",
    "context": "EXHIBIT 67: Why Are Data Center Operators Choosing BTM Power? Per Crusoe, the Average BTM Data Center Project Can Be Energized in 18 Months vs. Years Via The Traditional Route Data Center Development - Master Timeline"
  },
  {
    "figure_id": "F397",
    "report_id": "R021",
    "label": "EXHIBIT 68",
    "context": "EXHIBIT 68: Active Capacity Sits at 48 GW With Hyperscalers (25 GW) and Colos (20GW) Leading the Way"
  },
  {
    "figure_id": "F398",
    "report_id": "R021",
    "label": "EXHIBIT 69",
    "context": "EXHIBIT 69: Hyperscalers and Colos Account For 90%+ of Current Capacity Mix of Active Capacity"
  },
  {
    "figure_id": "F399",
    "report_id": "R021",
    "label": "EXHIBIT 70",
    "context": "EXHIBIT 70: Hyperscalers and Colos Accounted For \\~80% of the 9 GW of New Capacity Added in the Last 12 Months Mix of Current vs. TTM Added Active Capacity by Operator"
  },
  {
    "figure_id": "F400",
    "report_id": "R021",
    "label": "EXHIBIT 71",
    "context": "EXHIBIT 71: Active Capacity by Hyperscalers is Up to \\~25 GW With Amazon (9 GW) Leading the Way. Meta, Google, and Microsoft Each Have \\~5 GW Available"
  },
  {
    "figure_id": "F401",
    "report_id": "R021",
    "label": "EXHIBIT 72",
    "context": "EXHIBIT 72: Current Hyperscaler Capacity is Dominated by Amazon. The Other 3 Each Have 20% of the Market Mix of Hyperscalers' Active Capacity"
  },
  {
    "figure_id": "F402",
    "report_id": "R021",
    "label": "EXHIBIT 73",
    "context": "EXHIBIT 73: Amazon Has Been the Most Aggressive in Adding Capacity in the Last 12 Months Relative to its Current Capacity Mix of Current vs. TTM Added Active Capacity by Hyperscaler"
  },
  {
    "figure_id": "F403",
    "report_id": "R021",
    "label": "EXHIBIT 74",
    "context": "EXHIBIT 74: PJM (Where Virginia Resides) Houses \\~40% of All Active Data Center Capacity"
  },
  {
    "figure_id": "F404",
    "report_id": "R021",
    "label": "EXHIBIT 75",
    "context": "EXHIBIT 75: Virginia is the Top State For Active Capacity With 11 GW"
  },
  {
    "figure_id": "F405",
    "report_id": "R021",
    "label": "EXHIBIT 76",
    "context": "EXHIBIT 76: Virginia Alone Accounts For \\~25% of Active Data Center Capacity Mix of Active Capacity by State"
  },
  {
    "figure_id": "F406",
    "report_id": "R027",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Insurers' pricing interest rate caps have been declining over the past three years in China"
  },
  {
    "figure_id": "F407",
    "report_id": "R027",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Par account cash flows as a % of operating cash flows increased across most peers in 1Q26 vs. 1Q25"
  },
  {
    "figure_id": "F408",
    "report_id": "R027",
    "label": "Exhibit 5",
    "context": "Exhibit 3: Industry-wide banca channel premiums"
  },
  {
    "figure_id": "F409",
    "report_id": "R027",
    "label": "Exhibit 4",
    "context": "Exhibit 4: More term deposits in China in 2023, with potentially higher demand to reinvest at maturity"
  },
  {
    "figure_id": "F410",
    "report_id": "R027",
    "label": "Exhibit 6",
    "context": "Exhibit 5: 1Q26 par product mix in banca channel"
  },
  {
    "figure_id": "F411",
    "report_id": "R027",
    "label": "Exhibit 6",
    "context": "Exhibit 6: 1Q26 banca channel mix as a % of total premium vs. total asset"
  },
  {
    "figure_id": "F412",
    "report_id": "R027",
    "label": "Exhibit 7",
    "context": "Exhibit 7: 1Q26 channel structure across insurers – gross premium basis"
  },
  {
    "figure_id": "F413",
    "report_id": "R027",
    "label": "Exhibit 9",
    "context": "Exhibit 8: 10-year treasury bond yield slightly rebounded after bottoming in 1H25"
  },
  {
    "figure_id": "F414",
    "report_id": "R027",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Long-duration allocation becoming more attractive as long-end yield continues to widen"
  },
  {
    "figure_id": "F415",
    "report_id": "R027",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Listed insurers' overall bond allocation slightly declined in 2025 while government bond allocation increased"
  },
  {
    "figure_id": "F416",
    "report_id": "R027",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Divergent FVOCI stocks allocation across listed insurers"
  },
  {
    "figure_id": "F417",
    "report_id": "R027",
    "label": "Exhibit 12",
    "context": "Exhibit 12: FVTPL mix in par accounts continues to rise"
  },
  {
    "figure_id": "F418",
    "report_id": "R027",
    "label": "Exhibit 13",
    "context": "Exhibit 13: FVOCI equity mix in par accounts vs. overall FVOCI stock mix"
  },
  {
    "figure_id": "F419",
    "report_id": "R027",
    "label": "Exhibit 15",
    "context": "Exhibit 14: Listed insurers' net investment yields have continuously declined over the past few years"
  },
  {
    "figure_id": "F420",
    "report_id": "R027",
    "label": "Exhibit 15",
    "context": "Exhibit 15: In 1Q26, industry median investment yield was around 0.65%, while median comprehensive investment yield was only about 0.31%"
  },
  {
    "figure_id": "F421",
    "report_id": "R027",
    "label": "Exhibit 19",
    "context": "Exhibit 16: Life insurers' 1Q26 solvency ratio versus total assets"
  },
  {
    "figure_id": "F422",
    "report_id": "R027",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Listed insurers' solvency ratios were maintained relatively higher"
  },
  {
    "figure_id": "F423",
    "report_id": "R027",
    "label": "Exhibit 18",
    "context": "Exhibit 18: China life insurers saw sequential decline in core solvency ratio in 1Q26."
  },
  {
    "figure_id": "F424",
    "report_id": "R027",
    "label": "Exhibit 19",
    "context": "Exhibit 19: 2Q26 core solvency ratios expected to decline from insurers' disclosure"
  },
  {
    "figure_id": "F425",
    "report_id": "R028",
    "label": "FIGURE 1",
    "context": "BARC Bank, Hong Kong the US rose by 6.2% m/m-better than the 2022–24 average of around 5.6% (excluding tariff-distorted dynamics in 2025)-pointing to recovery in shipment momentum. It contributed 3.2pp to headline export growth, well above the 1.2pp recorded i"
  },
  {
    "figure_id": "F426",
    "report_id": "R028",
    "label": "FIGURE 2",
    "context": "FIGURE 2. ... with faster regional trade (Asean, Japan, Korea and Taiwan) and shipments to the US"
  },
  {
    "figure_id": "F427",
    "report_id": "R028",
    "label": "FIGURE 3",
    "context": "FIGURE 3. Strong exports were led by AI-related and green-tech products"
  },
  {
    "figure_id": "F428",
    "report_id": "R028",
    "label": "FIGURE 4",
    "context": "FIGURE 4. High frequency shipping data showed still strong exports in early June"
  },
  {
    "figure_id": "F429",
    "report_id": "R028",
    "label": "FIGURE 5",
    "context": "On a volume basis, imports of energy-related products showed mixed developments. Crude oil imports fell at a faster pace of 29% y/y, following a 20% decline in April. Imports of coal continued to decline, but the pace moderated to -7.7% versus -12.5% previousl"
  },
  {
    "figure_id": "F430",
    "report_id": "R028",
    "label": "FIGURE 6",
    "context": "FIGURE 6. ...with semiconductor import surging on a value basis"
  },
  {
    "figure_id": "F431",
    "report_id": "R028",
    "label": "FIGURE 7",
    "context": "FIGURE 7. Imports of steel and iron ore stayed soft"
  },
  {
    "figure_id": "F432",
    "report_id": "R028",
    "label": "FIGURE 8",
    "context": "FIGURE 8. Imports of crude oil weakened further"
  },
  {
    "figure_id": "F433",
    "report_id": "R029",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Performance of AI-related stocks"
  },
  {
    "figure_id": "F434",
    "report_id": "R029",
    "label": "Exhibit 2",
    "context": "Exhibit 2: Return dispersion of AI-exposed equities standard deviation of returns of GSTMTAIP basket constituents"
  },
  {
    "figure_id": "F435",
    "report_id": "R029",
    "label": "Exhibit 3",
    "context": "Exhibit 3: Distribution of AI-exposed equities' YTD returns"
  },
  {
    "figure_id": "F436",
    "report_id": "R029",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Consensus expects the hyperscalers will spend \\$757 billion in 2026 and \\$920 billion in 2027"
  },
  {
    "figure_id": "F437",
    "report_id": "R029",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Hyperscalers expected to allocate 100% of cash flows from operations to capex"
  },
  {
    "figure_id": "F438",
    "report_id": "R029",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Consensus hyperscaler capex estimates versus realized capex Consensus capex growth estimates for AI hyperscalers"
  },
  {
    "figure_id": "F439",
    "report_id": "R029",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Recent consensus hyperscaler capex estimate revisions Consensus hyperscaler capex estimates"
  },
  {
    "figure_id": "F440",
    "report_id": "R029",
    "label": "Exhibit 8",
    "context": "Exhibit 8: AI hyperscaler 2027 capex scenarios 2027 AI hyperscaler capex scenarios ($ billion)"
  },
  {
    "figure_id": "F441",
    "report_id": "R029",
    "label": "Exhibit 9",
    "context": "Historical technology cycles provide precedent for more than \\$1 trillion in capex in 2027. Incremental AI spending equated to 0.9% of GDP in 2025 and is estimated to reach 1.5% of GDP in 2026. This impulse is similar to the peak impulse during the 1990s, but "
  },
  {
    "figure_id": "F442",
    "report_id": "R029",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Incremental investment in emerging technologies as a share of GDP \"US Generative AI\" includes 2026 forecast"
  },
  {
    "figure_id": "F443",
    "report_id": "R029",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Hyperscaler net debt to EBITDA has risen but is close to zero"
  },
  {
    "figure_id": "F444",
    "report_id": "R029",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Sizing potential IG market issuance capacity"
  },
  {
    "figure_id": "F445",
    "report_id": "R029",
    "label": "Exhibit 13",
    "context": "Exhibit 13: Rapid price appreciation with low volatility in many pockets of AI infrastructure"
  },
  {
    "figure_id": "F446",
    "report_id": "R029",
    "label": "Exhibit 14",
    "context": "Exhibit 14: P/E of the median AI infrastructure stock had been range-bound until recently"
  },
  {
    "figure_id": "F447",
    "report_id": "R029",
    "label": "Exhibit 15",
    "context": "Exhibit 15: YTD change in earnings vs. price among AI infrastructure complex Median stock YTD change in 2-year ahead EPS vs. price"
  },
  {
    "figure_id": "F448",
    "report_id": "R029",
    "label": "Exhibit 16",
    "context": "Exhibit 16: Semiconductors returns outpaced earnings starting in late April"
  },
  {
    "figure_id": "F449",
    "report_id": "R029",
    "label": "Exhibit 17",
    "context": "Exhibit 17: Hyperscaler earnings have recently outpaced share price returns"
  },
  {
    "figure_id": "F450",
    "report_id": "R029",
    "label": "Exhibit 19",
    "context": "Exhibit 19: Cloud business revenues and margins Exhibit 20: Cloud companies' revenue expectations have been improving"
  },
  {
    "figure_id": "F451",
    "report_id": "R029",
    "label": "Exhibit 21",
    "context": "Exhibit 21: Public software companies remain well below their valuations from late 2025 Software = IGV"
  },
  {
    "figure_id": "F452",
    "report_id": "R029",
    "label": "Exhibit 22",
    "context": "Exhibit 22: Wide dispersion in Software returns YTD based on RBICS classifications within IGV, excludes industries with only two stocks"
  },
  {
    "figure_id": "F453",
    "report_id": "R029",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Estimated share of S&P 500 value in the “terminal value”"
  },
  {
    "figure_id": "F454",
    "report_id": "R029",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Growth vs. margins by sector sales growth = 30-year average, net profit margin = 5-year average"
  },
  {
    "figure_id": "F455",
    "report_id": "R029",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Company commentary on AI productivity during earnings season Share of S&P 500 firms discussing AI productivity on earnings calls"
  },
  {
    "figure_id": "F456",
    "report_id": "R031",
    "label": "Exhibit 1",
    "context": "EXHIBIT 1: May Taiwan import for SPE was \\$4.4bn, -8% MoM."
  },
  {
    "figure_id": "F457",
    "report_id": "R031",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: Likewise, May Taiwan SPE import from Japan was \\$700mn, -17% MoM."
  },
  {
    "figure_id": "F458",
    "report_id": "R031",
    "label": "Exhibit 4",
    "context": "EXHIBIT 3: May tester import from Japan and Malaysia collectively was \\$613mn, +7% MoM."
  },
  {
    "figure_id": "F459",
    "report_id": "R031",
    "label": "EXHIBIT 4",
    "context": "EXHIBIT 4: Taiwan tester imports data shows good directional correlation with Advantest's Taiwan sales."
  },
  {
    "figure_id": "F460",
    "report_id": "R031",
    "label": "EXHIBIT 5",
    "context": "EXHIBIT 5: Our regression analysis indicates JunQ Taiwan sales of +6% QoQ for Advantest. EXHIBIT 6: Advantest Taiwan sales show good correlation with Taiwan import data."
  },
  {
    "figure_id": "F461",
    "report_id": "R031",
    "label": "Exhibit 7",
    "context": "EXHIBIT 7: Monthly Taiwan litho Imports and ASML's Taiwan system sales divided by 3 have historically shown a quite solid correlation. April TW litho imports was €543mn, down 38% MoM from April but up 21% YoY versus May 2025."
  },
  {
    "figure_id": "F462",
    "report_id": "R031",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: TW's 2M litho import data shows a strong correlation with ASML's system sales in Taiwan, with an R $^{2}$ of 75%. Based on €1.42bn of TW litho imports in April and May, our regression estimates ASML's Taiwan system sales"
  },
  {
    "figure_id": "F463",
    "report_id": "R031",
    "label": "EXHIBIT 9",
    "context": "EXHIBIT 10: Based on our regression model, ASML TW system sales should reach €2.33bn in Q2, up 61% sequentially and 18% YoY. This would represent the second-strongest quarter on record for ASML TW system sales."
  },
  {
    "figure_id": "F464",
    "report_id": "R031",
    "label": "Exhibit 12",
    "context": "EXHIBIT 11: May import from Japan for WFE equipments where TEL has exposure was collectively -19% MoM."
  },
  {
    "figure_id": "F465",
    "report_id": "R031",
    "label": "EXHIBIT 12",
    "context": "EXHIBIT 12: Taiwan monthly SPE import from Japan shows good directional correlation with TEL's Taiwan revenue."
  },
  {
    "figure_id": "F466",
    "report_id": "R031",
    "label": "EXHIBIT 14",
    "context": "EXHIBIT 14: TEL Taiwan sales show decent correlation with Taiwan import data. TEL Quarterly Taiwan Sales vs. Taiwan 2M Import: 1QCY16-1QCY26"
  },
  {
    "figure_id": "F467",
    "report_id": "R031",
    "label": "Exhibit 16",
    "context": "EXHIBIT 15: May cleaning SPE import globally was \\$116mn, +11% MoM."
  },
  {
    "figure_id": "F468",
    "report_id": "R031",
    "label": "EXHIBIT 16",
    "context": "EXHIBIT 16: Taiwan cleaning SPE import shows directional correlation with Screen's Taiwan revenue."
  },
  {
    "figure_id": "F469",
    "report_id": "R031",
    "label": "EXHIBIT 18",
    "context": "EXHIBIT 18: Screen Taiwan sales show decent correlation with import data. Screen Quarterly Taiwan Sales vs. Taiwan 2M Import: 2QCY18-1QCY26"
  },
  {
    "figure_id": "F470",
    "report_id": "R034",
    "label": "Figure 2",
    "context": "Figure 2: Monthly total passenger-vehicle sales trend"
  },
  {
    "figure_id": "F471",
    "report_id": "R034",
    "label": "Figure 3",
    "context": "Figure 3: Monthly new-energy vehicle (NEV) passenger-vehicle sales trend"
  },
  {
    "figure_id": "F472",
    "report_id": "R034",
    "label": "Figure 4",
    "context": "Figure 4: Monthly NEV sales trend"
  },
  {
    "figure_id": "F473",
    "report_id": "R034",
    "label": "Figure 5",
    "context": "Figure 5: Monthly NEV penetration rate trend"
  },
  {
    "figure_id": "F474",
    "report_id": "R034",
    "label": "Figure 6",
    "context": "Figure 6: BYD monthly wholesale volume trend"
  },
  {
    "figure_id": "F475",
    "report_id": "R034",
    "label": "Figure 7",
    "context": "Figure 7: BYD market share trend"
  },
  {
    "figure_id": "F476",
    "report_id": "R034",
    "label": "Figure 8",
    "context": "Figure 8: Tesla China monthly wholesale volume trend"
  },
  {
    "figure_id": "F477",
    "report_id": "R034",
    "label": "Figure 9",
    "context": "Figure 9: Tesla China market share trend"
  },
  {
    "figure_id": "F478",
    "report_id": "R034",
    "label": "Figure 10",
    "context": "Figure 10: Li Auto monthly wholesale volume trend"
  },
  {
    "figure_id": "F479",
    "report_id": "R034",
    "label": "Figure 11",
    "context": "Figure 11: Li Auto market share trend"
  },
  {
    "figure_id": "F480",
    "report_id": "R034",
    "label": "Figure 12",
    "context": "Figure 12: NIO monthly wholesale volume trend"
  },
  {
    "figure_id": "F481",
    "report_id": "R034",
    "label": "Figure 13",
    "context": "Figure 13: NIO market share trend"
  },
  {
    "figure_id": "F482",
    "report_id": "R034",
    "label": "Figure 14",
    "context": "Figure 14: Xpeng monthly wholesale volume trend"
  },
  {
    "figure_id": "F483",
    "report_id": "R034",
    "label": "Figure 15",
    "context": "Figure 15: Xpeng market share trend"
  },
  {
    "figure_id": "F484",
    "report_id": "R034",
    "label": "Figure 16",
    "context": "Figure 16: Leapmotor monthly wholesale volume trend"
  },
  {
    "figure_id": "F485",
    "report_id": "R034",
    "label": "Figure 17",
    "context": "Figure 17: Leapmotor market share trend"
  },
  {
    "figure_id": "F486",
    "report_id": "R034",
    "label": "Figure 18",
    "context": "Figure 18: AITO monthly wholesale volume trend"
  },
  {
    "figure_id": "F487",
    "report_id": "R034",
    "label": "Figure 19",
    "context": "Figure 19: AITO market share trend"
  },
  {
    "figure_id": "F488",
    "report_id": "R034",
    "label": "Figure 20",
    "context": "Figure 20: Voyah monthly wholesale volume trend"
  },
  {
    "figure_id": "F489",
    "report_id": "R034",
    "label": "Figure 21",
    "context": "Figure 21: Voyah market share trend"
  },
  {
    "figure_id": "F490",
    "report_id": "R034",
    "label": "Figure 22",
    "context": "Figure 22: Xiaomi monthly wholesale volume trend"
  },
  {
    "figure_id": "F491",
    "report_id": "R034",
    "label": "Figure 23",
    "context": "Figure 23: Xiaomi market share trend"
  },
  {
    "figure_id": "F492",
    "report_id": "R034",
    "label": "Figure 24",
    "context": "Figure 24: Great Wall monthly wholesale volume trend"
  },
  {
    "figure_id": "F493",
    "report_id": "R034",
    "label": "Figure 25",
    "context": "Figure 25: Great Wall market share trend"
  },
  {
    "figure_id": "F494",
    "report_id": "R034",
    "label": "Figure 26",
    "context": "Figure 26: Geely monthly wholesale volume trend"
  },
  {
    "figure_id": "F495",
    "report_id": "R034",
    "label": "Figure 27",
    "context": "Figure 27: Geely market share trend"
  },
  {
    "figure_id": "F496",
    "report_id": "R034",
    "label": "Figure 28",
    "context": "Figure 28: Chery monthly wholesale volume trend"
  },
  {
    "figure_id": "F497",
    "report_id": "R034",
    "label": "Figure 29",
    "context": "Figure 29: Chery market share trend"
  },
  {
    "figure_id": "F498",
    "report_id": "R034",
    "label": "Figure 30",
    "context": "Figure 30: Dongfeng monthly wholesale volume trend"
  },
  {
    "figure_id": "F499",
    "report_id": "R034",
    "label": "Figure 31",
    "context": "Figure 31: Dongfeng market share trend"
  },
  {
    "figure_id": "F500",
    "report_id": "R034",
    "label": "Figure 32",
    "context": "Figure 32: GAC monthly wholesale volume trend"
  },
  {
    "figure_id": "F501",
    "report_id": "R034",
    "label": "Figure 33",
    "context": "Figure 33: GAC market share trend"
  },
  {
    "figure_id": "F502",
    "report_id": "R034",
    "label": "Figure 34",
    "context": "Figure 34: BAIC monthly wholesale volume trend"
  },
  {
    "figure_id": "F503",
    "report_id": "R034",
    "label": "Figure 35",
    "context": "Figure 35: BAIC market share trend"
  },
  {
    "figure_id": "F504",
    "report_id": "R034",
    "label": "Figure 36",
    "context": "Figure 36: Brilliance monthly wholesale volume trend"
  },
  {
    "figure_id": "F505",
    "report_id": "R034",
    "label": "Figure 37",
    "context": "Figure 37: Brilliance market share trend"
  },
  {
    "figure_id": "F506",
    "report_id": "R034",
    "label": "Figure 38",
    "context": "Figure 38: SAIC monthly wholesale volume trend"
  },
  {
    "figure_id": "F507",
    "report_id": "R034",
    "label": "Figure 39",
    "context": "Figure 39: SAIC market share trend"
  },
  {
    "figure_id": "F508",
    "report_id": "R034",
    "label": "Figure 40",
    "context": "Figure 40: Chang'an monthly wholesale volume trend"
  },
  {
    "figure_id": "F509",
    "report_id": "R034",
    "label": "Figure 41",
    "context": "Figure 41: Chang'an market share trend"
  },
  {
    "figure_id": "F510",
    "report_id": "R034",
    "label": "Figure 42",
    "context": "Figure 42: BMW monthly wholesale volume trend"
  },
  {
    "figure_id": "F511",
    "report_id": "R034",
    "label": "Figure 43",
    "context": "Figure 43: BMW market share trend"
  },
  {
    "figure_id": "F512",
    "report_id": "R034",
    "label": "Figure 44",
    "context": "Figure 44: Mercedes monthly wholesale volume trend"
  },
  {
    "figure_id": "F513",
    "report_id": "R034",
    "label": "Figure 45",
    "context": "Figure 45: Mercedes market share trend"
  },
  {
    "figure_id": "F514",
    "report_id": "R034",
    "label": "Figure 46",
    "context": "Figure 46: VW monthly wholesale volume trend 000 Unit"
  },
  {
    "figure_id": "F515",
    "report_id": "R034",
    "label": "Figure 47",
    "context": "Figure 47: VW market share trend"
  },
  {
    "figure_id": "F516",
    "report_id": "R034",
    "label": "Figure 48",
    "context": "Figure 48: Ford monthly wholesale volume trend"
  },
  {
    "figure_id": "F517",
    "report_id": "R034",
    "label": "Figure 49",
    "context": "Figure 49: Ford market share trend"
  },
  {
    "figure_id": "F518",
    "report_id": "R034",
    "label": "Figure 50",
    "context": "Figure 50: GM monthly wholesale volume trend"
  },
  {
    "figure_id": "F519",
    "report_id": "R034",
    "label": "Figure 51",
    "context": "Figure 51: GM market share trend"
  },
  {
    "figure_id": "F520",
    "report_id": "R034",
    "label": "Figure 52",
    "context": "Figure 52: Stellantis monthly wholesale volume trend"
  },
  {
    "figure_id": "F521",
    "report_id": "R034",
    "label": "Figure 53",
    "context": "Figure 53: Stellantis market share trend"
  },
  {
    "figure_id": "F522",
    "report_id": "R034",
    "label": "Figure 54",
    "context": "Figure 54: Hyundai-Kia monthly wholesale volume trend"
  },
  {
    "figure_id": "F523",
    "report_id": "R034",
    "label": "Figure 55",
    "context": "Figure 55: Hyundai-Kia market share trend"
  },
  {
    "figure_id": "F524",
    "report_id": "R034",
    "label": "Figure 56",
    "context": "Figure 56: Honda monthly wholesale volume trend"
  },
  {
    "figure_id": "F525",
    "report_id": "R034",
    "label": "Figure 57",
    "context": "Figure 57: Honda market share trend"
  },
  {
    "figure_id": "F526",
    "report_id": "R034",
    "label": "Figure 58",
    "context": "Figure 58: Nissan monthly wholesale volume trend"
  },
  {
    "figure_id": "F527",
    "report_id": "R034",
    "label": "Figure 59",
    "context": "Figure 59: Nissan market share trend"
  },
  {
    "figure_id": "F528",
    "report_id": "R034",
    "label": "Figure 60",
    "context": "Figure 60: Toyota monthly wholesale volume trend"
  },
  {
    "figure_id": "F529",
    "report_id": "R034",
    "label": "Figure 61",
    "context": "Figure 61: Toyota market share trend"
  },
  {
    "figure_id": "F530",
    "report_id": "R035",
    "label": "Figure 2",
    "context": "Figure 2: Weekly new orders trend of key automakers (Li, NIO, XPeng, Leap, Xiaomi, Tesla)"
  },
  {
    "figure_id": "F531",
    "report_id": "R035",
    "label": "Figure 2",
    "context": "Figure 2: Weekly new orders trend of key automakers (Li, NIO, XPeng, Leap, Xiaomi, Tesla)"
  },
  {
    "figure_id": "F532",
    "report_id": "R035",
    "label": "Figure 4",
    "context": "Figure 4: Weekly HIMA (mainly AITO) new orders trend"
  },
  {
    "figure_id": "F533",
    "report_id": "R035",
    "label": "Figure 5",
    "context": "Figure 5: Weekly Li Auto new orders trend"
  },
  {
    "figure_id": "F534",
    "report_id": "R035",
    "label": "Figure 6",
    "context": "Figure 6: Weekly NIO group new orders trend"
  },
  {
    "figure_id": "F535",
    "report_id": "R035",
    "label": "Figure 7",
    "context": "Figure 7: Weekly Tesla new orders trend"
  },
  {
    "figure_id": "F536",
    "report_id": "R035",
    "label": "Figure 8",
    "context": "Figure 8: Weekly Xiaomi new orders trend"
  },
  {
    "figure_id": "F537",
    "report_id": "R035",
    "label": "Figure 9",
    "context": "Figure 9: Weekly XPeng new orders trend"
  },
  {
    "figure_id": "F538",
    "report_id": "R036",
    "label": "Exhibit 1",
    "context": "Exhibit 1: Total bidding value of 9 main medical devices in China In Rmb, mn"
  },
  {
    "figure_id": "F539",
    "report_id": "R036",
    "label": "Exhibit 2",
    "context": "Exhibit 2: The YoY change rate of bidding value"
  },
  {
    "figure_id": "F540",
    "report_id": "R036",
    "label": "Exhibit 5",
    "context": "Exhibit 5: Patient monitor procurement value since Jan-23 Patient monitor"
  },
  {
    "figure_id": "F541",
    "report_id": "R036",
    "label": "Exhibit 6",
    "context": "Exhibit 6: Patient monitor procurement value decreased by -23% yoy in May-26 vs. +25% in Apr-26 Patient monitor"
  },
  {
    "figure_id": "F542",
    "report_id": "R036",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Endoscope procurement value since Jan-23 Endoscope"
  },
  {
    "figure_id": "F543",
    "report_id": "R036",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Endoscope procurement value decreased by -25% yoy in May-26 vs. -25% in Apr-26 Endoscope"
  },
  {
    "figure_id": "F544",
    "report_id": "R036",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Ultrasound procurement value since Jan-23 Ultrasound"
  },
  {
    "figure_id": "F545",
    "report_id": "R036",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Ultrasound procurement value decreased by $-20\\%$ in May-26 yoy vs. $-12\\%$ in Apr-26 Ultrasound"
  },
  {
    "figure_id": "F546",
    "report_id": "R036",
    "label": "Exhibit 11",
    "context": "Exhibit 11: CT scanner procurement value since Jan-23 CT"
  },
  {
    "figure_id": "F547",
    "report_id": "R036",
    "label": "Exhibit 12",
    "context": "Exhibit 12: CT scanner procurement value increased by +12% yoy in May-26 vs. -31% in Apr-26 CT"
  },
  {
    "figure_id": "F548",
    "report_id": "R036",
    "label": "Exhibit 13",
    "context": "Exhibit 13: MRI procurement value since Jan-23 MRI"
  },
  {
    "figure_id": "F549",
    "report_id": "R036",
    "label": "Exhibit 14",
    "context": "Exhibit 14: MRI procurement value increased by $+20\\%$ yoy in May-26 vs. $-50\\%$ in Apr-26 MRI"
  },
  {
    "figure_id": "F550",
    "report_id": "R036",
    "label": "Exhibit 15",
    "context": "Exhibit 15: PET-CT procurement value since Jan-23 PET-CT"
  },
  {
    "figure_id": "F551",
    "report_id": "R036",
    "label": "Exhibit 16",
    "context": "Exhibit 16: PET-CT procurement value decreased by $-33\\%$ yoy in May-26 vs. $-28\\%$ in Apr-26 PET-CT"
  },
  {
    "figure_id": "F552",
    "report_id": "R036",
    "label": "Exhibit 17",
    "context": "Exhibit 17: DR procurement value since Jan-23"
  },
  {
    "figure_id": "F553",
    "report_id": "R036",
    "label": "Exhibit 18",
    "context": "Exhibit 18: DR procurement value decreased by $-26\\%$ yoy in May-26 vs. $-13\\%$ in Apr-26 DR"
  },
  {
    "figure_id": "F554",
    "report_id": "R036",
    "label": "Exhibit 19",
    "context": "Exhibit 19: LINAC procurement value since Jan-23 LINAC"
  },
  {
    "figure_id": "F555",
    "report_id": "R036",
    "label": "Exhibit 20",
    "context": "Exhibit 20: LINAC procurement value increased by +109% yoy in May-26 vs. +24% in Apr-26 LINAC"
  },
  {
    "figure_id": "F556",
    "report_id": "R036",
    "label": "Exhibit 21",
    "context": "Exhibit 21: DSA (IGT) procurement value since Jan-23 DSA (IGT)"
  },
  {
    "figure_id": "F557",
    "report_id": "R036",
    "label": "Exhibit 22",
    "context": "Exhibit 22: DSA (IGT) procurement value decreased by -3% yoy in May-26 vs. -18% in Apr-26 DSA (IGT)"
  },
  {
    "figure_id": "F558",
    "report_id": "R036",
    "label": "Exhibit 23",
    "context": "Exhibit 23: Total bidding value of United Imaging since Jan-23 In Rmb, mn United Imaging"
  },
  {
    "figure_id": "F559",
    "report_id": "R036",
    "label": "Exhibit 24",
    "context": "Exhibit 24: Total bidding value of GEHC since Jan-23 In Rmb, mn GEHC"
  },
  {
    "figure_id": "F560",
    "report_id": "R036",
    "label": "Exhibit 25",
    "context": "Exhibit 25: Total bidding value of Philips since Jan-23 In Rmb, mn Philips"
  },
  {
    "figure_id": "F561",
    "report_id": "R036",
    "label": "Exhibit 26",
    "context": "Exhibit 26: Total bidding value of Siemens since Jan-23 In Rmb, mn Siemens"
  },
  {
    "figure_id": "F562",
    "report_id": "R036",
    "label": "Exhibit 27",
    "context": "Exhibit 27: Total bidding value of Elekta since Jan-23 In Rmb, mn Elekta"
  },
  {
    "figure_id": "F563",
    "report_id": "R036",
    "label": "Exhibit 28",
    "context": "Exhibit 28: Total bidding value of Mindray since Jan-23 In Rmb, mn Mindray"
  },
  {
    "figure_id": "F564",
    "report_id": "R036",
    "label": "Exhibit 29",
    "context": "Exhibit 29: Total bidding value of SonoScape since Jan-23 In Rmb, mn SonoScape"
  },
  {
    "figure_id": "F565",
    "report_id": "R036",
    "label": "Exhibit 30",
    "context": "Exhibit 30: Total bidding value of Olympus since Jan-23 In Rmb, mn Olympus"
  },
  {
    "figure_id": "F566",
    "report_id": "R036",
    "label": "Exhibit 31",
    "context": "Exhibit 31: Total bidding value of Aohua since Jan-23 In Rmb, mn Aohua"
  },
  {
    "figure_id": "F567",
    "report_id": "R039",
    "label": "Figure 1",
    "context": "Figure 1: Home appliance sector stocks under JPM coverage - share price performance vs China/HK index Indexed to Jun 5, 2026 = 100"
  },
  {
    "figure_id": "F568",
    "report_id": "R039",
    "label": "Figure 3",
    "context": "Figure 3: Global (ex-China) home appliance market size\\* and China Big 3's market share \\* Market size is based on ex-factory prices"
  },
  {
    "figure_id": "F569",
    "report_id": "R039",
    "label": "Figure 4",
    "context": "Figure 4: China home appliance market size\\* and China Big 3's market share \\* Market size is based on ex-factory prices"
  },
  {
    "figure_id": "F570",
    "report_id": "R039",
    "label": "Figure 5",
    "context": "Figure 5: EPS growth vs P/E multiple"
  },
  {
    "figure_id": "F571",
    "report_id": "R039",
    "label": "Figure 6",
    "context": "Figure 6: ROE vs total shareholder return"
  },
  {
    "figure_id": "F572",
    "report_id": "R039",
    "label": "Figure 7",
    "context": "Figure 7: China home appliance companies - revenue structure 2022"
  },
  {
    "figure_id": "F573",
    "report_id": "R039",
    "label": "Figure 8",
    "context": "Figure 8: China HA Big 3 - historical valuation"
  },
  {
    "figure_id": "F574",
    "report_id": "R039",
    "label": "Figure 9",
    "context": "Figure 9: Midea-A - historical valuation"
  },
  {
    "figure_id": "F575",
    "report_id": "R039",
    "label": "Figure 10",
    "context": "Figure 10: Haier-A - historical valuation"
  },
  {
    "figure_id": "F576",
    "report_id": "R039",
    "label": "Figure 11",
    "context": "Figure 11: Gree-A - historical valuation"
  },
  {
    "figure_id": "F577",
    "report_id": "R039",
    "label": "Figure 12",
    "context": "Figure 12: Home appliance sector stocks under JPM coverage - share price performance vs China/HK index Indexed to Jun 5, 2026 = 100"
  },
  {
    "figure_id": "F578",
    "report_id": "R039",
    "label": "Figure 13",
    "context": "Figure 13: China home appliances: Retail sales and YoY growth"
  },
  {
    "figure_id": "F579",
    "report_id": "R039",
    "label": "Figure 14",
    "context": "Figure 14: Global (ex-China) home appliance market size and revenue by brand"
  },
  {
    "figure_id": "F580",
    "report_id": "R039",
    "label": "Figure 15",
    "context": "Figure 15: China home appliance market size and revenue by brand"
  },
  {
    "figure_id": "F581",
    "report_id": "R039",
    "label": "Figure 16",
    "context": "Figure 16: China home appliance companies - revenue structure 2022"
  },
  {
    "figure_id": "F582",
    "report_id": "R039",
    "label": "Figure 17",
    "context": "Figure 17: CoGS structure - Midea, Haier and Gree (FY25, B2C only)"
  },
  {
    "figure_id": "F583",
    "report_id": "R039",
    "label": "Figure 18",
    "context": "Figure 18: CoGS structure - Robam, Supor and Ecovacs (FY25)"
  },
  {
    "figure_id": "F584",
    "report_id": "R039",
    "label": "Figure 19",
    "context": "Figure 19: Home appliance manufacturer cost index"
  },
  {
    "figure_id": "F585",
    "report_id": "R039",
    "label": "Figure 20",
    "context": "Figure 20: Cost trend by raw material"
  },
  {
    "figure_id": "F586",
    "report_id": "R039",
    "label": "Figure 21",
    "context": "## Our take 2Q26 to face the toughest comp. We believe 2Q26 will see the retail sales YoY trough (due to the high base consistently shown in the data from NBS, AVC and ChinaIOL), while 3Q-4Q26 should be more manageable (as this year's budget will be evenly dis"
  },
  {
    "figure_id": "F587",
    "report_id": "R039",
    "label": "Figure 22",
    "context": "Pull-forward demand = realized retail sales (as reported by NBS) - natural sales assuming no subsidy program (following historical average growth of 2% p.a.)"
  },
  {
    "figure_id": "F588",
    "report_id": "R039",
    "label": "Figure 24",
    "context": "Figure 23: Revenue (12 month rolling) growth YoY - Midea, Haier, Whirlpool and Electrolux"
  },
  {
    "figure_id": "F589",
    "report_id": "R039",
    "label": "Figure 26",
    "context": "Figure 26: US tariff rate on home appliances imported from China Figure 25: US inventory/sales ratio vs China export growth Figure 24: Net margin (12 month rolling) - Midea, Haier, Whirlpool and Electrolux"
  },
  {
    "figure_id": "F590",
    "report_id": "R039",
    "label": "Figure 27",
    "context": "Figure 27: China AC market share in the online channel"
  },
  {
    "figure_id": "F591",
    "report_id": "R039",
    "label": "Figure 28",
    "context": "Figure 28: China robot vacuum market share in the online channel"
  },
  {
    "figure_id": "F592",
    "report_id": "R039",
    "label": "Figure 29",
    "context": "Figure 29: Share price decomposition into forward P/E ratio and consensus forward EPS estimate"
  },
  {
    "figure_id": "F593",
    "report_id": "R039",
    "label": "Figure 29",
    "context": "Figure 29: Share price decomposition into forward P/E ratio and consensus forward EPS estimate"
  },
  {
    "figure_id": "F594",
    "report_id": "R039",
    "label": "Figure 30",
    "context": "Figure 30: 12M forward P/E correlation with 12M forward net earnings YoY% ## The comparative view Relative to the broader China/HK market, home appliance stocks offer an attractive quality-adjusted valuation. The sector's 2026 P/"
  },
  {
    "figure_id": "F595",
    "report_id": "R039",
    "label": "Figure 31",
    "context": "Figure 31: Consensus revenue revisions (2026E)"
  },
  {
    "figure_id": "F596",
    "report_id": "R039",
    "label": "Figure 32",
    "context": "Figure 32: Consensus earnings revisions (2026E)"
  },
  {
    "figure_id": "F597",
    "report_id": "R039",
    "label": "Figure 33",
    "context": "Figure 33: Revenue by region - Midea, Haier, Gree (FY25)"
  },
  {
    "figure_id": "F598",
    "report_id": "R039",
    "label": "Figure 34",
    "context": "Figure 34: Revenue by product - Midea, Haier, Gree (FY25)"
  },
  {
    "figure_id": "F599",
    "report_id": "R039",
    "label": "Figure 35",
    "context": "Figure 35: Revenue by region - Supor, Ecovacs, Robam (FY25)"
  },
  {
    "figure_id": "F600",
    "report_id": "R039",
    "label": "Figure 36",
    "context": "Figure 36: Revenue by product - Supor, Ecovacs, Robam (FY25)"
  },
  {
    "figure_id": "F601",
    "report_id": "R039",
    "label": "Figure 37",
    "context": "Figure 37: Revenue mix by product - Midea, Haier, Gree and industry (FY25)"
  },
  {
    "figure_id": "F602",
    "report_id": "R039",
    "label": "Figure 38",
    "context": "Figure 38: Revenue mix by region - Midea, Haier, Gree and industry (FY25)"
  },
  {
    "figure_id": "F603",
    "report_id": "R039",
    "label": "Figure 39",
    "context": "Figure 39: Revenue mix by product - Supor, Ecovacs, Robam and industry (FY25)"
  },
  {
    "figure_id": "F604",
    "report_id": "R039",
    "label": "Figure 40",
    "context": "Figure 40: Revenue mix by region - Supor, Ecovacs, Robam and industry (FY25)"
  },
  {
    "figure_id": "F605",
    "report_id": "R039",
    "label": "Figure 41",
    "context": "Figure 41: Midea - sales breakdown"
  },
  {
    "figure_id": "F606",
    "report_id": "R039",
    "label": "Figure 42",
    "context": "Figure 42: Midea - B2B sales breakdown"
  },
  {
    "figure_id": "F607",
    "report_id": "R039",
    "label": "Figure 43",
    "context": "Figure 43: Midea - B2B sales mix by region - all by JPMe (FY25)"
  },
  {
    "figure_id": "F608",
    "report_id": "R039",
    "label": "Figure 44",
    "context": "Figure 44: Midea - OP margin by segment - all by JPMe"
  },
  {
    "figure_id": "F609",
    "report_id": "R039",
    "label": "Figure 45",
    "context": "Figure 45: Midea - historical P/E band"
  },
  {
    "figure_id": "F610",
    "report_id": "R039",
    "label": "Figure 46",
    "context": "Figure 46: Haier - A share historical P/E band"
  },
  {
    "figure_id": "F611",
    "report_id": "R039",
    "label": "Figure 47",
    "context": "Figure 47: Haier - H share historical P/E band"
  },
  {
    "figure_id": "F612",
    "report_id": "R039",
    "label": "Figure 48",
    "context": "Figure 48: Haier - H share discount to the A share"
  },
  {
    "figure_id": "F613",
    "report_id": "R039",
    "label": "Figure 49",
    "context": "Figure 49: Gree - Historical P/E band"
  },
  {
    "figure_id": "F614",
    "report_id": "R039",
    "label": "Figure 50",
    "context": "Figure 50: Supor - Historical P/E band"
  },
  {
    "figure_id": "F615",
    "report_id": "R039",
    "label": "Figure 51",
    "context": "Figure 51: Ecovacs - historical P/E band"
  },
  {
    "figure_id": "F616",
    "report_id": "R039",
    "label": "Figure 52",
    "context": "Figure 52: Robam - Historical P/E band"
  },
  {
    "figure_id": "F617",
    "report_id": "R040",
    "label": "Figure 67",
    "context": "Figure 1: Tech ETF Outflows at All-Time-Highs Weekly flows in \\$B, as of Jun 10 $^{th}$"
  },
  {
    "figure_id": "F618",
    "report_id": "R040",
    "label": "Figure 2",
    "context": "Figure 2: Retail P&L in ETFs - Underperforming QQQ"
  },
  {
    "figure_id": "F619",
    "report_id": "R040",
    "label": "Figure 3",
    "context": "Figure 3: Retail P&L in Single Stocks - Recent Drawdown"
  },
  {
    "figure_id": "F620",
    "report_id": "R040",
    "label": "Figure 4",
    "context": "Figure 4: Crowding in Oil Sensitive Outperformers and Underperformers - persistent"
  },
  {
    "figure_id": "F621",
    "report_id": "R040",
    "label": "Figure 5",
    "context": "Figure 5: Retail Investor Daily Purchases by Stocks and ETFs"
  },
  {
    "figure_id": "F622",
    "report_id": "R040",
    "label": "Figure 6",
    "context": "Figure 6: Daily Retail Imbalance in USO"
  },
  {
    "figure_id": "F623",
    "report_id": "R040",
    "label": "Figure 7",
    "context": "Figure 7: Cumulative Retail Imbalance in USO"
  },
  {
    "figure_id": "F624",
    "report_id": "R040",
    "label": "Figure 8",
    "context": "Figure 8: Daily Retail Imbalance in BNO"
  },
  {
    "figure_id": "F625",
    "report_id": "R040",
    "label": "Figure 10",
    "context": "Figure 10: Daily Retail Imbalance in SCO"
  },
  {
    "figure_id": "F626",
    "report_id": "R040",
    "label": "Figure 9",
    "context": "Figure 9: Cumulative Retail Imbalance in BNO"
  },
  {
    "figure_id": "F627",
    "report_id": "R040",
    "label": "Figure 11",
    "context": "Figure 11: Cumulative Retail Imbalance in SCO"
  },
  {
    "figure_id": "F628",
    "report_id": "R040",
    "label": "Figure 14",
    "context": "Figure 14: Retail Single Stock Activity by Sector (\\$B) Activity is dominated by Tech and Cons. Disc. Retail Single Stocks Buying, by Sector (\\$B)"
  },
  {
    "figure_id": "F629",
    "report_id": "R040",
    "label": "Figure 13",
    "context": "Figure 13: Retail Cumulative Purchases in Mag 7 + PLTR (\\$B) Mag 7 + 1: Cumulative Retail Net Bought (\\$B)"
  },
  {
    "figure_id": "F630",
    "report_id": "R040",
    "label": "Figure 15",
    "context": "Figure 15: Retail ETF Activity by Themes Buying / Selling of ETFs aggregated by themes, in \\$B. Retail ETF Buying per ETF Style (\\$B)"
  },
  {
    "figure_id": "F631",
    "report_id": "R040",
    "label": "Figure 16",
    "context": "Figure 16: Retail Buying Pressure vs 3M Return of Stocks to Benefit from the FIFA World Cup"
  },
  {
    "figure_id": "F632",
    "report_id": "R040",
    "label": "Figure 17",
    "context": "Figure 17: Daily Retail Imbalance in HST"
  },
  {
    "figure_id": "F633",
    "report_id": "R040",
    "label": "Figure 18",
    "context": "Figure 18: Cumulative Retail Imbalance in HST"
  },
  {
    "figure_id": "F634",
    "report_id": "R040",
    "label": "Figure 19",
    "context": "Figure 19: Daily Retail Imbalance in H"
  },
  {
    "figure_id": "F635",
    "report_id": "R040",
    "label": "Figure 20",
    "context": "Figure 20: Cumulative Retail Imbalance in H"
  },
  {
    "figure_id": "F636",
    "report_id": "R040",
    "label": "Figure 21",
    "context": "Figure 21: Daily Retail Imbalance in ABNB"
  },
  {
    "figure_id": "F637",
    "report_id": "R040",
    "label": "Figure 22",
    "context": "Figure 22: Cumulative Retail Imbalance in ABNB"
  },
  {
    "figure_id": "F638",
    "report_id": "R040",
    "label": "Figure 23",
    "context": "Figure 23: Daily Retail Imbalance in BKNG"
  },
  {
    "figure_id": "F639",
    "report_id": "R040",
    "label": "Figure 25",
    "context": "Figure 25: Daily Retail Imbalance in UBER"
  },
  {
    "figure_id": "F640",
    "report_id": "R040",
    "label": "Figure 27",
    "context": "Figure 27: Daily Retail Imbalance in LYFT"
  },
  {
    "figure_id": "F641",
    "report_id": "R040",
    "label": "Figure 24",
    "context": "Figure 24: Cumulative Retail Imbalance in BKNG"
  },
  {
    "figure_id": "F642",
    "report_id": "R040",
    "label": "Figure 26",
    "context": "Figure 26: Cumulative Retail Imbalance in UBER"
  },
  {
    "figure_id": "F643",
    "report_id": "R040",
    "label": "Figure 28",
    "context": "Figure 28: Cumulative Retail Imbalance in LYFT"
  },
  {
    "figure_id": "F644",
    "report_id": "R040",
    "label": "Figure 29",
    "context": "Figure 29: Daily Retail Imbalance in DASH"
  },
  {
    "figure_id": "F645",
    "report_id": "R040",
    "label": "Figure 31",
    "context": "Figure 31: Daily Retail Imbalance in GOOGL"
  },
  {
    "figure_id": "F646",
    "report_id": "R040",
    "label": "Figure 33",
    "context": "Figure 33: Daily Retail Imbalance in META"
  },
  {
    "figure_id": "F647",
    "report_id": "R040",
    "label": "Figure 30",
    "context": "Figure 30: Cumulative Retail Imbalance in DASH"
  },
  {
    "figure_id": "F648",
    "report_id": "R040",
    "label": "Figure 32",
    "context": "Figure 32: Cumulative Retail Imbalance in GOOGL"
  },
  {
    "figure_id": "F649",
    "report_id": "R040",
    "label": "Figure 34",
    "context": "Figure 34: Cumulative Retail Imbalance in META"
  },
  {
    "figure_id": "F650",
    "report_id": "R040",
    "label": "Figure 35",
    "context": "Figure 35: Daily Retail Imbalance in MAR"
  },
  {
    "figure_id": "F651",
    "report_id": "R040",
    "label": "Figure 37",
    "context": "Figure 37: Daily Retail Imbalance in HLT"
  },
  {
    "figure_id": "F652",
    "report_id": "R040",
    "label": "Figure 39",
    "context": "Figure 39: Daily Retail Imbalance in FOXA"
  },
  {
    "figure_id": "F653",
    "report_id": "R040",
    "label": "Figure 36",
    "context": "Figure 36: Cumulative Retail Imbalance in MAR"
  },
  {
    "figure_id": "F654",
    "report_id": "R040",
    "label": "Figure 38",
    "context": "Figure 38: Cumulative Retail Imbalance in HLT"
  },
  {
    "figure_id": "F655",
    "report_id": "R040",
    "label": "Figure 40",
    "context": "Figure 40: Cumulative Retail Imbalance in FOXA"
  },
  {
    "figure_id": "F656",
    "report_id": "R040",
    "label": "Figure 41",
    "context": "Figure 41: Daily Retail Imbalance in OUT"
  },
  {
    "figure_id": "F657",
    "report_id": "R040",
    "label": "Figure 43",
    "context": "Figure 43: Daily Retail Imbalance in DKS"
  },
  {
    "figure_id": "F658",
    "report_id": "R040",
    "label": "Figure 45",
    "context": "Figure 45: Daily Retail Imbalance in BAC"
  },
  {
    "figure_id": "F659",
    "report_id": "R040",
    "label": "Figure 42",
    "context": "Figure 42: Cumulative Retail Imbalance in OUT"
  },
  {
    "figure_id": "F660",
    "report_id": "R040",
    "label": "Figure 44",
    "context": "Figure 44: Cumulative Retail Imbalance in DKS"
  },
  {
    "figure_id": "F661",
    "report_id": "R040",
    "label": "Figure 46",
    "context": "Figure 46: Cumulative Retail Imbalance in BAC"
  },
  {
    "figure_id": "F662",
    "report_id": "R040",
    "label": "Figure 47",
    "context": "Figure 47: Daily Retail Imbalance in VZ"
  },
  {
    "figure_id": "F663",
    "report_id": "R040",
    "label": "Figure 49",
    "context": "Figure 49: Daily Retail Imbalance in LUV"
  },
  {
    "figure_id": "F664",
    "report_id": "R040",
    "label": "Figure 51",
    "context": "Figure 51: Daily Retail Imbalance in BALL"
  },
  {
    "figure_id": "F665",
    "report_id": "R040",
    "label": "Figure 48",
    "context": "Figure 48: Cumulative Retail Imbalance in VZ"
  },
  {
    "figure_id": "F666",
    "report_id": "R040",
    "label": "Figure 50",
    "context": "Figure 50: Cumulative Retail Imbalance in LUV"
  },
  {
    "figure_id": "F667",
    "report_id": "R040",
    "label": "Figure 52",
    "context": "Figure 52: Cumulative Retail Imbalance in BALL"
  },
  {
    "figure_id": "F668",
    "report_id": "R040",
    "label": "Figure 53",
    "context": "Figure 53: Daily Retail Imbalance in YOU"
  },
  {
    "figure_id": "F669",
    "report_id": "R040",
    "label": "Figure 55",
    "context": "Figure 55: Daily Retail Imbalance in BUD"
  },
  {
    "figure_id": "F670",
    "report_id": "R040",
    "label": "Figure 57",
    "context": "Figure 57: Daily Retail Imbalance in LYV"
  },
  {
    "figure_id": "F671",
    "report_id": "R040",
    "label": "Figure 54",
    "context": "Figure 54: Cumulative Retail Imbalance in YOU"
  },
  {
    "figure_id": "F672",
    "report_id": "R040",
    "label": "Figure 56",
    "context": "Figure 56: Cumulative Retail Imbalance in BUD"
  },
  {
    "figure_id": "F673",
    "report_id": "R040",
    "label": "Figure 58",
    "context": "Figure 58: Cumulative Retail Imbalance in LYV"
  },
  {
    "figure_id": "F674",
    "report_id": "R040",
    "label": "Figure 59",
    "context": "Figure 59: Daily Retail Imbalance in TKO"
  },
  {
    "figure_id": "F675",
    "report_id": "R040",
    "label": "Figure 61",
    "context": "Figure 61: Daily Retail Imbalance in CMCSA"
  },
  {
    "figure_id": "F676",
    "report_id": "R040",
    "label": "Figure 63",
    "context": "Figure 63: Daily Retail Imbalance in KO"
  },
  {
    "figure_id": "F677",
    "report_id": "R040",
    "label": "Figure 60",
    "context": "Figure 60: Cumulative Retail Imbalance in TKO"
  },
  {
    "figure_id": "F678",
    "report_id": "R040",
    "label": "Figure 62",
    "context": "Figure 62: Cumulative Retail Imbalance in CMCSA"
  },
  {
    "figure_id": "F679",
    "report_id": "R040",
    "label": "Figure 64",
    "context": "Figure 64: Cumulative Retail Imbalance in KO"
  },
  {
    "figure_id": "F680",
    "report_id": "R040",
    "label": "Figure 65",
    "context": "Figure 65: Daily Retail Imbalance in WH"
  },
  {
    "figure_id": "F681",
    "report_id": "R040",
    "label": "Figure 67",
    "context": "Figure 67: Daily Retail Imbalance in MCD"
  },
  {
    "figure_id": "F682",
    "report_id": "R040",
    "label": "Figure 69",
    "context": "Figure 69: Daily Retail Imbalance in AXON"
  },
  {
    "figure_id": "F683",
    "report_id": "R040",
    "label": "Figure 66",
    "context": "Figure 66: Cumulative Retail Imbalance in WH"
  },
  {
    "figure_id": "F684",
    "report_id": "R040",
    "label": "Figure 68",
    "context": "Figure 68: Cumulative Retail Imbalance in MCD"
  },
  {
    "figure_id": "F685",
    "report_id": "R040",
    "label": "Figure 70",
    "context": "Figure 70: Cumulative Retail Imbalance in AXON"
  },
  {
    "figure_id": "F686",
    "report_id": "R040",
    "label": "Figure 71",
    "context": "Figure 71: Daily Retail Imbalance in LAMR"
  },
  {
    "figure_id": "F687",
    "report_id": "R040",
    "label": "Figure 73",
    "context": "Figure 73: Daily Retail Imbalance in MGM"
  },
  {
    "figure_id": "F688",
    "report_id": "R040",
    "label": "Figure 75",
    "context": "Figure 75: Daily Retail Imbalance in UAL"
  },
  {
    "figure_id": "F689",
    "report_id": "R040",
    "label": "Figure 72",
    "context": "Figure 72: Cumulative Retail Imbalance in LAMR"
  },
  {
    "figure_id": "F690",
    "report_id": "R040",
    "label": "Figure 74",
    "context": "Figure 74: Cumulative Retail Imbalance in MGM"
  },
  {
    "figure_id": "F691",
    "report_id": "R040",
    "label": "Figure 76",
    "context": "Figure 76: Cumulative Retail Imbalance in UAL"
  },
  {
    "figure_id": "F692",
    "report_id": "R040",
    "label": "Figure 77",
    "context": "Figure 77: Daily Retail Imbalance in DAL"
  },
  {
    "figure_id": "F693",
    "report_id": "R040",
    "label": "Figure 78",
    "context": "Figure 78: Cumulative Retail Imbalance in DAL"
  },
  {
    "figure_id": "F694",
    "report_id": "R040",
    "label": "Figure 79",
    "context": "Figure 79: Daily Retail Imbalance in NKE"
  },
  {
    "figure_id": "F695",
    "report_id": "R040",
    "label": "Figure 80",
    "context": "Figure 80: Cumulative Retail Imbalance in NKE"
  },
  {
    "figure_id": "F696",
    "report_id": "R040",
    "label": "Figure 81",
    "context": "Figure 81: Daily Retail Imbalance in V"
  },
  {
    "figure_id": "F697",
    "report_id": "R040",
    "label": "Figure 82",
    "context": "Figure 82: Cumulative Retail Imbalance in V"
  },
  {
    "figure_id": "F698",
    "report_id": "R040",
    "label": "Figure 83",
    "context": "Figure 83: Daily Retail Imbalance in AAL"
  },
  {
    "figure_id": "F699",
    "report_id": "R040",
    "label": "Figure 84",
    "context": "Figure 84: Cumulative Retail Imbalance in AAL"
  },
  {
    "figure_id": "F700",
    "report_id": "R040",
    "label": "Figure 85",
    "context": "Figure 85: Daily Retail Imbalance in EXPE"
  },
  {
    "figure_id": "F701",
    "report_id": "R040",
    "label": "Figure 86",
    "context": "Figure 86: Cumulative Retail Imbalance in EXPE"
  },
  {
    "figure_id": "F702",
    "report_id": "R040",
    "label": "Figure 87",
    "context": "Figure 87: Daily Retail Imbalance in PSN"
  },
  {
    "figure_id": "F703",
    "report_id": "R040",
    "label": "Figure 88",
    "context": "Figure 88: Cumulative Retail Imbalance in PSN"
  },
  {
    "figure_id": "F704",
    "report_id": "R040",
    "label": "Figure 89",
    "context": "Figure 89: Daily Retail Imbalance in DKNG"
  },
  {
    "figure_id": "F705",
    "report_id": "R040",
    "label": "Figure 90",
    "context": "Figure 90: Cumulative Retail Imbalance in DKNG"
  },
  {
    "figure_id": "F706",
    "report_id": "R040",
    "label": "Figure 91",
    "context": "Figure 91: Daily Retail Imbalance in CAR"
  },
  {
    "figure_id": "F707",
    "report_id": "R040",
    "label": "Figure 92",
    "context": "Figure 92: Cumulative Retail Imbalance in CAR"
  },
  {
    "figure_id": "F708",
    "report_id": "R040",
    "label": "Figure 93",
    "context": "Figure 93: Daily Retail Imbalance in FLUT"
  },
  {
    "figure_id": "F709",
    "report_id": "R040",
    "label": "Figure 94",
    "context": "Figure 94: Cumulative Retail Imbalance in FLUT"
  },
  {
    "figure_id": "F710",
    "report_id": "R040",
    "label": "Figure 95",
    "context": "Figure 95: Daily Retail Imbalance in VSNT"
  },
  {
    "figure_id": "F711",
    "report_id": "R040",
    "label": "Figure 96",
    "context": "Figure 96: Cumulative Retail Imbalance in VSNT"
  },
  {
    "figure_id": "F712",
    "report_id": "R040",
    "label": "Figure 98",
    "context": "Figure 98: Increasing Squeeze Risk in Meme Stocks: Retail Buying in High Short Interest Names Positive Slope = Opposite Positioning (Heightened Risk of Short Squeeze or Retail Losses); Negative Slope = Similar Positioning (Diffusin"
  },
  {
    "figure_id": "F713",
    "report_id": "R040",
    "label": "Figure 99",
    "context": "Figure 99: Retail Activity in CELH"
  },
  {
    "figure_id": "F714",
    "report_id": "R040",
    "label": "Figure 100",
    "context": "Figure 100: Retail Activity in PENG"
  },
  {
    "figure_id": "F715",
    "report_id": "R040",
    "label": "Figure 101",
    "context": "Figure 101: Retail Activity in SNBR"
  },
  {
    "figure_id": "F716",
    "report_id": "R040",
    "label": "Figure 102",
    "context": "Figure 102: Top 40 Equities with Most Delta Bought (in \\$Mn)"
  },
  {
    "figure_id": "F717",
    "report_id": "R040",
    "label": "Figure 103",
    "context": "Figure 103: Top 40 Equities with Most Delta Sold (in \\$Mn)"
  },
  {
    "figure_id": "F718",
    "report_id": "R040",
    "label": "Figure 104",
    "context": "Figure 104: Top 40 Equities with Most Gamma Bought (in \\$Mn)"
  },
  {
    "figure_id": "F719",
    "report_id": "R040",
    "label": "Figure 105",
    "context": "Figure 105: Top 40 Equities with Most Gamma Sold (in \\$Mn)"
  },
  {
    "figure_id": "F720",
    "report_id": "R040",
    "label": "Figure 106",
    "context": "Figure 106: Daily Retail Imbalance in COO"
  },
  {
    "figure_id": "F721",
    "report_id": "R040",
    "label": "Figure 107",
    "context": "Figure 107: Cumulative Retail Imbalance in COO"
  },
  {
    "figure_id": "F722",
    "report_id": "R040",
    "label": "Figure 108",
    "context": "Figure 108: Daily Retail Imbalance in PODD"
  },
  {
    "figure_id": "F723",
    "report_id": "R040",
    "label": "Figure 109",
    "context": "Figure 109: Cumulative Retail Imbalance in PODD"
  },
  {
    "figure_id": "F724",
    "report_id": "R040",
    "label": "Figure 110",
    "context": "Figure 110: Daily Retail Imbalance in HUM"
  },
  {
    "figure_id": "F725",
    "report_id": "R040",
    "label": "Figure 112",
    "context": "Figure 112: Daily Retail Imbalance in BAX"
  },
  {
    "figure_id": "F726",
    "report_id": "R040",
    "label": "Figure 114",
    "context": "Figure 114: Daily Retail Imbalance in CAH"
  },
  {
    "figure_id": "F727",
    "report_id": "R040",
    "label": "Figure 111",
    "context": "Figure 111: Cumulative Retail Imbalance in HUM"
  },
  {
    "figure_id": "F728",
    "report_id": "R040",
    "label": "Figure 113",
    "context": "Figure 113: Cumulative Retail Imbalance in BAX"
  },
  {
    "figure_id": "F729",
    "report_id": "R040",
    "label": "Figure 115",
    "context": "Figure 115: Cumulative Retail Imbalance in CAH"
  },
  {
    "figure_id": "F730",
    "report_id": "R040",
    "label": "Figure 116",
    "context": "Figure 116: Daily Retail Imbalance in SJM"
  },
  {
    "figure_id": "F731",
    "report_id": "R040",
    "label": "Figure 117",
    "context": "Figure 117: Cumulative Retail Imbalance in SJM"
  },
  {
    "figure_id": "F732",
    "report_id": "R040",
    "label": "Figure 118",
    "context": "Figure 118: Daily Retail Imbalance in CLX"
  },
  {
    "figure_id": "F733",
    "report_id": "R040",
    "label": "Figure 119",
    "context": "Figure 119: Cumulative Retail Imbalance in CLX"
  },
  {
    "figure_id": "F734",
    "report_id": "R040",
    "label": "Figure 120",
    "context": "Figure 120: Daily Retail Imbalance in CASY"
  },
  {
    "figure_id": "F735",
    "report_id": "R040",
    "label": "Figure 121",
    "context": "Figure 121: Cumulative Retail Imbalance in CASY"
  },
  {
    "figure_id": "F736",
    "report_id": "R040",
    "label": "Figure 122",
    "context": "Figure 122: Daily Retail Imbalance in CPB"
  },
  {
    "figure_id": "F737",
    "report_id": "R040",
    "label": "Figure 124",
    "context": "Figure 124: Daily Retail Imbalance in CIEN"
  },
  {
    "figure_id": "F738",
    "report_id": "R040",
    "label": "Figure 126",
    "context": "Figure 126: Daily Retail Imbalance in SMCI"
  },
  {
    "figure_id": "F739",
    "report_id": "R040",
    "label": "Figure 123",
    "context": "Figure 123: Cumulative Retail Imbalance in CPB"
  },
  {
    "figure_id": "F740",
    "report_id": "R040",
    "label": "Figure 125",
    "context": "Figure 125: Cumulative Retail Imbalance in CIEN"
  },
  {
    "figure_id": "F741",
    "report_id": "R040",
    "label": "Figure 127",
    "context": "Figure 127: Cumulative Retail Imbalance in SMCI"
  },
  {
    "figure_id": "F742",
    "report_id": "R040",
    "label": "Figure 128",
    "context": "Figure 128: Daily Retail Imbalance in AVGO"
  },
  {
    "figure_id": "F743",
    "report_id": "R040",
    "label": "Figure 130",
    "context": "Figure 130: Daily Retail Imbalance in QCOM"
  },
  {
    "figure_id": "F744",
    "report_id": "R040",
    "label": "Figure 132",
    "context": "Figure 132: Daily Retail Imbalance in FSLR"
  },
  {
    "figure_id": "F745",
    "report_id": "R040",
    "label": "Figure 129",
    "context": "Figure 129: Cumulative Retail Imbalance in AVGO"
  },
  {
    "figure_id": "F746",
    "report_id": "R040",
    "label": "Figure 131",
    "context": "Figure 131: Cumulative Retail Imbalance in QCOM"
  },
  {
    "figure_id": "F747",
    "report_id": "R040",
    "label": "Figure 133",
    "context": "Figure 133: Cumulative Retail Imbalance in FSLR"
  },
  {
    "figure_id": "F748",
    "report_id": "R040",
    "label": "Figure 134",
    "context": "Figure 134: Daily Retail Imbalance in WDC"
  },
  {
    "figure_id": "F749",
    "report_id": "R040",
    "label": "Figure 136",
    "context": "Figure 136: Daily Retail Imbalance in ON"
  },
  {
    "figure_id": "F750",
    "report_id": "R040",
    "label": "Figure 138",
    "context": "Figure 138: Daily Retail Imbalance in MU"
  },
  {
    "figure_id": "F751",
    "report_id": "R040",
    "label": "Figure 135",
    "context": "Figure 135: Cumulative Retail Imbalance in WDC"
  },
  {
    "figure_id": "F752",
    "report_id": "R040",
    "label": "Figure 137",
    "context": "Figure 137: Cumulative Retail Imbalance in ON"
  },
  {
    "figure_id": "F753",
    "report_id": "R040",
    "label": "Figure 139",
    "context": "Figure 139: Cumulative Retail Imbalance in MU"
  },
  {
    "figure_id": "F754",
    "report_id": "R040",
    "label": "Figure 140",
    "context": "Figure 140: Retail Options Trading Share"
  },
  {
    "figure_id": "F755",
    "report_id": "R040",
    "label": "Figure 142",
    "context": "Figure 142: Retail Options Volume (Calls and Puts), Information Technology"
  },
  {
    "figure_id": "F756",
    "report_id": "R040",
    "label": "Figure 144",
    "context": "Figure 144: Retail Options Volume (Calls and Puts), Health Care"
  },
  {
    "figure_id": "F757",
    "report_id": "R040",
    "label": "Figure 141",
    "context": "Figure 141: Retail Options Volume (Calls and Puts)"
  },
  {
    "figure_id": "F758",
    "report_id": "R040",
    "label": "Figure 143",
    "context": "Figure 143: Retail Options Volume (Calls and Puts), Communication Services"
  },
  {
    "figure_id": "F759",
    "report_id": "R040",
    "label": "Figure 145",
    "context": "Figure 145: Retail Options Volume (Calls and Puts), Financials"
  },
  {
    "figure_id": "F760",
    "report_id": "R040",
    "label": "Figure 146",
    "context": "Figure 146: Retail Options Volume (Calls and Puts), Discretionary"
  },
  {
    "figure_id": "F761",
    "report_id": "R040",
    "label": "Figure 147",
    "context": "Figure 147: Retail Options Volume (Calls and Puts), Staples"
  },
  {
    "figure_id": "F762",
    "report_id": "R040",
    "label": "Figure 148",
    "context": "Figure 148: Retail Options Volume (Calls and Puts), Energy"
  },
  {
    "figure_id": "F763",
    "report_id": "R040",
    "label": "Figure 149",
    "context": "Figure 149: Retail Options Volume (Calls and Puts), Materials"
  },
  {
    "figure_id": "F764",
    "report_id": "R040",
    "label": "Figure 150",
    "context": "Figure 150: Retail Brokerage Volume Hit Record \\~37% in January 2021"
  },
  {
    "figure_id": "F765",
    "report_id": "R040",
    "label": "Figure 151",
    "context": "Figure 151: NYSE Margin Account – Monthly Net Debit Balance Change \\$ in Billions, Net Debit balance equals margin debit balance less total credit balances"
  },
  {
    "figure_id": "F766",
    "report_id": "R041",
    "label": "Figure 3",
    "context": "Figure 1 - Pop Mart Labubu 1.0 second-hand price in mainland China"
  },
  {
    "figure_id": "F767",
    "report_id": "R041",
    "label": "Figure 2",
    "context": "Figure 2 - Pop Mart Instagram Interaction Index"
  },
  {
    "figure_id": "F768",
    "report_id": "R041",
    "label": "Figure 4",
    "context": "Figure 4 - Pop Mart eCommerce sales Pop Mart"
  },
  {
    "figure_id": "F769",
    "report_id": "R041",
    "label": "Figure 6",
    "context": "Figure 6 - Kayou eCommerce sales Kayou"
  },
  {
    "figure_id": "F770",
    "report_id": "R041",
    "label": "Figure 8",
    "context": "Figure 8 - Top Toy eCommerce sales"
  },
  {
    "figure_id": "F771",
    "report_id": "R041",
    "label": "Figure 5",
    "context": "Figure 5 - Bloks eCommerce sales Bloks"
  },
  {
    "figure_id": "F772",
    "report_id": "R041",
    "label": "Figure 7",
    "context": "Figure 7 - 52 Toys eCommerce sales 52 Toys"
  },
  {
    "figure_id": "F773",
    "report_id": "R041",
    "label": "Figure 9",
    "context": "Figure 9 - Miniso eCommerce sales"
  },
  {
    "figure_id": "F774",
    "report_id": "R041",
    "label": "Figure 10",
    "context": "Figure 10 - Pop Mart Labubu 1.0 second-hand price in mainland China"
  },
  {
    "figure_id": "F775",
    "report_id": "R041",
    "label": "Figure 12",
    "context": "Figure 12 - Pop Mart Twinkle Twinkle plush series second-hand price Figure 11 - Pop Mart Labubu x Sanrio second-hand price in mainland China Figure 13 - Pop Mart Pucky plush series second-hand price"
  },
  {
    "figure_id": "F776",
    "report_id": "R041",
    "label": "Figure 12",
    "context": "Figure 12 - Pop Mart Twinkle Twinkle plush series second-hand price Figure 11 - Pop Mart Labubu x Sanrio second-hand price in mainland China Figure 13 - Pop Mart Pucky plush series second-hand price Figure 14 - Most wanted IPs"
  },
  {
    "figure_id": "F777",
    "report_id": "R041",
    "label": "Figure 12",
    "context": "Figure 12 - Pop Mart Twinkle Twinkle plush series second-hand price Figure 11 - Pop Mart Labubu x Sanrio second-hand price in mainland China Figure 13 - Pop Mart Pucky plush series second-hand price Figure 14 - Most wanted IPs"
  },
  {
    "figure_id": "F778",
    "report_id": "R041",
    "label": "Figure 15",
    "context": "Figure 15 - Pop Mart TikTok Interaction Index"
  },
  {
    "figure_id": "F779",
    "report_id": "R041",
    "label": "Figure 17",
    "context": "Figure 17 - Pop Mart Facebook Interaction Index"
  },
  {
    "figure_id": "F780",
    "report_id": "R041",
    "label": "Figure 19",
    "context": "Figure 19 - Pop Mart official accounts' followers on TikTok"
  },
  {
    "figure_id": "F781",
    "report_id": "R041",
    "label": "Figure 21",
    "context": "Figure 21 - Pop Mart app's active users"
  },
  {
    "figure_id": "F782",
    "report_id": "R041",
    "label": "Figure 16",
    "context": "Figure 16 - Pop Mart Instagram Interaction Index"
  },
  {
    "figure_id": "F783",
    "report_id": "R041",
    "label": "Figure 18",
    "context": "Figure 18 - Pop Mart share price vs social media engagement"
  },
  {
    "figure_id": "F784",
    "report_id": "R041",
    "label": "Figure 20",
    "context": "Figure 20 - Pop Mart official accounts' followers on Instagram"
  },
  {
    "figure_id": "F785",
    "report_id": "R041",
    "label": "Figure 22",
    "context": "Figure 22 - Pop Mart app's active users - Asian countries more resilient"
  },
  {
    "figure_id": "F786",
    "report_id": "R041",
    "label": "Figure 23",
    "context": "Figure 23 - Popmart website visits from worldwide and the US"
  },
  {
    "figure_id": "F787",
    "report_id": "R041",
    "label": "Figure 25",
    "context": "Figure 25 - Google search trends for Pop Mart and Labubu – Worldwide"
  },
  {
    "figure_id": "F788",
    "report_id": "R041",
    "label": "Figure 27",
    "context": "Figure 27 - Google search trends for Pop Mart and Labubu - Japan"
  },
  {
    "figure_id": "F789",
    "report_id": "R041",
    "label": "Figure 29",
    "context": "Figure 29 - Google search trends for Pop Mart and Labubu - France"
  },
  {
    "figure_id": "F790",
    "report_id": "R041",
    "label": "Figure 24",
    "context": "Figure 24 - Sanrio website visits"
  },
  {
    "figure_id": "F791",
    "report_id": "R041",
    "label": "Figure 26",
    "context": "Figure 26 - Google search trends for Pop Mart and Labubu - Thailand"
  },
  {
    "figure_id": "F792",
    "report_id": "R041",
    "label": "Figure 28",
    "context": "Figure 28 - Google search trends for Pop Mart and Labubu - the US"
  },
  {
    "figure_id": "F793",
    "report_id": "R041",
    "label": "Figure 30",
    "context": "Figure 30 - Google search trends for Pop Mart and Labubu - Italy"
  },
  {
    "figure_id": "F794",
    "report_id": "R041",
    "label": "Figure 31",
    "context": "Figure 31 - Pop Mart blind box launches"
  },
  {
    "figure_id": "F795",
    "report_id": "R041",
    "label": "Figure 32",
    "context": "Figure 32 - Bloks product launches by IP"
  },
  {
    "figure_id": "F796",
    "report_id": "R041",
    "label": "Figure 33",
    "context": "Figure 33 - LTM performance"
  },
  {
    "figure_id": "F797",
    "report_id": "R041",
    "label": "Figure 34",
    "context": "Figure 34 - YTD share performance of IP toys related names 2026YTD"
  },
  {
    "figure_id": "F798",
    "report_id": "R042",
    "label": "Exhibit 1",
    "context": "Exhibit 1: DRAM Stocks vs. 200-Day Moving Average"
  },
  {
    "figure_id": "F799",
    "report_id": "R042",
    "label": "Exhibit 2",
    "context": "Exhibit 2: DRAM Stocks: Major sell-offs through the rally"
  },
  {
    "figure_id": "F800",
    "report_id": "R042",
    "label": "Exhibit 4",
    "context": "Exhibit 4: Long-Term DRAM cycle YoY chart"
  },
  {
    "figure_id": "F801",
    "report_id": "R042",
    "label": "Exhibit 5",
    "context": "Exhibit 5: AI vs. Dot.com: NASDAQ Performance from the Technology's arriva"
  },
  {
    "figure_id": "F802",
    "report_id": "R042",
    "label": "Exhibit 6",
    "context": "Exhibit 6: We estimate the Agentic CPU TAM to grow at a 251% CAGR from FY26 to FY30"
  },
  {
    "figure_id": "F803",
    "report_id": "R042",
    "label": "Exhibit 7",
    "context": "Exhibit 7: We estimate incremental DRAM demand to reach \\~221EB as orchestration CPU racks scale Bull case"
  },
  {
    "figure_id": "F804",
    "report_id": "R042",
    "label": "Exhibit 8",
    "context": "Exhibit 8: NTM consensus EPS trend over last 1 year"
  },
  {
    "figure_id": "F805",
    "report_id": "R042",
    "label": "Exhibit 9",
    "context": "Exhibit 9: Memory's earnings revision breadth since 2018"
  },
  {
    "figure_id": "F806",
    "report_id": "R042",
    "label": "Exhibit 10",
    "context": "Exhibit 10: DRAM inventory"
  },
  {
    "figure_id": "F807",
    "report_id": "R042",
    "label": "Exhibit 11",
    "context": "Exhibit 11: NAND inventory"
  },
  {
    "figure_id": "F808",
    "report_id": "R042",
    "label": "Exhibit 12",
    "context": "Exhibit 12: DRAM Capex (US\\$ mn)"
  },
  {
    "figure_id": "F809",
    "report_id": "R042",
    "label": "Exhibit 13",
    "context": "Exhibit 13: NAND Capex (US\\$ mn)"
  },
  {
    "figure_id": "F810",
    "report_id": "R042",
    "label": "Exhibit 14",
    "context": "Exhibit 14: DRAM in the context of the semiconductor cycle – revenue YoY is highly correlated for memory with DRAM at a more advanced stage relative to NAND"
  },
  {
    "figure_id": "F811",
    "report_id": "R044",
    "label": "Exhibit 1",
    "context": "Exhibit 1: China's finished steel net exports increased 10% MoM (day-adjusted) in May Steel net exports from China"
  },
  {
    "figure_id": "F812",
    "report_id": "R044",
    "label": "Exhibit 2",
    "context": "Exhibit 2: China steel trade data Exhibit 3: China finished steel net exports Steel net exports from China"
  },
  {
    "figure_id": "F813",
    "report_id": "R044",
    "label": "Exhibit 4",
    "context": "Exhibit 4: China finished steel gross exports to EU28 Steel Gross Exports from China to EU-28"
  },
  {
    "figure_id": "F814",
    "report_id": "R044",
    "label": "Exhibit5",
    "context": "Exhibit5: Price spreads: EU HRC less China HRC"
  },
  {
    "figure_id": "F815",
    "report_id": "R044",
    "label": "Exhibit6",
    "context": "Exhibit6: Spreads: EU HRC gross profit per tonne\\*"
  },
  {
    "figure_id": "F816",
    "report_id": "R044",
    "label": "Exhibit 7",
    "context": "Exhibit 7: Monthly steel imports to EU from all destinations"
  },
  {
    "figure_id": "F817",
    "report_id": "R044",
    "label": "Exhibit 8",
    "context": "Exhibit 8: Monthly steel imports to US from all destinations"
  },
  {
    "figure_id": "F818",
    "report_id": "R044",
    "label": "Exhibit 9",
    "context": "Exhibit 9: India's monthly steel imports/exports"
  },
  {
    "figure_id": "F819",
    "report_id": "R044",
    "label": "Exhibit 10",
    "context": "Exhibit 10: Russia's monthly steel imports/exports"
  },
  {
    "figure_id": "F820",
    "report_id": "R044",
    "label": "Exhibit 11",
    "context": "Exhibit 11: Turkey's monthly steel imports/exports"
  },
  {
    "figure_id": "F821",
    "report_id": "R044",
    "label": "Exhibit 13",
    "context": "Exhibit 13: EU total steel imports by geography – Turkey, S. Korea, China and Vietnam dominate"
  },
  {
    "figure_id": "F822",
    "report_id": "R044",
    "label": "Exhibit 15",
    "context": "Exhibit 15: EU imports from China (cold rolled sheet) – sharp declines following AD"
  },
  {
    "figure_id": "F823",
    "report_id": "R044",
    "label": "Exhibit 12",
    "context": "Exhibit 12: Vietnam's monthly steel imports/exports"
  },
  {
    "figure_id": "F824",
    "report_id": "R044",
    "label": "Exhibit 14",
    "context": "Exhibit 14: China's steel exports by geography, showing significant fragmentation of recipients China Steel Exports 2026 YTD"
  },
  {
    "figure_id": "F825",
    "report_id": "R044",
    "label": "Exhibit 16",
    "context": "Exhibit 16: EU imports from China (hot dipped) – at low level"
  },
  {
    "figure_id": "F826",
    "report_id": "R044",
    "label": "Exhibit 17",
    "context": "Exhibit 17: EU imports from China (hot rolled wide strip) – impact of AD driving lower"
  },
  {
    "figure_id": "F827",
    "report_id": "R044",
    "label": "Exhibit 18",
    "context": "Exhibit 18: EU imports from China (quarto plate) – impact of AD driving lower"
  },
  {
    "figure_id": "F828",
    "report_id": "R046",
    "label": "Figure 2",
    "context": "Figure 3: Key Chart - Value Performance Isn't Priced for a BoJ Rate Hike"
  },
  {
    "figure_id": "F829",
    "report_id": "R046",
    "label": "Figure 5",
    "context": "Figure 5: Japan QMI since 2010"
  },
  {
    "figure_id": "F830",
    "report_id": "R046",
    "label": "Figure 6",
    "context": "Figure 6: Japan QMI State Positions for the Past 1 Year ```mermaid graph TD"
  },
  {
    "figure_id": "F831",
    "report_id": "R046",
    "label": "Figure 8",
    "context": "Figure 8: Japan QMI and EPS Revision index (MXJP)"
  },
  {
    "figure_id": "F832",
    "report_id": "R046",
    "label": "Figure 9",
    "context": "Figure 9: Japan QMI and US Capital Goods Shipments"
  },
  {
    "figure_id": "F833",
    "report_id": "R046",
    "label": "Figure 11",
    "context": "Figure 11: Top Performer Last Month – Momentum"
  },
  {
    "figure_id": "F834",
    "report_id": "R046",
    "label": "Figure 13",
    "context": "Figure 13: Worst Performer Last Month –Low Vol (Low vs. High Volatility)"
  },
  {
    "figure_id": "F835",
    "report_id": "R046",
    "label": "Figure 12",
    "context": "Figure 12: Second-best Performer Last Month –Size (L-S)"
  },
  {
    "figure_id": "F836",
    "report_id": "R046",
    "label": "Figure 14",
    "context": "Figure 14: Second-worst Performer Last Month –Q-scores(Multi-factor model)"
  },
  {
    "figure_id": "F837",
    "report_id": "R046",
    "label": "Figure 15",
    "context": "Figure 15: P/B Spread of Momentum (High vs. Low Return) The Y axis is P/B that is Z-Scored and flipped – the higher the Z-score, the cheaper the L/S portfolio is on P/B."
  },
  {
    "figure_id": "F838",
    "report_id": "R046",
    "label": "Figure 16",
    "context": "Figure 16: P/B Spread of Size (Large vs. SMid caps) The Y axis is P/B that is Z-Scored and flipped – the higher the Z-score, the cheaper the L/S portfolio is on P/B."
  },
  {
    "figure_id": "F839",
    "report_id": "R046",
    "label": "Figure 17",
    "context": "Figure 17: P/B Spread of Low Vol (Low vs. High Volatility) The Y axis is P/B that is Z-Scored and flipped – the higher the Z-score, the cheaper the L/S portfolio is on P/B. Price to Book of Low Vol Spread Over Time"
  },
  {
    "figure_id": "F840",
    "report_id": "R046",
    "label": "Figure 18",
    "context": "Figure 18: P/B Spread of Q-scores (Multi-factor model) The Y axis is P/B that is Z-Scored and flipped – the higher the Z-score, the cheaper the L/S portfolio is on P/B."
  },
  {
    "figure_id": "F841",
    "report_id": "R046",
    "label": "Figure 19",
    "context": "Figure 19: Beta Spread of Momentum (High vs. Low Return) The Y axis is Beta that is Z-Scored – the higher the Z-score, the higher the L/S portfolio is on Beta."
  },
  {
    "figure_id": "F842",
    "report_id": "R046",
    "label": "Figure 20",
    "context": "Figure 20: Beta Spread of Size (Large vs. SMid caps) The Y axis is Beta that is Z-Scored – the higher the Z-score, the higher the L/S portfolio is on Beta."
  },
  {
    "figure_id": "F843",
    "report_id": "R046",
    "label": "Figure 21",
    "context": "Figure 21: Beta Spread of Low Vol (Low vs. High Volatility) The Y axis is Beta that is Z-Scored – the higher the Z-score, the higher the L/S portfolio is on Beta. Figure 22: Beta Spread of Q-scores (Multi-factor model) The Y axis"
  },
  {
    "figure_id": "F844",
    "report_id": "R046",
    "label": "Figure 21",
    "context": "Figure 21: Beta Spread of Low Vol (Low vs. High Volatility) The Y axis is Beta that is Z-Scored – the higher the Z-score, the higher the L/S portfolio is on Beta. Figure 22: Beta Spread of Q-scores (Multi-factor model) The Y axis"
  },
  {
    "figure_id": "F845",
    "report_id": "R046",
    "label": "Figure 24",
    "context": "Figure 24: Exposure Changes in Momentum Long/Short Portfolio Over the Past 3 Months Exposures of the long-short momentum for MSCI Japan (Decile, Sector Neutralized)"
  },
  {
    "figure_id": "F846",
    "report_id": "R046",
    "label": "Figure 25",
    "context": "Figure 25: P/B Spread of Momentum The Y axis is P/B that is Z-Scored and flipped – the higher the Z-score, the cheaper the Momentum portfolio is on P/B."
  },
  {
    "figure_id": "F847",
    "report_id": "R046",
    "label": "Figure 27",
    "context": "Figure 27: Quality Spread of Momentum The Y axis is Quality that is Z-Scored – the higher the Z-score, the higher the Momentum portfolio is on Quality"
  },
  {
    "figure_id": "F848",
    "report_id": "R046",
    "label": "Figure 26",
    "context": "Figure 26: Size Spread of Momentum The Y axis is Size (L-S) that is Z-Scored – the higher the Z-score, the higher the Momentum portfolio is on Size."
  },
  {
    "figure_id": "F849",
    "report_id": "R046",
    "label": "Figure 28",
    "context": "Figure 28: Beta Spread of Momentum The Y axis is Beta that is Z-Scored – the higher the Z-score, the higher the Momentum portfolio is on Beta"
  },
  {
    "figure_id": "F850",
    "report_id": "R047",
    "label": "EXHIBIT 2",
    "context": "EXHIBIT 2: GST cuts announced in Aug'25"
  },
  {
    "figure_id": "F851",
    "report_id": "R047",
    "label": "EXHIBIT 3",
    "context": "EXHIBIT 3: Despite Triumph's drawdown from 398cc to 349cc, the price differential has not narrowed in materially Triumph vs Royal Enfield: Price gap before and after GST 2.0 Triumph's relaunched vehicles narrow the premium by a lit"
  },
  {
    "figure_id": "F852",
    "report_id": "R047",
    "label": "EXHIBIT 7",
    "context": "EXHIBIT 7: Distribution Gap by City tier"
  },
  {
    "figure_id": "F853",
    "report_id": "R047",
    "label": "EXHIBIT 8",
    "context": "EXHIBIT 8: Triumph's service network density"
  }
]