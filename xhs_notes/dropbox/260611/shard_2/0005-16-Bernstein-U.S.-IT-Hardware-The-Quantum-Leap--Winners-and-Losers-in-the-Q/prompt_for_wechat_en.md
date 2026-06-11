You are a senior financial newsletter editor with a consulting-style strategy lens. You turn research-report material into a long-form English article that is structured, insightful, and suitable for a serious business audience.

Objective:
- Write an English Markdown article based on the report parsing below.
- Target length: around 2200 words, plus or minus 15%.
- Tone: serious, analytical, strategic, and readable.
- The article should not feel like a summary. It should make an argument.
- You may extend the report's logic into reasonable second-order implications, but do not invent data, company actions, or quotes.
- Do not disclose every detail. Leave several meaningful open questions that make readers want the full report.

McKinsey-style writing principles:
1. Answer first: open with the controlling idea, not background.
2. Governing thought: every section must support the main answer.
3. Mutually exclusive, collectively exhaustive logic: avoid overlapping sections.
4. So what: every section must explain why the point matters.
5. Synthesis over summary: do not list facts; interpret what the pattern means.
6. Action titles: section headings must be complete, insight-bearing sentences. Do not use generic headings such as "Key Takeaways", "Market Background", "Core View", or "Reader Implications".
7. Natural hooks: if you want readers to join the community or read the full report, the hook should emerge from unresolved analytical questions, not from promotional language.

Required Markdown structure:
- `# Title`: make it a direct argument, not a topic label.
- Opening: 4-6 short paragraphs that state the main thesis and why now matters.
- 4-6 `##` sections. Each `##` heading must be an action title: a sentence that tells the reader the insight.
- One section should identify what the report does not fully answer yet.
- One section should translate the report into a decision framework for readers.
- Final section: naturally invite readers to join the community or read the full report using this CTA: Join the community to read the full report and review the original charts.
- End with: `*This article is for learning and discussion only and does not constitute investment advice.*`

Content boundaries:
- Do not mention specific investment bank names such as GS. Use "a global investment bank report" if needed.
- Do not use emoji.
- Do not write like a viral post.
- Do not output your reasoning process.
- Do not generate image Markdown; the system will insert original MinerU images afterward.

