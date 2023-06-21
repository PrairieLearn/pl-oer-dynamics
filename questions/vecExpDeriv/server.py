import random

import numpy as np
import prairielearn as pl


def generate(data):
    a = randIntNonZeroArray(2, -5, 5)
    aDot = randIntNonZeroArray(2, -5, 5)

    aMag = np.linalg.norm(a)
    aHat = a / aMag
    aMagDot = np.dot(aDot, aHat)
    aHatDot = (aDot - (np.dot(aDot, aHat) * aHat)) / aMag

    case = random.randint(1, 21)

    if case == 1:
        expr = "\\left\\|\\frac{d}{dt}\\vec{a}(t)\\right\\|"
        ansScalar = np.linalg.norm(aDot)
        units = "{\\rm\\ m/s}"
        data["correct_answers"]["ansScalar"] = ansScalar

    elif case == 2:
        expr = "\\frac{d}{dt}\\left\\|\\vec{a}(t)\\right\\|"
        ansScalar = aMagDot
        units = "{\\rm\\ m/s}"
        data["correct_answers"]["ansScalar"] = ansScalar

    elif case == 3:
        expr = "\\frac{da(t)}{dt}"
        ansScalar = aMagDot
        units = "{\\rm\\ m/s}"
        data["correct_answers"]["ansScalar"] = ansScalar

    elif case == 4:
        expr = "\\dot{\\hat{a}}(t)"
        ansValue1 = float(aHatDot[0])
        ansValue2 = float(aHatDot[1])
        units = "{\\rm\\ s^{-1}}"
        data["correct_answers"]["ansValue1"] = ansValue1
        data["correct_answers"]["ansValue2"] = ansValue2

    elif case == 5:
        expr = "\\frac{d\\hat{a}(t)}{dt}"
        ansValue1 = float(aHatDot[0])
        ansValue2 = float(aHatDot[1])
        units = "{\\rm\\ s^{-1}}"
        data["correct_answers"]["ansValue1"] = ansValue1
        data["correct_answers"]["ansValue2"] = ansValue2

    elif case == 6:
        expr = "\\displaystyle \\frac{d}{dt}\\left(\\frac{\\vec{a}(t)}{a(t)}\\right)"
        ansValue1 = float(aHatDot[0])
        ansValue2 = float(aHatDot[1])
        units = "{\\rm\\ s^{-1}}"
        data["correct_answers"]["ansValue1"] = ansValue1
        data["correct_answers"]["ansValue2"] = ansValue2

    elif case == 7:
        expr = "\\dot{\\vec{a}}(t) \\cdot \\hat{a}(t)"
        ansScalar = np.dot(aDot, aHat)
        units = "{\\rm\\ m/s}"
        data["correct_answers"]["ansScalar"] = ansScalar

    elif case == 8:
        expr = "\\dot{\\hat{a}}(t) \\cdot \\dot{\\vec{a}}(t)"
        ansScalar = np.dot(aHatDot, aDot)
        units = "{\\rm\\ m/s^2}"
        data["correct_answers"]["ansScalar"] = ansScalar

    elif case == 9:
        expr = "\\dot{\\hat{a}}(t) \\cdot \\vec{a}(t)"
        ansScalar = 0
        units = "{\\rm\\ m/s}"
        data["correct_answers"]["ansScalar"] = ansScalar

    elif case == 10:
        expr = "\\frac{d}{dt}\\left(\\vec{a}(t) \\cdot \\vec{a}(t)\\right)"
        ansScalar = 2 * aMag * aMagDot
        units = "{\\rm\\ m^2/s}"
        data["correct_answers"]["ansScalar"] = ansScalar

    elif case == 11:
        expr = "\\frac{d}{dt}\\left(a(t)\\right)^2"
        ansScalar = 2 * aMag * aMagDot
        units = "{\\rm\\ m^2/s}"
        data["correct_answers"]["ansScalar"] = ansScalar

    elif case == 12:
        expr = "\\frac{d}{dt}\\left(\\vec{a}(t) \\cdot \\hat{a}(t)\\right)"
        ansScalar = aMagDot
        units = "{\\rm\\ m/s}"
        data["correct_answers"]["ansScalar"] = ansScalar

    elif case == 13:
        expr = "\\displaystyle \\frac{d}{dt}\\left(\\frac{\\vec{a}(t) \\cdot \\vec{a}(t)}{a(t)}\\right)"
        ansScalar = aMagDot
        units = "{\\rm\\ m/s}"
        data["correct_answers"]["ansScalar"] = ansScalar

    elif case == 14:
        expr = "\\frac{d}{dt}\\left(\\hat{a}(t) \\cdot \\hat{a}(t)\\right)"
        ansScalar = 0
        units = "{\\rm\\ s^{-1}}"
        data["correct_answers"]["ansScalar"] = ansScalar

    elif case == 15:
        expr = "\\displaystyle \\frac{d}{dt}\\left(\\frac{\\vec{a}(t) \\cdot \\vec{a}(t)}{(a(t))^2}\\right)"
        ansScalar = 0
        units = "{\\rm\\ s^{-1}}"
        data["correct_answers"]["ansScalar"] = ansScalar

    elif case == 16:
        expr = (
            "\\frac{d}{dt} \\operatorname{Proj}\\left(\\vec{a}(t), \\hat{a}(t)\\right)"
        )
        ansValue1 = float(aDot[0])
        ansValue2 = float(aDot[1])
        units = "{\\rm\\ m/s}"
        data["correct_answers"]["ansValue1"] = ansValue1
        data["correct_answers"]["ansValue2"] = ansValue2

    elif case == 17:
        expr = "\\frac{d}{dt} \\left\\| \\operatorname{Proj}\\left(\\vec{a}(t), \\hat{a}(t)\\right) \\right\\|"
        ansScalar = aMagDot
        units = "{\\rm\\ m/s}"
        data["correct_answers"]["ansScalar"] = ansScalar

    elif case == 18:
        expr = "\\frac{d}{dt}\\left(a(t) \\hat{a}(t)\\right)"
        ansValue1 = float(aDot[0])
        ansValue2 = float(aDot[1])
        units = "{\\rm\\ m/s}"
        data["correct_answers"]["ansValue1"] = ansValue1
        data["correct_answers"]["ansValue2"] = ansValue2

    elif case == 19:
        expr = "\\frac{d}{dt}\\left\\|a(t) \\hat{a}(t)\\right\\|"
        ansScalar = aMagDot
        units = "{\\rm\\ m/s}"
        data["correct_answers"]["ansScalar"] = ansScalar

    elif case == 20:
        expr = (
            "\\frac{d}{dt} \\operatorname{Proj}\\left(\\hat{a}(t), \\vec{a}(t)\\right)"
        )
        ansValue1 = float(aHatDot[0])
        ansValue2 = float(aHatDot[1])
        units = "{\\rm\\ s^{-1}}"
        data["correct_answers"]["ansValue1"] = ansValue1
        data["correct_answers"]["ansValue2"] = ansValue2

    else:
        expr = "\\frac{d}{dt} \\left\\|\\operatorname{Proj}\\left(\\hat{a}(t), \\vec{a}(t)\\right)\\right\\|"
        ansScalar = 0
        units = "{\\rm\\ s^{-1}}"
        data["correct_answers"]["ansScalar"] = ansScalar

    data["params"]["a_vec"] = cartesianVector(a)
    data["params"]["aDot_vec"] = cartesianVector(aDot)
    data["params"]["a"] = pl.to_json(a)
    data["params"]["aDot"] = pl.to_json(aDot)
    data["params"]["expr"] = expr
    data["params"]["units"] = units

    vector_list = [4, 5, 6, 16, 18, 20]

    if case not in vector_list:
        data["params"][
            "submitAnswer"
        ] = """<pl-number-input answers_name="ansScalar" comparison="relabs" rtol="1e-2" atol="1e-5" size="15" show-placeholder="false"></pl-number-input>"""
    else:
        data["params"][
            "submitAnswer"
        ] = """<pl-number-input answers_name="ansValue1" comparison="relabs" rtol="1e-2" atol="1e-5" display="inline" size="15" show-placeholder="false"></pl-number-input> $\\hat{\\imath} + $\
		<pl-number-input answers_name="ansValue2" comparison="relabs" rtol="1e-2" atol="1e-5" display="inline" size="15" show-placeholder="false"></pl-number-input> $\\hat{\\jmath}$"""

    return data


