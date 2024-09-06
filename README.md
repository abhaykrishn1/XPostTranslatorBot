# XPostTranslatorBot
.
Sprint1: initial Plan
using google's translation library understand lang & convert the text to english language.    done 
Post with the bot using valid credentials of api key & twetter dev on the api level.      done 

Problem: Paid service to utilize @mention & reply service with the twitter n tweetpy library.
Solution: => Swithching to handel the replies on front end.
pros: free, good enough speed for protype & few requests per seconds.
cons: slower, can not be highly scaled due to rate-limiter constraints of twitter.


Proposal: utilizing the selenium automation we will handel mention request on the localhost-initially for the prototype.

Sprint2: 
set up selenium to get elements & get the post-id from @mention.
check the speed how fast we can reply with a simple text to that mention. is this actually usable?
understand rate limitter of twitter to avoid getting timeouts and blocked.

sprint3:


sprint4:
deployment

