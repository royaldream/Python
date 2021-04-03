from PIL import Image, ImageFont, ImageDraw, ImageEnhance


def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(' ')
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word, 
            # add the line to the lines array
            lines.append(line)
    return lines


source_img = Image.open("./main/download.png").convert("RGBA")
draw = ImageDraw.Draw(source_img)
width, height = source_img.size

font = ImageFont.truetype("arialbd.ttf", 20)

text_qno = "QUESTION 2/20"
text_o1 = ["Amazon", "Facebook", "Google", "Bing"]
text_q = "The Competition Commission of the European Union(EU) has recently imposed a fine of about Rs 11,760 crore " \
         "on which company?"
text_o = []
text_qnu = "Q.2"
ans = '1'
h, w = 0, 0

for i in range(4):
    if font.getsize(text_o1[i])[0] > w:
        w = font.getsize(text_o1[i])[0]
for i in range(4):
    if font.getsize(text_o1[i])[1] > h:
        h = font.getsize(text_o1[i])[1]

button_size_1 = (w + 200, h + 20)

button_img_1 = Image.open('./main/a.png').convert("RGBA")
button_img_1.thumbnail(button_size_1)
button_img_2 = Image.open('./main/b.png').convert("RGBA")
button_img_2.thumbnail(button_size_1)
button_img_3 = Image.open('./main/c.png').convert("RGBA")
button_img_3.thumbnail(button_size_1)
button_img_4 = Image.open('./main/d.png').convert("RGBA")
button_img_4.thumbnail(button_size_1)

draw.text((width / 2 - 50, 20), text_qno, fill='rgb(255,165,0)', font=font)
(x, y) = 70, 50
draw.text((x - 40, y), text_qnu, fill='rgb(255,255,255)', font=font)
line_height = font.getsize('hg')[1]
lines = text_wrap(text_q, font, width - 80)
for line in lines:
    draw.text((x, y), line, fill='rgb(255,255,255)', font=font)
    y = y + line_height
source_img.save("./images/1.png", "PNG")

button_draw_1 = ImageDraw.Draw(button_img_1)
button_draw_1.text((50, 10), text_o1[0], font=font)
button_draw_2 = ImageDraw.Draw(button_img_2)
button_draw_2.text((50, 10), text_o1[1], font=font)
button_draw_3 = ImageDraw.Draw(button_img_3)
button_draw_3.text((50, 10), text_o1[2], font=font)
button_draw_4 = ImageDraw.Draw(button_img_4)
button_draw_4.text((50, 10), text_o1[3], font=font)
ans_1 = (x + 10, y + line_height)
ans_2 = (int(width / 2 + x + 10), y + line_height)
ans_3 = (x + 10, y + h + 100)
ans_4 = (int(width / 2 + x + 10), y + h + 100)
source_img.paste(button_img_1, ans_1)
source_img.save("./images/2.png", "PNG")
source_img.paste(button_img_2, ans_2)
source_img.save("./images/3.png", "PNG")
source_img.paste(button_img_3, ans_3)
source_img.save("./images/4.png", "PNG")
source_img.paste(button_img_4, ans_4)
source_img.save("./images/5.png", "PNG")
for i in range(6):
    timer_img = Image.open("./main/" + str(i) + 's.png').convert("RGBA")
    timer_img.thumbnail((50, 50))
    source_img.paste(timer_img, (int(width / 2), y + h + 200))
    source_img.save("./images/" + str(i + 6) + ".png", "PNG")
tick = Image.open('./main/tick.png').convert("RGBA")
tick.thumbnail((50, 50))

if ans == str(1):
    righta = Image.open('./main/righta.png').convert("RGBA")
    righta.thumbnail(button_size_1)
    right = ImageDraw.Draw(righta)
    right.text((50, 10), text_o1[0], font=font)
    source_img.paste(righta, ans_1)
    source_img.paste(tick, (x + 190, y + line_height + 10))
if ans == str(2):
    rightb = Image.open('./main/rightb.png').convert("RGBA")
    rightb.thumbnail(button_size_1)
    right = ImageDraw.Draw(rightb)
    right.text((50, 10), text_o1[0], font=font)
    source_img.paste(rightb, ans_2)
    source_img.paste(tick, (int(width / 2 + x + 10), y + line_height + 10))
if ans == str(3):
    rightc = Image.open('./main/rightc.png').convert("RGBA")
    rightc.thumbnail(button_size_1)
    right = ImageDraw.Draw(rightc)
    right.text((50, 10), text_o1[0], font=font)
    source_img.paste(rightc, ans_3)
    source_img.paste(tick, (x + 190, y + line_height + 10))
if ans == str(4):
    rightd = Image.open('./main/rightd.png').convert("RGBA")
    rightd.thumbnail(button_size_1)
    right = ImageDraw.Draw(rightd)
    right.text((50, 10), text_o1[0], font=font)
    source_img.paste(rightd, ans_4)
    source_img.paste(tick, (int(width / 2 + x + 10), y + h + 110))

timer_end_img = Image.open('./main/timeisup.png').convert("RGBA")
timer_img.thumbnail((50, 50))
source_img.paste(timer_end_img, (int(width / 2 - 100), y + h + 200))
source_img.save("./images/12.png", "PNG")
source_img.save("./images/13.png", "PNG")
source_img.save("./images/14.png", "PNG")
