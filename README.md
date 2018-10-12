# Usage

## Create a deposit account and or a set of target accounts

touch ~/.jobcoin.db.json
docker run -it -v "$HOME/.jobcoin.db.json:/usr/src/app/.jobcoin.db.json" \ 
    --rm cbeach/gemini_challenge

mix [--targets <addr1> <addr2> ... ] [--branching <int>] [--duration <int>]

  --targets: optional list of addresses that you would like the jobcoins to be sent to.
  --branching: The number of addresses to create if targets is not specified. Default is 5
  --duration: The number of minutes to stagger the mixing over. Increases difficulty of deanonomization Default is 60.

## Do the mixing transactions

docker run -it --rm -v "$HOME/.jobcoin.db.json:/usr/src/app/.jobcoin.db.json" \
    cbeach/gemini_cron_challenge

# Explanation

  I use a simple cli to create the deposit and (optionally) target accounts.
  After a user deposits job coins into the deposit account a cron job starts processing the 
  transactions. First to the house account, and then to the target account.
  This implementation is not ideal as there will be a strong temporal correlation between the
  deposits and transfers. This will make it easy-ish for third parties to figure out what's 
  going on. This is highly dependent on how big and how busy the mixer is of course.

  I didn't have time to implement this, but a better implementation would add a random delay to
  all of the transfers instead of doing them as soon as possible. 
  
  A third party may be able to deanonomyze a mixer given a sufficient number of transactions 
  with the naive solution. Randomizing the time of deposit along with the target accounts should 
  make that more difficult.


# Additions thoughts


## Additional Tests

There are a _bunch_ of tests that I would like to put in here. The following is a short list.

  - Test more argument combinations for mixer.create_mixer_addresses.
  - Negative tests for just about everything.
    - Exceptions, bad inputs, missing db file, etc.
  - Test that the "database" is written correctly.
  - I would test the _hell_ out of the mix script, since that's the most complex and
    the most critical piece of code.


## The "database"

  I just used a flat file instead of a full fledged database like postgres to simplify the 
  implementation and make it faster to code.

## Rounding errors

  I got a rounding error of 1e-14. Not worth spending time on (in the case of a non-production 
  coding challenge) but still _very_ annoying. A small part of me _swears_ that that .00000000000001 
  is mocking me.
  
  I would remedy this with an arbitrary precision floating point math library such as decimal 
  or mpmath. This would come with performance costs and extra work though. It's really not worth 
  though. Even if jobcoins were worth what bitcoin was at it's highest valueation, we're still
  talking about 1e-10 dollars...


