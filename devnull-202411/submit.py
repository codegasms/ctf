import requests


def submit(challenge_id: str, flag: str) -> str:
    r = requests.post(
        "https://enigma-iiits-940425c54ad6.herokuapp.com/submit",
        json={
            "team_id": "e7be80d0ab78474aba4854b66cdac8cc",
            "flag": flag,
            "challenge_id": challenge_id,
        },
    )
    return r.json()


# print(submit("1", "ENIGMA{M4sk3d_L4y3r_Unc0v3r3d}"))
# print(submit("2", "ENIGMA{R5A_i5_3A5y_bF9laXZFbF9zZVZFbl9fN468ELejZrNOWc5oGd9SSXeDDSDkNjy8GVTR90Tkw4msGbaKge6iZtSXnnvRIYhIKQ==}"))
# print(submit("3", "ENIGMA{d3crypt!_c0mp13t3_857b1d4891cf5c9171c2e117b46e4d0e}"))
# print(submit("4", "ENIGMA{3CH0-0F-3N1GMA}"))
# print(submit("5", "ENIGMA{0r1giN_0f_3N1GM4}"))
# print(submit("6", "ENIGMA{fd8abd1f770d242ee40a0e76d7b493552135a6cb4d53923f19659bab7dbce64f}"))
# print(submit("7", "ENIGMA{c0mm1t_0r_d13_try1ng_8548f6c834f4a9e55e6553b12ab92dbd}"))
# print(submit("9", "ENIGMA{LSB_ST3g_bF9laXZFbF9TRVZlbl83XwgDinDp8+zPHSBGj/NRmeWdKH0BnBtUensV/p5Z8xGdLGFPxDi5fjWYLTkhBuFkUQ==}"))
# print(submit("10", "ENIGMA{f1naL_b0S5_cLl3ar3D}"))
# print(submit("11", "ENIGMA{c2a4ebfd3d010764ec98fce00ec9cc30_50}"))
# print(submit("12", "ENIGMA{mY_34Rs_4r3_bl33D1nG}"))
