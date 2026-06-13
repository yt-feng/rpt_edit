# Weekend Consumer Blast: How "agentic" is AI shopping today? We tested 5 models...

Agentic shopping burst onto the US Retail scene last October after Walmart announced its partnership with ChatGPT. $^{1}$ More than six months later, how agentic is shopping today?

We tested five different tools. Three are foundational AI models - ChatGPT, Gemini, and Claude - with broad capabilities. The other two, Amazon's Alexa and Walmart's Sparky, are retail-native AI tools built directly on top of retail ecosystems. The goal was to see how each approaches the shopping funnel: from identifying the right product, to validating pricing, and actually enabling a purchase. More importantly, we assess where each tool breaks down and how far we are from a true end-to-end agentic e-commerce experience. While human interaction is still needed at every stage, payment is where the whole experience unravels. Even in the simplest case - buying a single, generic item - the hand off from “AI found it” to “I bought it” still requires the user to engage. Until payment is embedded directly into the experience, AI remains one step removed from making shopping decisions on behalf of users.

Underpinning that is a tension between general and retailer-integrated systems. The foundational AI models feel powerful because they can roam freely, comparing products, surfacing deals, and stitching together options across a fragmented retail landscape. However, they are doing so without direct access to the structured catalog data, real-time pricing, inventory, or delivery options. Meanwhile, those retail ecosystems have the opposite problem: they are highly precise and almost-transaction-ready, but confined to their own assortment (1P and/or 3P). Bridging this gap, from either end, will be key as the technology evolves.

## BUYING ONE ITEM - REQUIRES INTEGRATION!

We evaluated how effective each AI assistant is through each step of the basic e-commerce process for one item, from product discovery to final transaction execution: I want to make scrambled eggs, but I've run out of milk. Could you please find me a 64 fl oz carton of organic whole milk? How soon can it be delivered to me in ZIP 22201 (Arlington, VA)? Exhibit 1 shows each AI tool's performance at each stage.

EXHIBIT 1: Amazon Alexa and Walmart Sparky currently maintain an advantage in real-time pricing accuracy, total cost estimation, and transaction execution.


Definitions - Identifies Category: Ability to correctly determine the relevant product category; Identifies SKU: Ability to accurately identify the specific item, including its brand, size, and variant; Identifies Pricing: Ability to correctly determine the exact price of the selected item; Estimate Full Cost: Ability to accurately calculate the total order cost, including fulfillment, taxes, and any additional fees; Add to Cart: Ability to successfully add selected items to the shopping cart; Payment: Ability to complete the checkout process and successfully execute the order.

Source: Bernstein analysis

There is currently no agentic shopping tool capable of buying a product in an unsupervised fashion. Human engagement is needed at many steps.

ChatGPT, Claude, and Gemini are primarily research and recommendation tools. Because they lack direct access to retailers' assortment (unless shared by retailers directly), they seem to rely on workarounds such as web scraping or third-party articles (Exhibit 2). Therefore, they sometimes struggle with SKU identification and pricing accuracy. In addition, they are incapable of handling fulfillment and payment (in so far as they lack a connection). As a result, these are product discovery tools. However, they are partnering with retailers to bridge the gap. ChatGPT, for example, has introduced its Agentic Commerce Protocol (ACP), and Claude integrates with Uber Eats to enable grocery and food delivery (Exhibit 6). Still, users need to follow links to retailers' websites to complete transactions.

In contrast, Amazon and Walmart operate fundamentally differently. Their AI assistants have access to the real time inventory data. This allows them to manage the entire purchase funnel within their ecosystems, from product discovery through payment. Amazon's implementation illustrates both the potential and the limitations of this approach. Alexa can add non-perishable items to a cart (Exhibit 7) but currently excludes Amazon Fresh and Whole Foods products (Exhibit 8). There are still limitations at the final step. The payment process is not fully integrated within either Sparky or Alexa, so users cannot complete the transaction directly within the assistant.

## EXHIBIT 2: ChatGPT can identify the SKU and estimate an approximate price range, but appears to rely on web scraping at times.

