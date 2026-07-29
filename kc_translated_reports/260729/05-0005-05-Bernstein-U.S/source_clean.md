# Cybersecurity: mid-'26 CISO conference call transcript covering budget trends and priorities + AI-impact

We recently hosted a conference call with three CISOs discussing the latest budget trends, AI-impact, and priorities. A full edited transcript is below and replay is here.

Cybersecurity spending continues to outpace broader IT spending, driven primarily by AI. Security leaders consistently described AI as the biggest catalyst for new investments, both because organizations must defend against AI-enabled attacks and because they need to securely enable internal AI adoption.

Identity has become the new security perimeter, and non-human identities are now a top concern. The focus is shifting to securing AI agents (human-in-the-loop + independent) — how to allocate identities for data / system / application access and apply privileged access and governance frameworks that ensure least-privilege time constrained access across both human and non-human actors.

Organizations are struggling to balance AI adoption with control and visibility. Security leaders reported sharp increases in employee experimentation across multiple LLMs leading to concerns around what data is being entered into models, what systems agents can access, what actions they can perform, and how those actions are monitored and audited. As a result, organizations are investing in AI governance through either centralized AI routers or endpoint, network, and data-layer controls that provide visibility into prompts, agent behavior, data access, and potential exfiltration risks.

Beyond increased budgets, vendor consolidation is the main funding mechanism for new security priorities. CISOs are retiring legacy platforms, reevaluating existing security stacks, and looking to add features from current vendors as this is generally much cheaper than adding best-of-breed standalone products. ...but vendor consolidation is at the key cyber pillar level, not end-to-end. Participants generally preferred maintaining dedicated leaders within “core pillars” such as identity, endpoint, network, web security, cloud security, and email. CrowdStrike, Wiz, Palo Alto, and Okta were frequently praised for innovation.

Security operations are moving toward automation because human-speed response is no longer sufficient. Participants agreed that AI-enabled attackers are accelerating the pace of threats forcing organizations to actively evaluate Agentic SOC platforms and autonomous response capabilities to reduce investigation times, improve resilience, and operate closer to machine speed. "Switzerland" VC-backed startups (e.g., Torq, Tines) that could look across cyber pillars seemed to be preferred. The discussion also suggested that traditional SIEM is becoming less strategic vs. an Agentic ITDR/SOC model.

The overarching message from the discussion was that AI is forcing a redesign of cybersecurity strategy. Budgeting, identity management, security operations, vendor selection, governance, and risk management are all being reevaluated through an AI lens. Security leaders are no longer treating AI as an emerging trend; they are restructuring security programs around the assumption that AI will define both the future threat landscape and the future technology environment.

## BERNSTEIN TICKER TABLE


O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended

CRWD, OKTA, S base year is 2026;

Source: Bloomberg, Bernstein estimates and analysis.

## INVESTMENT IMPLICATIONS

No impact to target prices or investment recommendations.

## DETAILS

We recently hosted a conference call with three CISOs from three different industries: Insurance, Manufacturing, and Healthcare Software to get their perspectives on cybersecurity spending. This note provides a summary of our key takeaways and a full edited transcript and a replay of the call is available through this link.

For complete results of our recent CISO survey, please check out link.

## Detailed takeaways:

Cybersecurity spending continues to outpace broader IT spending, driven primarily by AI. Across industries, security budgets are either growing faster than overall IT budgets or being protected while other IT functions face cuts. Security leaders consistently described AI as the biggest catalyst for new investments, both because organizations must defend against AI-enabled attacks and because they need to securely enable internal AI adoption.

Identity has become the new security perimeter, and non-human identities are now a top concern. CISOs emphasized that remote work, AI agents, and autonomous workflows have fundamentally changed access management requirements. The focus is shifting beyond employee / customer accounts toward identity for independent AI agents — how to allocate identities for data/system/application access and apply privileged access and governance frameworks that ensure least-privilege time constrained access across both human and non-human actors.

Organizations are struggling to balance AI adoption with control and visibility. AI usage is growing rapidly across engineering and business teams, often faster than expected. Security leaders reported sharp increases in token consumption, employee experimentation across multiple LLMs, and growing concerns around what data is being entered into models, what systems agents can access, what actions they can perform, and how those actions are monitored and audited. As a result, organizations are investing in AI governance through either centralized AI routers or endpoint, network, and data-layer controls that provide visibility into prompts, agent behavior, data access, and potential exfiltration risks. The discussion was less about restricting AI usage and more about establishing guardrails around data protection, access rights, and agent autonomy.

Particularly in budget-constrained environments, CISOs are retiring legacy platforms, reevaluating existing security stacks, and looking to add features from current vendors as this is generally much cheaper than adding best-of-breed standalone products. Rather than purchasing standalone point solutions, many are adding capabilities from existing strategic vendors where possible because add-on modules are typically far cheaper than introducing new products. The goal is to free resources for higher-priority initiatives.

Vendor consolidation is at the key cyber pillar level, not end-to-end. While companies like Microsoft and Palo Alto continue to expand their security portfolios, participants generally preferred maintaining dedicated leaders within “core pillars” such as identity, endpoint, network, web security, cloud security, and email. CrowdStrike, Wiz, Palo Alto, and Okta were frequently praised for innovation, while concerns were raised about vendors that have been slower to evolve around AI and modern identity requirements.

