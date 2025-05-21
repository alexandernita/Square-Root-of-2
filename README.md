# The Square Root of 2

We present three **root finding methods** and their resulting **algorithms**, 
1. The **bisection method**.
2. The **fixed-point method**.
3. **Newton's method**
then use them to compute the square root of 2.  The **Babylonian method** gives us a particular function $\displaystyle g(x)=\frac{1}{2}\Bigl(x+\frac{2}{x}\Bigr)$ which, applied to any seed $x\in [1,2]$, gives a sequence $(g^n(x))_{n\in\mathbf{N}}$ converging to a fixed point $x = p$ of $g$, satisfying, that is, $g(p)=p$, and therefore $p=\sqrt{2}$. 

We provide the mathematical derivation of each algorithm, and explain how to adapt it to a particular problem, in this case finding an approximate value for $\sqrt{2}$. 