Report parsing:
"""
## U.S. IT Hardware

# The Quantum Leap: Winners and Losers in the Quantum future - Industry Expert Webinar Transcript and Takeaways

![](images/09ef5861d0f6f1be4ce1151af68bbc768b05dba4eb93ac06b4e747bf23a8522d.jpg)

Mark C. Newman

+1 212 845 7822

mark.newman@bernsteinsg.com

![](images/35cfb116b4d788546c2402c2b2b7901d034a3bf59d7d3d1ca1edd93f4fe5c15e.jpg)

April Li

+1 917 344 8339

april.li@bernsteinsg.com

![](images/d68a0d07d71cf6722f4997bfd7b15bd3707bf4bcee4372fe812379987b629bee.jpg)

Phoebe Sun

+1 917 344 8481

phoebe.sun@bernsteinsg.com

We hosted a webinar with a Quantum industry expert with 15 years experience in leading Quantum companies and large tech, as a follow-up to our recently published Quantum Deep dive note. This note is an edited transcript with key takeaways.

A key framework to understand the quantum landscape is the distinction between manufactured qubits and natural qubits. Manufactured qubits, such as superconducting, silicon spin, and topological, are engineered systems that benefit from fast speeds. However, they tend to suffer from higher noise and shorter coherence times. In contrast, natural qubits, including trapped ions and neutral atoms, are inherently identical with long coherence and strong noise resistance, while the main drawback being speed.

Currently, there are three leading modalities: superconducting (manufactured), trapped ions (natural) and neutral atoms (natural). Superconducting leads in scale, speed, and industrial maturity, supported by significant investment from large tech. Meanwhile, trapped ions and neutral atoms are advancing rapidly due to their superior qubit quality and natural ability to perform long-range interactions. Other modalities, such as spin qubits and photonic, are still earlier in development but show scaling potential, while topological represent a high-risk, high-reward approach that remains far from practical implementation.

The trade-off between speed and accuracy influences application fit. Problems that require repeated sampling to estimate real-valued outputs, such as chemistry simulations, materials science, favor fast systems like superconducting. Problems requiring a discrete correct answer, such as cryptography or combinatorial optimization, favor the higher fidelity of natural qubits. While IBM expects Quantum Advantage will be achieved this year, large-scale, fault-tolerant quantum computing is still many many years away. Progress depends on key milestones incl. development of logical qubits, logical gates, and scalable error-corrected systems.

Quantum computing is highly capital intensive. As a result, the dominant model will likely be cloud-based, rather than widespread ownership of machines. Early demand is driven by academia, government, and research fields with growing interest from industries like finance, logistics, and optimization.

Competitive dynamics favor large technology companies such as IBM and Google due to their access to capital, infrastructure, and talent. IBM, in particular, has a strong advantage in software and ecosystem like Qiskit, though its hardware leadership is increasingly challenged by higher-quality natural qubit systems. Startups are more likely to succeed through specialization, partnerships, or government-backed initiatives rather than competing head-on at full scale.

Overall, the industry is likely to evolve into a multi-modality ecosystem, where both manufactured and natural qubit coexist, each optimized for different applications, with hybrid quantum-classical computing emerging as the most practical path forward.

BERNSTEIN TICKER TABLE

<table><tr><td rowspan="2">Ticker</td><td colspan="4">9 Jun 2026</td><td rowspan="2">TTMRel.</td><td colspan="4">Adjusted EPS</td><td colspan="3">Adjusted P/E (x)</td></tr><tr><td>Rating</td><td>Cur</td><td>Closing Price</td><td>Price Target</td><td>Cur</td><td>2025A</td><td>2026E</td><td>2027E</td><td>2025A</td><td>2026E</td><td>2027E</td></tr><tr><td>AAPL (Apple )</td><td>O</td><td>USD</td><td>290.55</td><td>350.00</td><td>20.4%</td><td>USD</td><td>7.46</td><td>8.87</td><td>10.65</td><td>39.0</td><td>32.8</td><td>27.3</td></tr><tr><td>DELL (Dell)</td><td>O</td><td>USD</td><td>381.78</td><td>500.00</td><td>214.1%</td><td>USD</td><td>10.35</td><td>18.77</td><td>22.84</td><td>36.9</td><td>20.3</td><td>16.7</td></tr><tr><td>HPE (HPE)</td><td>M</td><td>USD</td><td>48.27</td><td>62.00</td><td>140.2%</td><td>USD</td><td>1.96</td><td>3.42</td><td>4.14</td><td>24.6</td><td>14.1</td><td>11.7</td></tr><tr><td>HPQ (HPQ)</td><td>M</td><td>USD</td><td>24.94</td><td>27.00</td><td>(25.4)%</td><td>USD</td><td>3.12</td><td>3.00</td><td>3.04</td><td>8.0</td><td>8.3</td><td>8.2</td></tr><tr><td>IBM (IBM)</td><td>M</td><td>USD</td><td>277.49</td><td>280.00</td><td>(22.5)%</td><td>USD</td><td>11.58</td><td>12.35</td><td>13.93</td><td>24.0</td><td>22.5</td><td>19.9</td></tr><tr><td>SNDK (SanDisk)</td><td>O</td><td>USD</td><td>1,646.54</td><td>1,700.00</td><td>3836.0%</td><td>USD</td><td>2.99</td><td>64.73</td><td>200.47</td><td>550.7</td><td>25.4</td><td>8.2</td></tr><tr><td>STX (Seagate)</td><td>O</td><td>USD</td><td>846.01</td><td>1,000.00</td><td>538.0%</td><td>USD</td><td>8.10</td><td>14.89</td><td>32.49</td><td>104.4</td><td>56.8</td><td>26.0</td></tr><tr><td>SMCI (SMCI)</td><td>M</td><td>USD</td><td>40.64</td><td>37.00</td><td>(28.3)%</td><td>USD</td><td>2.60</td><td>2.80</td><td>3.25</td><td>15.6</td><td>14.5</td><td>12.5</td></tr><tr><td>WDC (Western Digital)</td><td>O</td><td>USD</td><td>517.72</td><td>590.00</td><td>802.3%</td><td>USD</td><td>4.80</td><td>9.81</td><td>20.19</td><td>107.8</td><td>52.8</td><td>25.6</td></tr><tr><td>SPX</td><td></td><td></td><td>7,386.65</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended  
DELL estimate is Reported EPS; DELL, SMCI base year is 2026;  
Source: Bloomberg, Bernstein estimates and analysis.

## DETAILS

We hosted Quantum industry expert with 15 years experience in leading Quantum companies and large tech, as a follow-up to our recently published Quantum Deepdive note. This note is an edited transcript with key takeaways.

Speaker Key:

Mark Newman = MN

Technology manager in the quantum computing industry = Expert

MN: Good morning, everyone. I'm Mark Newman, Bernstein's US IT Hardware Analyst. And today, we have the pleasure of hosting this webinar with a Technology Manager in the Quantum Computing Industry, who has 15 years experience in leading Quantum companies and large tech. At both companies, he worked on Quantum, so he has a wealth of knowledge and experience in quantum. And he is not biased because he is working for a non-profit currently. Expert, thank you very much for joining us. Anything else you'd like to add in terms of your background?

Expert: Yeah, absolutely. I've worked in the quantum computing industry and academia for the last 15 years or so. My career is sort of taking me up the whole stack that makes a viable quantum computer. I started off much more focused on hardware, even though I am a theoretical physicist by training, and then slowly over time moved to more system-level considerations, and then nowadays I work more on the software applications and algorithm side. My primary research expertise and focus for the last decade has been on characterization and benchmarking of quantum computers, so really understanding not only what they are capable of doing now, but what we can learn now to tell us about what they might be capable of in the near-term future and in the far-term future. So that's really been my focus.

MN: Great, thanks very much, Expert. And a reminder for everyone joining on the call, we do have a pigeonhole link where you can enter your own questions. I'm going to start off with a bunch of my own questions, and I'll refer to that later in the call to get some investor questions in as well. So let's get started. I'd like to start off talking about all the different, approaches, or what's referred to as the modalities for quantum. So, you have a lot of experience here, in quantum. You're neutral, as you said, working at a non-profit currently. If you had to rank the six modalities, can we talk about each of the six modalities and talk about them in terms of which ones you think have the best chance of success going forwards? I'll just list them all — superconducting, trapped ion, neutral atom, silicon spin, photonics, and topological.

Expert: Yeah, absolutely. So, I think, before I go into that, I want to put in a few caveat statements. Quantum computing as an industry is not necessarily following the path that classical computing and traditional computing has, in the sense that when you look at the early, early, early days of classical computing, when we had vacuum tubes and these sort of massive-scale systems, the industry was really revolutionized by the transistor. And it sort of unified around this single architecture that was going to be the one moving forward. That could happen in quantum computing, absolutely, and I think some of the modalities you mentioned there, even some that aren't on that list, that are even less solidified now, could have that kind of impact. But at the moment, we don't anticipate that necessarily in the next 10 or 15 years. It's one of these situations where an absolute revolution in science and in physics could cause this amalgamation or homogenization of the architecture. But right now, in my view, there's no clear winner in terms of the long-term bet. I think each architecture has their advantages and disadvantages, and it's a hard engineering and a hard science problem to overcome the roadblocks that they each have to getting to a large-scale quantum computer. There certainly are ones that are leading right now and ahead of the game. But these sort of revolutions do even happen on a small scale. Like, I'm gonna place neutral atoms somewhere, and if we had this call two years ago, they would have been in a completely different location on the scale. So, these kind of things can happen, just keep that in mind, that information needs to be refreshed periodically.

Expert: I like to break things into two buckets, into manufactured qubits and natural qubits. So manufactured qubits are superconducting qubits, the spin qubits, and the topological. The natural qubits are the trapped ions and neutral atoms. And then, kind of in the middle is photonic. Photonic qubits are “natural,” because they're light. But they require manufactured waveguides, manufactured substrates to live in. Now, this is actually also true of trapped ions, trapped neutral atoms, they have manufactured traps that they live in. So, the lines are all a little bit blurry here, right? But the reason this distinction is important is because it really impacts the quality of the individual qubits themselves.

With the natural ones, where you would see the trapped ions, the neutral atoms, and the photonic qubits, these qubits themselves have really good properties. One, they're consistent, every single one of them is the same in the world. And that makes a big difference about designing your control architecture, so the higher level stuff in the stack that controls the quantum is much more reliable, right? If you put 50 atoms in a trap, you know that all 50 are more or less the same to levels of accuracy that you don't really care about. Because they're natural the parts of their system that we use to store information also have

very natural properties. They're naturally long-lived, so they have good coherence times, which means that we can store the information for a long time. They're naturally robust to error, because again, these are systems that exist in the isolated world, independent of us creating them. So they have a lot of nice properties like that. The flip side is that all those properties that make them nice make them very hard to control. The control is very slow, so you think about the operation rate of these natural qubits, the ions and the atoms, it's at the... you can repeat a computation at most at a 1Hz repetition rate, so once per second. Some of this is engineering challenges, and these groups are working very hard to overcome them, right? But a lot of it is just the physical, natural operational speed of these devices is much slower. I'll touch on that in a bit.

Expert: By contrast, the manufactured qubits, they have much faster operation rates, because we are making that to be the case, right? So they operate at kilohertz, or even megahertz repetition rates, where we can repeat computations at a much faster timescale. The natural clock speed of the operations are also much faster, because again, we've designed the system to be the way we want. Where they fail, so where the superconductors, the spin qubits, and the Majoranas suffer, is that they, don't have as nice natural properties, with the exception of the Majoranas, which I'll get to in a second. But the superconducting and spin qubits are naturally noisier, they're not as consistent. When you make two superconducting qubits, for instance, even if you try to make them the same, you're not going to. There's a roughly 10% spread in fabrication, typically. That means your control systems have to be a lot more robust and work in a much larger bandwidth because they have to adapt naturally to the spread and the qubit properties. They don't have as good coherence times either. Because they're these macroscopic manufactured systems, they're much more susceptible to noise in the environment, and they have to be much more carefully isolated. And all of this means that typically the manufactured qubits are going to have worse properties. They're going to have worse error rates, as we call them, per operation. They're going to have worse coherence times, and the benefit for them is really the speed versus quality of the natural qubits.

Now, if we go on to dive into the details, each one in particular, the way I view it right now is sort of a three-way tie at the top, and it's hard to really say which one is leading, because it really depends on what you're looking for. And that three-way tie is between superconducting qubits, trapped ions, and neutral atoms. Two years ago, I would have put neutral atoms probably at the bottom of the whole list, right? In the last 3 years, there's been really revolutionary work out of the Harvard and MIT collaboration that has a spin-out company, QuEra, and they've really pushed the field. But it's important to caveat that they're so far the only ones who can get this good performance out of neutral atoms, whereas we see multiple trapped ion groups and multiple superconducting groups in industry and academia demonstrating good performance overall.

The superconductors win on speed, in the sense that if you want to do many, many repetitions of a circuit of a computation, which is something you naturally need to do for quantum computing - you can do that orders of magnitude, factors of a thousand, faster than anywhere else on them. They also have one of the largest scale computers, hundreds of qubits, and their quality has improved drastically in the last 5 years. So the quality of the gates is good, the reproducibility and robustness of the gates is very good. They're certainly, very ahead right now overall. So they're just maybe the 1A, right? The problem with them is the long-term vision is a little bit more murky. Because they're manufactured planar devices that exist on a flat plane, it's very hard to engineer interactions that aren't nearest neighbor, aren't between two qubits that are next to each other. And what we believe is that these longer-range interactions are necessary to do better error correction codes that will lower all the error rates to be where we can reach this fault-tolerant logical quantum computer that is going to be able to solve the applications we really care about. So there's tremendous savings in the number of physical qubits you need to make one logical qubit if you can enable these long-range interactions. That naturally just doesn't happen in superconducting qubits. Groups like the big industrial people like IBM and Google are working on finding ways to be able to do that. And I actually just saw this startup in Europe, IQM, has just released today their roadmap for that, for how they will enable these long-range interactions. So that's where I think things get a little murky. It's a lot of, to be frank, world-first demonstrations anywhere, even outside of academia, that has to be done for these groups to achieve that.

But, preliminary results that we have seen publicly look good, so they are on their pathway, but it is a big engineering and technical challenge. The ions and atoms naturally can do this, either by moving the ions around, or moving the atoms around as well, which are slightly different technologies to do that. So they can enable these long-range interactions, these multi-qubit connections, very naturally. And we'll see, probably in the next couple years, very quickly demonstrations from these groups, of those logical or early fault-tolerant demonstrations. But it's going to be hard for them to overcome this, the slowness of their sampling rates. So for applications like chemistry, material science that require estimation of a real number, where you need, you know, to some precision that's given by how many times you can repeat the computation. They're going to struggle, because the computations are going to take a thousand times longer. It's really a trade-off here, but there are applications that don't need that, like factoring, that just need the answer once, right? As long as you get it. So, you know, it really is application-dependent which one is going to be a long-term winner.

Expert: Spin qubits, photonics are at a much earlier stage, even though they've been explored for just as long, and photonic quantum computing was one of the first proposals. Photonic quantum computing has always, struggled with being able to interact photons. They naturally don't interact, so doing gates between the qubits is very hard, and that's still a problem. You have some companies that are exploring it, they have proposals, but we don't really see a lot of actual demonstrations coming out of those, so it's hard to judge where they're really at. Similarly, spin qubits are notoriously noisy and dirty and just difficult to manage. Once you can solve the problem of how do you make a high-quality spin qubit, how you can make interaction between two of them, it's very 

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
