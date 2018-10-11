# Decisions

  - I'm using Couchbase
    - I'm familiar with it
    - I have code laying around ready to cargo culted
    - I don't have to deal with a schema
  - I'm not going to keep a log of who owns what


# Questions for Gemini dev

  - I've never done one of these before. What gotchas/security implications should I be looking out for?
  - RESTful API or bag-o-functions
  - What kind of branching factor are you looking for?
  - Seeing as this is a toy example, how should I deal with incomplete transactions? (should I care?)
  - I can see clear problems with keeping a log, mainly revolving around privacy (what if that log were compromised). Are there any counter examples FOR keeping a log that I should be aware of?


# Answered myself

  - How do I create a new address through the api?
    - curl 'https://jobcoin.gemini.com/greeting/create' --data 'address=Casey'