Participants agreed that AI-enabled attackers are accelerating the pace of threats, making traditional SOC models increasingly difficult to sustain. Organizations are actively evaluating Agentic SOC platforms and autonomous response capabilities to reduce investigation times, improve resilience, and operate closer to machine speed — "Switzerland" startups that could look across cyber pillars seemed to be preferred. The discussion also suggested that traditional SIEM is becoming less strategic than integrated threat detection, threat intelligence, orchestration, and response capabilities that can convert signals into action. The end state is increasingly an Agentic ITDR/SOC model that combines detection, enrichment, investigation, prioritization, and response into a largely automated workflow.

The overarching message from the discussion was that AI is forcing a redesign of cybersecurity strategy. Budgeting, identity management, security operations, vendor selection, governance, and risk management are all being reevaluated through an AI lens. Security leaders are no longer treating AI as an emerging trend; they are restructuring security programs around the assumption that AI will define both the future threat landscape and the future technology environment.

## Full transcript:

This transcript has been edited for clarity and consistency.

## Speaker Key:

## Bernstein analyst: PW: Peter Weed (US SMID-Cap Software)

CIOs: Sean (Insurance); Kristie (Manufacturing); Raj (Healthcare Software)

PW: Good morning, everyone. We're going to give it 30 seconds or so for attendees to file in. I know it takes a little bit to get everything connected. Just bear with us as that goes on. Well, I think I'm going to jump in and hopefully everybody was able to get connected.

Just a little bit of housekeeping just from the top. A reminder, there's a Pigeonhole link for anybody who is joining. If you have questions, please feel free to submit them there and we will take a look at them. As you know, we do a series of these type of webinars. Obviously, we just did one around CIOs. I've asked the panelists here to be actually off video, given that we're dealing with perhaps a slightly more sensitive topical area of cybersecurity as part of this.

Where I'd really love to start is just with a really quick reflection on the CISO survey that we had. Then I'm going to introduce the panelists and we're going to go into some of their experience. But hopefully, many, if not most, of you saw earlier this week we published the results of 100-CISO survey, our biannual survey. This is the mid-year one. It very much focuses on US cyber practitioners.

What were the large findings? Not surprising, very consistent with what we even saw in our CIO survey, what was the number-one budgetary line item for CIOs to be increasing? Cybersecurity. In cybersecurity, what did we hear from the cybersecurity professionals? We heard that their budgets, by and large, are going up and, on average, going up greater than IT budgets.

In fact, if you looked across all the responses we had, we had budgets going up, depending on the industry, between, say, four and six-plus percent on average. But there's a bit of a bell curve. There are some organizations increasing it as much as the teens and some increasing it in the lower single digits.

From a topical standpoint, I think it's also not surprising to say that a lot of what was driving some of the energy is AI, both threats from attacks coming in as well as the demands of their organization to secure the projects, the AI projects, that the businesses were trying to get done.

There's a lot of, obviously, nuanced detail in the overall report that we have. When we looked at the categories of cybersecurity within there that get invested in, certain categories are seeing much greater than others and it implicitly suggests that those areas are probably where people are investing around these threats as well as supporting this infrastructure.

That includes topical areas that I think a lot of conversation has been around. Identity is front and center. Some of the other categories like endpoint security continue to end up near the top, threat intelligence.

But, really interesting, where we're seeing a bunch of movement is also in security operations itself. At least my personal experience is that the human side of cybersecurity can be up to 40% of budgets. Those areas are places where both more expertise is needed, but also the application of tools may be coming in to those organizations. I think that'll be some of the interesting conversations we'll have with the participants here.

On the other end of the spectrum, the things that actually continue to do more poorly, the worst of the worst was Security Service Edge. Again, I think it'll be interesting to understand with some of the CISOs on the call here why that is and how its position is not a priority today. I don't think it means that people are probably ripping these things out. It just means that, relative to other things that could be done, that is not a top-of-mind topic right now.

Other tail, lower investment areas included SIEM. Think of this as more of the traditional SIEM, the things that, say, a Splunk is doing as opposed to what I really think of more as threat intelligence, which would be the next-generation SIEM or XIM or some of these things that you're hearing from some other vendors, at least in my opinion, email security, secure browser. Those are going to be areas of lower investment focus today.

So, anyway, with some of that context out of the way... And again, please go into the CISO survey. If you have other questions, please surface them as part of this conversation. What I'd love to do is actually go around the horn with the participants today where they can introduce their organization. Obviously, they're not going to get into their company name but more of, what

industry are they in? What size of organization and cybersecurity budget are we talking about?

I guess, just because I see you first on my screen here, Sean, I'm going to ask you that first. Tell us a little bit about your context as an organization, what industry, what budget, and really help us understand how that budget is changing this year. What's really driving that change? How have those priorities changed and where are you putting money to work?

Sean: Yes. Hello. So I'm in the insurance sector on the commercial side. We have about 6,000 employees globally and the predominant number of those employees work remotely. Our focus this year is to increase probably our security spend between 12% to 15%.

We've been deployed with traditional security services from the endpoint side and, as Peter said, a lot of the SIEM stuff, mail stuff, but now we're really shifting to the focus on the AI side of the house. More and more of our users are obviously leveraging the tools. I'm sure that's the same across the board. We're trying to gain more insights into how they're using the tools and where the threat vectors are coming from. They seem to be moving and changing daily.

We're trying to wrap our heads around where we're going to spend those additional funds. We're talking with several different possible vendors to see what works with our deployment. We've got quite a variety of deployments on different sides, depending on how we service the client. So we don't have a one-size-fits-all approach. So we've got to be more flexible, and so I think that's been a little bit of a challenge for us, but we're definitely increasing double digits on the security spend, mostly focused on the AI side, though. You're muted.

