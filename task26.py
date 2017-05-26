
perm = "(-32 -39 +106 +101 +52 +57 +40 -67 +88 -12 -131 +54 -126 -59 -25 +36 +119 +89 +69 -1 +87 +100 +122 +53 +21 +93 -105 -134 +111 -23 +43 +33 +107 +13 -113 -133 +80 -77 -29 -102 -10 -26 +125 -62 -19 -90 -9 +96 +123 +75 +114 +20 +65 -49 -68 +118 -117 -81 -11 -24 +17 +116 +7 -124 +42 +31 +45 -51 -82 +4 +79 +104 -76 +63 -132 -130 -56 +15 -35 -30 -92 +60 -61 +41 -129 +110 -14 +16 +2 -94 +85 -3 -34 +70 +48 -8 +28 -97 +86 +91 +72 -99 +71 -121 +112 +84 +27 -46 +50 +37 +83 -108 -95 +120 -18 +44 +58 +78 -6 +38 -5 +22 +74 -109 +128 +55 -98 -66 -64 -115 -103 -73 -135 -47 +127)".replace(")", "").replace("(", "").split()
perm = map(int, perm)

def perm_sort(perm):
    result = []
    # result.append(perm)
    i = 0
    while i < len(perm):
        if perm[i] == i + 1:
            i += 1
        else:
            next = [abs(item) for item in perm].index(i+1)
            perm = perm[:i] + [-item for item in perm[i:next+1]][::-1] + perm[next+1:]
            result.append(perm)
    return result


for item in perm_sort(perm):
    print("(" + " ".join([(str(item) if item < 0 else "+"+str(item)) for item in item]) + ")")