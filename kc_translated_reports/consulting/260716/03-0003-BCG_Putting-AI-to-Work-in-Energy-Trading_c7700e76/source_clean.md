# Putting AI to Work in Energy Trading

By Wade Barnes, Sébastien Rexhausen, Antti Belt, Matthew Abel, Smith Sangiambut, and Anna Temple

ARTICLE JULY 15, 2026 15 MIN READ

Energy trading will not be transformed by a single AI solution. Electric power, pipeline gas, liquefied natural gas, physical liquids, and financial energy trading operate at different tempos, with different constraints, data structures, workflows, and sources of advantage. As AI moves from pilots into live trading workflows, those differences matter more than ever.

The implication is clear: build a common AI foundation, but tailor deployment by commodity, workflow, and AI capability. (See “Four AI Capabilities.”) In power and financial energy trading, where markets are more quantitative, most value comes from predictive AI, optimization, automation, and risk analytics. In pipeline gas, LNG, and liquids—more physical and logisticsheavy markets—the larger opportunity lies in using agentic AI to turn operational, contractual, and approval-heavy work into structured, controlled execution.

## - Four AI Capabilities

In this article, AI encompasses four capabilities:

\- Numerical analytics and optimization techniques that identify feasible or optimal decisions under physical, commercial, risk, or logistical constraints

\- Predictive AI and machine learning models that learn from historical and real-time data to forecast prices, flows, exposures, volatility, outages, anomalies, or operational conditions

\- Generative AI, including large language models, that interpret, summarize, generate, and transform text, code, documents, and other unstructured information

\- Agentic AI systems that combine models, data, tools, and workflow orchestration logic so they can observe conditions, plan next steps, operate systems, prepare actions, and escalate exceptions under human supervision

Numerical optimization and predictive AI have been used in trading for years. The newer opportunity is GenAI and agentic AI, especially where trading teams rely on fragmented documents, emails, approvals, broker messages, inputs from energy trading and risk management systems, credit checks, risk workflows, and manual handoffs. The practical question is not “Where can AI replace traders?” but “Which type of AI belongs in which workflow, and how should it be governed?”

Although not the focus of this article, the data layer and data architecture that support AI capabilities are critical enablers that should not be overlooked.

While straightforward in concept, this is demanding in practice. Data integrity, governance, and model discipline must be standardized across the organization without undermining the ability of traders and analysts to innovate. Across all markets, the goal is not to replace existing systems but to build an intelligent layer that helps teams operate them faster, more safely, and with better control.

## The Sources of Value

BCG's analyses indicate that the value at stake is substantial. For example, oil and gas companies taking full advantage of AI could deliver incremental profits equal to as much as $30\%$ to $70\%$ of EBIT over five years.

This estimate is not trading specific, because AI will drive increases across energy value chains in fundamentally interconnected ways. Yet it illustrates the scale of value unlocked when AI is embedded into core business workflows rather than treated as a standalone tool. In trading, the same principle applies: the most incremental value is captured when AI improves margin, control, speed, and cycle time across the transaction life cycle.

Trading organizations are deploying AI to pursue this value in multiple ways, including the following:

\- Rewiring Process-Heavy Workflows. Much of the near-term value will come from applying AI to workflows that support trading: onboarding products and counterparties, checking credit and completing know-your-customer processes, securing approvals, confirming transactions, reconciling breaks, and managing exceptions. These workflows are often manual, fragmented, and heavily reliant on controls. GenAI can interpret the information; agents can move the work forward.

\- Improving Commercial Decision Making. Predictive AI, machine learning, numerical analysis, and optimization can improve forecasts, exposures, dispatch, hedging, execution timing, and asset optimization decisions. This is the value pool most directly tied to front-office margin, but it is not the only one.

\- Turning Fragmented Information Into Competitive Edge. Proprietary advantage increasingly comes from using messy information faster and better. Broker messages, contracts, plant-level or unit-level operational notices, shipping documents, and market color become valuable only with context and when converted into signals, decisions, or controlled workflow actions.

\- Strengthening Controls. AI can detect anomalies and breaks, explain P&L movements, and monitor trading limits in real time. It can also support the valuation of complex originated transactions, streamline middle-office reviews, and improve audit quality and coverage. The prize is not just lower cost. It is fewer errors, faster resolution, and less margin leakage.