PW: I am muted. I am securing you guys from my blather here. Just remind us the scale of your organization.

Sean: We're about 5,500 employees globally.

PW: Yes. Kristie, same question to you, just a little background on the industry and how your priorities have been changing and budgets have been changing.

Kristie: Sure. Yes. I'm in the manufacturing industry. My company is about 50,000 people in 170 locations in 29 countries, so we have a pretty big global footprint. So a lot of new regulations coming out of Europe drive a lot of the compliance activities that we're doing. Our industry, manufacturing globally, is always under a lot of cost pressure. So we are being pushed to try to maintain a flat budget going into 2027. Given the amount of AI adoption that the business is trying to push for, it's making that a little bit challenging.

Two areas we really need to invest in is better internal data classification, role-based access, least privilege enforcement as we're adding new language models into our environment to make sure that we're not overexposing our internal data. Then, also on the new proliferation of non-human identities is building out our IGA to make sure that we're really managing those identities properly and that we're not going to get into a situation where we have an agentic identity taking more action than they should be able to have privilege to do.

PW: Thank you, Kristie. Raj, same for you.

Raj: Good morning, good afternoon, and good evening, folks, wherever you are. My name is Raj. I am the CISO for a healthcare data analytics company. We're primarily based in the US market, but we have development centers across the globe. We're probably around 12,000 to 15,000 total employees. We're in roughly the 2 to 5 billion revenue range.

My cybersecurity budget for 2026 was around \$20 million, which is roughly about 10% to 12% of our overall IT budget. Going into 2026, the primary focus was around, again, securing internal AI initiatives as well as putting in controls for emerging AI offensive threats and capabilities that we saw out there.

I would say, between 2025 and 2026, my overall cybersecurity budget was projected to go up by around 6% to 7%, which is fairly normal over the years, but we did have to recalibrate and reevaluate stuff around March of this year with all the disclosures around the Mythos LLM and the advanced frontier models and their offensive capabilities. So I was able to go back to my leadership and my board and ask for additional funding to mitigate some of those threats.

So, at this point of time, my projection is that, for 2026, our cybersecurity budget will probably end up 20% more than what we had the previous year. Most of those investments have been focused around attack surface reduction. So we hear a lot of stuff about what Mythos and some of these frontier models can do, and we don't really want to take a chance. So we want to make sure that we are as secure as we can be by reducing our attack surface, reducing our technical debt.

Then there's a lot of projects that we are expediting around identity management, especially around non-human identities as the agentic AI gets more adopted, both externally as well as internally within the company. Then the third area, I would say, we are focused on is around business resiliency. Because at the end of the day, we are assuming that cyber events will happen, and it's going to be important in terms of how quickly we can bounce back from those and get to an operational state.

PW: Thank you. Raj. Maybe we'll continue the conversation here because you brought up the pretty significant budget increment around the worries that you have. How did that work? Do you go to the CIO? Are you having to take that above the CIO? What's the argument that is getting people aligned?

Then, as much as you have an understanding of it, where is that budget coming from? Is the CIO having to reduce their spend in some other areas and their envelope is going to stay the same? Was this completely new dollars? How much are they pushing on you to get more efficient so that you're retiring some legacy architectures or consolidating vendors or needing to push on your employment levels so that you can afford more technology? How does that get paid for?

Raj: ; Absolutely. So I think in this particular context, when we started evaluating the threats that were evolving from these frontier offensive models and their offensive capabilities, we immediately started to see what our exposure is. We are healthcare. We deal with a lot of healthcare data, PHI, a highly regulated environment. So I conducted a risk assessment and identified key areas that we need to remediate or expedite in terms of risk reduction.

One of the things that really helped me in this process is, we do use a fair methodology for risk quantification. So I was able to estimate, in terms of dollar amounts, what a certain incident or a situation could cost the company. So, with all of those assessments, we had to go all the way up to the board and put our case in front of them and say, okay, here's the initiatives that we want to expedite and prioritize and here's what it's going to cost us from a budgetary perspective.

There was some discussion, but I think what really helped was all the discussion that's in the media about these advanced offensive capabilities. So the board was very supportive and so we were able to get additional funding. So, to answer your question, Peter, these were new dollars that were sanctioned by the board in view of the emerging threats.

PW: Yes. You got more help over the last couple of days as OpenAI and Sol set up a pretty weak containerized application just to prove that they could break out of something that is not secure.

Kristie, I think you had a different setup, if I heard you right, which is, there's a lot of pressure not to grow the budget beyond the normal pace that you have, unlike Raj, who had this 6% growing budget, and then they went and were able to get more money. How has that conversation differed in your own organization?

Kristie: Yes. I think, overall, central services is under a lot of pressure to reduce costs to the business. It cuts into their profit margins on the products that we sell. It's a really difficult global environment right now with tariffs and the like influencing the piece price of what we're able to sell.

So the rest of the business is leaning pretty hard on central services in general to make a lot of cuts across the board, which is impacting our ability to spend and to grow. I would love to be able to get... 6% would be great, 20% is amazing, but it's just not really feasible in the current financial environment of the company.

PW: It's interesting, though. If the central services is actually being required to tighten up its budget... And I take that to mean that perhaps it's even shrinking as a percentage of overall revenue, but you're able to keep your budget more stable in some ways. I guess you have increased. Are you increasing as a portion of overall IT spend or are you staying more stable there?

