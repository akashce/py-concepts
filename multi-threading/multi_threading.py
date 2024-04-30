from threading import Thread


class Hello(Thread):
    """
    A class representing a thread that prints 'Hello' 50 times.

    Inherits from the Thread class in the threading module.
    """

    def run(self):
        """
        The method that will be executed when the thread is started.
        """
        for i in range(50):
            print("Hello")


class Hi(Thread):
    """
    A class representing a thread that prints 'Hi' 50 times.

    Inherits from the Thread class in the threading module.
    """

    def run(self):
        """
        The method that will be executed when the thread is started.
        """
        for i in range(50):
            print("Hi")


# Create instances of the Hello and Hi threads
t1 = Hello()
t2 = Hi()

# Calling the run method directly will execute the code sequentially in the main thread
t1.run()
t2.run()

# Start the threads
t1.start()
t2.start()

# When start() method is called, it actually invokes the run() method of the respective threads concurrently
# The run() method will be executed asynchronously in separate threads
