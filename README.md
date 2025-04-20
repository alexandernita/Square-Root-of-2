# The Square Root of 2

Three root finding algorithms to compute the square root of 2, the bisection method, the Babylonian method, and Newton's method.

## The Bisection Algorighm

### The Mathematical Basis
The **bisection algorithm** is based on the Intermediate Value Theorem (IVT) from calculus, 

* **IVT:** If $f\in C([a,b])$, then every intermediate $y$-value $k$ between $f(a)$ and $f(b)$ is achieved: there exists a solution $x=c\in (a,b)$ of the equation $f(x)=k$.

To use this theorem, we must choose a function $f$ which is continuous on a compact interval $[a,b]$ containing $x=\sqrt{2}$, the solution to $f(x)=0$.  From the definition of $\sqrt{2}$ we know 

$(\sqrt{2})^2=2\ \Longleftrightarrow\ (\sqrt{2})^2-2=0$ 

which demonstrates that the polynomial 

$f(x)=x^2-2$ 

has $x=\sqrt{2}$ as such a solution. Lastly, we need $[a,b]$ with $f(a)<0<f(b)$ or $f(a)>0>f(b)$.  Clearly $[1,2]$ serves this purpose.  

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

The **fixed point method** requires $g\in C([a,b])$, as before, *and also* $g([a,b])\subseteq [a,b]$, because we are interested in finding a **fixed point** $p\in [a,b]$, satisfying $g(p)=p$.  The IVT can be use to show that such a $g$ has at least one fixed point:  If $g(a)=a$ or $g(b)=b$, we are done, we have a fixed point.  Otherwise, $a<g(a)$ and $g(b)<b$, in which case define 

$h(x)=g(x)-x$ 

and observe that $h(b)<0<h(a)$.  IVT says $\exists p\in (a,b)$ with $h(p)=0$.  But $h(p)=0$ means $g(p)=p$.  

If, *thirdly*, $\sup |g'|<1$ on $[a,b]$ (making $g$ what is called a **contraction**), then the Mean Value Theorem (MVT) implies uniqueness for the fixed point. (Exercise!)  The **Banach Fixed-Point Theorem** is the name given to this proposition.  An algorithm is got by starting with any initial guess $p_0$ and then *plugging* $p_n$ *back into* $g$ to get $p_{n+1}$,

$p_0\in [a,b]$\
$p_{n+1}=g(p_n)$

The MVT guarantees convergence $p_n\to p$ to the unique fixed point of $g$.  The algorithm is the essence of simplicity, but depends heavily on the choice of contraction $g$.  If $g$ is not a contraction, the sequence $(p_n)_{n\in \mathbb{N}}$ may not converge.

### Choosing the best $g$ for $\sqrt{2}$

#### Choice \#1

The following simple observation may be of potential help.

* ***Proposition*** $f\in C([a,b])$ has a root $f(p)=0$ in $[a,b]$ iff the associated function $g\in C([a,b])$ given by $g(x)=x-f(x)$ has a fixed point at $p$.

Now, $\sqrt{2}$ is a root of the polynomial $f(x) = x^2-2$, so our first choice of $g$ will be $f$'s associated fixed point function $g(x) = x-f(x) = x-x^2+2$.  Note that $g\in C([0,2])$ and an easy calculation shows that $g([0,2])\subseteq [0,2]$.  Since $0<\sqrt{2}<2$, $g$ will hit this value by IVT, and this is the fixed point of $g$ associated to the root of $f$. But $g$ is *not a contraction* (in fact $\sup |g'|=3.5$ on $[0,2]$).  

#### Choice \#2

A similar problem occurs with $g(x) = 2/x$ on $[1,2]$. (Exercise!)

#### Choice \#3: the Babylonian Method

The solution the **Babylonian method**, which uses $g\in C([1,2])$ given by $g(x) = (x+2/x)/2$: this function satisfies $g([1,2])=[\sqrt{2}, 3/2] \subseteq [1,2]$, showing that it has a fixed point, and this fixed point is $\sqrt{2}$ since $p=g(p)$ means $p=(p+2/p)/2$, which simplifies to $p^2=2$. Moreover, $g$ is a contraction satisfying $|g'(x)| \leq 1/2 < 1$ Banach Fixed Point Theorem can also be used.  

### The Fixed Point Algorithm

* **Input:**  $\displaystyle g(x)=\frac{1}{2}\Bigl(x+\frac{2}{x}\Bigr)$, $a=1$ and $b=2$.

    1. **Set error, tolerance, and counter:** $0<e=$ error size, $N=$ number of iterations, $n=0$ counter initial value.
    2. **Choose initial estimate:** Choose $p_0\in [1,2]$.
    3. **Recursion (Babylonian method):** Let $\displaystyle p_1=g(p_0)=\frac{1}{2}\Bigl(p_0+\frac{2}{p_0}\Bigr)$
        + If $|p_2-p_1|<e$, stop.  We have a good enough approximation in $p_2$. 
        + If $n=N$, we stop without reaching a good enough approximation.
        + Else, set $n=n+1$ and repeat this step, iii.  

## Newton's Method

### The Mathematical Basis

Suppose we know that $f\in C^2[a,b]$ has a root $p\in [a,b]$ (for example by observing $f(a)f(b)<0$ and applying IVT). Take an initial guess $p_0\approx p$ in $[a,b]$, and expand $f$ into a linear Taylor polynomial about $x=p_0$,

$\displaystyle 0=f(p)\approx f(p_0)+f'(p_0)(p-p_0)
\ \implies\ p\approx p_0-\frac{f(p_0)}{f'(p_0)}$

Needless to say, we must require $f'(p)\neq 0$, since then $f'(x)\neq 0$ in a small neighborhood $\overline{V_\delta(p)}=[p-\delta,p+\delta]$ of $p$ (because $f'\in C^1([a,b])$).  The function 

$g(x)=x-f(x)/f'(x)$

is then continuous on $\overline{V_\delta(p)}$.  Its derivative

$g'(x)=\frac{f(x)f"(x)}{f'(x)^2}$

is continuous on $\overline{V_\delta(p)}$ and satisfies $g'(p)=0$.  Shrinking $\delta$ as needed, we can make sure that $\sup |g'|\leq k<1$ on $\overline{V_\delta(p)}$, and then use the Banach Fixed Point Theorem to guarantee convergence of the recursive sequence 

$p_0\in [a,b]$\
$p_{n+1}=g(p_n)$