\- Accelerating Technology Delivery. AI can help accelerate the build-out of data pipelines, testing and back testing, enhancements to commodity trading and risk management systems, and model documentation. The value arises from faster conversion of trading ideas into governed production capabilities, not generic coding productivity.

Impact concentrates where AI sits directly in the flow of work. A better forecast creates value only if the trading desk can act on it. A document summary creates value only if it accelerates an approval, reduces an error, or moves a transaction forward. A model output creates value only if it is connected to decision rights, controls, and systems of record.

This is where agentic AI changes the operating model. Agents do not simply produce recommendations; they help execute the work around the recommendation, often facilitated by AI orchestrators. They retrieve information, check rules, prepare actions, route approvals, and escalate exceptions. The goal is less repetitive work, tighter controls, and faster execution on the basis of human judgment—not the replacement of traders or the systems they use.

## The New Infrastructure Layer: Agents Operating Existing Tools

To make this practical, firms need a trading IT architecture that connects AI to existing systems rather than bypassing them. Trading firms have plenty of tools. The problem is that people still spend too much time moving between them: copying data, chasing approvals, reconciling entries, and proving controls. The next step is not another standalone tool but an AI agent layer that can operate across trading, risk, operations, credit, compliance, and technology workflows with clear controls.

Architecturally, the separation of roles matters. Existing trading platforms remain the systems of record. Shared AI platform services provide the models, retrieval capabilities, and risk policies and limits that agents can access on demand. Agents then become the orchestration layer between users and systems: they prepare actions, route approvals, update records where permitted, and escalate exceptions under human supervision. (See Exhibit 1.) This makes AI practical without requiring firms to replace the core trading stack.

Agents Create an Intelligent Operating Layer Across the Energy Trading IT Stack


[[KC_IMAGE_001]]

Source: BCG analysis.

Consider a broker-to-book workflow. An agent reads a broker's trading message, extracts the key terms, checks whether the product and counterparty are approved, prepares the trade entry, runs basic risk and credit checks, routes it for approval, and drafts the confirmation. In cargo operations, an agent could spot a missing document, a scheduling conflict at a terminal, or rising demurrage costs before margin is lost.

This changes the operating model. Traders and operators spend less time navigating multiple disparate systems and more time supervising decisions. Firms will need clear rules for what agents can do on their own, where they can only prepare actions, where human approval is required, and how every step is recorded for accountability.

# Adoption Is Uneven, with Leaders in Integrated Workflows Pulling Ahead

Adoption varies across markets, but AI is not advancing along a single path. Power, pipeline gas, and financial energy trading are generally further along in predictive AI, optimization, and

automation because they have longer histories of quantitative analytics and repeatable decision loops. LNG and physical liquids often have more opportunities to apply GenAI and agentic AI because their pain points relate to the work supporting trading rather than generating signals. The real divide is between firms embedding AI into integrated workflows and firms still running isolated pilots.

A recent BCG survey highlighted differences in adoption among trading organizations in power, pipeline gas, and physical liquids—the markets for which directly comparable benchmark data exists. (See Exhibit 2.) Power and pipeline gas traders lead in adoption, reflecting the fundamentally numeric nature of their work. (The survey covered automation, analytics, and advanced AI use cases; it should not be read as a GenAI or an agentic-AI maturity ranking.)

## EXHIBIT 2

Power and Pipeline Gas Traders Lead Physical Liquids in AI Adoption

Respondents reporting deployment of automation, analytics, or advanced AI in their organizations (%)

[[KC_IMAGE_002]]

Source: BCG power and gas trading survey, 2024–2026.

Adoption patterns across markets are not simply a matter of digital maturity or budget allocation. They also reflect differences in the data and architecture investments required to make AI usable at scale—and the fact that early adopters building these foundations have an advantage that competitors cannot quickly replicate. Across markets, AI returns depend not only on model quality but also on whether firms have created decision-grade data, integrated workflows, and technical architectures that allow insights to move into action reliably. In practice, firms are using AI agents to validate, clean, and structure high-volume operational data so that errors and anomalies in live data feeds do not propagate into models responsible for commercial decision making.

