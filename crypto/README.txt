OVERVIEW:This program outputs the frequency of characters in a file,
as well as testing the I.C. (Index of Coincidence) to see how close
to a real English sentence the string possibly is.

FEATURES: This program features functions to calculate the frequncy
of letters in a file, a function to calculate the probabilty of
text from that file being a real English sentence, and a quality of
life function fileformat.

LIMITATIONS: The main limitation is that this will only work on
ciphers that use alphabetical characters to scramble a message.
Also as the length of a key of a polyalphabetic cipher gets larger,
the accuracy of the I.C. drops.

PYTHON VERSION: 3.4

LIBRARIES: collections; imported to use specifically to format my
dictionary correctly so that I could run my I.C. calculator

COMMAND LINE: run as python3 cipher2.py
This should run my program fine, follow the prompts after
I'm currently having issues with the click import, so I didn't
use it for this HW.

REFERENCES: (https://github.com/CryptoUSF/Course-Material/blob/master/code/cipher.py#L226)
(Cornell University :http://pi.math.cornell.edu/~mec/2003-2004/cryptography/polyalpha/polyalpha.html)
(UC Davis: http://nob.cs.ucdavis.edu/classes/ecs155-2013-04/extras/vigenere.html)
(Practical Cryptography: http://practicalcryptography.com/cryptanalysis/text-characterisation/monogram-bigram-and-trigram-frequency-counts/)
(Stack overflow: many times)