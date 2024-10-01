import sympy as sp


def SampleExercises():
    n = sp.symbols("n")
    f1 = sp.Pow(10, n)
    f2 = sp.Pow(n, 1 / 3)
    f3 = sp.Pow(n, n)
    f4 = sp.log(n, 2)
    f5 = sp.Pow(2, sp.sqrt(f4))

    print(f4, f5)

    lim = sp.limit(f5 / f4, n, sp.oo)
    print("Limit f5/f4 =", lim)

    if lim == sp.oo:
        print("Order of gorth: f5 > f4")
    elif lim == 0:
        print("Order of gorth: f5 < f4")
    elif lim > 0:
        print("Order of gorth: f5 = f4")

    functions = [f1, f2, f3, f4, f5]
    for i in range(len(functions)):
        for j in range(i + 1, len(functions)):
            if sp.limit(functions[i] / functions[j], n, sp.oo) > 0:
                functions[i], functions[j] = functions[j], functions[i]

    print(functions)


def Ex01():
    def Ex01A(array):
        print("Basic operation (BO) is the compare:")
        print("=> Has (n - 1)! compare/BOs")
        print("C(n) = (n - 1)!")

        for i in range(0, len(array) - 1):
            for j in range(i + 1, len(array)):
                if array[i] == array[j]:
                    return False
        return True

    def Ex01B(array):
        print("Basic operation (BO) is the compare:")
        print("=> Has (n - 1)! compare/BOs")
        print("C(n) = (n - 1)!")

        n = len(array)
        for i in range(0, n - 1):
            max = array[i]
            imax = i
            for j in range(i + 1, n):
                if array[j] > max:
                    max = array[j]
                    imax = j
            array[i], array[imax] = array[imax], array[i]
        return array

    def Ex01C(n):
        count = 0
        i = n
        print("Basic operation (BO) is the assignment :")
        print("=> Has (log3(n) + 1) * n  assignment/BOs")
        print("C(n) = (log3(n) + 1) * n")

        while i >= 1:
            for j in range(1, n + 1):
                count += 1
                print(j)
            i = i / 3
        return count

    print(Ex01A([3, 6, 8, 7, 4, 9, 4, 3, 3, 1, 3, 1, 5, 6, 2, 7, 8, 6, 3, 9]))
    print(Ex01B([2, 3, 3, 3, 8, 3, 5, 1, 1, 2, 10, 7, 10, 3, 2, 5, 9, 4, 3, 4]))

    print(Ex01C(40))


def Ex02():
    n = sp.symbols("n")
    f = 32 * n**2 + 17 * n + 32

    lim_a = sp.limit(f, n, sp.oo)

    if lim_a == 0:
        print("32*n**2 + 17*n + 32 ∈ O(n)")
    else:
        print("32*n**2 + 17*n + 32 ∉ O(n)")

    if lim_a == 0:
        print("32*n**2 + 17*n + 32 ∈ O(n**3)")
    else:
        print("32*n**2 + 17*n + 32 ∉ O(n**3)")

    if lim_a == 0:
        print("32*n**2 + 17*n + 32 ∈ Omega(n**3)")
    else:
        print("32*n**2 + 17*n + 32 ∉ Omega(n**3)")

    if lim_a == 0:
        print("32*n**2 + 17*n + 32 ∈ Omega(n)")
    else:
        print("32*n**2 + 17*n + 32 ∉ Omega(n)")

    f2 = sp.Pow(2, n + 1)
    lim_f2 = sp.limit(f2, n, sp.oo)

    if lim_f2 == 0:
        print("2**(n+1) ∈ O(2**n)")
    else:
        print("2**(n+1) ∉ O(2**n)")

    f3 = sp.Pow(2, n) + 3 * n
    lim_f3 = sp.limit(f3, n, sp.oo)
    if lim_f3 == 0:
        print("2**n + 3*n ∈ O(2**n)")
    else:
        print("2**n + 3*n ∉ O(2**n)")


def Ex03():
    # Ex03A
    n = sp.symbols("n")
    f = sp.log(n, 2)
    g = sp.log(n, 2)

    lim = sp.limit(f / g, n, sp.oo)
    if lim == 0:
        print("log_2(f(n)) ∈ O(log_2(g(n))")
    else:
        print("log_2(f(n)) ∉ O(log_2(g(n))")

    # Ex03B
    f = sp.Pow(n, 2)
    g = sp.Pow(2, n)

    lim = sp.limit(f / g, n, sp.oo)

    if lim == 0:
        print("2^f(n) ∈ O(2^g(n))")
    else:
        print("2^f(n) ∉ O(2^g(n))")

    # Ex03C
    f = sp.Pow(n, 2)
    g = sp.Pow(n, 2)

    lim = sp.limit(f / g, n, sp.oo)
    if lim == 0:
        print("f(n)^2 ∈ O(g(n)^2)")
    else:
        print("f(n)^2 ∉ O(g(n)^2)")


def Ex04():
    n = sp.symbols("n")

    f1 = sp.Pow(n, 2.5)
    f2 = sp.sqrt(2 * n)
    f3 = n + 10
    f4 = sp.Pow(10, n)
    f5 = sp.Pow(100, n)
    f6 = sp.Pow(n, 2) * sp.log(n, 2)

    functions = [f1, f2, f3, f4, f5, f6]

    for i in range(len(functions)):
        for j in range(i + 1, len(functions)):
            if sp.limit(functions[i] / functions[j], n, sp.oo) > 0:
                functions[i], functions[j] = functions[j], functions[i]

    print(functions)


def Ex05():
    n = sp.symbols("n")

    g1 = sp.Pow(2, sp.log(n, 2))
    g2 = sp.Pow(2, n)
    g3 = sp.Pow(n, 4 / 3)
    g4 = n * sp.Pow(sp.log(n, 2), 3)
    g5 = sp.Pow(n, sp.log(n, 2))
    g6 = sp.Pow(2, sp.Pow(2, n))
    g7 = sp.Pow(2, sp.Pow(n, 2))

    functions = [g1, g2, g3, g4, g5, g6, g7]

    for i in range(len(functions)):
        for j in range(i + 1, len(functions)):
            if sp.limit(functions[i] / functions[j], n, sp.oo) > 0:
                functions[i], functions[j] = functions[j], functions[i]

    print(functions)


def main():
    print("Sample Exercises")
    SampleExercises()
    print("\nEx01")
    Ex01()
    print("\nEx02")
    Ex02()
    print("\nEx03")
    Ex03()
    print("\nEx04")
    Ex04()
    print("\nEx05")
    Ex05()


if __name__ == "__main__":
    main()
