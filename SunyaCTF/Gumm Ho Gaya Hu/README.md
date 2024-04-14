# Gumm Ho Gaya Hu [Misc/Web]

## Description

Hello, my friends, this is yo boi Snip3R straight outta P-town, here we go another web challenge from me, saw your rants and thought of creating an EZPZ challenge for ya'll (maybe). So here you go, solve this ez web based chall currently introduced to misc section COZ WHY NOT.

Mai jo guum hogaya hu inn aankho me jaan, Don't you know bout mah love, ye an bewafa, Tere fizao me mai khoya reheta hu, Sab dil ki baate, tujhi se meri jaan (that was just rubbish nothing related to the challenge ~ maybe)

A bit to describe, you ain't getting da whole flag in a single go, so keep hunting like my sweet little child. 💋

<https://noverse.net/>

## Solution

`0CTF{50m371m35_17_0nly_l00k5_d1ff1cul7_bu7_15n7_4c7u4lly}`

## But How?

### Inspect Elements

Since this was an easy challenge, started with the basics i.e. Inspect Elements.

1. **HTML**

    ```html
    ...
    <!--        0CTF{50m371m35_          -->
    </html>
    ```

2. **CSS**

    ```css
    ...
    /* 17_0nly_l00k5 */
    label {
        font-weight: bold;
    }
    ...
    ```

3. **JS**

    ```javascript
        ...
        loginMessage.style.fontWeight = "bold"; // _d1ff1cul7_bu7
        return; // Stop further execution
    }
    ...
    ```

4. **robots.txt**

    ```plaintext
    ...
    Disallow: /tmp/
    Disallow: _15n7_4c7u4lly}
    Disallow: /wp-admin/
    Disallow: /checkout
    ...
    ```

P.S. : Other possible locations to look for the flag could be in the cookies, local storage, network tab, etc.
