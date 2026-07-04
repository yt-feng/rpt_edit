# The Agentic Era of Next-Best Action

Well-designed customer journeys unlock highly targeted audiences, and for over a decade they have been the organizing principle behind personalization strategies. But today the journey model operates in an increasingly dynamic environment: channels have multiplied; customer signals manifest in real time; and the shelf of possible content, offers, and experiences has grown substantially.

As a result, the journey model's impact has plateaued. Personalization must evolve by changing its unit of decision from marketer-orchestrated journeys to agent-orchestrated actions, with AI agents selecting, sequencing, and composing interactions from a modular shelf in real time. The marketer's role shifts, too, from designing journey flows to curating the shelf's content and setting the objectives that agents pursue.

The stakes of getting these shifts right are significant. Organizations that modernize their next-best action (NBA) architecture will compound value across both efficiency and growth: from dramatic reductions in campaign cycle time to step-change increases in addressable revenue. (See Exhibit 1.)

## EXHIBIT 1

AI-Native Marketing Drives More Efficient, More Effective Growth Across the Enterprise

Savings from NBA

Savings from AI
Source: BCG analysis leveraging industry benchmarks and BCG research commissioned by Google. Note: NBA = next-best action.

Reduction in campaign cycle time

More assets in market

Increase in addressable revenue

## How NBA Is Evolving

Each new evolution of NBA is defined by a different unit of decision and a different role for the marketer. Understanding where an organization sits on this continuum is the first step toward preparing for what comes next. (See Exhibit 2.)

# What Companies Build for Evolution 2 Today Becomes the Foundation for Evolution 3

Each era changes the unit of decision and the role of marketer


[[KC_IMAGE_001]]

Source: BCG analysis.
Note: NBA = next-best action.

First Evolution. Today, most organizations operate marketer-orchestrated journeys, in which marketers manually build audiences, design journey flows, and define the rules governing which customers receive which communications. The unit of decision is the journey itself. A well-honed journey remains very effective, but it scales poorly because every new segment, product launch, or channel requires a new journey—and the number of journeys quickly increases beyond the team's ability to manage them.

Second Evolution. More and more organizations are moving to model-optimized journeys, in which marketers define the components, objectives, and guardrails, but machine learning models optimize within the prebuilt journey. The models choose the best branch, offer, or message to optimize an objective function, but they operate within boundaries set by the marketer.

The unit of decision in this evolution shifts from the journey to the journey step, as NBA embraces algorithmic optimization without disrupting the underlying approach. The architecture still rests on the assumption that journeys are the appropriate organizing construct and that humans should define the options and constraints.

Third Evolution. NBA is headed toward agent-composed actions, in which the marketer's role shifts from designing journeys to curating a shelf of composable assets and setting the objectives for AI agents. The agents select, sequence, and compose atomic actions from that shelf to suit the real-time context.

The unit of decision in the third evolution is the atomic action. The marketer governs the option space (which assets are available, which constraints apply), while agents determine the activation (what, when, and in what combination or sequence). In practice, this enables a marketing organization to launch personalized programs in hours rather than weeks. Every interaction

# Four Capabilities of Agent-Native NBA

Evolving to agent-native NBA requires building four interconnected capabilities: composable shelf, agent architecture, tools/state management, and learning and optimization. (See Exhibit 3.) These four capabilities constitute a system designed from the ground up to support AI agents in autonomously reasoning, selecting actions, and composing them, rather than operating as a retrofitted traditional stack with agent capabilities bolted on top.

## EXHIBIT 3

Four Capabilities Separate Agent-Native NBA from Traditional Decisioning Stacks


[[KC_IMAGE_002]]


Composable shelf
Modular catalog of offers, creatives, and micro-journeys that agents select from and assemble on demand

Source: BCG analysis.
Note: NBA = next-best action.

## Agent architecture

Use of specialized agents to reason about customer context, collaborate across decisioning tasks, and orchestrate real-time actions

## Tools/state management

Exposure of every model, integration, and data source as a modular tool that agents invoke on demand, with persistent memory of customer state

## Learning and optimization

Learning and optimization
Experimentation engine that measures every shelf asset and agent decision through causal testing, compounding performance over time

## Inside the Composable Shelf

