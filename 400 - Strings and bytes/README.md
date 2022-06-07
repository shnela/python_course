# Python strings and bytes
    
## [A Guide to Unicode, UTF-8 and Strings in Python][]

### What is ASCII?
> While reading bytes from a file, a reader needs to know what those bytes mean.
> So if you write a JSON file and send it over to your friend,
> your friend would need to know how to deal with the bytes in your JSON file.
> For the first 20 years or so of computing, upper and lower case English characters,
> some punctuations and digits were enough. These were all encoded into a 127 symbol list called ASCII.
> 7 bits of information or 1 byte is enough to encode every English character.
> You could tell your friend to decode your JSON file in ASCII encoding, and voila
> — she would be able to read what you sent her.
>
> This was cool for the initial few decades or so,
> but slowly we realized that there are way more number of characters than just English characters.
> We tried extending 127 characters to 256 characters (via Latin-1 or ISO-8859–1)
> to fully utilize the 8 bit space — but that was not enough.
> We needed an international standard that we all agreed on to deal with hundreds and thousands
> of non-English characters.

### What is Unicode?
> Unicode is international standard where a mapping of individual characters and a unique number
> is maintained. As of May 2019, the most recent version of Unicode is 12.1 which contains over
> 137k characters including different scripts including English, Hindi, Chinese and Japanese,
> as well as emojis. These 137k characters are each represented by a unicode code point.
> So unicode code points refer to actual characters that are displayed.
> 
> These code points are encoded to bytes and decoded from bytes back to code points.
> Examples: Unicode code point for alphabet a is U+0061, emoji 🖐 is U+1F590, and for Ω is U+03A9.

### What does it have to do with Python?
[Pragmatic Unicode by Ned Batchelder][]  
[Unicode sandwich][]

## String and bytes in python3
[Łona - ąę][] (album "Absurd i Nonsens")

```python
unicode_string = 'Łona - ąę'
print(unicode_string)
# Łona - ąę
assert len(unicode_string) == 9
assert type(unicode_string) is str
assert unicode_string[0] == 'Ł'
assert unicode_string[::-1] == 'ęą - anoŁ'

bytes_sequence = unicode_string.encode()
print(bytes_sequence)
# b'\xc5\x81ona - \xc4\x85\xc4\x99'
assert len(bytes_sequence) == 12
assert bytes_sequence[0] == 0xc5  # 197 (int)

assert bytes_sequence.decode() == unicode_string
print(bytes_sequence[::-1])
# b'\x99\xc4\x85\xc4 - ano\x81\xc5'
bytes_sequence[::-1].decode()  # UnicodeDecodeError: 'utf-8' ...
```

## Working with files   
[Python open file][]
```python
f = open('output1.txt', 'w')
f.write('Internal of file')
f.close()

# But it's more convenient to skip close
with open('output2.txt', 'w') as f:
    f.write('Internal of file')
```

### Exercises
* [count_words.py](count_words.py)
* [rewrite_order.py](rewrite_order.py)


<!--- Links -->
[Python open file]: https://www.w3schools.com/python/python_file_handling.asp
[A Guide to Unicode, UTF-8 and Strings in Python]: https://towardsdatascience.com/a-guide-to-unicode-utf-8-and-strings-in-python-757a232db95c
[Pragmatic Unicode by Ned Batchelder]:  https://bit.ly/unipain
[Unicode sandwich]: https://nedbatchelder.com/text/unipain/unipain.html#35
[Łona - ąę]: https://www.youtube.com/watch?v=T2iISWltdzc
