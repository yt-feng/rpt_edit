# Cyber Thoughts on Hugging Face Security Incident

Detection and mitigation of Hugging Face's security breach this week took place largely by utilizing other LLMs / internal tools. The sophistication of the attack, and seeming lack of traditional cyber tools being used, has caused investors to question impact to traditional cyber vendors.

## Key Takeaways

Hugging Face reported a highly sophisticated attack last week, carried out by an autonomous agent of an advanced LLM.

Their anomaly-detection pipeline utilized LLM-based triage over security telemetry vs noting usage of a SIEM/XDR, which would normally be used by enterprises.

SIEM/XDRs designed to detect the very type of attacks we saw, however, need to be well tuned and modernized to detect advanced behaviors in a timely fashion.

Leaves us positive on vendors with most modern solutions, namely CRWD / PANW / ESTC.

Does the SIEM adapt to next-generation attacks? As we highlighted in our deep dive into the SIEM market last month, the security information and event management (SIEM) and extended detection and response (XDR) market today is the traditional line of defense in helping security operations centers (SOCs) detect and remediate attacks. In a breach such as the one that Hugging Face (private) reported last week, a SIEM, receiving logs from identity, cloud, endpoints, network devices, and application infrastructure, could have generated alerts on: use of stolen credentials, privilege escalation, access to sensitive repositories, lateral movement, data exfiltration, large number of API calls, frequency of actions from ephemeral compute. It would need to be a more mature and well-tuned SIEM that would have needed a solid behavioral baseline, particularly to detect the actions from the ephemeral compute so quickly. The speed of detection, particularly to as sophisticated an attack, necessitates more advanced alerting and certainly the collection of a fuller set of logs (SIEM+XDR+SOAR can improve mean time to remediation by 96%). While we see some customers deploying advanced analytics such as we saw from Hugging Face, we would expect most to still rely on the logs / alerts / baselining of their SIEM, though they would increasingly turn to the most next-gen vendors. Given the advanced data signal collection from security vendors, we still see them as best positioned (CRWD/PANW/ESTC highlighted in our note as having screened best in customer / VAR conversations).

What happened? The breach, as reported by Hugging Face on July 16th, originated in their data processing pipeline, which ingests raw data from multiple data sources,

MS & CO. LLC

Meta A Marshall


## SOFTWARE


## What type of other cyber tools could have helped detect the breach? A

traditional SIEM that is used primarily for log detection could see static rules bypassed, have novel attacks not match previous signatures and without behavioral analytics, wouldn't necessarily pick up on the low-level events the ephermeral compute carried out. As we highlighted in our piece, the addition of XDR and SOAR would help with bringing detection more into real time, with UEBA (User & Entity Behavior Analytics), Cloud Detection & Response (CDR) and Identity Threat Detection and Response (ITDR) helping as well.

Elastic NV is covered by Sanjit Singh

Exhibit 1: Traditional SIEM Alone Not Enough For Newer Sophisticated Attacks, but Combination of Tools Leads To Significantly Higher MTTR

[[KC_IMAGE_001]]

Source: Medium.

Exhibit 2: Modern SOC Architecture Combines Detection Engine with Response

[[KC_IMAGE_002]]

Source: Medium.

Exhibit 3: Customers Need to Evolve Their SIEM Architectures Towards XDR +SOAR

[[KC_IMAGE_003]]

Source: MS.

## Valuation Methodology and Risks

## CrowdStrike Holdings Inc (CRWD.O)

Our \$227 PT is based on 60X CY30e FCF of \$5.21B, discounted back at 12%. This multiple implies \~33X EV/CY27 Sales, a premium to Large Cap SaaS/Security peers.

## Risks to Upside

■ Stronger than expected endpoint security demand remains elevated due to rising cyber threats

■ TAM expansion opportunities (XDR, Identity, Cloud Workload Protection) materialize faster than expected

## Risks to Downside

■ Competition makes new customer acquisition tougher

■ Lower cost alternatives commoditize CRWD's premium pricing

■ Softer hiring environment pressures upsell activity

## Elastic NV (ESTC.N)

We arrive at our \$66 price target by applying a \~13x multiple (0.51x growth-adjusted) to our CY28 FCF/shr estimate of \$5.09. This implies 3.0x EV/CY27 Sales or 0.20x growth-adjusted, which reflects a discount to the DevOps peer median of 4.8x/0.44x.

## Risks to Upside

■ Elastic drives faster than expected use case expansion in Security and Observability

■ The \~5% GenAI tailwind materializes, accelerating sales-led subscription growth

■ Adoption of Elastic Cloud grows at a faster rate

## Risks to Downside

■ Competition intensifies across observability, SIEM and hyperscalers

■ Internal disruption from sales changes or management departures

■ New search paradigms arrive through GenAI

## Palo Alto Networks Inc (PANW.O)

Based on 52x Base Case 2028e FCF per share of \$7.05; this multiple is a premium to similarly growing large cap software peers.

## Risks to Upside

■ Stronger firewall refresh cycle and higher subscription attach rates

■ Faster uptake of new Cloud-based Next-Gen Security solutions such as Cortex (AI-Powered Security Analytics) and Prisma SASE

## Risks to Downside

■ Slowing firewall refreshes could drive a greater than expected impact to PANW's top line growth

■ An increasingly competitive environment could necessitate additional S&M spending,

limiting margin leverage.
