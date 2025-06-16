import numpy as np


def sortd(datas, labels):

    m = len(datas)
    # print(m)
    datasort = []
    labelsort = []
    mind = []
    labelmin = []
    labelk = 1
    i = 1
    while m >= i:

        mind = min(datas)
        minloc = datas.index(mind)
        lmin = labels[minloc]
        datas[minloc] = 10000

        # print(lmin)

        datasort.append(mind)
        labelsort.append(lmin)
        i = i + 1

    return datasort, labelsort


def cum_sum(d):
    c_sum = 0
    exe = []
    for i in range(len(d)):
        c_sum += d[i]
        exe.append(c_sum)
    return exe


def pres(c_s):
    val = sum(c_s)
    val_e = []
    for i in range(len(c_s)):
        val_e.append((100 * c_s[i]) / val)
    return val_e


def nearest(c, p, label):
    m = []
    for i in range(len(c)):
        m.append(abs(c[i] - p))
    min1 = min(m)
    parat = m.index(min1)

    return label[parat]


def parato(data, label):
    d, l = sortd(data, label)
    c_d = cum_sum(d)

    c_d_pre = pres(c_d)

    val_cum_pre = cum_sum(c_d_pre)

    parato = 80
    print("more likely choose according to parato analysis")

    print(nearest(val_cum_pre, parato, l))


label = ["janitha", "anurudha", "william", "anuja"]
score = [7, 5, 8, 4]
parato(score, label)
