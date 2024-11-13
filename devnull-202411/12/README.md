# 12. ThisIsHowTheStoryGoeso

## Flag

```
ENIGMA{mY_34Rs_4r3_bl33D1nG}
```

## Solution

I first wrote `fail.py` to find if something is stored in the LSB of audio frames. Could not find anything.

When listening to the entire song, which the challenge description emphasizes, there is some beeping sound towards the end. Opening the `KSI.wav` file in Audacity and switching to spectrogram view shows text embedded in the spectrogram towards the end of the song timeline.
