# Moonshot AI releases Kimi K3

Takes first step in post-transformer world with open-source, large-scale coding model

Manabu Akizuki - NSC


Kimi K3: Groundbreaking innovation with hybrid architecture featuring Transformer and recurrent model

Moonshot AI's Kimi K3, released on 16 July, has become a hot topic as it has coding performance on par with that of cutting-edge AI lab models in the US. On top of this, its innovative hybrid model combines Transformer (multi-head latent attention; MLA) with a recurrent model (Kimi Delta Attention; KDA), and we were surprised by this. In terms of implications for the technology industry, we think the emergence of Kimi K3 provides fresh evidence of China's strong ability to develop AI models, as the cutting-edge agentic coding model has shaken up the dominant position of the US's closed models.

Achieves long-term reasoning by substantially reducing KV cache with a recurrent model using KDA

Kimi K3 is a mixture of experts (MoE) model with 2.8trn parameters. It is made up of 896 experts, and when carrying out inference, the router selects and activates 16 experts per token. The maximum context length is 1mn tokens, and the model is specialized for long-term agentic coding.

As noted above, the core of the model is a hybrid architecture that combines Transformer with a recurrent model. Based on the company's past announcements, we surmise that the attention architecture consists of four layers as one unit: three KDA layers and one MLA layer. While the Transformer model holds the keys and values of all tokens in the context window, and analyzes the necessary data based on the degree of similarity to the query, the recurrent model compresses and updates past data to a fixed-length state and carries out inference by referencing the state, thereby substantially reducing reliance on KV cache. It is well known that longer KV caches result in: (1) higher compute and memory access volumes during decoding, as well as increased inter-GPU communication loads for MoE models, resulting in higher compute costs; and (2) lower performance for long contexts and long-term reasoning as a result of attention being widely dispersed, making it difficult to focus on important information. To counter this, the use of KDA in Kimi K3 is aimed at achieving both computational efficiency and long-term reasoning performance by updating token-level data in a fixed-length state. We think Kimi K3 features an MLA layer in order to provide the ability to reference, from the KV cache, detailed token level data that cannot be stored in a fixed-length state, and precisely search and reference data even when it is stored far away.

As the recurrent model is not reliant on context length, it is a good match for autonomous learning models that carry out learning and inference while continuing to interact with the environment, and we had thought they could be adopted in cutting-edge models within the next two to three years. While Kimi K3 is a hybrid model, it came as a surprise to us that the company has able to implement a recurrent model in a large-scale cutting-edge model.

Industry impact: Positive over longer term, but we note risk of weakening fund flows in near term

We expect Kimi K3 to provide a new approach to AI model development and boost longer-term growth in the AI industry. That said, in the near term, fiercer competition could delay the monetization of closed models developed by AI labs in the US, and we think it is important to be aware of the risk that the flow of funds from AI labs to cloud operators to producers of electronic devices such as memory and storage could weaken.

## Appendix A-1

This report has been produced by NOM Securities Co., Ltd. (NSC), Japan.

See Disclaimers for NOM Group entity details.


I, Manabu Akizuki, hereby certify (1) that the views expressed in this Research report accurately reflect my personal views about any or all of the subject securities or issuers referred to in this Research report, (2) no part of my compensation was, is or will be directly or indirectly related to the specific recommendations or views expressed in this Research report and (3) no part of my compensation is tied to any specific investment banking transactions performed by NOM Securities International, Inc., NOM International plc or any other NOM Group company.

## Important Disclosures

The lists of issuers that are affiliates or subsidiaries of NOM Holdings Inc., the parent company of NOM Securities Co., Ltd., issuers that have officers who concurrently serve as officers of NOM Securities Co., Ltd., issuers in which the NOM Group holds 1% or more of any class of common equity securities and issuers for which NOM Securities Co., Ltd. has lead managed a public offering of equity or equity linked securities in the past 12 months are available at https://www.NOMholdings.com/report/. Please contact the Research Production Operation Dept. of NOM Securities Co., Ltd. for additional information.

## Online availability of research and conflict-of-interest disclosures

NOM Group research is available on www.NOMnow.com/research, Bloomberg, Capital IQ, Factset, LSEG.


NOM Global Financial Products Inc. (NGFP) NOM Derivative Products Inc. (NDP) and NOM International plc. (NIplc) are registered with the Commodities Futures Trading Commission and the National Futures Association (NFA) as swap dealers. NGFP, NDPI, and NIplc are generally engaged in the trading of swaps and other derivative products, any of which may be the subject of this report.

## Distribution of ratings (NOM Group)


58% have been assigned a Buy rating which, for purposes of mandatory disclosures, are classified as a Buy rating; 33% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services\*\* by the NOM Group.

39% have been assigned a Neutral rating which, for purposes of mandatory disclosures, is classified as a Hold rating; 57% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group

3% have been assigned a Reduce rating which, for purposes of mandatory disclosures, are classified as a Sell rating; 15% of companies with this rating are investment banking clients of the NOM Group\*. 0% of companies (which are admitted to trading on a regulated market in the EEA) with this rating were supplied material services by the NOM Group.

As at 30 June 2026.

\*The NOM Group as defined in the Disclaimer section at the end of this report.

\*\* As defined by the EU Market Abuse Regulation


The rating system is a relative system, indicating expected performance against a specific benchmark identified for each individual stock, subject to limited management discretion. An analyst's target price is an assessment of the current intrinsic fair value of the stock based on an appropriate valuation methodology determined by the analyst. Valuation methodologies include, but are not limited to, discounted cash flow analysis, expected return on equity and multiple analysis. Analysts may also indicate expected absolute upside/downside relative to the stated target price, defined as (target price - current price)/current price.

## STOCKS

A rating of 'Buy', indicates that the analyst expects the stock to outperform the Benchmark over the next 12 months. A rating of 'Neutral', indicates that the analyst expects the stock to perform in line with the Benchmark over the next 12 months. A rating of 'Reduce', indicates that the analyst expects the stock to underperform the Benchmark over the next 12 months. A rating of 'Suspended', indicates that the rating, target price and estimates have been suspended temporarily to comply with applicable regulations and/or firm policies. Securities and/or companies that are labelled as 'Not rated' or shown as 'No rating' are not in regular research coverage. Investors should not expect continuing or additional information from NOM relating to such securities and/or companies. Benchmarks are as follows: United States/Europe/Asia ex-Japan: please see valuation methodologies for explanations of relevant benchmarks for stocks, which can be accessed at: http://go.NOMnow.com/research/m/Disclosures; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia, unless otherwise stated in the valuation methodology; Japan: Russell/NOM Large Cap.

## SECTORS

A 'Bullish' stance, indicates that the analyst expects the sector to outperform the Benchmark during the next 12 months. A 'Neutral' stance, indicates that the analyst expects the sector to perform in line with the Benchmark during the next 12 months. A 'Bearish' stance, indicates that the analyst expects the sector to underperform the Benchmark during the next 12 months. Sectors that are labelled as 'Not rated' or shown as 'N/A' are not assigned ratings. Benchmarks are as follows: United States: S&P 500; Europe: Dow Jones STOXX 600; Global Emerging Markets (ex-Asia): MSCI Emerging Markets ex-Asia. Japan/Asia ex-Japan: Sector ratings are not assigned.

## Target Price

A Target Price, if discussed, indicates the analyst's forecast for the share price with a 12-month time horizon, reflecting in part the analyst's estimates for the company's earnings. The achievement of any target price may be impeded by general market and macroeconomic trends, and by other risks related to the company or the market, and may not occur if the company's earnings differ from estimates.

## Disclaimers
