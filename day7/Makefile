CC=g++
CFLAGS=-g

all:	day7

day7:	day7.cpp
	$(CC) $(CFLAGS) -o $@ $^

test: clean day7
	./day7

clean:
	rm -f day7