Whole Foods link, in exhibit, directs to an article on Whole Foods delivery policy.

I want to make scrambled eggs, but I've run out of milk. Could you please find me a 64 fl oz carton of organic whole milk? How soon can it be delivered to me in zip 22201 (Arlington, VA)?


[[KC_IMAGE_001]]


Here are the best quick options I found for a 64 fl oz organic whole milk delivery to Arlington, VA 22201:

## Fastest + Cheapest Likely Option

• Great Value Organic Whole Vitamin D Milk, Half Gallon, 64 fl oz
Price: about \$3.98 at Walmart ↗
Delivery: typically same-day within 1–3 hours through Walmart delivery in Arlington if slots are
available.

## Best Premium Organic Brand

• Organic Valley Organic Whole Milk Half Gallon Carton 64 oz

Price: about \$4.96-\$6.26 at Walmart ↗

Delivery: generally same-day in your ZIP if ordered soon. Whole Foods ...

## Whole Foods Option

• Organic Valley Organic Whole Milk 64 Oz

Price: usually around \$6–7 at Whole Foods Market ↗

Delivery: often under 2 hours via Amazon/Whole Foods delivery depending on availability.


Source: ChatGPT (OpenAI), Bernstein analysis

## EXHIBIT 3: With the initial prompt, Gemini suggests relevant product and delivery options but does not identify items at the SKU level.

It also appears to rely on online scraping to generate its responses.

For your immediate cooking needs in zip code 22201 (Arlington, VA), you have a few highly efficient options to secure a 64 fl oz carton of organic whole milk (commonly available from trusted organic brands like Horizon Organic, Organic Valley, or Stonyfield):

## On-Demand & Instant Delivery (Fastest)

If you are mid-recipe and need it immediately, delivery apps are your best option:

Instacart, DoorDash, or Uber Eats: You can order a 64 oz carton directly from local stores right in your neighborhood (such as the Safeway on Wilson Blvd or the Whole Foods Market in Clarendon).
Delivery Speed: These services typically offer on-demand rush delivery that can arrive at your door in 30 to 60 minutes.

## Same-Day Store Services

If you have a bit more flexibility later in the day:

Safeway Flash / DriveUp & Go: The Safeway location at 1525 Wilson Blvd handles rapid fulfillment online, often preparing "Flash" delivery orders or window pickups in 30 minutes or less. Safeway
Amazon Fresh / Whole Foods Market: Standard same-day delivery slots for the Arlington area are usually available within a 2-hour window depending on current courier availability. Dragonfly

To get it fastest, checking DoorDash or Instacart mapped to your exact street address will show you the precise real-time courier ETA, which should easily be under an hour.

Source: Google Gemini, Bernstein analysis

## EXHIBIT 4: This is not due to a lack of capability. When prompted further, such as asking for the price of the milk, Gemini is able to retrieve SKU-level product information.

what's the price of the milk

In the Arlington, VA area (zip 22201), a 64 fl oz carton of organic whole milk generally ranges between \$4.69 and \$7.49 depending on the store brand and specific label:

Store Brands (Most Affordable):
Whole Foods (365 Brand): \$4.69 per 64 oz carton. Whole Foods Market
- Premium National Brands:
Organic Valley: \$6.29 per 64 oz carton. Whole Foods Market
- Horizon Organic: \$6.99 (Standard Whole Milk) to \$7.49 (DHA Omega-3 formula) per 64 oz carton.

Note: If you order through a third-party application like Instacart or DoorDash, the base price may be slightly marked up by \$0.50 to \$1.00, and standard delivery fees/service tips will apply.

Source: Google Gemini, Bernstein analysis

## EXHIBIT 5: Similar to Gemini, Claude initially presents delivery options along with item recommendations and approximate delivery times.

I want to make scrambled eggs, but I've run out of milk. Could you please find me a 64 fl oz carton of organic whole milk? How soon can it be delivered to me in zip 22201 (Arlington, VA)?

Shopping and grocery delivery isn't something I can search directly, but here are some great options for getting organic whole milk delivered quickly to Arlington, VA (22201):

