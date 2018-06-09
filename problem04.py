# 문제4. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

s = s.replace('<html>', '')
s = s.replace("<body style='background-color:#ffff'>", '')
s = s.replace('<h4>Click</h4>', 'Click')
s = s.replace("<a href='http://www.python.org'>Here</a>", 'Here')
s = s.replace('<p>', '')
s = s.replace('</p>', '')
s = s.replace('</body>', '')
s =s.replace('</html>', '')
print(s)