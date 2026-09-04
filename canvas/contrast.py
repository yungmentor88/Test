def lin(c):
    c=c/255
    return c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
def L(h):
    h=h.lstrip('#'); r,g,b=(int(h[i:i+2],16) for i in (0,2,4))
    return 0.2126*lin(r)+0.7152*lin(g)+0.0722*lin(b)
def ratio(a,b):
    la,lb=L(a),L(b); hi,lo=max(la,lb),min(la,lb)
    return (hi+0.05)/(lo+0.05)
def rep(a,b,label=""):
    r=ratio(a,b)
    tag=lambda t: "PASS" if r>=t else "fail"
    print(f"{label:<42} {a} on {b}  {r:5.2f}:1   normal-AA(4.5) {tag(4.5):4}  large-AA(3.0) {tag(3.0):4}  UI(3.0) {tag(3.0)}")
if __name__=="__main__":
    import sys
    pass