## Same-day or fast delivery options:

- Instacart (instacart.com) — connects to local stores like Whole Foods, Safeway, Giant, and more. Often delivers in 1-2 hours.
- Amazon Fresh — if you're a Prime member, same-day or next-day delivery is common in Arlington.
• Whole Foods (via Amazon) — Prime members often get free 2-hour delivery.
- DoorDash / Uber Eats — both partner with grocery stores and can deliver in under an hour from nearby locations.

For a 64 fl oz carton of organic whole milk, brands like Organic Valley, Horizon Organic, or 365 by Whole Foods are widely available through all of the above.

Arlington is very well-served by these services, so same-day delivery within 1-2 hours is very likely. In the meantime, for your scrambled eggs — a small splash of water or a bit of cream cheese actually works wonderfully as a milk substitute!

Source: Claude (Anthropic), Bernstein analysis

## EXHIBIT 6: Through its partnership with Uber Eats, Claude enables users to complete purchases via Uber Eats directly within the interface.

I don't have a grocery delivery connector available to place orders directly. Let me see if there's one I can suggest for you!

Searching connectors >

Unfortunately there's no grocery delivery connector (like Instacart or Amazon Fresh) available to connect right now. The closest option I found is Uber Eats, which does partner with some grocery stores:


[[KC_IMAGE_002]]


Your connectors

Beta


[[KC_IMAGE_003]]


[[KC_IMAGE_004]]


Looking for something else? Browse all connectors

None of these

Uber Eats is one option — would you like to connect it to search for grocery stores near you? Otherwise, your quickest bet would be heading directly to instacart.com or Amazon Fresh to search for that 64 fl oz organic whole milk — both should have it to you in Arlington within an hour or two.

Source: Claude (Anthropic), Bernstein analysis

## EXHIBIT 7: Amazon provides product recommendations at the SKU level, presenting users with a range of options to choose from.

I want to make scrambled eggs, but I've run out of milk. Could you please find me a 64 fl oz carton of organic whole milk? How soon can it be delivered to me in zip 22201 (Arlington, VA)?

Great news! I found some 64 fl oz organic whole milk options that can be delivered today between 1 PM – 3 PM in Arlington, VA (22201):

## 64 fl oz Organic Whole Milk - Delivered Today See more


[[KC_IMAGE_005]]


365 by Whole Foods Market, Organic Whole Milk, 64 oz

4.7 ★★★★★☆ (12,677)

10K+ bought in past month

\$479 (\$0.07/fluid ounce)

FREE delivery Today 1 PM - 3 PM on orders over \$25.00

365 by Whole Foods Market – USDA Organic, pasture-raised, GMO-free, fortified with Vitamin D3. \$4.79

## More details


[[KC_IMAGE_006]]


Organic Valley, Organic Whole Milk, 64 Oz (Half Gallon)

Source: Amazon Alexa, Bernstein analysis

## EXHIBIT 8: Alexa is unable to do so for Amazon Fresh and Whole Foods products; it directs the user to an external link.

All four options qualify for free delivery today (1 PM – 3 PM) on qualifying orders. The 365 by Whole Foods Market option is the most budget-friendly at \$4.79. Would you like me to add one to your cart?

Add the 365 Whole Foods milk to my cart

I wasn't able to add this item directly to your cart — Fresh/Whole Foods products need to be added from the product page. You can do so here:

365 by Whole Foods Market Organic Whole Milk, 64 fl oz — \$4.79

Just tap the link to go to the product page and add it to your cart from there!

Source: Amazon Alexa, Bernstein analysis

## EXHIBIT 9: Sparky is capable of handling the full flow from product discovery through to building a basket (or cart).

Great news — two of these options show delivery as soon as 18 minutes to 22201 (Arlington, VA). Here are your 64 fl oz organic whole milk options:

## Sparky's Picks

## Best seller, most affordable at \$3.97


[[KC_IMAGE_007]]


[[KC_IMAGE_008]]


Whole Vitamin D Milk, Hal...

★★★★★ (3329)

Best seller

\+ Add

