# The Square Root of 2

Three root finding algorithms to compute the square root of 2, the bisection method, the Babylonian method, and Newton's method.

## The Bisection Algorighm

The **bisection algorithm** is based on the Intermediate Value Theorem from calculus, 
```
If $f\in C([a,b])$, then every intermediate $y$-value $k$ between $f(a)$ and $f(b)$ is achieved: there exists a solution $x=c\in (a,b)$ of the equation $f(x)=k$.
```
and requires inputting the endpoints $a$ and $b$ of the compact interval $[a,b]$ over which $g(x)=x^2-2$, in this case, is continuous (automatic, since $g$ is a polynomial) and has opposite signs at $a$ and at $b$.  For this $g(x)$ the interval $[1,2]$ works because $g(1)=-1<0<2=g(2)$.  

## The Fixed Point Method

The **fixed point method** requires that $g([a,b])\subset [a,b]$ over and above $g$'s continuity on $[a,b]$. If also $\sup |g'|<1$ on $[a,b]$, then the fixed point $x=p$, satisfying $g(p)=p$, is unique.  Thus, in addition to $[a,b]$, we need $g\in C([a,b])$ satisfying $g([a,b])\subset [a,b]$, and ideally $\sup |g'|<1$.   

Since $\sqrt{2}$ is by definition a root of the quadratic polynomial $f(x) = x^2-2$, we'll work with the associated fixed point function $g(x) = x-f(x) = x-x^2+2$.  We're not interested in the roots of $g$, but in the **fixed point** of $g$, which satisfies $g(p) = p$ (and which is equivalent to $f(p)=0$).  To understand how this works, note that $g(0) = 2$, $g(2) = 0$, and $g$ is continuous, so by the IVT it must hit every $y$-value between $0$ and $2$, and this must happen somewhere in the interval $[0,2]$.  Since $0<\sqrt{2}<2$, $g$ will hit this value somewhere, and this is the fixed point.

Consider also the Banach Fixed-Point Theorem:  The vertex of the parabola $g$ is at the midpoint between the roots $-1$ and $2$, at $x = 0.5$.  Now, $g(0.5)=2.25$, and $g(2.25) = -8.125$, so $g$ maps the interval $[-1,2.25]$ into itself, $g : [-1,2.25]-->[-1,2.25]$.  Also, $g'(x) = 1-2x$, which is a decreasing function everywhere, so has no critical points, and must attain its max and min at the endpoints of $[-1,2]$, $g'(-1) = 3$, $g'(2.25) = -3.5$.  Therefore $g$ is not a contraction. We know $g$ has a fixed point, but the Banach Fixed-Point Theorem doesn't apply, so we don't know that the iteration will converge.  

A similar problem occurs with $g(x) = 2/x$ on $[1,2]$.

The solution is the to use the **Babylonian method**:  Let $g : [1,2] --> [\sqrt{2}, 3/2] \subset [1,2]$ be given by $g(x) = (x+2/x)/2$, on the interval $[1,2]$. Note that the fixed point of $g$ is $\sqrt{2}$, since $p=g(p)$ implies $p=(p+2/p)/2$, so that $2p=p+2/p$, whence $p=2/p$, or $p^2=2$. Moreover, $g'(x) = (1-2/x^2)/2$, and we can find its max and min on $[1,2]$ using Calc 1 optimization: $g''(x) = 2/x^3$, so $g'$ is increasing, and therefore has its max and min at the endpoints:  $g'(1) = -1/2$, $g'(2) = 1/4$.  Therefore $|g'(x)| \leq 1/2 < 1$.

This $g$ is a contraction, so we can apply the Banach Fixed Point Theorem to conclude it has a unique fixed point on $[1,2]$.  We can start the algorithm like this: $p_0$ any point in $[1,2]$, $p_{n+1}=g(p_n$)$
 with any guess $p\in [1,2]$, say $p_0=1$!

 (3) 