These investments matter because advances in AI trading are cumulative. Firms that invest earlier in data models, system integration, and workflow-oriented architecture can deploy use cases faster, scale them more safely, and improve them over time as more decisions run through the system. Laggards find it hard to catch up quickly. In addition to investing in technology, firms must harmonize data definitions, integrate trading and operational platforms, and implement control frameworks that allow AI outputs to be trusted in live commercial decisions.

Once that foundation is in place, the sources of value differ by commodity. In some markets, the analytical engine matters most. In others, the bigger prize lies in orchestrating workflows around documents, approvals, operations, and controls.

## AI Creates Commodity-Specific Advantages

Building a durable advantage starts with understanding how AI creates an edge in specific commodities.

Power: Improving Decision Speed, Risk Management, and Portfolio Control. In electric-power markets, advantage comes from turning forecasts, constraints, and risk signals into disciplined action across hundreds or thousands of trading, dispatch, scheduling, and portfolio decisions. These markets are granular, subject to constraints, and highly time sensitive: transmission limits, nodal or zonal pricing, congestion, outages, load forecasts, and intermittent availability of renewable energy can create opportunities and risks that change quickly.

The main applications of AI are predictive AI, numerical optimization, and automation, rather than GenAI and agents. Many desks already have credible congestion, pricing, dispatch, and load-forecasting models. The differentiator is embedding those models into live workflows to refresh exposures quickly, route alerts to the right people, control approvals, and enable trading, risk, and scheduling teams to act at market speed without losing discipline.

GenAI and agents are more relevant in adjacent workflows, including P&L explanation, risk decomposition, product onboarding, portfolio monitoring, market rule interpretation, and exception escalation. An agent might summarize why P&L moved, identify which assets or constraints drove the change, prepare a risk commentary, or route a limit exception for approval.

More advanced tools, such as AI-empowered digital twins of optimization systems or autonomous decision support tools, are not yet the main source of value in most power markets. They are, however, gaining traction in parts of Europe where hydro portfolios and similar complex optimization problems make them more relevant. In those settings, AI can help evaluate asset constraints, optionality, and dispatch choices across a wider range of scenarios.

Pipeline Gas: Enhancing Operational Intelligence. In pipeline gas markets, advantage is shaped less by trading speed than by the ability to read a changing physical system. Pipeline constraints, storage levels, nominations, and maintenance events continually reshape regional supply and demand.

The core AI use case is operational intelligence. Predictive models and optimization tools can translate physical system changes into better storage, basis or locational spread, transport, and hedging decisions before those shifts are fully reflected in price.

GenAI and agents matter most where operational information is fragmented. An agent can read a pipeline or transmission system operator notice, interpret a nomination update, identify affected positions, check contract rights, and route an exception to the right trader, scheduler, or risk owner.

The goal is not to replace the tools that gas desks already use. It is to add an agent layer across scheduling platforms, energy trading and risk management platforms, risk systems, and communications channels so teams can act faster, reconcile less, and preserve control. The main barrier is usually not model sophistication but the quality and consistency of operational data.

LNG: Evaluating Options. LNG trading has distinct economic logic and time horizons. Margin depends on where each cargo can go, under what terms, at what cost, and with what hedge. Arbitrage opportunities can look attractive on the screen but disappear once freight, terminal access, credit, and contractual limits are considered.

Predictive models and optimization tools help traders evaluate cargo options faster and more systematically. They can compare routing, timing, freight, storage, and hedge alternatives so desks can capture value before spreads or capacity windows move.

Optimization models serve distinct purposes across time horizons. Over the long term, they simulate a range of price scenarios to quantify the intrinsic and extrinsic value of supply, demand, and logistics positions. Over the short term, they are deployed to commercially optimize annual delivery programs, shipping schedules, and trading opportunities on a portfolio basis.

GenAI and AI agents are especially relevant because LNG relies heavily on contracts and approvals. An AI agent can interpret terms of sales and purchase agreements, surface destination or volume flexibility, prepare approval materials, test whether a diversion is permissible, and route exceptions to the right owner before execution slows.

The biggest challenge is fragmentation. Contract terms, cargo schedules, vessel status, approvals, and risk positions often sit in different systems. The frontrunners build a portfolio view across those elements and use AI to move from optionality analysis to controlled execution.

Physical Liquids: Managing Cargo Optionality, Risk, and Operations. In physical liquids—crude oil, refined products, and natural-gas liquids—value creation depends heavily on identifying options and executing effectively. Cargo timing, blending, inventory, product specifications, and contract terms often matter as much as price direction.

