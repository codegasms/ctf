# 1. Buried Truths

## Flag

```
ENIGMA{M4sk3d_L4y3r_Unc0v3r3d}
```

## Solution

The description:

```json
      "description": [
        "A peculiar file has buried_truths.xcf.",
        "Rumor has it that something valuable is buried within, hidden carefully from plain sight.",
        "Those who look deep enough, past the obvious, may discover what lies beneath.",
        "",
        "Unravel the mysteries concealed within.",
        "Somewhere, among the layers and whispers of this file, a flag is waiting to be found.",
        "Can you see what others cannot?",
        "",
        "buried_truths.xcf: https://enigma-iiits-940425c54ad6.herokuapp.com/file?team_id=e7be80d0ab78474aba4854b66cdac8cc&challenge_id=1",
        ""
      ],
```

gives it away that the flag is hidden in some layer of the image file when opened in GIMP. Opening in GIMP and moving the layers reveals the flag.