Kristie: That's a great question. So the IT budget is being pushed to reduce by 10% overall. My budget is going to stay flat, but I only represent about 6% of the overall IT budget. So at least that puts me maybe a little bit closer to a reasonable Gartner metric of overall IT spend. But I also own IT manufacturing and embedded product cybersecurity, so that includes the customer - facing products. How do we secure those as well, is also included in that budget.

PW: When you think about that budget, I can imagine some parts of cybersecurity is almost like cost centers because it's for internal operations. What you have customer-facing, that's almost part of the product team, so it scales with the scale of that business. Do you have different pressures, whether or not it's that internal-facing versus customer-facing budgets?

Kristie: Yes, definitely. I think more on the embedded product, cybersecurity is really what kind of cryptography that we're using, our HSMs that we're buying and installing in these manufacturing plants globally. So a lot of that really comes down to technology pressure and, can we do this cheaper? Can we do it more open-source? Can we build it in a low-cost country? Can we use low-cost labor to try to reduce that overall impact on the piece price?

But once it's set up in that vein, once it has built that infrastructure, then it is pretty justifiable to pass... We're a tier-one supplier, so it's pretty easy for us to justify passing that on to our customer.

PW: When you're in this more constrained environment where your budget's going to be pretty consistent, but you talked about some of the changing priorities, how are you able to reallocate budget to spend on those new topics?

Kristie: Yes. It's really taking a hard look at what we have in place today and if the priorities of the business have shifted, if we've removed a lot of our on-prem stuff into the cloud. Obviously, the cybersecurity spend needs to move in that direction as well, but we're also looking really hard at trying to do more tool consolidation to try to get more bang for the buck out of some of our primary vendors that we use today and trying to think creatively.

Do we need a dedicated data loss prevention tool or can we cover it enough between our endpoint network and email security tools that we already have in place today to get an 80%-of-the-way solution that'll free up some budget to do better data protection and user behavior analytics-type tools that would give us a better data protection foundation to support this AI movement internal to the business?

PW: You mentioned a couple things there. So, one of them is, as you move to the cloud, maybe you can retire some of the tools that were for your on-prem historic environment. Then the second is maybe some vendor consolidation.

Maybe if we start with that first category, what are those tools that you are hoping to retire? Is it just things like on-prem identity, so things like a PingID? When you move to the cloud, then you move to a cloud vendor? I guess it's reallocating budget, so you're not really saving dollars, but it's moving from one vendor to another. Is that the situation there?

Kristie: Yes. For stuff like that where you're just following the technology trend, it's really just a shift more so. But, like I said, we're trying to do more consolidation and trying to leverage more features that are on the tool sets that we already have today or where you're doing an add-on module to add capability, you can usually get those at a much cheaper price than buying a tool dedicated to do that as a standalone.

Then, presumably, that agent's already deployed and you already have maybe managed services or a team dedicated to maintaining that. So you can get some reductions and cost savings by doing this consolidation effort. That's really where the cost savings come from that frees up the dollars to do the new investment.

PW: I think you mentioned a few, I guess, vendor categories. I think you said network and email and maybe one other when you were talking about DLP.

Kristie: Endpoint.

PW: Endpoint. Are those the anchors that you're trying to accumulate as features into or are there others?

Kristie: No. Those three pretty much make up the foundation of our cybersecurity program that represents our biggest threat vectors into our environment. So those tools are really where we've made the most investment and make up the majority of our budget and also the majority of our tool suite.

PW: If you feel comfortable talking about individual vendors, I will at least bring up a couple. Obviously, you've got folks like Palo Alto that have traditionally been in the network security and CrowdStrike in the endpoint. Palo Alto is trying to be even broader to cover most areas, including endpoint. It doesn't really have something, I guess, that's great in email security today.

How attractive is that type of vision, that a Palo Alto could go very broadly? Or, really, Microsoft. They're another good example of an organization that has a cybersecurity suite that could almost go end to end. Do you prefer to stay with those pillars and having a leading vendor in each one or could you imagine a case where you could try to go to more of a single shop vendor that can give you access across everything like a Microsoft or Palo Alto?

Kristie: Yes. We actually did our Microsoft renewal this year. So we got the Microsoft pitch on Defender and really did the deep dive there. From a performance perspective, it just doesn't compare to the best-in-class tools, especially for those particular

pillars. There's also, of course, the risk of consolidating everything to a single tool and putting all of your eggs in the Microsoft basket in case that doesn't go well, similar to the CrowdStrike event where everyone got the blue screen a year or so ago, whenever that was. So that's the areas where we'd like to diversify.

We'd like to keep those three pillars independent, representing best-in-class, and then find opportunities where maybe our email security provider can also do our phishing training instead of having a standalone security awareness training platform. Maybe our endpoint tools can give us more... CrowdStrike with their Falcon Exposure Management can do a lot of vulnerability management. Identity Security can really expand out from the platforms that they've been adding. That's given us some opportunity to do some more tool consolidation.

PW: Yes. It's interesting you bring up identity as part of that. I was literally just with the executives of CrowdStrike and they consider identity... Obviously, they have some identity pieces, but they consider the identity as a separate pillar. So they would look to an Okta or others to provide the underlying identity infrastructure. How are you thinking about identity as part of that overall stack and set of pillars? Do you see it as something that can be brought under one of them or it really does remain its own beast but intersects with the others?

Kristie: I think as the shift to remote work and the idea that the identity is the new perimeter-type of phraseology that's been used a lot, I think that identity does need to stand on its own. Unfortunately, the program that I've inherited has a legacy identity tool for IGA that's probably not representative of best-in-class anymore, and it's really fallen behind, especially when it comes to managing non-human identities and some other critical features that are important for our business.

