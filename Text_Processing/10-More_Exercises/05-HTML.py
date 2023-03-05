title = input()
article = input()
comment = input()

result = f"<h1>" \
         f"\n    {title}" \
         f"\n</h1>" \
         f"\n<article>" \
         f"\n    {article}" \
         f"\n</article>"

while comment != "end of comments":
    result += f"\n<div>" \
              f"\n    {comment}" \
              f"\n</div>"

    comment = input()

print(result)
