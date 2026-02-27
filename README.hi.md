<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.md">English</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/ally-demo-python/readme.png" alt="Ally Demo Python" width="400">
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/ally-demo-python/actions/workflows/ci.yml"><img src="https://github.com/mcp-tool-shop-org/ally-demo-python/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://codecov.io/gh/mcp-tool-shop-org/ally-demo-python"><img src="https://codecov.io/gh/mcp-tool-shop-org/ally-demo-python/branch/main/graph/badge.svg" alt="codecov"></a>
  <a href="https://pypi.org/project/ally-demo-python/"><img src="https://img.shields.io/pypi/v/ally-demo-python" alt="PyPI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License"></a>
  <a href="https://mcp-tool-shop-org.github.io/ally-demo-python/"><img src="https://img.shields.io/badge/Landing_Page-live-blue" alt="Landing Page"></a>
</p>

एक न्यूनतम पायथन कमांड-लाइन इंटरफेस (CLI) जो `cli.error.v0.1` (सत्य मान) उत्पन्न करता है और संपूर्ण एली पाइपलाइन को प्रदर्शित करता है:

- `a11y-assist` (प्रोफाइल: कम दृष्टि, संज्ञानात्मक भार, स्क्रीन रीडर, डिस्लेक्सिया, सरल भाषा)
- `a11y-lint` (सत्यापित करें + स्कैन करें)
- `a11y-ci` (गेट)

यह रिपॉजिटरी जानबूझकर छोटा और साधारण है। यह एक संदर्भ एकीकरण है।

## शुरुआत कैसे करें

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -e .
pip install a11y-assist a11y-lint
```

एक ऐसा कमांड चलाएं जो संरचित JSON उत्पन्न करता है:

```bash
demo-cli network-timeout --json-out /tmp/cli_error.json || true
```

विभिन्न प्रोफाइल का उपयोग करके समान त्रुटि को समझाएं:

```bash
a11y-assist explain --json /tmp/cli_error.json --profile lowvision
a11y-assist explain --json /tmp/cli_error.json --profile cognitive-load
a11y-assist explain --json /tmp/cli_error.json --profile screen-reader
a11y-assist explain --json /tmp/cli_error.json --profile dyslexia
a11y-assist explain --json /tmp/cli_error.json --profile plain-language
```

संदेश अनुबंध को मान्य करें:

```bash
a11y-lint validate /tmp/cli_error.json
```

## उपलब्ध त्रुटि परिदृश्य

इस डेमो CLI में कई त्रुटि परिदृश्य शामिल हैं जो विभिन्न पैटर्न को प्रदर्शित करते हैं:

| कमांड | त्रुटि आईडी | विवरण |
|---------|----------|-------------|
| `demo-cli network-timeout` | DEMO.NETWORK.TIMEOUT | HTTP अनुरोध समय समाप्त |
| `demo-cli config-missing` | DEMO.CONFIG.MISSING | कॉन्फ़िगरेशन फ़ाइल गायब है |
| `demo-cli auth-failed` | DEMO.AUTH.INVALID_TOKEN | प्रमाणीकरण विफलता |
| `demo-cli permission-denied` | DEMO.FS.PERMISSION_DENIED | फ़ाइल अनुमति त्रुटि |
| `demo-cli validation-error` | DEMO.VALIDATION.SCHEMA | स्कीमा सत्यापन विफलता |

प्रत्येक कमांड:
- stdout पर मानव-पठनीय आउटपुट प्रिंट करता है
- निर्दिष्ट `--json-out` पथ पर JSON लिखता है
- मशीन द्वारा कैप्चर करने के लिए stderr पर JSON उत्सर्जित करता है

## "अच्छा" कैसा दिखता है

CLI एक अनुमानित संरचना में एक मानव-पठनीय संदेश प्रिंट करता है:

```
[ERROR] Title (ID: ...)

What:
  Description of what happened.

Why:
  Explanation of why it happened.

Fix:
  Steps to resolve the issue.
  Re-run: command --dry-run
```

CLI मशीन द्वारा कैप्चर करने के लिए मान्य `cli.error.v0.1` JSON भी उत्सर्जित करता है।

- `a11y-assist` कभी भी मूल आउटपुट को फिर से नहीं लिखता है; यह एक ASSIST ब्लॉक जोड़ता है।
- केवल SAFE कमांड सुझाए जाते हैं (और केवल तभी जब वे इनपुट में मौजूद हों)।

## डिज़ाइन नोट्स

यह डेमो जानबूझकर उत्सर्जित करता है:

- एक स्थिर `id` नेमस्पेस (DEMO.*)
- ऐसे लाइनें जो `--dry-run` (SAFE) युक्त एक `Re-run:` कमांड शामिल करती हैं

यह पूरे पाइपलाइन का एंड-टू-एंड परीक्षण करना आसान बनाता है।

## 10 मिनट में एली को अपनाएं (उपकरण लेखकों के लिए)

1. विफलता पर `cli.error.v0.1` JSON उत्सर्जित करें (मशीन आउटपुट)
2. समान सामग्री को एक अनुमानित पाठ संरचना में प्रिंट करें (मानव आउटपुट)
3. CI जोड़ें:
- `a11y-lint validate <message.json>`
- यदि आप पाठ आउटपुट का सत्यापन करते हैं तो स्कोरकार्ड के लिए `a11y-ci gate`
4. उपयोगकर्ताओं को बताएं:
- `a11y-assist explain --json <file>`
- या रैपर-फर्स्ट: `assist-run <command>` फिर `a11y-assist last`

## सुरक्षा और गोपनीयता

**डेटा जिस पर कार्रवाई की गई:** केवल प्रदर्शन त्रुटि परिदृश्य - वैकल्पिक `--json-out` फ़ाइल आउटपुट के अलावा कोई वास्तविक डेटा नहीं पढ़ा या लिखा जाता है।

**डेटा जिस पर कोई कार्रवाई नहीं की गई:** कोई उपयोगकर्ता क्रेडेंशियल नहीं, कोई सिस्टम फ़ाइलें नहीं, कोई नेटवर्क कॉल नहीं (सभी त्रुटियां सिमुलेटेड हैं)। कोई टेलीमेट्री एकत्र या भेजा नहीं जाता है।

**अनुमतियाँ:** केवल उपयोगकर्ता द्वारा निर्दिष्ट `--json-out` पथ के लिए फ़ाइल सिस्टम लिखने की अनुमति। पूर्ण नीति के लिए [SECURITY.md](SECURITY.md) देखें।

## लाइसेंस

MIT

---

द्वारा निर्मित <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
