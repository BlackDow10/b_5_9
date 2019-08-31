import time

def time_this(num_runs=10):
    def wrapp(func):
        def time_test():
            print("Старт теста")
            time_compare = 0
            for i in range(num_runs):
                t0 = time.time()
                func()
                t1 = time.time()
                time_compare += (t1 - t0)
            time_compare /= num_runs
            print("Конец теста.")
            print("время меняется, запустить несколько раз")
            print("Среднее время выполнения %sсекунд" %(time_compare))
        return time_test
    return wrapp


@time_this(10)
def fobina():
	def sub(n1 = 0, n2 = 1):
		sum = n1 + n2
		if sum < 40000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
			sub(n2, sum)
		else: print(sum)
		return n2
	return sub()


fobina()
print("end")