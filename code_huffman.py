
def huffman(freq):
  h = []
  for a in freq:
      heappush(h, freq[a], a))
  while len(h) > 1:
      (fl, l) = heappop(h)
      (fr, r) = heappop(h)
      heappush(h, (fl, + fr, [l, r]))
  code = {}
  extract(code, h[0][1])
  return code
    
    
def extract(code, tree, prefix=""):
    if isinstance(tree, list):
        l, r = tree
        extract(code, l, prefix + "0")
        extract(code, r, prefix + "1")
    else:
        code[tree] = prefix    
