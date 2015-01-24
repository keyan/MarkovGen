# MarkovGen
This module takes any string input and constructs a dictionary containing the frequency that following words occur. This can be used to probabilistically generate text which resembles the original input. The user can also specify how long to make the final output. 

I had originally planned to add the option of accepting a user defined n-gram length, but I feel that I reached the point of diminishing educational return. Currently uses n-gram of 2, which generates decent, but oftentimes nonsensical text.

Usage: `python markov.py <filename>.txt <# of words>`

Some example text generate from [The Sayings of Confucius]:
>In awe he is stable a man with enquiries to another state

>Come from afar do we not rejoice to live unknown

>They are unprincipled stern men of arts and learning delights 

>His face changed when he was asked what is meant by kindness without waste

[The Sayings of Confucius]: https://www.gutenberg.org/ebooks/24055