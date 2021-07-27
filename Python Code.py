from python_imagesearch.imagesearch import imagesearch as search
import pyautogui as auto
import time
import keyboard
import sys

auto.FAILSAFE = False


def onscreen(path, precision=0.8):
    return search(path, precision)[0] != -1


def search_to(path):
    pos = search(path)
    auto.moveTo(pos)
    # print(path + " found")
    return pos


def click_key(key, delay=.1):
    auto.keyDown(key)
    time.sleep(delay)
    auto.keyUp(key)


def click_left(delay=.1):
    auto.mouseDown()
    time.sleep(delay)
    auto.mouseUp()


def click_right(delay=.1):
    auto.mouseDown(button='right')
    time.sleep(delay)
    auto.mouseUp(button='right')


def click_to(path, delay=.1):
    if onscreen(path):
        auto.moveTo(search(path))
        click_left(delay)
    else:
        pass



def triple_click(path, delay=.1):
    if onscreen(path):
        auto.moveTo(search(path))
        click_left(delay)
        click_left(delay)
        click_left(delay)

def click_7(path, delay=.1):
    if onscreen(path):
        auto.moveTo(search(path))
        click_left(delay)
        click_left(delay)
        click_left(delay)
        click_left(delay)
        click_left(delay)
        click_left(delay)
        click_left(delay)


def click_star(path, delay=.1):
    if onscreen(path):
        pos = search(path)
        k1 = (pos[0])
        k1 -= 10
        k2 = (pos[1])
        auto.moveTo(k1, k2)
        click_left(delay)



def gwiazkda():
    if onscreen("./captures/gwiazdka.png"):
        click_star("./captures/gwiazdka.png")
    else:
        click_star("./captures/halfstar.png")
    click_to("./captures/entrace.png")
    while not onscreen("./captures/info.png") or onscreen("./captures/enginfo.png"):
        time.sleep(0.5)


    while not onscreen("./captures/tak.png") or onscreen("./captures/Yes.png"):
        click_to("./captures/info.png")
        click_to("./captures/enginfo.png")
        click_to("./captures/water.png")
        click_to("./captures/trash.png")
        click_to("./captures/feed.png")
        click_to("./captures/sponge.png")
        click_to("./captures/ball.png")
    click_to("./captures/tak.png")
    click_to("./captures/Yes.png")



def gwiazdkowanie():
    time.sleep(1)
    if onscreen("./captures/gwiazdka.png") or onscreen("./captures/halfstar.png"):
        gwiazkda()
    elif onscreen("./captures/next.png"):
        click_to("./captures/next.png")
        return gwiazdkowanie()
    else:
        return jd()




def jd():
    while onscreen("./captures/feed.png"):
        triple_click("./captures/feed.png")

    while onscreen("./captures/ball.png"):
        triple_click("./captures/ball.png")

    while onscreen("./captures/water.png"):
        click_to("./captures/water.png")

    while onscreen("./captures/trash.png"):
        click_to("./captures/trash.png")

    while onscreen("./captures/sponge.png"):
        triple_click("./captures/sponge.png")

    while onscreen("./captures/cash.png"):
        click_to("./captures/cash.png")

    while onscreen("./captures/Scash.png"):
        click_to("./captures/Scash.png")
    while onscreen("./captures/hammer.png"):
        click_to("./captures/hammer.png")
    return gwiazdkowanie()


print("""My Free Zoo Bot by rafafunt
https://www.youtube.com/channel/UCAyLSu6CTegWhJEUVwWS4fg
https://github.com/rafafunt""")

while not onscreen("./captures/plus.png"):
    pass
click_7("./captures/plus.png")
triple_click("./captures/minus.png")


while True:
    gwiazdkowanie()
    jd()
    if keyboard.read_key() == "x":
        sys.exit(2)


#Author: rafafunt