The composable shelf is the modular catalog of offers, creatives, and micro-journeys that agents select from and assemble on demand. It organizes everything that is available for an agent to deploy into three levels of granularity—atomic assets, compiled communications, and micro-journeys—each tagged with metadata that agents use to evaluate what to select and how to combine the selected items. (See Exhibit 4.)

The Composable Shelf Organizes Deployable Experiences into Three Levels

[[KC_IMAGE_003]]

Source: BCG analysis.

If content, offers, and experiences are not tagged and modularized at the right level of granularity, agents will have nothing meaningful to work with. The shelf is not a static content library. It is a living inventory that agents continually tap, test, and learn from.

Atomic assets—copy variants, image assets, offer constructs, and content templates—are the most granular building blocks. They are individually reusable and are tagged with metadata such as channel compatibility, regulatory flags, and expiration dates. Marketers, designers, and generative AI contribute to building this layer. Drawing from the resulting pool of information, agents compose whatever combination the context demands.

Compiled communications bundle an offer with a creative treatment and a channel to form a single unit that is ready for delivery at a specific touchpoint. These communications are conceived as preassembled modules: each one is a unique email message with a specific offer and creative, approved and ready to deploy. Agents select the right compiled communication for the moment and determine the optimal timing and sequence of delivery.

Micro-journeys are precomposed sequences of communications (usually consisting of two to five steps) designed to address the reality that not every brand interaction needs to be decomposed into atomic parts. Unlike the sprawling journeys in the first evolution of NBA, micro-journeys are short, self-contained, and purpose-built: a product launch sequence, an onboarding welcome series, a loyalty tier celebration. They provide curated experiences in situations where the brand has a deliberate story to tell. Agents decide when to trigger them to deliver the sequence as a complete block, but they do not rearrange the internal structure.

## What the Agent Architecture Looks Like

Agent architecture is the hub-and-spoke system of specialized agents that reason, collaborate, and orchestrate decisions. (See Exhibit 5.) The key components are agents, tools, Model Context Protocol (MCP), and learning and optimization:

\- Agents are the reasoning layer. A central orchestrator responds to a trigger action (a customer event, a scheduled cadence, a real-time signal, or a long hiatus in activity) and routes them to specialized agents. Each agent is responsible for a distinct part of the decision process—assembling context, checking eligibility, selecting the best action, composing the final communication, or managing experimentation. Agents do not execute in a fixed sequence. Instead, they identify the information they need, decide which tools to invoke, and adapt their approach based on what they find. This flexible process is what separates an agent architecture from a traditional decisioning pipeline, in which the sequence is always the same: ingest data, score, select, and deliver.

\- Tools are the action layer. Every model, data source, channel integration, and business rule in the stack is exposed as a discrete, callable tool that agents can invoke on demand. An eligibility check is a tool. A propensity model is a tool. A channel application programming interface (API) is a tool. By modularizing the stack in this way, the system gains composability. Agents can combine tools in whatever sequence the context requires, rather than following a prewired pipeline. Tools also maintain a persistent state, giving agents memory of prior interactions, customer preferences, and in-flight communications.

\- MCP is the connective layer. This protocol is what makes the architecture modular rather than monolithic. Agents use MCP to discover and invoke tools through a shared interface. New models, channels, and data sources plug in as new tools without requiring architectural reworking.

\- Learning and optimization provide the measurement engine. Through continuous experimentation, they score every shelf asset and every agent decision, thereby improving performance over time. Causal measurement and incrementality testing are essential, not optional.

Note: CDP = customer data platform; DAM = digital asset manager; DWH = data warehouse; ESP = email service provider; MCP = Model Context Protocol; ML = machine learning; SMS = short message service.

The power of this architecture will make agent-native NBA architectures far superior to today's systems. Consider a credit card customer who calls to dispute a fraudulent charge, gets it resolved, and then opens the issuer's app 20 minutes later. In the first evolution of NBA, the app displays a scheduled balance transfer promotion that had been queued before the call, misinterpreting a moment when trust was just tested. In the second evolution of NBA, a propensity model suppresses the promotion in response to a recency rule, but it can't recognize that the resolved fraud case is a moment to reinforce trust.