## ♦ Added DHA Omega-3, also a best seller


[[KC_IMAGE_009]]


[[KC_IMAGE_010]]


Horizon Organic DHA Omega-3 Whole Milk, DH...

★★★★★ (2524)

Best seller

\+ Add

## Organic Valley, currently on rollback

Source: Walmart Sparky, Bernstein analysis

## BUILDING A GROCERY BASKET - DESIGN CHOICES GUIDE LLM'S

Beyond finding and buying a single item, we tested AI agents' ability to build a grocery basket. It requires translating a multi-day meal plan into a complete grocery basket, estimating appropriate quantities for a family of four, and accounting for constraints such as a nut allergy. In addition, it assesses the ability to demonstrate contextual awareness, organize items and avoid duplication. The prompt is:

Household description: family of four (two adults and two children, ages 6 and 10) living in New York City, with a total household income of \$100,000. This family has nut allergies. [Inserted Exhibit 10 as list]. Please build me a grocery basket for this week. Thank you!

## EXHIBIT 10: We fed this meal plan as text into the prompt.

We kept meal choices rudimentary, this isn't a culinary exercise.


Source: Bernstein analysis

## EXHIBIT 11: Foundational LLMs are better at understanding context while retail-integrated models provide SKU-level detail.


Definitions - List: A set of relevant product suggestions based on the user's request; Basket: A structured collection of specific SKUs selected for purchase; Pricing: The accuracy and reasonableness of the price information provided for each item; Add to Cart: The capability of a shopping tool to add selected items directly into a virtual cart for purchase.

Source: Bernstein analysis

Design choices guide performance in this task. The foundational LLM's understand the complexity in full, and are able to provide detailed answers. However, there is no clear link down the funnel, so the output is (for now) more akin to a shopping list. Alexa operates best within Amazon's shelf-stable assortment, while Fresh items are not yet available. This could be by choice, or for a lack of wiring in the back end. Sparky takes a completely different approach and provides product recommendations in the context of recipes. Is this computationally more efficient? It generates recipes that loosely align with the requested meals. Each recipe can be opened in detail, and from there, users can add all required ingredients to their cart with accurate pricing, creating a smooth path from idea to purchase. Once again, human engagement is required.

ChatGPT, Gemini, and Claude generate comprehensive shopping lists that operate at the ingredient level, not at SKU-level. These platforms understand the full scope of the request: processing the five-day meal plan, accounting for family size, and flagging the nut allergy constraint to suggest appropriate substitutions. They can infer that "tacos" require tortillas, ground meat, cheese, lettuce, and salsa, then aggregate ingredients across multiple meals to avoid duplication. Eggs purchased for Tuesday's breakfast could also cover Thursday's fried rice. However, this output resembles a traditional handwritten shopping list, rather than a stoppable basket. Users must still translate these ingredient-level recommendations into specific brand and size selections when actually purchasing, whether through manual shopping or searching within a grocery app. This again reflects the lack of integration into a retail ecosystem.

Amazon's Alexa provides SKU-level specificity with direct add-to-cart functionality but sacrificing meal planning comprehensiveness. When the assistant suggests only pizza dough for Friday's "pizza and fries" dinner, Amazon's AI appears optimized to identify concrete product requests and map them to its catalog, but struggles with the inferential leap required to understand that "pizza" implies not just dough but also sauce, cheese, and toppings, while "fries" requires frozen fries or potatoes and oil. Alexa's advantage is its ability to check out across part of Amazon's shelf-stable assortment. For fresh items, it is also easily directed to the page and the item, although checkout is not integrated in the AI tool

yet.

Sparky appears to operate as a content recommendation engine pulling from a recipe database. For instance, it treats allergy information as context rather than a hard filter. Similarly, the absence of basket consolidation (suggesting items meal-by-meal rather than creating a week-long shopping list) indicates the system is optimized for individual transaction moments rather than comprehensive planning.

## EXHIBIT 12: While Amazon Alexa takes allergies into account, it falls short of assembling complete meals.

