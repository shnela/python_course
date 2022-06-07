var = 'global value'


def fun_with_local_vars():
    var = 'local value'
    print(var)


def fun_with_local_vars2():
    print(var)
    var = 'local value'


def fun_with_global_ro_var():
    print(var)


def fun_with_global_rw_var():
    global var
    var = 'global updated value'
    print(var)


if __name__ == '__main__':
    fun_with_local_vars()
    # fun_with_local_vars2()
    fun_with_global_ro_var()
    fun_with_global_rw_var()
