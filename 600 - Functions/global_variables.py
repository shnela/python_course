var = 'global value'


def fun_with_local_var():
    var = 'local value'
    print(var)


def fun_with_global_var():
    # global var
    print(var)
    # var = 'local value'


if __name__ == '__main__':
    fun_with_global_var()

    fun_with_local_var()