Got it! Here's a full grocery basket for your 5-day meal plan, tailored for a family of 4 with a nut allergy. I've flagged the Thursday PB&J — since peanut butter is a nut product, I've swapped it with SunButter (sunflower seed butter), which is 100% nut-free and a perfect kid-friendly alternative! All items with same-day delivery are available in NYC today.

! Nut Allergy Note: Please double-check all packaged product labels, especially the sliced ham (Wellshire Farms notes it may be processed on shared equipment with tree nuts) and other deli items, to confirm they're safe for your family.

## Breakfast

## See more


[[KC_IMAGE_011]]


Chobani® Whole Milk Plain Greek Yogurt 32oz

4.7 ★★★★★☆ (3,406)

20K+ bought in past month

\$699 (\$0.22/ounce)

FREE delivery Today 4 PM - 6 PM on orders over \$25.00

Greek yogurt for Monday — great family-size container, high protein (★17)

More details


[[KC_IMAGE_012]]


Source: Amazon Alexa, Bernstein analysis

## EXHIBIT 13: Of the 15 meals listed, Sparky was able to match 14 to existing recipes in its database.

Recipes seem to come from the American Diabetes Association (ADA).


[[KC_IMAGE_013]]


Here's a full 5-day grocery basket built around your meal plan — covering all 3 meals per day, Monday through Friday. I matched 14 recipes from Walmart's library spanning breakfast, lunch, and dinner. Tap any card to see the full ingredient list and add everything to your cart.


[[KC_IMAGE_014]]


Frozen yogurt bark with strawberries and dark c..

Prep time: 3 hrs 15 mins
Cook time: n/a
Est. per serving

\$0.39


[[KC_IMAGE_015]]


Hellmann's
Leftover turkey sandwich

Prep time: 10 mins
Cook time: n/a
Est. per serving

\$0.58

Tap any recipe card to open the full ingredient list and add it to your cart. Many ingredients overlap across meals (eggs, chicken, rice, onions) so you'll likely need fewer items than it looks!

Source: Walmart Sparky, Bernstein analysis

EXHIBIT 14: Users can open recipes within the Sparky interface, adjust the serving size, and add the relevant SKUs to cart.

[[KC_IMAGE_016]]


Ingredients you will need
Deselect all


[[KC_IMAGE_017]]


[[KC_IMAGE_018]]


\$328

10.3 ¢/oz

Great Value Plain Nonfat Greek Yogurt, 32 oz Tub

2 cup low-fat plain Greek yogurt

Replace

Qty needed:


[[KC_IMAGE_019]]


[[KC_IMAGE_020]]


[[KC_IMAGE_021]]


\$484

40.3 ¢/oz

Est. total \$16.78

5 items selected

Add to cart

Source: Walmart Sparky, Bernstein analysis

EXHIBIT 15: Gemini manages the allergy, but its list lacks quantitative budgeting and retailer optimization.


Source: Google Gemini, Bernstein analysis

EXHIBIT 16: Unlike Gemini, ChatGPT provides a more extensive product list from different retailers, while recognizing allergies / substitutions.

[[KC_IMAGE_022]]


Source: ChatGPT (OpenAI), Bernstein analysis

EXHIBIT 17: Estimated weekly cost provides a useful benchmark, helping shoppers plan.

[[KC_IMAGE_023]]


Source: ChatGPT (OpenAI), Bernstein analysis

## EXHIBIT 18: Claude's HTML interface creates a visually polished and engaging experience, but lacks shoppability.

Pricing is somewhat consistent with that of other models.


[[KC_IMAGE_024]]


Source: Claude (Anthropic), Bernstein analysis

## EXHIBIT 19: It also includes budgeting tips, recommending options like Trader Joe's and local supermarkets.

## A few notes on this basket:

