with open('/Users/valery/ige_1/24_7600.txt', 'r') as f:
    text = f.readline()

# QRS
text = text.replace('QQ', '*').replace('QR', '*').replace('QS', '*').replace('RQ','*').replace('RR', '*').replace('RS', '*') \
        .replace('SQ', '*').replace('SR','*').replace('SS', '*')

print(len(max(text.split('*'), key=len)))