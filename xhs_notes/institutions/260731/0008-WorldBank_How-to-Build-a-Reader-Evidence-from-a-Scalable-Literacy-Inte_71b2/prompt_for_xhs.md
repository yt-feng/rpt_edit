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
- 默认避免出现具体投行品牌名，比如“高盛”“Goldman Sachs”，统一写作“某外资投行研报”。
- 不要解释你的思考过程，不要输出多余说明。

【推荐写法】
- 开头直接给一个自然判断，不要加“结论：”标签。
- 中间用 1/2/3 拆逻辑，但小标题要像正常内容标题，不要像写作模板。
- 结尾可以留下一个自然讨论问题，但不要引导关注、点赞或评论。
- 最后一行输出 2-4 个标签，优先：`#学习笔记 #研究笔记 #学习研究 #研报解读`。

【研报解析内容】
"""
# How to Build a Reader

# Evidence from a Scalable Literacy Intervention in Ghana

Erik T. J. Andersen

Simon Graffy

Jason T. Kerwin

Monica Lambon-Quayefio

Development Economics
Development Research Group
July 2026

Policy Research Working Paper 11433

## Abstract

Addressing the massive test score gaps between rich and poor countries will require programs that are both high-impact and scalable. This study uses the results of a randomized controlled trial in low-fee private schools in Ghana to study a program that meets both needs. The Tools for Foundational Learning Improvement program increased test scores by 0.5 standard deviation after just nine months of intervention. A machine learning method decomposes the effects by predicted test scores if the students did not receive the treatment, and the findings show that the gains were larger for weaker students. Moreover, the program's impacts scale roughly linearly with time compared to a shorter-term, smaller-scale pilot randomized controlled trial. The program's developers used generative artificial intelligence to accelerate lesson plan development and adaptation to new settings. An observational pilot test of this adaptation in Uganda yielded comparable results to those of this study's randomized controlled trial. The study developed a model in which basic skills constrain the development of advanced skills, which predicts the pattern of effects observed across early reading capabilities, and it makes forecasts about the future impacts of the program as it continues into second grade.

# How to Build a Reader: Evidence from a Scalable Literacy Intervention in Ghana

Erik T. J. Andersen, Simon Graffy, Jason T. Kerwin, and Monica Lambon-Quayefio\*

Authorized for distribution by Sergio Schmukler, Lead Economist, Development Research Group, World Bank Group

JEL Codes: I21, I25, O15

Keywords: Economics of Education, The Learning Crisis, Structured Pedagogy, Differentiated Instruction, Human Capital, Generative AI, Development Economics

The learning gaps between the world's poorest and richest countries are staggering. In 2021, South African fourth-graders scored 2.99 standard deviations (SDs) lower on reading than their counterparts in Singapore (PIRLS 2021). This gap is almost four times as large as the black-white test score gap for fourth graders in the United States (NAEP 2022). Indeed, these gaps are so massive that it is rare to even measure the richest and poorest countries using the same exam: South Africa is the only country in Sub-Saharan Africa that participated in the PIRLS, and it is one of the richest countries on the continent. A 3-SD gap between the poorest and richest countries is therefore likely to be a lower bound.

Addressing these gaps will require changes that are far more ambitious than the ones that governments have typically tried in the past. The average education program raises reading test scores by just 0.20 SD (Evans and Yuan 2022); we would have to repeat such a program more than 15 times to bring African reading scores up to rich-country levels. Whether these gains are cost-effective in dollar terms matters very little, as it is logistically impossible to actually run one of these programs over a dozen times.

We present the initial results from a promising approach to this challenge. Our data comes from a randomized trial we conducted with the education non-profit Inspiring Teachers, in which we evaluated their program, Tools for Foundational Learning Improvement (TFLI). TFLI is a smartphone-enhanced structured pedagogy program where teachers are given upfront training on the science of reading, and equipped with high-quality, semi-scripted lesson plans linked with student workbooks, to run daily literacy lessons and given coaching. The program incorporates a digital layer; teachers and coaches assess children's literacy skills and are provided with integrated student tracking, coaching management tools, and training videos through a mobile app called SmartCoach. We study the effects of the program's literacy model, Inspiring Reading, on first-grade students in low-fee private schools in the Central Region of Ghana. We randomly assigned 80 schools to either the Inspiring Reading program or a control group during the 2024-25 school year, and measured outcomes using end-of-year Early Grade Reading Assessments (EGRAs). We complement the data from the assessments with the survey data. The Inspiring Reading program will continue for the same cohort of students for two additional years, until the end of grade 3.

The program causes large increases in student learning: our pre-specified primary outcome, overall EGRA reading scores, increases by 0.504 SDs ( $p = 0.011$ ) which is the equivalent of more than two years of progress under the status quo. This puts TFLI at the $91^{\text{st}}$ percentile of all reading interventions within the first of what will be three years of the program. The effects on individual components of the reading score are consistent with the program's theory of change. The largest effects are on mapping letters to sounds ( $d = 0.764$ , $p < 0.001$ ) and phonemic awareness ( $d = 0.712$ , $p < 0.001$ ), which are the key skills targeted by the program in grade 1. The impacts on oral reading fluency and reading comprehension are smaller and do not reach conventional levels of statistical significance, although they are quite large relative to typical impacts in the literature ( $d > 0.2$ ). These are downstream skills that the program is building toward, and where effects are more likely as students progress through the program in grades 2-3.

We present extensive evidence that these impacts are real and not artifacts of our research design. We pre-specified a single primary outcome and the exact data analysis that we would run, so the p-value for that main test can be interpreted literally. Our findings are also robust to a wide range of robustness checks that vary the controls and address the small level of school-level non-compliance with treatment assignments, with point estimates ranging from 0.44 to 0.52 SDs. $^{1}$ The attrition rate was just 20%, nearly identical across study arms, and not differentially correlated with covariates by treatment status; we nevertheless compute Lee bounds and find a treatment effect range of 0.40 to 0.54 SDs, with both ends being statistically significant. Our exam scores come from an internationally standardized test (the Early Grade Reading Assessment); the NGO was blinded to the content of the test until the exams began, and the tests were administered by external contractors. We ran a separate experiment to estimate potential demand effects, randomizing whether each student was tested by an enumerator who was from the teaching profession. Assessor type matters for average scores but has no differential effects by study arm.

To understand how TFLI achieved such large effects so quickly, we develop a model of skill formation in which basic skills constrain the development of advanced skills. The model predicts that it is optimal to differentiate instruction: we should teach the basics to children with lower skills and advanced materials to children who are higher-skilled. It also predicts that high teaching quality and targeted instruction are complements, so that programs that combine the two approaches (structured pedagogy and targeted instruction) will have particularly large impact. TFLI operationalizes this approach, providing scripted lesson plans and workbooks (to improve teaching quality) along with regularly-scheduled targeted instruction (for differentiation of instruction). Moreover, the SmartCoach app helps to enhance both components, easing the management of program adherence for coaches and also the process of assessment and differentiation for teachers.

Consistent with the model, we see the largest impacts on the most basic skills: letter sound knowledge and initial sound identification. More advanced skills progress by less. We also see stark variation in the effects of the program across the distribution of test scores. In particular, there are large and statistically significant reductions in the fraction of students who cannot recognize words or read any words in a passage, both of which fall by over 40%. Impacts at the higher end are smaller, which is consistent with the program building basic skills more at this grade level. The effects also appear to be larger for male students; control-group girls are ahead by 0.26 SDs, and the treatment closes two-thirds of this gender gap. More broadly, the program appears to be most beneficial for weaker students, consistent with its design focus on supporting teachers in using assessment-informed instruction and in-classroom remediation.

We cannot decompose our treatment effects by students' initial test scores because there were no baseline exams. Instead, we use machine learning methods to predict the endline test scores for the control group, and then generate these predictions for the treatment group as well. We test for treatment effect heterogeneity by these counterfactual untreated outcomes. We see consistent increases across the ability distribution for most skills, with stronger treatment effects for initial sound identification among students we predict would perform worse without treatment. There are also distinctly lower treatment effects for the strongest students on the reading speed tasks, as well as for our overall reading score index. This and our other analyses are consistent with the prediction that weaker students and weaker skills are targeted more by the intervention.

We see evidence for a number of potential mechanisms for the treatment effects. A pre-specified index of teaching quality improves by nearly 2 SDs, with notable gains in key phonics activities such as having learners say the same correct sounds as the teacher and blending sounds to make words. Classroom observations also reveal increases in the teacher moving around the room and in student engagement with the workbooks. Student self-perceptions appear to improve, with statistically significant reductions in students thinking they are at the bottom of the class. Students are also more likely to practice reading at home, in line with previous evidence on shifting beliefs about relative performance (Dizon Ross 2020).

To further test these mechanisms we run an A/B test to examine how further enhancements to teaching quality affect test scores. A/B tests are rapid randomized experiments that allow organizations to improve their operations (Angrist, Cullen, and Magat 2025). We tested an intervention in which school leaders (principals) were trained to provide additional coaching to teachers on their implementation of the program, with the goal of improving teaching quality. Using a lower bar for statistical significance (which is standard in A/B testing (Azevedo et al., 2020)), we see evidence of gains in quality from this intervention. The effects on learning are not yet distinguishable from zero, but based on these findings Inspiring Teachers is continuing the intervention in the 2025-26 school year. Moreover, the impacts on learning are quantitatively consistent with our model: we see larger relative effects on more-advanced skills, with the impact on reading speed being $70\%$ of the main treatment effect, while the impact on letter sound recognition is just $10\%$ of the main effect.

Our model makes specific predictions about the program impacts we expect to see in second grade, which we will test in future data collection for the project. Specifically, we expect to see larger gains in more advanced skills now that students have developed the basic reading skills that constrain them. We also expect to see higher gains in advanced skills for students who are further up the skill distribution at the end of grade one, and lower gains for those who are at lower levels.

The impressive gains achieved by TFLI have important policy implications because the intervention is scalable both over time and across space. We conducted a previous small-scale pilot RCT during the 2023-24 school year; the intervention ran in four randomly-assigned treatment schools that year for just four months. Comparing those treatment schools to four randomized control schools, we see gains of 0.25 SDs, with the impacts distinguishable from zero despite the small sample size. Moreover, the actual RCT results in 2024-25 are very close to what we would have extrapolated from this pilot based on the additional time spent in the program: the program ran for 2.25 times as long and had effects that were nearly 2.25 times larger. This suggests that continued exposure to the program may raise test scores almost linearly, so we can expect gains of over 1 SD by the time the program finishes at the end of grade three.

The intervention is also designed to be scaled across space, not just within Ghana but also across Africa. Within Ghana, Inspiring Teachers is already scaling up the program to more of the country and to different kinds of school. It is currently running in 139 schools in the 2025-26 academic year, including in 80 government schools. The organization has been invited to expand to 400 government schools and 100 low-fee private schools in 2026-27, and is collaborating with the national and regional offices of the Ghana Education Service to roll out TFLI in all 1,638 government schools in the Central Region by 2029-30. This expansion is slated to be highly cost-effective: the current marginal cost of the program is \$48 per student, and so the cost per 1-SD gain is \$96, which already makes the program competitive with existing interventions. By 2029, Inspiring Teachers' budget model predicts the cost will drop to \$6 per student, which would make it extremely cost-effective if its current effectiveness can be sustained.

Scaling TFLI across Africa more broadly will require adapting the materials to other local contexts, education systems, and languages of instruction. It has two key advantages on that front. First, TFLI is currently English-language-first, which means that it can in principle be used across all of Anglophone Africa. It works even though English is not the native language of our study sample: TFLI has achieved significant gains in learning despite just 15% of our sample speaking English at home. This means it can serve as a complement to existing mother-tongue-first instruction programs. Second, TFLI's lesson plan developers use a component-based design system (where lessons are assembled from a common pool of adaptable components) and generative AI tools to accelerate lesson guide and workbook development. This allows Inspiring Teachers to efficiently leverage a highly scarce talent pool—highly-skilled instructional designers, which are rare not just in Africa but around the

world.

The organization is already using this tool to adapt the program to Uganda. They ran a preliminary pilot test of the program in Kanungu District during the 2025 school year, covering grade 1 classrooms. The pilot was not randomized, but they did post-intervention tests in both the program schools and in similar nearby schools. A regression-adjusted comparison of the mean test scores, following our specification for the main RCT, yields a difference of 0.514 SDs. These results suggest that the genAI-assisted curriculum adaptation approach can help the program scale to other countries with different early-grade reading curricula. Inspiring Teachers is in talks to do this in Zambia. TFLI has the potential to substantially narrow the learning gap between schools in Africa and those in the developed world.

Our results make contributions to four strands of the economics literature. First, we provide additional evidence that it is possible to drastically improve test-scores in learning-impoverished contexts. Previous work has shown that two types of intervention are capable of achieving impacts larger than half a standard deviation. The first is targeted instruction, which has proven benefits in a number of contexts (Duflo, Dupas, and Kremer 2011, Banerjee et al. 2007, Muralidharan, Singh, and Ganimian 2019) including in Ghana (Beg, Fitzpatrick, and Lucas 2023) and has been successfully scaled up (Banerjee et al. 2017). Angrist and Meager (2023) argue that targeted instruction has impacts of 0.9 SDs when implemented with high fidelity; fidelity (and, concomitantly, impacts) vary substantially across studies. The second is structured pedagogy, which has achieved large impacts in both local-level randomized trials (Piper et al. 2018c, Eble et al. 2021, Buhl-Wiggers et al. 2024) and at national scale (Piper et al. 2018a). It is also a key component of the extremely high-impact programs studied in Gray-Lobe et al. (2022) and Fazzio et al. 2021. We contribute to these existing findings by showing that large gains are achievable after just one grade of exposure, and using English-first instruction, despite most students speaking a different language at home.

Second, we show that targeted instruction and structured pedagogy can be combined successfully. While these two types of intervention are

[中间内容因长度限制已省略]

together...

![](images/971147bea87cca3c3c47de0d02622b35ea2bd26b808c2ec9c03fe9872c9bf690.jpg)

## Word Chains

den > hen > ten > pen

fin > fig > fog > frog

Ted > bed > bend > send

Next, I would like you to read them through again quietly in your pairs...

![](images/35021f8ed52c3e406f17de87fd3bab2b621ece1fa6408a5e4a9241bf4fb0ff35.jpg)

## Review Sight Words

7 min

![](images/65cc809648e788ada021eeb0abf98c432dfc9e5115c874c27f61d68ef1a909e8.jpg)

Let's practise reading the new sight words we learnt yesterday and remind ourselves of how they sound, and what they mean...

![](images/29502257c0fd4cb5c9b2f37e05d064fa4738b065d45eea34b5605879ec17fbd7.jpg)

Recent Sight Words

she

of

❤️

Turn to page 100 in your workbook.

We are going to read through some sight words we've learnt recently together.

![](images/e49506471e27a2332e384b56b37f172a5c352a1e09d3c86622b9a74387abc4f4.jpg)

## Sight Word Practice

<table><tr><td>so</td><td>of</td><td>by</td><td>on</td></tr><tr><td>for</td><td>can</td><td>not</td><td>she</td></tr></table>

Now I want you to read them again, quietly with your partner.

## Writing

15 min

For our writing session today we are going to learn about full stops.

![](images/49af2fd1934ecb8103107e34de5dc8a9ac6abcd0732a1d1137f91c4d78182af6.jpg)

## Teach Full Stops

5 min

We have learnt that sentences start with a capital letter.

Today we will learn what sentences end with.

![](images/d1d3618488743e0d15c960cfb0b101eac2f2f82a6fb37f40afaf563713e157cf.jpg)

Show & explain a full stop

I pat the mat.

![](images/6d0da88b1569839a48a51f01a0683491da77e246e86db586924dd14bef22736c.jpg)

I have circled the full stop. It is at the end of my sentence.

Full stops are very important. They tell us when a sentence has ended.

This helps to separate our sentences so that we can understand them.

![](images/e300e7e74f98e054ce1999d06df2950cc790c65e33a2e69be7f30730a32097f4.jpg)

## Shared Writing Practice

5 min

> Write out the sentences without full stops.

![](images/73db09c8f84b71544b36317be1593625b51bde8a2fa11b340f3ab52a8c3f3648.jpg)

Example (without full stops)

Sam is a man Pat is an ant

Let's read these sentences together.

It is hard to understand the sentences because the full stop is missing.

I know we start a sentence with a capital letter so my full stop must go before it.

Example (with full stops)

Sam is a man. Pat is an ant.

Let's read the sentences again and add the full stops together. "Sam is a man, Pat is an ant"
Where do the full stops need to go?

Yes, that's right. One after man. And another at the end, after ant. Why is that?

<table><tr><td colspan="2">Lesson Recap 2 min</td></tr><tr><td colspan="2">&gt; Ask the class these questions to recap the lesson.</td></tr><tr><td colspan="2">Let&#x27;s review what we&#x27;ve learnt today...</td></tr><tr><td>Oral</td><td>Have you seen someone building a house? What did you see?</td></tr><tr><td>Phonics</td><td>Is there an /e/ sound in the word &#x27;net&#x27;?</td></tr><tr><td>Reading</td><td>We read a story. What happened in the village?</td></tr><tr><td>Writing</td><td>How do you know a sentence is finished?</td></tr></table>

## 4.3 Independent Writing

Now, turn to page 101 in your workbook.

I want you to read the text and circle all the full stops you can see.

Check all learners are circling the full stops.

Now, look at the next text in your workbook.

![](images/6461decf2669d8729c4d911ce267d2a99daf62fa7b57f297ac4eeea33abddbf5.jpg)

What do you think is missing?

That's right, full stops.

I want you to spend 3 minutes adding in all the missing full stops.

Use the capital letters to help you.

√ End of lesson

## Sam and the Dog

Sam is on a mat

A dog is on a log Dad pats the dog

The dog did a spin Sam pats dog

Dad and Sam sit on the mat

Check all learners are circling the full stops.

What do you notice comes after a full stop?

# Week 7 | Day 2 Our Community

![](images/a3efc642822bc5dc1268ae22aa89a8bfbe46cd8786adaf60e53bcd6f5c7defae.jpg)

# Activities in our Community

## Oral Language

1. Talk about the new vocabulary:

![](images/cfbd1011b308c7f0dc718695f89571d3577d3557d6678627b13d175c1433fdc8.jpg)  
building

![](images/37902a914952a24f2720bc5d64fd014571e3faa173bf5fe7f071edc30f70b6e6.jpg)  
trading

![](images/1b3d4f42656206cb65385a15889b5f665aedaa1e454f9a1d8ab38ddb8d3c7990.jpg)  
teaching  
2. Read Aloud - Talk about the picture:

![](images/381137c2301f4b234cf7ecd96984cabe034b4a2dc24a7d06593fa7b460d5ab7d.jpg)

# Figure I6 Workbook Example Page 2

## Phonics

1. Write the letter sound you hear:

2. Write e:

3. Read words with e:

<table><tr><td>bet</td><td>ten</td><td>sent</td><td>bed</td></tr></table>

He gets ten pens.

## Reading

1. Read the word chains:

den > hen > ten > pen

fin > fig > fog > frog

Ted > bed > bend > send

2. Read recent Sight Words:

<table><tr><td>so</td><td>of</td><td>by</td><td>on</td></tr><tr><td>for</td><td>can</td><td>not</td><td>she</td></tr></table>

## Writing

1. Circle the full stops:

Sam is a man. Pat is an ant.

"It is my pan. It is a tin pan."

Pat is in the pan . "Spin me," said Pat .

Sam spins Pat in the pan .

2. Add the missing full stops:

Sam is on a mat

A dog is on a log Dad pats the dog

The dog did a spin Sam pats dog

Dad and Sam sit on the mat
"""
