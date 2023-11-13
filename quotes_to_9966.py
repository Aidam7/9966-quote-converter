import re

def count_quotes(text):
    return len(re.findall(r'"[^"]*"', text))

def replace_quotes(text):
    quote_count = count_quotes(text)
    if(quote_count > 3):
        # Too many quotes
        return None
    # Replace quotes based on quote count
    if quote_count == 1:
        return re.sub(r'^"(.*)"$', r'„\1“', text)
    elif quote_count == 2:
        return re.sub(r' "([^"]*?)" ', r' ‚\1‘ ', re.sub(r'^"(.*)"$', r'„\1“', text))
    elif quote_count == 3:
        return re.sub(r' "([^"]*?)" ', r' ‚\1‘ ', re.sub(r' "([^"]*?)" ', r' »\1« ', re.sub(r'^"(.*)"$', r'„\1“', text)))
    else:
        return text
print(replace_quotes('"Lorem ipsum "dolor sit amet, "consectetuer" adipiscing elit" a vamos"'))