So that's probably an area where we're going to have to do some significant transformation to be able to support the business going forward. That's also an area where, if you have a stronger identity tool that can also... Right now, I have a separate tool for MFA and a separate tool for PAM and a separate tool for EPM. So, if I can build a better, stronger identity foundation, I can start to roll some of those into a single identity platform and I won't rely on all these one-off tools that I have today.

PW: Well, my old boss, who leads product at SailPoint, will be excited to hear that people are looking to get to best-of-breed there. Sean, saving the best for last, right? We'd love to hear a little bit about how this budgeting conversation has evolved in your organization. How are you getting these dollars? Because it sounded like you guys are having a material step up. Where is that coming from and how much fighting does it take to get that done?

Sean: It's mostly with the CFO I've got the fight with because I do wear both hats. So I am the CIO of the company. So that does help a little bit when it comes to budgeting. I said maybe a $12\%$ increase. A lot of that is just going to be reallocated from the IT infra side as we continue to move off of traditional to AWS.

We're not backfilling some roles, so we're offsetting that increase, either sunsetting older platforms that we don't need or transitioning to open-source tools to save some money. We did have a net increase of about 5% of spend across the board, but we're adding about 7% for the security side. That's transitioning away from the infra side. We're using the automation tools that we've enabled with AI to pay for that. I think it's been pretty easy to do, with all the work we've done in the last year, to set up for that success on that side.

PW: So, effectively, there's some internal reallocation within your CIO hat from some of the legacy systems. Were you also able to get incremental budget, just top-down, beyond that from the CFO or has it been mostly forced within your CIO envelope?

Sean: Yes. It falls under the CIO envelope, but we got about 5% for the year. Then we're just shuffling the balance to make sure that we can meet the security need at this point. Because we identified the gaps and we decided, based on what we're deploying with automation and the open-source tools, we're able to reallocate those funds.

PW: What are the places that you're pushing most of those incremental dollars in terms of some of the cyber pillars?

Sean: Well, for us, some of it is actually mail because we run a hybrid system. We run multiple systems. So we're trying to get more visibility on that front, but then we're also doing in-house development on some tools from the end point because we're lacking at the DLP side.

I think every time we've looked at a tool from the DLP perspective, it's very difficult, at least in the insurance sector, because of the data elements we have. We have so many false positives. We went through two different tools, spent a lot of money, and weren't really able to get to a point where it was valuable to us. So we decided to bring it in-house. So, right now, it's mostly

going towards DLP at this point.

PW: And that's something that you're having to build in-house. What are the weaknesses? Obviously, you've got a lot of different vendors that are out there trying to say, hey, DLP is part of it. You brought up email. Obviously, email vendors have it. You look at security service edge, and they're going to tell you they have it. What have been the limitations of working with the existing vendors that has forced you to actually have to shoulder this yourself?

Sean: Yes. We just can't model the data elements in a way that allows us to have good reporting on what is happening with the data. There's so many false positives. We spent months on both different tools, and we weren't able to get to a point where it was functional, and so we just decided to take it in-house. So we built an agent platform that we deployed at all our endpoints now that gives us complete control over how we monitor the endpoints on top of our other endpoint protection. So we run a blended Sophos with CrowdStrike.

So we run a couple different things. We like a multi-layered approach to how we handle the security. But this just gives us the ability to customize what we can see at the endpoint. We can see everything that happens down to the kernel on the endpoint, and we can set rules around that within that endpoint monitor. That's just been the best fit for us now, short-term. Now, we're still looking for other tools to come in, again on the AI side, but we haven't found one that's a really good fit for our deployment.

PW: And if you think through the lens that Kristie was getting at, she thinks of cybersecurity around a few pillars. She mentioned email and communication, endpoint network, identity as core pillars that they invest around but are consolidating. How consistent is that strategy with how you think about it? Are you approaching things differently?

Sean: No. That's about right. We leverage Okta on our side. We've been with them four years. Great product. It's really made our lives a lot easier on the security side. I think that that was a big change for us with all the workflows and everything that they support. It's a great product. But I think the pillars are right the way she laid them out and how we approach it.

PW: Interesting. Given that you brought up Okta, identity is a space that feels like it's getting its day in the sun right now where there's a lot of question about how we should approach identity with the new complexity that comes in around building agent. In your case, you probably have a customer-facing application, so you also have customer access to agents and applications. How are you seeing that evolve? Because, at least if I think through the narratives that are out there being debated, obviously you've got an Okta doing both customer and worker identity. They have a broader platform, so you could use PAM and IGA solutions from them. But you've got others like CyberArk out there trying to argue that you need a purpose-built, PAM-like solution to do Least Privilege Access and composable password access with agents. You've got a tremendous number of startups out there that are all approaching this differently. How has GenAI, both from the customer utilization of your tools as well as your internal use of tools, changed your thinking around identity and how you might have to evolve that looking forward?

Sean: Yes. That's a good question. We're still trying to work through that. We do have a couple platforms that we're working on, but we're still working to deploy those. We are working through those security issues that we see and how we're going to deploy agents within client systems and manage those on the identity side. We do run a PAM, but, again, that's just for most of the folks. Everybody in our enterprise has tokens, right? So we run the YubiKeys across the enterprise. The software-based MFAs were problematic for us. We were getting a lot of attacks on that front. So we decided to go with the YubiKeys and that's been good for us. But, yes, I think we're still working through. As engineering builds out these platforms, it's a moving target. We're not able to discern which way to go forward with them yet because, even though we're trying to get things launched, we don't know where they're going to end up yet.