Allergy swap: PB&J became SunButter & J — sunflower seed butter is widely available at NYC grocery stores (Trader Joe's, Whole Foods, most Key Foods) and kids generally love it. Always double-check the label, as some brands are made in facilities that also process tree nuts.

Stretching ingredients across meals: The ground beef covers both tacos (Monday) and meatloaf (Wednesday). The chicken works for Tuesday's lunch and can be batch-cooked. Rice is used both Tuesday and Thursday. The 18-pack of eggs covers scrambled eggs, meatloaf binding, and fried rice.

Where to shop in NYC to stay on budget: A mix of Trader Joe's (great for pantry staples), a local Key Food or Associated Supermarket, and possibly Costco for bulk items like eggs and rice will keep costs near that \~\$178 estimate. NYC grocery prices run 20–30% higher than the national average, so this estimate already reflects that.

Pantry items you may already have: Salt, pepper, cooking spray, basic spices, and sugar aren't included — if you have those, your actual spend will be a touch lower.

Want me to order this through Uber Eats grocery delivery, or would you like a printable version?

Source: Claude (Anthropic), Bernstein analysis

## EXACT PRICE DISCOVERY FOR TWO DISCRETIONARY PRODUCTS - THE MARKETPLACE PLAY

How about leveraging AI agents to find the best pricing for a product you already have in mind? We tested various AI agents by asking them to find the best available price for a Longchamp Le Pliage Original Tote Bag in Large/Black and Sony WH-1000XM5 headphones in Black. The exact prompt used is:

Please find the best available price for these two discretionary products across major retailers in the New York area or online - a Longchamp Le Pliage Original Tote Bag in Size Large, Color Black, and Sony WH-1000XM5 Wireless Noise Canceling Headphones in Black.

For each item, identify the lowest currently available price for the exact product and specify the retailer or platform offering it.

The challenge goes well beyond simply identifying the correct SKU. A truly effective AI agent must also navigate fragmented digital marketplaces to uncover the best promotional environment and pricing. In practice, none of the tools fully delivered on this. It is also worth noting that Amazon's Alexa and Walmart's Sparky were not able to handle both product requests at once, requiring the task to be broken down into individual queries to get usable results. For these tools, we split the task into two separate prompts — “please find the best available price for a Longchamp Le Pliage Original Tote Bag in size large, color black” and “please find the best available price for Sony WH-1000XM5 wireless noise-canceling headphones in black” — to obtain usable results.

Among the group, ChatGPT and Gemini stand out by identifying accurate pricing along with promotions. Claude has an incorrect SKU matching, which undermines its pricing accuracy. Amazon's Alexa takes a more flexible approach, directing users to alternative retailers when an item is not available on Amazon, and presenting product variations clearly within its interface when it is. Walmart's Sparky follows a similar pattern, but when an item is unavailable, it keeps the user within its ecosystem by recommending close substitutes, often sourced from its third-party marketplace. It was notable that the foundational models could not access Amazon's marketplace.

## EXHIBIT 20: ChatGPT and Gemini are consistently stronger at true price discovery, including on promotions.


Definitions - Product Accuracy - if AI agent can identify the correct product; Pricing Accuracy - is the pricing consistent with the product offering; Identifying Lowest Price - is the AI agent surfacing the lowest price available across the retailers.
Source: Bernstein analysis

## EXHIBIT 21: Gemini is the only AI model that identifies Nordstrom's availability and Bloomingdale's loyalist promotion.

## 1. Longchamp Le Pliage Original Tote Bag (Large, Black)

○ Lowest Price: \$180.00 Nordstrom
Retailers: Multiple major retailers are currently matching the standard MSRP on this highly controlled-price item. You can purchase it for this price online or in-store in the New York area at:

Longchamp Official Store / Website (Free ground shipping or free Click & Collect at local NYC boutiques) Longchamp
Nordstrom (Available online and for pickup at NYC locations like the flagship on W 57th St)
Nordstrom
Bloomingdale's (Available online and at NY area locations; Bloomingdale's is also offering a "Loyallists" reward bonus of \$50 for every \$200 spent if you are adding other items to your cart).

(Note: While unauthorized third-party platforms or resale sites like eBay or Poshmark list lower prices, \$180.00 is the lowest verified price from an authorized major retailer ensuring product authenticity).

Source: Gemini, Bernstein analysis

## EXHIBIT 22: ChatGPT is the only one that pulled the cheaper Costco pricing for the Sony headphones.

