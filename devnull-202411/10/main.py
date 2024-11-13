def poly(a, x):
    value = 0
    for ai in a:
        value *= x
        value += ai

    return value


def make_correct_array(s):
    from itertools import accumulate

    s = map(ord, s)  # maps each character to their ascii value
    s = accumulate(s)  # sums all of them up
    return [x for x in s]


def validate(a, xs):
    if len(a) != len(xs) + 1:
        return False
    else:
        for x in xs:
            value = poly(a, x)
            if value != 0:
                return False

        return True


def solve(a: list[int]):
    flag_str = ""
    pref = 0

    for _ in range(len(a) - 1):
        for c in range(1, 128):
            if poly(a, pref + c) == 0:
                flag_str += chr(c)
                pref += c
                break

    flag = make_correct_array(flag_str)
    assert validate(a, flag)
    print(flag_str)


if __name__ == "__main__":
    a = [
        1,
        -30886,
        453546012,
        -4213674459504,
        27804035388011796,
        -138671897811922779120,
        543178459158535321695744,
        -1714023446590241825599620888,
        4434713053917745333136248121742,
        -9525733017914185678994508748853676,
        17136846938963676129666191162770578120,
        -25976102950212508247952789672284715938424,
        33302212151428123065129233293063623648862068,
        -36178712845702939664537069938839543151428218592,
        33311871065155942467647888289882350852530164963456,
        -25958942258695665028912725953469335994824470751623560,
        17067599451929810038541773883085595126305686470416921369,
        -9421806504069495193142716685514449856795549328337994668478,
        4336772747326070909827233644258088737490203326982121667996892,
        -1648933499121905939942939873107871839866348337715045435408671736,
        511489795126307247583061570839863381805128474049498180425594452304,
        -127315184501287716543244446315506551597567384367167202932453269730848,
        24867990336339297930402645390116144748790590254854233760982977511059776,
        -3695463685118689992364882952953931477248090279675416069452193455153973888,
        399385898629832852418700507872158203067058347204092764839730571326456798720,
        -29244813341049522639942347704680700920705188178823103590645875147398038886400,
        1277538368507685816686109727374539531501006544681036553725723237906270563328000,
        -24601444193306808305027283216475321083817842282573039702949168787885669498880000,
    ]

    solve(a)

if False:
    print(a)
    flag_str = input("flag: ").strip()
    flag = make_correct_array(flag_str)
    print("flag text from make_correct_array: ", flag)
    if validate(a, flag):
        print("Yes, this is the flag!")
        print(flag_str)
    else:
        print("Incorrect, sorry. :(")
