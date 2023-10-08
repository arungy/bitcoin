#makefile
CPP = g++
CPPFLAGS = -I.
DEPS =
TARGET = hello_world print_date

all: $(TARGET)

%.o: %.cpp $(DEPS)
	$(CPP) -c -o $@ $< $(CPPFLAGS)

.PHONY: all clean

clean:
	rm -f $(TARGET) *.o *.out

hello_world: hello_world.o
	$(CPP) -o $@ $^ $(CPPFLAGS)

print_date: print_date.o
	$(CPP) -o $@ $^ $(CPPFLAGS)
