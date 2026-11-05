"""Write an original Word template (.dotx) for the #3433 screenshots.

Usage: python3 -I make_template.py out.dotx
Hand-written from ECMA-376 Part 1; the text and colours are our own.
"""
import sys
import zipfile

W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"


def para(text, size=22, color="333333", bold=False, after=120):
    b = "<w:b/>" if bold else ""
    return (
        f'<w:p><w:pPr><w:spacing w:after="{after}"/></w:pPr><w:r><w:rPr>{b}<w:color w:val="{color}"/><w:sz w:val="{size}"/></w:rPr>'
        f'<w:t xml:space="preserve">{text}</w:t></w:r></w:p>'
    )


body = (
    para("Harbour Lane Studio", 44, "1F4E79", True, 0)
    + para("12 Harbour Lane · Portside · hello@harbourlane.example", 18, "7F7F7F", False, 360)
    + para("[Date]")
    + para("[Recipient name]", after=0)
    + para("[Address]", after=360)
    + para("Dear [Name],")
    + para("[Write your letter here.]", after=360)
    + para("Kind regards,", after=0)
    + para("[Your name]")
    + '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="708" w:footer="708" w:gutter="0"/></w:sectPr>'
)
doc = f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<w:document xmlns:w="{W}"><w:body>{body}</w:body></w:document>'
ct = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    '<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml"/>'
    "</Types>"
)
rels = (
    '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
    '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>'
    "</Relationships>"
)
with zipfile.ZipFile(sys.argv[1], "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", ct)
    z.writestr("_rels/.rels", rels)
    z.writestr("word/document.xml", doc)