This excludes Amazon's marketplace offering, which it cannot seem to access.


Source: ChatGPT (OpenAI), Bernstein analysis

## EXHIBIT 23: Claude is displaying the wrong price for the Longchamp bag at \$170, with the actual price being \$180.

1. Longchamp Le Pliage Original Tote — Large, Black

Best available price (new): \~\$170 Retailer: Bloomingdale's (online + in-store pickup available in NYC area)

Bloomingdale's is currently listing the Longchamp Le Pliage at \$170, which is the standard market price across all major authorized retailers. Nordstrom also carries the Large Le Pliage Tote with free shipping and returns, and Longchamp's own website carries it as well — but none of these authorized retailers are discounting below \$170 at this time, as Longchamp tightly controls pricing across its distribution network. Bloomingdale's Nordstrom

A few notes:

- The Longchamp boutique at SoHo or the Longchamp shop-in-shop at Bloomingdale's 59th St. (both NYC) would carry this in-store at the same price.
- If you're open to pre-owned, platforms like Poshmark have listings for significantly less, but condition varies.
- There is no meaningful discount available at authorized retailers for this item right now.

Source: Claude (Anthropic), Bernstein analysis

## EXHIBIT 24: Amazon Alexa identified a retail price of \$175 instead of the correct \$180, showing a slight miss on pricing accuracy.

Longchamp.com US price is \$180.

▼ alexa for shopping

⑦ :

Unfortunately, the Longchamp Le Pliage Original Large Tote in Black doesn't appear to be available directly through Amazon at this time. Longchamp is typically sold through their own website and select retail partners.

Here's where you can find the best available prices:

- Longchamp.com – Official retail price is approximately \$175 for the Large Le Pliage Original Tote. Shopping directly ensures authenticity and the full color/size selection.
- Nordstrom (nordstrom.com) – Often carries it at the same retail price (\~\$175), sometimes with free shipping and returns.
- Saks Fifth Avenue (saksfifthavenue.com) – Occasionally offers it at the same price; worth checking for any promotions.

Source: Amazon Alexa, Bernstein analysis

## EXHIBIT 25: For the Sony headphones, since the product is listed on Amazon, Alexa is able to present multiple purchase options clearly and conveniently.

▼ alexa for shopping

⑦ :

Please find the best available price for the Sony WH-1000XM5 Wireless Noise Canceling Headphones in Black

Here's a breakdown of the best available prices for the Sony WH-1000XM5 Wireless Noise Canceling Headphones in Black:

Best Price - Certified Refurbished

See more


[[KC_IMAGE_025]]


Sony WH-1000XM5/B Wireless Industry Leading Noise Cance...

4.3 ★★★★☆ (1,234)
100+ bought in past month

\$19895
\$248.00
FREE delivery Tomorrow, Jun 2

Add to cart

Source: Amazon Alexa, Bernstein analysis

## EXHIBIT 26: Walmart doesn't stock Longchamp (1P), similar to its absence on Amazon. However, Sparky still provides alternatives from its third-party marketplace.

Here's what's available for the Longchamp Le Pliage Original large tote in black. Note: the first result is a new canvas travel bag variant — confirm the exact colorway on the product page, as black isn't explicitly listed in the title.


New condition, lowest price, free shipping included


[[KC_IMAGE_026]]


\$169 $^{99}$ Le Pliage Original Large


[[KC_IMAGE_027]]


\$280 $^{00}$ Pre-Owned Longchamp
Le ↓ Je Nylon Tote Bag...

Source: Walmart Sparky, Bernstein analysis

## OUR RECENT RESEARCH

\- US Broadlines Retail: Artificial intelligence...sooner or later...WMT best positioned in an AI era

- The Age of Agents: Agentic shopping and the future of retail media
- The Age of Agents: Insights from our Inaugural Agentic Commerce Day


O - Outperform, M - Market-Perform, U - Underperform, NR - Not Rated, CS - Coverage Suspended
TGT base year is 2025;
Source: Bloomberg, Bernstein estimates and analysis.
