import bs4
from bs4.element import Comment
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def split_records(stream):
    payload = ''
    for line in stream:
        if line.strip() == "WARC/1.0":
            yield payload
            payload = ''
        else:
            payload += line
with open("data\\0000tw-00.warc.565132",errors='ignore') as f:
    for record in split_records(f):
        print('-----------------------------------------------')
        #print(record)
        soap=bs4.BeautifulSoup(record)
        texts = soap.findAll(text=True)
        visible_texts = filter(tag_visible, texts)
        #print(u" ".join(t.strip() for t in visible_texts))
        #print(soap.get_text())