PW: Well, I think maybe this is a great way to segue into the second half of this conversation where I think we wanted to talk a little bit about the changing IT requirements because of AI. I guess maybe we should really split that conversation into two sides. One is the increasing velocity and sophistication of attacks and the risks associated with those. I, tongue in cheek, put Mythos into the title of this note, but obviously we have Daybreak coming out from OpenAI. Nobody wants to be left behind on saying that their tools can be used to attack anybody. So there's the inbound side, but then there's also your internal infrastructure. Maybe it would be helpful to start with just, where is your organization in its own journey of adopting AI, just as context for what the cyber footprint needs to be to deal with that risk?

Sean: Yes. So we've got two different segments. We have the engineering folks. Obviously, they leverage Codex and code, and that brings a certain level of complexity around vectors. Then we have the general operations folks and admin folks. We separate those. We run them on different tenants, essentially, so we can maintain those and have a little bit more control over them. From my perspective, we're still in our infancy from a general deployment. Engineering is far ahead and keeping governance on them has been a challenge. None of the engineers like to have any kind of endpoint or anything on their machine. That can get

frustrating sometimes, but they come around a little bit.

PW: Are you using Copilots or anything on the desktop like Microsoft?

Sean: Yes. So we use all the models. We make those available to all the teams. Now, the engineers are again separate, but I'm just talking about the regular folks. They have access to those today, but we don't allow them to generally have all four. They have to have a business case and, depending on what they're going to do, we're going to assign them either Copilot, ChatGPT, Gemini, or Claude. But Claude has been definitely the front-runner the last two months. I would say 90% of the requests are for Claude and Cowork. Their integrations have really set them aside from everybody else. They've got HubSpot and Office 365 and Monday and all the MCP connectors are great. Everybody wants them. What we're bumping into, obviously, is the token utilization. That has gone up. We were hitting our limit in Claude on the 28th of March. By June, we were hitting it on the 3rd of June. So it increased that much. But our user numbers only went up about 30%. So, as the users become more adept at the tools, they're building skills and agents, and they're doing all this stuff. Then they say, well, I'm getting an alert that I've run out of tokens. But on the other side, the security side, we're trying to wrap our heads around, what are they prompting? What are they doing? What's the output? What's the point? Are they just creating artwork? Where's the ROI to the company? I think we haven't seen that yet.

PW: How are you doing that? If I listen to the vendors, if you go to a Palo Alto or a CrowdStrike or a Zscaler, each one of them are talking about having an agent at runtime on the desktop, whether that's a Prisma AIRS, or AIDR that CrowdStrike bought, or Red Canary that Zscaler has brought in-house. Is that the direction that you think you need to go? How are you thinking about dealing with evaluating everything from the prompts and being able to have a handle on this?

Sean: Yes. We're going to be deploying an AI router within our environment, so all the folks will basically go through that portal. That gives us complete control over token utilization, LLM direction, and prompt monitoring at a good level that we'd feel comfortable with.

Then, obviously, from a costing perspective, we run some local LLMs. Some folks only need a local LLM. They don't need Claude. They don't need Fable. It just depends. So we're deploying those now. We've been testing. They work really well, and I think that's going to allow us to have really good oversight and governance on how the tools are used.

PW: Yes. Spending 1/20 or 1/30 per inference is pretty nice.

Sean: Well, it's the Uber, right? They ran out of AI budget. It's great, but, again, where's the ROI? If you're out of tokens by the third day of the month and what we're seeing with the subsidies coming down from the AI models, that party is going to end unless the cost continues to drop, which we'll see. The adoption is so much faster, obviously.

PW: So, at least right now, it sounds like a hub-and-spoke model. So you're at the router level as opposed to really using some of these concepts, like I mentioned before, like Palo Alto or the secure service edge.

Sean: Yes. We're just not at a point where we're going to leverage those. We looked at some of the tools and it was cost-prohibitive for us, based on our budgeting today. Now, next year, I will say that, just from an IT spend, though, we are not signing any deals longer than a year anymore, just across the organization. Our PDF provider, we did a one-year because I don't know if we'll need it next year. Same with our endpoint security. We just renewed with our EDR solution, but we only did a one-year because I don't know what it's going to look like next year. That product may not fit the bill and I don't want to be locked into a three-year term.

PW: Interesting. The funny thing with you bringing that up... I didn't intend to pull the thread on this because I want to get to the others, but the perception from the EDR vendors is, there's a lot of vendor lock-in because of all the customization and rules and everything you build into them. But I think how you just described that is, you make it seem a lot more achievable to reconsider your EDR vendors. How real would that be and the ability to move away from them?

Sean: Yes. Well, nobody likes forklifting off to another if you've got thousands of endpoints and you're entrenched in a tool that you've been using it a long time. But at the end of the day, the reality has changed and it changes every day now. So we will just do it if we have to do it. We have to be right 100% of the time and we're not. So I think, in that regard, we've just got to be flexible. If there's a tool that's going to be better that can fit the bill, even if it's a little more money, we're going to have to move in that direction.

PW: Yes. Kristie, maybe we pick up where Sean is there on a couple of different things. You aren't as much on the CIO side, so maybe you have a little bit of less perspective on the length of contracts, but it would be interesting even to hear from the cyber side on that. But I think more broadly, just from a context standpoint, how is AI being adopted by the organization or changing your perception around risk from attackers coming in?

