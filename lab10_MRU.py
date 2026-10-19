pages = [1, 2, 3, 4, 1, 2, 3, 1]

frame_size = 3
recent = []
frames = []
page_fault = 0
page_hit = 0

for page in pages:

    if page in frames:
        page_hit += 1
        recent.remove(page)
        recent.append(page)

    else :
        page_fault += 1

        if len(frames)<frame_size:
            frames.append(page)

        else :
            old = recent[-1]
            frames.remove(old)
            recent.remove(old)
            frames.append(page)

        recent.append(page)

    print(page, "=>", frames)

print ("page fault =", page_fault)
print("page hit = ", page_hit)

hit_ratio =  page_hit / len(pages)
print ("page hit ratio = ", hit_ratio)