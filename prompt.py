prompt_for_sentiment_analysis = """

Analyze the sentiment of the following text.
Classify the sentiment as positive, negative, or neutral based on the emotions, tone, and language used. 
Provide a brief explanation of why you classified the sentiment that way, citing specific words or phrases from the text.

Examples:

1. Text: "The product arrived on time and exceeded my expectations. I love it!"
   Sentiment: Positive
   
   Percentage: Positive (90%), Neutral (10%), Negative (0%)
   Explanation: The text uses phrases like "arrived on time" and "exceeded my expectations," indicating satisfaction. The expression "I love it!" reinforces the positive sentiment.

2. Text: "I was really disappointed with the service. It was slow, and the staff seemed uninterested."
   Sentiment: Negative
   
   Percentage: Negative (85%), Neutral (15%), Positive (0%)
   Explanation: Words like "disappointed," "slow," and "uninterested" indicate a negative experience.

3. Text: "The event was fine, but nothing special. It met the basic expectations."
   Sentiment: Neutral
   
   Percentage: Neutral (80%), Positive (10%), Negative (10%)
   Explanation: The text uses neutral phrases like "fine" and "nothing special," showing no strong positive or negative feelings.

Now, analyze the sentiment of the following text:

Text: {user_text}"""