Kristie: Yes. Just a few things that Sean said that I just want to comment on. We saw the same uptick in our AI token utilization. I think that, actually, Microsoft Copilot did some recategorization starting June 1st and that really hit us hard. Similarly, we're getting engineers coming back after three days and saying that they don't have any more tokens left to do their job. So we're looking at doing more, trying to enable more an on-prem LLM through a Llama model to try to give them the opportunity to do coding, but we're probably going to have to upgrade a lot of laptops to be able to get that kind of horsepower on an individual device to be able to run a large language model, not just some of these smaller ones. That was one I just wanted to add to, but going back to your question in terms of, how are we preparing for... Could you repeat it for me one more time?

PW: Yes. So I guess one piece of it is, it sounds like you've got Copilots running both for developers and for business workers. How are you thinking about securing those, monitoring what's going into the prompts, making sure that business secrets aren't being leaked, things being done poorly? So I think there's one around that that maybe we start with.

Kristie: Yes. So we've built an AI security framework that we're working off of now where we have areas where we want to make investments in endpoint, network, data, identity, and our DevOps environment on the product side. Probably some of the easier ones... The endpoint and the network are really just looking at the tools that we have in place today. So we're a CrowdStrike and a Zscaler shop in that sense. They have products that you can use to try to evaluate what prompts people are using. We're also looking at Varonis from a data security perspective, we don't have that today, to try to get more visibility into what people are using it for. How are they using it? What data is being put into it? How can we protect it? Then, also on the receiving side of, what data is being returned back to them from our environment? Should they have access and permission to actually view those files? So, looking at it across, again, those primary tiers.

PW: Yes. So it sounds like, for the endpoint, you're either looking at it through the web security, the Zscaler lens, or the endpoint lens, which was a little different from Sean, who was doing more of the hub-and-spoke where they're doing it more at the token routing level. What makes having that runtime security on device attractive? How do you make that decision between what your secure service edge can do relative to, say, what the endpoint agent could do?

Kristie: Yes. I think CrowdStrike would give us visibility at the endpoint to see what shadow AI exists out there, what people have put on their local machine. Are they doing a local egress of data? Do they have any unsanctioned tools or browser extensions that could potentially be used to exfiltrate data directly from the device? Then, any internal AI-operated tools, MCP, improper prompt management, that type of thing all can come out of CrowdStrike on the endpoint. Then the network security from Zscaler would be more of the uncontrolled egress, so what data is leaving the environment without inspection or without hitting the DLP.

PW: I think you had mentioned before that you also have a network security pillar, but it doesn't sound like you're using the types of things that Palo Alto does with a Prisma AIRS. That's not the direction that you're thinking. It's more around the secure service edge and endpoints. So it's really much more attached around the user agent, the end users.

Kristie: Yes, exactly. We want it to be more individual user-based just because of the breadth of the company, right? Trying to manage that many people, trying to manage how tokens are being routed across 25,000 knowledge workers... That's very challenging.

So it really has to be building guardrails that can be put across the organization so that whatever tools they're using, whatever LLMs they've deployed, whatever SaaS tools have been approved can still be protected. So we're still managing our data independent of what the direction of AI is by the business.

PW: Sure. That makes sense. How have you had to change your cyber posture as a result of more of the inbound risk? So, whether that's the risk of, for instance, a Mythos or Daybreak at the application security attack side or at the phishing and a whole variety of other attacks, the sophistication and volume of those.

Kristie: Yes. So I think we're looking at basically modernizing our entire tool stack in that vein. So, right now, we have a fully outsourced MSSP for our security operations center, and we're looking at basically switching that to an agentic SOC or heavily subsidizing that with being able to operate at machine speed in the age of Mythos. A three to four-hour time to triage is no longer acceptable when the mean time to exploit is four minutes. So you need to be able to operate faster. That's one area that we're making changes in in the near term. That's an area we're going to make investments.

PW: How are you doing that? Obviously, there are startups out there like Torq, but then you've got the vendors you were talking about before with CrowdStrike launching Charlotte, and others. How are you thinking about that agentic SOC and where you bring those agents, and who is well positioned to support you?

Kristie: Yes. So, right now, we're looking at Torq and Prophet. And it seems like Prophet, at least out of the box, has more capability. Torq is maybe more customizable, but we don't have the manpower to necessarily build all the playbooks. We need something that works more out of the box and just operates off of the MITRE Attack framework and best practices. So we'll probably end up with a tool similar to that that can help us operate at that speed.

PW: Now, why go with a startup, though, versus going with CrowdStrike or some of these that are being built by the existing vendors?

Kristie: Honestly, because it seems cumbersome when it comes out of the existing vendors. They're building it on their legacy platforms and on their legacy technology, and it's not necessarily built to be an independent agentic AI by itself. It seems like they don't really necessarily have that as best-in-class capability. So we're trying to keep that independent so that we still have the benefit of CrowdStrike and the protections that it's providing on the endpoint, but the decision-making is happening from a different tool. It also gives more flexibility. CrowdStrike isn't as great at integrations across all these other tools to ingest all the data. So it's easier to just push it to a third party, essentially, like a Prophet or a Torq.

PW: Yes. This is what I've heard. The Switzerland aspect of a Torq or Prophet... They're the natural fit in this area because they need to work across multiple cyber pillars and trusting that to one of the vendors from one of the pillars is not as effective.

## Kristie: Yes.

PW: Raj, I know we don't have a ton of time left, but how has AI impacted the technologies that you're having to think about securing, whether it's Copilot or the application of AI for the agentic SOC?

