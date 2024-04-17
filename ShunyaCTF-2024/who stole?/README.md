# who stole? [OSINT]

## Description

One of our members love guitar and music. ⁠

Don’t wanna badmouth but he’s a boomer, bro uses YouTube instead of Spotify XD. ⁠Also, he’s very defensive of his fav artists and will not like if anyone sample their beats (or as he calls that “stealing”)

## Solution

`0CTF{mu51c41_fl4g}`

## But How?

### Find The Boomer

![boomer](./img/boomer.png)

This guy looked like a `Boomer` to me. At this point it is naive to just search for this guy's name on social media platforms (time consuming & we don't even know his social handles). So, went to `ncreeps` social handles to search for this guy.

![found](./img/guitarguy.png)

Found the `Guitar Guy` on `ncreeps` social handles. He is the `Boomer` we are looking for.

### Trace Him

![instagram](./img/insta.png)

![threads](./img/threads.png)
![youtube](./img/youtube.png)

**BAMM!!**, Found the youtube channel : <https://www.youtube.com/@tavishguitar>

### Who Are The Fav Artists?

Checked the first video `i love this song` and the description was not that interesting as compared to `my fav song`.

> this song is also special to me. it's about secret and how you lose them as you become more transparent :(
>
> _____
> since I LOVE this song, I will DEFEND her from whoever steals the music RAHHH 🦅🦅🦅

Now, what is this song? Using any tool such as `Shazam` or `SoundHound` or even `Google Assistant` we can find the song.

It was `Familiar - Agnes Obel`.

P.S : I knew this music from the series `Dark` (Recommended By Me :D)

### THA DESCRIPTION MANN

Both the description of the challenge and the video had something about `music sampling`. So, went ahead to check if this song was sampled by any other artist.

> Found this website : <https://www.whosampled.com/>

![sample](./img/sample.png)

The 3rd one was taken down on Youtube, so went with the first 2.

### THA FLAGS

Just searched for the songs on Youtube and found the flags in the comments.

1. **Ice Spice - Euphoric** <https://www.youtube.com/watch?v=Hjoqr2_-Fhw>
2. **PHARAOH - RAW 2** <https://www.youtube.com/watch?v=52i5LO8eETQ>

P.S. : Don't forget to sort the comments by `Newest First`.

![falg1](./img/f1.png)
![flag2](./img/f2.png)
