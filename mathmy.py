def sqrt(n):
    n *= 1 if n > 0 else -1
    root = 0
    if (n < 1):
        aprox = n
        while (aprox > 0.0):
            if ((root + aprox) * (root + aprox) < n):
                aprox *= 2
            else:
                if ((root + aprox) * (root + aprox) == root or root + aprox == root):
                    return (root + aprox)
                root += aprox / 2
                div_count = 0
                while((root + aprox) * (root + aprox) > n):
                    div_count += 1
                    aprox /= 2
                if (div_count == 1):
                    return (root + aprox)

    else:
        aprox = n/2
        while (aprox > 0.0):
            if ((root + aprox) * (root + aprox) > n):
                aprox /= 2
            else:
                if ((root + aprox) * (root + aprox) == root or root + aprox == root):
                    break
                root += aprox
                aprox = ((aprox * 2) - aprox) / 2
    return root
