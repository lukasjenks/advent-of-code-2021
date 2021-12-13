CC=g++
CFLAGS=-g

all:	day7

day6:	day6.cpp
	$(CC) $(CFLAGS) -o $@ $^

test: clean day6
	./day6

clean:
	rm -f day6