These markets are less suited to pure algorithmic trading than power or financial markets. The bigger near-term prize is gaining visibility into what can move, when it can move, under which specifications, and with which approvals. That same visibility can also help identify cargoes at risk of becoming distressed, allowing owners to intervene sooner or other market participants to recognize opportunities to capitalize on before they become widely apparent.

GenAI and agents can turn messy communication into a controlled workflow. A broker message becomes a structured trade entry. An unapproved product or counterparty becomes an exception. A missing document or demurrage risk reaches the right owner before value is lost.

Predictive models and optimization still matter, especially for refinery slates, blending economics, inventory positioning, logistics, and contract optionality. But the edge in physical liquids comes from connecting commercial decisions with operations, risk, credit, and logistics—not from faster directional trading alone.

Financial Energy Trading: Optimizing Signals, Research, and Controls. In financial energy trading, value creation depends on converting information into risk-adjusted positions quickly and consistently. These markets are deep and transparent, so advantage rarely stems from data access alone. It comes from knowing which signals matter now and sizing positions with discipline.

The most relevant AI applications are predictive AI, numerical analysis, and optimization. Models can combine market structure, price behavior, positioning, macro indicators, and proprietary physical signals to classify conditions and identify higher-conviction opportunities. Execution tools can then help optimize order placement and manage market impact.

GenAI and agents are more useful in supporting the trading workflow than in generating the underlying signal. They can summarize market developments, accelerate research and back-testing, draft risk commentary, support model documentation, and route approvals or limit exceptions.

The main risk is false precision. Financial markets generate enormous amounts of data, so weak AI models can overfit to patterns that do not persist. The firms advancing fastest link research, execution, and risk into a single loop: rapid experimentation, disciplined controls, regime detection, and fast feedback on trading-signal quality and performance.

# Standardize the Foundation, Tailor the Edge

Although these markets should monetize AI differently, they all require the same foundation: trusted data, disciplined governance, and integrated workflows. Without that foundation, even strong models remain disconnected from the decisions that move risk, optimize assets, and drive financial results.

Firms that have already built decision-grade data, linked core trading and operational systems, and embedded controls into workflows can deploy AI use cases faster, scale them more safely, and improve them over time. Firms starting from fragmented architectures face a slower and more expensive path because each new use case must overcome the same underlying data and integration gaps.

Some AI capabilities are already becoming table stakes. Coding copilots, generic forecasting, document summarization, and basic automation will improve productivity, but they will not create a sustained advantage on their own. A durable edge will come from the capabilities that are harder to build and replicate: proprietary data, commodity-specific models, redesigned workflows, and controls that allow AI to move work safely from insight to action.

The most effective starting points vary by commodity but share three characteristics: a clearly defined value pool, a workflow that repeats frequently enough to improve over time, and data that can be made sufficiently reliable to support decision making. (See Exhibit 3.) By prioritizing these entry points, firms can embed AI into the decisions that matter most for generating returns in each market.

EXHIBIT 3 High-Value Entry Points for AI in Energy Trading

[[KC_IMAGE_003]]

Source: BCG analysis.

As volatility and operational complexity rise, AI is becoming central to how energy-trading organizations compete. But the edge will not come from applying a generic model across every market or replacing the systems traders use today. It will come from embedding the right AI capabilities into the workflows that move decisions into action.

Leaders will build an intelligent operating layer across existing tools. Predictive AI and optimization will sharpen the market view. GenAI will make unstructured information usable. Agents will move work through systems with controls and escalation. The compounding advantage is simple: better data improves models; better workflows create cleaner feedback; cleaner feedback makes the next trade faster, safer, and more valuable.

The authors thank the following colleagues for their contributions to this article: Johannes Große, Sönke Lorenz, Martin Elxnath, Jay Barnard, and Stephanie Bachas-Daunert.

## Authors


Managing Director & Partner
Denver


## Antti Belt

Managing Director & Senior Partner; BCG Institute Fellow Helsinki


## Sébastien Rexhausen


Managing Director & Senior Partner
Cologne

## Matthew Abel

Managing Director & Senior Partner
Perth


Managing Director & Partner
Singapore

## Smith Sangiambut


## Anna Temple


Associate Director, Commodity Trading & Optimization
Houston

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
