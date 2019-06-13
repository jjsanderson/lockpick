# Lockpick - pick Wendy’s bike lock

My friend Wendy has a bike lock with a four-letter combination, which she’s forgotten.
This script takes the possible code wheel letters and iterates across all possible combinations, 
checking each possibility against lists of common English and Welsh words. Possible combinations
 which appear in the lists are output to the console.

## Usage

Pull the repository to a local Python3 environment; run `lockpick.py` in a terminal. The only 
dependency is `io`, which should be internal.

## Improvements

Longer word lists would increase the chances of a successful hit. However, lists like this are
tricky to come by for Welsh. For English, there’s a 470k word list elsewhere on github. Pull requests welcome.

## Development

This script was written in the small hours of the morning on my phone, using the amazing [Pythonista](http://omz-software.com/pythonista/), while
balancing my sleeping three-day-old baby on my knee. It’s not a great way of doing it, but it does work. 
Run time on an iPhone 6s is of order a second.
