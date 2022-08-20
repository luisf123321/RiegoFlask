

class BodyEmail:

    @classmethod
    def bodyToRegister(cls):
        html = """\
            <html>
            <body>
                <p><b>Python Mail Test</b><br>
                This is HTML email with attachment.<br>
                Click on <a href="https://fedingo.com">Fedingo Resources</a> 
                for more python articles.
                </p>
            </body>
            </html>
            """
        return html
