import scrapy
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup


ALLOWED_DOMAIN = "tehisintellekt.ee"

DENY_PATTERNS = [
    ".pdf",
    ".jpg",
    ".png",
    ".jpeg",
]


class TehisintellektSpider(scrapy.Spider):
    name = "tehisintellekt"

    allowed_domains = [ALLOWED_DOMAIN]
    start_urls = ["https://tehisintellekt.ee/"]

    def parse(self, response):
        """
        1. Salvesta selle lehe sisu
        2. Leia lingid ja järgi neid
        """

        body_html = response.xpath("//body").get(default="")

        soup = BeautifulSoup(body_html, "html.parser")
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        text = soup.get_text(separator="\n")

        lines = [line.strip() for line in text.splitlines()]
        lines = [line for line in lines if line]
        cleaned_text = "\n".join(lines)

        yield {
            "url": response.url,
            "content": cleaned_text,
        }

        for href in response.css("a::attr(href)").getall():
            if not href:
                continue

            if href.startswith("#"):
                continue

            if href.startswith("mailto:") or href.startswith("tel:"):
                continue

            next_url = urljoin(response.url, href)
            parsed = urlparse(next_url)

            if parsed.scheme not in ("http", "https"):
                continue

            if not parsed.netloc.endswith(ALLOWED_DOMAIN):
                continue

            if any(patt in next_url for patt in DENY_PATTERNS):
                continue

            yield response.follow(next_url, callback=self.parse)
