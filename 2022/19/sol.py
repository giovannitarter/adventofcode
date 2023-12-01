#!/usr/bin/python


import sys
import copy
import re
import functools

ORE = 0
CLY = 1
OBS = 2
GEO = 3

STR_TO_IDX = {
    "ore" : ORE,
    "clay" : CLY,
    "obsidian": OBS,
    "geode" : GEO,
    }

IDX_TO_STR = {
        ORE : "ore",
        CLY : "clay",
        OBS : "obsidian",
        GEO : "geode",
    }


def parse_input(text):

    res = {}
    text = text.replace("\n", "")
    bps = [x for x in text.split("Blueprint ") if x != ""]

    for b in bps:

        bp = [[0 for _ in range(3)] for _ in range(4)]

        bnr, resources = b.split(":")
        resources = [r.strip() for r in resources.split(".") if r != ""]

        for r in resources:
            m = re.match(r"Each (\w+) robot costs (\d*) (\w+)", r)
            row = bp[STR_TO_IDX[m.group(1)]]
            row[STR_TO_IDX[m.group(3)]] = int(m.group(2))

            rest = r[m.end() + 1:]
            if rest:
                m = re.match(r"and (\d*) (\w*)", rest)
                row[STR_TO_IDX[m.group(2)]] = int(m.group(1))

        bp = tuple([tuple(x) for x in bp])
        res[int(bnr)] = bp

    return res


def print_blueprint(nr, mat):

    txt = [f"blueprint {nr}"]
    for idx, row in enumerate(mat):
        tp = IDX_TO_STR[idx]

        txt.append(tp)
        for ridx, cost in enumerate(row):
            txt.append(f" - {IDX_TO_STR[ridx]}: {cost}")
        txt.append("")

    print("\n".join(txt))

    return


@functools.lru_cache(maxsize=100000)
def get_neighs(resources, robots, blueprint, max_req):

    res = []


    for rob_type in IDX_TO_STR:

        rs_need = [rs - rq for rs, rq in zip(resources, blueprint[rob_type])]

        max_time = 0
        cant_build = False
        for i in range(3):
            rb = robots[i]
            rs_nd = rs_need[i]

            if rs_nd == 0 and rb == 0:
                continue

            elif rs_nd != 0 and rb == 0:
                cant_build = True
                break

            else:
                tmp = -(rs_nd // rb) + 1

                if tmp < 1:
                    tmp = 1

                if tmp > max_time:
                    max_time = tmp

        if cant_build:
            continue

        #print(f"{IDX_TO_STR[rob_type]} needs {max_time} time")

        new_res = [rs - rq + (rb * max_time) for rs, rb, rq
                in zip(resources, robots, blueprint[rob_type])]
        new_res.append(resources[3] + robots[3] * max_time)
        new_res = tuple(new_res)

        new_rob = list(robots)
        new_rob[rob_type] = new_rob[rob_type] + 1
        new_rob = tuple(new_rob)

        res.append((max_time, rob_type, new_res, new_rob))

    return res


def sum_up_to(n):
    return (n) * (n + 1) / 2


#@functools.cache
def analyze_blueprint(time, resources, robots, blueprint, max_req, path, max_time=32, curr_max=0):

    #indent = " " * time
    #print(f"{indent}analyze_blueprint t:{time} res:{resources}, rob:{robots}")

    if time > max_time:
        #print(f"{indent}ret {resources[GEO]}")
        return (resources[GEO] - ((time - max_time) * robots[3]), path)

    curr_geo = robots[3]
    if curr_geo > 0:
        remaining = max_time - time
        max_geo = resources[3] + sum_up_to(curr_geo + remaining) - sum_up_to(curr_geo)
        if max_geo < curr_max:
            return (0, [])

    res = []


    neighs = get_neighs(resources, robots, blueprint, max_req)
    for t, r_type, new_res, new_rob in neighs:

        if r_type < 3:
            if new_rob[r_type] > max_req[r_type]:
                continue

        npath = list(path)
        npath.append((time + t, r_type))

        if time + t > max_time:
            res.append((new_res[GEO] - ((time + t - max_time) * new_rob[3]), npath))
        else:
            #recursive call
            #print(f"{indent}build {r_type}")

            tmp = analyze_blueprint(time + t, new_res, new_rob, blueprint, max_req, npath, max_time, curr_max)
            curr_max = max(curr_max, tmp[0])
            res.append(tmp)


    if res:
        geodes = [r[0] for r in res]
        max_g = max(geodes)
        idx = geodes.index(max_g)
        res = res[idx]

    else:
        res = (0, [])

    return res


#def analyze_blueprint(time, resources, robots, blueprint, max_req, path, min_time=24, max_time=32):
#
#    indent = " " * time
#    #print(f"{indent}analyze_blueprint t:{time} res:{resources}, rob:{robots}")
#
#    if time > min_time:
#        return (max_time, [])
#
#    if robots[CLY] >= 2 and robots[GEO] >= 5:
#        #print(f"{robots}")
#        return (time, path)
#
#    res = (max_time, [])
#
#    neighs = get_neighs(resources, robots, blueprint, max_req)
#    #for n in neighs:
#        #print(f"{indent}{n}")
#
#    for t, r_type, new_rob, new_res in neighs:
#
#        npath = list(path)
#        npath.append((time + t, r_type))
#
#        tmp = analyze_blueprint(time + t, new_res, new_rob, blueprint, max_req, npath, min_time, max_time)
#        if tmp[0] < min_time:
#            min_time = tmp[0]
#            res = tmp
#
#    return res


def sol01(data):

    res = 0

    bp = data[2]
    max_req = tuple([max(l) for l in zip(*bp)])
    print(max_req)

    res = analyze_blueprint(
            0,
            (0, 0, 0, 0),
            (1, 0, 0, 0),
            bp,
            max_req,
            [],
            )


    #res = []
    #for k in data:
    #    bp = data[k]

    #    max_req = tuple([max(l) for l in zip(*bp)])

    #    get_neighs.cache_clear()
    #    max_geo = analyze_blueprint(
    #            0,
    #            (0, 0, 0, 0),
    #            (1, 0, 0, 0),
    #            bp,
    #            max_req,
    #            [],
    #            )

    #    print(f"bp: {k} -> {max_geo[0]}")
    #    res.append(max_geo[0] * k)

    #res = sum(res)

    return res


def sol02(data):

    res = 1

    for i in [1, 2, 3]:
        bp = data[i]

        max_req = tuple([max(l) for l in zip(*bp)])
        print(f"max_req: {max_req}")

        bp_res = analyze_blueprint(
            0,
            (0, 0, 0, 0),
            (1, 0, 0, 0),
            bp,
            max_req,
            [],
            )

        print(bp_res)
        res = res * bp_res[0]

    return res


if __name__ == "__main__":

    RES = None

    FD = open(sys.argv[1])
    TEXT = FD.read()
    FD.close()

    DATA = parse_input(TEXT)

    #for d in DATA:
    #    print("")
    #    print_blueprint(d, DATA[d])

    # print(f"DATA:\n{DATA}\n")

    #SOL01 = sol01(DATA)
    #print("SOL01: {}".format(SOL01))

    SOL02 = sol02(DATA)
    print("SOL02: {}".format(SOL02))