Raj: So we've had to look at our existing tools over the last few years and augment a lot of them in a lot of areas. So I would think, in my case, it's similar to what Sean said. We're following the hub-and-spoke model, trying to enforce governance at an enterprise level. So, over the last few years, looking at all the AI initiatives that were happening internally within the organization, we've deployed several tools purpose-built for AI monitoring. So we have a tool, I don't know if people are familiar with that, called Aim Security. It was a company that was bought by Cato Networks earlier this year. That essentially is our AI prompt monitoring and firewall platform. So we use that to ensure that there's no data exfiltration or prompt poisoning or prompt engineering going on as people interact with public LLMs from our internal applications.

PW: By the way, on that one, do you use Cato Networks more broadly or you just use that product that they had acquired?

Raj: No, just that product. In fact, in full transparency, we probably will be looking at other alternatives down the line which are more comprehensive as the market evolves. But, last year, that was one of the more mature products in the market. So we signed up for that and it's delivering on the initial objectives. Then I think, on the agentic SOC side, we actually use Tines. We're a Tines shop. So Tines is very similar to Torq, and they are coming up with some innovations around the agentic SOC capabilities and autonomous response. So we are testing that right now. I think the biggest hurdle is to get the business comfortable with autonomous response. Because sometimes there might be false positives that would cause a certain server or service to be contained. So we're having those conversations and making sure that we're fine-tuning our internal policies and autonomic response. Then, finally, like others, we have CrowdStrike. We have Wiz. We have other tools that also have autonomous response capabilities. So we are starting to leverage those in certain areas to make sure that we can respond to these attacks that happen at machine speed.

PW: And do you use Tines to coordinate across those, so it's like agents talking to agents? How do you use multiple different agent platforms in parallel?

Raj: Right now, in terms of the cyber defensive agents, Tines is the only one that we use that has the agentic capability. What we do is, we stream all the signals and alerts from other products and solutions to our SIEM. We actually have a Cribl implementation, if you're familiar with Cribl. It provides that real-time log streaming. Part of that is monitored by Tines where we built the policies and the use cases and, based on those use cases, if the agentic processes in Tines sees something that needs an autonomous response or an escalation, it triggers the workflow.

PW: I know we only have a couple minutes left, so maybe we'll do a quick lightning round of each of you before we end. I guess, Raj, because you've been with us, I'll ask you first. What have been three vendors that have impressed you the most this year and why? And maybe the other side, which vendors on the negative?

Raj: Sure. So I think Wiz is one of our key pillars. We're a hybrid environment. We've got a pretty big cloud platform. So Wiz has just been a great partner with all the stuff that they're doing and coming up with, the new innovations and capabilities. CrowdStrike has been a mainstay of our security program for years and so we really depend on that. Then, recently, Palo Alto has done quite a good job of coming up with stuff like agentic registry, MCP gateways, and those capabilities that we're looking for at the enterprise level.

PW: On the negative side, who has been disappointing you lately?

Raj: I would say maybe just one, Microsoft. We've had a lot of conversations with Microsoft. Their solutions and their concepts and roadmaps look good on paper, but, during implementations and testing, they really haven't panned out. I think it's going to take them some time to get to the top of the stack.

PW: And Kristie, the same. Who are two or three vendors that have impressed you this year?

Kristie: Yes. I think, going in a different direction, I agree with what Raj said, but we've been looking at a lot of the startup companies to try to fill some of our needs. So we're looking at Remedio for vulnerability management and patch management configuration. We are switching to Frame for our security awareness training and phishing training. They can do a lot of really good AI-generated quick videos for custom training.

PW: And you were with KnowBe4 or something else before, or what were you before?

Kristie: Yes. We're going to switch off of KnowBe4 to go to Frame.

PW: And what was the third vendor you were talking?

Kristie: I guess I would reiterate CrowdStrike. I think they've been a really good partner in this space and they've been pretty dynamic, I think, in their investments and the capabilities they're asking. I think it just becomes, everything's another module, another bolt-on, another chunk of money. It just becomes frustrating.

PW: Gotcha. So that's more on the negative side, I guess?

Kristie: Yes. I would say another underperforming or underwhelming vendor is Proofpoint. I don't think they've made a lot of investments in the last couple of years to really stay top of best-in-class. So it'll be interesting to see what happens to them over the next couple of years. Then, our identity provider is One Identity. They won a head-to-head competition five years ago to get this business as best-in-breed for our environment, and they have just stagnated and dropped off completely. So it's been a real challenge to work with them as well.

PW: Who do you think you might go to instead?

Kristie: Probably a Saviynt, a SailPoint, even a Pathlock, anything that's more leaning into, again, like I talked about at the beginning, managing non-human identities, managing inherent segregation of duties, things that are just part of normal business operations instead of just movers, joiners, and leavers.

PW: Yes. Sean, who has impressed you the most this year?

Sean: I'd say Okta and CrowdStrike. They're keeping up with the paces. Those are the last two I've really talked to about product changes, but they're doing what needs to get done. On the disappointing side, 7AI. I spoke with them, it seemed like a really great product, but they didn't have any control over their costing. We got it and the cost was 10X what we thought it was going to be. It just didn't make any sense. Then, Zenity was the other one. It again seemed like something that was really good, but I don't think they were thinking through the whole picture of agentic AI. They definitely had some gaps and they didn't have answers to them. So I think, again, it's a moving target and everybody's trying to answer all the questions, but they can't. I think a lot of them are getting spread out a little too thin.

PW: I appreciate it. Well, thank you so much, you all, for joining. I know we went a couple minutes over. Audience, if you have any questions, please reach out to me. I'm happy to chat about all of this more. All of you, I look forward to continuing our

conversations into the future.
