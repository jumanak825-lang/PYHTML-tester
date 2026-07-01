import pyhtml as h
t=h.html(
    h.head(
        h.title('Test Page')
    ),
    h.body(
        h.h1('This is a title'),
        h.div('This is some text'),
        h.div(h.h2('inside title'),
         h.p('some text inside paragraph.'))
    )
)
print(t.render())