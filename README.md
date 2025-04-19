<script type="text/javascript" id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
    </script>

# The Square Root of 2

Three root finding algorithms to compute the square root of 2, the bisection method, the Babylonian method, and Newton's method.

## The Bisection Algorighm

### The Mathematical Basis
The **bisection algorithm** is based on the Intermediate Value Theorem (IVT) from calculus, 

* **IVT:** If $f\in C([a,b])$, then every intermediate $y$-value $k$ between $f(a)$ and $f(b)$ is achieved: there exists a solution $x=c\in (a,b)$ of the equation $f(x)=k$.

To use this theorem, we must choose a function $f$ which is continuous on a compact interval $[a,b]$ containing $x=\sqrt{2}$, the solution to $f(x)=0$.  From the definition of $\sqrt{2}$ we know $(\sqrt{2})^2=2\ \Longleftrightarrow\ (\sqrt{2})^2-2=0$, which demonstrates that the polynomial $f(x)=x^2-2$ has $x=\sqrt{2}$ as such a solution. Lastly, we need $[a,b]$ with $f(a)<0<f(b)$ or $f(a)>0>f(b)$.  Clearly $[1,2]$ serves this purpose.  

### The Bisection Algorithm
* **Input:**  $f(x)=x^2-2$, $a=1$ and $b=2$.

    1. **Set error, tolerance, and counter:** $0<e=$ error size, $N=$ number of iterations, $n=0$ counter initial value.
    2. **Set initial values, and their midpoint bisector:** $a_1=a$, $b_1=b$ and $c_1=(a_1+b_1)/2$.
    3. **Test $c_1$** to make sure we haven't accidentally hit upon the solution.
        + If $f(c_1)=0$, then $x=c_1$ is our solution. We are done. (Very unlikely, as $\sqrt{2}$ is irrational, but good to check generally).
        + If $|f(c_1)|<e$, we have satisfied our error tolerance, and $x=c_1$ is an approximate solution. We are done. 
        + If $n=N$, we stop without reaching a good enough approximation.
        + Else, set $n=n+1$ and proceed to the next step.  
    4. **Test for the sign of $f(c_1)$:** Neither $f(a_1)$, nor $f(b_1)$ nor $f(c_1)$ equal $0$. 
        + If $f(c_1)f(a_1)<0$, then the solution lies in $(a_1,c_1)$ by IVT.  Therefore set 
            * $a_2=a_1$, $b_2=c_1$, $c_2=\frac{a_2+b_2}{2}$.  (The solution lies in $[a_2,b_2]=[a_1,c_1]$, and now we will test its midpoint $c_2$)
            * Repeat steps 3 and 4 with $a_2$, $b_2$ and $c_2$ in place of $a_1$, $b_1$, $c_1$.
        + Else, the solution lies in $(c_1,b_1)$ by IVT.  Therefore set 
            * $a_2=c_1$, $b_2=b_1$, $c_2=\frac{a_2+b_2}{2}$.
            * Repeat steps 3 and 4 with $a_2$, $b_2$ and $c_2$ in place of $a_1$, $b_1$, $c_1$.
    5. etc.

## The Fixed Point Method

### The Mathematical Basis

The **fixed point method** requires $g\in C([a,b])$, as before, *and also* $g([a,b])\subseteq [a,b]$, because we are interested in finding a **fixed point** $p\in [a,b]$, satisfying $g(p)=p$.  The IVT can be use to show that such a $g$ has at least one fixed point:  If $g(a)=a$ or $g(b)=b$, we are done, we have a fixed point.  Otherwise, $a<g(a)$ and $g(b)<b$, in which case define $h(x)=g(x)-x$ and observe that $h(b)<0<h(a)$.  IVT says $\exists p\in (a,b)$ with $h(p)=0$.  But $h(p)=0$ means $g(p)=p$.  

