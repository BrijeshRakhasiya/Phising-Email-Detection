import re
import json
from urllib.parse import urlparse
import tldextract
import requests


class DomainChecker:
    def __init__(self, config_path='config/trusted_entries.json'):
        self.trusted_domains = self._load_trusted_domains(config_path)
        self.trusted_shorteners = {'bit.ly', 'app.link'}  # Add more as needed
    
    def _load_trusted_domains(self, path):
        with open(path) as f:
            data = json.load(f)
        return set([domain.lower() for domain in data['trusted_domains']])
    
    def extract_domain(self, url):
        """Extract main domain using tldextract for accurate parsing"""
        try:
            extracted = tldextract.extract(url)
            if not extracted.domain or not extracted.suffix:
                return None
            return f"{extracted.domain}.{extracted.suffix}".lower()
        except:
            return None
    
    def contains_trusted_domain(self, text):
        """Check if text contains any trusted domains"""
        # Find all URLs in text
        urls = re.findall(r'https?://\S+', text)
        
        for url in urls:
            domain = self.extract_domain(url)
            if domain and domain in self.trusted_domains:
                return True
        return False
        
    def is_trusted_shortener(self, url):
        """Check if URL is from trusted shortening service"""
        domain = self.extract_domain(url)
        return domain in self.trusted_shorteners

    def resolve_short_url(self, url):
        """Resolve shortened URL to final destination"""
        try:
            session = requests.Session()
            resp = session.head(url, allow_redirects=True, timeout=2)
            return resp.url
        except:
            return url

    def analyze_url(self, url):
        """Full URL analysis pipeline"""
        resolved_url = self.resolve_short_url(url)
        final_domain = self.extract_domain(resolved_url)
        return {
            'original': url,
            'resolved': resolved_url,
            'final_domain': final_domain,
            'is_shortened': url != resolved_url,
            'trusted_shortener': self.is_trusted_shortener(url),
            'trusted_final_domain': final_domain in self.trusted_domains
        }

