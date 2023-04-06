import random
import time
import curses


def main(stdscr):
    # ターミナルの色設定
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)

    # ターミナルのウィンドウ設定
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)

    # 文字列を生成
    matrix_code = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-=_+[]{}|;':\",./<>?`~"
    matrix_code += ' ' * len(matrix_code) * 5

    # 行毎にランダムな文字と開始位置を設定
    lines = []
    for _ in range(0, 100):
        line = [random.choice(matrix_code) for _ in range(sh)]
        lines.append(line)

    # 文字の流れを制御
    while True:
        for i in range(len(lines)):
            line = lines[i]
            for y, char in enumerate(line):
                if y == 0:
                    new_char = random.choice(matrix_code)
                    line[y] = new_char
                else:
                    line[y] = random.choice(matrix_code)

            # 文字を画面に描画
            for y, char in enumerate(line):
                x = i * 2
                if x < sw and y < sh:
                    w.addch(y, x, char, curses.color_pair(1))

        # 画面を更新
        w.refresh()

        # アニメーションの速度を制御
        time.sleep(0.05)


if __name__ == "__main__":
    curses.wrapper(main)