In third evolution of NBA, the orchestrator routes the app-open event to a context agent, which assembles the full picture: fraud dispute resolved favorably, long-tenure cardholder, high monthly spending, no prior fraud incidents. An action selection agent evaluates available options and selects a security reassurance message paired with a complimentary credit monitoring upgrade. A composition agent assembles the in-app card from atomic assets on the shelf in seconds, with no human intervention. The experimentation layer records the outcome to improve the next similar moment.

# Building for Tomorrow's Agent Infrastructure

The agent-native architecture does not require or assume a greenfield build. Every component that organizations build today for the second evolution of NBA will map directly to a capability that agents can use in the third evolution of NBA. (See Exhibits 6 and 7.) The investment path is cumulative, not sequential. There is no throwaway work, and no replatforming is required.

## EXHIBIT 6

Key Parts of the Agent Architecture Are Built in Evolution 2


[[KC_IMAGE_004]]

Source: BCG analysis.
Note: AWS = Amazon Web Services; CLV = customer lifetime value; DAM = digital asset manager; ESP = Email Service Provider; MCP = Model Context Protocol; SMS = short message service.

The key design principle is modularity. Every component built today should be designed as a modular tool that agents can invoke autonomously in the future. This means creating API-first interfaces, clean metadata, and well-defined inputs and outputs. The difference between an organization that can adopt agent-native NBA in 12 months and one that requires multiyear replatforming is whether it designs today's build with modularity in mind.

# The Path Forward: How to Get Started

Building these capabilities in the correct sequence ensures that every investment dollar delivers value today while building toward the third evolution of NBA. The steps are as follows:

\- Start with the composable shelf. Build a modular, metadata-rich catalog of creative, offer, product, and action assets. This work delivers immediate value by reducing content redundancy and improving reuse. Over time, it becomes the library that agents will leverage in real time.

\- Modularize the tools layer. Replatform every model and integration as a modular, API-first component. This action delivers near-term efficiency gains. Each model and integration exposed as a tool becomes a capability that agents can invoke autonomously.

\- Stand up experimentation to learn and optimize. Build causal measurement and incrementality testing to start compounding performance gains. This practice creates continuous experimentation and feedback loops that agents will eventually use for self-optimization.

\- Pilot agent use cases to build the architecture. Start with a single, bounded use case to build organizational confidence and track the rapidly evolving vendor landscape. The agent architecture is the orchestration layer that connects the other capabilities, but it benefits from the maturity of the components it orchestrates. Sequencing matters: the capabilities must be in place for an agentic approach to perform the orchestration role.

# From Campaign Operator to System Architect

The technology to build toward agent-native NBA is already widely available. The challenge lies in reinventing the marketing operating model—defining which decisions agents should make autonomously, which require human oversight, and how governance should scale as the system matures. Organizations that begin piloting single-agent use cases early will build the muscle and technical intuition they need to expand in scope over time. As the scope expands, the marketer will become the architect of the system rather than a campaign operator.

Organizations that delay adopting agentic approaches face a self-reinforcing disadvantage. Their campaign cycles will take weeks while competitors' take hours, they will assemble content manually while competitors compose dynamically from thousands of tested assets, and their experimentation will run in quarterly cycles while competitors will get smarter with every customer touchpoint. For many companies, the next 12 to 18 months will determine which side of that divide it falls on.

This is Part 2 of a five-part series on the future of next-best action. Part 1 explores why most NBA programs underdeliver and identifies four structural gaps. Part 3 unpacks the decisioning science, from propensity models to contextual bandits to foundation model reasoning. Part 4 examines how marketing organizations can

restructure around the new operating model. Part 5 addresses measurement: from campaign-level attribution to agentic measurement.

## Authors


## Silvio Palumbo

Managing Director & Senior Partner


## Karl Johnson


Managing Director & Partner
Washington, DC

## ABOUT BOSTON CONSULTING GROUP

Boston Consulting Group bridges the gap between ambition and outcomes for the world's leading companies and organizations. We are built for this era of unprecedented change — bringing strategic clarity rooted in over 60 years of deep domain knowledge, combined with applied AI shaped by our practitioners. BCG works shoulder-to-shoulder with CEOs across industries and geographies to deliver transformative impact at scale: stronger returns, transferred capabilities, and change that sticks. For more information, visit bcg.com.