If, *thirdly*, $\sup |g'|<1$ on $[a,b]$ (making $g$ what is called a **contraction**), then the Mean Value Theorem (MVT) implies uniqueness for the fixed point. (Exercise!)  The **Banach Fixed-Point Theorem** is the name of this proposition.  An algorithm is got by starting with any initial guess $p_0\in [a,b]$, and just *plugging back in*, $p_{n+1}=g(p_n)$.   The MVT shows convergence $p_n\to p$ to the unique fixed point of $g$.  

#### Test Case \#1

* ***Proposition*** $f\in C([a,b])$ has a root $f(p)=0$ in $[a,b]$ iff the associated function $g\in C([a,b])$ has a fixed point in $p$.

Since $\sqrt{2}$ is a root of the polynomial $f(x) = x^2-2$, we'll work with the associated fixed point function $g(x) = x-f(x) = x-x^2+2$.  Note that $g(0) = 2$, $g(2) = 0$, and $g$ is continuous, so by the IVT it must hit every $y$-value between $0$ and $2$, and this must happen somewhere in the interval $[0,2]$.  Since $0<\sqrt{2}<2$, $g$ will hit this value somewhere, and this is the fixed point of $g$ associated to the root of $f$. 

The vertex of the parabola $g(x)$ is at the midpoint between the roots $x=-1$ and $x=2$, at $x = 0.5$.  Now, $g(0.5)=2.25$, and $g(2.25) = -8.125$, so $g$ maps the interval $[-1,2.25]$ into itself, $g([-1,2.25])\subseteq [-1,2.25]$.  Also, $g'(x) = 1-2x$, which is a decreasing function everywhere, so has no critical points, and must attain its max and min at the endpoints of $[-1,2]$, $g'(-1) = 3$, $g'(2.25) = -3.5$.  Therefore $g$ is *not a contraction*. We know $g$ has a fixed point, but the Banach Fixed-Point Theorem doesn't apply, so we don't know that the iteration below will converge.  

#### Test Case \#2

A similar problem occurs with $g(x) = 2/x$ on $[1,2]$. (Exercise!)

#### Test Case \#3: the Babylonian Method

The solution is the to use the **Babylonian method**:  Let $g\in C([1,2])$ be given by $g(x) = (x+2/x)/2$, which satisfies $g([1,2])=[\sqrt{2}, 3/2] \subseteq [1,2]$, so $g$ has a fixed point. Moreover, the fixed is $\sqrt{2}$ since $p=g(p)$ means $p=(p+2/p)/2$, which simplifies to $p^2=2$. Note also that $g'(x) = (1-2/x^2)/2$, and we can find its max and min on $[1,2]$ using calculus optimization: $g''(x) = 2/x^3$, so $g'$ is increasing, and therefore has its max and min at the endpoints:  $g'(1) = -1/2$, $g'(2) = 1/4$.  Therefore $|g'(x)| \leq 1/2 < 1$.  The Banach Fixed Point Theorem can accordingly be applied to get a *unique* fixed point.

### The Fixed Point Algorithm

* **Input:**  $f(x)=x^2-2$, $a=1$ and $b=2$.

    1. **Set error, tolerance, and counter:** $0<e=$ error size, $N=$ number of iterations, $n=0$ counter initial value.
    2. **Choose initial estimate:** Choose $p_0\in [1,2]$.
    3. **Recursion (Babylonian method):** Let $p_1=g(p_0)=(p_0+2/p_0)/2$
        + If $|p_2-p_1|<e$, stop.  We have a good enough approximation in $p_2$.  ∏
        + If $n=N$, we stop without reaching a good enough approximation.
        + Else, set $n=n+1$ and repeat this step.  

## Newton's Method

### The Mathematical Basis

Suppose we know that $f\in C^2[a,b]$ has a root $p\in [a,b]$ (for example by observing $f(a)f(b)<0$ and applying IVT). Take an initial guess $p_0\approx p$ in $[a,b]$, and expand $f$ into a quadratic Taylor polynomial 
$$
0=f(p)=f(p_0)+f'(p_0)(p-p_0)+\frac{(p-p_0)^2}{2}f"(\xi(p))
$$