def vectorInBasis(v, basis1, basis2, basis3):
    """v: numpy array of size (3,)
    basis1: first basis vector
    basis2: second basis vector
    basis3: third basis vector, default ""
    """

    basis_list = [basis1, basis2, basis3]
    s = []
    e = 0
    v = v.tolist()
    for i in range(len(v)):
        if type(v[i]) == float:
            if v[i] == int(v[i]):
                v[i] = int(v[i])
        e = str(v[i])
        if e == "0":
            continue
        if e == "1" and basis_list[i] != "":
            e = ""
        if e == "-1" and basis_list[i] != "":
            e = "-"
        e += basis_list[i]
        if len(s) > 0 and e[0] != "-":
            e = "+" + e
        s.append(e)
    if len(s) == 0:
        s.append("0")
    return "".join(s)


def cartesianVector(v):
    return vectorInBasis(v, "\\hat{\\imath}", "\\hat{\\jmath}", "\\hat{k}")


def randIntNonZeroArray(n, a, b, step=1):

    """n: size of the array
       a: lower bound of the range of integers
       b : upper bound of the range of integers
    returns a non-zero vector whose components are integers in the range [a,b]

    """

    r = np.zeros(n)

    while np.linalg.norm(r) == 0:
        if n == 2:
            r = np.array(
                [random.randrange(a, b, step), random.randrange(a, b, step), 0]
            )
        elif n == 3:
            r = np.array(
                [
                    random.randrange(a, b, step),
                    random.randrange(a, b, step),
                    random.randrange(a, b, step),
                ]
            )

    return r
